# Fusion Power Calculator for Arc Reactor Concept
import math

# Constants
AVOGADRO = 6.02214076e23  # mol^-1

# Fusion energies (Joules per reaction)
ENERGIES = {
    "DT": 17.6e6 * 1.602176634e-19,   # D-T fusion ~17.6 MeV
    "DD": 3.65e6 * 1.602176634e-19,   # D-D average ~3.65 MeV
    "pB11": 8.7e6 * 1.602176634e-19   # Proton-Boron11 ~8.7 MeV
}

# Approx molar masses (g/mol)
MOLAR_MASS = {
    "DT": 2.014,  # deuterium approx
    "DD": 2.014,
    "pB11": 1.008  # proton mass (boron is abundant, so we track proton)
}


def fusion_calculator(traps, rate, probability, fuel="DT"):
    """
    traps: number of nano-traps (e.g., 4e10)
    rate: attempts per trap per second (Hz)
    probability: tunneling success probability (0.0–1.0)
    fuel: "DT", "DD", or "pB11"
    """

    # Total attempts per second
    attempts = traps * rate

    # Successful fusions per second
    successes = attempts * probability

    # Energy per fusion
    energy_per_reaction = ENERGIES[fuel]

    # Total power (Watts)
    power_watts = successes * energy_per_reaction
    power_mw = power_watts / 1e6

    # Fuel consumption (grams per second)
    moles_per_s = successes / AVOGADRO
    grams_per_s = moles_per_s * MOLAR_MASS[fuel]

    return {
        "attempts/s": attempts,
        "successes/s": successes,
        "power (MW)": power_mw,
        "fuel consumption (g/s)": grams_per_s
    }


# ------------------ CALCULATIONS -------------------
if __name__ == "__main__":
    # Example parameters
    traps = 4.0e10           # 40 billion traps
    rate = 5.0e7             # 50 MHz per trap
    probability = 0.25       # 25% tunneling probability
    fuel = "DD"              # Deuterium-Tritium

    results = fusion_calculator(traps, rate, probability, fuel)

    print("\n=== Fusion Calculator Results ===")
    for k, v in results.items():
        print(f"{k:25s}: {v:.3e}")

