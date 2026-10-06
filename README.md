# Dieline 3D

Illustrator'da çizilen kutu açınımını (AI/PDF) tarayıcıda 3D'ye çevirir:
tasarımı kutunun üstünde görürsün, düz açınımdan kutuya katlanma animasyonunu izlersin.

Web adresi: https://mustafa85yks-arch.github.io/dieline3d/

## Açma

`Baslat.command` dosyasına çift tıkla. Yerel sunucuyu (`sunucu.py`) başlatır ve tarayıcıyı açar.
Ayarları sabitlemek için sunucu şart. İnternet gerekir, çünkü Three.js ve pdf.js CDN'den yükleniyor.

AI/PDF dosyasını sağ tarafa sürükle ya da **AI / PDF aç** butonunu kullan.

**Doğrudan .ai çalışma dosyasıyla çalış, PDF almaya gerek yok.** Dosyayı açınca **Illustrator'da aç** ile düzenlemeye geç,
**⌘S** ile kaydedince 3D kendiliğinden güncellenir (açılar, roller, duruş, karton korunur; bıçak değiştiyse taban yeniden seçilir).
Elle yenilemek için **Güncelle**. Tarayıcı dosyanın diskteki yerini vermediği için sunucu dosyayı Spotlight'ta ad + boyut + tarihle bulur;
bulamazsa (Spotlight'ın aramadığı bir klasör) bu iki buton kapalı kalır.

## Ön / Arka baskı

**2 sayfalı PDF/AI'de sayfa 1 = ön yüz, sayfa 2 = arka yüz** (bizim işleyişte hep böyle). Sayfa 2 aynı bıçağın üstüne, karton içine (arka yüze) kaplanır:
kutuyu açınca ya da alttan bakınca iç baskı görünür. 3D'nin üstündeki **Ön / Arka** düğmesi açıktır; **Page 1 / Page 2** sayfaları tek tek gösterir.
**↔ Arka aynası** arka baskının iç yüze nasıl oturacağını seçer: yatay (kitap gibi çevrilen sayfa, varsayılan) · dikey · yok. Ayarları sabitle ile saklanır.
3 ve daha çok sayfalı dosyada sayfalar ayrı sekmedir (ön/arka sayılmaz).

## Karton kalınlığı

**Görünüm → Kalınlık** (0 / 0,3 / 0,5 / 1 mm, varsayılan 0 = ince yaprak). Parçalar üst üste gelince (klape duvarın içinde, kapak duvarın üstünde)
aynı düzlemde titreşme ve varak/baskı sızması olmasın diye kartona gerçek kalınlık verir: baskı yüzü yerinde, arka yüz kalınlık kadar altta, kenarlar karton renginde.
Kat ekseni kartonun **çukur (içe bakan) yüzünde** durur, dış yüz köşede yarıçapı kalınlık kadar yuvarlanır (baskı köşeyi sarar), 180° katta iki kat birbirine yapışık biner. Kalın bir karton numunesinin fotoğraflarına göre kuruldu.
Ayarları sabitle ve müşteri dosyasına girer. Kırma (kavisli) parçalar ve silindirde denenmedi.

## Katmanlar (kontrol aracı)

Dosyada birden çok kanal varsa Görünüm'ün altında **Katmanlar** bölümü çıkar: Baskı, BEYAZ, Yaldız, Gofre, Lak. BEYAZ her modda listelenir; Multiply'de beyaz zaten görünmez olduğu için **Sadece BEYAZ** dediğinde zemin geçici gri olur ve beyaz boya onun üstünde opak beyaz görünür. Her satırda göster/gizle kutusu ve **Sadece** düğmesi var:
**Sadece Gofre** → baskı, yaldız ve lak kapanır, kutu yalnızca gofre kabartmasıyla görünür (kontrol için). **Tümünü göster** hepsini geri açar.
Duruş, açılış ve ayarlar korunur, kutu yeniden yüklenmez. Müşteri dosyasına etkisi yok, hepsi açık gider.

## Karton yüzeyi

Baskılı **ön yüz parlak** (kuşe gibi, ışık yansıması), **arka yüz mat ve bir ton koyu** (beyazda hafif kirli beyaz, kraftta daha koyu esmer, grida bir ton koyu). **Ön yüz** seçimi Parlak / Yarı parlak / Mat. Arka yüz hep mat. Varsayılan karton türüne bağlı: **Kraft mat**, Beyaz ve Gri parlak; karton değişince Ön yüz kendiliğinden buna göre ayarlanır. Ön yüz'ü elle seçtiysen karton değişse de seçimin korunur. Ayarları sabitle ve müşteri dosyasına girer.

Karton **Kraft** seçilince gerçek kraft dokusu (`kraft_doku.jpg`) kaplanır: aynalı döşeme (dikiş görünmez), her parça 100 mm; arka yüz aynı dokunun bir ton koyusu.
Müşteri dosyasına doku gömülür (~250 KB). Web sürümünde `kraft_doku.jpg` `dieline3d.html` ile aynı klasörde olmalı.

## Yaldız (varak)

Varak dokusuz, pürüzsüz, **ayna gibi** pirinç tonlu altın folyo olarak çizilir (operatörün varak videolarına göre): kutuyu çevirdikçe yansıyan bölge değişir, folyo parlak şampanya ↔ koyu zeytin-bronz arasında gider. Gümüş ve bakır aynı mantıkla.
Yaldız izi (deboss) kenarda hafif eğim verir. Kırışık/dalga deseni yok; `foil_doku.jpg` artık kullanılmıyor, silindi. Web sürümü ve müşteri dosyası için ekstra dosya gerekmez.

## Yaldız izi (deboss)

Yaldız basılan yer hafif içe göçer: folyo maskesi bulanıklaştırılıp kabartma haritasına çukur olarak işlenir, hem kartona hem folyoya. Kenarda yumuşak bir eğim oluşur, yaldızın kenarı ışıkta belirir.
**Yaldız izi** seçimi (varak varsa görünür): Az (varsayılan) / Yok / Belirgin. Varak "Kapalı (düz baskı)" iken uygulanmaz. Ayarları sabitle ve müşteri dosyasına girer.

## GOFRE spotu (emboss / kabartma)

Adında `gofre / emboss / kabartma / blind` geçen spot kabartma sayılır: spotun yer tutucu rengi (örn. pembe) 3D'de görünmez, o alan hafif **yükselir**, kenarı ışıkta belirir (kabartma haritası, kenarda 0,3 mm yumuşak eğim; gerçek yükseklik değil, ışık-gölge). Pilyaj ve yaldız izi gibi ışıkla görünür. Kenar yumuşak ve geniş (0,55 mm, yastık gibi, gofre videosuna göre). **Gofre ayarı** kaydırıcıları (dosyada GOFRE varsa Görünüm'de çıkar): **Kenar** (0,05–1,2 mm, kenar yumuşaklığı), **Köşelilik** (0 yuvarlak/yastık, 1 köşeli: düz tepe ve keskin omuz), **Şiddet** (2–20, kabartma gücü). Değerler yanında yazar, **Sıfırla** varsayılana döner, Ayarları sabitle ile saklanır. **Arka yüzde aynı şekil ters iz (yumuşak çukur)** olarak, ön yüzde yükselen yerin tam arkasında görünür (arka baskıdan farklı olarak aynalanmaz); kutuyu açıp içine bakınca (veya düz açınımı arkadan) gofrenin ters izi okunur.
**GOFRE** seçimi (dosyada varsa görünür): Kabartma (varsayılan) / Eskisi gibi. Ayarları sabitle ve müşteri dosyasına girer. 

