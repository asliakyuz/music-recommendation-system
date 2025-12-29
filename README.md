Derin Öğrenme ile Müzik Öneri Sistemi


Proje Konusu ve Seçilme Gerekçesi

Dijital müzik platformlarında kullanıcıların dinleme alışkanlıklarına uygun içeriklerin önerilmesi, kullanıcı memnuniyeti ve platform etkileşimi açısından kritik bir öneme sahiptir. Kullanıcıların ilgi alanlarına uygun sanatçı ve albümlerin otomatik olarak önerilmesi, veri analizi ve makine öğrenmesi tekniklerinin yaygın olarak uygulandığı temel problemlerden biridir.

Bu projede, kullanıcıların geçmiş dinleme verileri kullanılarak, son dinlenen sanatçı ve albümlere dayalı olarak yeni sanatçı ve albüm önerileri sunan derin öğrenme tabanlı LSTM (Long Short-Term Memory) modelleri geliştirilmiştir. LSTM, sıralı veri üzerinde öğrenme yeteneğine sahip olması nedeniyle kullanıcıların son dinleme alışkanlıklarını analiz edip bir sonraki olası tercihi tahmin etmede tercih edilmiştir. Bu yaklaşım, geleneksel makine öğrenmesi yöntemlerinin aksine, zaman içindeki bağımlılıkları yakalayabilme ve uzun dizilerle çalışabilme avantajı sunar.

Proje konusu; gerçek dünya uygulamalarına doğrudan karşılık gelmesi, veri bilimi ve derin öğrenme yöntemlerinin uygulanmasına uygun olması ve kullanıcı davranışlarını modelleme açısından öğretici nitelik taşıması nedeniyle tercih edilmiştir.
Daha Önce Yapılan Çalışmalar

Literatürde müzik öneri sistemleri için farklı yaklaşımlar geliştirilmiştir:

Geleneksel Yöntemler: Kullanıcı-öğe etkileşimlerine dayalı işbirlikçi filtreleme (collaborative filtering), içerik tabanlı öneri sistemleri ve kullanıcı-öğe matrisleri.

Makine Öğrenmesi Tabanlı Yaklaşımlar: Lojistik regresyon, karar ağaçları, sıralı (sequence-based) tahmin modelleri.

Derin Öğrenme Tabanlı Yaklaşımlar: Kullanıcının geçmiş dinleme sıralarını dikkate alan RNN ve LSTM tabanlı modeller. Bu modeller, uzun vadeli bağımlılıkları öğrenerek kullanıcının sonraki tercihlerine dair daha isabetli tahminler yapabilir.

İlgili Alanın Önemi

Müzik öneri sistemleri:

Kullanıcı deneyimini iyileştirir,

Platformda geçirilen süreyi artırır,

Kişiselleştirilmiş içerik sunar.

Derin öğrenme tabanlı modeller, kural tabanlı ve klasik makine öğrenmesi yöntemlerine kıyasla:

Uzun sıralı bağımlılıkları öğrenebilir,

Kullanıcı davranışlarını daha doğru modelleyebilir,

Veri miktarı arttıkça performansını koruyabilir.

Bu nedenle geliştirilen sistemler, modern dijital içerik servislerinin temel bileşenlerinden biri hâline gelmiştir.

Veri Setinin Belirlenmesi

Bu projede, kullanıcıların dinleme alışkanlıklarını içeren açık kaynaklı bir müzik veri seti kullanılmıştır. Veri seti, kullanıcıların geçmiş dinleme davranışlarını yansıtan etiketli verilerden oluşmakta ve aşağıdaki dosyaları içermektedir:

users.csv: Kullanıcı bilgileri (user_id: benzersiz kullanıcı kimliği, opsiyonel ek bilgiler: yaş, ülke vb.)

user_top_artists.csv: Kullanıcıların en çok dinlediği sanatçılar (user_id, artist_name, playcount)

user_top_albums.csv: Kullanıcıların en çok dinlediği albümler (user_id, album_name, playcount)

Veri Hazırlığı ve Kullanım:

Tüm veriler, kullanıcı bazında playcount değerine göre sıralanmıştır.

