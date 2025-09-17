"""
Minimal test of refined model - single scenario only
"""
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

class SimplifiedAMM:
    """Simplified constant-product AMM."""
    
    def __init__(self, pool_depth):
        self.initial_depth = pool_depth
        self.stablecoin_reserve = float(pool_depth)
        self.usd_reserve = float(pool_depth)
        self.k = pool_depth ** 2
        
    @property
    def price(self):
        return self.usd_reserve / self.stablecoin_reserve
    
    def execute_swap(self, stablecoin_amount):
        if stablecoin_amount == 0:
            return 0.0
            
        new_stablecoin_reserve = self.stablecoin_reserve + stablecoin_amount
        new_usd_reserve = self.k / new_stablecoin_reserve
        usd_received = self.usd_reserve - new_usd_reserve
        
        self.stablecoin_reserve = new_stablecoin_reserve
        self.usd_reserve = new_usd_reserve
        
        return usd_received

class MinimalDepegSim:
    """Minimal version of the simulation for testing."""
    
    def __init__(self, pool_depth=1_000_000, attack_size_frac=0.05):
        self.pool_depth = pool_depth
        self.attack_amount = pool_depth * attack_size_frac
        self.amm = SimplifiedAMM(pool_depth)
        
    def run_simulation(self):
        print(f"Initial price: ${self.amm.price:.4f}")
        
        # Execute attack
        proceeds = self.amm.execute_swap(self.attack_amount)
        print(f"After attack: Price=${self.amm.price:.4f}, Proceeds=${proceeds:,.0f}")
        
        # Check peg failure
        peg_failure = self.amm.price < 0.98
        
        return {
            'peg_failure': peg_failure,
            'min_price': self.amm.price,
            'profit': proceeds
        }

if __name__ == "__main__":
    print("=== MINIMAL REFINED MODEL TEST ===")
    
    sim = MinimalDepegSim()
    result = sim.run_simulation()
    
    print(f"\nResult: {result}")
    print("Test completed!")
