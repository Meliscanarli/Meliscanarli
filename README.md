GlOBAL AI HUB AKBANK PYTHON İLE YAPAY ZEKAYA GİRİŞ BOOTCAMP PROJESİ
Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)
# Bu projede, Ankara şehrindeki bir metro ağında iki istasyon arasındaki A* algoritması ile en hızlı ve BFS (Breadth-First Search) algoritması ile en az aktarmalı rotayı bulan bir simülasyon geliştirmeyi hedefledik. 
'defaultdict' varsayılan bir değer tipi belirleyebilme özelliğine sahiptir ve bu simülasyonda metro hatlarını ve istasyon bağlantılarını saklamak için kullanılmıştır.
'deque (double-ended queue)', hızlı ekleme ve çıkarma işlemleri yapabilen bir veri yapısıdır. FIFO veya LIFO işlemleri için sıklıkla kullanılmaktadır.
'heapq' (Heap Queue - Yığın Kuyruğu) öncelik kuyruğu (priority queue) veya minimum yığın (min-heap) veri yapısını kullanmamızı sağlar. Bu simülasyonda A* algoritmasını uygularken yani en hzılı rotayı hesaplamak için kulllanılmıştır.
Dict, List, Optional, Tuple veri tiplerini belirtmek için kullanılır. Python'un statik kontrol yapmasını sağlar ve kodu daha okunaklı hale getirir. Bu simülasyonda istasyonları, komşuları ve bağlantıları tutmak için kullanılmıştır.
'networkx (nx)' kütüphanesi ağ grafikleri oluşturmak ve analiz etmek için kullanılmaktadır.
'matplotlib.pyplot (plt)' kütüphanesi grafikleri görselleştirmek için kullanılmaktadır. Bu simülasyonda istasyonları ve bağlantıları modellemek için kullanılmıştır.
BFS (Breadth-First Search) bir graf veya ağ üzerindeki en kısa yolu bulmak için kullanılan aradaki adım sayısını (kenar sayısını) minimize eden bir algoritmadır. İlk önce başlangıç düğümünü (node) kuyruğa ekler. Sonra, FIFO mantığı ile komşu düğümleri keşfeder ve kuyruğa ekler. Daha sonra, keşfedilen düğümlerin komşularına gider ve onları da kuyruğa ekler. En son olarak, hedef düğüme ulaşırsa aramayı sonlandırır.
A* algoritması hem en kısa hem de en hızlı yolu bulmaya çalışır. İlk olarak başlangıç düğümünden başlar. Sonra her düğüm için iki maliyeti hesaplar:
g(n): Başlangıçtan o düğüme olan maliyet 
h(n): Hedefe olan tahmini maliyet
f(n) = g(n) + h(n) → Toplam maliyet hesaplanır.
Her adımda en düşük f(n) değerine sahip düğüm işlenir. Son olarak hedefe ulaşılınca durur.
Bu simülasyonda, en az aktarmalı rotayı bulmak istediğimiz için BFS'i, en hızlı rotayı (dakikaya göre) bulmak istediğimiz için A* kullandık.
Belki benim yapmaya çalıştığım gibi daha detaylı/farklı rotalar arası görselleştirmeler yapılabilir.
