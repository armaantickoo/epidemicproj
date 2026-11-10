$\text{\large{Formula for the reproductive number in the store environment}}$

$$
R_{0, \text{store}} =
\frac{\sigma(1-\sigma)^2+\sigma(1-\sigma)(1-\gamma)+\sigma(1-\sigma)^2}
{1-(1-\sigma)^3} 
\times
\frac{\beta_s}
{1-(1-\gamma)^3(1-\beta_s)}
$$

This formula can be split into 3 main portions, $E_s$, $\frac{\sigma(1-\sigma)^2+\sigma(1-\sigma)(1-\gamma)+\sigma(1-\sigma)^2}
{1-(1-\sigma)^3}$ which for simplicities sake we will call $A$, and $\frac{\beta_s}
{1-(1-\gamma)^3(1-\beta_s)}$ which we will call $B$.  

The first portion, $E_s$ is very simple, as it is just the expected number of susceptible store visitors, which at time 0 is simply the number of households minus one, or $hh-1$. 

The second portion A, is nothing but the percentage of infected people infected on day 0, who are infectious on shopping days. To set this up, we can think about it as modulo 3, as shopping days happen every 3 days. The code dictates that shoppers go to the store, then have the chance to switch from the exposed stage to the infectious stage. This means that the probability of an infectious shopper on day 0 is 0. The residues mod 3 are {0,1,2} and they go in reverse order as there is 2 days that the shopper has to go through to reach the store, then 2 then 1. This means we can think of the weighting as the sum of 3 geometric series.
