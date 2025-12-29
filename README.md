Derin Öğrenme ile Müzik Öneri Sistemi

Proje Konusu ve Seçilme Gerekçesi

Dijital müzik platformlarında kullanıcıların dinleme alışkanlıklarına uygun içeriklerin önerilmesi, kullanıcı memnuniyeti ve platform etkileşimi açısından büyük önem taşımaktadır. Kullanıcıların ilgi alanlarına uygun sanatçı ve albümlerin otomatik olarak önerilmesi, veri analizi ve makine öğrenmesi tekniklerinin yaygın olarak uygulandığı temel problemlerden biridir.

Bu projede, kullanıcıların geçmiş dinleme verileri kullanılarak, son dinlenen sanatçı ve albümlere dayalı yeni sanatçı ve albüm önerileri sunan makine öğrenmesi tabanlı bir öneri sistemi geliştirilmiştir.

Proje konusu; gerçek dünya uygulamalarına doğrudan karşılık gelmesi, veri bilimi ve makine öğrenmesi yöntemlerinin uygulanmasına uygun olması ve kullanıcı davranışlarını modelleme açısından öğretici nitelik taşıması nedeniyle tercih edilmiştir.

Daha Önce Yapılan Çalışmalar

Literatürde müzik öneri sistemleri için farklı yaklaşımlar geliştirilmiştir. Geleneksel yöntemlerde kullanıcı–öğe etkileşimlerine dayalı işbirlikçi filtreleme (collaborative filtering), içerik tabanlı öneri sistemleri ve kullanıcı–öğe matrisleri yaygın olarak kullanılmaktadır.

Son yıllarda ise kullanıcı davranışlarının zaman içindeki sıralı yapısını dikkate alan makine öğrenmesi ve derin öğrenme tabanlı yaklaşımlar ön plana çıkmıştır. Kullanıcının son dinlediği içeriklerden yola çıkarak bir sonraki olası tercihin tahmin edilmesi, modern öneri sistemlerinde sıkça kullanılan etkili bir yöntemdir.

İlgili Alanın Önemi

Müzik öneri sistemleri;
Kullanıcı deneyimini iyileştirme
Platformda geçirilen süreyi artırma
Kişiselleştirilmiş içerik sunma
gibi açılardan dijital müzik platformları için kritik bir rol oynamaktadır.

Makine öğrenmesi tabanlı öneri sistemleri, kural tabanlı yaklaşımlara kıyasla daha esnek, ölçeklenebilir ve gerçek kullanıcı davranışlarını daha iyi yansıtan çözümler sunmaktadır. Bu nedenle geliştirilen sistemler, dijital içerik servislerinin temel bileşenlerinden biri haline gelmiştir.

Veri Setinin Belirlenmesi

Bu projede, kullanıcıların dinleme alışkanlıklarını içeren açık kaynaklı bir müzik veri seti kullanılmıştır. Veri seti, kullanıcıların geçmiş dinleme davranışlarını yansıtan etiketli verilerden oluşmaktadır ve aşağıdaki dosyaları içerir:

users.csv – Kullanıcı bilgileri
user_id: Her kullanıcı için benzersiz kimlik
Ek bilgiler (opsiyonel, örneğin yaş, ülke vb.)
user_top_artists.csv – Kullanıcıların en çok dinlediği sanatçılar
userid: Kullanıcı kimliği
artist_name: Sanatçının adı
playcount: Kullanıcının bu sanatçıyı dinleme sayısı
user_top_albums.csv – Kullanıcıların en çok dinlediği albümler
user_id: Kullanıcı kimliği
album_name: Albümün adı
playcount: Kullanıcının bu albümü dinleme sayısı

Veri Hazırlığı ve Kullanım
Tüm veriler, kullanıcı bazında playcount değerine göre sıralanmıştır. Böylece en çok dinlenen içerikler öne çıkarılmıştır.
Proje geliştirme sürecinde eğitim süresini kısaltmak amacıyla veri setinin sınırlı bir örneklemi (örneğin 3.000 satır) kullanılmıştır.
Sistemin final aşamasında, daha büyük veri setleri ile yeniden eğitilmesi mümkündür.
Veri setinin bu şekilde hazırlanması, modelin kullanıcıların son 3 tercihini girdi olarak alıp bir sonraki olası tercihi tahmin etmesine olanak sağlar.
Seçilme nedenleri: Açık erişimli olması, kullanıcı bazlı sıralı veriler içermesi ve öneri sistemi problemine uygun yapıda olmasıdır.

veri setinin linki:
https://www.kaggle.com/datasets/gabrielkahen/music-listening-data-500k-users/suggestions

Uygulanacak Yöntem / Algoritma / Yaklaşımın Seçim Gerekçesi

Bu projede öneri problemi, çok sınıflı sınıflandırma (multi-class classification) problemi olarak ele alınmıştır. Amaç, kullanıcının son dinlediği üç sanatçıya veya albüme bakarak bir sonraki olası tercihin tahmin edilmesidir.

Literatürde Kullanılan Yöntemler

Geleneksel Öneri Sistemleri
Collaborative Filtering
Content-Based Filtering
Matris faktörizasyonu
Makine Öğrenmesi Tabanlı Yaklaşımlar
Lojistik Regresyon
Sıralı (sequence-based) tahmin modelleri
Seçilen Yöntem: Lojistik Regresyon (Sequence-Based Yaklaşım)

Bu projede, kullanıcı bazlı sıralı dinleme verileri kullanılarak Logistic Regression modeli tercih edilmiştir.

Bu yöntemin seçilme nedenleri:

