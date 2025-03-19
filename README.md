# Monty Hall Paradox Proof by Simulation

## Table of Contents
1. [The Problem](#The-Problem)
2. [My Solution](#My-Solution)
3. [How to Run](#How-to-Run)
4. [Results](#Results)

## The Problem
The Monty Hall paradox is based on a game show
scenario where the player is presented with 3
doors. Behind 1 of the doors there is a prize, and
the other 2 are empty. The goal of the game is
straightforward - to choose the door with
the prize. After the player randomly guesses one
of the doors to be the prize, the host opens one
of the empty doors. Then the player has to decide
whether to stick with the same door or switch the
door; That's where the paradox takes place.
Initially it might seem that it doesn't matter, and
that the chances are 50%/50%, but that's not true.
The paradox states that the chances are actually
66.6%/33.3%, so in order to increase the chances
to win the prize, the player should switch the door
that was chosen initially.

## My Solution
To prove (or debunk) the paradox, I decided to
simulate the game show scenario for n times twice, 
one time sticking with the same door, and the other
time switching the door.  
I implemented 2 functions `simulate_stay` and
`simulate_swap`. Each takes the list of doors and
player's initial choice as an input, and returns
a Boolean value that indicates would the player find
the prize or not.
Then I implemented the `main` function that runs
the simulation for `TOTAL_TEST` times (constant
variable declared at the head of the file),
and counts the amount of times won for each strategy.
Finally I print the results using string formatting,
and limiting the amount of decimal places to 1 to
avoid binary representation errors such as 1/3
or 0.1 + 0.2.

## How to Run
1. Make sure you have git and Python 3 installed.
2. Navigate to the directory where you want to have
the script downloaded.
3. Clone the repository by running the following
command:
```bash
git clone https://github.com/Denomant/MontyHall_Proof.git
```
4. Run the following command:  
You might need to change the backslashes on
Linux based systems
```bash
python3 MontyHall_Proof/monty_hall.py
```

## Results
Results per 1000 simulations for each strategy:

| Strategy   | Wins | Win Percentage |
|------------|------|----------------|
| Stay       | 325  | 32.5%          |
| Swap       | 672  | 67.2%          |