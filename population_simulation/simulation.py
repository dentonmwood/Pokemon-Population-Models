import csv
import random
import numpy


def simulation(male_pop, female_pop, is_human_present):
    tick = 0
    num_eggs = 21
    eggs = numpy.zeros(num_eggs, dtype=int)
    
    output_file_path = 'output/BulbasaurPopulation'
    if is_human_present:
        output_file_path += 'NoHuman'
    output_file_path += '.csv'

    with open(output_file_path, 'a', newline='') as csv_file:
        fieldnames = ['tick', 'females', 'males']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    while True:
        with open(output_file_path, 'a', newline='') as csv_file:
            fieldnames = ['tick', 'females', 'males']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'tick': tick, 'females': female_pop, 'males': male_pop})
            csv_file.close()
        tick += 1
        print('Tick:', tick)
        for x in range(female_pop):
            death = random.randint(1,10000)
            if death <= 243:
                female_pop += -1

        for x in range(male_pop):
            death = random.randint(1,10000)
            if death <= 243:
                male_pop += -1

        if eggs[0] > 0:
            print(eggs[0], 'Bulbasaur eggs are hatching!')
            for x in range(eggs[0]):
                sexroll = random.randint(1,8)
                if sexroll <= 7:
                    male_pop += 1
                else:
                    female_pop += 1

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

        if male_pop >= 1 and human_check:
            for x in range(female_pop):
                egg = random.randint(1,100)
                if egg <= 50:
                    eggs[20] += 1

        elif female_pop >=1:

            for x in range(female_pop):
                egg = random.randint(1,100)
                if egg <=10:
                    eggs[20] += 1

        print('Total Population:', female_pop + male_pop)
        print('Females:', female_pop)
        print('Males:', male_pop)
        print('')

        if female_pop+male_pop >= 20000:
            print('Population max reached')

            break
        elif female_pop == 0 and numpy.count_nonzero(eggs) == 0:
            print('Extinction')
            break
