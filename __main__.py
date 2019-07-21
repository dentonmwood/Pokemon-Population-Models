import sys
from population_simulation.BULBASAUR import bulbasaur
from population_simulation.BULBASAUR_NO_HUMANS import bulbasaur_no_humans


def main():
    usage_text = "Usage: python -m pokemon_population_models [-n]"

    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print(usage_text)
        return

    if len(sys.argv) == 2 and sys.argv[1] == "-n":
        print("calling no humans")
        bulbasaur_no_humans()
    elif len(sys.argv) == 1:
        print("calling regular")
        bulbasaur()
    else:
        print(usage_text)
        return


if __name__ == "__main__":
    main()

