# Fusion Power Calculator

## Installation

This project is a complete Python script and does not require any external dependencies. You can simply clone the repository or download it as a compressed zip file.

## Usage

To use the fusion power calculator, The basic understandings are the following parameters:

```python

traps = 4.0e10           # Number of nano-traps
rate = 5.0e7             # Attempts per trap per second (Hz)
probability = 0.25       # Tunneling success probability (0.0–1.0)
fuel = "DD"              # Fuel type: "DT", "DD", or "pB11"

results = fusion_calculator(traps, rate, probability, fuel)

for k, v in results.items():
    print(f"{k:25s}: {v:.3e}")
```

The `fusion_calculator` function returns a dictionary with the following keys:

- `"attempts/s"`: Total fusion attempts per second
- `"successes/s"`: Successful fusion reactions per second
- `"power (MW)"`: Total power output in megawatts (MW)
- `"fuel consumption (g/s)"`: Fuel consumption rate in grams per second

## API

The main function in this project is:

```python
def fusion_calculator(traps, rate, probability, fuel="DT"):
    """
    Calculate fusion power and fuel consumption.

    Args:
        traps (float): Number of nano-traps.
        rate (float): Fusion attempts per trap per second (Hz).
        probability (float): Tunneling success probability (0.0–1.0).
        fuel (str, optional): Fuel type, one of "DT", "DD", or "pB11". Defaults to "DT".

    Returns:
        dict: A dictionary with the following keys:
            - "attempts/s": Total fusion attempts per second
            - "successes/s": Successful fusion reactions per second
            - "power (MW)": Total power output in megawatts (MW)
            - "fuel consumption (g/s)": Fuel consumption rate in grams per second
    """
    pass
```

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/Vikas-AI968/Fusion_Power_Calculator-Arc-Reactor-Technology-).

## License

This project is licensed under the [MIT License](LICENSE).
