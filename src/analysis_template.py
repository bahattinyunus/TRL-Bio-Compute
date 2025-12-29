import json
import os

def generate_trl_report(data_path):
    """
    Bio-matrix verisinden detaylı bir analiz raporu oluşturur.
    """
    if not os.path.exists(data_path):
        print(f"Hata: {data_path} bulunamadı.")
        return

    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        techs = data.get('technologies', [])
        if not techs:
            print("Analiz edilecek teknoloji bulunamadı.")
            return

        total_trl = 0
        high_risk = []
        mature_techs = []
        
        print("-" * 50)
        print("🧬 TRL-BIO-COMPUTE STRATEJİK ANALİZ RAPORU")
        print("-" * 50)
        
        for t in techs:
            name = t.get('name', 'N/A')
            trl = t.get('trl_level', 0)
            status = t.get('status', 'Unknown')
            total_trl += trl
            
            if trl <= 3:
                high_risk.append(name)
            elif trl >= 6:
                mature_techs.append(name)
            
            print(f"- {name:25} | TRL: {trl} | Durum: {status}")

        avg_trl = total_trl / len(techs)
        
        print("-" * 50)
        print(f"Sektör Ortalama TRL: {avg_trl:.2f}")
        print(f"Yüksek Riskli (TRL <= 3) Teknolojiler: {len(high_risk)}")
        print(f"Ticarileşmeye Yakın (TRL >= 6) Teknolojiler: {len(mature_techs)}")
        print("-" * 50)
        
        if high_risk:
            print(f"UYARI: {', '.join(high_risk)} için Ar-Ge desteği kritik.")
        
        # Matrix verisini güncelle
        data['global_metrics']['sector_average_trl'] = round(avg_trl, 2)
        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"Analiz sırasında bir hata oluştu: {e}")

if __name__ == "__main__":
    matrix_path = "data/bio_matrix.json"
    generate_trl_report(matrix_path)
