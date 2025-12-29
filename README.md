Derin Öğrenme ile Müzik Öneri Sistemi


Proje Konusu ve Seçilme Gerekçesi

Dijital müzik platformlarında kullanıcıların dinleme alışkanlıklarına uygun içeriklerin önerilmesi, kullanıcı memnuniyeti ve platform etkileşimi açısından kritik bir öneme sahiptir. Kullanıcıların ilgi alanlarına uygun sanatçı ve albümlerin otomatik olarak önerilmesi, veri analizi ve makine öğrenmesi tekniklerinin yaygın olarak uygulandığı temel problemlerden biridir.

Bu projede, kullanıcıların geçmiş dinleme verileri kullanılarak, son dinlenen sanatçı ve albümlere dayalı olarak yeni sanatçı ve albüm önerileri sunan derin öğrenme tabanlı LSTM (Long Short-Term Memory) modelleri geliştirilmiştir. LSTM, sıralı veri üzerinde öğrenme yeteneğine sahip olması nedeniyle kullanıcıların son dinleme alışkanlıklarını analiz edip bir sonraki olası tercihi tahmin etmede tercih edilmiştir. Bu yaklaşım, geleneksel makine öğrenmesi yöntemlerinin aksine, zaman içindeki bağımlılıkları yakalayabilme ve uzun dizilerle çalışabilme avantajı sunar.

Proje konusu; gerçek dünya uygulamalarına doğrudan karşılık gelmesi, veri bilimi ve derin öğrenme yöntemlerinin uygulanmasına uygun olması ve kullanıcı davranışlarını modelleme açısından öğretici nitelik taşıması nedeniyle tercih edilmiştir.
Daha Önce Yapılan Çalışmalar

Daha Önce Yapılan Çalışmalar

Literatürde müzik öneri sistemleri için farklı yaklaşımlar geliştirilmiştir. Geleneksel yöntemlerde kullanıcı–öğe etkileşimlerine dayalı işbirlikçi filtreleme (collaborative filtering), içerik tabanlı öneri sistemleri ve kullanıcı–öğe matrisleri yaygın olarak kullanılmaktadır.

Son yıllarda, kullanıcı davranışlarının zaman içindeki sıralı yapısını dikkate alan makine öğrenmesi ve derin öğrenme tabanlı yaklaşımlar ön plana çıkmıştır. Kullanıcının son dinlediği içeriklerden yola çıkarak bir sonraki olası tercihin tahmin edilmesi, modern öneri sistemlerinde sıkça kullanılan etkili bir yöntemdir. Bu bağlamda, LSTM gibi sıralı veri modelleri, öneri sistemlerinde kullanıcı davranışlarını anlamak ve tahmin etmek için akademik ve endüstriyel olarak tercih edilmektedir.

Literatürde müzik öneri sistemleri için farklı yaklaşımlar geliştirilmiştir:

Geleneksel Yöntemler: Kullanıcı-öğe etkileşimlerine dayalı işbirlikçi filtreleme (collaborative filtering), içerik tabanlı öneri sistemleri ve kullanıcı-öğe matrisleri.

Makine Öğrenmesi Tabanlı Yaklaşımlar: Lojistik regresyon, karar ağaçları, sıralı (sequence-based) tahmin modelleri.

Derin Öğrenme Tabanlı Yaklaşımlar: Kullanıcının geçmiş dinleme sıralarını dikkate alan RNN ve LSTM tabanlı modeller. Bu modeller, uzun vadeli bağımlılıkları öğrenerek kullanıcının sonraki tercihlerine dair daha isabetli tahminler yapabilir.


İlgili Alanın Önemi

Müzik öneri sistemleri;

Kullanıcı deneyimini iyileştirme,

Platformda geçirilen süreyi artırma,

Kişiselleştirilmiş içerik sunma

gibi açılardan dijital müzik platformları için kritik bir rol oynamaktadır.

LSTM tabanlı derin öğrenme modelleri, geleneksel kural tabanlı veya temel makine öğrenmesi yöntemlerine kıyasla daha esnek ve ölçeklenebilir çözümler sunar. Kullanıcıların zaman içinde değişen tercihlerini modelleyebilmesi, gerçek kullanıcı davranışlarını daha iyi yansıtan öneriler üretmesini sağlar.

Veri Setinin Belirlenmesi

Bu projede, kullanıcıların dinleme alışkanlıklarını içeren açık kaynaklı bir müzik veri seti kullanılmıştır. Veri seti, kullanıcıların geçmiş dinleme davranışlarını yansıtan etiketli verilerden oluşmakta olup aşağıdaki dosyaları içerir:

users.csv – Kullanıcı bilgileri

user_id: Her kullanıcı için benzersiz kimlik

Ek bilgiler (opsiyonel, ör. yaş, ülke vb.)

user_top_artists.csv – Kullanıcıların en çok dinlediği sanatçılar

user_id: Kullanıcı kimliği

artist_name: Sanatçının adı

playcount: Kullanıcının bu sanatçıyı dinleme sayısı

user_top_albums.csv – Kullanıcıların en çok dinlediği albümler

user_id: Kullanıcı kimliği

album_name: Albümün adı

playcount: Kullanıcının bu albümü dinleme sayısı

