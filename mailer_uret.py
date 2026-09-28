#!/usr/bin/env python3
"""Parametrik mailer kutu (roll end tuck front) dieline'ı üretir.

Pacdora'daki mailer açınımından ölçülerek yeniden çizildi. İç ölçüler verilir,
diğer her şey (kapak, kulaklar, dil, çift duvar, kilit dilleri) bunlardan türetilir.

    python3 mailer_uret.py 315 202 62                 → mailer_315x202x62.pdf
    python3 mailer_uret.py 315 202 62 -o kutu.pdf

Katmanlar: "Kesim" (kırmızı, düz) ve "Kat" (yeşil, kesikli). Dieline 3D bu adları tanır.
Bütün kat çizgileri kesime değer; kilit yarıkları tabanın içinde kapalı delik olarak durur.
"""
import argparse
import math
import fitz

MM = 72 / 25.4
PAD = 12          # mm sayfa kenar boşluğu

# ekran görüntüsünden ölçülen sabitler (mm) — 315×202×62 kutuda
FLAP = 80         # toz kapağı genişliği
SLIT = 3          # toz kapağı ile yan panel arasındaki yarık
SIDE_GAP = 2      # yan panelin taban kenarından içeride başlaması
STRIP = 5         # çift duvarın üst şeridi (duvar kalınlığı payı)
INNER_EXTRA = 2   # iç duvar dış duvardan bu kadar uzun (kilit dili tabana otursun)
TAB = 4.4         # kilit dili çıkıntısı
LID_INSET = 4.8   # kapak her yandan duvardan bu kadar dar (kulaklar içeri girsin)
LID_EXTRA = 2     # kapak derinliği = taban derinliği + bu
EAR = 60          # kapak kulağı genişliği
EAR_DIAG = (54.6, 20)   # kulak uçlarındaki eğik kesim (dx, dy)
TUCK_INSET = 2.2  # ön dil her yandan duvardan bu kadar dar
WING = 50         # ön dil kanadı genişliği


def rounded(p0, corners):
    """Köşe listesini yuvarlatılmış çokgene çevirir. corners: [(x, y, r)]"""
    out = [p0]
    for i, (x, y, r) in enumerate(corners):
        if r <= 0:
            out.append((x, y)); continue
        px, py = out[-1]
        nx, ny = corners[i + 1][:2]
        a = (px - x, py - y); b = (nx - x, ny - y)
        la, lb = math.hypot(*a), math.hypot(*b)
        a = (a[0] / la, a[1] / la); b = (b[0] / lb, b[1] / lb)
        s = (x + a[0] * r, y + a[1] * r); e = (x + b[0] * r, y + b[1] * r)
        for k in range(9):   # ikinci dereceden Bezier ile yay
            t = k / 8
            out.append(((1 - t) ** 2 * s[0] + 2 * (1 - t) * t * x + t * t * e[0],
                        (1 - t) ** 2 * s[1] + 2 * (1 - t) * t * y + t * t * e[1]))
    return out