## LAK spotu (kısmi UV lak)

Adında `lak / uv / varnish / vernik / lacquer / laque` geçen spot kısmi UV lak sayılır: spotun yer tutucu rengi (örn. mavi) 3D'de görünmez, o alan **parlak yüzey** olur: mat zeminin üstünde pürüzsüz, ayna gibi bir film (kısmi UV lak). Lak parlak bir ofisi yansıtır: açıya göre gümüşi açık gri/beyaz (duvar, tavan, pencere) ile derin siyah (koyu nesne) arasında gider, renkli baskıda doygun ve derin görünür, üstünde beyaz parlama lekeleri olur; altındaki mat yüzey koyu ve yumuşak kalır. Kutuyu çevirdikçe parlama yerleri değişir. Kenarında lak kalınlığı kadar hafif kabartma var. Mat kartonda LAK alanı ışık yansıtarak belirgin öne çıkar.
**LAK** seçimi (dosyada varsa görünür): Parlak yüzey (varsayılan) / Eskisi gibi. Ayarları sabitle ve müşteri dosyasına girer. 

## Metalize karton (Karton: Metalize / gri)

**Karton → Metalize (gri)** gerçek metalize kâğıt gibi çizilir: ön yüz aynalı gümüş metal (baskısız yer parlak gümüş, baskı metali renklendirir, koyu mürekkep koyu metal), arka yüz mat kâğıt. **BEYAZ** spotu varsa (kendiliğinden Opak beyaz): beyaz alt baskı alanı metal parlamayı yutmaz ama bastırıp dağıtır: buzlu, yarı-metal (metal oranı 0,5, pürüzlülük 0,5); açıya göre beyazdan açık griye kayar (operatörün metalize baskı videolarından). Üstündeki baskı gerçek rengini alır. BEYAZ'ı elle seçtiysen kendiliğinden değişmez.

