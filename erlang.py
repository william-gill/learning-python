#Looking for the Erlang distribution
# I want to see if I can replicate an Erlang distribtion.
# Generate a random number, and keep generating unil the number is 5. Count how many attempts is required to get a 5.

from random import randint
iterations = 0
results = []


while iterations < 100000:
    count=0
    while True:
        count += 1
        num = randint(0,10)
        #print (num)
        if num == 5:
            break
    iterations += 1
    results.append(count)

#print (results)

results_list = []
x=0
while x < 100:
    print(results.count(x))
    results_list.append(results.count(x))
    x += 1

import matplotlib.pyplot as plt
plt.hist(results_list, bins=20)
plt.show()

#Save results to a file
save_log = open('erlang-results.txt', 'w+')
save_log.write(str(results))
save_log.close()
