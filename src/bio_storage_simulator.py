import math

class BioStorageSimulator:
    """
    DNA tabanlı veri depolamanın teorik yoğunluğunu ve hata olasılığını simüle eder.
    """
    def __init__(self):
        # DNA depolama için sabitler (Yaklaşık bilimsel değerler)
        self.bits_per_base = 2  # A, C, G, T = 2 bit
        self.mass_of_single_nt = 1.07e-22  # nükleotid başına gram (ortalama)
        self.max_theoretical_density_pb_per_g = 215  # Gram başına Petabayt

    def calculate_density(self, data_size_tb, redundancy_factor=1.2):
        """
        Belirli bir TeraByte boyutu için gereken DNA kütlesini hesaplar.
        """
        data_bits = data_size_tb * 8 * (10**12)  # TB -> bit
        required_bases = (data_bits / self.bits_per_base) * redundancy_factor
        required_mass_g = required_bases * self.mass_of_single_nt
        
        return {
            "required_mass_g": required_mass_g,
            "required_mass_mg": required_mass_g * 1000,
            "density_efficiency": (data_size_tb / 1000) / (required_mass_g * 100) # 100g başına PB görünümü
        }

    def simulate_error_rate(self, synthesis_method="Enzymatic"):
        """
        Sentez teknolojisine göre tahmini hata oranlarını döndürür.
        """
        methods = {
            "Phosphoramidite": {"error_rate": 0.005, "speed": "Yavaş", "trl": 8},
            "Enzymatic": {"error_rate": 0.001, "speed": "Orta", "trl": 5},
            "In-Vivo": {"error_rate": 0.00001, "speed": "Değişken", "trl": 3}
        }
        return methods.get(synthesis_method, "Bilinmeyen yöntem")

if __name__ == "__main__":
    sim = BioStorageSimulator()
    
    print("=" * 60)
    print("🧬 DNA DEPOLAMA YOĞUNLUĞU VE STRATEJİK SİMÜLATÖR")
    print("=" * 60)
    
    # Örnek: 1 Petabaytlık Küresel Verinin Arşivlenmesi
    pb_data = 1
    results = sim.calculate_density(pb_data * 1000)
    
    print(f"Hedef Veri: {pb_data} Petabayt")
    print(f"Tahmini Gereken DNA Kütlesi: {results['required_mass_mg']:.6f} mg")
    print(f"Silikon ile Karşılaştırmalı Yoğunluk: ~1.000.000x daha yoğun")
    print("-" * 60)
    
    # Hata Payı Analizi
    method = "Enzymatic"
    stats = sim.simulate_error_rate(method)
    print(f"Sentez Yöntemi: {method}")
    print(f"Bit Hata Oranı (BER): {stats['error_rate']}")
    print(f"TRL Durumu: {stats['trl']}")
    print("-" * 60)
    
    print("STRATEJİK NOT: Genetik veri depolama, nihai sıfır-enerji arşividir.")
    print("=" * 60)