def dieline(W, D, H):
    L = D + LID_EXTRA                 # kapak derinliği
    T = H                             # ön dil yüksekliği
    yL = -H - L                       # kapak / dil katı
    yT = yL - T                       # dilin üst kenarı
    xin = -(H + STRIP + H + INNER_EXTRA)   # iç duvarın dış kenarı
    t1, t2 = D * 0.196, D * 0.393     # kilit dilleri (taban derinliğine orantılı)
    t3, t4 = D * 0.589, D * 0.796

    # sol yarı: dilin sol üst köşesinden aşağı, ön duvarın ortasına kadar
    left = rounded((TUCK_INSET, yT), [
        (-WING + TUCK_INSET, yT, 25),              # kanat
        (-WING + TUCK_INSET, yL, 8),
        (TUCK_INSET, yL, 0),
    ]) + [
        (LID_INSET, yL),                            # kulak
        (LID_INSET - EAR_DIAG[0], yL + EAR_DIAG[1]),
        (LID_INSET - EAR, yL + EAR_DIAG[1] + 7),
        (LID_INSET - EAR, -H - EAR_DIAG[1] - 7),
        (LID_INSET - EAR_DIAG[0], -H - EAR_DIAG[1]),
        (LID_INSET, -H),
        (0, -H),                                    # arka toz kapağı
        (-FLAP, -H), (-FLAP, -SLIT), (0, -SLIT),
        (0, 0), (0, SIDE_GAP),
        (xin, SIDE_GAP),                            # yan panel + kilit dilleri
        (xin, t1), (xin - TAB, t1 + 2), (xin - TAB, t2 - 2), (xin, t2),
        (xin, t3), (xin - TAB, t3 + 2), (xin - TAB, t4 - 2), (xin, t4),
        (xin, D - SIDE_GAP),
        (0, D - SIDE_GAP), (0, D), (0, D + SLIT),   # ön toz kapağı
        (-FLAP, D + SLIT), (-FLAP, D + H), (0, D + H),
    ]
    right = [(W - x, y) for x, y in reversed(left)]
    outline = left + right

    creases = []
    for s in (1, -1):   # sol (s=1) ve ayna (s=-1)
        X = (lambda x: x) if s == 1 else (lambda x: W - x)
        creases += [
            ((X(TUCK_INSET), yT), (X(TUCK_INSET), yL)),          # dil kanadı
            ((X(LID_INSET), yL), (X(LID_INSET), -H)),            # kapak kulağı
            ((X(0), -H), (X(0), -SLIT)),                         # arka toz kapağı
            ((X(0), SIDE_GAP), (X(0), D - SIDE_GAP)),            # taban / dış duvar
            ((X(-H), SIDE_GAP), (X(-H), D - SIDE_GAP)),          # dış duvar / şerit
            ((X(-H - STRIP), SIDE_GAP), (X(-H - STRIP), D - SIDE_GAP)),  # şerit / iç duvar
            ((X(0), D + SLIT), (X(0), D + H)),                   # ön toz kapağı
        ]
    creases += [
        ((LID_INSET, yL), (W - LID_INSET, yL)),   # kapak / dil
        ((LID_INSET, -H), (W - LID_INSET, -H)),   # arka duvar / kapak
        ((0, 0), (W, 0)),                         # taban / arka duvar
        ((0, D), (W, D)),                         # taban / ön duvar
    ]

    # kilit yarıkları: tabanın içinde, kenara 0.8 mm mesafede kapalı delik (kilit dilleriyle aynı hizada)
    slots = []
    for x0 in (0.8, W - 0.8 - 4.5):
        for a, b in ((t1, t2), (t3, t4)):
            m = (a + b) / 2
            slots.append(rounded((x0, m), [(x0, a, 2), (x0 + 4.5, a, 2), (x0 + 4.5, b, 2), (x0, b, 2), (x0, m + 0.01, 0)]))

    xs = [p[0] for p in outline]; ys = [p[1] for p in outline]
    return outline, creases, slots, (min(xs), min(ys), max(xs), max(ys))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("en", type=float, help="iç uzunluk (mm)")
    ap.add_argument("derinlik", type=float, help="iç genişlik / taban derinliği (mm)")
    ap.add_argument("yukseklik", type=float, help="iç yükseklik (mm)")
    ap.add_argument("-o", "--cikti")
    a = ap.parse_args()
    W, D, H = a.en, a.derinlik, a.yukseklik
    outline, creases, slots, (x0, y0, x1, y1) = dieline(W, D, H)

    doc = fitz.open()
    page = doc.new_page(width=(x1 - x0 + 2 * PAD) * MM, height=(y1 - y0 + 2 * PAD + 10) * MM)
    P = lambda x, y: fitz.Point((x - x0 + PAD) * MM, (y - y0 + PAD) * MM)
    kes, kat, bilgi = doc.add_ocg("Kesim"), doc.add_ocg("Kat"), doc.add_ocg("Bilgi")
    page.draw_polyline([P(*p) for p in outline], color=(0.93, 0.11, 0.14), width=0.5, closePath=True, oc=kes)
    for s in slots:
        page.draw_polyline([P(*p) for p in s], color=(0.93, 0.11, 0.14), width=0.5, closePath=True, oc=kes)
    for p, q in creases:
        page.draw_line(P(*p), P(*q), color=(0, 0.65, 0.32), width=0.5, dashes="[3 2] 0", oc=kat)
    # bilgi yazısı açınımın dışında, sayfanın altında: 3D dokuya karışmasın
    page.insert_text(P(x0, y1 + 8), f"Mailer {W:g} x {D:g} x {H:g} mm (ic olcu)",
                     fontsize=10, color=(0.4, 0.4, 0.4), oc=bilgi)
    out = a.cikti or f"mailer_{W:g}x{D:g}x{H:g}.pdf"
    doc.save(out)
    print(f"yazıldı: {out}  ({x1 - x0:.1f} × {y1 - y0:.1f} mm açınım, {len(creases)} kat, {len(slots)} yarık)")


if __name__ == "__main__":
    main()
