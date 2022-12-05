import numpy as np

# Simplified Genshin damage formula
def f(x,y,z):
    return (1000*(1 + 0.466 + 0.058*x) + 311)*(1 + (0.361 + 0.039*y)*(0.5 + 0.078*z))
    

# Allowable range of rolls each sub-stat can have
minRoll = 4;
x = np.linspace(minRoll, 24, 24-minRoll+1) # ATK%
y = np.linspace(minRoll, 24, 24-minRoll+1) # Crit Rate
z = np.linspace(minRoll, 30, 30-minRoll+1) # Crit Dmg

# Can't have more rolls than this
maxNumberOfRolls = 38

# Brute force search for best sub-stats
bestSubStats = np.array([4,4,4])
maxDmg = 0;

for xn in range(len(x)):
    for yn in range(len(y)):
        for zn in range(len(z)):
            if x[xn] + y[yn] + z[zn] <= maxNumberOfRolls:
                dmg = f(x[xn], y[yn], z[zn])
                if dmg > maxDmg:
                    maxDmg = dmg
                    bestSubStats = np.array([x[xn], y[yn], z[zn]])
                                
print(bestSubStats)