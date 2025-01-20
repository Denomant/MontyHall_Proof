from random import randint, shuffle, choice

total_tests = 1000
doors = ["car", "goat", "goat"]

def try_to_stay() -> bool:
    return doors[initial_choice] == "car"

def try_to_swap() -> bool:
    # host removes one door that is not the initial choice, and not the car
    can_open = []
    for i in range(3):
        if doors[i] != "car" and i != initial_choice:
            can_open.append(i)
    host_opened = choice(can_open)

    # player swaps his door
    for i in range(3):
        if i != host_opened and i != initial_choice:
            return doors[i] == "car"

# ran tests
wins_stay = 0
wins_swap = 0

for i in range(total_tests):
    initial_choice = randint(0,2)
    if try_to_stay():
        wins_stay += 1
    shuffle(doors)

for i in range(total_tests):
    if try_to_swap():
        wins_swap += 1
    shuffle(doors)

print(f"Results after {total_tests} tests:")
print(f"If you keep with your initial choice you will find a car in {wins_stay} out of {total_tests}, or in {wins_stay / total_tests * 100}%")
print(f"If you swap your initial choice you will find a car in {wins_swap} out of {total_tests}, or in {wins_swap / total_tests * 100}%")