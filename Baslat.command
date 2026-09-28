#!/bin/bash
# Dieline 3D'yi yerel sunucuyla açar. Pencereyi kapatınca sunucu durur.
# Sunucu, operatörün sabitlediği ayarları ayarlar/ klasörüne yazar.
cd "$(dirname "$0")"
PORT=8765
while lsof -i :$PORT >/dev/null 2>&1; do PORT=$((PORT+1)); done
( sleep 1; open "http://localhost:$PORT/dieline3d.html" ) &
echo "Dieline 3D çalışıyor: http://localhost:$PORT/dieline3d.html"
echo "Kapatmak için bu pencereyi kapat (veya Ctrl+C)."
python3 sunucu.py $PORT
