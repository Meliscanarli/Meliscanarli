from collections import defaultdict, deque
import heapq
from typing import Dict, List, Optional, Tuple

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:  # Düzeltilen 'id' hatası
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edildi = set([baslangic])
        
        while kuyruk:
            mevcut, rota = kuyruk.popleft()
            
            if mevcut == hedef:
                return rota
            
            for komsu, _ in mevcut.komsular:
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    kuyruk.append((komsu, rota + [komsu]))
        
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        oncelik_kuyrugu = []
        heapq.heappush(oncelik_kuyrugu, (0, id(baslangic), baslangic, [baslangic]))
        ziyaret_edildi = {}
        
        while oncelik_kuyrugu:
            toplam_sure, _, mevcut, rota = heapq.heappop(oncelik_kuyrugu)
            
            if mevcut == hedef:
                return (rota, toplam_sure)
            
            if mevcut in ziyaret_edildi and ziyaret_edildi[mevcut] <= toplam_sure:
                continue
            
            ziyaret_edildi[mevcut] = toplam_sure
            
            for komsu, sure in mevcut.komsular:
                yeni_sure = toplam_sure + sure
                yeni_rota = rota + [komsu]
                heapq.heappush(oncelik_kuyrugu, (yeni_sure, id(komsu), komsu, yeni_rota))
        
        return None
    
# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 

#Aşti'den OSB'ye en kısa rotanın şematik gösterimi
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# İstasyonları ekleme
istasyonlar = {
    "K1": "Kızılay", "K2": "Ulus", "K3": "Demetevler", "K4": "OSB",
    "M1": "AŞTİ", "M2": "Kızılay", "M3": "Sıhhiye", "M4": "Gar",
    "T1": "Batıkent", "T2": "Demetevler", "T3": "Gar", "T4": "Keçiören"
}

# Bağlantılar ve süreler (dakika cinsinden)
baglantilar = [
    ("K1", "K2", 4), ("K2", "K3", 6), ("K3", "K4", 8),
    ("M1", "M2", 5), ("M2", "M3", 3), ("M3", "M4", 4),
    ("T1", "T2", 7), ("T2", "T3", 9), ("T3", "T4", 5),
    ("K1", "M2", 2), ("K3", "T2", 3), ("M4", "T3", 2)
]

# Düğümleri ekleme
for key, name in istasyonlar.items():
    G.add_node(key, label=name)

# Kenarları ekleme ve süreleri saklama
kenar_etiketleri = {}
for u, v, sure in baglantilar:
    G.add_edge(u, v)
    kenar_etiketleri[(u, v)] = f"{sure} dk"

# AŞTİ'den OSB'ye en kısa rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
en_kisa_rota = ["M1", "M2", "K1", "K2", "K3", "K4"]

# Kenar renklerini ayarla (yeşil en kısa rota, diğerleri gri)
edge_colors = ["green" if (u, v) in zip(en_kisa_rota, en_kisa_rota[1:]) or (v, u) in zip(en_kisa_rota, en_kisa_rota[1:]) 
               else "lightgray" for u, v in G.edges()]

# Hatlara göre düğüm renklerini belirleme
def get_node_color(node):
    if node.startswith("K"):
        return "red"  # Kırmızı Hat
    elif node.startswith("M"):
        return "blue"  # Mavi Hat
    elif node.startswith("T"):
        return "yellow"  # Sarı Hat
    return "gainsboro"

node_colors = [get_node_color(n) for n in G.nodes()]

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
labels = nx.get_node_attributes(G, 'label')

# Grafı çiz
nx.draw(G, pos, with_labels=True, labels=labels, node_size=2800, node_color=node_colors, 
        font_size=10, edge_color=edge_colors, width=2)

# Kenar etiketlerini (dakikaları) ekle
nx.draw_networkx_edge_labels(G, pos, edge_labels=kenar_etiketleri, font_size=9)

plt.title("Metro Ağı: En Kısa Rota (Dakika Bilgileriyle)")
plt.show()

