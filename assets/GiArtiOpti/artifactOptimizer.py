import numpy as np

def f(x,y,z):
    return (1000*(1 + 0.466 + 0.058*x) + 311)*(1 + (0.361 + 0.039*y)*(0.5 + 0.078*z))
    

minRoll = 4;
x = np.linspace(minRoll, 24, 24-minRoll+1)
y = np.linspace(minRoll, 24, 24-minRoll+1)
z = np.linspace(minRoll, 30, 30-minRoll+1)
maxNumberOfRolls = 38

bestRoll = np.array([4,4,4])
maxDmg = 0;

for xn in range(len(x)):
    for yn in range(len(y)):
        for zn in range(len(z)):
            
            if x[xn] + y[yn] + z[zn] <= maxNumberOfRolls:
            
                dmg = f(x[xn], y[yn], z[zn])
                
                if dmg > maxDmg:
                    maxDmg = dmg
                    bestRoll = np.array([x[xn], y[yn], z[zn]])
                
                
print(bestRoll)