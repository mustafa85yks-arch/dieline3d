#!/usr/bin/env python3
"""Test dieline PDF'leri üretir (PyMuPDF).

Katmanlar (PDF optional content): "Artwork" ve "Kesim".
Kesim konturu magenta tek kapalı path, kat izleri yeşil kesikli 2 düğümlü çizgi.

    python3 ornek_uret.py      → ornek_tuckend.pdf, ornek_piramit.pdf
"""
import math
import fitz

MM = 72 / 25.4
PAD = 15  # mm, sayfa kenar boşluğu


def P(x, y):
    return fitz.Point((x + PAD) * MM, (y + PAD) * MM)


def cizim(ad, w, h, kontur, katlar, boyalar, yazilar):
    doc = fitz.open()
    page = doc.new_page(width=(w + 2 * PAD) * MM, height=(h + 2 * PAD) * MM)
    art = doc.add_ocg("Artwork")
    kes = doc.add_ocg("Kesim")

    # artwork: paneller + 3 mm taşma
    for poly, renk in boyalar:
        page.draw_polyline([P(*p) for p in poly], color=None, fill=renk,
                           closePath=True, oc=art)
    for x, y, metin, boy, renk in yazilar:
        page.insert_text(P(x, y), metin, fontsize=boy, color=renk, oc=art)

    # kesim konturu
    page.draw_polyline([P(*p) for p in kontur], color=(0.93, 0.11, 0.14), width=0.5,
                       closePath=True, oc=kes)
    # kat izleri
    for a, b in katlar:
        page.draw_line(P(*a), P(*b), color=(0, 0.65, 0.32), width=0.5,
                       dashes="[3 2] 0", oc=kes)
    doc.save(ad)
    print("yazıldı:", ad)


def tuckend():
    # W=60 D=40 H=100 mm, straight tuck end
    kontur = [
        (15, 55), (75, 55),
        (77, 32), (108, 30), (113, 40), (115, 55),           # sağ yan toz kapağı
        (115, 15), (120, 0), (170, 0), (175, 15),            # üst kapak + dil
        (175, 55), (177, 40), (182, 30), (213, 32), (215, 55),  # sol yan toz kapağı
        (215, 155),
        (213, 178), (182, 180), (177, 170), (175, 155),      # alt toz kapağı
        (115, 155),
        (113, 170), (108, 180), (77, 178), (75, 155),        # alt toz kapağı
        (75, 195), (70, 210), (20, 210), (15, 195),          # alt kapak + dil
        (15, 155), (0, 150), (0, 60),                         # yapıştırma
    ]
    katlar = [
        ((15, 55), (15, 155)), ((75, 55), (75, 155)),
        ((115, 55), (115, 155)), ((175, 55), (175, 155)),
        ((75, 55), (115, 55)), ((115, 55), (175, 55)), ((175, 55), (215, 55)),
        ((15, 155), (75, 155)), ((75, 155), (115, 155)), ((175, 155), (215, 155)),
        ((115, 15), (175, 15)), ((15, 195), (75, 195)),
    ]
    lacivert, turuncu, krem = (0.1, 0.2, 0.45), (0.95, 0.5, 0.1), (0.98, 0.95, 0.85)
    boyalar = [
        ([(-3, -3), (218, -3), (218, 213), (-3, 213)], krem),
        ([(12, 55), (78, 55), (78, 155), (12, 155)], lacivert),     # ön
        ([(112, 55), (178, 55), (178, 155), (112, 155)], lacivert),  # arka
        ([(72, 55), (118, 55), (118, 155), (72, 155)], turuncu),    # sağ yan
        ([(172, 55), (218, 55), (218, 155), (172, 155)], turuncu),  # sol yan
    ]
    beyaz = (1, 1, 1)
    yazilar = [
        (24, 100, "ÖN / FRONT", 13, beyaz),
        (27, 120, "60x40x100", 9, beyaz),
        (124, 100, "ARKA / BACK", 12, beyaz),
        (82, 105, "SAG", 12, lacivert),
        (182, 105, "SOL", 12, lacivert),
        (128, 38, "ÜST KAPAK", 10, lacivert),
        (28, 178, "ALT KAPAK", 10, lacivert),
    ]
    cizim("ornek_tuckend.pdf", 215, 210, kontur, katlar, boyalar, yazilar)


def piramit():
    # kare taban 60 mm, üçgen yan yüz yüksekliği 60 mm, serbest form (açılı kenarlar)
    a, s = 60, 60
    ox, oy = 70, 70  # taban sol üst
    b = [(ox, oy), (ox + a, oy), (ox + a, oy + a), (ox, oy + a)]
    tepe = [(ox + a / 2, oy - s), (ox + a + s, oy + a / 2),
            (ox + a / 2, oy + a + s), (ox - s, oy + a / 2)]
    # yapıştırma klapesi: üst üçgenin sağ kenarına
    p1, p2 = tepe[0], b[1]
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    L = math.hypot(dx, dy)
    nx, ny = dy / L * 10, -dx / L * 10  # dışa normal
    g1 = (p1[0] + dx * 0.2 + nx, p1[1] + dy * 0.2 + ny)
    g2 = (p1[0] + dx * 0.85 + nx, p1[1] + dy * 0.85 + ny)
    kontur = [b[0], tepe[0], g1, g2, b[1], tepe[1], b[2], tepe[2], b[3], tepe[3]]
    katlar = [(b[0], b[1]), (b[1], b[2]), (b[2], b[3]), (b[3], b[0]), (tepe[0], b[1])]
    renkler = [(0.85, 0.2, 0.25), (0.2, 0.55, 0.35), (0.2, 0.35, 0.75), (0.9, 0.7, 0.1)]
    boyalar = [([b[0], b[1], b[2], b[3]], (0.15, 0.15, 0.15))]
    # tepe[i], b[i]-b[i+1] kenarına ait üçgenin ucu
    boyalar += [([b[i], b[(i + 1) % 4], tepe[i]], renkler[i]) for i in range(4)]
    yazilar = [(ox + 14, oy + 34, "TABAN", 12, (1, 1, 1))]
    cizim("ornek_piramit.pdf", 200, 200, kontur, katlar, boyalar, yazilar)


if __name__ == "__main__":
    tuckend()
    piramit()
