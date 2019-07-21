import csv
import random
import numpy


def simulation(male_pop, female_pop, is_human_present):
    """
    Simulates the breeding and death of a population

    Arguments:
        male_pop: number of males in the population
        female_pop: number of females in the population
        is_human_present: whether human activity will affect the population
    """
    tick = 0
    num_eggs = 21
    eggs = numpy.zeros(num_eggs, dtype=int)
    
    output_file_path = 'output/BulbasaurPopulation'
    if not is_human_present:
        output_file_path += 'NoHuman'
    output_file_path += '.csv'

    csv_field_names = ['tick', 'females', 'males']
    csv_file = open(output_file_path, 'w', newline='')
    writer = csv.DictWriter(csv_file, fieldnames=csv_field_names)
    writer.writeheader()

    pop_max_reached = False
    extinction = False

    # Keep iterating while the population is stable
    while not pop_max_reached and not extinction:
        writer.writerow({csv_field_names[0]: tick,
                         csv_field_names[1]: female_pop,
                         csv_field_names[2]: male_pop})
        tick += 1
        print('Tick:', tick)

        # For females, probability of death is 243/10000
        female_death_max = 243
        for x in range(female_pop):
            female_death_check = random.randint(1, 10000)
            if female_death_check <= female_death_max:
                female_pop -= 1

        # For males, probability of death is also 243/10000
        male_death_max = 243
        for x in range(male_pop):
            male_death_check = random.randint(1, 10000)
            if male_death_check <= male_death_max:
                male_pop -= 1

        # If we have eggs ready to hatch, hatch them
        if eggs[0] > 0:
            # Ratio of males to females is 7 to 1
            print(eggs[0], 'Bulbasaur eggs are hatching!')
            for x in range(eggs[0]):
                baby_male_ratio = 7
                baby_sex_check = random.randint(1, 8)
                if baby_sex_check <= baby_male_ratio:
                    male_pop += 1
                else:
                    female_pop += 1

        """
        Eggs in Pokemon require 20 ticks to hatch. The eggs variable is a series of buckets to
        simulate this effect. Eggs are moved backward through the buckets until they are ready to hatch.
        """
        # TODO: fix Python anti-pattern
        for i in range(len(eggs)):
            if i < len(eggs) - 1:
                eggs[i] = eggs[i] - eggs[i] + eggs[i + 1]
            else:
                eggs[i] = eggs[i] - eggs[i]

        # TODO: fix awkward handling of human condition
        human_check = True
        if is_human_present and tick > 100:
            human_check = False

        # Eggs are more likely to hatch if there's at least one female present
        for x in range(female_pop):
            egg_check = random.randint(1, 100)
            if male_pop > 0 and human_check and egg_check <= 50:
                eggs[20] += 1
            elif female_pop > 0 and egg_check <= 10:
                eggs[20] += 1

        birth_check = 0
        if male_pop > 0 and human_check:
            birth_check = 50
        elif female_pop > 0:
            birth_check = 10

        if birth_check:
            for x in range(female_pop):
                egg_check = random.randint(1, 100)
                if egg_check <= birth_check:
                    eggs[20] += 1

        print('Total Population:', female_pop + male_pop)
        print('Females:', female_pop)
        print('Males:', male_pop)
        print('')

        population_maximum = 20000
        if female_pop + male_pop >= population_maximum:
            print('Population max reached')
            pop_max_reached = True
        elif female_pop == 0 and numpy.count_nonzero(eggs) == 0:
            print('Extinction')
            extinction = True

    csv_file.close()
