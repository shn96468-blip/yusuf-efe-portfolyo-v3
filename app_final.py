# YAPAY ZEKA (AKIL) FONKSİYONU - TÜM DERSLER AKTİF!
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    response = ""

    # ===============================================
    # 7. SINIF MATEMATİK KONULARI (DAHA DA UZUN VE DETAYLI)
    # ===============================================
    if "rasyonel sayılar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Rasyonel Sayılar (Öğretmen Detayında!)
        
        **Tanım ve Kavramlar:** Rasyonel sayılar, $a$ bir tam sayı ve $b$ sıfırdan farklı bir tam sayı olmak üzere, $\\frac{a}{b}$ şeklinde yazılabilen sayılar kümesidir ($\\mathbb{Q}$). Her tam sayı (örneğin 5) paydası 1 olan bir rasyonel sayıdır (5/1). Ondalık gösterim ve devirli ondalık gösterimler de rasyonel sayıları ifade etmenin farklı yollarıdır.

        **Toplama ve Çıkarma İşlemleri:** Rasyonel sayılarda toplama ve çıkarma yapmanın temel kuralı, **paydaların eşit olmasıdır**. Paydalar eşitlendikten sonra, sadece paylar toplanır veya çıkarılır. Payda aynen yazılır.
        * **Örnek 1 (Eşitleme):** $\\frac{1}{2} + \\frac{1}{4}$ işleminde paydalar 4'te eşitlenir. $\\frac{1 \\cdot 2}{2 \\cdot 2} + \\frac{1}{4} = \\frac{2}{4} + \\frac{1}{4} = \\mathbf{\\frac{3}{4}}$
        * **Örnek 2 (Tam Sayılarla):** $3 - \\frac{1}{5}$ işleminde $3 = \\frac{15}{5}$ kabul edilir. $\\frac{15}{5} - \\frac{1}{5} = \\mathbf{\\frac{14}{5}}$

        **Çarpma ve Bölme İşlemleri:**
        * **Çarpma:** Paylar kendi arasında, paydalar kendi arasında çarpılır. **İşaret kuralını unutmayın!** $\\frac{2}{3} \\cdot (-\\frac{5}{7}) = \\mathbf{-\\frac{10}{21}}$
        * **Bölme:** Birinci rasyonel sayı aynen yazılır, ikinci rasyonel sayı ters çevrilir ve çarpma işlemi yapılır. $\\frac{1}{2} : \\frac{3}{4} \\rightarrow \\frac{1}{2} \\cdot \\frac{4}{3} = \\mathbf{\\frac{4}{6}} = \\mathbf{\\frac{2}{3}}$
        """
    elif "tam sayılar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Tam Sayılar (Öğretmen Detayında!)
        
        **Kümeler ve Gösterim:** Tam sayılar kümesi ($\\mathbb{Z}$), doğal sayılar kümesini ($\\mathbb{N}$) de içine alan daha geniş bir kümedir. Negatif sayılar ($-1, -2, -3, ...$), pozitif sayılar ($1, 2, 3, ...$) ve nötr olan sıfır (0) tam sayıları oluşturur. Sayı doğrusunun sağ tarafı pozitif, sol tarafı negatiftir.
        
        **Çıkarma İşlemi (Kural):** Çıkarma işlemi toplama işlemine dönüştürülür ve çıkan sayının işareti ters çevrilir.
        * **Örnek:** $(-7) - (-3) \\rightarrow (-7) + (+3) = \\mathbf{-4}$ (Büyük sayıdan küçük sayı çıkarılır, büyüğün işareti alınır).
        
        **Tam Sayıların Kuvveti:**
        * **Kural:** Negatif bir tam sayının **çift kuvvetleri pozitif** olurken, **tek kuvvetleri negatif** olur. Bu kural parantezli kullanımlarda geçerlidir.
        * **Örnek:** $(-5)^2 = +25$, $(-5)^3 = -125$. **DİKKAT:** Parantezsiz durumda $-2^4 = -16$ (çünkü eksi işareti etkilenmez).
        """
    elif "cebirsel ifadeler" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Cebirsel İfadeler (Öğretmen Detayında!)
        
        **Tanım ve Yapı:** Cebirsel ifadeler, en az bir değişken (bilinmeyen) ve en az bir işlem içeren matematiksel ifadelerdir. Örneğin, 'Bir sayının 3 katının 5 fazlası' ifadesi $\\mathbf{3x + 5}$ şeklinde gösterilir. Toplama ve çıkarma yapılırken sadece **benzer terimler** (değişkeni ve üssü aynı olanlar) toplanıp çıkarılabilir.

        **Temel Kavramların Ayrımı:** Cebirsel ifadeleri anlamak için bu terimleri çok iyi bilmelisiniz:
        1.  **Değişken (Bilinmeyen):** $x, y, a$ gibi harflerle gösterilen ve değeri değişebilen semboldür.
        2.  **Katsayı:** Değişkenin önündeki çarpım durumunda olan sayıdır. ($\mathbf{4}x - 7$'de $x$'in katsayısı $4$'tür.)
        3.  **Sabit Terim:** Yanında değişken bulunmayan sayıdır. ($\mathbf{4x - 7}$'de sabit terim $\mathbf{-7}$'dir.)
        4.  **Terim:** Bir cebirsel ifadede artı (+) veya eksi (-) işaretleriyle ayrılmış her bir kısım bir terimdir. ($4x - 7$ ifadesi iki terimlidir: $4x$ ve $-7$.)
        """
    
    # ===============================================
    # 7. SINIF TÜRKÇE KONULARI (DAHA DA UZUN VE DETAYLI)
    # ===============================================
    elif "fiiller" in topic_lower or "ek fiil" in topic_lower or "zarflar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Fiiller, Ek Fiil ve Zarflar (Öğretmen Detayında!)
        
        **Fiiller (Eylemler):** Bir iş, oluş veya durum bildiren kelimelerdir. Fiiller anlamlarına göre:
        1.  **İş (Kılış) Fiilleri:** Öznenin iradesiyle gerçekleşir ve nesne alabilirler. (Neyi, Kimi?) $\rightarrow$ **Okumak** (Kitabı okumak).
        2.  **Oluş Fiilleri:** Öznenin iradesi dışında, kendiliğinden zamanla gerçekleşir. $\rightarrow$ **Büyümek**, **Paslanmak**.
        3.  **Durum Fiilleri:** Öznenin içinde bulunduğu durumu bildirir, nesne almazlar. $\rightarrow$ **Uyumak**, **Gülmek**.
        
        **Ek Fiil (Ek Eylem):** 'İmek' fiilidir. İki hayati görevi vardır:
        1.  **İsimleri Yüklem Yapmak:** 'Burası dünkü maçın **yeriydi**.' (yer-i-idi)
        2.  **Basit Zamanlı Fiili Birleşik Zamanlı Yapmak:** 'Güneş her gün **doğuyormuş**.' (Şimdiki zamanın rivayeti)
        
        **Zarflar (Belirteçler):** Fiilin nasıl, ne zaman, ne kadar ve nereye yapıldığını belirten sözcüklerdir.
        * **Durum (Hal) Zarfları (Nasıl?):** 'Çocuk **hızlı** koşuyor.'
        * **Zaman Zarfları (Ne zaman?):** 'Misafirler **az önce** geldi.'
        * **Yer-Yön Zarfları (Nereye?):** 'Dışarı **çık**.'
        """
    elif "söz sanatları" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Söz Sanatları (Öğretmen Detayında!)
        
        Anlatıma güzellik, çekicilik ve etki gücü katan sanatlardır.
        
        **1. Benzetme (Teşbih):** Zayıf bir varlığın, ortak özellik bakımından güçlü bir varlığa benzetilmesidir. Dört temel ögesi vardır: benzeyen, benzetilen, benzetme yönü, benzetme edatı.
        * **Örnek:** 'Çocuğun dişleri **inci gibi** parlıyordu.' (Benzeyen: diş, Benzetilen: inci, Benzetme Yönü: parlaklık, Benzetme Edatı: gibi)
        
        **2. Kişileştirme (Teşhis):** İnsan dışındaki varlıklara insan özellikleri yüklenmesidir.
        * **Örnek:** 'Yorgun **bulutlar** şehre gözyaşı **döktü**.' (Ağlamak ve yorgunluk, bulutlara ait özelliklerdir.)
        
        **3. Abartma (Mübalağa):** Bir durumu, inandırıcı olmayacak derecede büyütmek veya küçültmek.
        * **Örnek:** 'Sana dünyalar kadar **ödev** verdim.' (Çokluk abartılmıştır.)
        """

    # ===============================================
    # 7. SINIF FEN BİLİMLERİ KONULARI (DAHA DA UZUN VE DETAYLI)
    # ===============================================
    elif "hücre" in topic_lower or "mitoz" in topic_lower or "mayoz" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Hücre ve Bölünmeler (Öğretmen Detayında!)
        
        **Hücre:** Canlıların en küçük yapısal ve işlevsel birimidir. Hayvan hücresi ve bitki hücresi arasında organel farkları vardır (Bitkide hücre duvarı, kloroplast, büyük koful bulunur).
        
        **1. Mitoz Bölünme:**
        * **Amaç:** Büyüme, gelişme, yıpranan doku ve organların onarımı. Tek hücrelilerde üremeyi sağlar.
        * **Sonuç:** Ana hücre ile **aynı** kromozom sayısına ve genetik yapıya sahip **2 yeni hücre** oluşur ($2n \\rightarrow 2n$).
        
        **2. Mayoz Bölünme:**
        * **Amaç:** Eşeyli üreme için **üreme hücrelerini (gamet)** oluşturmak.
        * **Sonuç:** Kromozom sayısı **yarıya iner** ve genetik yapısı farklı **4 yeni hücre** oluşur ($2n \\rightarrow n$). Mayoz, krossing over (parça değişimi) ile **tür içi çeşitliliği** sağlar.
        """
    elif "kütle ve ağırlık" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Kütle ve Ağırlık İlişkisi (Öğretmen Detayında!)
        
        Bu iki fiziksel kavram arasındaki ayrımı netleştirelim. Aralarındaki fark, kütlenin değişmez, ağırlığın ise kuvvete bağlı olarak değişir olmasıdır.
        
        * **Kütle (m):** Bir cisimdeki madde miktarıdır. Evrenin neresine giderseniz gidin **değişmez**. Ölçüm aracı **eşit kollu terazi**dir. Birimi kilogramdır (kg).
        * **Ağırlık (G):** Kütleye etki eden **yer çekimi kuvvetidir**. Bu kuvvet, gezegenlere göre değişir. Ölçüm aracı **dinamometre**dir. Birimi Newton (N)'dur.
        
        **Örnek:** Kütlesi 70 kg olan bir öğrencinin Dünya'daki kütlesi de 70 kg, Ay'daki kütlesi de 70 kg'dır. Ancak Dünya'daki ağırlığı $\\approx 700$ N iken, Ay'daki ağırlığı $\\approx 117$ N'dur (çünkü Ay'ın çekimi Dünya'nın $\\frac{1}{6}$'sı kadardır).
        """
        
    # ===============================================
    # 7. SINIF SOSYAL BİLGİLER KONULARI (DAHA DA UZUN VE DETAYLI)
    # ===============================================
    elif "kültür ve miras" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Kültür ve Miras (Öğretmen Detayında!)
        
        **Kültür:** Bir toplumun tarih boyunca ürettiği maddi (somut) ve manevi (soyut) tüm değerlerin bütünüdür. Bir toplumun yaşam tarzını, inançlarını, sanatını ve geleneklerini kapsar.
        
        **Kültürel Mirasın Unsurları:**
        1.  **Somut Miras (Maddi):** Gözle görülebilen, elle tutulabilen eserlerdir. Mimari yapılar (cami, saray), kıyafetler, yemekler, aletler ve tarihi eserler bu gruba girer. **Örnek:** Ayasofya Cami, Türk kahvesi.
        2.  **Soyut Miras (Manevi):** Gelenekler, sözlü anlatımlar, dil, inançlar, halk oyunları ve törenlerdir. **Örnek:** Hacivat ve Karagöz gölge oyunu, Alevi-Bektaşi semahı.
        
        Bu mirasları korumak, bir milleti millet yapan değerleri geleceğe taşımaktır.
        """
    elif "birey ve toplum" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Birey ve Toplum (Rol ve Statü)
        
        Bireyler, toplum içinde doğar ve toplumun bir parçası olur. Toplum içindeki yerimizi ve görevlerimizi **Statü** ve **Rol** kavramları belirler.
        
        **Statü:** Bireyin toplum içindeki pozisyonudur. Statü, kazanılmış (çalışarak elde edilen, Örn: Doktor) veya doğuştan (cinsiyet, ırk, Örn: Evlat) olabilir.
        
        **Rol:** Bireyin sahip olduğu statü gereği sergilemesi beklenen davranışlardır. Her statünün bir rolü vardır.
        * **Örnek:** Yusuf Efe'nin Statüsü: **Öğrenci** $\\rightarrow$ Rolü: **Ders çalışmak, okula gitmek, saygılı olmak.**
        * **Örnek:** Annenizin/Babanızın Statüsü: **Ebeveyn** $\\rightarrow$ Rolü: **Çocuğuna bakmak, eğitim vermek, rehberlik etmek.**
        
        Rollerinizi doğru oynamak, toplumun düzenini sağlamak için önemlidir.
        """
        
    # ===============================================
    # 7. SINIF DİN KÜLTÜRÜ KONULARI (YENİ EKLENEN)
    # ===============================================
    elif "melekler" in topic_lower or "ahiret" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Melekler ve Ahiret İnancı
        
        **Melekler:** Nurdan yaratılmış, gözle görülmeyen, Allah'ın emirlerine itaat eden varlıklardır. Temel görevlerine göre ayrılırlar:
        1.  **Cebrail:** Vahiy meleğidir, peygamberlere emir ve yasakları iletmekle görevlidir.
        2.  **Mikail:** Doğa olaylarını (yağmur, rüzgar, bitkilerin büyümesi) yönetmekle görevlidir.
        3.  **İsrafil:** Sur'a üflemekle görevlidir. İlk üfleyişte kıyamet kopar, ikincide yeniden diriliş başlar.
        4.  **Azrail:** Can almakla görevli olan ölüm meleğidir.
        
        **Ahiret İnancı:** Dünya hayatından sonraki ebedi hayattır. Bu inanç, insanın davranışlarına yön verir, iyiliğe teşvik eder ve sorumluluk bilincini artırır.
        """
    elif "hac" in topic_lower or "kurban" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Hac ve Kurban İbadeti
        
        **Hac:** İslam'ın beş şartından biri olup, imkan bulan Müslümanların Kâbe'yi ve kutsal yerleri ziyaret etmesidir. Hac, belirli zamanlarda (Zilhicce ayında) yapılır. **Umre** ise Hac'dan farklı olarak, yılın herhangi bir zamanında yapılabilir ve vacip değil sünnettir.
        
        **Hac'ın Farzları:**
        1.  **İhrama girmek:** Hac yasaklarına uymak.
        2.  **Kâbe'yi tavaf etmek:** Kâbe etrafında 7 defa dönmek.
        3.  **Arafat'ta vakfe yapmak:** Belirli bir süre Arafat'ta beklemek.
        
        **Kurban:** Allah'a yaklaşmak amacıyla, belirli şartları taşıyan hayvanı usulüne uygun kesmektir. Kurban ibadeti, paylaşmayı ve yardımlaşmayı öğretir.
        """
        
    # ===============================================
    # 7. SINIF İNGİLİZCE KONULARI (YENİ EKLENEN)
    # ===============================================
    elif "appearance" in topic_lower or "personality" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Appearance and Personality (Görünüş ve Kişilik)
        
        **Appearance (Görünüş):** Bir kişinin dış görünüşünü tarif etmek için kullanılır.
        * **Boy/Yapı:** **Tall** (Uzun), **Short** (Kısa), **Slim** (İnce), **Overweight** (Fazla Kilolu).
        * **Saç:** **Straight** (Düz), **Wavy** (Dalgalı), **Curly** (Kıvırcık), **Blonde** (Sarı), **Dark** (Koyu).
        * **Örnek Cümle:** "**She is tall and has long curly hair.**" (O uzundur ve uzun kıvırcık saçı vardır.)
        
        **Personality (Kişilik):** Bir kişinin karakterini ve huylarını tarif etmek için kullanılır.
        * **Pozitif:** **Kind** (Nazik), **Generous** (Cömert), **Funny** (Komik), **Helpful** (Yardımsever), **Ambitious** (Hırslı).
        * **Negatif (Dikkat!):** **Selfish** (Bencil), **Rude** (Kaba), **Stubborn** (İnatçı).
        * **Örnek Cümle:** "**He is usually cheerful, but sometimes he can be stubborn.**" (O genellikle neşelidir, ama bazen inatçı olabilir.)
        """
    elif "sports" in topic_lower or "biographies" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Sports and Biographies (Sporlar ve Biyografiler)
        
        **Sports (Sporlar):** Fiillerle birlikte kullanımı önemlidir:
        * **Play (Oynamak):** Takım sporları ve top oyunları için. $\rightarrow$ **Play** football, **play** volleyball.
        * **Go (Gitmek):** Sonu -ing ile biten sporlar için. $\rightarrow$ **Go** swimming, **go** running.
        * **Do (Yapmak):** Bireysel ve dövüş sporları için. $\rightarrow$ **Do** karate, **do** athletics.
        
        **Biographies (Biyografiler):** Bir kişinin hayat hikayesini anlatan metinlerdir. Bu konularda genellikle **Simple Past Tense (Geçmiş Zaman)** kullanılır.
        * **Örnek (Simple Past):** "He **was born** in 1980." (O 1980'de doğdu.) / "She **won** the championship in 2005." (O 2005'te şampiyonluğu kazandı.)
        """
        
    # ===============================================
    # DİĞER TÜM KONULAR REDDEDİLİR (Sohbet Yasağı)
    # ===============================================
    else:
        response = f"""
        ## ⚠️ Akıl Asistan Uyarısı
        
        **'{topic[:20].upper() + ('...' if len(topic) > 20 else '')}'** şu an için anlatabileceğim konular arasında değildir. 
        
        Ben sadece 7. Sınıf **Matematik, Türkçe Dil Bilgisi, Fen, Sosyal, Din Kültürü ve İngilizce (Appearance/Sports/Personality)** ana konularını **detaylı** anlatmak üzere programlanmış bir öğrenci asistanıyım ve **sohbet özelliğim kapalıdır.**
        """
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic
