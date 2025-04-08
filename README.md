# :rocket: GLOBAL AI HUB AKBANK PYTHON İLE YAPAY ZEKAYA GİRİŞ BOOTCAMP PROJESİ
# 🚇 Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

⚡ Bu projede, Ankara şehrindeki bir metro ağında iki istasyon arasındaki en hızlı rotayı A* algoritması ve en az aktarmalı rotayı BFS (Breadth-First Search) algoritması ile bulan bir simülasyon geliştirmeyi hedefledik. 

# 🧰 Kullanılan Teknoloji ve Kütüphaneler:
- 'defaultdict' varsayılan bir değer tipi belirleyebilme özelliğine sahiptir ve bu simülasyonda metro hatlarını ve istasyon bağlantılarını saklamak için kullanılmıştır.

- 'deque (double-ended queue)', hızlı ekleme ve çıkarma işlemleri yapabilen bir veri yapısıdır. FIFO veya LIFO işlemleri için sıklıkla kullanılmaktadır.

- 'heapq' (Heap Queue - Yığın Kuyruğu) öncelik kuyruğu (priority queue) veya minimum yığın (min-heap) veri yapısını kullanmamızı sağlar. Bu simülasyonda A* algoritmasını uygularken yani en hızlı rotayı hesaplamak için kulllanılmıştır.

- Dict, List, Optional, Tuple veri tiplerini belirtmek için kullanılır. Python'un statik kontrol yapmasını sağlar ve kodu daha okunaklı hale getirir. Bu simülasyonda istasyonları, komşuları ve bağlantıları tutmak için kullanılmıştır.

- 'networkx (nx)' kütüphanesi ağ grafikleri oluşturmak ve analiz etmek için kullanılmıştır.

- 'matplotlib.pyplot (plt)' kütüphanesi grafikleri görselleştirmek için kullanılmaktadır. Bu simülasyonda istasyonları ve bağlantıları modellemek için kullanılmıştır.

# 📊 Kullanılan Algoritmalar:
✅ BFS (Breadth-First Search) bir graf veya ağ üzerindeki en kısa yolu bulmak için kullanılan aradaki adım sayısını (kenar sayısını) minimize eden bir algoritmadır. İlk önce başlangıç düğümünü (node) kuyruğa ekler. Sonra, FIFO mantığı ile komşu düğümleri keşfeder ve kuyruğa ekler. Daha sonra, keşfedilen düğümlerin komşularına gider ve onları da kuyruğa ekler. En son olarak, hedef düğüme ulaşırsa aramayı sonlandırır.

✅ A* algoritması hem en kısa hem de en hızlı yolu bulmaya çalışır. İlk olarak başlangıç düğümünden başlar. Sonra her düğüm için iki maliyeti hesaplar:
g(n): Başlangıçtan o düğüme olan maliyet 
h(n): Hedefe olan tahmini maliyet
f(n) = g(n) + h(n) → Toplam maliyet hesaplanır.
Her adımda en düşük f(n) değerine sahip düğüm işlenir. Son olarak hedefe ulaşılınca durur.

🎯 Bu simülasyonda, en az aktarmalı rotayı bulmak istediğimiz için BFS'i, en hızlı rotayı (dakikaya göre) bulmak istediğimiz için A* kullandık.

# 📝 Örnek Kullanım ve Test Sonuçları
# 🌟 BFS Örneği:
```python
#Graf Yapısı:

A -- B -- C
|    |
D -- E

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B'],
    'D': ['A', 'E'],
    'E': ['B', 'D']
}

def bfs(graph, start):
  visited = set()         #Ziyaret edilen düğümleri takip etmek için boş bir küme oluştur
  queue = [start]    #Kuyruk veri yapısı, başlangıç düğümü ile başlatılır

  #Kuyruk boş olmadığı sürece devam et
  while queue:
    node = queue.pop(0) # Kuyruğun başından bir düğüm çıkar (FIFO - İlk giren ilk çıkar)
    if node not in visited:
      visited.add(node) # Düğümü ziyaret edildi olarak işaretle
      print(node, end=' ')
      #Mevcut düğümün ziyaret edilmemiş tüm komşularını kuyruğa ekle
      for neighbor in graph[node]:
        if neighbor not in visited:
          queue.append(neighbor)  # Düğümü ziyaret edildi olarak işaretle

print("Genişlik Öncelikli Arama Sonucu:")
bfs(graph, 'A')  #BFS'i 'A' düğümünden başlayarak çağır
```

# ÇIKTI: 
```python
Genişlik Öncelikli Arama Sonucu:
A B D C E 
```
# 🌟 A* Örneği:
```python
#Graf Yapısı:
        A
       / \
      1   4
     /     \
    B        D
     \     /
      2   1
       \ /
        C
#A başlangıç noktası, C hedef nokta
# CODE:
import heapq

#Heuristik fonksiyonu (tahmini maliyetler)
def heuristic(node):
    heuristics = {'A': 3, 'B': 2, 'C': 0, 'D': 1}
    return heuristics[node]

#A* algoritması
def a_star(graph, start, goal):
    queue = [(0, start, [start], 0)]  # (f(n), node, path, g_cost)
    visited = set()
    while queue:
        f_cost, node, path, g_cost = heapq.heappop(queue)
        if node == goal:
            return path, g_cost  # Hedefe ulaşıldı, yol ve toplam maliyet döndürülür
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    new_g_cost = g_cost + edge_cost  # Yeni g(n) = mevcut g(n) + kenar maliyeti
                    h_cost = heuristic(neighbor)   # h(n)
                    f_cost = new_g_cost + h_cost    # f(n) = g(n) + h(n)
                    heapq.heappush(queue, (f_cost, neighbor, path + [neighbor], new_g_cost))
    return None, float('inf')  # Hedefe ulaşılamadı

#Graf yapısı (düğüm: [(komşu, maliyet)])
graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('D', 1)],
    'D': [('A', 4), ('C', 1)]
}

#A* algoritmasını çağır
start = 'A'
goal = 'C'
path, total_cost = a_star(graph, start, goal)

#Sonuçları yazdır
print("A* Algoritması Sonucu:")
print("Yol:", " -> ".join(path))
print("Toplam Maliyet:", total_cost)
```
# ÇIKTI:
```python
A* Algoritması Sonucu:
A -> B -> C
Toplam Maliyet: 3
```
# 💡 Projeyi Geliştirme Fikirleri:
Daha detaylı/farklı rotalar arası görselleştirmeler yapılabilir.

Farklı algoritmalar kullanılabilir. Örneğin; en kısa yolu bulmak için Dijkstra, enerji verimliliğinde en optimal rotaları bulmak için Dinamik programlama vs.
