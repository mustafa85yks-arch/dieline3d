# Dieline 3D

Illustrator'da çizilen kutu açınımını (AI/PDF) tarayıcıda 3D'ye çevirir:
tasarımı kutunun üstünde görürsün, düz açınımdan kutuya katlanma animasyonunu izlersin.

Geliştirme planı ve not listesi: [YOL_HARITASI.md](YOL_HARITASI.md)

## Açma

`Baslat.command` dosyasına çift tıkla. Yerel sunucuyu (`sunucu.py`) başlatır ve tarayıcıyı açar.
Ayarları sabitlemek için sunucu şart. İnternet gerekir, çünkü Three.js ve pdf.js CDN'den yükleniyor.

AI/PDF dosyasını sağ tarafa sürükle ya da **AI / PDF aç** butonunu kullan.

**Doğrudan .ai çalışma dosyasıyla çalış, PDF almaya gerek yok.** Dosyayı açınca **Illustrator'da aç** ile düzenlemeye geç,
**⌘S** ile kaydedince 3D kendiliğinden güncellenir (açılar, roller, duruş, karton korunur; bıçak değiştiyse taban yeniden seçilir).
Elle yenilemek için **Güncelle**. Tarayıcı dosyanın diskteki yerini vermediği için sunucu dosyayı Spotlight'ta ad + boyut + tarihle bulur;
bulamazsa (Spotlight'ın aramadığı bir klasör) bu iki buton kapalı kalır.

## Web sürümü (GitHub Pages)

Aynı editör web adresinden de açılır, kurulum gerekmez. Dosyalar hiçbir yere yüklenmez, her şey tarayıcının içinde işlenir.
Web'de iki fark var:
- **Ayarları sabitle** dosyaya değil **bu tarayıcının hafızasına** yazar: sadece o bilgisayarda, o tarayıcıda görünür.
  Başka bilgisayara taşımak için **Ayarları kaydet / Ayar yükle** (JSON dosyası) kullanılır.
- **Illustrator'da aç / Güncelle** web'de yoktur (bilgisayardaki dosyaya erişemez). Bunlar için `Baslat.command` ile yerel aç.

## Dosya nasıl hazırlanmalı

**Kesim ile katı operatör renkle ayırır, araç tahmin yürütmez.** Böylece operatör kendi işini kontrol etmiş olur.

- AI dosyası **"PDF uyumlu dosya oluştur"** seçeneği açık kaydedilmiş olmalı (Illustrator'da varsayılan).
- Kesim ve kat **ayrı renkte** olmalı. Araç sırayla şuna bakar:
  1. **Spot adı:** `KESIM`, `BICAK`, `Kesim izi`, `cutting`, `Cutter Guide`, `Dieline`, `Stanze`, `découpe` kesim sayılır.
     `KAT`, `Katlama izi`, `PILYAJ`, `fold`, `crease`, `Rill`, `Nut`, `rainage` kat sayılır.
     Diğer spotlar (PANTONE, LAK, VARAK, GLUE, UV, Emboss, Perfo…) yok sayılır. Dosyada adı dieline olan bir spot varsa
     spotsuz çizgilerin hepsi yok sayılır.
  2. **Spot yoksa renk:** kırmızı kesim, yeşil kat. Başka her renk (yazı, ölçü oku, çerçeve) yok sayılır.
  3. Katman adında `kesim / cut / die / bıçak` ya da `kat / biga / crease` geçerse sadece o katmandaki çizgilere bakılır.
- **Tek renk BICAK** (kesim ve kat aynı spotta) ayrılmaz. Araç "kat çizgisi bulunamadı" der: katları ayrı spota (KAT) al
  ya da *Çizgi grupları*'ndan elle seç.
- Her grubun neden o rolü aldığı *Çizgi grupları* tablosunda yazar. Gerekirse oradan elle düzeltilir.
- Kesim konturu kapalı olmalı. Kat çizgilerinin uçları kontura değmeli (0,2 mm tolerans; 4 mm'ye kadar kısa kalan kat uzatılır).

## Nasıl çalışır

1. **Çizgi grupları**: çizgiler katman, renk ve kesikli/düz özelliğine göre gruplanır.
   Kural yukarıda. Yanlışsa her grubu *Kesim / Kat / Yok say* olarak düzelt.
2. **Paneller**: kesim ve kat çizgilerinin oluşturduğu kapalı alanlar bulunur. Dikdörtgen
   varsayımı yok. Açılı klapeler, pencereler (iç kesim) ve iç klapeler de çalışır.
3. **Taban**: otomatik seçilir (kat sayısı × alan en büyük panel; kutunun dört duvara bağlı tabanı).
   Açınımda kalın çerçeveyle gösterilir. Değiştirmek için açınımda parçaya tıkla, adının altında çıkan **⌂ Taban yap**'a bas
   (ya da *Katlar* bölümündeki **Taban** seçimini kullan).
   Taban değişince önceki Devir/Çevir döndürmeleri sıfırlanır: kutu yeni tabanının üstüne oturur, **⌂ Başa dön** de buraya döner.
   **Taban elle seçildiyse kutu hep o tabanın üstünde durur:** Oynat tabanın üstünde biter. **↻ Çevir** kaydedilir (hangi yan öne bakacak),
   **⟲ Devir** sadece bakmak içindir, kaydedilmez. Otomatik tabanda duruş eskisi gibi serbesttir (baskılı yüz üste gelir).
   Bıçak izi **Açık hâli**'ne geçince kendiliğinden açılır; kapatılabilir, kapalı hâle dönünce önceki durumuna döner.
   Kat çizgisi kesimden 4 mm'ye kadar önce bitiyorsa otomatik uzatılır. Kilit yarıkları gibi hiçbir kata bağlı
   olmayan küçük parçalar delik sayılır.
4. **Katlar** (tıklayınca açılır), her kat için:
   - **Açı**: 0° düz. Varsayılan 90°, uç klapelerde 91°: klape 1° fazla katlanıp örttüğü duvarın ya da kapağın içine girer.
     90°'de iki parça aynı düzlemde kalıp görüntü titreşir. 88° ise klapeyi duvarın içinden dışarı taşırıyordu.
     Bir panelin **içinden kesilmiş** parça (kilit dili, U kanca) ve ona bağlı parçalar 0°: düz kalır, kilit dili dik durup yarığa girer.
     İçten kesilmiş sayılması için: kesim kenarlarının yarıdan fazlası tek bir komşu panele bakmalı ve parça o panelin sınır kutusunun içinde olmalı.
   - **Yön**: *İçe* seçilirse baskılı yüz dışarıda kalır.
   - **Adım**: aynı adımdaki katlar birlikte katlanır, adımlar birbirine %35 binerek akar. Varsayılan sıra (Oynat):
     önce içeride kalacak parçalar (yapıştırma kulağı, toz kapakları, kapak dilleri, kilitler) duvarlar düzken katlanır,
     sonra duvarlar kalkar, sonra kapanışlar, **en son kapak kapanır**. Taban değişince sıra yeniden hesaplanır (açı ve yön korunur).
     Kutunun altı tek parça değilse (bazı ayakkabı kutuları gibi) sırayı elle düzeltmek gerekebilir.
     bir parça bağlı olduğu parçadan önce katlanmaz; mailer kapağı gibi büyük parçalar en sona kalır.
5. **Açık hâli / Kapalı hâli**: tek tıkla düz açınıma, tepeden dik bakışa geçer.
6. **Bıçak izi**: kesim (kırmızı) ve kat (yeşil kesikli) çizgilerini tasarımın üstüne çizer, panel kenar
   çizgilerini de gösterir. Kapalı kutuda da çalışır. Kapalıyken kutuda hiç çizgi görünmez.
   **Tek tıkla** (3D'de ya da açınımda): *Katlar*'da o parçayı katlayan satır açılır, vurgulanır ve açı kutusu seçili gelir; yeni açıyı hemen yazabilirsin. Tabana tıklanırsa *Taban* seçimi gösterilir.
   **Çift tıkla** (telefonda çift dokun): tıklanan parça bağlı olduğu kattan açılır, tekrar çift tıklayınca kapanır.
   Kapalı bir kapağın altındaki parçaya ulaşmak için önce kapağı açmak gerekir. *Oynat* ve *Başa dön* hepsini kapatır.
7. **Kontrol paneli** (3D'nin sağ altı), üç grup:
   - Duruş: **⟲ Devir** kutuyu sana doğru bir yüzünün üstüne devirir, **↻ Çevir** olduğu yerde 90° döndürür,
     **⌂ Başa dön** başlangıç duruşuna döner.
   - Sürükleme modu (biri hep seçili): **⟳ Döndür** kamerayı kutunun etrafında döndürür (varsayılan),
     **✥ Taşı** kaydırır (sağ tık her modda kaydırır).
   - **＋ / －** yakınlaş/uzaklaş, **⤢ Sığdır** kutuyu ortalar ve Döndür moduna döner.
   Dar ekranda panel alta yatay dizilir. Yeni açılan dosyada en çok baskının olduğu yüz otomatik üste gelir. Bu iki hareketle kutunun 24 duruşunun hepsine ulaşılır.
   Katlama animasyonunun son çeyreğinde kutu seçilen duruşa kendiliğinden döner.
   Ayarladığın duruş müşteri dosyasında başlangıç duruşu olur ve ayar dosyasına da kaydedilir.
8. **Karton**: beyaz / kraft / gri. Tasarım kartonla multiply karışır; kraftta baskısız alanlar kraft görünür
   (beyaz alt baskı simüle edilmez).
   **Varak (hot foil):** adında `VARAK`, `foil`, `folie`, `yaldız`, `hot stamp` ya da `shiny` geçen spot renk ya da katman
   varak sayılır ve metalik, ışığı yansıtan folyo olarak görünür: yüzeydeki 45° çapraz, geniş dalgalanma (bant aralığı 25 mm) gerçek varaktaki
   gibi parlak/koyu bantlar verir, kutuyu döndürdükçe bantlar gezer (`FOIL_WAVE_MM`, `FOIL_COLORS` ile ayarlanır). *Görünüm*'deki **Varak**
   seçiminden Altın / Gümüş / Bakır ya da Kapalı (spotun kendi rengiyle düz baskı). Adında renk yoksa Altın açılır;
   `silver/gümüş` Gümüş, `copper/bakır` Bakır. Seçim sabitlenebilir, müşteri dosyasında da parlar.
   Varak kalıbı Illustrator'ın ayrımı gibi çıkar: varak nesnesinin üstüne sonradan çizilen yazı, şekil ve fotoğraf varakı deler
   (overprint yok sayılır); bıçak çizgileri delmez. Saydamlık grubu / maske içindeki varak tanınmayabilir.
9. **Ayarları sabitle**: operatör çizgi rollerini, tabanı, açıları, yönleri, adımları, duruşu ve kartonu ayarlayıp basar.
   Ayar `ayarlar/` klasörüne yazılır. Aynı bıçak tekrar açılınca **kendiliğinden gelir**. Bıçak, dosya adına değil
   geometrisine göre tanınır: dosya yeniden adlandırılsa ya da tasarımı değişse de bıçak aynıysa ayar bulunur.
   **Sabitle = ekranda gördüğün hâl kutunun son hâlidir.** Çift tıklayarak açtığın parçalar o anki açılarıyla tabloya yazılır
   (90°'lik kapak açıkken -19° olur); Oynat da artık o hâlde biter.
   Sabitledikten sonra bir şey değişirse ya da bir parçayı çift tıklayıp açarsan buton **Değişikliği sabitle ●** olur.
   **Varsayılana dön** sabit ayarı siler.
   Sabitlemek için editör `Baslat.command` ile açılmalı (ayarı o sunucu yazar).
   **Ayarları kaydet / Ayar yükle** aynı ayarı JSON dosyası olarak indirir / geri yükler (başka bilgisayara taşımak için).
10. Çıktılar: **PNG** (o anki görüntü) ve **video** (Chrome/Safari'de MP4, diğerlerinde WebM).

## Müşteriye gönderme

**Müşteriye gönder** bölümünde ürün adını yaz, dili seç, **Müşteri dosyası oluştur**'a bas.
Tek bir `…_3D.html` dosyası iner (örnek kutularda 2–3 MB). E-postayla gönderilir.

- Müşteri çift tıklayıp açar. Kutu kendiliğinden katlanır ve senin ayarladığın duruşa geçer.
  Butonlar: *Tekrar oynat*, *Açık hâli*, *Bıçak izi*; sağ altta aynı kontrol paneli (*Başa dön* senin duruşuna döner).
  Müşteri de parçalara çift tıklayıp kapakları açabilir.
- İçinde sadece tasarımın görüntüsü (JPEG) ve geometri var. PDF, vektör dieline ve düzenleme araçları yok.
- 3D kütüphanesi dosyanın içine gömülü, **internetsiz** açılır.
- Dosya oluşturulurken editörün internete bağlı olması gerekir (kütüphane o an indirilir).
- `testler/` klasörü (gerçek dosyalar, müşteri tasarımları) depoya dahil değildir.

## Sınırlar

- Çarpışma simülasyonu yok. Crash-lock gibi kilitli yapılarda açıları ve adımları elle ayarlaman gerekir.
- Karton kalınlığı yok, paneller sıfır kalınlıkta. Üst üste gelen klapeleri 1–2° farkla ayır.
- Sadece PDF'in **1. sayfası** okunur.
- Kesim ve kat renginde çizilmiş artwork çizgileri de dokudan düşer (dieline rengiyle aynı renkte kontur kullanma).

## Dosyalar

| Dosya | İçerik |
|---|---|
| `dieline3d.html` | Uygulama (tek dosya) |
| `Baslat.command` | Yerel sunucu + tarayıcı |
| `ornek_uret.py` | Test PDF'lerini üretir (PyMuPDF) |
| `ornek_tuckend.pdf` | 60×40×100 mm straight tuck end (test için; editörde butonu yok) |
| `ornek_piramit.pdf` | Kare tabanlı piramit (yan yüzler 120°) |
| `YOL_HARITASI.md` | Geliştirilecekler, bilinen sınırlar, yapılanlar |
| `mailer_uret.py` | Parametrik mailer dieline'ı: `python3 mailer_uret.py 315 202 62` |
