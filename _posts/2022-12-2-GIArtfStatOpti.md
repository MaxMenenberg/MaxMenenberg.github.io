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

I have been playing Genshin Impact (GI) since launch and I would say I have put a decent amount of time into the game (check out my [Enka](https://enka.network/u/605793099) ). Part of learning about the game for me involved following online content creators to see how they were playing and experimenting with the mechanics. Everyone who plays GI knows that upgrading artifacts is one of the most painful and nessesary mechanics to make strong characters and this makes for popular content online. When every I watch youtube videos or streamers upgrade their artifcats they always hope the substats level up to (also refered to as rolling) to either crit rate or crit damage. They always view an upgrade to attackas a a dissapointment. It's as if there is this assumption that for a typical build (i.e. ATK% Sands, Dmg Bonus Goblet, Crit Rate/Crit Damge Circlet) already has the optimal attack and all other resources should be allocated towards maximizing crit rate and crit damage. I don't think its obvious that there is no more need to allocate stats towards attack. In this blog post I will do a somewhat formal analysis of the damage formula and try to solve for what the optimal artifact substat distribution should be. 

## Damage Formula and Assumptions

Below I have provided a simplified version of the GI damage formula. This simplified formula assumes that LOTS of things are held constant and/or set to 0 or 1. Basically we are looking at the formula through the lens of hitting a speacial dev mode test dumming with a single attack from a character igoring things like passive buffs, elemental reactions, and other things like that. 

<div style="text-align:center;"><img src="/assets/GiArtiOpti/LateXEquations/dmgFormula.PNG"></div>

For those who aren't familiar, the crit rate (CR) and the crit damage (CD) values are multiplied together to represent long term average damage bonus from the crit stats. Its like asking the questions, "given the CR/CD pair I have, what would be an equivalent CD value for a CR = 100%?".

$$\{CR, CD\} = \{100\%, (CR)(CD)\}$$

