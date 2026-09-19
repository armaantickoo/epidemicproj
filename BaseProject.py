#imports
import matplotlib.pyplot as plt

import numpy as np




#Parameter definitions
re_int = 100
tot_day = 2000
grace = 210
omega = 0.0014
gamma = 1/10        #recovery rate
sigma = 1/4         #incubation period 
beta_house = 0.0215 #callibrated for SAR of about 18percent
beta_store = 0.02   #MUST be recalibrated every time population size changes, callibrated for casual attack rates across research
n_households = 20   #number of houses
#household_size = 4  #number of ppl per house

store_int = 3       #store visit every 3 days
avgrlday = 1    

#adding the number of people in each house to validate that the sorting was done correctly(also can be used later to see how different household populations effect the mdoel)

#creating age distinctions - varying susceptibility based on age grp
age_bands = ['child', 'adult', 'senior']
age_band_probs = [0.22, 0.60, 0.18]
susceptibility_by_age = {'child': 0.5, 'adult': 1.0, 'senior': 1.5}
gamma_mult_by_age = {'child': 1.2, 'adult': 1.0, 'senior': 0.7}
omega_mult_by_age = {'child': 0.7, 'adult': 1.0, 'senior': 2.5}

#manually creating an array of those visiting the house
#print(household_pop)
#print(household(0))



#strategy 0 is designated, 1 is rotate, 2 is random, 3 is adaptive, 4 is adaptive smart
def get_shopper(hh, day, strategy, adaptive_shopper):
    members = households[hh]
    
    if strategy == 0:
        shopper = members[0]
    elif strategy == 1:
        shopper = members[day % len(members)]
    elif strategy == 2:
        shopper = np.random.choice(members)
    elif strategy == 3:
       
        if adaptive_shopper[hh] != None:
            shopper = adaptive_shopper[hh]
        else:
            shopper = members[day % len(members)]
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
            #if np.random.random() < 1-(1-beta_store)**infected_count:
            if np.random.random() < 1-(1-beta_store*susceptibility[s])**infected_count:
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
            #if np.random.random() < 1 - (1-beta_house)**inh_infected:
            if np.random.random() < 1 - (1-beta_house*susceptibility[u])**inh_infected:
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
        elif state[i] == 2 and np.random.random() < gamma_i[i]:
        #elif state[i] == 2 and np.random.random() < gamma:
            new_state[i] = 3
            recovered_time[i] = day
            if strategy == 3 and adaptive_shopper[house[i]] == None:
                adaptive_shopper[house[i]] = i
            if strategy == 4:
                adaptive_shopper[house[i]] = i
        elif state[i] == 3: # and np.random.random() < 1/avgrlday:
            days_since_rec = day-recovered_time[i]
            if days_since_rec >= grace:
                if np.random.random() < omega:
                    new_state[i] = 0
    return new_state

 

def sim(strategy, tot_day):
    global house, households, household_pop, n, susceptibility, gamma_i, omega_i
    household_size = np.random.choice(
    [1,2,3,4,5,6,7],
    size=n_households,
    p=[0.29,0.35,0.16,0.13,0.04,0.02,0.01]
)


    n = np.sum(household_size)

    age_band = np.random.choice(age_bands, size=n, p=age_band_probs)
    susceptibility = np.array([susceptibility_by_age[a] for a in age_band])
    gamma_i = np.array([gamma * gamma_mult_by_age[a] for a in age_band])
    omega_i = np.array([omega * omega_mult_by_age[a] for a in age_band])


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
    recovered_time = np.full(n, -100000, dtype=int)

    state[initial_infected] = 1
    ever_infected = {initial_infected}
    adaptive_shopper = {}
    for i in range(n_households):
        adaptive_shopper[i] = None
    #print(adaptive_shopper)
    peak = 0
    wave_ct = []
    last_tot = 0
    for i in range(tot_day):
        infected_mask = state == 2
        infected_pop = state[infected_mask]
        susceptible_mask = state == 0
        susceptible_pop = np.where(susceptible_mask)[0]
        
        if len(infected_pop) > peak:
            peak = len(infected_pop)
        if day % re_int == 0 and day > 0:
            if len(susceptible_pop) > 0:
                wave_ct.append(len(ever_infected) - last_tot)
                last_tot = len(ever_infected)
                new_inf = np.random.choice(susceptible_pop)
                state[new_inf] = 1
                ever_infected.add(new_inf)
    
        state = one_day(state, day, strategy, ever_infected, adaptive_shopper, recovered_time)
        day = day + 1
    wave_ct.append(len(ever_infected) - last_tot)
    
    return wave_ct, len(ever_infected), n