Basit ve anlaşılır bir yapıya sahip olması
Küçük ve orta ölçekli veri setleri için uygun olması
Eğitim süresinin kısa olması
Akademik projeler için yorumlanabilir sonuçlar sunması
Sanatçı ve albüm önerileri için iki ayrı model eğitilmiştir. Her model, kullanıcının son üç tercihini girdi olarak alarak bir sonraki olası tercihi tahmin etmektedir.

Model Eğitimi

Veri ön işleme aşamasında, kullanıcıların dinleme geçmişleri sıralı şekilde hazırlanmıştır. Her bir kullanıcı için son üç dinlenen sanatçı ve albüm bilgisi, modelin girdi verisi (X) olarak belirlenmiş, çıktılar (y) ise bir sonraki olası tercih olacak şekilde düzenlenmiştir. Bu yapı, sequence-based (sıralı) tahmin yaklaşımının uygulanabilmesini sağlamaktadır.

Eğitim ve test veri setleri, modelin performansını tarafsız bir şekilde değerlendirebilmek amacıyla %80 / %20 oranında ayrılmıştır. Bu sayede model, yeni ve daha önce görmediği kullanıcı davranışlarına karşı tahmin yeteneği kazanmıştır.

Sanatçı ve albüm önerileri için iki ayrı Logistic Regression modeli oluşturulmuş ve her biri bağımsız olarak eğitilmiştir. Eğitim işlemi CPU üzerinde gerçekleştirilmiş olup, modelin çıktıları .pkl formatında kaydedilmiştir. Bu yaklaşım, modeli daha taşınabilir ve yeniden kullanılabilir hale getirmektedir.

Logistic Regression algoritması, çok sınıflı sınıflandırma (multi-class classification) problemine uygun olarak seçilmiş, küçük ve orta ölçekli veri setleri üzerinde hızlı eğitim imkanı sunmuş ve akademik projeler için yorumlanabilir sonuçlar sağlamıştır. Ayrıca, sequence tabanlı yapı sayesinde kullanıcıların geçmiş davranışlarından yola çıkarak bir sonraki tercihi tahmin edebilme kapasitesi kazanılmıştır.

Veriler kullanıcı bazlı ve sıralı şekilde hazırlanmıştır
Girdi olarak son üç sanatçı / albüm kullanılmıştır
Çıkış olarak bir sonraki sanatçı / albüm tahmin edilmiştir
Eğitim ve test verileri %80 / %20 oranında ayrılmıştır

Model: Logistic Regression

Eğitim işlemi CPU üzerinde gerçekleştirilmiştir. Sanatçı ve albüm önerileri için oluşturulan modeller ayrı ayrı eğitilmiş ve .pkl formatında kaydedilmiştir.

Model Değerlendirilmesi

Model performansı, test veri seti üzerinde doğruluk (accuracy) metriği kullanılarak ölçülmüştür. Elde edilen doğruluk değerleri, veri setinin yüksek sınıf sayısı ve sıralı yapısı göz önüne alındığında makul seviyededir. Bu değerlendirme, modelin genel öneri performansını anlamak için temel bir göstergedir.

Ek olarak, modelin sınıf bazlı tahmin başarısı incelenebilir; örneğin top-N öneriler ve yanlış pozitif/negatif oranları üzerinden analiz yapılabilir. Bu tür analizler, sistemin gerçek kullanıcı senaryolarında ne kadar güvenilir sonuçlar üretebileceğini ortaya koymaktadır.

Bu proje kapsamında, temel amaç yüksek doğruluk elde etmekten ziyade çalışan, anlaşılır ve genişletilebilir bir öneri sistemi geliştirmek olmuştur. Kullanılan sequence-based Logistic Regression modeli, sistemin esnekliğini koruyarak, veri boyutu artırıldığında veya farklı modeller denendiğinde kolayca güncellenebilir bir altyapı sunmaktadır.

Genel Değerlendirme

Geliştirilen müzik öneri sistemi, kullanıcıların geçmiş dinleme davranışlarına dayalı olarak anlamlı ve tutarlı öneriler sunabilmektedir. Kullanıcının son üç tercihi temel alınarak yapılan tahminler, sistemin kişiselleştirilmiş öneriler üretme kapasitesini göstermektedir.

Sanatçı ve albüm önerilerinin ayrı modellerle ele alınması, sistemin esnekliğini artırmakta ve farklı veri kaynaklarından bağımsız olarak öneri üretilebilmesine olanak sağlamaktadır. Bu ayrım, gelecekte model geliştirme veya veri seti değişikliklerinde adaptasyonu kolaylaştırmaktadır.

Sistemin performansı, veri boyutu ve model kapasitesi ile doğrudan ilişkilidir. Veri setinin genişletilmesi, daha fazla kullanıcı davranışının sisteme dahil edilmesini sağlayarak öneri kalitesini artırabilir. Ayrıca, daha gelişmiş makine öğrenmesi ve derin öğrenme modellerinin kullanılmasıyla, özellikle kullanıcıların sıra tabanlı tercihlerini daha doğru tahmin edebilen, top-N öneri doğruluk oranı yüksek bir sistem elde edilebilir.

Bu proje, makine öğrenmesi temelli öneri sistemlerinin temel çalışma prensiplerini başarılı bir şekilde yansıtmakta ve aynı zamanda akademik ve pratik açıdan uygulanabilir bir örnek sunmaktadır. Sistem, hem esnekliği hem de genişletilebilirliği sayesinde, gerçek dünya dijital müzik platformlarında kullanıcı deneyimini iyileştirmek için temel bir altyapı sağlayabilir.
