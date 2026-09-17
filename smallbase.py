#imports
import matplotlib
import numpy as np



#Parameter definitions
gamma = 1/10        #recovery rate
sigma = 1/4        #incubation period
beta_house = 0.2 
beta_store = 0.2   # the beta values are higher because the population is smaller, they change for validation
n_households = 2   #number of houses
household_size = 1  #number of ppl per house
n = n_households * household_size
store_int = 3      #store visit every 3 days
avgrlday = 1


#create a dictionary that will return what house a person is in given there ID(number)
house = {}
person_id = 0
for household_id in range(0,n_households):
    for k in range(household_size):
        house[person_id] = household_id
        person_id = person_id + 1
#adding the number of people in each house to validate that the sorting was done correctly(also can be used later to see how different household populations effect the mdoel)

household_pop = {}
for key in house:
    val = house[key]
    if val in household_pop:
        household_pop[val] = household_pop[val] + 1
    else:
        household_pop[val] = 1
#manually creating an array of those visiting the house
#print(household_pop)
def household(hh):
    household_members = [hh]
    return household_members
#print(household(0))


#strategy 0 is designated, 1 is rotate, 2 is random, 3 is adaptive
def get_shopper(hh, day, strategy, adaptive_shopper):
    shopper = hh
    #if strategy == 0:
      #  shopper = hh*4
    #elif strategy == 1:
       # shopper = hh*4 + day % 4
    #elif strategy == 2:
        #shopper = hh*4 + np.random.randint(0,4)
    #else:
       
     #   if adaptive_shopper[hh] != None:
         #   shopper = adaptive_shopper[hh]
        #else:
         #   shopper = hh*4 + day % 4
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
        inh_susceptible = 0
        inh_s_p = []
        members = [i]
        for m in members:             
            if state[m] == 2:
                inh_infected = inh_infected + 1
            elif state[m] == 0:
                inh_susceptible = inh_susceptible + 1
                inh_s_p.append(m)
            if m == i*4 + 3:
                for u in inh_s_p:
                    if np.random.random() < 1-(1-beta_house)**inh_infected:
                        new_state[u] = 1
                        ever_infected.add(u)
    return new_state


def one_day(state, day, strategy, ever_infected, adaptive_shopper):
    new_state = state.copy()
    new_state = store_contact(state, new_state, day, strategy, ever_infected, adaptive_shopper)
    new_state = household_contact(state, new_state, ever_infected)
    for i in range(n):
        if new_state[i] == 1 and np.random.random() < sigma:
            new_state[i] = 2
        elif new_state[i] == 2 and np.random.random() < gamma:
            new_state[i] = 3
        elif new_state[i] == 3: # and np.random.random() < 1/avgrlday:
            if strategy == 3:
                if adaptive_shopper[house[i]] == None:
                    adaptive_shopper[house[i]] = i
    return new_state



def sim(strategy):
    day=0
    initial_infected = 0
    state = np.zeros(n, dtype=int)
    state[initial_infected] = 1
    ever_infected = set()
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
        state = one_day(state, day, strategy, ever_infected, adaptive_shopper)
        day = day + 1
    
    
    return len(ever_infected)

inf0 = 0
inf1 = 0
inf2 = 0
inf3 = 0
for i in range(100000):
    inf0 = inf0 + sim(0)
    #inf1 = inf1 + sim(1)
    #inf2 = inf2 + sim(2)
    #inf3 = inf3 + sim(3)
print("never infected:", (1-(inf0/100000)))


