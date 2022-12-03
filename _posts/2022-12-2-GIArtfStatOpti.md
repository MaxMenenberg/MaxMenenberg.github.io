---
layout: post
comments: true
published: true
title:  "Genshin Impact: Arifact Stats to Maximize Damage"
excerpt: "Most advice from Genshin Image (GI) influencers suggest that the best way to maximize damage is to 
invest all artifact substats towards crit rate and crit damage. I don't think this is correct and will discuss what the optimal 
stat distribution is."
date:   2022-12-02 01:00:00
---

## Introduction

I have been playing Genshin Impact (GI) since launch and I would say I have put a decent amount of time into the game (check out my [Enka](https://enka.network/u/605793099) ). Part of learning about the game for me involved following online content creators to see how they were playing and experimenting with the mechanics. Everyone who plays GI knows that upgrading artifacts is one of the most painful and nessesary mechanics to make strong characters and this makes for popular content online. One of the appealing aspects about optimizing artifacts in the GI community (as opposed to taking into account weapons and constellation) is that it's kmore or less an even playing field regardless how much players spend on the game. When every I watch youtube videos or streamers upgrade their artifcats they always hope the substats level up to (also refered to as rolling) to either crit rate or crit damage. They always view an upgrade to attackas a a dissapointment. It's as if there is this assumption that for a typical build (i.e. ATK% Sands, Dmg Bonus Goblet, Crit Rate/Crit Damge Circlet) already has the optimal attack and all other resources should be allocated towards maximizing crit rate and crit damage. I don't think its obvious that there is no more need to allocate stats towards attack. In this blog post I will do a somewhat formal analysis of the damage formula and try to solve for what the optimal artifact sub-stat distribution should be. 

## Damage Formula and Assumptions

Below I have provided a simplified version of the GI damage formula. This simplified formula assumes that LOTS of things are held constant and/or set to 0 or 1. Basically we are looking at the formula through the lens of hitting a speacial dev mode test dumming with a single attack from a character igoring things like passive buffs, elemental reactions, and other things like that. 

<div style="text-align:center;"><img src="/assets/GiArtiOpti/LateXEquations/dmgFormula.PNG"></div>

For those who aren't familiar, the crit rate (CR) and the crit damage (CD) values are multiplied together to represent long term average damage bonus from the crit stats. Its like asking the questions, "given the CR/CD pair I have, what would be an equivalent CD value for a CR = 100%?".

<div style="text-align:center;"><img src="/assets/GiArtiOpti/LateXEquations/CRCDEQ.PNG"></div>

I'm also going to assume the main stat triple for the sands, goblet, and circlet to be ATK%, DmgBonus%, and Crit Rate respectively. All of the methods I discuss in this post can be replicated on a different set of main stats. I thought about allowing the main stats to be variables to optimize, but that started to go down a path I didn't want to follow. Another assumption will be that the base attack of our test character will be 1000. This is a nice even number that is a reasonable value for 5-star character/weapon pairs. I'm also going to completely disregard flat attack sub-stat rolls because since we are assuming 1000 base attack we know the ATK% roll will always contribute a larger value than the flat attack roll. The last assumption will be that all artifacts will start with 4 sub-stats, all max rolls,every subsequent roll will be a max roll, and will always contain ATK%, CR, and CD if it can (e.g. the Crit Rate circlet cant have a crit rate sub-stat). This last assumption basically lets us turn on dev mode and just select the sub-stats we want. Just as a reminder the max rolls for  these stats are 

|  Sub-Stat   |   Max Roll  |
|-------------|-------------|
| ATK%        |    5.8%     |
| Crit Rate   |    3.9%     |
| Crit Damage |    7.8%     |


## Optimization Method

Since this post is about optimizing artifacts I'm going to re-write the damage formula to be a function of # of rolls into each substat. I'm also going to signficantly abbriviate the variables. I will also remove the DmgBonus% term from the goblet because it's just a constant with respect to optimizing the sub-stats.

<div style="text-align:center;"><img src="/assets/GiArtiOpti/LateXEquations/OptimizationFunction.PNG"></div>

Now we have a function of 3 variables that we just need to maximize, however there one main problem. 