## BEYAZ spotu (beyaz boya)

Adında `beyaz / white / blanc / weiss / bianco` geçen spot, beyaz boya (alt baskı) sayılır. Spotun yer tutucu rengi (örn. turuncu) 3D'de görünmez, tonları (tint) dahil. **BEYAZ** seçimi (dosyada varsa görünür):
- **Multiply** (varsayılan): beyaz boya kartonu örtmez, yok sayılır; baskı kartonla çarpılır (kraftta koyulaşır).
- **Opak beyaz**: beyaz boya kartonu örter, üstündeki baskı gerçek rengiyle görünür (kraft, renkli karton, metalize).
- **Eskisi gibi**: spotun yer tutucu rengi olduğu gibi çizilir.
Ayarları sabitle ve müşteri dosyasına girer. 

## Gölge

Alan ışığı gölgesi: kutuya değen yer koyu ve keskin, uzaklaştıkça yumuşayıp solar. Işık küçük bir disk gibi kaydırılıp çok örnekten toplanır (hareket ederken 14, durunca 64 örnek).
Gölge haritası yok, bu yüzden hafiftir. Müşteri dosyasında da aynısı çalışır.

## Kat izi (pilyaj)

**Görünüm → Kat izi** (Yok / Hafif / Belirgin, varsayılan Hafif). Kat çizgilerine ışığa tepki veren kabartma (bump) çizer: ortada oluk, iki yanında kabarık omuz.
Baskıya dokunmaz, sadece ışık-gölge. Kırma şeritlerinin kat çizgileri de aynı izi alır. Ayarları sabitle ve müşteri dosyasına girer.

## İç kesikler (çentik, yarık)

Kesim renginde olup panel sınırı oluşturmayan, panelin içinde kalan açık kesikler (yarım yarık, çentik, kilit çentiği) artık 3D'de karton yüzünde koyu iz olarak görünür (ön ve arka yüz) ve kabartma haritasına dar, derin oluk işlenir.
Kartonun dışına taşan sarkıntılar ve 0,6 mm'den kısa kalıntılar alınmaz. Gerçek yarık değil, boyanmış iz: karton bütün kalır ve parçalar ayrılmaz.

## Perforasyon

Adında `perfor` / `perfo` / `yırtma` / `tear` geçen spot (PERFORAJ) perforasyon sayılır: karton bütün kalır, panel sınırı olmaz,
Çizgi grupları'nda "kesim" görünür. Kesim renginde kesikli çizgi ya da aralıklı kısa parçalar da eskisi gibi perforasyon sayılır.
3D'de perforasyon karton yüzünde (ön ve arka) küçük kesik izleri olarak görünür: uzun/kesikli çizgi 3 mm kesik + 1,5 mm bağ, zaten kısa parçalarsa olduğu gibi. Kabartma haritasına da kesik başına ince oluk işlenir (Kat izi açıkken). Gerçek delik değil, boyanmış iz.

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
- Kesim konturu kapalı olmalı. Bir kesim çizgisinin açık ucu başka bir kesim/kat çizgisine 0,6 mm'ye kadar kala bitiyorsa (el çizimi küçük açıklık, örn. kilit kulağı eğrisi) araç kendiliğinden köprüler. Kat çizgilerinin uçları kontura değmeli (0,2 mm tolerans; 4 mm'ye kadar kısa kalan kat uzatılır).
- **Perforasyon:** kesim renginde kesikli çizgi (kesikli stil ya da aralıklı kısa parçalar) perforasyon sayılır; karton bütün kalır,
  panel sınırı oluşturmaz, bıçak izinde kesikli görünür.

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
   **Çift tıkla** (telefonda çift dokun): tıklanan parça bağlı olduğu kattan açılır, tekrar çift tıklayınca kapanır. Açılış, katta yazan açı kadardır (90° kat 90° açılıp düz olur, 179° askı klapesi tam açılır). Düzü aşmasını istediğin kapak için katın ayarına `acilis` değeri verilebilir (JSON).
   **📌 Konumu sabitle:** *Katlar* tablosunda her satırın sonunda (ve açınımda parçaya tıklayınca "Taban yap"ın altında).
   Parçayı açılarla yerine oturt, sonra bas: parça **o an ekranda göründüğü yerde** (kapak çift tıkla açıkken bile) kutuya göre kilitlenir (🔒). Kapak açılsa, diğer açılar değişse de o parça ve ona bağlı parçalar oynamaz
   (ör. bir müşteri dosyasında kapağa bağlı ama tepsinin içinde duran iç duvar). Tekrar basınca çözülür. Ayarları sabitle ile kalıcı olur.
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

