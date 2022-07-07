## A collection of Multi-Agent RL polices for the foundation/ai-aconomist Platform.

## Getting Started

## Introduction 

The game contains two main types of actors:

1. Agents - The agents represent individual actors who live in the environment, and their goal is to maximize their cumuluative earnings (coins) over an episode. Agents can choose to mine resources, build houses (or properties) or trade to earn coins. Each agents begins with a range of potential (or skill level) which determines how effective it would be in its chosen endeavour.

2. Planner - The planner acts indireclty in the environment by decding the tax schedule in a given period (an episode can have multiple periods). The agents are taxed according to this bracketed tax schedule at the end of each period and the accumulated wealth is redistributed. The objective of the planner is to maximize productivity while maintian social equality in the environment. 

## Envrionment

#### Agents 

1. Resources 
2. Properties 
3. Trade 

#### Planner 

## Implementations

### Scenario 1: The Extermes 

Two cases are presented here. In each of the cases, the planner works to acheive a given objective, while the agents work indepently to maximize their potential returns. The agents are independent and no assumption over the exchange of any information between the agents are made.  

#### Communism 

The objective of the planner in this scenario is to maximize the net social equality over an episode. At the end of each period (p=7), and choose an appropriate tax schedule such that the total social equality given by the following function is maximized. 

#### Capitalism 

The objectve of the planner in this scenario is to maximize the net productivity over an episode. At the end of each period (p=7), the planner choose an appropriate tax schedule such that the total prodictivy given by the following function is maximized. 
