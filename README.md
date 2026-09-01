# epidemicproj
```
#imports
import matplotlib.pyplot as plt

import numpy as np
from sympy import N



#Parameter definitions
gamma = 1/10        #recovery rate
sigma = 1/4         #incubation period
#beta_house = 0.1 #calibrated to give 2.2 R0_household
#beta_store = 0.5  #infectivity in store based off of R0 of 2.8ish
n_households = 20   #number of houses
#household_size = 4  #number of ppl per house

store_int = 3       #store visit every 3 days
avgrlday = 1    

#adding the number of people in each house to validate that the sorting was done correctly(also can be used later to see how different household populations effect the mdoel)



#manually creating an array of those visiting the house
#print(household_pop)
#print(household(0))



#strategy 0 is designated, 1 is rotate, 2 is random, 3 is adaptive
def get_shopper(hh, day, strategy, adaptive_shopper):
    members = households[hh]
    
    if strategy == 0:
        shopper = members[0]
    elif strategy == 1:
        shopper = members[day % len(members)]
    elif strategy == 2:
        shopper = np.random.choice(members)
    else:
       
        if adaptive_shopper[hh] != None:
            shopper = adaptive_shopper[hh]
        else:
            shopper = members[day % len(members)]
    return shopper




#print(get_shopper(2,3,3))



def store_contact(state, new_state, day, strategy, ever_infected, adaptive_shopper):
    if day % store_int == 0:
        shopper_list = []
        infected_count = 0
        Sshopper_list = []
        for i in range(n_households):
            chosen = get_shopper(i, day, strategy, adaptive_shopper)
            shopper_list.append(chosen)
            if state[chosen] == 2:
                infected_count = infected_count+1
            elif state[chosen] == 0:
                Sshopper_list.append(chosen)
        for s in Sshopper_list:
            if np.random.random() < 1-(1-beta_store)**infected_count:
                new_state[s] = 1
                ever_infected.add(s)
                
        return new_state
    
        



    else:
        return new_state
#print(store_contact(state, new_state, 0, 0))
#print(ever_infected)



def household_contact(state, new_state, ever_infected):

    for i in range(n_households):
        inh_infected = 0
        inh_s_p = []
        members = households[i]
        for m in members:
            if state[m] == 2:
                inh_infected = inh_infected+1
            elif state[m] == 0:
                inh_s_p.append(m)
        for u in inh_s_p:
            if np.random.random() < 1 - (1-beta_house)**inh_infected:
                new_state[u] = 1
                ever_infected.add(u)
    return new_state

def one_day(state, day, strategy, ever_infected, adaptive_shopper, recovered_time):
    new_state = state.copy()
    new_state = store_contact(state, new_state, day, strategy, ever_infected, adaptive_shopper)
    new_state = household_contact(state, new_state, ever_infected)
    for i in range(n):
        if state[i] == 1 and np.random.random() < sigma:
            new_state[i] = 2
        elif state[i] == 2 and np.random.random() < gamma:
            new_state[i] = 3
            recovered_time[i] = day
        elif state[i] == 3: # and np.random.random() < 1/avgrlday:
            if strategy == 3:
                if adaptive_shopper[house[i]] == None:
                    adaptive_shopper[house[i]] = i
    return new_state

 

def sim(strategy):
    global house, households, household_pop, n 
    household_size = np.random.choice(
    [1,2,3,4,5,6,7],
    size=n_households,
    p=[0.29,0.35,0.16,0.13,0.04,0.02,0.01]
)


    n = np.sum(household_size)


    #create a dictionary that will return what house a person is in given there ID(number)
    house = {}
    households = {}
    household_pop = {}
    person_id = 0
    for hh, size in enumerate(household_size):
        households[hh] = []
        household_pop[hh] = size

        for j in range(size):
            house[person_id] = hh
            households[hh].append(person_id)
            person_id = person_id + 1
    day=0
    initial_infected = np.random.randint(0,n)
    state = np.zeros(n, dtype=int)
    recovered_time = np.full(n, -10000, dtype=int)
    state[initial_infected] = 1
    ever_infected = {initial_infected}
    adaptive_shopper = {}
    for i in range(n_households):
        adaptive_shopper[i] = None
    #print(adaptive_shopper)
    peak = 0
    while np.any((state == 1) | (state == 2)):
        infected_mask = state == 2
        infected_pop = state[infected_mask]
        if len(infected_pop) > peak:
            peak = len(infected_pop)
        state = one_day(state, day, strategy, ever_infected, adaptive_shopper, recovered_time)
        day = day + 1
    
    
    return len(ever_infected), n

trials = 1000
beta_values = np.arange(0.1, 1.1, 0.1)  
results = {0: [], 1: [], 2: [], 3: []}
for beta in beta_values:
    #beta_house = beta
    beta_store = beta
    beta_house = beta
    for strategy in range(4):
        inf = []
        ppl = []
        for i in range(trials):
            f, p = sim(strategy)
            inf.append(f)
            ppl.append(p)
        total = np.mean([i/p for i,p in zip(inf, ppl)])
        results[strategy].append(total)


labels = {0: 'Designated', 1: 'Rotation', 2: 'Random', 3: 'Adaptive'}
for strategy in range(4):
    plt.plot(beta_values, results[strategy], label=labels[strategy], marker='o')

plt.xlabel('Beta Store')
plt.ylabel('Average total infected (%)')
plt.title('Total population infected across transmission rates')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('beta_sweep.png')
plt.show()
```
