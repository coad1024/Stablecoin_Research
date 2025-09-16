# tools/run_attack_sim.py
import argparse

def run_simulation(pool_depth, target_price, fee, attacker_has_s):
    # TODO: Replace with actual calls to DualTokenSim modules
    print(f"Running sim with pool_depth={pool_depth}, target_price={target_price}, fee={fee}, attacker_has_s={attacker_has_s}")
    return {"profit": 0.0, "cost": 0.0, "deltaS": 0}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pool-depth", type=float, default=5_000_000)
    parser.add_argument("--target-price", type=float, default=0.95)
    parser.add_argument("--fee", type=float, default=0.003)
    parser.add_argument("--attacker-has-s", action="store_true")
    args = parser.parse_args()

    res = run_simulation(args.pool_depth, args.target_price, args.fee, args.attacker_has_s)
    print(res)