Veriler, kullanıcı bazında playcount değerine göre sıralanmıştır, böylece en çok dinlenen içerikler öne çıkarılmıştır. Proje geliştirme sürecinde eğitim süresini kısaltmak amacıyla veri setinin sınırlı bir örneklemi (örneğin 5.000 satır) kullanılmıştır. Sistemin final aşamasında, daha büyük veri setleri ile yeniden eğitilmesi mümkündür.

Bu hazırlık, modelin kullanıcıların son 3 tercihini girdi olarak alıp bir sonraki olası tercihi tahmin etmesine olanak sağlamaktadır.
https://www.kaggle.com/datasets/gabrielkahen/music-listening-data-500k-users/suggestions

Uygulanacak Yöntem / Algoritma / Yaklaşımın Seçim Gerekçesi

Bu projede öneri problemi, sequence-based (sıralı) çok sınıflı sınıflandırma olarak ele alınmıştır. Kullanıcının son dinlediği üç sanatçı veya albüm, modelin girdi verisi olarak kullanılmıştır ve çıktısı bir sonraki olası tercihtir.

LSTM (Long Short-Term Memory), sıralı veri üzerindeki bağımlılıkları öğrenebilen bir RNN türevidir. Bu modelin tercih edilme gerekçeleri:

Uzun süreli kullanıcı davranışlarını yakalayabilme

Sıralı veri üzerinde etkili tahmin

Overfitting’e karşı görece dayanıklı yapı

Eğitim ve çıkarım süresinin makul olması

Modelin mimarisi aşağıdaki gibi yapılandırılmıştır:

Embedding katmanı: Kullanıcıların sanatçı/album ID’lerini yoğun vektör temsiline dönüştürür.

LSTM katmanı (64 unit): Zaman içindeki bağımlılıkları öğrenir.

Dense + Softmax: Çok sınıflı tahmin sağlar.

Model Eğitimi

Veri ön işleme aşamasında kullanıcıların dinleme geçmişleri sıralı şekilde hazırlanmıştır. Her bir kullanıcı için son 3 sanatçı ve albüm bilgisi, modelin girdi verisi (X) olarak belirlenmiş, çıktılar (y) bir sonraki olası tercih olacak şekilde düzenlenmiştir.

Eğitim ve test veri setleri %80 / %20 oranında ayrılmıştır. Bu sayede model, daha önce görmediği kullanıcı davranışlarına karşı tahmin yeteneği kazanmıştır.

Hiperparametreler ve eğitim ayarları:

Epoch: 5 (küçük veri seti için hızlı eğitim)

Batch size: 32

Validation split: 0.1 (erken overfitting kontrolü)

Loss: Categorical Crossentropy

Optimizer: Adam

Sanatçı ve albüm önerileri için iki ayrı LSTM modeli oluşturulmuş ve her biri bağımsız olarak eğitilmiştir. Model çıktıları .h5 formatında kaydedilmiş ve encoderlar .pkl olarak saklanmıştır.

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

Model performansı Top-1 ve Top-5 doğruluk (accuracy) metrikleri ile ölçülmüştür. Elde edilen değerler, veri setinin yüksek sınıf sayısı ve sıralı yapısı göz önüne alındığında makul seviyededir.

Ek analizler için:

Top-N doğruluk: Tahmin edilen ilk 5 öneriden kaçının doğru olduğu

Sınıf bazlı performans: Hangi sanatçı/album türlerinin daha zor tahmin edildiği

Yanlış pozitif/negatif analizi

Bu değerlendirmeler, modelin gerçek kullanıcı senaryolarında güvenilirliğini anlamak için önemlidir.

LSTM modeli, veri setindeki yüksek sınıf sayısı ve sıralı yapıyı öğrenerek makul seviyede doğruluk elde etmiştir.

Kullanıcı bazlı sequence yapısı sayesinde, model sıradaki olası tercihleri doğru şekilde tahmin edebilmektedir.

Ek olarak, top-N öneriler ve yanlış pozitif/negatif oranları üzerinden sistem güvenilirliği analiz edilebilir.

Genel Değerlendirme

Geliştirilen LSTM tabanlı müzik öneri sistemi, kullanıcıların geçmiş dinleme davranışlarına dayalı anlamlı ve tutarlı öneriler sunabilmektedir. Kullanıcının son üç tercihi temel alınarak yapılan tahminler, sistemin kişiselleştirilmiş öneriler üretme kapasitesini göstermektedir.

Sanatçı ve albüm önerilerinin ayrı modellerle ele alınması, sistemin esnekliğini artırmakta ve farklı veri kaynaklarından bağımsız öneri üretilebilmesine olanak sağlamaktadır. Bu yapı, gelecekte model geliştirme veya veri seti değişikliklerinde adaptasyonu kolaylaştırmaktadır.

Sistemin performansı, veri boyutu ve model kapasitesi ile doğrudan ilişkilidir. Veri setinin genişletilmesi, daha fazla kullanıcı davranışının modele dahil edilmesini sağlayarak öneri kalitesini artırabilir. Ayrıca, daha derin LSTM katmanları veya attention mekanizmaları eklenerek modelin sıralı tahmin performansı iyileştirilebilir.

Bu proje, LSTM temelli öneri sistemlerinin temel çalışma prensiplerini başarılı bir şekilde yansıtmaktadır ve akademik/uygulamalı açıdan değerlendirildiğinde, gerçek dünya dijital müzik platformlarında kullanıcı deneyimini iyileştirmek için sağlam bir altyapı sunmaktadır.