## Silindir (teneke kutu)

Teneke baskı şablonunda kesim dikdörtgeni ve bindirme çizgisi **SILINDIR** (ya da `TENEKE`) adlı spotta olursa araç kutu moduna geçer.
Spot adı yoksa *Çizgi grupları*'ndan şablon çizgisinin rolünü **Silindir** yap.
- Dikdörtgen = baskı alanı. İçindeki boydan boya dikey çizgi = bindirme payı (kenara yakın tarafı üst üste biner, görünmez).
- Çevre = en − bindirme, çap = çevre / π, yükseklik = dikdörtgenin boyu. Örnek: 171 × 121 mm, bindirme 4,7 mm → Ø52,9 mm (250 ml slim).
- Tasarım silindire sarılır, dikiş arkada kalır. Üst kapak (boyun, açma halkası) ve alt kubbe hazır gelir, alüminyum görünür.
- Baskısız (saydam) yerlerde metal görünür.
- **Müşteri dosyası** silindirde de çalışır: kutu döner, başlıkta çap × yükseklik yazar, katlama butonları gizlenir (teneke örneği: 5,5 MB).

## Sınırlar

- Çarpışma simülasyonu yok. Crash-lock gibi kilitli yapılarda açıları ve adımları elle ayarlaman gerekir.
- Kavisli katlar: **KIRMA** spotundaki katlar kavisli sayılır. Araç her yayı 21 noktaya böler, köşede buluşan yayların aynı sıradaki
  noktalarını birleştirip kırma çizgileri üretir (*Çizgi grupları*'nda "Kırma çizgileri", üretime gitmez) ve yıldız + mercek biçimli
  kutularda şekli kendisi hesaplar (mercek dik iner, yıldız kenarı yüksekliği = merceğin o noktadaki eninin yarısı). Bükülen bölge
  tek parça gibi davranır: kırımları *Katlar*'da tek tek listelenmez, tek tek açılmaz. Diğer kavisli biçimler (yastık kutu vb.) henüz yok;
  kuralı olmayan parçalar düz (0°) kalır.
- Karton kalınlığı yok, paneller sıfır kalınlıkta. Üst üste gelen klapeleri 1–2° farkla ayır.
- Çok sayfalı PDF'te 3D'nin sol üstünde **Page 1 / 2 / 3** sekmeleri çıkar; sayfa değişince roller, açılar ve karton korunur.
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


## Körüklü zarf (akordeon) ve yeni küçük seçenekler

**Katlar → Körük**: zarf gibi yan körüğü olan bıçaklarda derinliği panel yüksekliğinden hesaplar. *Derinlik paneli* (zarfta dipteki ince şerit, örn. P2), *Karşı gövde* (P1) ve körük zincirleri (tabana bağlı 3 panel, örn. P5→P6→P7) işaretlenir, **Körüğü uygula** açıları yazar. P1 ve P3 üstte birleşir, altta derinlik kadar açılır (kama); körük şeritleri üstte kapanır, altta açılır. **Kama** menüsü: *Dilimli* (varsayılan), *Sürekli yüzey (deneme)*, *Yok (levha)*.
**Görünüm → İç kesik izi**: panelin içine giren kesik uçları 3B'de koyu iz olarak çizilir. Var / Yok.
**Açınım → ⤢ Büyüt**: açınımı tam ekran açar (Esc ile kapanır); dar şeritlerin numarasını okumak için.

**Ölçü**: alt çubuktaki **Ölçü** düğmesi açıkken görünüm durunca kutunun üstünde ölçü çizgileri çıkar (dönerken gizlenir). Açınımda bir parçaya tıkla, çıkan **📏 Ölçü göster** düğmesine bas: o parçanın eni ve boyu 3B'de ölçülür (görünen kenarından, tercihen dış hatta). Tekrar basınca kalkar. Hiç parça seçilmemişse araç dış hattaki kenarları kendisi seçer. Seçim "Ayarları sabitle" ve müşteri dosyasına girer.
