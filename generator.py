import random
from scipy.stats import binom
import numpy as np


def roll_die_bias_for_4():
    # Generate a random number between 1 and 4 using a binomial
    # distribution with a probability of 0.85 of landing on 4
    roll = binom.rvs(n=1, p=0.85, size=1)

    # If the roll is 0, return a random number between 1 and 4
    # to simulate the roll of the die
    if roll == 0:
        return random.randint(1, 4)

    # Otherwise, return 4
    else:
        return 4


def roll_always_4():
    roll = binom.rvs(n=1, p=0.99, size=1)

    # If the roll is 0, return a random number between 1 and 4
    # to simulate the roll of the die
    if roll == 0:
        return random.randint(1, 4)

    # Otherwise, return 4
    else:
        return 4


def roll_fair_4_sided():
    return random.randint(1, 4)


def roll_only_2_or_3():
    dice_value = random.randint(1, 4)

    if dice_value == 2 or dice_value == 3:  # Check if the dice landed on 2 or 3
        return dice_value
    else:
        return roll_only_2_or_3()  # If the dice did not land on 2 or 3, roll it again


# Let's test the die by rolling it 8 times and printing the results
# result_bias_4 = []
# result_always_4 = []
# result_fair = []
# result_only_2_or_3 = []
# for i in range(8):
#     result_bias_4.append(roll_die_bias_for_4())
#     result_always_4.append(roll_always_4())
#     result_fair.append(roll_fair_4_sided())
#     result_only_2_or_3.append(roll_only_2_or_3())

# print("bias_4: ", result_bias_4)
# print("always_4: ", result_always_4)
# print("fair: ", result_fair)
# print("only_2_or_3: ", result_only_2_or_3)


# Generating data
out = None
for i in range(250):
    result_bias_4 = ["bias_4"]
    result_always_4 = ["always_4"]
    result_fair = ["fair"]
    result_only_2_or_3 = ["only_2_or_3"]
    for i in range(8):
        result_bias_4.append(roll_die_bias_for_4())
        result_always_4.append(roll_always_4())
        result_fair.append(roll_fair_4_sided())
        result_only_2_or_3.append(roll_only_2_or_3())
    if out is None:
        out = np.vstack([np.array(result_always_4), np.array(result_bias_4)])
    else:
        out = np.vstack([out, np.array(result_bias_4)])
        out = np.vstack([out, np.array(result_always_4)])

    out = np.vstack([out, np.array(result_fair)])
    out = np.vstack([out, np.array(result_only_2_or_3)])

print(out)
np.random.shuffle(out)

print(out)

np.savetxt("data.csv", out, delimiter=",", fmt='%s')

