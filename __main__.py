import sys
from population_simulation.simulation import simulation


def main():
    """
    Main function of the application
    """
    usage_text = "Usage: python -m pokemon_population_models [-n]"

    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print(usage_text)
        return

    if len(sys.argv) == 2 and sys.argv[1] == "-n":
        print("calling no humans")
        simulation(14, 2, False)
    elif len(sys.argv) == 1:
        print("calling regular")
        simulation(14, 2, True)
    else:
        print(usage_text)
        return


if __name__ == "__main__":
    main()

