import math
import matplotlib.pyplot as plt
import numpy as np

def fair_die(seq_len):
    return 1/(4**seq_len)

def weighted_die(num_1s, num_2s, num_3s, num_4s):
    # P(1 | theta, sigma, delta) = theta; P(tails | theta) = 1-theta
    # P(2 | theta, sigma, delta) = sigma; P(tails | theta) = 1-theta
    # P(3 | theta, sigma, delta) = delta; P(tails | theta) = 1-theta
    # P(4 | theta, sigma, delta) = 1-theta-sigma-delta; P(tails | theta) = 1-theta

    # 0|000|000|00
    # 0000000
    # P(theta | coin2) = uniform(0,1)
    # P(seq | coin2) = sum P(seq | theta) * P(theta | coin2)
    # 3
    p_seq_given_die = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                theta = (i+1)/100
                sigma = (j+1)/100
                delta = (k+1)/100
                if(theta + sigma + delta <= 1):
                    p_seq_given_rs = theta**num_1s * sigma**num_2s * delta**num_3s * (1-theta-sigma-delta)**num_4s
                    
                    p_rs_given_die = 1/171700 #uniform(0,1)

                    p_seq_given_die += p_seq_given_rs * p_rs_given_die
                else:
                    continue
    return p_seq_given_die

def log_posterior_ratio(p_seq_given_coin1, p_seq_given_coin2):
    return np.log(p_seq_given_coin1/p_seq_given_coin2) #Assume P(H1)/P(H2) = 0

def logistic_function(a, b, x):
    return 1/(1+np.exp(-a*x + b))

def plot_sequence(user_values, die_sequence, a, b, title):
    predicted_scores = []
    for i in range(len(die_sequence)):
        p_seq_given_fair = fair_die(die_sequence[i][0]+die_sequence[i][1]+die_sequence[i][2]+die_sequence[i][3])
        p_seq_given_weighted = weighted_die(die_sequence[i][0], die_sequence[i][1],die_sequence[i][2],die_sequence[i][3])
        score = logistic_function(a, b, log_posterior_ratio(p_seq_given_fair, p_seq_given_weighted))
        score = score * 7 #scaled to 1-7 score
        predicted_scores.append(score)

    coins = np.array([i+1 for i in range(4)])
    correlation = np.corrcoef(np.array(predicted_scores), np.array(user_values))
    print(title, "Correlation: \n", correlation)
    fig, ax = plt.subplots()
    ax.bar(coins-.5, predicted_scores,width = .5, label="predicted")
    ax.bar(coins, user_values, width=.5, label="user")
    ax.set(xlabel='Sequence #', ylabel='Die fairness score(1-7)', title=title);
    ax.legend()
    plt.show()

if __name__ == '__main__':
    # X_test = np.array([[1, 3, 4, 4, 1, 3, 2, 3],
    #                     [4, 4, 4, 4, 4, 4, 4, 2],
    #                     [4, 4, 4, 4, 4, 4, 4, 4],
    #                     [3, 3, 3, 3, 2, 2, 2, 3]])

    # y_test = np.array(['fair', 'bias_4', 'always_4', 'only_2_or_3'])

    die_sequence = [(2, 1, 3, 2), (0, 1, 0, 7), (0, 0, 0, 8), (0, 3, 5, 0)]

    # Cover Story 1
    user_responses_cover_1 = [6.021276596, 2.723404255, 2.085106383, 3.765957447]
    plot_sequence(user_responses_cover_1, die_sequence, .1, .0001, 'Cover Story 1')


    # Cover Story 2
    # TODO input user data here: 
    # user_responses_cover_2 = [5.617021277, 2.489361702, 1.829787234, 3.106382979]
    # plot_sequence(user_responses_cover_2, die_sequence, .3, .1, 'Cover Story 2')
    # total = 0
    # for i in range(100):
    #     for j in range(i,100):
    #         for k in range(j,100):
    #             total += 1
    # print(total)