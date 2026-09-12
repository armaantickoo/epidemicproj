import sympy as sp
#beta, gamma, sigma = sp.symbols("beta gamma sigma", positive=True)
beta = 0.2
gamma = 0.1
sigma = 0.25
P_store = sp.Matrix([
    [1-sigma, sigma, 0,0,0,0,0,0,0],
    [0, (1-beta)*(1-gamma), beta*(1-gamma), beta*gamma, 0,0,0, gamma*(1-beta),0],
    [0,0,(1-sigma)*(1-gamma), gamma*(1-sigma), sigma*(1-gamma), sigma*gamma,0,0,0],
    [0,0,0,(1-sigma),0,sigma,0,0,0],
    [0,0,0,0,(1-gamma)**2, gamma*(1-gamma), gamma*(1-gamma),0, gamma**2],
    [0,0,0,0,0,(1-gamma),0,0,gamma],
    [0,0,0,0,0,0,(1-gamma),0,gamma],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1]
])
P_home =sp.Matrix([
    [1-sigma, sigma, 0,0,0,0,0,0,0],
    [0, (1-gamma), 0, 0, 0,0,0, gamma,0],
    [0,0,(1-sigma)*(1-gamma), gamma*(1-sigma), sigma*(1-gamma), sigma*gamma,0,0,0],
    [0,0,0,(1-sigma),0,sigma,0,0,0],
    [0,0,0,0,(1-gamma)**2, gamma*(1-gamma), gamma*(1-gamma),0, gamma**2],
    [0,0,0,0,0,(1-gamma),0,0,gamma],
    [0,0,0,0,0,0,(1-gamma),0,gamma],
    [0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1]
])


I = sp.Matrix([
    [1,0,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1]
])


P_comp = sp.simplify(P_store * P_home)
P_3day = sp.simplify(P_comp * P_home)
Q_3day = P_3day[0:7, 0:7]
N_inv = I-Q_3day
N = N_inv.inv()
#sp.pprint(N)

R = P_3day[0:7, 7:9]
B = sp.simplify(N*R)
row_sum = sum(B[0, :])
print(row_sum)
p_never_infected = sp.factor(B[0, 0])
print(p_never_infected)
states = ['(E,S)', '(I,S)', '(I,E)', '(R,E)', '(I,I)', '(R,I)', '(I,R)', '(R,S)', '(R,R)']
for i in range(7):
    for j in range(7):
        entry = sp.factor(N[i, j])
        if entry != 0:
            print(f"{states[i]} -> {states[j]}: {entry}")
