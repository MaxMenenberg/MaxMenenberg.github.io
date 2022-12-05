---
layout: post
comments: true
published: true
usemathjax: true
future: true
title:  "Genshin Impact: Deriving Optimal Artifact Sub-Stat Distribution For Maximum Damage"
excerpt: "Most advice from Genshin Image (GI) influencers suggest that the best way to maximize damage is to 
invest all artifact subs-tats towards crit rate and crit damage. In this post I will derive the optimal distribution of sub-stats."
date:   2022-12-04 01:00:00
---

## Introduction

I have been playing Genshin Impact (GI) since launch and I would say I have put a decent amount of time into the game (check out my [Enka](https://enka.network/u/605793099) ). Part of learning about the game for me involved following online content creators to see how they were playing and experimenting with the mechanics. Everyone who plays GI knows that upgrading artifacts is one of the most painful and necessary mechanics to make strong characters and this makes for popular content online. One of the appealing aspects about optimizing artifacts in the GI community (as opposed to taking into account weapons and constellation) is that it's more or less an even playing field regardless how much players spend on the game. When every I watch YouTube videos or streamers upgrade their artifacts they always hope the sub-stats level up to (also referred to as rolling) to either crit rate or crit damage. They always view an upgrade to attack a a disappointment. It's as if there is this assumption that for a typical build (i.e. ATK% Sands, Dmg Bonus Goblet, Crit Rate/Crit Damge Circlet) already has the optimal attack and all other resources should be allocated towards maximizing crit rate and crit damage. I don't think its obvious that there is no more need to allocate stats towards attack. In this blog post I will do a somewhat formal analysis of the damage formula and try to solve for what the optimal artifact sub-stat distribution should be. 

## Damage Formula and Assumptions

Below I have provided a simplified version of the GI damage formula. This simplified formula assumes that LOTS of things are held constant and/or set to 0 or 1. Basically we are looking at the formula through the lens of hitting a special dev mode test dummy with a single attack from a character ignoring things like passive buffs, elemental reactions, energy recharge/team rotation, and other things like that. 

<div style="text-align:center;"><img src="/assets/GiArtiOpti/LateXEquations/dmgFormula.PNG"></div>

For those who aren't familiar, the crit rate (CR) and the crit damage (CD) values are multiplied together to represent long term average damage bonus from the crit stats. Its like asking the questions, "given the CR/CD pair I have, what would be an equivalent CD value for a CR = 100%?".

<div style="text-align:center;"><img src="/assets/GiArtiOpti/LateXEquations/CRCDEQ.PNG"></div>

I'm also going to assume the main stat triple for the sands, goblet, and circlet to be ATK%, DmgBonus%, and Crit Rate respectively. All of the methods I discuss in this post can be replicated on a different set of main stats. I thought about allowing the main stats to be variables to optimize, but that started to go down a path I didn't want to follow. Another assumption will be that the base attack of our test character will be 1000. This is a nice even number that is a reasonable value for 5-star character/weapon pairs. I'm also going to completely disregard flat attack sub-stat rolls because since we are assuming 1000 base attack we know the ATK% roll will always contribute a larger value than the flat attack roll. The last assumption will be that all artifacts will start with 4 sub-stats, all max rolls,every subsequent roll will be a max roll, and will always contain ATK%, CR, and CD if it can (e.g. the Crit Rate circlet cant have a crit rate sub-stat). This last assumption basically lets us turn on dev mode and just select the sub-stats we want. Just as a reminder the max rolls for  these stats are 

<div style="text-align:center;"><img src="/assets/GiArtiOpti/LateXEquations/subStatMaxRolls.PNG" width="240" height="120"></div>


## Optimization Method

Since this post is about optimizing artifacts I'm going to re-write the damage formula to be a function of # of rolls into each sub-stat. I'm going to abbreviate the variables and also remove the DmgBonus% term from the goblet because it's just a constant with respect to optimizing the sub-stats.

<div style="text-align:center;"><img src="/assets/GiArtiOpti/LateXEquations/OptimizationFunction.PNG"></div>

Now the goal is to find the values of x, y, and z that maximize f(x,y,z) (to save time I'll sometimes abbreviate f(x,y,z) with f). The typical approach to solve this problem is to use calculus. For the single variable case (suppose we just have f(x)) we would find the value of x that maximizes (or minimizes) f(x) by solving the equation f'(x) = 0, where f'(x) is the derivative of f(x). However this won't work for our f because it clearly has no maximum. If this isn't obvious at first glance, pick a set of values for x, y, and z to try and make f and large as possible. Any values you pick, I can increase your choice for x, y, z, or any combination of the three and get a larger value for f. 

This is the point where we need to include the constraint of number of artifact rolls GI allows us to have. We all know we can't have 200 rolls into crit damage, because we only have 5 artifacts and they only can have at most 6 rolls into a sub-stat (the starting value + the 5 rolls from leveling). The constraint should have a form like x + y + z = total # of rolls. The total number of rolls is easy to calculate, we just need to add the starting rolls plus the number of rolls from leveling up. Remember and artifact can't have a sub-stat that is the same as its main stat. So for our (ATK%, DmgBonus%, Crit Rate) scenario our starting rolls will be 4 AKT%, 4 Crit Rate, and 5 Crit Damage, with a sum of 13 starting rolls. The remaining rolls can be calculated by (5 artifacts) x (5 rolls from level up) = 25. So the total number of rolls is 13 + 25 = 38. Now we have our constraint equation x + y + z = 38. It's worth mentioning not all combinations of x, y, and z that add up to 38 are valid. Obviously negative values don't make sense. Like I mentioned earlier sub-stats can't be the same as a main stat, so for example there can't be 38 rolls into ATK% (i.e. x = 38, y = 0, z = 0). For now I am just going to proceed ignoring these issue and address them once we start getting candidate solutions to the problem. 

<div style="text-align:center;"><img src="/assets/GiArtiOpti/LateXEquations/OptimizationProblem.PNG"></div>

Fortunately for this problem there is the well established method of [Lagrange multipliers](https://en.wikipedia.org/wiki/Lagrange_multiplier) which is specifically motivated by the problem of optimizing a function with respect to an equality constraint. Below I outline the process for using Lagrange multipliers given that you have a function to maximize f(x,y,z) and an equality constraint. For this outline I will explicitly write out all variables, but just know this method works regardless the number of variables. 

**Step #1:** Define $g(x,y,z)$ by "moving" all terms of the constraint equation to one side. I.e. $g(x,y,z) = x + y + z - 38$ 

**Step #2:** Define the Lagrangian function $\mathcal{L}(x,y,z,\lambda) = f(x,y,z) + \lambda g(x,y,z)$ 
$\mathcal{L}(x,y,z,\lambda) = (1000\times(1 + 0.466 + 0.058x) + 311)\times(1 + (0.361 + 0.039y)\times(0.5 + 0.078z)) + \lambda(x + y + z - 38)$ 

**Step #3:** Calculate the gradient of the Lagrangian $\nabla\mathcal{L}(x,y,z,\lambda) = \left( \frac{\partial\mathcal{L}}{\partial x}, \frac{\partial\mathcal{L}}{\partial y}, \frac{\partial\mathcal{L}}{\partial z}, \frac{\partial\mathcal{L}}{\partial \lambda}\right)$ 

$\frac{\partial\mathcal{L}}{\partial x} = 58 \times (1 + (0.361 + 0.039y)\times(0.5 + 0.078z)) + \lambda$ 

$\frac{\partial\mathcal{L}}{\partial y} = 0.039 \times (1000\times(1 + 0.466 + 0.058x) + 311)\times(0.5 + 0.078z) + \lambda$ 

$\frac{\partial\mathcal{L}}{\partial z} = 0.078 \times (1000\times(1 + 0.466 + 0.058x) + 311) \times (0.361 + 0.039y) + \lambda$ 

$\frac{\partial\mathcal{L}}{\partial \lambda} = x + y + z - 38$ 

**Step #4:** Construct a system of equations by setting $\nabla\mathcal{L}(x,y,z,\lambda) = 0$. I.E. $\frac{\partial\mathcal{L}}{\partial x} = 0 , \frac{\partial\mathcal{L}}{\partial y} = 0, \frac{\partial\mathcal{L}}{\partial z} = 0, \frac{\partial\mathcal{L}}{\partial \lambda} = 0$

$0 = 58 \times (1 + (0.361 + 0.039y)\times(0.5 + 0.078z)) + \lambda$ 

$0 = 0.039 \times (1000\times(1 + 0.466 + 0.058x) + 311)\times(0.5 + 0.078z) + \lambda$ 

$0 = 0.078 \times (1000\times(1 + 0.466 + 0.058x) + 311) \times (0.361 + 0.039y) + \lambda$ 

$0 = x + y + z - 38$ 

Once we are at **Step #4** there are 4 equations with 4 unknowns and the last step is to solve. I started trying to solve this by hand hoping to get a clean closed form solution...long story short it turned into a mess, and I gave up and used the source of all truth WolframAlpha. Giving these 4 equations to WolframAlpha's system of equation solver yielded 4 solutions.

Solution #1: $(x, y, z, \lambda) \rightarrow (-30.63, -12.99, 81.62, 0)$

Solution #2: $(x, y, z, \lambda) \rightarrow (-30.63, 78.78, -10.14, 0)$

Solution #3: $(x, y, z, \lambda) \rightarrow (6.81, 14.17, 17.01, -154.80)$

Solution #4: $(x, y, z, \lambda) \rightarrow (44.31, -4.57, -1.732, -61.86)$

Solutions 1, 2, and 4 clearly aren't valid because they have negative value for x, y, or z, which remember is suppose to describe how many rolls go into a certain sub-stat. Only solution 3 has an almost valid solution with the only issue being that our final values for x, y, and z must be integers (we don't need to worry about $\lambda$). This can be fixed easily with rounding, giving the solution of $(x, y, z) \rightarrow (7, 14, 17)$. This is telling us that the best sub-stats to maximize damage for ATK% Sands, DmgBonus% Goblet, and Crit Rate Circlet should be

$7 \times 0.058 = 0.406 \rightarrow ATK\; +40.6\% $

$14 \times 0.039 = 0.546 \rightarrow CRIT\;Rate +54.6\% $

$17 \times 0.078 = 1.326 \rightarrow CRIT\;DMG +132.6\% $

with the total Crit Rate = 90.7% and Crit Dmg = 182.6%, and with a total ATK% bonus of 87.2%. As a sanity check I wrote a python program that did a brute force search through all possible combinations of different sub-stat rolls for the simplified damage formula. As hoped, the program returns the same result as the solution from Lagrange multipliers. 

{% highlight python %}
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
#Returned Results
[ 7. 14. 17.]
{% highlight python %}

## Some Closing Comments

### Crit Ratio

One thing that has always bugged me about the GI community is how they have butchered the word *ratio*. People will always say things like "wow this guy has a really good crit ratio" in response to a character having high crit rate and crit damage. But this isn't how ratios work, if you want a ratio to be big you need to make one value big (the numerator) and the other value small (the denominator). However the notion of crits in genshin impact is a *product*, you want both values to be high such that when they are multiplied together the result is large. We should be taking about crit products, not crit ratios. 

I think some of the origin of the word ratio in the GI community come from the way the developers distribute crit rate and crit damage stats in the game. They come in these pairs that them selves that have a ratio of 2:1 (CritDmg:CritRate). We see this in artifact rolls, weapon sub-stats, and character ascension stats. There is also a common piece of advice that players should aim for their characters to have a 2:1 CritDmg/CritRate ratio which never made sense to me. Obviously 140%/70% and 200%/100% are both 2:1 CritDmg/CritRate ratios but we all know that one of them is better than the other. This just goes back to me complaining about the use of the word ratio. However, the ironic thing is that my finals results from Lagrange multipliers of Crit Rate = 90.7% and Crit Dmg = 182.6% perfectly fit that 2:1 advice that always bugged me. LOL. 

### Different Main Stats

The method in this post could be applied to different sets of main stats like (ATK%, ATK%, Crit Rate),  (ATK%, DmgBonus%, and Crit Dmg), (ATK%, ATK%, ATK%), to see which sub-stats are the best, and which main stats are the best. I can quickly mention that the case of (ATK%, DmgBonus%, and Crit Rate) and (ATK%, DmgBonus%, and Crit Dmg) are equivalent with some re-balancing of the sub-stats.

### The 311 Feather

If GI had no notion of flat attack and only had the ATK% stat, then there wouldn't be much of a point for having the damage bonus stat. I would love to get some insight in how the developers came up with the flat attack value for the feather and how it factored into their stat distributions and game balancing. If anyone know why they might have chose this value to be 311, and its broader consequences for the damage formula, please let me know. 


### Conclusion

Remember ATK% stat isn't that bad, and you didn't necessarily get unlucky if you missed a crit roll for an ATK%. I really like when games have their damage formulas published so players can effectivly optimize (or try) their characters. I hope you found this post interesting. 



