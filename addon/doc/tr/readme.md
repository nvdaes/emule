# eMule #

*	Yazarlar: Noelia, Chris, Alberto.
*	İndir [kararlı versiyon][1]
*	İndir [geliştirme sürümü][3]

Bu eklenti NVDA ile eMule erişilebilirliğinin geliştirilmesine yardımcı
olur. Ayrıca farklı pencerelerde hareket için ek klavye komutları sağlar ve
eMule ile ilgili faydalı bilgi verir.

Bu eklenti aynı yazar tarafından geliştirilen eMuleNVDASupport adlı
eklentiye dayanılarak geliştirildi. Her ikisin ortak tuş komutlarına ve
benzer özelliklere sahip olduğu için bunu kurmadan önce eskisini
kaldırmalısınız. gerekir.

[EMule] [2] 0.50a test edilmiştir.

## Tuş komutları: ##

*	control+shift+h: odak ve fareyi Ana araç çubuğuna  taşır.
*	kontrol + shift + t: Geçerli pencereyi okur.
*	kontrol + shift + n: Bul penceresinde odağı Ad alanınna taşır.
*	kontrol + shift + p: Arama penceresinde, odağı ve fareyi arama
  parametreleri listesine  veya alan düzenleme seçeneklerine taşır.
*	control+shift+b: Move the focus to the list in the current window. For
  example usable in the Search window, downloads in Transfer window, etc.
*	control+shift+o: Move the focus to read-only edit boxes in the current
  window. For example the IRC received messages, available Servers, etc.
*	kontrol + NVDA + f: Düzenleme imleci bir salt okunur düzenleme kutusunda
  bulunuyorsa, bul iletişim kutusunu açar.
*	kontrol + f3: Daha önce aranan ifadeyi metnin sonraki kısmında arar.
*	kontrol+shift+f3: Daha önce aranan ifadeyi metnin önceki kısmında arar.
*	kontrol + shift + l: Fare ve nesne sunucusunu Mevcut listenin başlıkları
  üzerine taşır.
*	kontrol + shift + q: durum çubuğunda ilk nesneyi okur; son etkinlik
  hakkında bilgi verir.
*	kontrol + shift + w: geçerli sunucu üzerinde dosya ve kullanıcılar
  hakkında bilgi içeren durum çubuğunun ikinci nesnesini okur.
*	kontrol + shift + e: yükleme ve indirme hızıyla ilgili bilgi veren durum
  çubuğunun üçüncü nesnesini okur.
*	kontrol + shift + r: eD2K ve Kad ağ bağlantı raporlarıyla ilgili durum
  çubuğunun dördüncü nesnesini okur.

## Sütunların yönetimi. ##

Bir liste içindeyken, alt + kontrol + yön tuşlarıyla satır ve sütunlar
arasında dolaşabilirsiniz. Eklenti aşağıdaki tuş komutlarını da sağlar:

*	NVDA + kontrol 1-0: ilk 10 sütunu okur.
*	NVDA + shift 1-0: 11-20 sütunları okur.
*	NVDA + shift + C: son okunan sütunun içeriğini panoya kopyalar .

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## 1.2 için Değişiklikler ##
*	 IRC mesajları arasında dolaşılırken, seçilen metin düzgün bildiriliyor.
*	 The keystroke used for moving to the Search results list has been
   generalized to be able to move focus to any available list in the current
   window.
*	 The command used to focus the IRC messages has been generalized to move
   to any read-only edit box, making it possible to review connection
   information in the Servers window.
*	 When moving mouse and focus to the toolbar, in some cases it was
   announced twice. This has been fixed.

## 1.1 Değişiklikler ##
*	 NVDA yardım menüsü altındaki EMule ögesiyle ilgili sorun giderildi.
*	 Kısayollar şimdi NVDA girdi hareketleri iletişim kutusu kullanılarak
   yeniden atanabilir.

## 1.0 Değişiklikler ##
*	 İlk versiyon.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev
