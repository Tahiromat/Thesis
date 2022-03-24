BASE_URL = "https://sim.csb.gov.tr/STN/STN_Report/StationDataDownloadNew"

SELECT_ALL_CITIES_PATH = "//*[@id='StationDataDownloadForm']/fieldset[1]/div[1]/div[1]/div[1]/div[2]/div/div/div/div/span[3]/i"

SELECT_STATION_DROPDOWN_BUTTON_PATH = "//*[@id='StationDataDownloadForm']/fieldset[1]/div[1]/div[1]/div[1]/div[5]/div/div/span[1]/span/span[2]/span"

STATION_NAME_PATH = "/html/body/div[12]/div/span/input"

SELECT_ALL_PARAMETERS_FOR_DF_PATH = "//*[@id='StationDataDownloadForm']/fieldset[1]/div[1]/div[1]/div[1]/div[6]/div/div/div/div/span[3]/i"

HOURLY_DF_PATH = "//*[@id='StationDataDownloadForm']/fieldset[1]/div[1]/div[1]/div[2]/div[1]/div/div/label[1]"

START_DATE_PATH = "//*[@id='StationDataDownload_StartDateTime']"

END_DATE_PATH = "//*[@id='StationDataDownload_EndDateTime']"

INQUIRE_FOR_DF_PATH = "//*[@id='StationDataDownloadForm']/fieldset[1]/div[1]/div[2]/div[1]/div/div/div/button"

EXPORT_DF_TO_XLSX_PATH = "//a[@class='k-button k-button-icontext k-grid-excel']"



