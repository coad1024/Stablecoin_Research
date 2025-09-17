Improving DeFi Mechanisms with Dynamic Games and Optimal
Control: A Case Study in Stablecoins

Nicholas Strohmeyer
The University of Texas at Austin
Austin, United States
nstrohmeyer@utexas.edu

Sriram Vishwanath
The University of Texas at Austin
Austin, United States
sriram@utexas.edu

David Fridovich-Keil
The University of Texas at Austin
Austin, United States
dfk@utexas.edu

4
2
0
2

t
c
O
8
2

]
T
G
.
s
c
[

1
v
6
4
4
1
2
.
0
1
4
2
:
v
i
X
r
a

ABSTRACT
Stablecoins are a class of cryptocurrencies which aim at providing
consistency and predictability, typically by pegging the token’s
value to that of a real world asset. Designing resilient decentral-
ized stablecoins is a challenge, and prominent stablecoins today
either (i) give up on decentralization, or (ii) rely on user-owned
cryptocurrencies as collateral, exposing the token to exogenous
price fluctuations. In this latter category, it is increasingly common
to employ algorithmic mechanisms to automate risk management,
helping maintain the peg. One example of this is Reflexer’s RAI,
which adapts its system-internal exchange rate (redemption price)
to secondary market conditions according to a proportional con-
trol law. In this paper, we take this idea of active management a
step further, and introduce a new kind of control scheme based
on a Stackelberg game model between the token protocol and its
users. By doing so, we show that (i) we can mitigate adverse depeg
events that inevitably arise in a fixed-redemption scheme such as
MakerDao’s DAI and (ii) generally outperform a simpler, adaptive-
redemption scheme such as RAI in the task of targeting a desired
market price. We demonstrate these results through extensive sim-
ulations over a range of market conditions.

KEYWORDS
Decentralized Finance, Stablecoin, Stackelberg Game

1 INTRODUCTION
Decentralized Finance (DeFi) utilizes blockchain technology to pro-
vide financial services through secure, peer-to-peer transactions,
eliminating the need for intermediaries [56]. Although DeFi has sig-
nificant potential, many cryptocurrencies experience high volatility,
reducing their effectiveness as a reliable medium of exchange. Sta-
blecoins, a subset of digital currencies, are designed to counter
this volatility by pegging their value to real-world assets like the
US dollar. However, maintaining a stable peg while preserving de-
centralization presents a challenge, typically addressed through
two flawed approaches. The first method involves backing the sta-
blecoin with exogenous, on-chain assets, which are often volatile
cryptocurrencies that introduce additional risk. The second method
employs algorithmic mechanisms to maintain the peg via auto-
mated monetary policy, but these systems can be fragile and have
failed during crises [15].

A key component of stablecoin systems is the process of token
creation (“minting”) and redemption (“burning”). This usually in-
volves a transaction between the protocol and participants, where a
basket of collateral assets is exchanged for new tokens, or vice versa.
When the rate of minting and burning aligns with market supply

and demand, the peg is maintained. However, if there is a significant
imbalance in this exchange, the stablecoin risks “depegging.”

To address such imbalances, the protocol may adjust the endoge-
nous rate at which participants can exchange stablecoin tokens for
the underlying collateral assets—referred to as the redemption price.
This alters the incentive structure for participants. For example,
increasing the redemption price raises the future expected cost
of recovering collateral, encouraging participants to burn, while
lowering the price has the opposite effect. By modulating the re-
demption price, the protocol can indirectly influence token supply
dynamics.

Several past stablecoins have implemented variable redemption
price mechanisms [1, 9, 36, 37]. A particularly relevant example
is Reflexer’s RAI [36], which uses a feedback control law to con-
tinuously adjust based on market conditions. Reflexer’s controller
updates the redemption price at a rate proportional to its current
deviation from the market price, allowing RAI to maintain relative
stability while staying fully decentralized. This contrasts with its
predecessor, DAI, which uses a fixed redemption price and has
increasingly had to rely on fiat-backed assets in recent years [17].
However, RAI does not target a fixed peg value; instead, its goal is
to align the redemption and market price movements. Despite this,
RAI’s success highlights the potential of feedback control mecha-
nisms in stablecoin systems.

Our main contribution in this paper is to introduce a novel
feedback control scheme for dynamically updating the redemption
price of a decentralized stablecoin system. Like Reflexer’s RAI, we
incorporate feedback signals from the market to inform future de-
cisions. Unlike Reflexer, we leverage domain-specific insights to
model the supply dynamics of decentralized stablecoins, enabling
us to use techniques from optimal control. Specifically, we capture
the effect of protocol redemption price decisions on the behavior of
system participants as a dynamic Stackelberg game [39, 55] and for-
mulate this as a mathematical program with equilibrium constraints
[42]. Lastly, we demonstrate how to efficiently find first-order equi-
librium solutions to the resulting optimization problem.

To assess our design, we implement it using a receding horizon
approach, re-solving for the optimal sequence of redemption rates
over a finite future window at each time step, and applying the
first rate from that sequence. We compare this approach against
two existing methods: a fixed-rate scheme based on DAI and a
proportional control scheme based on RAI. Our results show that
the Stackelberg controller reduces the volatility of the stablecoin’s
market price in simulations relative to an arbitrary peg value and
enables faster recovery from market shocks when compared to the
two baselines.

2 BACKGROUND
The breakthrough innovations of Bitcoin in 2009 and Ethereum
in 2015 led to the emergence of DeFi. The former ushered in a
new way of conducting peer-to-peer transactions using blockchain
technology while the latter introduced smart contracts, allowing
for specific sets of rules to be executed automatically on-chain. DeFi
has since grown into a complex, integrated system of applications
supporting many traditional functions of institutional finance [28,
50]. In 2014, Tether introduced the first stablecoin (USDT) which
uses the classic model of targeting a 1:1 peg to the US dollar. More
broadly, a stablecoin can be pegged to a variety of real world assets,
such as other fiat currencies, commodities, precious metals, real
estate, etc. [46]. Stablecoins play a critical role in the emerging
crypto-economy since they serve as safe-haven assets [8, 23].

2.1 Stablecoin Design Paradigms
While most stablecoins have the same (or similar) end goals, their
designs can vary drastically. To understand the many designs that
exist today, a useful, first distinction is to separate custodial from
non-custodial stablecoins [19, 32].
Custodial Stablecoins rely on a central entity to maintain reserves
of real-world assets from which the on-chain token derives its
stability. This is generally effective, but a key drawback is that
decentralization is sacrificed in order to maintain the peg. Also,
backing a stablecoin with a reliable fiat currency is still no guarantee
of stability and there has been history of these tokens temporarily
losing their peg [4–6]. Despite this, custodial tokens dominate the
stablecoin market where today Tether’s USDT and Circle’s USDC
make up roughly 86% of total market cap [16].
Non-custodial stablecoins, on the other hand, seek to maintain
a peg while preserving system decentralization. These stablecoins
can be further broken down into two sub-categories corresponding
to the strategies used for supporting the peg.

Crypto-backed stablecoins maintain decentralization by using
cryptocurrencies as system collateral rather than resorting to the
safer choice of fiat currencies. However this increases risk exposure,
and the system must rely on several additional design features to
help mitigate this.

Algorithmic stablecoins rely solely on incentive-based mecha-
nisms and endogenous system value (“seigniorage shares") to main-
tain their peg. They have become somewhat notorious due to sev-
eral past depegs and failures (TerraUSD [41], NuBits[53] and Iron[1],
among others). Such events have called into question the viability
of total reliance on algorithmic mechanisms [15] and have moti-
vated the growing popularity of so-called hybrid models [31, 36],
which use a combination of both crypto-backing and algorithmic
operations.

2.2 Crypto-backed Stablecoins (DAI)
MakerDAO’s DAI [52] is a leading example of a crypto-backed
stablecoin model and serves as a useful case to highlight key design
principles, risks, and mitigation strategies. In its initial version,
DAI was backed solely by Ethereum. To manage Ethereum’s price
volatility, MakerDAO implemented an over-collateralization system,
meaning that the total market value of the collateral assets exceeds
the value of the tokens in circulation.

DAI’s minting process functions as a lending agreement between
the protocol and participants. The main incentive for participants,
which we refer to as “speculators,” is to make leveraged bets on
the long-term value of Ethereum. They do this by opening a col-
lateralized debt position (CDP) with MakerDAO, which requires
them to deposit initial collateral worth 𝛽𝑁 (where 𝛽 > 1 is the
minimum collateral ratio set by MakerDAO) to mint 𝑁 tokens. This
mechanism distributes system collateral ownership across multiple
speculators and ensures over-collateralization is maintained when
positions are created.

The speculator’s assets are locked in the CDP (also referred to
as a “vault") until they are either redeemed or liquidated. The latter
occurs if ever the speculator’s vault falls below the minimum re-
quired ratio 𝛽, in which case the vault is auctioned off (typically at
a loss). Vault redemption is the reverse process of creation in which
a speculator recovers their collateral by returning the borrowed
DAI (usually plus some interest e.g. "stability fee" in MakerDao).
Specifically, in a single-collateral system, when the speculator re-
turns some fraction of the 𝑁 borrowed tokens, they recover the
proportionate quantity of the collateral asset invested.

2.3 The Role of the Redemption Price
Consider the decision faced by the speculator. Assuming they sell
new tokens created from the process above to make leveraged bets
on ETH, then, when they decide to redeem, they will need to buy
𝑡 > $1,
those tokens back at the market price 𝑝Stb
this could result in a loss if they borrowed tokens at a redemption
price of $1 (as is the case with DAI). However, the opposite is true
when (cid:98)

𝑡 < $1, where the difference is in their favor.
𝑝Stb

. Supposing 𝑝Stb

𝑡

2.4 Deleveraging Risk and Dynamics
Collateral devaluation due to market fluctuations is a primary
source of risk in crypto-backed stablecoins. Prior works [33, 34]
have highlighted a particular phenomenon, known as a “deleverag-
ing spiral," which can occur when a large number of vault-owners
face immediate risk of liquidation. This triggers a spike in market
demand as these owners rush to buy back the tokens needed to
settle their positions. Interestingly, [33] predicted this pattern prior
to these exact dynamics playing out in the MakerDao system during
the infamous “Black Thursday" crisis. The authors also pointed out
that reducing the cost of redemption during extreme deleveraging
could alleviate buying pressure and that such a technique could be
used as a mitigation strategy.

3 PRELIMINARIES AND RELATED WORK
This section provides a formal definition of proportional-integral-
derivative (PID) control and how it is used specifically in Reflexer’s
autonomous redemption price setting mechanism. This discussion
motivates the use of optimal control as an alternative. We also
highlight several key related works which have studied similar
problems in the context of DeFi protocols, token based economies
and leader-follower economic models.

3.1 PID Control
Proportional-integral-derivative (PID) control is a feedback control
technique which determines the input to a dynamical system in

proportion to an “error” signal 𝑒, its integral over time, and its time
derivative. In discrete-time, this takes the following form:

𝛿𝛼𝑡 = 𝐾𝑝𝑒𝑡 + 𝐾𝐼

𝑡
∑︁

𝜏=𝑡 −𝑇

𝑒𝜏 + 𝐾𝑑

(cid:18)
𝑒𝑡 − 𝑒𝑡 −1

(cid:19)

(1)

Reflexer’s controller uses only the left-most (proportional) term,
dropping the integral and derivative terms. This can be described
by 𝛿𝛼 = 𝐾𝑝𝑒𝑡 , where the control input 𝛿𝛼𝑡 is the rate of change
to the redemption price 𝛼𝑡 , 𝐾𝑝 > 0 is the constant gain factor set
by the protocol, and 𝑒𝑡 = 𝛼𝑡 − 𝑝Stb
is the difference between the
redemption price 𝛼𝑡 and the market price of the stablecoin.

𝑡

𝑡

𝑡

The goal of this design is to drive the difference between 𝑝Stb
> 𝛼𝑡 → 𝑒𝑡 <
and 𝛼𝑡 smoothly to 0. For instance, when 𝑝Stb
0, the derived redemption rate 𝛿𝛼𝑡 is negative, and 𝛼𝑡 decreases
proportionally to the magnitude of 𝑒𝑡 . As 𝛼𝑡 decreases, system debt
becomes cheaper and the incentive for speculators to mint tokens
increases. Meanwhile token holders in the secondary market have
an incentive to sell as they expect the near-future market value to
decrease. These forces combine to push 𝑝Stb
back towards 𝛼𝑡 . In
the limit 𝑡 → ∞, both 𝑒𝑡 , 𝛿𝛼𝑡 → 0 and a temporary equilibrium is
𝑡 < 𝛼𝑡 .
met where 𝑝Stb
In addition to Reflexer, there are other examples of proportional
(P) and proportional-integral (PI) control across DeFi [22] such as
in the Mars [44] and Euler [20] lending protocols. While they are
straightforward to implement and computationally efficient, PID
controllers are not built around any notion of optimality, leaving
an opening for improvement.

𝑡 = 𝛼𝑡 . The opposite pattern occurs when 𝑝Stb

𝑡

3.2 Optimal Control
In this work, we design a redemption price controller in terms of an
optimization problem. This is inspired by past works [2, 11, 14, 49]
which have approached related DeFi problem settings from the
perspective of optimal control. Optimal control enables designers
to encode their goals, such as minimizing fluctuations around the
peg, into tailored cost functions while adding system dynamics and
key features, such as specified bounds, as constraints.

The resulting controller is not just reactive (as is the case for
PID) but also predictive. In particular, it can make use of arbitrarily
complex forecasting models and solve a corresponding optimal
control problem over a user-specified time interval extending into
the future. Meanwhile, by re-solving the forward-looking problem
at each time 𝑡, the resulting controller is still always responsive to
new market observations.

To illustrate, consider that token demand is trending up and is
expected to continue increasing. In this case, the protocol can decide
to reduce the current redemption price to preemptively keep pace
with the anticipated growth. On the other hand, when the realized
demand trajectory inevitably differs (ideally very little) from the
forecast, the solution to the optimization problem at the next step
corrects for the difference. This means feedback and short-term
prediction are integrated into every control decision, a powerful
advantage of this approach over PID control.

The technique just described is often referred to as receding
horizon or model predictive control [3, 21], and it is widely used,
appearing in both engineering [48, 51] and financial applications
[26, 27, 54]. Despite this, it is relatively unexplored in DeFi, with

Symbol

Definition

𝑆𝑡
Δ𝑡
(cid:98)𝐷𝑡
𝛼𝑡
𝛿𝛼𝑡
𝐶𝑡
𝑝𝐶
𝑡 ,
,
𝑝Stb
𝑡

𝑝𝐶
𝑡
(cid:98)
𝑝Stb
𝑡
(cid:98)

𝑟𝑡
Γ𝑡

Total stablecoin supply at time 𝑡

Change in supply; speculator’s burn/mint decision
Market demand forecast 𝑇 steps ahead of current 𝑡

System redemption price, protocol’s state variable
One-step change in 𝛼𝑡 , protocol’s decision variable
Total quantity of collateral assets in CDP’s at 𝑡

Collateral asset market price / forecast

Stablecoin market price / forecast
Collateral one-step returns (cid:0)𝑝𝐶
𝑡 +1/𝑝𝐶
𝑡
System Collateralization Ratio at 𝑡: (𝐶𝑡 𝑝𝐶

(cid:1)

𝑡 )/(𝛼𝑡 𝑆𝑡 )

the exception of a few notable works which have demonstrated its
utility in designing algorithmic policy [14, 49] and setting interest
rates in lending/borrowing applications [11].

3.3 Stackelberg Equilibrium Model
Implementing the method from the preceding section requires an
effective model of decentralized stablecoin dynamics. Recent work
[2] shows that the evolution of a token-based economy can be
accurately captured by a dynamical system driven by the decisions
of a central controller and its primary participants. Analogously,
the supply dynamics of a CDP-backed stablecoin are driven by the
primary market interaction between the protocol and speculators.
Inspired by this, we choose to model the interaction as a dynamic
Stackelberg game [55] where the protocol acts as a leader, which sets
the redemption price at each time 𝑡, and the speculators, modeled
as a single follower, who burn and mint based on this price in an
effort to maximize their expected wealth.

Game-theoretic, leader-follower relationships are naturally struc-
tured as bilevel optimization problems [2, 10, 18] in which a subset
of decision variables of an upper-level are constrained to lie within
the solution set of a lower-level problem. Bilevel optimization ap-
pears frequently in economic settings as it can capture this notion
of agents responding to common, central incentives. Some appli-
cations include optimal pricing [13, 35], efficient network design
[29, 43], and energy market models [57, 58] among many others
[30].

4 METHODS
We now formalize the dynamic Stackelberg game model of a decen-
tralized crypto-backed stablecoin. At each step 𝑡, the key quantities—
or state variables—update according a discrete-time dynamical sys-
tem driven by net burns/mints Δ𝑡 and the exogenous market price
of collateral 𝑝𝐶
𝑡 . The speculator’s decision Δ𝑡 is affected by the cur-
rent redemption price 𝛼𝑡 ; the protocol anticipates this, accounting
for the speculator’s best response in its own decision for 𝛼𝑡 . This
dynamic interaction is organized into a single bilevel optimization
problem which is solved over a finite time horizon of 𝑇 ∈ N future
steps.

4.1 Protocol Objective
The protocol’s main objective is to maintain the target 𝑝peg. This is
translated into minimizing a sum of squared errors (𝑒peg
) between
𝑡
) and the target price (𝑝peg)
𝑝Stb
predicted market stablecoin prices ((cid:98)
𝑡
( (cid:98)𝐷𝑡 , 𝑆𝑡 ) − 𝑝peg(cid:105)
at each step 𝑡 ∈ {0, 1, . . . ,𝑇 }, where 𝑒peg
.
Meanwhile, the protocol’s control variable is the step-wise change
to redemption price 𝛿𝛼. Motivated by Reflexer [36], we model the
speculator’s reaction to 𝛿𝛼 as a proportional response and thus
introduce a bi-linear term 𝛿𝛼𝑒peg
to the protocol’s cost function.
Generally desiring smooth updates to the redemption price, we add
a term which penalizes large values of 𝛿𝛼 by weight 𝜔𝑝 . In full, the
protocol’s cost is given by the following:
𝑇
∑︁

(cid:104)
𝑝Stb
𝑡
(cid:98)

=

𝑡

𝑡

(cid:2)(𝑒peg
𝑡

)2 + 𝜔𝑝 · 𝛿𝛼 2

𝑡 + 𝛿𝛼𝑡 · 𝑒peg

𝑡

(cid:3) .

𝐽 Ptcl =

(2)

𝑡 =0

Remark: In our implementation of (2), we adapt 𝜔𝑝 to relax
falls outside a tolerance threshold. For
| > .01, then 𝜔𝑝 = 1, otherwise

the penalty whenever 𝑒peg
example, we chose that if |𝑒peg
𝜔𝑝 = 1/|𝑒peg

𝑡

𝑡

|.

𝑡

4.2 Speculator Objective
The speculator’s control variable is the change in token supply
(Δ𝑡 ) at time 𝑡 where the sign of Δ𝑡 indicates whether the action
was a net mints or net burn. We model the decision as a utility
maximization problem. In [33], the authors model the speculator’s
expected long-term extractable wealth after a single decision Δ𝑡 as
follows:

𝑊𝑡 +1 = 𝑟𝑡

(cid:16)
𝐶𝑡 𝑝𝐶

𝑡 + 𝑝Stb

𝑡 Δ𝑡

(cid:17)

− 𝛼𝑡 (𝑆𝑡 + Δ𝑡 ) .

(3)

Inspection of (3) reveals that 𝑊𝑡 +1 is the value of the speculator’s
collateral assets at 𝑡 minus their liabilities (the token supply at the
current redemption level 𝛼𝑡 ).

Next, we assume the speculator acts as if maximizing 𝑊𝑡 +1 by
greedily maximizing the sum of discounted marginal gains at each
step. The marginal gain at 𝑡 can be derived from (3) by dropping
the terms which do not depend on Δ𝑡 . By replacing 𝑟𝑡 , 𝑝Stb
𝑡 with
and adding the discount factor 𝛾, we obtain the
𝑟𝑡 ,
forecasts (cid:98)
following:

𝑝Stb
𝑡
(cid:98)

on differences between the endogenous redemption price and the
token’s market price.

4.3 System Dynamics
State variables evolve over a single transition, driven by agent
decisions

𝛼𝑡 +1 =𝛼𝑡 + 𝛿𝛼𝑡
𝑆𝑡 +1 =𝑆𝑡 + Δ𝑡

𝐶𝑡 +1 =𝐶𝑡 +

𝑝Stb
𝑡
𝑝𝐶
𝑡

Δ𝑡

(6a)

(6b)

(6c)

𝑝Stb
𝑡 /𝑝𝐶
𝑡

The ratio (cid:98)

is the instantaneous conversion factor between
the token and the collateral asset at time 𝑡. Equation (6c) therefore
implies that, whenever the speculator burns or mints stablecoins,
they are instantaneously converting to or from the collateral asset.
Constraint Equations (6a) to (6c) are central to the model predic-
tive approach, as they allow for a trajectory of actions to be jointly
optimized over a horizon of 𝑇 time steps into the future. Since up-
dates depend on future market observations (𝑝Stb
𝑡 ), which are
unknown at present (time 𝑡 = 0), we replace the actual values with
𝑝Stb
forecasts (cid:98)
𝑡

𝑝𝐶
𝑡 .
(cid:98)

, 𝑝𝐶

𝑡

,

4.4 Minimum Vault Constraint
The vault collateralization ratio is given by Γ𝑡 = 𝐶𝑡 𝑝𝐶
𝑡 /𝛼𝑡 𝑆𝑡 . The
speculator must always ensure Γ𝑡 ≥ 𝛽𝑡 to avoid liquidation. As is
the case with DAI Section 2.2, we set a constant 𝛽𝑡 = 1.5 ∀𝑡.

4.5 Bilevel Problem
Next, we compile the preceding sections into a single bilevel for-
mulation. For compactness, variables and constraints are collected
according to their corresponding level, so 𝑥𝑡 := [𝛼𝑡 , 𝛿𝛼𝑡 ] ∈ R2 and
𝑦𝑡 := [𝑆𝑡 , 𝐶𝑡 , Δ𝑡 ] ∈ R3 are the upper-level (protocol) and lower-
level (speculator) variables, respectively, at time 𝑡.

Then, 𝒙 := [𝑥0, 𝑥1, . . . , 𝑥𝑇 ] ∈ R2𝑇 and 𝒚 := [𝑦0, 𝑦1, . . . , 𝑦𝑇 ] ∈
R3𝑇 are the upper and lower variables concatenated over all steps
𝑡 ∈ {0, 1, . . . ,𝑇 }.

The upper-level dynamics (6a) are collected into the map 𝐺 :

R𝑇 → R𝑇

𝑈 Spec =

𝑇 −1
∑︁

𝑡 =0

𝛾𝑡 (cid:16)

𝑝Stb
𝑡 − 𝛼𝑡

𝑟𝑡 (cid:98)
(cid:98)

(cid:17) Δ𝑡 .

(4)

𝐺 (𝒙, 𝒚) :=

(cid:104)
𝛼𝑡 +1 − 𝛼𝑡 − 𝛿𝛼𝑡

(cid:105)𝑇
𝑡 =1

∈ R𝑇 .

(7)

Lastly, in a system with an adaptive redemption price, the specu-
𝑝Stb
lators will naturally make arbitraging trades tending to align (cid:98)
𝑡
with 𝛼𝑡 . We encode this notion as a quadratic “penalty" term, which
the speculator tries to minimize. The overall utility is thus given as
follows:

𝑈 Spec =

𝑇 −1
∑︁

𝑡 =0

𝛾𝑡 (cid:16)

𝑝Stb
𝑡 − 𝛼𝑡

𝑟𝑡 (cid:98)
(cid:98)

(cid:17) Δ𝑡 + 𝑤𝑆 [𝛼 (𝑡) − 𝑝 (Δ𝑡 )]2

(5)

where 𝑤𝑆 is a configurable weight parameter, which we set to 1.
In summary, the first term represents a greedy maximization of
long term wealth and depends on exogenous collateral prices, while
the second term represents presence of arbitrageurs capitalizing

Similarly, the lower-level dynamics (6b), (6c) map 𝑔 : R2𝑇 → R2𝑇
is:

(cid:2)𝑆𝑡 − 𝑆𝑡 −1 − Δ𝑡 −1

𝑔(𝒙, 𝒚) :=







and the vault constraint (Section 4.4)

𝑝Stb
(cid:2)𝐶𝑡 − 𝐶𝑡 −1 − (cid:98)
𝑡
𝑝𝐶
𝑡
(cid:98)

(cid:3)𝑇
𝑡 =1
(cid:3)𝑇
𝑡 =1

Δ𝑡 −1

∈ R2𝑇








ℎ(𝒙, 𝒚) :=

(cid:104) 𝐶𝑡 (cid:98)
𝑝𝐶
𝑡
𝑆𝑡

− 𝛽𝑡

(cid:105)𝑇
𝑡 =0

∈ R𝑇 .

(8)

(9)

Lastly, the upper and lower objectives are given by 𝐹 (𝒙, 𝒚) :=
𝐽 Ptcl and 𝑓 (𝒙, 𝒚) := −𝑈 Spec, where we negate 𝑈 Spec so that both
agents are minimizing. We can now express the bilevel problem in

compact notation.

(𝒙∗, 𝒚∗) ∈ arg min

𝒙, ˜𝒚

𝐹 (𝒙, ˜𝒚)

s.t.𝐺 (𝒙, ˜𝒚) = 0
˜𝒚 ∈ arg min

𝒚

𝑓 (𝒙, 𝒚)

s.t. 𝑔(𝒙, 𝒚) = 0
ℎ(𝒙, 𝒚) ≥ 0

(10a)

(10b)

(10c)

(10d)

(10e)

𝑡 = 𝑝Stb
𝑝Stb

A solution (𝒙∗, 𝒚∗) to (10) is a Stackelberg equilibrium. We note
that, by setting (cid:98)
(the current market price observation),
across all time steps in (6c), the lower level problem in (10) becomes
linear (and convex) in 𝑦. This slight approximation to problem (10)
will ensure that the algorithm we employ for solving (10) finds a
local minimizer [10, 18].

0

4.6 Transforming Problem (10)
It is well-known that bilevel formulations can be transformed into
a single-level optimization problem by replacing the lower level
problem in (10) with its Karush-Kuhn-Tucker (KKT) conditions
[10, 18]. To this end, we first introduce the speculator’s Lagrangian:

L = 𝐽 Spec − 𝝀

(11)
where 𝝀 ∈ R2𝑇 and 𝝁 ∈ R𝑇 are dual variables. Now, (10) can be
rewritten as:

⊺𝑔(𝒙, 𝒚) − 𝝁

⊺ℎ(𝒙, 𝒚)

𝐹 (𝒙, 𝒚)

min
𝒙,𝒚,𝝀,𝝁
subject to 0 = 𝐺 (𝒙, 𝒚)

0 = ∇𝒚 L (𝒙, 𝒚, 𝝀, 𝝁)
0 = 𝑔(𝒙, 𝒚)
0 ≤ 𝝁 ⊥ ℎ(𝒙, 𝒚) ≥ 0 .

(12a)

(12b)

(12c)

(12d)

(12e)

Line (12e) makes Problem (12) a special case of a broader class
of problems known as mathematical programs with complementar-
ity constraints (MPCC) [42]. In practice, an MPCC can be difficult
to solve due to the non-smoothness induced by the complemen-
tarity constraints. However, techniques for solving MPCC’s are
well-studied [7, 24, 40]. In particular, one can introduce a slack
variable 𝝐 ∈ R𝑇 [24] and replace (12) with the following relaxation:

𝐹 (𝒙, 𝒚)

min
(𝒙,𝒚,𝝀,𝝁 )
subject to 𝐺 (𝒙, 𝒚) = 0; 𝑔(𝒙, 𝒚) = 0

(13a)

(13b)

(13c)

(13d)

∇𝒚 L (𝒙, 𝒚, 𝝀, 𝝁) = 0
ℎ(𝒙, 𝒚) ≥ 0; 𝝁 ≥ 0
⊺ℎ(𝒙, 𝒚) − 𝝐 = 0 .
𝝁
, 1𝑇 −1(cid:105)
We initialize 𝝐 =
and solve (13) iteratively, grad-
ually reducing 𝝐 → 0 and tightening (12e) at every step while using
the solution from the prior iteration to warm-start the next. This
will not always lead to an exact solution, but will often converge
to an accurate approximation. The procedure is given explicitly
within the inner loop of Algorithm 1.

(13e)

. . .

1,

(cid:104)

Algorithm 1: Relaxed Receding Speculator Game
1 𝑆0, 𝐶0, 𝛼0,

, 𝜇tol,𝑇 ← Initial State, Price Forecasts,

,

𝑝𝑆
(cid:98)
0

𝑝𝐶
(cid:98)
0

Solver Tolerance, Time Horizon

// Reset 𝜖

2 while 𝑡 < ∞ do
𝝐 ← 1 ;
3
for 𝑛 = 1 to 10 do
(cid:16)

4

x∗, y∗(cid:17)
z∗ =
if ||z∗ − z∗

5

6

7

8

9

10

11

12

13

← Solve relaxed Problem (13)

𝒕 −1||2 < 𝜇tol then

𝛼𝑡 ← Select from first time step of x∗ break

else

// Gradually reduce 𝝐 → 0

𝝐 ← 1
2 𝝐 ;
𝒕 −1 ← z∗
z∗
Δ, 𝑝𝐶
𝑡 , 𝑝𝑆
𝑡 ← Get Market Observations
𝑝𝐶
𝑝𝑆
𝑡 ← Update forecasts from 𝑝𝐶
𝑡 , 𝑝𝑆
𝑡 ,
𝑡
(cid:98)
(cid:98)
𝑡 , 𝑝𝑆
𝑆𝑡 , 𝐶𝑡 ← From 𝑝𝐶

𝑡 , Δ, 𝛼 using (6b), (6c)

5 EXPERIMENTS
We benchmark the bilevel redemption price controller (which we
label “UTAI") against two baselines. The first of these (“DAI") fixes
the redemption price at $1. The second baseline (“RAI") adapts the
redemption price according to equation (1).

5.1 No Arbitrage
We test in scenarios with both low and high volume of market arbi-
trage activity. This is because in a market with ample arbitrage and
perfect efficiency, the $1 constant redemption price is theoretically
optimal, as arbitrageurs constantly eliminate price discrepancies.
We expect UTAI to select a similar policy of relatively fixed re-
demption prices in this setting. Without arbitrageurs, on the other
hand, the protocol will have to adapt redemption price more aggres-
sively to incentivize speculators to keep the peg, through temporary
changes to the cost of CDP maintenance. In low-arbitrage scenarios,
DAI is especially vulnerable, and RAI will attempt to adapt, but we
expect that neither can maintain a strong peg, especially in extreme
conditions.

5.2 Market Simulation
The secondary market is modeled as consisting of these two primary
forces: short-term arbitrageurs and longer-term CDP speculators
who act as independent agents; in reality, these can be the same
participants synchronously or asynchronously acting on different
incentives.

Agent actions are calculated as linear functions of their respec-
tive reference signals. Thus, the arbitrageur responds proportionally
(𝐾𝐴) to the difference between 𝛼 (the redemption price) and 𝑝 (the
market price), and the speculator responds proportionally (𝐾𝑆 ) to
both the change in redemption price as well as expected future ETH
returns. Both agents use a time-disounted history of observations.
Specifically:

Figure 1: Arbitrage Makes the Difference: In the absence of arbitrage (𝐾𝐴 = 0), RAI and DAI both struggle to regain their peg.
When 𝐾𝐴 = 50 we see the arbitrageur actions correlate across all three tokens; however, only UTAI’s redemption price decisions
motivates unique speculator agent behavior which helps the system to regain the peg smoothly and within a shorter duration.
In particular, note the trends highlighted within the red windows. UTAI regains the peg with or without arbitrage.

Δ𝐴
𝑡 = 𝐾𝐴

∞
∑︁

𝛾𝑡 −𝜏 (cid:16)

𝑝mkt
𝑡

− 𝛼𝑡

Δ𝑆
𝑡 = 𝐾𝑆

𝜏=0
∞
∑︁

𝜏=0

𝛾𝑡 −𝜏 (cid:16)

𝑝mkt
𝑡

− 𝛼𝑡

(cid:17)

(cid:17)

(14)

(15)

Agents add (or remove) Δ𝐴

𝑡 + Δ𝑆
𝑡 to the market supply at every
𝐷𝑡
step according to these rules. Market price is calculated as
𝑆𝑡
and the market clears at the target peg when 𝐷𝑡 = 𝑆𝑡 . Across
experiments, 𝐾𝑆 is set to a constant value of 100 and 𝐾𝐴 varies
between 50 or 0 to “activate" or “deactivate" arbitrage. The values of
50 and 100 are chosen arbitrarily such that the maximum possible
effects of the speculator and the arbitrageur in a single step are
about equal.

Figure 2: A sample path from each scenario in Section 5.3.

5.3 Market Scenarios
Each scenario is driven by a tuple of two exogenous random pro-
cesses (𝑫, 𝒑Eth) , representing token demand and Ethereum prices,
both of which are simulated as geometric Brownian motions spec-
ified by volatility and drift parameters (𝜎, 𝜇). The test cases are
designed to cover a range of both extreme and benign conditions.
Figure 2 depicts a sample path from each case as a visual reference.

5.3.1 Normal Operations (Default). The default case is character-
ized by relatively flat demand with some volatility in token demand.
Minimal adjustments to the redemption price is expected to be
optimal in this case, with the possible need for small corrections
due to volatility.

5.3.2 Drifting Demand. This simulates a definitive linear trend
of either increasing or decreasing exogenous token demand. As
the bilevel protocol integrates forecasting information, it should
anticipate the growth (or decline) and adjust the redemption price
accordingly.

Stress Test. “Stress" is characterized by both a larger 𝜎 than
5.3.3
the default case and several inserted point shocks (2 positive and one
negative) to the demand which decay exponentially. This simulates
market ‘turbulence.’ Shocks can be destabilizing, especially in low-
arbitrage scenarios. We will be interested in seeing which token
recovers the quickest and most gracefully.

Sustained Shock. This case involves a sudden increase in
5.3.4
demand which is sustained over a brief period of time, which then
decays slowly, representing temporary one-sided price pressure.
Again, this is expected to result in a depeg and we will be interested
in observing recoveries.

Figure 3 displays a single sample path from each of these 4
cases in a no-arbitrage environment, comparing the supply demand

Figure 3: Four sample runs exemplifying our four different scenarios selected from the “no arbitrage" (𝐾𝐴 = 0) case. Each
panel highlights unique behavior of UTAI under each condition. Specifically, the light orange series (𝛼𝑈𝑇 𝐴𝐼 ) are the controlled
redemption prices which help guide the dark orange 𝑝𝑆𝑡𝑏 to the peg of $1. Unlike RAI, which had to be re-tuned for the best
results in each case/scenario, UTAI is naturally able to adapt to the scenario due to inherent reasoning through the predictive
bilevel game model. In the absence of arbitrageurs, DAI’s market price depegs and essentially tracks the exogenous demand.

trends of each simulated token, as well the resulting market price
trajectories. The results exemplify the nontrivial control decisions
𝛼𝑈𝑇 𝐴𝐼 (in orange) versus 𝛼𝑅𝐴𝐼 and the fixed redemption baseline.
The key takeaway from this is that UTAI can achieve the proper
incentives to motivate speculator actions even in the absence of
arbitrageurs. Introducing arbitrageurs back into the simulation
only serves to improve all tokens, including UTAI. Figure 1 demon-
strates the two scenarios side by side for Section 5.3.3. the effects
of the arbitraging force on performance highlights the effects of
the arbitraging force on performance in the stress test scenario.

Table 1: Monte Carlo Trials Summary

Arbitrage Level Scenario

N Samples

p-MAD

r-MAD

𝐾𝐴 = 0

𝐾𝐴 = 50

Default

Demand Drift

Stress Test

Sustained Shock

Default

Demand Drift

Stress Test

Sustained Shock

Avg.

Median

Std. Dev.

20

20

20

20

20

20

20

20

160

160

160

DAI

RAI

UTAI

RAI

UTAI

0.019417 0.022534 0.015386 0.038161 0.056736

0.013664 0.006298 0.002304 0.012685 0.009242

0.027140 0.020917 0.012997 0.026070 0.033247

0.030878 0.050162 0.012525 0.046472 0.045980

0.006178 0.006188 0.004522 0.006533 0.009078

0.002804 0.002028 0.001682 0.002718 0.003005

0.012895 0.013284 0.012052 0.013365 0.020706

0.049517 0.075299 0.024873 0.074763 0.068955

0.020051 0.023702 0.010421 0.026980 0.030126

0.010998 0.008668 0.004630 0.012164 0.012259

0.023755 0.035049 0.018451 0.043770 0.058678

5.4 Monte Carlo Study
Next, we demonstrate the general performance of our method by
conducting 20 trials over 100 time steps across the four scenar-
ios both in the presence and absence of arbitrage. Performance is
measured by mean absolute deviation from the $1 peg (p-MAD)
and mean absolute deviation of market price about the redemption
price (r-MAD). The latter metric provides another way to compare

to RAI since, as discussed in Section 3.1, Reflexer’s stated goal is to
align RAI with market prices and not necessarily peg to a specific
value.

The results are summarized in Table 1 and Figure 5. In short,
UTAI achieves the best p-MAD in all cases, and closely approxi-
mates RAI’s performance in the r-MAD metric. The way to interpret
this is that, in our experiments, UTAI not only maintains the target
peg but it does so without too much variation in its redemption
price from that target peg. Figure 3 depicts this fact where UTAI can
be observed making flexible and timely redemption price changes
before smoothly returning redemption back to par. RAI suffers in
several categories due to the simplicity of proportional control,
often leading to overshoot from which it can be slow to recover.

This also explains why, in low-arbitrage scenarios, RAI may
perform slightly better than DAI but ultimately still struggles. Our
results indicate that, given a fixed 𝐾𝑝 , RAI needs arbitraging trades
nearly as much DAI and even with this, requires more sophisticated
control if it is to target a specific peg. On the other hand, UTAI is
highly flexible and resilient in every scenario regardless of arbitrage.

5.5 Vault Safety Test
Figure 4 presents the results of our final experiment, which inves-
tigates how each token responds to a crisis event modeled after
the “deleveraging spiral” discussed in Section 2.4. Specifically, this
experiment tests whether UTAI can return the system to a sufficient
collateralization level faster than the baselines while minimizing
deviation from the price peg. In our market simulation, we include
arbitrageurs (as discussed above), and amplify the speculator’s burn-
ing behavior when collateral falls below a particular threshold (the
red dashed line in the figure). Observe how UTAI is immediately
able to adapt to the perceived extreme conditions, and quickly
steers the system away from the collateralization floor. This action
mitigates deviation from the peg and facilitates eventual recovery.

Figure 4: (Left) The demand shock triggered by token burning pressure leads to a deleveraging spiral in the price of DAI. RAI
adapts but proportional control is slow to recover the peg. UTAI is quickest to recover. (Right) System collateral levels overlaid
with a crashing ETH price pattern. The dashed red line depicts the threshold at which mass burning is activated in simulation;
the bold red line shows the absolute minimum collateralization ratio. DAI performs worst, as any arbitraging is drowned out by
the speculator’s mass burn actions, and the system even falls below the minimum 𝛽 requirement. Both RAI and UTAI mitigate
deleveraging by adapting the redemption price, which effectively relaxes the vault constraint temporarily. UTAI stays furthest
from the minimum collateralization threshold during the shock.

be considered. A key issue is a lack of sophisticated, faithful market
simulations to more rigorously stress test new ideas for algorithmic
DeFi mechanisms. To that end, we note that our model also provides
utility as an off-line simulator for DeFi protocols, especially for sys-
tem designers interested in algorithmic searches for setting optimal
governance or in understanding microeconomic interactions and
emergent behaviors. We believe there exists significant room in
this domain to apply the rich tools of optimal control and dynamic
game theory for both online and offline applications.

Future Work: The framework we presented allows for several
interesting extensions. One direction might be to consider a proto-
col with a more complex control space. In this work, we modeled a
single-collateral system, but it is now common for stablecoins to be
backed by multiple cryptocurrencies. For example, a recent work
[25] used mean-variance optimization for selecting an optimal port-
folio of collateral assets, but highlights the need for a mechanism
to achieve it in practice. Our dynamic Stackelberg model naturally
complements this approach and could be used to find the right
incentives to build target collateral portfolios in reasonable time.
Another interesting direction is a data-driven variant of the
problem. Here, we considered a forward dynamic game model, in
which the utility function of the participating agents is assumed
to be known. One could instead investigate the inverse game [38,
45, 47] in which the protocol attempts to learn more precise agent
utilities by filtering observations through a structured game model.

REFERENCES
[1] Austin Adams and Markus Ibert. 2022. Runs on algorithmic stablecoins: Evidence

from Iron, Titan, and Steel. (2022).

[2] Oguzhan Akcin, Robert P Streit, Benjamin Oommen, Sriram Vishwanath, and
Sandeep Chinchali. 2022. A control theoretic approach to infrastructure-centric
blockchain tokenomics. arXiv preprint arXiv:2210.12881 (2022).

[3] Frank Allgower, Rolf Findeisen, Zoltan K Nagy, et al. 2004. Nonlinear model
predictive control: From theory to application. Journal-Chinese Institute Of
Chemical Engineers 35, 3 (2004), 299–316.

[4] Chain Analysis. 2023. Here’s What On-Chain Data Tells Us About Crypto’s
Reaction to the Demise of Silicon Valley Bank And Its Impact on USDC. https:
//www.chainalysis.com/blog/crypto-market-usdc-silicon-valley-bank/

Figure 5: Results from Table 1 pooled and plotted over the
100 time steps. Shading represents a 90% confidence interval
over the p-MAD metric.

6 CONCLUSIONS & FUTURE WORK
In this paper, we have put forth a novel algorithmic redemption
price controller for a decentralized crypto-backed stablecoin system
based on dynamic game theory and optimal control. Experiments
show that our bilevel control design outperforms existing propor-
tional control techniques and a fixed rate baseline, especially in
extreme market conditions and in the absence of arbitrageurs. Fur-
thermore, our bilevel controller gives more precise autonomous
pricing decisions to maintain a peg than the proportional controller
baseline, which also must rely on offline re-tuning of the 𝐾𝑝 param-
eter [12] as circumstances change. This is significant as it shows it
can be possible for crypto-backed decentralized stablecoins while
targeting a specific peg with the right controller.

Discussion: Although our results point to advantages of adopt-
ing more sophisticated control designs than those used in DeFi
today, there are practical implementation details which still need to

020406080100Time Steps01234567p-MADDAIRAIUTAI[36] Reflexer Labs. [n. d.]. RAI Finance. https://rai.finance/RAI-Finance-WhitePaper.

pdf

[37] Robert Lauko and Richard Pardoe. 2021. Liquity: Decentralized borrowing
protocol. Technical Report. Technical report. Available at https://docsend.
com/view/bwiczmy.

[38] Jingqi Li, Chih-Yuan Chiu, Lasse Peters, Somayeh Sojoudi, Claire Tomlin, and
David Fridovich-Keil. 2023. Cost inference for feedback dynamic games from
noisy partial state observations and incomplete trajectories. arXiv preprint
arXiv:2301.01398 (2023).

[39] Tao Li and Suresh P Sethi. 2017. A review of dynamic Stackelberg game models.

Discrete & Continuous Dynamical Systems-B 22, 1 (2017), 125.

[40] Gui-Hua Lin and Masao Fukushima. 2005. A modified relaxation scheme for
mathematical programs with complementarity constraints. Annals of Operations
Research 133, 1 (2005), 63–84.

[41] Jiageng Liu, Igor Makarov, and Antoinette Schoar. 2023. Anatomy of a run: The
terra luna crash. Technical Report. National Bureau of Economic Research.
[42] Zhi-Quan Luo, Jong-Shi Pang, and Daniel Ralph. 1996. Mathematical programs

with equilibrium constraints. Cambridge University Press.

[43] Patrice Marcotte. 1986. Network design problem with congestion effects: A case
of bilevel programming. Mathematical programming 34, 2 (1986), 142–162.

[44] MARS. 2021. LitePaper.

https://blog.marsprotocol.io/blog/mars-protocol-

litepaper-2-0

[45] Negar Mehr, Mingyu Wang, Maulik Bhatt, and Mac Schwager. 2023. Maximum-
entropy multi-agent dynamic games: Forward and inverse solutions. IEEE trans-
actions on robotics 39, 3 (2023), 1801–1815.

[46] Makiko Mita, Kensuke Ito, Shohei Ohsawa, and Hideyuki Tanaka. 2019. What is
stablecoin?: A survey on price stabilization mechanisms for decentralized pay-
ment systems. In 2019 8th International Congress on Advanced Applied Informatics
(IIAI-AAI). IEEE, 60–66.

[47] Lasse Peters, Vicenç Rubies-Royo, Claire J Tomlin, Laura Ferranti, Javier Alonso-
Mora, Cyrill Stachniss, and David Fridovich-Keil. 2023. Online and offline learning
of player objectives from partial observations in dynamic games. The International
Journal of Robotics Research 42, 10 (2023), 917–937.

[48] S Joe Qin and Thomas A Badgwell. 2003. A survey of industrial model predictive

control technology. Control engineering practice 11, 7 (2003), 733–764.

[49] David Cerezo Sánchez. 2019. Truthful and faithful monetary policy for a sta-
blecoin conducted by a decentralised, encrypted artificial intelligence. arXiv
preprint arXiv:1909.07445 (2019).

[50] Patrick Schueffel. 2021. Defi: Decentralized finance-an introduction and overview.

Journal of Innovation Management 9, 3 (2021), I–XI.

[51] Max Schwenzer, Muzaffer Ay, Thomas Bergs, and Dirk Abel. 2021. Review on
model predictive control: An engineering perspective. The International Journal
of Advanced Manufacturing Technology 117, 5 (2021), 1327–1349.

[52] Maker Team. 2017. The Dai Stablecoin System Whitepaper. https://makerdao.

com/whitepaper/DaiDec17WP.pdf

[53] Reserve Research Team. 2018. The End of a Stablecoin — The Case of Nu-
https://blog.reserve.org/the-end-of-a-stablecoin-the-case-of-nubits-

Bits.
dd1f0fb427a9

[54] Torsten Trimborn, Lorenzo Pareschi, and Martin Frank. 2017. Portfolio op-
timization and model predictive control: a kinetic approach. arXiv preprint
arXiv:1711.03291 (2017).

[55] Heinrich Von Stackelberg. 2010. Market structure and equilibrium. Springer

Science & Business Media.

[56] Sam Werner, Daniel Perez, Lewis Gudgeon, Ariah Klages-Mundt, Dominik Harz,
and William Knottenbelt. 2022. Sok: Decentralized finance (defi). In Proceedings
of the 4th ACM Conference on Advances in Financial Technologies. 30–46.
[57] Mengmeng Yu and Seung Ho Hong. 2016. Supply–demand balancing for power
management in smart grid: A Stackelberg game approach. Applied energy 164
(2016), 702–710.

[58] Marco Zugno, Juan Miguel Morales, Pierre Pinson, and Henrik Madsen. 2013. A
bilevel model for electricity retailers’ participation in a demand response market
environment. Energy Economics 36 (2013), 182–197.

[5] Moody’s Analytics. 2023. Large fiat-backed stablecoins depegged 600+ times in
2023. https://www.moodys.com/web/en/us/insights/banking/moody-launches-
new-digital-asset-monitor-to-track-risk.html

[6] Moody’s Analytics. 2023.

Stablecoins have been unstable. Why?
https://www.moodys.com/web/en/us/about/insights/data-stories/stablecoins-
instability.html

[7] Roberto Andreani and José Mario Martı´ nez. 2001. On the solution of mathemat-
ical programming problems with equilibrium constraints. Mathematical Methods
of Operations Research 54 (2001), 345–358.

[8] Lennart Ante, Ingo Fiedler, and Elias Strehle. 2021. The influence of stablecoin
issuances on cryptocurrency markets. Finance Research Letters 41 (2021), 101867.
[9] Daniel Perez Ariah Klages-Mundt, Lewis Gudgeon. 2021. Gryoscopic Stablecoins.

https://github.com/gyrostable/gyroscope-landing/tree/master/pdfs

[10] Jonathan F Bard. 2013. Practical bilevel optimization: algorithms and applications.

Vol. 30. Springer Science & Business Media.

[11] Charles Bertucci, Louis Bertucci, Mathis Gontier Delaunay, Olivier Gueant, and
Matthieu Lesbre. 2024. Agents’ Behavior and Interest Rate Model Optimization
in DeFi Lending. Available at SSRN 4802776 (2024).

[12] BlockScience. 2021. Summoning the Money God. https://medium.com/reflexer-

labs/summoning-the-money-god-2a3f3564a5f2

[13] Luce Brotcorne, Martine Labbé, Patrice Marcotte, and Gilles Savard. 2001. A
bilevel model for toll optimization on a multicommodity transportation network.
Transportation science 35, 4 (2001), 345–358.

[14] Tarun Chitra, Kshitij Kulkarni, Guillermo Angeris, Alex Evans, and Victor Xu.
2022. Defi liquidity management via optimal control: ohm as a case study.
[15] Ryan Clements. 2021. Built to fail: The inherent fragility of algorithmic stable-

coins. Wake Forest L. Rev. Online 11 (2021), 131.

[16] CoinMarketCap. 2024. Top Stablecoin Tokens by Market Capitalization. https:

//coinmarketcap.com/view/stablecoin/

[17] Maker Dao. 2021. MIP29: Peg Stability Module. https://mips.makerdao.com/

mips/details/MIP29

[18] Stephan Dempe and Alain Zemkoho. 2020. Bilevel optimization. In Springer

optimization and its applications. Vol. 161. Springer.

[19] Adrien d’Avernas, Thomas Bourany, and Quentin Vandeweyer. 2021. Are stable-
coins stable? https://www.banque-france.fr/sites/default/files/media/2021/06/
10/gdre_bounary.pdf

[20] Euler Finance. 2023. White Paper. https://docs-v1.euler.finance/getting-started/

white-paper

[21] Carlos E Garcia, David M Prett, and Manfred Morari. 1989. Model predictive
control: Theory and practice—A survey. Automatica 25, 3 (1989), 335–348.
[22] Gauntlet. 2020. Feedback Control as a New Primitive. https://medium.com/
gauntlet-networks/feedback-control-as-a-new-primitive-for-defi-27b493f25b1
[23] Klaus Grobys, Juha Junttila, James W Kolari, and Niranjan Sapkota. 2021. On the
stability of stablecoins. Journal of Empirical Finance 64 (2021), 207–223.
[24] Lei Guo, Gui-Hua Lin, and Jane J Ye. 2015. Solving mathematical programs with
equilibrium constraints. Journal of Optimization Theory and Applications 166
(2015), 234–256.

[25] Bretislav Hajek, Daniel Reijsbergen, Anwitaman Datta, and Jussi Keppo. 2024.
Collateral Portfolio Optimization in Crypto-Backed Stablecoins. arXiv preprint
arXiv:2405.08305 (2024).

[26] Florian Herzog, Gabriel Dondi, and Hans P Geering. 2007. Stochastic model
predictive control and portfolio optimization. International Journal of Theoretical
and Applied Finance 10, 02 (2007), 203–233.

[27] Florian Herzog, Simon Keel, Gabriel Dondi, Lorenz M Schumann, and Hans P
Geering. 2006. Model predictive control for portfolio selection. In 2006 American
Control Conference. IEEE, 8–pp.

[28] Johannes Rude Jensen, Victor von Wachter, and Omri Ross. 2021. An introduc-
tion to decentralized finance (defi). Complex Systems Informatics and Modeling
Quarterly 26 (2021), 46–54.

[29] Magnus Josefsson and Michael Patriksson. 2007. Sensitivity analysis of separable
traffic equilibrium equilibria with application to bilevel optimization in network
design. Transportation Research Part B: Methodological 41, 1 (2007), 4–31.
[30] Vyacheslav V Kalashnikov, Stephan Dempe, Gerardo A Pérez-Valdés, Nataliya I
Kalashnykova, José-Fernando Camacho-Vallejo, et al. 2015. Bilevel programming
and applications. Mathematical Problems in Engineering 2015 (2015).

[31] Sam Kazemian, Jason Huan, Jonathan Shomroni, and Kedar Iyer. 2022. Frax: A
Fractional-Algorithmic Stablecoin Protocol. In 2022 IEEE International Conference
on Blockchain (Blockchain). IEEE, 406–411.

[32] Ariah Klages-Mundt, Dominik Harz, Lewis Gudgeon, Jun-You Liu, and Andreea
Minca. 2020. Stablecoins 2.0: Economic foundations and risk-based models. In
Proceedings of the 2nd ACM Conference on Advances in Financial Technologies.
59–79.

[33] Ariah Klages-Mundt and Andreea Minca. 2021. (In)stability for the blockchain:

Deleveraging spirals and stablecoin attacks. (2021).

[34] Ariah Klages-Mundt and Andreea Minca. 2022. While stability lasts: A stochastic
model of noncustodial stablecoins. Mathematical Finance 32, 4 (2022), 943–981.
[35] Martine Labbé and Alessia Violin. 2016. Bilevel programming and price setting

problems. Annals of operations research 240 (2016), 141–169.

