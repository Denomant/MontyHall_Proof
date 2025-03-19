from random import randint, shuffle, choice

TOTAL_TESTS = 1000

def simulate_stay(doors, initial_choice) -> bool:
    return doors[initial_choice] == "car"

def simulate_swap(doors, initial_choice) -> bool:
    # The host removes one door that is neither the initial choice nor the car
    can_open = []
    for i in range(3):
        if doors[i] != "car" and i != initial_choice:
            can_open.append(i)
    host_opened = choice(can_open)

    # player swaps his door
    for i in range(3):
        if i != host_opened and i != initial_choice:
            return doors[i] == "car"

def main():
    doors = ["car", "nothing", "nothing"]

    # run tests
    wins_stay = 0
    wins_swap = 0

    # Run tests
    for i in range(TOTAL_TESTS):
        initial_choice = randint(0,2)
        # Simulate stay
        if simulate_stay(doors, initial_choice):
            wins_stay += 1

        # Simulate swap
        if simulate_swap(doors, initial_choice):
            wins_swap += 1
        shuffle(doors)

    # Print results
    print(f"Results after {TOTAL_TESTS} tests:")
    print(f"If you keep with your initial choice you will find a car in {wins_stay} out of {TOTAL_TESTS}, or in {(wins_stay / TOTAL_TESTS * 100):.1f}%")
    print(f"If you swap your initial choice you will find a car in {wins_swap} out of {TOTAL_TESTS}, or in {(wins_swap / TOTAL_TESTS * 100):.1f}%")


if __name__ == "__main__":
    main()