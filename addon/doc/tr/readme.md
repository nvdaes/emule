# eMule #

*	Yazarlar: Noelia, Chris, Alberto.

Bu eklenti eMule'un nVDA ile erişilebilirliğini artırmaya yardımcı olur.
Ayrıca farklı pencerelerde hareket etmek için ek klavye komutları sağlar ve eMule hakkında Faydalı bilgiler verir.

Aynı yazar tarafından geliştirilen eMuleNVDASupport eklentisine dayanmaktadır. Her ikisinin de ortak tuş vuruşları ve özellikleri olduğundan, bunu kullanmak için eski eklentiyi kaldırmalısınız.

[eMule][1] 0.50a ve 70b'de test edilmiştir.

## Tuş Komutları: ##

*	kontrol+shift+h: Odağı ve fareyi ana araç çubuğuna taşır.
*	kontrol+shift+t: Geçerli pencereyi okur.
*	kontrol+shift+n: Odağı Bul penceresindeki Ad alanına taşır.
*	kontrol+shift+p: Arama penceresinde odağı ve fareyi arama parametreleri listesine veya alan seçeneklerini düzenlemeye taşır.
*	kontrol+shift+b: Odağı geçerli penceredeki listeye taşır. Örneğin Arama penceresinde, Aktarım penceresindeki indirmelerde vb. kullanılabilir.
*	kontrol+shift+o: Odağı geçerli penceredeki salt okunur düzenleme kutularına taşır. Örneğin IRC'nin aldığı mesajlar, mevcut Sunucular vb.
*	kontrol+NVDA+f: İmleç salt okunur bir düzenleme kutusunda bulunuyorsa, NVDA'da mevcut olan metni aramak için komutları kullanmak üzere bir bulma iletişim kutusu açar.
*	kontrol+shift+l: Gezgin nesnesini ve fareyi geçerli listenin başlıklarına taşır.
*	kontrol+shift+q: Durum çubuğundaki ilk nesneyi okur; son etkinlikler hakkında bilgi sağlar.
*	kontrol+shift+w: Durum çubuğunun ikinci nesnesini okur; Geçerli sunucudaki dosyalar ve kullanıcılar hakkında bilgi içerir.
*	kontrol+shift+e: Durum çubuğunun üçüncü nesnesini okur; Yükleme/İndirme hızını bilmek faydalıdır.
*	kontrol+shift+r: Durum çubuğunun dördüncü nesnesini okur; eD2K ve Kad ağının bağlanmasına ilişkin raporlar.
* Atanmamış: Kaydırıcıları okumak için alternatif bir yaklaşımın kullanımını açıp kapatır.

## Sütunları yönetme. ##

Liste içindeyken, Alt+Kontrol+Ok tuşlarını kullanarak imleci satırlar ve sütunlar arasında hareket ettirebilirsiniz.
Bu Eklentide aşağıdaki tuş komutları da mevcuttur:

*	nvda+Kontrol+1-0: İlk 10 sütunu okur.
*	nvda+shift+1-0: 11'den 20'ye kadar olan sütunları okur.
*	nvda+shift+C: Son okunan sütunun içeriğini panoya kopyalar.


## 20.0.0 için değişiklikler
* Bu eklentinin yazarlarından biri olan Alberto Buffolino tarafından geliştirilen [labelAutofinderCore projesi](https://github.com/ABuffEr/labelAutofinderCore) sayesinde bazı düzenleme kutuları ve kaydırıcılar etiketlenmiştir.
* Kaydırıcıları okumak için alternatif bir yaklaşımın kullanımını (varsayılan olarak kapalı) değiştirmek için bir komut (atanmamış) eklenmiştir.

## 7.0 için değişiklikler
* NVDA 2023.1 ile uyumludur.

## 6.0 Sürümü İçin Değişiklikler
*	NVDA 2022.1 veya üzerini gerektirir.

## 5.0 Sürümü İçin Değişiklikler
*	NVDA 2021.1 ile uyumludur.

## 4.0 Sürümü İçin Değişiklikler ##
*	NVDA 2019.3 veya üzerini gerektirir.

## 3.0 Sürümü İçin Değişiklikler ##
*	 Salt okunur düzenleme kutularında metin aramak için bulma iletişim kutusunu etkinleştirmek amacıyla nvda+Kontrol+f gibi bulma iletişim kutusu kullanılabilir.

## 2.0 Sürümü İçin Değişiklikler ##
*	 Eklenti yardımına Eklenti Mağazası'ndan ulaşılabilir.

## 1.2 Sürümü İçin Değişiklikler ##
*	 IRC mesajlarına geçerken seçilen metin düzgün şekilde seslendirilir.
*	 Arama sonuçları listesine gitmek için kullanılan tuş vuruşu, odağı geçerli penceredeki mevcut herhangi bir listeye taşıyabilecek şekilde genelleştirildi.
*	 IRC mesajlarına odaklanmak için kullanılan komut, herhangi bir salt okunur düzenleme kutusuna taşınacak şekilde genelleştirildi ve Sunucular penceresinde bağlantı bilgilerinin gözden geçirilmesini mümkün kılındı.
*	 Fareyi hareket ettirip araç çubuğuna odakladığınızda bazı durumlarda iki kez duyuruluyordu. Bu düzeltildi.

## 1.1 Sürümü İçin Değişiklikler ##
*	 NVDA'nın yardım menüsündeki eMule öğesinde, kullanıcı yapılandırma klasörünün adında Latin olmayan karakterler bulunduğunda ortaya çıkan hata düzeltildi.
*	 Artık kısayollar, NVDA Girdi Hareketleri iletişim kutusu kullanılarak yeniden atanabiliyor.

## 1.0 Sürümü İçin Değişiklikler ##
*	 İlk sürüm.

[1]: http://www.emule-project.net
