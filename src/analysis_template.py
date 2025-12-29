import json

def calculate_average_trl(data_path):
    """
    Bio-matrix verisinden ortalama TRL seviyesini hesaplar.
    """
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        techs = data.get('technologies', [])
        if not techs:
            return 0
        
        total_trl = sum(t.get('trl_level', 0) for t in techs)
        return total_trl / len(techs)
    except Exception as e:
        print(f"Hata: {e}")
        return None

if __name__ == "__main__":
    matrix_path = "data/bio_matrix.json"
    avg = calculate_average_trl(matrix_path)
    if avg:
        print(f"Bio-Compute Sektörü Ortalama TRL Seviyesi: {avg:.2f}")
