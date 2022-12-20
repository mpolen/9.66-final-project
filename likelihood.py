import numpy as np
import matplotlib.pyplot as plt
import random

# Sequences of 4-sided die
# s1 = 1,3,4,4,1,3,2,3
# s2 = 4,4,4,4,4,4,4,2
# s3 = 4,4,4,4,4,4,4,4
# s4 = 3,3,3,3,2,2,2,3

# Likelihood for a fair 4-sided die = 1/4^8
likelihood_fair_s1 = 1/(4 ** 8)
likelihood_fair_s2 = 1/(4 ** 8)
likelihood_fair_s3 = 1/(4 ** 8)
likelihood_fair_s4 = 1/(4 ** 8)

# likelihood for only rolls 4 4-sided die
likelihood_only_4_s1 = .003 * .003 * .99 * .99 * .003 * .003 * .003 * .003
likelihood_only_4_s2 = .99 * .99 * .99 * .99 * .99 * .99 * .99 * .003
likelihood_only_4_s3 = .99 * .99 * .99 * .99 * .99 * .99 * .99 * .99
likelihood_only_4_s4 = .003 * .003 * .003 * .003 * .003 * .003 * .003 * .003

# likelihood for mostly rolls 4 4-sided die
likelihood_mostly_4_s1 = .05 * .05 * .85 * .85 * .05 * .05 * .05 * .05
likelihood_mostly_4_s2 = .85 * .85 * .85 * .85 * .85 * .85 * .85 * .05
likelihood_mostly_4_s3 = .85 * .85 * .85 * .85 * .85 * .85 * .85 * .85
likelihood_mostly_4_s4 = .05 * .05 * .05 * .05 * .05 * .05 * .05 * .05

# likelihood for only rolls 2 or 3 4-sided die
likelihood_bw_2_or_3_s1 = .00066 * .499 * .00066 * .00066 * .00066 * .499 * .499 * .499
likelihood_bw_2_or_3_s2 = .00066 * .00066 * .00066 * .00066 * .00066 * .00066 * .00066 * .499
likelihood_bw_2_or_3_s3 = .00066 ** 8
likelihood_bw_2_or_3_s4 = .499 * .499 * .499 * .499 * .499 * .499 * .499 * .499

print("likelihood of s1,s2,s3,s4 given hypotheis fair die rolls: ", likelihood_fair_s1)

print("likelihood of s1 given hypothesis only rolls 4: ", likelihood_only_4_s1)
print("likelihood of s2 given hypothesis only rolls 4: ", likelihood_only_4_s2)
print("likelihood of s3 give hypothesis only rolls 4: ", likelihood_only_4_s3)
print("likelihood of s4 given hypothesis only rolls 4: ", likelihood_only_4_s4)

print("likelihood of s1 give hypothesis mostly rolls 4: ", likelihood_mostly_4_s1)
print("likelihood of s2 given hypothesis mostly rolls 4: ", likelihood_mostly_4_s2)
print("likelihood of s3 given hypothesis mostly rolls 4: ", likelihood_mostly_4_s3)
print("likelihood of s4 given hypothesis mostly rolls 4: ", likelihood_mostly_4_s4)

print("likelihood of s1 givenhypothesis rolls either 2 or 3: ",
      likelihood_bw_2_or_3_s1)
print("likelihood of s2 given hypothesis rolls either 2 or 3: ",
      likelihood_bw_2_or_3_s2)
print("likelihood of s3 given hypothesis rolls either 2 or 3: ",
      likelihood_bw_2_or_3_s3)
print("likelihood of s4 given hypothesis rolls either 2 or 3: ",
      likelihood_bw_2_or_3_s4)
      