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

Bu projede, kullanıcıların dinleme alışkanlıklarını içeren açık kaynaklı bir müzik veri seti kullanılmıştır. Veri seti aşağıdaki dosyalardan oluşmaktadır:

users.csv – Kullanıcı bilgileri
user_top_artists.csv – Kullanıcıların en çok dinlediği sanatçılar
user_top_albums.csv – Kullanıcıların en çok dinlediği albümler

Veriler, her kullanıcı için dinlenme sayısına (playcount) göre sıralanmıştır. Proje geliştirme sürecinde eğitim süresini kısaltmak amacıyla veri setinin sınırlı bir örneklemi (örneğin 3000 satır) kullanılmıştır. Sistem, final aşamasında daha büyük veri setleriyle yeniden eğitilebilecek şekilde esnek bir yapıda tasarlanmıştır.

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

Veriler kullanıcı bazlı ve sıralı şekilde hazırlanmıştır
Girdi olarak son üç sanatçı / albüm kullanılmıştır
Çıkış olarak bir sonraki sanatçı / albüm tahmin edilmiştir
Eğitim ve test verileri %80 / %20 oranında ayrılmıştır

Model: Logistic Regression

Eğitim işlemi CPU üzerinde gerçekleştirilmiştir. Sanatçı ve albüm önerileri için oluşturulan modeller ayrı ayrı eğitilmiş ve .pkl formatında kaydedilmiştir.

Model Değerlendirilmesi

Model performansı, test veri seti üzerinde doğruluk (accuracy) metriği kullanılarak değerlendirilmiştir. Elde edilen doğruluk değerleri, sınıf sayısının yüksekliği ve verinin sıralı yapısı göz önüne alındığında makul seviyededir.

Bu proje kapsamında temel amaç, yüksek doğruluk elde etmekten ziyade çalışan, anlaşılır ve genişletilebilir bir öneri sistemi geliştirmektir.

Genel Değerlendirme

Geliştirilen sistem, kullanıcıların son dinleme alışkanlıklarına dayalı anlamlı öneriler sunabilmektedir.
Sanatçı ve albüm önerilerinin ayrı modellerle ele alınması, sistemin esnekliğini artırmıştır.
Veri boyutunun artırılması ve daha gelişmiş modellerin kullanılmasıyla performans daha da iyileştirilebilir.
Proje, makine öğrenmesi tabanlı öneri sistemlerinin temel çalışma prensiplerini başarılı bir şekilde yansıtmaktadır.