STATION_LIST = [
"Adana - Çatalan",
"Adana - Doğankent",
"Adana - Meteoroloji",
"Adana - Valilik",
"Adana-Çukurova",
"Adana-Seyhan",
"Adana-Turhan Cemal Beriker Bulvarı ",
"Adana-Yakapınar",
"Adıyaman",
# "Afyon",
"Afyon - Merkez/Karayolları",
"Afyon - Sandıklı",
"Afyon-Selçuk Cami",
"Ağrı",
"Ağrı - Doğubeyazıt",
"Ağrı - Patnos",
"Aksaray",
"Amasya",
"Amasya - Merzifon",
"Amasya - Suluova",
"Amasya - Şehzade",
"Ankara - Bahçelievler",
"Ankara - Batıkent",
"Ankara - Demetevler",
"Ankara - Etimesgut",
"Ankara - Etlik",
"Ankara - Kayaş",
"Ankara - Keçiören Sanatoryum",
"Ankara - Ostim",
"Ankara - Polatlı",
"Ankara - Sıhhıye",
"Ankara - Sincan",
"Ankara - Siteler",
"Ankara - Törekent",
"Ankara - Ulus Trafik",
"Ankara Yaşamkent",
"Antalya",
"Antalya - Alanya",
"Antalya - Gazipaşa",
"Antalya - Kumluca Sanayi",
"Antalya - Manavgat",
"Antalya - Muratpaşa",
"Antalya - Serik",
"Antalya - Trafik",
"Ardahan",
"Artvin",
"Artvin - Hopa",
"Aydın",
"Aydın - Didim",
"Aydın - Efeler",
"Aydın - Germencik",
"Aydın - Nazilli",
"Aydın - Söke",
"Aydın - Trafik",
"Balıkesir",
"Balıkesir - Bandırma-MTHM",
"Balıkesir - Edremit - MTHM",
"Balıkesir - Erdek-MTHM",
"Balıkesir - Merkez - MTHM",
"Bartın",
"Batman",
"Bayburt",
"Bilecik",
"Bilecik - Bozüyük-MTHM",
"Bingöl",
"Bitlis",
"Bolu - Abant",
"Bolu - Karaçayır Parkı",
"Bolu - Kızılay Parkı",
"Burdur",
"Burdur - Bucak",
"Bursa",
"Bursa - Beyazıt Cad.-MTHM",
"Bursa - İnegöl-MTHM",
"Bursa - Kestel-MTHM",
"Bursa - Kültür Park-MTHM",
"Bursa - Uludağ Üniv.-MTHM",
# Bursa-Gürsu
# Bursa-Kestel (Hilal Parkı)
# Bursa-Nilüfer
# Çanakkale
# Çanakkale - Biga - MTHM
# Çanakkale - Biga İçdaş
# Çanakkale - Çan-MTHM
# Çanakkale - Lapseki-MTHM
# Çankaya Yaygınlaştırma
# Çankırı
# Çorum
# Çorum - Bahabey
# Çorum - Mimar Sinan
# Denizli - Bayramyeri
# Denizli - Çivril
# Denizli - Merkezefendi
# Denizli - Sümer
# Denizli - Trafik
# Denizli Honaz Yaygınlaştırma
# Diyarbakır
# Düzce
# Düzce - Bahçeşehir
# Düzce - Belediye
# Edirne
# Edirne - Karaağaç-MTHM
# Edirne - Keşan-MTHM
# Elazığ
# EMEP - Ankara Çubuk
# EMEP - İzmir Seferihisar
# EMEP - Kırklareli Vize
# Erzincan
# Erzincan - Trafik
# Erzurum
# Erzurum - Aziziye
# Erzurum - Palandöken
# Erzurum - Pasinler
# Erzurum - Taşhan
# Eskişehir - Cumhuriyet Bulvarı
# Eskişehir - Metin Sonmez
# Eskişehir - Odunpazarı
# Eskişehir - Tepebaşı
# Eskişehir Vişnepark Yaygınlaştırma
# Gaziantep
# Gaziantep - Beydilli
# Gaziantep - Gaski D6
# Gaziantep - Nizip
# Gaziantep - Sankopark
# Gaziantep Atapark Yaygınlaştırma
# Giresun
# Giresun - Gemilercekeği
# Gümüşhane
# Hakkari
# Hatay - Antakya
# Hatay - İskenderun
# Hatay - İskenderun Merkez
# Hatay - Vali Kavşağı
# Iğdır
# Iğdır - Aralık
# Isparta
# Isparta - Orman
# İstanbul - Aksaray
# İstanbul - Alibeyköy
# İstanbul - Arnavutköy
# İstanbul - Avcılar
# İstanbul - Bağcılar
# İstanbul - Başakşehir-MTHM
# İstanbul - Beşiktaş
# İstanbul - Büyükada
# İstanbul - Çatladıkapı
# İstanbul - Esenler
# İstanbul - Esenyurt-MTHM
# İstanbul - Göztepe
# İstanbul - Kadıköy
# İstanbul - Kağıthane
# İstanbul - Kağıthane-MTHM
# İstanbul - Kandilli
# İstanbul - Kandilli-MTHM
# İstanbul - Kartal
# İstanbul - Kumköy
# İstanbul - Maslak
# İstanbul - Mecidiyeköy-MTHM
# İstanbul - Portatif
# İstanbul - Sancaktepe
# İstanbul - Sarıyer
# İstanbul - Selimiye
# İstanbul - Silivri-MTHM
# İstanbul - Sultanbeyli-MTHM
# İstanbul - Sultangazi 1
# İstanbul - Sultangazi 2
# İstanbul - Sultangazi 3
# İstanbul - Sultangazi-MTHM
# İstanbul - Şile-MTHM
# İstanbul - Şirinevler-MTHM
# İstanbul - Tuzla
# İstanbul - Ümraniye
# İstanbul - Ümraniye-MTHM
# İstanbul - Üsküdar
# İstanbul - Üsküdar-MTHM
# İstanbul - Yenibosna
# İzmir - Aliağa
# İzmir - Aliağa - Bozköy
# İzmir - Alsancak İBB
# İzmir - Bayraklı İBB
# İzmir - Bornova
# İzmir - Bornova İBB
# İzmir - Çeşme
# İzmir - Çiğli İBB
# İzmir - Eğitim İstasyonu
# İzmir - Gaziemir
# İzmir - Güzelyalı İBB
# İzmir - Karabağlar
# İzmir - Karaburun
# İzmir - Karşıyaka
# İzmir - Karşıyaka İBB
# İzmir - Konak
# İzmir - Menemen
# İzmir - Ödemiş
# İzmir - Şirinyer İBB
# İzmir - Torbalı
# İzmir - Yenifoça
# İzmir-Kemalpaşa (yeni)
# Kahramanmaraş - Dulkadiroğlu
# Kahramanmaraş - Elbistan
# Kahramanmaraş - Kent Meydanı
# Kahramanmaraş - Onikişubat
# Karabük - . Yıl
# Karabük - Kardemir 1
# Karabük - Kardemir 2
# Karabük - Safranbolu
# Karabük - Tören Alanı
# Karaman
# Karaman - Ermenek
# Kars - İstasyon Mah.
# Kars - Trafik
# Kastamonu
# Kastamonu - Azdavay
# Kayseri - Hürriyet
# Kayseri - Kocasinan
# Kayseri - Melikgazi
# Kayseri - OSB
# Kayseri - Talas
# Kayseri - Trafik
# Kırıkkale
# Kırıkkale - Bulvar Park
# Kırklareli
# Kırklareli - Limanköy-MTHM
# Kırklareli - Lüleburgaz-MTHM
# Kırşehir
# Kilis
# Kocaeli
# Kocaeli - Alikahya-MTHM
# Kocaeli - Dilovası
# Kocaeli - Dilovası-İMES OSB 1-MTHM
# Kocaeli - Dilovası-İMES OSB 2-MTHM
# Kocaeli - Gebze - MTHM
# Kocaeli - Gebze OSB - MTHM
# Kocaeli - Gölcük-MTHM
# Kocaeli - İzmit-MTHM
# Kocaeli - Kandıra-MTHM
# Kocaeli - Körfez-MTHM
# Kocaeli - Yeniköy-MTHM
# Konya - Akşehir
# Konya - Karatay (SunayPark)
# Konya - Karkent
# Konya - Meram
# Konya - Merkez/Trafik
# Konya- Bosna (Yeni)
# Konya Ereğli Yaygınlaştırma
# Konya Laboratuvar Yaygınlaştırma
# Konya-Erenköy-Belediye
# Konya-Karatay
# Konya-Selçuklu-Belediye
# Kütahya - Ataturk Bulvarı
# Kütahya - Heymeana Cad.
# Kütahya - Kentpark
# Kütahya - Tavşanlı
# Malatya
# Mamak Yaygınlaştırma
# Manisa
# Manisa - Akhisar (Yeni)
# Manisa - Alaşehir
# Manisa - Kırkağaç
# Manisa - Salihli (Yeni)
# Manisa - Soma
# Manisa - Turgutlu (Yeni)
# Manisa - Ulupark
# Manisa - Yunusemre
# Mardin
# Mersin - Akdeniz
# Mersin - Huzurkent
# Mersin - İstiklal Cad.
# Mersin - Tarsus
# Mersin - Tasucu
# Mersin - Toroslar
# Mersin - Yenişehir
# Muğla - Datça
# Muğla - Fethiye
# Muğla - Milas
# Muğla - Milas Ören
# Muğla - Musluhittin
# Muğla - Trafik
# Muğla - Yatağan
# Muş
# Nevşehir
# Nevşehir - Avanos
# Niğde
# Niğde - Bor
# Ordu - Fatsa
# Ordu - Karşıyaka
# Ordu - Stadyum
# Ordu - Ünye
# Osmaniye
# Osmaniye - Kadirli
# Rize
# Rize - Ardeşen
# Sakarya
# Sakarya - Hendek OSB - MTHM
# Sakarya - Merkez-MTHM
# Sakarya - Ozanlar-MTHM
# Samsun - Atakum
# Samsun - Bafra
# Samsun - Canik
# Samsun - İlkadım Hastane
# Samsun - Tekkeköy
# Samsun - Yüzüncüyıl
# Sarayönü Arkaplan
# Siirt
# Sinop
# Sinop - Boyabat
# Sinop - Erfelek
# Sivas - Başöğretmen
# Sivas - İstasyonkavşağı
# Sivas - Meteoroloji
# Şanlıurfa
# Şırnak
# Tekirdağ
# Tekirdağ - Çerkezköy-MTHM
# Tekirdağ - Çorlu - MTHM
# Tekirdağ - Çorlu OSB - MTHM
# Tekirdağ - Merkez-MTHM
# Tokat
# Tokat - Erbaa
# Tokat - Meydan
# Tokat - Turhal
# Trabzon - Akçaabat
# Trabzon - Beşirli
# Trabzon - Fatih
# Trabzon - Meydan
# Trabzon - Uzungöl
# Trabzon - Valilik
# Tunceli
# Uşak (Yeni)
# Uşak-Trafik (Yeni)
# Van
# Yalova
# Yalova - Altınova-MTHM
# Yalova - Armutlu-MTHM
# Yozgat
# Yozgat - Sorgun
# Zonguldak - Çatalağzı Cumayanı
# Zonguldak - Çatalağzı Kuzyaka
# Zonguldak - Çaycuma
# Zonguldak - Karadeniz Ereğli
# Zonguldak - Kilimli
# Zonguldak - Kozlu
# Zonguldak - Muslu Tepeköy
# Zonguldak - Trafik
]