Kullanıcının son üç tercihi girdi olarak alınmış ve bir sonraki olası tercihi tahmin edecek şekilde LSTM için sequence verisi oluşturulmuştur.

Eğitim süresini yönetebilmek amacıyla başlangıçta veri seti sınırlı bir örneklemle (ör. 10.000 satır) kullanılmıştır.
https://www.kaggle.com/datasets/gabrielkahen/music-listening-data-500k-users/suggestions

Uygulanacak Yöntem / Algoritma / Yaklaşımın Seçim Gerekçesi

Bu projede öneri problemi, sequence-based çok sınıflı sınıflandırma problemi olarak ele alınmıştır. Amaç, kullanıcının son üç sanatçı veya albümüne bakarak bir sonraki olası tercihi tahmin etmektir.

Seçilen yöntem: LSTM (Long Short-Term Memory) tabanlı derin öğrenme modeli

Seçim Gerekçeleri:

Kullanıcı davranışlarındaki sıralı bağımlılıkları öğrenme yeteneği

Uzun vadeli bağımlılıkları modelleyebilme kapasitesi

Geniş veri setlerinde iyi performans ve genelleme yeteneği

Akademik projeler için anlaşılabilir ve yeniden kullanılabilir model mimarisi

Model Eğitimi

Veri Ön İşleme ve Sequence Oluşturma:

Kullanıcı bazlı sıralı veri oluşturuldu.

Son üç tercihe göre X (girdi) ve bir sonraki tercih y (çıktı) verisi hazırlanmıştır.

Sequence uzunluğu SEQ_LEN=3 olarak belirlenmiştir.

Eğitim/Doğrulama Ayrımı:

Eğitim ve test veri setleri %80 / %20 oranında ayrılmıştır.

Bu, modelin daha önce görmediği kullanıcı davranışlarını tahmin etme yeteneğini artırır.

LSTM Modeli:

Embedding Katmanı: Kategorik veriyi düşük boyutlu sürekli vektörlere dönüştürür.

LSTM Katmanı: Kullanıcıların sıralı dinleme davranışlarını öğrenir.

Dense + Softmax Katmanı: Olası bir sonraki tercih için olasılık dağılımı üretir.

Sanatçı ve albüm önerileri için ayrı modeller eğitilmiştir.

Model çıktıları .h5 formatında kaydedilmiştir; encoderlar ise .pkl formatında saklanmıştır.

Hiperparametreler:

Epoch: 5

Batch size: 32

LSTM birimi: 64

Embedding boyutu: 50

Model Değerlendirilmesi

Test veri seti üzerinde doğruluk (accuracy) ve top-5 öneri doğruluğu ile performans değerlendirilmiştir.

LSTM modeli, veri setindeki yüksek sınıf sayısı ve sıralı yapıyı öğrenerek makul seviyede doğruluk elde etmiştir.

Kullanıcı bazlı sequence yapısı sayesinde, model sıradaki olası tercihleri doğru şekilde tahmin edebilmektedir.

Ek olarak, top-N öneriler ve yanlış pozitif/negatif oranları üzerinden sistem güvenilirliği analiz edilebilir.

Genel Değerlendirme

Geliştirilen LSTM tabanlı müzik öneri sistemi, kullanıcıların geçmiş dinleme davranışlarına dayalı anlamlı ve tutarlı öneriler sunabilmektedir.

Son üç tercihe dayalı tahminler, sistemin kişiselleştirilmiş öneri üretme kapasitesini göstermektedir.

Sanatçı ve albüm önerilerinin ayrı modellerle ele alınması, sistemin esnekliğini artırmakta ve farklı veri kaynaklarından bağımsız olarak öneri üretilebilmesini sağlamaktadır.

Veri setinin genişletilmesi ve daha derin LSTM/RNN katmanlarının kullanılmasıyla, özellikle top-N öneri doğruluğu ve uzun vadeli kullanıcı davranış tahminleri geliştirilebilir.

Bu proje, derin öğrenme temelli öneri sistemlerinin temel prensiplerini başarılı bir şekilde yansıtarak, akademik ve pratik açıdan uygulanabilir bir örnek sunmaktadır.