total = 0
totall = 0
totalll = 0
totallll = 0
totalllll = 0
perc = 0
perc1 = 0
perc2 = 0
perc3 = 0
perc4 = 0
#s, f, p = sim(0, tot_day)
#total = f/p
#print("designated tot:", total)
#print("inf per wave:", s)

#q, w, l = sim(3, tot_day)
#totalll= w/l
#print("adaptive tot:", totalll)
trials=50
#print("inf per wave:", q)
for i in range(trials):
    
    s, f, p = sim(0, tot_day)
    total = f/p
    perc = (total/trials)+perc

    sa, fp, pf = sim(1, tot_day)
    totall = fp/pf
    perc1 = (totall/trials)+perc1

    sr, fr, pr = sim(2, tot_day)
    totalllll = fr/pr
    perc4 = (totalllll/trials)+perc4

    q, w, l = sim(3, tot_day)
    totalll= w/l
    perc2 = (totalll/trials)+perc2

    x, y, z = sim(4, tot_day)
    totallll= y/z
    perc3 = (totallll/trials)+perc3

print("designated tot:", perc)
print("rotation tot:", perc1)
print("random tot:", perc4)
print("adaptive tot:", perc2)
print("adaptive smart tot:", perc3)

#trials = 1000
#beta_values = np.arange(0.1, 1.1, 0.1)  
#results = {0: [], 1: [], 2: [], 3: []}
#for beta in beta_values:
    #beta_house = beta
#    beta_store = beta
#    beta_house = beta
#    for strategy in range(4):
#        inf = []
#        for i in range(trials):
#            s, f, p = sim(strategy, tot_day)
#            inf.append(f)
#            ppl.append(p)
#        total = np.mean([i/p for i,p in zip(inf, ppl)])
#        results[strategy].append(total)


#labels = {0: 'Designated', 1: 'Rotation', 2: 'Random', 3: 'Adaptive'}
#for strategy in range(4):
#    plt.plot(beta_values, results[strategy], label=labels[strategy], marker='o')

#plt.xlabel('Beta Store')
#plt.ylabel('Average total infected (%)')
#plt.title('Total population infected across transmission rates')
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
#plt.savefig('beta_sweep.png')
#plt.show()







#inf0 = 0
#inf1 = 0
#inf2 = 0
#inf3 = 0
#for i in range(5000):
#    inf0 = inf0 + sim(0)
#    inf1 = inf1 + sim(1)
#    inf2 = inf2 + sim(2)
#    inf3 = inf3 + sim(3)
#print("designated avg infected", (inf0/5000))
#print("rotation avg infected", (inf1/5000))
#print("random avg infected", (inf2/5000))
#print("adaptive avg infected", (inf3/5000))
#print("how much better:", inf3/inf0)




#at_store = [0,3,9,11]
#manually assigning people as sick
#states_array = np.array([0,1,0,2,0,0,0,2,0,1,0,0]) 

#creating arrrays that only include people in each category
#infected_mask = states_array == 2
#infected_pop = states_array[infected_mask]

#susceptible_mask = states_array == 0
#susceptible_pop = states_array[susceptible_mask]

#exposed_mask = states_array == 1
#exposed_pop = states_array[exposed_mask]

#print("total people =",infected_pop.size + exposed_pop.size + susceptible_pop.size) DEBUG LINE

#Finding the location of the infectious
#infectious_personID = np.where(states_array == 2)[0]
#infectious_loc = [house[key] for key in infectious_personID]
#print(infectious_personID)
#Code to verify gamma/the recovery mechanism
#N=len(states_array)
#tot_recovered = 0
#new_state = states_array.copy()

#for i in range(10000):
#    recovered_mask = (states_array == 2) & (np.random.random(N) < gamma)
#    new_state[recovered_mask] = 3
#    tot_recovered = tot_recovered + recovered_mask.sum() 
#print(tot_recovered/20000)








#create a dictionary where the key is the household number and the value is the number of sick in that house
#infected_pop = {}

#for person in at_store:
#    if states_array[person] == 2:
 #       loc = house[person]
  #      infected_pop[loc] = infected_pop.get(loc, 0) + 1
#print(infected_pop)
