import math

class BioStorageSimulator:
    """
    Simulates the theoretical density and error probability of DNA-based data storage.
    """
    def __init__(self):
        # Constants for DNA storage (Approximate scientific values)
        self.bits_per_base = 2  # A, C, G, T = 2 bits
        self.mass_of_single_nt = 1.07e-22  # grams per nucleotide (average)
        self.max_theoretical_density_pb_per_g = 215  # Petabytes per gram

    def calculate_density(self, data_size_tb, redundancy_factor=1.2):
        """
        Calculates the required grams of DNA for a given TeraByte size.
        """
        data_bits = data_size_tb * 8 * (10**12)  # TB to bits
        required_bases = (data_bits / self.bits_per_base) * redundancy_factor
        required_mass_g = required_bases * self.mass_of_single_nt
        
        return {
            "required_mass_g": required_mass_g,
            "required_mass_mg": required_mass_g * 1000,
            "density_efficiency": (data_size_tb / 1000) / (required_mass_g * 100) # PB per 100g view
        }

    def simulate_error_rate(self, synthesis_method="Enzymatic"):
        """
        Returns estimated error rates based on synthesis technology.
        """
        methods = {
            "Phosphoramidite": {"error_rate": 0.005, "speed": "Slow", "trl": 8},
            "Enzymatic": {"error_rate": 0.001, "speed": "Medium", "trl": 5},
            "In-Vivo": {"error_rate": 0.00001, "speed": "Variable", "trl": 3}
        }
        return methods.get(synthesis_method, "Unknown method")

if __name__ == "__main__":
    sim = BioStorageSimulator()
    
    print("=" * 60)
    print("🧬 DNA STORAGE DENSITY & STRATEGIC SIMULATOR")
    print("=" * 60)
    
    # Example: Archiving 1 Petabyte of Global Data
    pb_data = 1
    results = sim.calculate_density(pb_data * 1000)
    
    print(f"Target Data: {pb_data} Petabyte")
    print(f"Estimated DNA Mass Required: {results['required_mass_mg']:.6f} mg")
    print(f"Density compared to Silicon: ~1,000,000x denser")
    print("-" * 60)
    
    # Error Margin Analysis
    method = "Enzymatic"
    stats = sim.simulate_error_rate(method)
    print(f"Synthesis Method: {method}")
    print(f"Bit Error Rate (BER): {stats['error_rate']}")
    print(f"TRL Status: {stats['trl']}")
    print("-" * 60)
    
    print("STRATEGIC NOTE: Genetic data storage is the ultimate zero-energy archive.")
    print("=" * 60)
