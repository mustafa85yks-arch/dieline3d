#!/usr/bin/env python3
"""Dieline 3D yerel sunucusu.

Dosyaları sunar ve operatörün sabitlediği ayarları ayarlar/<imza>.json olarak yazar.
İmza, bıçağın (kesim + kat çizgileri) geometrisinden tarayıcıda hesaplanır: dosya adı ya da
tasarım değişse de bıçak aynıysa aynı ayar bulunur.

Kullanım: python3 sunucu.py [port]
"""
import glob
import http.server
import json
import os
import re
import subprocess
import sys
import urllib.parse

KOK = os.path.dirname(os.path.abspath(__file__))
AYAR = os.path.join(KOK, "ayarlar")
IMZA = re.compile(r"^/ayar/([0-9a-f]{16,64})$")
UZANTI = (".pdf", ".ai")


def illustrator_yolu():
    """En yeni Illustrator: uygulama adı her sürümde "Adobe Illustrator.app", sürüm klasör adında."""
    yollar = glob.glob("/Applications/Adobe Illustrator*/Adobe Illustrator.app")
    yil = lambda y: int((re.search(r"(\d{4})", y) or [0, 0])[1])
    return max(yollar, key=yil) if yollar else None


def dosya_bul(ad, boyut, mtime):
    """Tarayıcı dosyanın yolunu vermez: Spotlight'ta aynı ad + boyut (+ tarih) olanı bul."""
    try:
        cikti = subprocess.run(["mdfind", "-name", ad], capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return None
    adaylar = []
    for yol in cikti.splitlines():
        if os.path.basename(yol) != ad or not os.path.isfile(yol):
            continue
        st = os.stat(yol)
        if st.st_size != boyut:
            continue
        adaylar.append((abs(st.st_mtime - mtime), yol))
    adaylar.sort()
    return adaylar[0][1] if adaylar and adaylar[0][0] < 5 else None


def gecerli_yol(yol):
    return bool(yol) and yol.lower().endswith(UZANTI) and os.path.isfile(yol)


class Isleyici(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=KOK, **k)

    def end_headers(self):
        # editör her zaman güncel sürümüyle açılsın (tarayıcı önbelleği eski HTML'i açıyordu)
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _cevap(self, kod, veri=None):
        govde = json.dumps(veri if veri is not None else {}, ensure_ascii=False).encode()
        self.send_response(kod)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(govde)))
        self.end_headers()
        self.wfile.write(govde)

    def _sorgu(self):
        u = urllib.parse.urlparse(self.path)
        return u.path, {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}

    def _govde(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n) or b"{}")

    def do_GET(self):
        yol, q = self._sorgu()
        if yol == "/durum":   # açık dosya kaydedildi mi (Illustrator'dan kaydedince 3D kendini günceller)
            d = q.get("yol")
            if not gecerli_yol(d):
                return self._cevap(200, {"yok": True})
            st = os.stat(d)
            return self._cevap(200, {"mtime": st.st_mtime, "boyut": st.st_size})
        if yol == "/dosya":
            d = q.get("yol")
            if not gecerli_yol(d):
                return self._cevap(404, {"hata": "dosya yok"})
            with open(d, "rb") as f:
                veri = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Length", str(len(veri)))
            self.end_headers()
            self.wfile.write(veri)
            return
        m = IMZA.match(self.path)
        if not m:
            return super().do_GET()
        yol = os.path.join(AYAR, m.group(1) + ".json")
        if not os.path.exists(yol):
            return self._cevap(200, {"yok": True})   # 404 değil: tarayıcı konsolu kırmızıya boyanmasın
        with open(yol, encoding="utf-8") as f:
            return self._cevap(200, json.load(f))

    def do_POST(self):
        yol, _ = self._sorgu()
        try:
            g = self._govde()
        except ValueError:
            return self._cevap(400, {"hata": "geçersiz JSON"})
        if yol == "/bul":
            return self._cevap(200, {"yol": dosya_bul(g.get("ad", ""), g.get("boyut", -1), g.get("mtime", 0))})
        if yol == "/illustrator":
            d = g.get("yol")
            if not gecerli_yol(d):
                return self._cevap(404, {"hata": "dosya bulunamadı"})
            app = illustrator_yolu()
            if not app:
                return self._cevap(500, {"hata": "Illustrator /Applications altında bulunamadı"})
            r = subprocess.run(["open", "-a", app, d], capture_output=True, text=True)
            if r.returncode != 0:
                return self._cevap(500, {"hata": r.stderr.strip() or "açılamadı"})
            return self._cevap(200, {"tamam": True, "uygulama": os.path.basename(os.path.dirname(app))})
        return self._cevap(404)

    def do_PUT(self):
        m = IMZA.match(self.path)
        if not m:
            return self._cevap(404)
        n = int(self.headers.get("Content-Length", 0))
        try:
            veri = json.loads(self.rfile.read(n))
        except ValueError:
            return self._cevap(400, {"hata": "geçersiz JSON"})
        os.makedirs(AYAR, exist_ok=True)
        gecici = os.path.join(AYAR, m.group(1) + ".json.tmp")
        with open(gecici, "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=1)
        os.replace(gecici, os.path.join(AYAR, m.group(1) + ".json"))
        return self._cevap(200, {"tamam": True})

    def do_DELETE(self):
        m = IMZA.match(self.path)
        if not m:
            return self._cevap(404)
        yol = os.path.join(AYAR, m.group(1) + ".json")
        if os.path.exists(yol):
            os.remove(yol)
        return self._cevap(200, {"tamam": True})

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    http.server.ThreadingHTTPServer(("127.0.0.1", port), Isleyici).serve_forever()
