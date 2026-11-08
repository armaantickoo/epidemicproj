Formula for the reproductive number in the household $R_{0,\text{house}}$

$$
R_{0,\text{house}} =
E_h(1-
\frac{(1-\beta_h)\gamma}
{1-(1-\gamma)(1-\beta_h)}
)
$$

where $E_h$ is the expected number of susceptible people in the household, which can also be written as $P_{\text{avg}}-1$ where $P_{\text{avg}}$ is the average number of people in each household. 
$\gamma$ is the recovery probability, and
$\beta_h$ is the household infectivity rate.

To derive this, we can think of it in 2 pieces, the probability that each person is infected, and the total number of people. With this thought process it becomes evident that our formula is nothing but

$$
E_h(p_{inf})
$$

where $p_{inf}$ is the probability of infection. we can also tell that $p_{inf}$ is simply equal to $1-p_{esc}$ where $p_{esc}$ is the probability that the person does not get infected. From here, we can realize that the probability of escaping the first day and the infectious person recovering is $\gamma(1-\beta_h)$ because the model triggers infection before recovery, and each subsequent day that probability is multiplied by $(1-\gamma)(1-\beta_h)$. Now we can recognize this is a geometric series of the form

$$
p_{esc} = \sum_{i=1}^{n} \gamma(1-\beta_h)^{i}(1-\gamma)^{i-1}
$$

where $n$ is the total number of days that have passed. Now because both $\gamma$ and $\beta_h$ are positive and less than one, we can find the series sum as n goes to infinity. The sum is of the form

$$
p_{esc} =
\frac{\gamma(1-\beta_h)}
{1-(1-\gamma)(1-\beta_h)}
$$

which plugging into $E_h(1-p_{esc})$ gives us our original formula for $R_{0,\text{house}}$






