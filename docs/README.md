### Gather and Build Game 

Modelled as a Partially Observable Markov Game, where optimal solutions correspond to refinements of Nash quilibrias. 

#### LEVEL 1: Agents.

A 2D grid where agents can move to collect resources, and earn coins by selling or exchanging. 


Actions: Collect, Trade or Build. 

Observation: A world map with 4 quadrants, seperated by water. Four agents with given building skills and starting locations. 
1. *o_world* - spatial observations of the world.
2. *o_agent* - the public agent state (coins and resources) + private state (skills and labor)
3. *o_market* - the full market state, including avaialbe offer to buy/sell. 
4. *o_tax* - the tax rates effect.    

Rewards: Utility function over Money (directly propotional) and Labor (inversely propotional).

Agent Characteristics: Labor and Skill. 

Resources: Stone and Wood. 

#### Level 2: Social Planner. 

Social Planner which uses policy to improve social outcomes, in particular taxation together with redistribution.

The plannner determines a tax schedule T(z) over each tax period M for the net income of each agent Z, in that period. At the end of the taxation round
the collected tax is redistributed equally among all agents. The tax schedule T(z) is a brackated tax schedule over a pre-defined scheme. 

Actions: 

Observation: 

Rewards: Defined as an objective over Social Welfare Functions. 

