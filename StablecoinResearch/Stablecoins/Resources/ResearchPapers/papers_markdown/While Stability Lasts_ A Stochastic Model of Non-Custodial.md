2
2
0
2

l
u
J

1
3

]

R
T
.
n
i
f
-
q
[

3
v
4
0
3
1
0
.
4
0
0
2
:
v
i
X
r
a

While Stability Lasts: A Stochastic Model of Non-Custodial
Stablecoins ∗

Ariah Klages-Mundt†

Andreea Minca‡

June 8, 2022

Abstract

The ‘Black Thursday’ crisis in cryptocurrency markets demonstrated deleveraging risks in
over-collateralized non-custodial stablecoins. We develop a stochastic model that helps explain
deleveraging crises in these over-collateralized systems. In our model, the stablecoin supply is
decided by speculators who optimize the proﬁtability of a leveraged position while incorporating
the forward-looking cost of collateral liquidations, which involves the endogenous price of the
stablecoin. We formally characterize regimes that are interpreted as stable and unstable for the
stablecoin. We prove bounds on quadratic variation and the probability of large deviations in
the stable domain and we demonstrate distinctly greater price variance in the unstable domain.
We identify a deﬂationary deleveraging spiral by means of a submartingale. These deleverag-
ing spirals, which resemble short squeezes, lead to faster collateral drawdown (and potential
shortfalls) and are accompanied by higher price variance, as experienced on Black Thursday.
We conclude by discussing non-custodial ways in which the issues raised in this paper can be
mitigated.

1 Introduction

On March 12, 2020, called ‘Black Thursday’ during the COVID-19 market panic, cryptocurrency
prices dropped ∼ 50% in the day.1 This was accompanied by cascading liquidations on cryptocur-
rency leverage platforms, including both centralized platforms like exchanges and new decentralized
ﬁnance (DeFi) platforms that facilitate on-chain over-collateralized lending. Among many events
from this day, the story of Maker’s stablecoin Dai stands out, which entered a deﬂationary delever-
aging spiral (akin to a short squeeze on Dai). This triggered high volatility of the ‘stable’ asset
and a breakdown of the collateral liquidation process. Due to market illiquidity exacerbated by
network congestion, some collateral liquidations were performed at near-zero prices. As a result,
the system developed a collateral shortfall, which prompted an emergency response and had to be
made up by selling new equity-like tokens to recapitalize MakerDAO [2020a].

During this time, there was a huge demand for Dai. It became a much riskier and more volatile
asset, yet traded at a high premium and fetched lending rates in the mid double digits. Leveraged
speculators, who must repurchase Dai in order to deleverage their positions, were exhausting Dai

∗This paper is based on work supported by NSF CAREER award #1653354 and the Bloomberg Fellowship. We
thank Dominik Harz, Georgios Konstantopoulos, the anonymous referees for valuable feedback that helped improve
the paper.

†Cornell University, Center for Applied Mathematics, Ithaca, NY, 14853, USA, email: aak228@cornell.edu.
‡Cornell University, School of Operations Research and Information Engineering, Ithaca, NY, 14850, USA, email:

acm299@cornell.edu.

1This occurred while writing up the ﬁrst draft of this paper.

1

Figure 1: Stablecoin supply.

liquidity, driving up the price of Dai and subsequently increasing the cost of future deleveraging
(we discuss some further causes that led to market illiquidity in developing the model in the next
section). These speculators began to realize that, in these conditions, they face concrete risk that
a debt reduction of $1 could cost a signiﬁcant premium. Eventually, a new exogenously stable
asset–the USD-backed custodial stablecoin USDC–had to be brought in as a new collateral type to
stabilize the system Coindesk [2020].

1.1 Stablecoins

A stablecoin is a cryptocurrency with added economic structure that aims to stabilize price/purchasing
power. For a recent overview of stablecoins, see Bullmann et al. [2019], Klages-Mundt et al. [2020]
and the references therein. Stablecoins are meant to bootstrap price stability into cryptocurrencies
as a stop-gap measure for adoption. They also serve as mechanics to avoid ﬁat to crypto conver-
sions, which are rather costly. This is in fact a key motivation for their use, hence the system can
remain ‘fully decentralized’.

Stablecoins are either custodial and rely on custodians to hold reserve assets oﬀ-chain (e.g., $1
per coin) or non-custodial and set up a risk transfer market through smart contracts, which are
programs that execute on the blockchain computer. Custodial stablecoins include Tether, USDC,
and the proposed Diem/Libra and can often be viewed analogously to narrow banks or money
market funds in terms of underlying structure. Alternatively, non-custodial stablecoins aim to
retain the property of reduced counterparty/censorship risk. Figure 1 illustrates the market share
of the main stablecoins. The largest three are custodial stablecoins (USDT, USDC, BUSD) whereas
only one non-custodial stablecoin, Dai, is among the top four stablecoins in terms of market share.

Non-custodial stablecoins have a wide design space, which is captured in the taxonomy of
Klages-Mundt et al. [2020]. A key dimension in this design space is the source of value backing
the stablecoin. This ranges from exogenous asset backing, where assets have value unrelated to the
system, to endogenous asset backing, where assets are like ‘system equity’ and have value that is
circular with the system itself. This latter class, which is often ill-deﬁned as ‘algorithmic’, often
blurs the line with being eﬀectively unbacked, as the value of endogenous assets can spiral to zero
if conﬁdence is broken. This latter type includes the Terra UST stablecoin that collapsed in May
2022 Bloomberg [2022]. These stablecoins that are fully or partly endogenously backed can largely
be understood using generalizations of currency peg models, such as Morris and Shin [1998], for
which the risks of currency runs and speculative attacks are well studied. These existing tools help
to understand these systems and how they (usually) fail, considering that the ‘economies’ around

2

these stablecoins are quite fragile.

In contrast, non-custodial stablecoins that are backed by exogenous assets have greater similari-
ties to non-custodial forms of the current monetary system of commercial bank money, as discussed
in Klages-Mundt et al. [2020]. In this paper, we focus on new risks that arise in these types of
stablecoins, which require further study. Stablecoins of this type transfer risk from stablecoin hold-
ers to speculators, who hold leveraged collateralized positions in cryptocurrencies.2 The speculator
represents any actor (usually automated) who has an incentive to issue the coin.3 Such actor is-
sues the stablecoin continuously by locking in collateral. The incentive to issue (or redeem) coin
is captured by the speculators’ return expectations including potential liquidation costs and the
endogenous stablecoin price.

The collateralization structure is diﬀerent for non-custodial stablecoins than for the custodial
ones. It is similar to a tranche structure, in which stablecoins act like senior debt while speculators
are akin the buyers of the junior tranche of a CDO. In contrast to the classical case, the ‘CDO’ issue
is dynamic and by anyone in the system. We refer the reader to the Dai white paper MakerDAO
[2017]. The white paper describes how anyone could generate Dai using that system by leveraging
Ethereum (ETH) as collateral through smart contracts known as Collateralized Debt Positions
(CDPs).

A dynamic and automatic deleveraging process balances positions if collateral value deviates too
much, as determined by a price feed. Two major risks in non-custodial stablecoins emerge around
market structure collapse and price feed and governance manipulation.
In this paper, we focus
completely on the market structure risk, assuming that price feeds, governance, and the underlying
blockchain perform as expected.4

In addition to the COVID-19 panic, the eﬀects of these risks are also witnessed in bitUSD,
Steem Dollars, and NuBits, which suﬀered serious depegging events in 2018 Klages-Mundt [2018],
and Terra and Synthetix, which suﬀered price feed manipulation attacks in 2019 (Synthetix [2019b],
Synthetix [2019a], Terra Research [2019]). Similar manipulations were also observed on the bZx
lending protocol in 2020 (PeckShield [2020a], PeckShield [2020b]). Many similar examples of mech-
anism failures and exploitations occurred through the rest of 2020 (see Klages-Mundt et al. [2020],
Werner et al. [2021]). Stablecoins currently serve a central role in an increasingly complex de-
centralized ﬁnance environment, involving composability with other DeFi platforms. In addition,
many other blockchain assets, such as synthetic and cross-chain assets, rely on the basic mechanism
behind stablecoins, which we explore further in the discussion section.

1.2 This paper

In this paper, we construct a stochastic model of over-collateralized non-custodial stablecoins, with
an endogenous price (Section 2). The system is based on a speculator who solves an optimization
problem accounting for potential returns from leverage as well as potential liquidation costs. The
speculator decides the supply of stablecoins secured by its collateral position while considering
demand for the stablecoin. Our interest in non-custodial stablecoins lies in understanding delever-
aging spirals when the price and stablecoin issue is endogenous and the collateral management is
decentralized. In this case, a deleveraging spiral results from the intertwining of a short squeeze in
the stablecoin price and a liquidation spiral of the collateral. This is in contrast to potential liqui-
dation crises in custodial coins such as Tether and USDC or ‘algorithmic’ stablecoins such as Terra

2‘Leverage’ means that speculators holds > 1× initial assets but face new liabilities.
3They are part a form of ‘keepers’ in the MakerDAO protocol.
4Note, however, that blockchain congestion can serve to decrease elasticity in the market structure, which we

discuss in the model construction.

3

UST (which coincidentally also had a partial custodial reserve). Custodial stablecoins maintain
stability through arbitrageurs who mint and redeem for assets with the custodian. Unbacked or
partially backed stablecoins like Terra UST instead are subject to death spiral risks from runs and
speculative attacks due to insolvency. In both of these cases, classical models for money market
funds and currency pegs apply well. 5 We focus on the non-custodial variant involving exogenous
over-collateralization, whose risks are yet to be analyzed rigorously.

We derive fundamental results about non-custodial stablecoins in our model, including economic
limits to the speculator’s behavior, in Section 3. In Section 4 we develop the primary results of
the paper: we analytically characterize regions in which the stablecoin can be intepreted as stable
(Theorems 1 and 2) and unstable (Theorems 4 and 5), and a region in which a deleveraging spiral
occurs that can cause liquidity problems in a crisis (Theorem 3). These deleveraging spirals, which
resemble short squeezes, are counterintuitive as they lead to stablecoin price appreciation during
times of shock, whereas we might otherwise expect prices to depreciate given the riskier state of
the system. Further, this appreciation is detrimental: it leads to faster collateral drawdown, and
potentially shortfalls, as more collateral is required to fulﬁll liquidations and is accompanied by
higher price variance.

The context for our analytical results is a model with a single speculator facing imperfectly
elastic demand for the stablecoin; however, many of the methods can extend to generalized settings.
In Section 5, we consider idealized settings that lead to ‘perfect’ stability properties.

We discuss in Section 6 a seeming contradiction that arises: while the goal is to make decen-
tralized non-custodial stablecoins, these can only be fully stabilized from deleveraging eﬀects by
adding uncorrelated assets, which are currently centralized/custodial. This is a consequence of our
instability results in Section 4 and, as introduced in Section 5, the absence of a stable region in
idealized settings when underlying asset markets deviate from a submartingale setting. We suggest
an alternative: a buﬀer to dampen deleveraging eﬀects without directly incorporating custodial
assets. This buﬀer works by separating those who are willing to have stablecoins swapped to cus-
todial assets in a crisis (in return for an ongoing yield from option buyers) from those who require
full decentralization.

Non-custodial stablecoins such as Dai, Rai, and Liquity have since moved in directions such as

this to overcome the issues we illustrate in this paper.

1.3 Relation to Prior Work

While there is a rich literature on related ﬁnancial instruments, there is limited research directly
applicable to stablecoins. Cao et al. [2021] are the ﬁrst to point out the analogy of stablecoins to
Collateralized Loan Obligations, and contribute to the securitization literature by proposing designs
in the decentralized context. They use option pricing theory and PDE methods for valuation of
their new design features. Our work is complimentary: we analyze the stability over time of these
new securities.

A simple stablecoin model is developed in Klages-Mundt and Minca [2021] and introduces the
concept of deleveraging spirals, which later materialized on Black Thursday. This paper supersedes
that model and its results. Whereas the model in Klages-Mundt and Minca [2021] doesn’t directly
account for the actual repurchase price in deleveraging–instead delegating to a risk constraint in

5The

of

recent

collapse

https://www.wsj.com/articles/
be modeled
cryptocurrency-terrausd-falls-below-fixed-value-triggering-selloff-11652122461
similarly to the run on money market funds in the ﬁnancial crisis, Kacperczyk and Schnabl [2013], or currency peg
attacks, Morris and Shin [1998].
In particular, restoring the peg relies on open market operations by an entity
running the reserve fund, such as Luna Foundation in the case of the TerraUSD stablecoins.

in TerraUSD,

e.g.,

peg

can

the

see

4

the optimization–we set up a stochastic process model in this paper that includes forward-looking
liquidation prices in the speculator’s optimization. Our analytical results supersede Klages-Mundt
and Minca [2021] in the following ways:

• We formally characterize a deleveraging spiral as a submartingale, whereas their paper lacks

a formal treatment.

• We give stability results in terms of probabilities of large deviations and quadratic variation

of the price process.

• An unstable region is conjectured in their paper, backed by simulation. We formally prove

distinct price variances in stable and unstable regions.

Evans [2019] analyzes credit risk stemming from collateral type in Maker’s stablecoin Dai. cLabs
[2019], Platias and DiMaggio [2019] model stability in Terra and Celo stablecoins under Brownian
motion scenarios in the absence of endogenous market feedback eﬀects that motivate this paper.
Huo et al. [2022], Klages-Mundt et al. [2020] discuss models of governance and oracle attack surfaces
for non-custodial stablecoins. More generally in the context of decentralized ﬁnance, Werner et al.
[2021] treat the governance extractable value.

Detrio [2015] discusses stablecoin concepts based on monetary policy and hedging strategies
and introduces methods for enhancing liquidity using combinatorial auctions and automated mar-
ket makers. Lipton et al. [2018] studied custodial stablecoins and considers the use of hedging
techniques to build an asset-backed cryptocurrency. Gudgeon et al. [2020] explores the robustness
of decentralized lending protocols to shocks and liquidations. Chitra [2020] explores competition
between decentralized lending yields and staking yields in proof-of-stake blockchains. However,
these do not model a stablecoin mechanism with endogenous price behavior.

Harz et al. [2019] designs a reputation system for crypto-economic protocols to reduce collateral
requirements. This does not readily apply to understanding stablecoin collaterals, however, as it
requires identiﬁcation of ‘good’ behavior and, additionally, stablecoin speculators face leveraged
exchange rate bets and will have reason to provide greater than minimal collateral. This additionally
motivates our model to understand how liquidation eﬀects aﬀect speculator decisions.

Stablecoins share similarities with currency peg models, e.g., Guimaraes and Morris [2007],
Morris and Shin [1998]. In these models, the government plays a mechanical market making role to
seek stability and is not a player in the game. In contrast, in non-custodial stablecoins, decentralized
speculators take the market making role. They issue/withdraw stablecoins to optimize proﬁts and
are not committed to maintaining a peg. In a stablecoin, the best we can hope is that the protocol
is well-designed and that the peg is maintained with high probability through incentives. A fully
strategic model would be a complicated (and likely intractable) dynamic game.

There are also similarities with collateral and debt security markets and repurchase agreements.
These have also experienced unprecedented stress in the COVID-19 market panic, during which
even 30-year US government bonds–normally highly liquid–have been diﬃcult to trade Rennison
et al. [2020]. Such debt securities diﬀer from stablecoins in that dollars are borrowed against the
collateral as opposed to a new instrument, like a stablecoin, with an endogenous price. These debt
security markets do, however, demonstrate that liquidity in the underlying markets can dry up in
crises even in highly liquid markets. Stablecoins face this liquidity risk in the underlying market
as well as an endogenous price eﬀect on the stable asset.

The problem resembles classical market microstructure models (e.g., O’Hara [1997]); it is a
multi-period system with agents subject to leverage constraints that take recurring actions accord-
In contrast, the stablecoin setting has no exogenously stable asset that
ing to their objectives.

5

is eﬃciently and instantly available. Instead, agents make decisions that endogenously aﬀect the
price of the ‘stable’ asset and aﬀect future incentives.

2 Model

Our model is very closely related to Maker’s stablecoin Dai MakerDAO [2017] as well as newer
stablecoins by UMA, Reﬂexer, and Liquity. Crucially, these stablecoins are backed by over-
collateralization in assets that have value exogenous to the stablecoin system as opposed to as-
sets whose value is circularly derived from the stablecoin itself. There are two primary feedback
eﬀects to consider in these stablecoins: (1) feedback of deleveraging on an endogenous stablecoin
price, and (2) feedback of deleveraging on collateral price. We focus on the former. The latter can
be described using existing deleveraging models (e.g., this is considered in the stablecoin context
in Gudgeon et al. [2020]). We later discuss how our model can be adapted to incorporate these
endogenous eﬀects on collateral in Section 6.

The model contains a stablecoin market and two assets: a risky asset (ETH)6 with exogenous
price Xt and an ETH-collateralized stablecoin STBL with endogenous price Zt. The stablecoin
market connects stablecoin holders, who seek stability, and speculators, who make leveraged bets
backing STBL. The STBL protocol requires the STBL supply to be over-collateralized in ETH by
collateral factor β.

In order to focus on the eﬀects of speculator decisions in this paper, we simplify the stablecoin
holder demand as exogenous with constant unit price-elasticity. This is equivalent to a ﬁxed STBL
demand D in dollar terms, though not quantity. Note that there is no direct redemption process
for stablecoin holders aside from a global settlement/shutdown of the system at par value, which
can be triggered by a governance process (see MakerDAO [2017]).

From a practical perspective, STBL demand is not elastic, at least short-term, even if it were
in principle elastic longer-term. A signiﬁcant portion of stablecoin supplies are locked in other
applications, like lending protocols and lotteries. These applications promise (in some sense) value
safety in over-collateralization, but don’t guarantee liquidity to withdraw. Additionally, Ethereum
transactions cannot be executed in parallel; during volatile times, transactions can be delayed due
to congestion, causing timely trades (especially involving transfer to/from centralized exchanges) to
fail. This occurs even if, in principle, there is liquidity in these markets. On the other hand, longer-
term demand elasticity will naturally depend on the presence of good uncorrelated alternatives.7

The speculator has ETH locked in the system and decides the STBL supply, which represents
a liability against its locked collateral. At the start of step t, there are Lt−1 STBL coins in supply.
The speculator holds Nt−1 ETH and chooses to change the STBL supply by ∆t = Lt − Lt−1.
If ∆t > 0, the speculator sells new STBL on the market for ETH at the market clearing price
Zt. This increases the ETH position Nt. If ∆t < 0, the speculator buys STBL on the market,
reducing Nt. We denote by ¯Nt the speculator’s locked collateral. Informed by limitations of actual
implementations, we formalize the process ( ¯Nt) based on (Nt).8 The speculator decides Lt by
optimizing expected proﬁtability in the next period based on expectations about ETH returns and
the cost of collateral liquidation if the collateral factor is breached.

6We designate the risky collateral asset as ETH for simplicity. In principle, it could be another cryptoasset or

even outside of a cryptocurrency setting.

7From another perspective, a strategic stablecoin holder would take into account expectations about speculator
issuance and ability to maintain the price target and expectations about a global settlement. This is outside of our
model as formulated.

8In principle, the speculator’s decision could be extended to deciding ¯Nt in addition to ∆t. Note however that

this would make most sense if the speculator’s position is further extended to include multiple assets.

6

In this way, the speculator myopically optimize for the next period. A simpliﬁcation of our
model is a one-oﬀ game, which hosts a single period of decision-making before the system is settled
in the ﬁnal period. In this case, the myopic setup is parallel to major single period games in ﬁnance
(e.g., Diamond and Dybvig [1983], Dybvig and Zender [1991], Guimaraes and Morris [2007], Morris
and Shin [1998], Parlatore [2016]). Our results make signiﬁcant contributions over the existing state
of research on stablecoins, describing diﬀerent system behavior depending on initial conditions in
one-oﬀ games. The more general multi-period form of our model then describes a dynamic process
composed of a series of one-oﬀ games with changing initial conditions. Our results also apply more
generally to this multi-period setting, where they are stronger than simply a series of the one-oﬀ
version of the results. Both of these contribute to stablecoin modeling as there are not better
candidates for multi-period models at this point, although we later discuss ideas toward adapting
the model into a multi-period control problem.

Given supply and demand, the STBL market clears by setting demand equal to supply in dollar
terms. This yields the clearing price Zt = D
.9 This clearing equation is related to the quantity
Lt
theory of money and is similar to the clearing in automated market makers Angeris et al. [2020]
but processed in batch.

2.1 Formal setup

We formalize the model as follows. We deﬁne the following parameters:

• D = STBL demand in dollar value (equivalent to constant unit price-elasticity)

• β = collateral factor for ETH

• α ≥ 1 = liquidation cost multiple (reﬂecting the fee paid to liquidators)

The system is composed of the following processes:

• (Xt)t≥0 = exogenous ETH price process in dollars.

• Lt = stablecoin supply at time t that obeys

Lt = ζ + Lt−1 + ∆t,

where Lt−1 > 0 is the speculator’s STBL liabilities from the previous period, ∆t is the
speculator’s change in liabilities at time t (such that Lt = Lt−1 + ∆t), and ζ is a real number
that modiﬁes circulating supply

• Nt = speculator’s ETH position at time t, including collateral

• ¯Nt = speculator’s locked ETH collateral at time t (and start of time t + 1)

• (Yt)t≥0 = speculator’s value process

• Zt = D
Lt

deﬁnes the STBL price process.

9We can consider constant elasticity STBL demand functions that depend on Zt. Letting q be the quantity
of STBL demanded at $1 price and assuming a constant price elasticity −γ < 0, the dollar-denominated demand
function is D(Zt) = ZtQ(Zt) = Ztq/(1 − γ(1 − Zt)). for γ = 1 we obtain the case of constant dollar denominated
demand. In clearing the market, the generalized price process is a linear transformation Zt = 1
γ

+ 1.

− 1

(cid:17)

(cid:16) q
Lt

7

We take (Ft)t≥0 to be the natural ﬁltration where Ft = σ(X0, . . . , Xt, L0, . . . , Lt). The system is
driven by the process (Xt) subject to the speculator’s decisions ∆t (equivalently Lt given Lt−1).

The parameter ζ modiﬁes circulating STBL supply. This could come from an outside amount
of STBL not created by the speculator (a positive adjustment), or some STBL could essentially be
locked (a negative adjustment). As formulated, our model applies to a system that can be described
with monopolistic agents, or where agents behave similarly (have similar beliefs). With ζ > 0, the
model becomes similar to having heterogeneous agents. Whereas, in general to do this, we would
have to consider both heterogeneous beliefs about the future as well as diﬀerent ζs, which together
would be intractable, ζ provides a way to aggregate these various eﬀects in a simpler model. In
particular, we suggest a positive ζ may make numerical results more applicable to real settings.

To simplify the exposition of analytical results going forward, we simplify to the case that β = 3
2
(the collateral factor used in Maker’s Dai stablecoin) and ζ = 0. Note that under these conditions,
and in the remainder of the paper, we use Lt and Lt interchangeably.

2.2 Collateral constraint

The collateral constraint requires the collateral locked in the system to be ≥ a factor of β times
by liabilities. It applies in both a pre-decision and post-decision sense. The pre-decision version
determines when a liquidation occurs: a liquidation is triggered at the start of time t if the following
condition is breached

¯Nt−1Xt ≥ βLt−1.

The post-decision version constrains the speculator’s decision-making, limiting Lt such that

¯NtXt ≥ βLt.

Note that the nominal stablecoin price ($1) is used in these constraints instead of the real price
because these are encoded by the protocol’s smart contracts as one of the means toward incentivizing
the $1 target.10 The collateral factor could be dynamic, in the sense that the governance of the
protocol could vote to change its value. Proposals to change the collateral factor are in practice
infrequent, see https://makerdao.world/en/learn/vaults/liquidation/, so we consider here
a constant factor. We leave it for future research to model the governance’s decision.

2.3 Speculator decides ∆t taking into account real liability value

We assume the speculator is risk-neutral and optimizes its next-period expected value, taking into
account expectations around liquidations. In particular, this means that the speculator takes into
account the real cost of deleveraging its liabilities in the event it needs to reduce its position in the
next time step and doesn’t simply measure the nominal value of liabilities. Its value at time t is its
nominal equity at the start of period (pre-decision), adjusted by a liquidation eﬀect that describes
how the real value deviates from nominal in the event that the speculator needs to deleverage.
That is

Yt = Nt−1Xt − Lt−1 − liquidation eﬀect.

A liquidation eﬀect is outlined in a following subsection.

10Conceptually, outside of this model, this has the eﬀect of upper bounding the stablecoin price at β as an arbitrage

opportunity would be created otherwise.

8

Note that Nt is a function of the decision variable ∆t, and recall Lt = Lt−1 +∆t. The speculator
decides ∆t (equivalently Lt given Lt−1) to optimize next-period expected value subject to the post-
decision collateral constraint in the current period:

max
∆t
s.t.

E[Yt+1|Ft]

¯NtXt ≥ βLt.

Thus the speculator accounts for the expected deviation of real from nominal liability value. If
the expected liquidation eﬀect is small —for instance if the probability that the speculator needs to
deleverage next period is small— then the speculator treats Lt near face value in the optimization
for a mix of short- and long-term reasons. As long as speculators can survive liquidation, they can
expect to dispose of liabilities near face value longer-term when markets are liquid. The protocol
smart contracts also add a precedent for treating liabilities at face value: it is encoded in this way
in the collateral constraint and in the event of global settlement of the system, which is intended to
be be triggered should the system diverge too signiﬁcantly from the intended structure (and which
would occur in the ﬁnal period of the one-oﬀ version).

2.4 Speculator’s collateral at stake

We consider that the speculator decides on a level of participation as a component of their entire
portfolio. This takes place in a separate optimization problem outside the scope of this model (al-
though we discuss how it could be extended later). The speculator’s level of participation amounts
to the initial collateral at the start of our model–for simplicity, we say this also includes any
amount they have decided beforehand may be accessible to top up collateral later. The specula-
tor’s behavior in our model amounts to maximizing the expected value of this component of their
portfolio. On the other hand, if this were the speculator’s entire portfolio, we note that the story
may be diﬀerent–e.g., they may want to maximize expected log values as in the Kelly criterion and
would probably choose to participate diﬀerently, as is common in problems of leverage if the whole
portfolio is at stake.

We take the speculator’s collateral at stake at the start of time t + 1 to be ¯Nt = Nt−1 minus
any collateral liquidation that happens at time t. This is consistent with the speculator’s collateral
being blocked:
it cannot be used to repurchase STBL in the same step. This means that the
speculator (1) has an outside amount (or is able to borrow) to repurchase STBL if ∆t < 0 and
then later repays this from unlocking collateral and (2) can’t post proceeds of new STBL issuance
(∆t > 0) as collateral within the same step.

While there are settings in which we could alternatively use Nt as the collateral at stake at
the start of t + 1 (e.g., if ﬂash loans are used), the choice of Nt−1 additionally leads to a simpler
exposition of results as it decouples the collateral from the decision variable.

2.5 Collateral liquidation mechanics
In time t + 1, the pre-decision collateral constraint is ¯NtXt+1 ≥ βLt.
If this is breached, then
the speculator’s collateral is partially liquidated, if possible, to repurchase an amount (cid:96)t+1 > 0 of
STBL. In real protocols, liquidation amounts are automated by an algorithm and will inherently be
ﬁrst order estimates of the amount needed to rebalance the debt position as the algorithm will not
be able to know the actual market structure and price impact. For instance, liquidations in Maker
and Compound release a certain amount of debt to be repaid, and unlock a corresponding amount
of collateral that an arbitrager can use to rebalance the debt position (both decided algorithmically

9

in Compound [2019] and MakerDAO [2017], and the latter decided through auction in Maker’s
newer version MakerDAO [2019]). Consistent with these protocols, we set the amount of debt
that needs to be repaid in a liquidation to be (cid:96)t+1 of STBL such that post liquidation we have
¯NtXt+1 − (cid:96)t+1 = β(Lt − (cid:96)t+1). With β = 3
2 , this amount is

(cid:96)t+1 =

βLt − ¯NtXt+1
β − 1

= 3Lt − 2 ¯NtXt+1.

We interpret this as the protocol’s encoded estimate, using nominal stablecoin price, of how much
collateral it should liquidate in an ‘auction’ to deleverage, similar to Maker. Our model simpliﬁes
the auction to settle on the endogenous stablecoin market. Other liquidation algorithms could also
be considered and would lead to similar qualitative eﬀects.

In a time step with a liquidation, the liquidation forces an upper bound ∆t+1 ≤ −(cid:96)t+1 as this
amount would, in the real protocol, be unlocked for arbitrageurs. But the speculator could choose
to repurchase more STBL to further reduce leverage. The repurchase of (cid:96)t+1 through the liquidation
mechanism is subject to a liquidation cost multiple α ≥ 1–i.e., the eﬀective repurchase price is α×
the STBL market price. The purpose of this fee is that, in real stablecoin systems, liquidations are
performed by arbitrageurs who capture this fee.

Notice that the STBL market price will itself be aﬀected by liquidations. Depending on market
impact, which the algorithms can only observe sequentially, the liquidation may be insuﬃcient to
fully rebalance the debt position back to the collateral constraint. If this occurs, then the issue
will be taken into account with further liquidations in subsequent time steps. The parameter β
in real systems is intended to provide safety in such events so that the system does not become
under-collateralized.

Two thresholds are relevant at time t for calculating expectations of a liquidation eﬀect at time

t + 1. These are non-time-dependent functions of the random variable Lt:

b(Lt) :=

βLt
¯Nt

c(Lt) :=

1
2 ¯Nt

(cid:16)(cid:113)

α2D2 + 4αDLt + L2

t − αD + Lt

(cid:17)

.

The threshold b(Lt) gives the highest t + 1 ETH price that breaches the collateral constraint while
the threshold c(Lt) gives the t + 1 ETH price that consumes the entirety of the speculator’s locked
collateral in a liquidation repurchase due to the eﬀect on STBL repurchase price.11 Below this level,
the speculator cannot meet the collateral demand even by liquidating everything. The formulation
of b(Lt) follows directly from the collateral constraint; the formulation of c(Lt) follows from equating
the repurchase cost of liquidation (cid:96)t+1 to ¯NtXt+1 and solving for Xt+1.
If c(Lt) ≤ Xt+1 ≤ b(Lt), then the liquidation eﬀect is (cid:96)t+1 − (cid:96)t+1
with liquidation fee
repurchase of (cid:96)t+1 STBL (reducing collateral by the repurchase price
factor α) and subsequent reduction of the speculator’s liabilities by the (cid:96)t+1. The variables Lt+1
and Nt are aﬀected similarly.12 If Xt+1 < c(Lt), then the speculator’s collateral position is zeroed
out in the liquidation. We deﬁne the corresponding events

D
Lt−(cid:96)t+1
D
Lt−(cid:96)t+1

α. This represents a

At = {Xt+1 ≥ b(Lt)}

Bt = {c(Lt) ≤ Xt+1 < b(Lt)}.
11The probability of a large deviation like this is not zero. For instance, it could represent the possibility of a

contentious hard fork that splits ETH value.

12Note that Nt is aﬀected because this is the locked collateral at time t + 1. Alternatively, working with Nt+1 as

locked collateral, we would update Nt+1.

10

2.6 System of random variables

Putting all the pieces together, we have the following system of random variables driven by the
random process (Xt):

Xt

Yt+1 =

∆tDXt+1
LtXt
(cid:16)

min




∆∗

t =

min


Lt = Lt−1 + ∆∗
t

(cid:16)
+ ( ¯NtXt+1 − Lt) 1At∪Bt + 1Bt(3Lt − 2 ¯NtXt+1)

1 −

αD
2 ¯NtXt+1 − 2Lt

(cid:17)

(cid:16)

arg max∆t

arg max∆t

¯Nt−1Xt

E[Yt+1|Ft],
(cid:17)
E[Yt+1|Ft], −(3Lt−1 − 2 ¯Nt−1Xt)

β − Lt−1

(cid:17)

if Xt ≥ βLt−1
¯Nt−1
if Xt < βLt−1
¯Nt−1

Nt =

¯Nt =

Zt =

(cid:40)Nt−1 + ∆∗
t
Nt−1 + Zt
Xt

(cid:40)Nt−1

Zt
Xt
(∆t + (1 − α)(3Lt−1 − 2 ¯Nt−1Xt))
if Xt ≥ βLt−1
¯Nt−1
if Xt < βLt−1
¯Nt−1

Nt−1 − α(3Lt−1 − 2 ¯Nt−1Xt)
D
Lt

.

if Xt ≥ βLt−1
¯Nt−1
if Xt < βLt−1
¯Nt−1

In the above, the ﬁrst case for ∆∗

decision collateral constraint while the second cases for ∆∗
that occur during time t.

t comes from maximizing expected value subject to the post-
t , Nt, and ¯Nt apply the liquidation eﬀects

3 Foundational Results

In this section, we derive foundational results about the model that we will use to prove the primary
results of the paper in the next section.

3.1 Assumptions

We begin by deﬁning the assumptions we will use in the rest of the paper.

Assumption 1. (Xt) is a submartingale with respect to (Ft) and is independent from (Lt) and
(Nt).

A submartingale is a stochastic process in which the expected future value, conditioned on all
prior values, is greater than or equal to the current value. The submartingale assumption can
be relaxed somewhat while preserving some results. It is useful, though not necessarily critical,
in our proof of problem concavity. However, the results are most meaningful in a setting like a
submartingale, which always provides a fundamental reason that a speculator might desire leverage.
In such a setting, it is conceivable that the stablecoin could maintain a dollar peg, whereas in long
periods of negative expected returns, the stablecoin concept falls apart as no speculators will want
to participate. As noted in the introduction, such a deviation from the submartingale setting
appears to have occurred in March 2020.

Assumption 2. Each Xt+1 has a conditional probability distribution given Ft, which admits a
density function ft that is continuous almost surely.

11

Equivalently, we consider the process in terms of returns Rt, where Xt+1 = XtRt+1. Conditioned
on Ft, then Rt+1 admits density function gt. In the i.i.d. setting for (Rt), the time dependence can
be dropped. For most results, we do not need to assume i.i.d.

Assumption 3. There is some upper bound r ≥ supn

E[Rn|Fn−1].

The next assumption is needed to interchange derivative and integration operators.

It also

translates to an upper bound on Lt and a lower bound on Nt−1.

Assumption 4. There is some upper bound u ≥ c(Lt) for all Lt.

The next assumption ensures that the STBL price is bounded away from inﬁnity.

Assumption 5. Lt ≥ v > 0 for some v.

The next assumption simpliﬁes repurchase considerations. It is reasonable given a reasonable

bound r on expected returns.

Assumption 6. The liquidation premium factor α is suﬃciently high that the repurchase price in
a liquidation is > 1 almost surely.

The next assumption translates to a reasonable condition on X distributions considering b(Lt)

is linearly increasing whereas c(Lt) decreases with Lt.

Assumption 7. P(Bt|Ft) = P

(cid:16)

c(Lt) ≤ Xt+1 ≤ b(Lt)|Ft

(cid:17)

is increasing in Lt.

Deﬁne ψ(Lt) := E[Yt+1|Ft]. Note that ψ could have a subscript t, or equivalently other time
t inputs ( ¯Nt, Xt, gt), but we relax notation as we only use it in the context of time t. The next
assumption ensures that ψ is concave in Lt, a result that we prove in Proposition 1. When
this is not met, the model starts in a strange region in which the speculator’s objective can be
non-concave and real and nominal liability values can be disassociated. This is an artifact of the
simpliﬁed structure of demand in the model, which we would expect to adapt in such a setting.
Thus we expect the model to not apply well outside of this assumption. Live stablecoin systems
that remain operational readily satisfy this assumption.

αDN ct

Assumption 8.

46 αD (or αZt ≤ 46

2(N ct−Lt)2 ≤ 2 (note Lt ≥ 27
Live stablecoin systems readily satisfy this assumption.13
Additionally, the next assumption ensures that ψ is strictly concave in Lt, which we also prove
in Proposition 1. Notice that this means that either the submartingale inequality is strict at time
t or there is non-zero probability that a liquidation is triggered in the next step. Given that the
latter is certainly reasonable, this assumption is not much stronger than the basic submartingale
assumption.

27 is suﬃcient).

Assumption 9. Either E[Rt+1|Ft] > 0 or P(Bt|Ft) = P

(cid:16)

c(Lt) ≤ Xt+1 ≤ b(Lt)|Ft

(cid:17)

> 0.

While strict concavity of ψ is not necessary for all results, it does simplify the analysis consid-
erably. More generally, concavity of ψ could reasonably be expected in many settings, and so the
assumptions can probably be relaxed. Informally, reasonable distributions for Xt will have con-
centration about the center. In this case, moving ∆t in the positive direction, expected liabilities
increase faster than revenue from new STBL issuance. Moving ∆t in the negative direction, the
cost to buyback grows faster than the decrease in expected liabilities.

13Recall that α ≥ 1 is the liquidation cost multiple (reﬂecting the fee paid to liquidators). Assuming α = 1.05, the

suﬃcient condition in Assumption 8 is implied by Zt < 1.62, which is veriﬁed in practice for all live stablecoins.

12

3.2 Concavity and scale invariance

Our ﬁrst result is to prove that ψ(Lt) is concave in Lt.

Proposition 1. Given Assumptions 1-8, ψ(Lt) := E[Yt+1|Ft] is concave in Lt.
Further, given additional Assumption 9, ψ(Lt) is strictly concave in Lt.

[Link to Proof]

In deriving some results, it will be useful to make assumptions about the scale of the system.
The next result shows that results about Zt should translate to diﬀerently scaled systems, validating
that such results will describe the STBL price process more generally. In the following, we deﬁne
h to output Lt as a function of the system state.

Proposition 2. Consider a system setup (Lt−1, D, Nt−1) with ETH price process (Xt). For γ > 0,

h(γLt−1, γD, γNt−1, Xt) = γh(Lt−1, D, Nt−1, Xt)

h(Lt−1, D,

1
γ

Nt−1, γXt) = h(Lt−1, D, Nt−1, Xt).

As a result, the STBL price process (Zt) is equivalent across these system rescalings.

[Link to Proof]

Under these condtions, we can interchange derivative and integration operators in ∂ψ
∂Lt

according
to Leibniz integral rules (a variation of dominated convergence theorems). The speculator’s choice
of Lt will fulﬁll the ﬁrst order condition of ∂ψ
= 0. From concavity, we can then conclude that
∂Lt
the speculator chooses to increase the STBL supply when ∂ψ
(Lt−1) > 0 and to decrease the STBL
∂Lt
supply when ∂ψ
∂Lt

(Lt−1) < 0.

Note that we can derive suﬃcient conditions for these events using Lemma 2 from the Appendix.
Such conditions can be useful as concrete interpretations of the events and can be checked against
incoming data. That said, these general suﬃcient conditions are far from necessary if we are given
additional information about the return distributions.

3.3 Economic limits to speculator behavior

We now present some fundamental results that bound the speculator’s decision-making. These
results will be useful in developing the primary results of the paper in the next section. The next
result introduces a lower bound to the speculator’s STBL supply decision that arises from the
fundamental price impact of repurchasing STBL.

Proposition 3. Suppose the pre-decision collateral constraint is met at time t. There is a com-
putable lower bound to ∆t.

We can interpret the lower bound in terms of a balance sheet constraint describing when the
speculator’s ETH position is exhausted in a repurchase. We give the speciﬁc bound in the proof but
note that it is not especially useful on its own. Given information about the returns distribution
and the level of current collateral and considering ∂ψ
, much better bounds are possible. Note that
∂Lt
if ζ > 0 is high enough, the lower bound may be the speculator’s entire debt position, which would
be expected in a liquid environment with heterogeneous agents.

13

[Link to Proof]

The next result provides a useful upper bound to the speculator decision Lt. The result is
derived from incentives to issue STBL. Intuitively, it says that if supply is below this bound, then
a speculator may see a proﬁtable opportunity to expand supply. It’s simply not proﬁtable to issue
more STBL than this bound. This doesn’t mean that the speculator decides to achieve the bound,
however, as it underestimates the liquidation costs that the speculator might face.14 Notice that
the bound is strongest when we have κ ∼ 1.

Proposition 4. Suppose either of the following hold for given κ:

• (cid:82)

(cid:16)

b(Lt)
Xt
c(Lt)
Xt

3 − αD ¯NtXtz

2( ¯NtXtz−Lt)2

(cid:17)

gt(z)dz ≤ 0 and P(At ∪ Bt|Ft) ≥ κ−1 > 0

• 1 ≥ P(At|Ft) − 2 P(Bt|Ft) ≥ κ−1 > 0.

Then Lt ≤ (cid:112)κLt−1D E[Xt+1|Ft]/Xt.

[Link to Proof].

The ﬁrst condition comes from the derivative of the expected liquidation eﬀect with respect
to Lt taking β = 3
2 . The integrand can be interpreted as the eﬀective leverage change in a given
liquidation. This quantity is < 0 evaluated at b(Lt) (small liquidations eﬀectively reduce leverage)
whereas it is > 0 evaluated at c(Lt) (in very large liquidations, leverage reduction may not be
eﬀective due to eﬀect on repurchase price). The integral condition then says that, in expectation,
liquidations eﬀectively reduce leverage. This is a reasonable assumption given a starting state of
suﬃcient over-collateralization, since reasonable distributions of Xt+1 will place most mass in the
integral around b(Lt) as opposed to c(Lt), which is a tail event.

The second (alternative) condition says that the probability of having a liquidation is suﬃciently

smaller than not having a liquidation.

This result holds if either of the two conditions hold, both of which could be checked in data-
driven modeling. We will formalize an assumption like the ﬁrst condition in the next section.
Similar results going forward could be derived instead using a variation on the second condition.

4 Stable and Unstable Domains

The primary results of the paper characterize regions in which the stablecoin price process can be
interpreted as ‘stable’ and ‘unstable’. In this section, we derive these results for the given model
of a single speculator facing imperfectly elastic demand for STBL. In the next section, we consider
generalizations of the model and how these results will diﬀer given diﬀerent design and market
structures.

14The model as formulated does not incorporate an interest rate paid by the speculator on issued STBL (the
‘stability fee’ in Dai). Additionally, it does not incorporate a possible yield if the speculator creates STBL to lend on
a lending platform as opposed to selling on the market. Under either of these extensions, Proposition 4 would change
by an appropriate factor.

14

4.1 Domain barriers/Stopped processes

We ﬁrst establish results in terms of barriers. While the stablecoin process is within certain barriers,
we prove that it behaves in ways that are interpretable as ‘stable’ and ‘unstable’. These barriers
are generally stopping times, and we proceed by considering the stopped processes.

Assume that in the initial condition we have E

times:

(cid:104) 1
L1

(cid:105)

|F0

≤ 1
L0

. We deﬁne the following stopping

• τ is the hitting time of E

(cid:104) 1
Lt+1

(cid:105)

|Ft

> 1
Lt

• Tm is the hitting time of Zt > m, for m ≥ Z0

• S1 is the hitting time of E[Lt+1|Ft] < Lt

• S2 is the hitting time of E[Lt+1|Ft] ≥ Lt such that S2 > S1.

As we will see, while the stablecoin mechanism is working as intended, we generally expect the
STBL supply to increase (equivalently in this setting, the STBL price to decrease, though in slow
and bounded way). With this context in mind, τ represents the ﬁrst time we expect the STBL
price to increase. Notice that this is an expectation of reciprocal of supply, a convex function, and
so through Jensen’s inequality, this is weaker than expecting the speculator to deleverage/reduce
supply. In particular, we have τ ≤ S1.

Note that the expectations of the process are not necessarily the same as the movements of the
process: τ does not necessarily correspond to the ﬁrst time the process actually increases in price.
We track this with Tm, the time the STBL price breaches a given level above Z0, which may be
before or after τ .

The stopping times S1 and S2 track when expectations about STBL supply change. These can
be equivalently stated (and calculated in a data-driven model) based on expectations about the
derivative of E[Yt+2|Ft] with respect to Lt+1 evaluated at Lt, similarly to the discussion from the
previous section on concavity.

Before proceeding, we formalize stopped versions of assumptions in Proposition 4. The interpre-
tation of these assumptions is the same as discussed in the previous section. Note that the results
going forward could also apply more generally subject to additional stopping times embedding these
assumptions. For notational simplicity, we just present the results subject to the stopping times
already deﬁned with the assumptions given.

Assumption 10. For t ≤ τ , P(At ∪ Bt|Ft) = P(Xt+1 ≥ c(Lt)|Ft) ≥ κ−1 > 0.

Assumption 11. For t ≤ τ , (cid:82)

(cid:16)

b(Lt)
Xt
c(Lt)
Xt

3 − αD ¯NtXtz

2( ¯NtXtz−Lt)2

(cid:17)

gt(z)dz ≤ 0.

Notice that κ will be > 1 but ∼ 1 as X < c(Lt) is a low probability event.
Recall that the STBL price Zt is a function of collateral value, expectations about ETH returns,
and expectations of liquidation costs (related to tail risks). These factors enter the speculator’s
supply decision, which then enters Zt. Going forward, we will explore how changes in these aﬀect
the STBL price process.

15

4.2 ‘Stable’ domain

Subject to the barriers τ and Tm, the stablecoin process can be interpreted as stable in the following
ways. In this domain, we derive bounds on large price movements and quadratic variation. We
show below that for realistic values of parameters, the bounds are suﬃciently powerful in practice.
Our ﬁrst result bounds Zt under the condition TZ0 > τ . Conditioned on this, the price is
κr ∼ 1. Recall that r represents
, whereas κ−1 is a lower bound for the probability that

contained within small variation–e.g., consider Z0 = 1 and consider 1
E[Xt+1]
the upper bound on returns, r = supt
Xt
the collateral is not exhausted in a liquidation event, P(Xt+1 ≥ c(Lt)|Ft) ≥ κ−1.

Proposition 5. If TZ0 > τ , then

(cid:115)

Z0 ≥ Zt∧τ ≥

D
κLt∧τ −1r

≥

D
1
2t−1
2t
2t L
0

(κDr)

.

Furthermore for any t, Lt∧τ ≤ κDr and Zt∧τ ≥ 1
κr .

[Link to Proof]

The condition TZ0 > τ introduces dependence on future events. As such, we can’t conclude

with the information at time t that the t + 1 price is bounded in this way.

However, we can bound our expectations on the t + 1 price given the information at time t (Ft).
This approach relies on the fact that the versions of the process behave as submartingales in the
stopped setting.

Proposition 6. (Lt∧τ ) is a submartingale bounded above and (Zt∧τ ) is a supermartingale bounded
below. Thus they converge almost surely.

[Link to Proof]

An immediate bound on expected price comes from the fact that stopped version of Zt is a
supermartingale. This is the ﬁrst result of the next proposition. Additionally, with a stronger
assumption on (Xt) that conditional expectation of returns is non-decreasing within the domain
barriers, we can bound the expected price further.

Proposition 7. The process (Zt∧τ ∧TZ0

) is bounded in expectation by

Further, assuming that for t < τ , (E[Rt+1|Ft]) is non-decreasing, then for t ≤ τ ,

Z0 ≥ E[Zt∧τ ∧TZ0

] ≥

1
κr

.

Zt−1 ≥ E[Zt∧τ |Ft−1] ≥

(cid:115)

D
κLt−1 E[Rt|Ft−1]

.

[Link to Proof]

Going forward, we will work with a variation on the price process

Z(cid:48)

t := |m − Zt|

for given m ≥ Z0.

Using m = 1, this has concrete interpretation as the absolute price deviation from the stablecoin
peg. The stopped version of this process has the useful property of being a non-negative submartin-
gale. In addition, (Z(cid:48)
t) shares similar large deviation and quadratic variation properties with (Zt),
which we explore in the remainder of this subsection.

16

Lemma 1. The stopped process (Z(cid:48)

t∧τ ∧Tm

) is a non-negative submartingale.

[Link to Proof]

We deﬁne the maximum process over some process (θt) as θ∗

N = maxt≤N |Θt|. The next result

bounds the expected maximum of the deviation process (Zt).
Proposition 8. Suppose m ≥ Z0. Denote E := E[Zτ ∧Tm − m|Zτ ∧Tm > m]. Suppose any one of
the following conditions holds:
κr > m and E > 1
κr = m and E > 0

κr − m

• 1

• 1

• 1

κr < m and E ≥ 0.

Then

E[Z(cid:48)∗

τ ∧Tm

] ≤ 2 (cid:0)m − 1
κr

(cid:1) .

[Link to Proof]

The value (m − 1

κr ) describes the range of the domain considered. Prior to Tm, we know that
the price falls in this range. The nontrivial part is describing what happens at the stopping time
as it exceeds this range if the stop is triggered by Tm. The value E is the expected deviation at the
stopping time given that Tm triggers the stop. By deﬁnition, we have that E > 0. Given reasonable
κ, r, and m, the condition for Proposition 8 is satisﬁed quite broadly. For instance, the concrete
instance with m = 1 is satisﬁed since 1

κr < 1 taking into account the above discussion on κ.

Notice that the analysis for the proof can lead to better bounds if we have more information
about E or p := P(Zτ ∧Tm ≤ m), e.g., by incorporating information from other results above or from
knowledge about the distributions of (Xt), such as from historical data. Additionally, the analysis
can be used to bound either E or p given bounds on the other.

We now state the ﬁrst main results of the paper. Our next result applies Doob’s inequality to

bound the probability of large deviations in the stopped process.

Theorem 1. For m ≥ Z0 and (cid:15) > 0,

P

(cid:18)

max
n≤τ ∧Tm

(cid:19)

Z(cid:48)

n > (cid:15)

≤ 2(cid:15)−1

(cid:18)

m −

(cid:19)

.

1
κr

[Link to Proof]

τ ∧T1

The result can be quite powerful. Consider the concrete case of m = 1, in which case Z(cid:48)
t
describes the deviation from the peg, and take (arguably reasonable) κ−1 = 0.999 (99.9% chance
Xt won’t drop below c(Lt)) and r annualized as 1.5 (daily r = 1.0011). Then the probability that
the stablecoin deviates from the peg by more than 0.1 is P(Z(cid:48)∗

> 0.1) ≤ 0.042.

Our next result derives from a form of Burkholder’s inequality that applies to non-negative

submartingales. We deﬁne the quadratic variation of (Z(cid:48)

t) by

[Z(cid:48)]t :=

t
(cid:88)

k=1

(Z(cid:48)

k − Z(cid:48)

k−1)2.

The quadratic variation is a stochastic process that measures how spread out the underlying process
is. Its expectation at time t is related to the variance at that time, supposing variance is deﬁned–
in particular, they are equal if the underlying process is a martingale. The result bounds the
probability of large quadratic variation in the stopped process. In essence, with high probability,
the quadratic variation can’t be too far away from the expected maximum.

17

Theorem 2. Suppose m ≥ Z0 and (cid:15) > 0. Then
(cid:16)(cid:112)[Z(cid:48)]τ ∧Tm > (cid:15)
(cid:17)

P

≤ 6(cid:15)−1

(cid:18)

m −

(cid:19)

.

1
κr

[Link to Proof]

This result is also quite powerful. Considering the same setting as above, we have

P((cid:112)[Z(cid:48)]τ ∧T1 > 0.1) ≤ 0.127

in the stable domain.

Bounds on the expectation of quadratic variation can also be obtained using a more classical
form of Burkholder’s inequality, albeit with stronger assumptions. We develop this idea in the next
remark.

Remark 1. There is an additional form of Burkholder’s inequality that extends to non-negative
submartingales. If we are additionally given a useful bound on E
for some 1 < p < ∞
(for instance, if we have some distribution assumptions on (Xt)), then we can apply Lemma 3.1 in
Burkholder [1973] to derive the following bound on quadratic variation expectations:

(cid:104)(cid:0)Z(cid:48)

(cid:1)p(cid:105)

τ ∧Tm

E

(cid:104)(cid:0)[Z(cid:48)]τ ∧Tm

(cid:1)p(cid:105) 1

p ≤

1
9p
2
1 − p−1

E

(cid:104)(cid:0)Z(cid:48)

τ ∧Tm

(cid:1)p(cid:105) 1
p .

A topic of ongoing research is obtaining the Best constants/bounds in Burkholder’s inequality,
which may be able to tighten the bound. The classical two-sided Burkholder inequailty may not
extend to non-negative submartinagales. In general, only the ﬁrst half of the Burkholder inequality
(bounding expectations about quadratic variation by the maximum) extends to this setting and only
for 1 < p < ∞. This contrasts with Proposition 2, where we can derive results about probability of
large quadratic variation of non-negative submartingales for the p = 1 case. From a practical point
of view, this may be suﬃcient.

Notice that with an eﬀective bound on the expectation of quadratic variation (QV) of the entire

stable process, we have by law of large numbers

QV
n

→ 0 as n → ∞.

So the longer the process is stable, the smaller the variability.

As we’ve characterized this ‘stable’ domain based on τ and Tm, an exit from this region corre-
sponds to either a change in expectations (τ ) or a large deviation event (Tm). In actual applications,
we will know when these stopping times arrive (or will at least have good measures of it, when
hard to directly observe). These could be used by system stakeholders as indicators that the local
regime is changing. Statistical analysis on historical data could also predict how likely we are to
see such indicators in coming steps.

4.3 ‘Unstable’ domain

We now characterize how the stablecoin can be interpreted as unstable outside of the barriers
described above. The intuition here is that the speculator’s position is nearer to c(Lt) and b(Lt),
and so expected costs of liquidation increase and are more sensitive to the threshold proximity,

18

in addition to being driven by the volatile process (Xt). The remaining results in this section
characterize a deﬂationary regime that is connected with instability in terms of forward-looking
variance of stablecoin prices and large deviations. In this regime, we observe deleveraging spirals,
which resemble short squeezes, and are counterintuitive as they lead to stablecoin price appreciation
during times of collateral shock and lead to faster collateral drawdown.

Our next result characterizes a deﬂationary regime deﬁned by stopping times S1 and S2. In
such a setting, an opposite behavior occurs compared to the stable region: (Zt) behaves as a
submartingale, tending to increase in price. The submartingale nature of the stablecoin price
underpins the short squeezes within deleveraging spirals.

Theorem 3. Restarting the process at S1, we have that (Lt∧S2) is a supermartingale and (Zt∧S2)
is a submartingale.

[Link to Proof]

The previous result guarantees that the process, after crossing S1, enters a deﬂationary regime
in a precise sense. This deﬂationary regime can be triggered by the factors aﬀecting S1, such as
any of the following: shocks to collateral levels, increased expectations around deleveraging costs,
or depressed ETH expectations. Similarly to the results above, in real applications, these stopping
times can be used by stablecoin stakeholders as indicators that the local regime is changing and to
statistically estimate the probable lengths of such deleveraging spirals.

The intuition behind deleveraging spirals is illustrated in Figure 2.

In an equilibrium, the
stablecoin supply is matched to demand. As a ﬁrst wave of speculator liquidations occur, whether
voluntary deleveraging or automated by the protocol, collateral is used to repurchase the stablecoin
to reduce the supply. In an imperfectly elastic market, this causes an imbalance in demand relative
to supply, and an increase in stablecoin price is needed to reduce demand. This has an amplifying
eﬀect, however, in follow-on rounds of liquidations: more collateral is needed to reduce supply by
the same amount because of the increased stablecoin price, and each round of liquidations continues
to increase the stablecoin price.

Black Thursday in March 2020 provides strong evidence of deleveraging spirals in the Dai
stablecoin. ETH price crashed ∼ 50% on 12 March 2020 (Figure 3a) This triggered a wave of
liquidations in Dai, as well as other cryptocurrency systems. These liquidations led to a cornering
eﬀect from deleveraging spirals in the Dai market, as shown in Figure 3b. Speculators faced
premiums in excess of 10% to deleverage during the crisis and lingering premiums > 2% several
weeks after. The cornering eﬀect is also supported by lending rates on Dai, which reached high
double digits during the crisis (Figure 3c). Maker was also aﬀected by global mempool ﬂooding on
Ethereum during the crisis, which caused many Dai liquidation auctions to clear at near zero prices.
This had the eﬀect of amplifying the deleveraging eﬀect on collateral and led to a $4m shortfall in
the system. See Blocknative [2020], Topbottom [2020] for more details. Many market participants
were surprised in this crisis that Dai traded at signiﬁcant premiums despite the much riskier state
of Maker in terms of collateral and liquidations, which our model explains as deleveraging spirals.

Remark 2. (Interaction with cascading liquidations) A diﬀerent type of deleveraging spiral can
occur in debt security models when the collateral asset price is endogenous to the model and can
be depressed from the market impact of liquidations (e.g., ﬁre sales). In this context, liquidations
can cascade with a ﬁrst round of liquidations triggering a follow-up rounds due to the impact on
the collateral market. Conceptually, when this endogenous collateral eﬀect is added to our model,
the two deleveraging spiral types amplify each other. In particular, when the price of the stablecoin
increases from the eﬀects described above, more collateral must be liquidated to deleverage the same

19

Figure 2: Illustration of deleveraging spirals. In liquidations, collateral is used to reduce supply.
Stablecoin price rises in response to imbalance with demand. This has an amplifying eﬀect in
follow-on liquidations.

(a)

(b)

Figure 3: Black Thursday in March 2020. (a) ∼ 50% ETH price crash (OnChainFX). (b) Delever-
aging eﬀects on Dai price and volatility (OnChainFX). (c) Deleveraging eﬀects on Dai lending rate
(LoanScan)

(c)

20

≠SupplyDemandPrice-$1CollateralLiquidation=SupplyDemandPrice-$1Collateral2ndLiquidation=SupplyDemandPrice-$1CollateralLiquidation≠SupplyDemandPrice-$1Collateral2ndLiquidationA. Deleveraging Round 1B. Deleveraging Round 1C. Deleveraging Round 2D. Deleveraging Round 2amount, and this greater collateral liquidation has a higher impact on the collateral asset market,
which can trigger further liquidations cyclically in larger size than with the ﬁre sale eﬀect solely.
We discuss how to endogenize collateral asset prices to the model in the Appendix.

We now derive practical tools that will connect these regimes containing deleveraging spirals
with instability in terms of forward-looking price variance of the stablecoin, and which do not
require the detection of whether S1 has occurred. This formalizes the high price variation observed
in Dai during and after Black Thursday. We begin in the next remark by setting up a variance
estimation idea based on Taylor approximation.

Remark 3. (Estimating variances) Taylor approximations can be applied to estimate the variances
of the stablecoin process. Consider Xt = Xt−1Rt for return Rt ≥ 0. For notational clarity, deﬁne15

h(ρ, n) := arg max

Lt

E[Yt+1|Ft] = Lt,

where ρ, n are realizations of Rt, ¯Nt. Variance in stablecoin supply follows
(cid:1)2 Var(Rt|Ft−1)

Var(Lt|Ft−1) ≈ h(cid:48) (cid:0)E[Rt|Ft−1], ¯Nt

and the stablecoin price variance approximation is

Var(Zt|Ft−1) ≈

Dh(cid:48)(E[Rt|Ft−1], ¯Nt)2
E[Lt|Ft−1]4

Var(Rt|Ft−1).

(1)

This is given informally, but could in principle be formalized using two steps of compounded Taylor
approximation error. The approximation error is arguably moderate considering that our domain
is bounded away from singularities (e.g., our lower bound results on L).

This variance approximation (Eq. 1 in Remark 3) is low in the stable domain and can be
high in the unstable domain, as formalized in the following Theorem 4. We introduce a few
more assumptions that we use only in deriving the remaining results in this section. All of these
assumptions come down to assumed properties of the Rt distribution.

Assumption 12. The post-decision collateral constraint at time t is not binding in the speculator’s
maximization.

This ﬁrst assumption means that the speculator’s objective fully accounts for the post-decision
collateral constraint (i.e., by maximizing the objective, the speculator by extension also satisﬁes
the constraint). This is reasonable unless expected returns are excessively high.

Assumption 13. Returns Rt−1 and Rt are independent.

Assumption 14. ψ is twice continuously diﬀerentiable.

This last assumption restricts the density gt. We now present the result, which applies the
implicit function theorem to derive the derivatives of h, which describe the sensitivity of h to price
and collateral level.

Theorem 4. Under the above assumptions, the following hold:

1. ∂

∂ρ h(ρ, n) ∂

∂n h(ρ, n) exist;

15As in the case of ψ, h could have a subscript t (or equivalently other time t inputs), but we relax notation as we

only use in the context of time t.

21

2. ∂

∂ρ h(ρ, n) ≥ 0 and is increasing in −ρ by order of 1

ρ for ρ ≥ bt−1
Xt−1

3.

∂

∂n h(ρ, n) ≥ 0 and is increasing in −n by order of 1

n for n ≥ bt−1
Xt

, Lt > 8;

, Lt > 8;

4. ∃ε with 0 < ε < 1, s.t. ∂

∂ρ h(ρ, n) > 1 if ρ < ε , Lt > 27

46 αD, and ct > 2.

As a result, the variance approximation in Eq. 1 increases by order of 1
R2
t

in −Rt and 1
¯N 2
t

in − ¯Nt.

[Link to Proof]

Theorem 4 shows that the variance approximation in Eq. 1 in Remark 3 increases by order of
1
during an ETH return shock (result 2). Recall that Rt is multiplicative return, and so the eﬀect
R2
t
is large for a signiﬁcant shock Rt < 1. Similarly, settings with lower collateralization in the initial
conditions have higher variance approximation by order of 1
(result 3). Such diﬀerences in initial
¯N 2
t
conditions of collateral could result from, for example, diﬀerent realizations of liquidations or the
speculator abandoning its collateral position (and so extracting any excess collateral it can). Result
4 shows that there are cases where the h(cid:48) factor in the variance approximation is > 1, meaning that
the variance of Rt, the inherently volatile process, will carry through directly to Zt, the ‘stable’
process.

Note that the extra conditions on the scale of Lt and ct in Theorem 4 results 2-4 may seem
strange at ﬁrst sight. Since the (Zt) process is scale-invariant, as proven in Proposition 2, the
results about Zt variance hold more generally. In particular, recall that a term of ∼ 1
shows up
Lt
in the variance approximation in Remark 3, which will cancel out the conditions on scale.

Up to this point, we have only been able to say things about variance estimations. We will
now show that the ‘stable’ and ‘unstable’ regimes are well-interpreted in the following sense: given
diﬀerent initial conditions of the same process, the forward-looking stablecoin price variances are
indeed distinct. If we start in the unstable regime, we will always have higher variance than if we
start in the stable regime. The next result formalizes this.

Theorem 5. In addition to the previous assumptions, suppose Xt ≥ b(Lt−1)+(cid:15) for some (cid:15) > 0 (the
pre-decision collateral constraint is exceeded by (cid:15), which restricts the ranges of both Xt and ¯Nt−1).
Consider two possible states s and u of the stablecoin at time t that diﬀer only in collateral amounts
¯N s
t−1 and evolve driven by the common price process (Xt). Then the forward-looking price
variances satisfy

t−1 > N u

Var(Zs

t |Ft−1) < Var(Zu

t |Ft−1).

[Link to Proof]

Special care should be given to the treatment of Zt under the condition Xt ≤ c(Lt−1), as the
STBL price may no longer be well-deﬁned without ζ > 0 as no collateral remains. In a real system,
this is equivalent to the event that all speculators are wiped out. The reason for our condition
on Xt in the above result is partly to keep things well-deﬁned and partly because there can be a
non-smooth point in h at Xt = b(Lt−1).

Similar variance diﬀerence results can be derived for varying initial conditions of Xt−1 and Lt−1
as opposed to ¯Nt−1. In some sense, these are all similar as they change the initial collateralization
level, though there will be some diﬀerence in price eﬀect.

These analytical results describe regimes in which the stablecoin can be interpreted as stable
and unstable. As we have discussed, they can be adapted into data-driven risk tools, for instance

22

to estimate probabilities of peg deviations and to infer about how likely regimes are to change in
the near future.

While these results apply over limited steps ahead–e.g., forward-looking variance is derived for
the next time period–they do point in the right direction that stability domains are related to
traditional measures in ﬁnance. Naturally, it would be good to have results describing further
periods into the future. In principle, these could be estimated, although the process in this section
is already complex. The fact that we are able to relate these regimes analytically to forward-looking
variance is already a step ahead, and a valuable new result in its own right. We conjecture that it
could work similarly over multi-steps, though in less tractable ways.

5 Stability in ‘Perfect’ Settings

In the previous section, we considered the given model of a single speculator facing imperfectly
elastic demand for STBL. We now consider idealized settings, in which STBL demand is perfectly
elastic and/or unlimited speculator supply exists. In these idealized settings, we demonstrate that
stablecoin can be interpreted as well-stabilized.

5.1 Perfectly elastic demand

Under perfectly elastic demand, STBL demand is time-dependent Dt, which adapts in each time
period to match STBL supply. This results in Zt = 1. In this case, the speculator’s issue and
repurchase price is always $1 and $α in a liquidation. The problem simpliﬁes to evaluating

E[Yt+1|Ft] = ∆t E[Rt+1|Ft] +

(cid:90) ∞

ct
Xt

( ¯NtXtz − Lt)g(z)dz

+ (1 − α)

(cid:90) bt
Xt

ct
Xt

βLt − ¯NtXtz
β − 1

g(z)dz,

where the liquidation eﬀect is now (cid:96)t+1(1 − α) where (cid:96)t+1 = βLt− ¯NtXt+1

β−1

.

In this setting, we have ∂ψ
∂Lt

β−1 (α − 1) P(Bt). Recalling that P(At)
and P(Bt) are functions of Lt and supposing a non-binding collateral constraint, the speculator
chooses Lt such that

= E[Rt+1|Ft] − P(At ∪ Bt) − β

E[Rt+1|Ft] = P(At ∪ Bt) +

(α − 1) P(Bt).

β
β − 1

Noting that E[Rt+1] ≥ 1, P(At ∪ Bt) is decreasing in Lt but generally ∼ 1, and P(Bt) is increasing
β
β−1 × the expected
in Lt, this is interpretable as the speculator balancing expected return against
(constant) liquidation cost in deciding whether to issue a new unit of STBL.

In this setting, the STBL price is identically $1 and the speculator only faces the risk of leveraged
ETH declines subject to a ﬁxed liquidation fee. Liquidations generally work well to keep the system
over-collateralized, and the only real risk to STBL holders is from extreme single period declines
in ETH price.

5.2 Unlimited speculator capital supply

Suppose there is an inﬁnite depth of speculator’s capital ready to enter the STBL market given what
they see as a proﬁtable opportunity subject to STBL demand D. The speculator in such a market
would choose to deposit collateral and issue new STBL at time t if DLt−1
E[Rt+1|Ft] − γ ≥ 0, where

L2
t

23

γ represents the representative speculator’s expected liability and liquidation cost after entering the
market. Arguably, γ ∼ 1 as, in an inﬁnite depth market, the speculator can start from a position
of low leverage.

The speculator’s proﬁtability (for the marginal STBL issue) will be 0, which yields equality in

the above condition, and therefore,

Lt = (cid:112)γDLt−1 E[Rt+1|Ft].

Notice the similarity with the upper bound in Proposition 4.

Further using that (Xt) is a submartingale, in which case E[Rt+1|Ft] ≥ 1, we ﬁnd the STBL
price is constrained to a small range of Z0 ≥ Zt ≥ 1
γr . This resembles the perfectly elastic demand
case. In this case speculators are able to liquidate positions without inﬂuencing STBL price, while
in the inﬁnite depth case because the speculator is always willing to issue new STBL to oﬀset a
liquidation.

5.3 No stable region if (Xt) is not a submartingale

The mechanisms that make the idealized settings well-stabilized break down when the ETH price
process (Xt) is not a submartingale. This stresses how fragile the stablecoin market is to negative
expectations in the primary ETH market, even under these idealized settings. In the unlimited
speculator case, speculators no longer enter the market if expectations are negative, and so we
don’t achieve the supply bound developed above. Instead, we return to the main setting of the
paper, which can be interpreted as unstable under negative expectations as it leads to deleveraging
eﬀects. In the perfectly elastic demand setting, the STBL supply goes to zero as the speculator
chooses not to participate.

6 Discussion

This paper presents a new stochastic model of non-custodial over-collateralized stablecoins, where
the collateral has value exogenous to the stablecoin system and the stablecoin has an endogenous
market price. These stablecoins bear a resemblance to a non-custodial form of the current monetary
system of commercial bank money but give rise to new risks such as those experienced on Black
Thursday. These stablecoins stand in contrast to unbacked or endogenously backed stablecoins, such
as Terra UST, which are better understood using tools of insolvency and currency peg models, as
well as custodial stablecoins such as Tether, which can resemble the underlying structures of narrow
banks or money market funds.

In our model, we formally characterize domains that can be interpreted as stable and unstable
for the stablecoin. By bounding the probability of large deviations and the quadratic variation of
the price process, we prove that the stablecoin behaves in a stable way when restricted to a certain
region.
In contrast, price variance is shown to be distinctly greater in a separate region. This
is triggered by large deviations, collapsed expectations, and liquidity problems from deleveraging.
We also characterize a deﬂationary deleveraging spiral as a submartingale, which can exacerbate
liquidity problems in a crisis. These deleveraging spirals resemble short squeezes, and are coun-
terintuitive as they lead to stablecoin price appreciation during times of shock, whereas we might
otherwise expect prices to depreciate given the riskier state of the system. Further, this appre-
it leads to faster collateral drawdown, and potentially shortfalls, as more
ciation is detrimental:
collateral is required to fulﬁll liquidations and is accompanied by higher price variance.

An observation from the model is that the speculator chooses a collateral level above the required
collateral factor. This is because the expected liquidation cost is greater than the $1 face value. The

24

speculator will desire to increase the collateralization during times when the expected liquidation
cost is higher, which can occur after a shock to collateral value or if the speculator expects the
collateral to be more volatile. This generally explains the high level of over-collateralization seen
in Dai, which typically ranges 2.5 − 5× although the collateral factor is 1.5×.

The presence of deleveraging eﬀects poses fundamental trade-oﬀs in decentralized design. One
way to bring the stablecoin closer to the ‘perfect’ stability cases is to increase elasticity of demand.
This relies on the presence of good uncorrelated alternatives to the stablecoin. As all non-custodial
stablecoins likely face similar deleveraging risks, greater elasticity relies on custodial stablecoins
or greater exchangeability to ﬁat currencies. Another way to bring the stablecoin closer ‘perfect’
stability is to increase the supply of new speculators. As there will not be unlimited supply of
speculators with positive ETH expectations (especially during an extended bear market), this relies
on having another uncorrelated collateral asset. As all decentralized assets are very correlated, this
again largely relies on including custodial collateral assets, like Maker’s recent addition of USDC.16
While these measures strengthen the stability results, it’s at the expense of greater centralization
and moves the system away from being ‘non-custodial’.

We suggest a way to improve the design of Dai’s savings pool toward damping deleveraging
eﬀects without greater centralization through incentivizing exchangeability of Dai during delever-
aging events. In its current state, the Maker system charges fees to speculators, part of which it
passes on to Dai holders as an interest rate if the holder locks the Dai into a savings pool. With
modiﬁed mechanics, this savings pool can provide a buﬀer to deleveraging eﬀects. For instance,
if we allow Dai in the savings pool to be bought out at a reasonable premium to face value by a
speculator who uses it to deleverage, then deleveraging eﬀects are bounded by the premium amount
up to the size of the savings buﬀer. The Dai holders who participate in this savings pool are then
compensated for providing a repurchase option to the speculator. The Dai holder could elect to
have the repurchase fulﬁlled in the collateral asset, or something else, like a custodial stablecoin.
In this way, this mechanism can provide some of the beneﬁts of the ‘perfect’ stability settings while
enabling Dai holders to choose how decentralized they want to be. A Dai holder who does not re-
quire high decentralization would elect to receive the compensation from the savings pool whereas
a Dai holder who requires higher decentralization would choose not to use the savings pool. Our
model can be extended to consider such mechanisms.

Since the release of our paper, mechanisms resembling this, which try to boost liquidity around
liquidations to quell deleveraging spirals, have been adopted by projects such as Liquity [2020].
Empirically, these mechanisms have the eﬀect of smoothing deleveraging eﬀects over a longer time
period, lowering the eﬀect of shocks but not entirely removing the short squeeze eﬀect (see Figure 4).
Maker has chosen to go a diﬀerent direction by maintaining direct exchangeability with the custodial
USDC MakerDAO [2020b], which has allowed Dai to maintain a close peg through subsequent crises
at the expense of heavy reliance on custodial stablecoins. The stablecoin Rai has chosen a third
path of instituting negative rates on stablecoin holders during crises Reﬂexer [2020] via a PID
controller, which is eﬀectively charging stablecoin holders insurance premiums when demand for
stablecoins outweights demand for leverage, thus lowering demand to help attain peg.

Our model and results can also apply more broadly to synthetic and cross-chain assets and over-
collateralized lending protocols that allow borrowing of illiquid and/or inelastic assets– whenever

16Recall that custodial assets face their own risks, however, which may not be uncorrelated in extreme crises.
Custodial stablecoins are subject to counterparty risk, systematic risks, bank run risks, asset seizure risk, and eﬀects
from negative interest rates. The treasury secretary J. Yellen referred to the materialization of these risks in her
annual testimony in front of the Senate Banking Committee, on May 10th 2022: “A stablecoin known as TerraUSD
experienced a run and declined in value,” Yellen said. “I think that this simply illustrates that this is a rapidly
growing product and there are rapidly growing risks.”

25

Figure 4: Eﬀect of Liquity’s stability pool on LUSD price in Curve’s on-chain market in the May
2021 crisis. Deleveraging eﬀect is delayed and smoother compared to Dai’s price eﬀect on Black
Thursday (cf. Figure 3b).

the mechanism is based on leveraged positions and leads to an endogenous price of the created
or borrowed asset. We have characterized the risk that such structures feature intertwining of
collateral liquidation spirals and short squeezes of the created asset. Synthetic assets generally use
a similar mechanism just with a diﬀerent target peg. Cross-chain assets that port an asset from a
blockchain without smart contract capability (e.g., Bitcoin) to a blockchain with smart contracts
(e.g., Ethereum) also tend to rely on a similar mechanism. In non-custodial constructions such as
Zamyatin et al. [2019] and Synthetix [2020], vault operators are required to lock ETH collateral
in addition to the deliverable BTC asset. They bear a leveraged ETH/BTC exchange rate risk
and face similar deleveraging risk. In particular, to reduce exposure, they need to repurchase the
version of the cross-chain asset on Ethereum.

Several generalizations of analytical results are left for future research. Here we considered
collateral prices exogenous, but it would be interesting to model market impact eﬀects of large
collateral liquidations and also enable modeling of stablecoins like Synthetix sUSD that have en-
dogenous collateral (see Klages-Mundt et al. [2020]). One possible way to endogenize collateral
prices is via an inverse demand function. We expect that the general methods used in this paper
can be applied to partial equilibrium settings such as this. Naturally, this would necessitate con-
ditions on the inverse demand function that ensure that the expected returns as a function of the
issuance remains concave.

We have speciﬁed the speculator’s decision-making in terms of a sequence of one-period op-
timization problems. Alternatively, the speculator could strategically coordinate the sequence of
decisions further into the future and develop long-term strategies. This could be formulated by
using an exit time for the speculator, when they can cash our their position by selling to someone
else at par. If this terminal time is deterministic, the problem can be formulated as a dynamic
program, in which the terminal decision results from the one-period optimization, intermediate
decisions solve a Bellman equation conditioned on the information revealed up to that point, and
random returns are independent. For instance, Biais et al. [2019] sets up a supermodular game in
a setting where agents exit at a random exponential time.
in t The model could be extended to
include multiple speculators. Speculators have in reality a ﬁnite depth and moreover, they main-
tain positions with diﬀerent leverage points and ETH expectations. This can lead to a sequential
schedule of liquidation points at a given time throughout the system, which will be reﬂected in a
speculator’s expected liquidation costs. A given speculator will take into account price eﬀects from
the potential liquidations of other speculators’ positions in addition to their own, see Minca and
Wissel [2020] for leveraging-deleveraging games in the traditional banking system. Here, the spec-
ulator’s value depends on liquidation costs and on the supply limit imposed by the ﬁnite market
depth. Incorporating strategic aspects is left for future research.

26

7 Data availability statement

The contribution of this paper is theoretical. Where examples have been provided to support
theoretical ﬁndings, price data is publicly available (by Kaiko - Digital Assets Data Provider and
LoanScan platform).

References

Angeris, G., Kao, H.-T., Chiang, R., Noyes, C., and Chitra, T. (2020). An analysis of Uniswap

markets. Crypto Economic Systems 2020.

Biais, B., Bisi`ere, C., Bouvard, M., and Casamatta, C. (2019). The Blockchain Folk Theorem.

Review of Financial Studies, 32(5):1662–1715.

Blocknative (2020). Evidence of mempool manipulation on black thursday: Hammerbots, mempool

compression, and spontaneous stuck transactions.

Bloomberg (20 May 2022). How $60 Billion in Terra Coins Went Up in Algorithmic Smoke. https:

//www.bloomberg.com/graphics/2022-crypto-luna-terra-stablecoin-explainer/.

Boyd, S. and Vandenberghe, L. (2009). Convex optimization. Cambridge university press.

Bullmann, D., Klemm, J., and Pinna, A. (2019).

In search for stability in crypto-assets: Are

stablecoins the solution? ECB Occasional Paper, (230).

Burkholder, D. L. (1973). Distribution function inequalities for martingales. the Annals of Proba-

bility, pages 19–42.

Cao, Y., Dai, M., Kou, S., Li, L., and Yang, C. (2021). Designing stable coins. Available at SSRN:

https: // ssrn. com/ abstract= 3856569 .

Chitra, T. (2020). Competitive equilibria between staking and on-chain lending. Crypto Economic

Systems 2020.

cLabs (2019). An analysis of the stability characteristics of Celo. Technical report, https://celo.

org/papers/Celo_Stability_Analysis.pdf.

(17 Mar.

Coindesk
eral
makerdao-adds-usdc-as-defi-collateral-following-black-thursday-chaos.

MakerDAO
chaos.

USDC
collat-
https://www.coindesk.com/

Thursday’

following

‘Black

2020).

DeFi

adds

as

Compound (2019).

Compound:the money market protocol.

https://compound.finance/

documents/Compound.Whitepaper.pdf.

Detrio, C. (2015).
smart-markets/.

Smart markets for stablecoins.

Technical report, http://cdetr.io/

Diamond, D. W. and Dybvig, P. H. (1983). Bank runs, deposit insurance, and liquidity. Journal

of political economy, 91(3):401–419.

Dybvig, P. H. and Zender, J. F. (1991). Capital structure and dividend irrelevance with asymmetric

information. The Review of Financial Studies, 4(1):201–219.

27

Evans, A. (2019). A Ratings-Based Model for Credit Events in MakerDAO.

Gudgeon, L., Perez, D., Harz, D., Gervais, A., and Livshits, B. (2020). The Decentralized Financial

Crisis: Attacking DeFi. arXiv preprint arXiv:2002.08099.

Guimaraes, B. and Morris, S. (2007). Risk and wealth in a model of self-fulﬁlling currency attacks.

Journal of Monetary Economics, 54(8):2205–2230.

Harz, D., Gudgeon, L., Gervais, A., and Knottenbelt, W. J. (2019). Balance: Dynamic Adjustment
of Cryptocurrency Deposits. In Proceedings of the 2019 ACM SIGSAC Conference on Computer
and Communications Security (CCS ’19). ACM.

Huo, L., Klages-Mundt, A., Minca, A., Munter, F., and Wind, M. (2022). Decentralized Governance
of Stablecoins with Closed Form Valuation. In Mathematical Research for Blockchain Economy
(to appear). https://arxiv.org/abs/2109.08939.

Kacperczyk, M. and Schnabl, P. (2013). How safe are money market funds? The Quarterly Journal

of Economics, 128(3):1073–1122.

Klages-Mundt, A. (14 Dec 2018). The state of stablecoins–update 2018. https://medium.com/

coinmonks/the-state-of-stablecoins-update-2018-56fb82efe6de.

Klages-Mundt, A., Harz, D., Gudgeon, L., Liu, J.-Y., and Minca, A. (2020). Stablecoins 2.0:
Economic Foundations and Risk-based Models. In Proceedings of the 2nd ACM Conference on
Advances in Financial Technologies, pages 59–79.

Klages-Mundt, A. and Minca, A. (2021). (In) Stability for the Blockchain: Deleveraging Spirals
and Stablecoin Attacks. Cryptoeconomic Systems, https: // arxiv. org/ abs/ 1906. 02152 .

Lipton, A., Hardjono, T., and Pentland, A. (2018). Digital trade coin: towards a more stable digital

currency. Royal Society open science, 5(7):180155.

Liquity (2020).

Stability pool

and liquidations.

https://docs.liquity.org/faq/

stability-pool-and-liquidations.

MakerDAO (12 Mar 2020a). Black Thursday response thread. https://forum.makerdao.com/t/

black-thursday-response-thread/1433.

MakerDAO (2017). The Dai stablecoin system whitepaper. https://makerdao.com/whitepaper/

DaiDec17WP.pdf.

MakerDAO (2019). The maker protocol: Makerdao’s multi-collateral dai (mcd) system. https:

//docs.makerdao.com/.

MakerDAO (Nov. 2020b). MIP29 - peg stability module. https://forum.makerdao.com/t/

mip29-peg-stability-module/5071.

Minca, A. and Wissel, J. (2020). Dynamic leveraging–deleveraging games. Operations Research,

68(1):93–114.

Morris, S. and Shin, H. S. (1998). Unique equilibrium in a model of self-fulﬁlling currency attacks.

American Economic Review, pages 587–597.

O’Hara, M. (1997). Market microstructure theory. Wiley.

28

Parlatore, C. (2016). Fragility in money market funds: Sponsor support and regulation. Journal

of Financial Economics, 121(3):595–623.

PeckShield (Feb. 2020a). bZx Hack Full Disclosure (With Detailed Proﬁt Analysis). https://

link.medium.com/LlXArFK7e7.

PeckShield (Feb. 2020b). bZx Hack II Full Disclosure (With Detailed Proﬁt Analysis). https:

//link.medium.com/9K9LrFQ7e7.

Platias, N. and DiMaggio, M. (2019). Terra money: stability stress test. Technical report, https:

//agora.terra.money/t/stability-stress-test/55.

Reﬂexer (2020). Rai. https://reflexer.finance/.

Rennison, J., Staﬀord, P., Smith, C., and Wigglesworth, R. (Mar. 23, 2020). ‘great liquidity crisis’

grips system as banks step back. Financial Times.

See, C.-T. and Chen, J. (2008). Inequalities on the variances of convex functions of random variables.

Journal of inequalities in pure and applied mathematics, 9(3):1–5.

Synthetix (16 Sep. 2019a). Addressing claims of deleted balances. https://blog.synthetix.io/

addressing-claims-of-deleted-balances/.

Synthetix (Jun. 2019b). Synthetix Response to Oracle Incident. https://blog.synthetix.io/

response-to-oracle-incident/.

Synthetix (Mar. 2020). tBTC: a decentralized redeemable BTC-backed ERC-20 token. https:

//docs.keep.network/tbtc.

Terra Research (Jul. 2019). Increasing Robustness of the Terra Oracle. https://agora.terra.

money/t/increasing-robustness-of-the-terra-oracle/82.

Topbottom, F. (2020). Black Thursday for MakerDAO: $8.32 million was liquidated for 0 DAI.

Werner, S. M., Perez, D., Gudgeon, L., Klages-Mundt, A., Harz, D., and Knottenbelt, W. J. (2021).

SoK: Decentralized Finance (DeFi). arXiv preprint arXiv:2101.08778.

Zamyatin, A., Harz, D., Lind, J., Panayiotou, P., Gervais, A., and Knottenbelt, W. J. (2019).
XCLAIM: Trustless, Interoperable, Cryptocurrency-Backed Assets. In Proceedings of the IEEE
Symposium on Security & Privacy, May 2019., pages 1254–1271.

29

A Proofs

In the proofs, we often use the following elementary result

Lemma 2. For α, D, L ≥ 0,

αD + L ≤

(cid:112)

α2D2 + 4αDL + L2 ≤ min

(cid:16)

2αD + L, αD + L +

√

(cid:17)

2αDL

.

√

√

Proof. Deﬁne ε :=
3 − 2), which
is true since α, D, L ≥ 0. Next, notice that ε = (cid:112)(αD + L)2 + 2αDL. Thus ε > αD + L since
√
2αDL ≥ 0. Lastly, by concavity, ε ≤ αD + L +

α2D2 + 4αDL + L2. We have ε ≤ 2αD + L as long as αD ≥ L(

2αDL.

Proposition 1
Proof. Consider Xt+1 = XtRt+1. For notational simplicity, drop subscripts as follows: ¯Nt (cid:55)→ N ,
Xt (cid:55)→ X, Lt (cid:55)→ L, ∆ = Lt − Lt−1, c(Lt) (cid:55)→ c, b(Lt) (cid:55)→ b, gt (cid:55)→ g, Rt+1 (cid:55)→ R. Deﬁne ψ := E[Yt+1|Ft].
Then

ψ(L) =

∆ · D
L

E[R|Ft] +

(cid:90) ∞

c/X

(N Xz − L)g(z)dz +

(cid:90) b/X

(cid:18)

3L −

c/X

αDL
2N Xz − L

(cid:19)

− 2N Xz

g(z)dz.

Recall that the integrand factor
evaluated at Xz = c is L − N c (the
2N Xz−L − 2N Xz
liquidation zeros out the speculator’s collateral position), and evaluated at Xz = b is 0 (on the
threshold of liquidation).

3L − αDL

(cid:16)

(cid:17)

We obtain

∂ψ
∂L

=

DLt−1
L2

E[R|Ft] −

(cid:16)

N X

c
X

(cid:17)

g

− L

(cid:16) c
X

(cid:17) ∂c
∂L

1
X

−

(cid:90) ∞

c
X

g(z)dz

(cid:16)

−

L − N X

(cid:17)

g

c
X

(cid:16) c
X

(cid:17) ∂c
∂L

1
X

+

(cid:90) b
X

(cid:18)

3 −

αDN Xz
2(N Xz − L)2

(cid:19)

g(z)dz

=

DLt−1
L2

E[R|Ft] −

(cid:90) ∞

c
X

g(z)dz +

(cid:18)

3 −

αDN Xz
2(N Xz − L)2

(cid:19)

g(z)dz

c
X
(cid:90) b
X

c
X

∂2ψ
∂L2 = −

2DLt−1
L3

E[R|Ft] + g

(cid:18) b
X

(cid:19) ∂b
∂L

1
X

(cid:18)

3 −

αDN b
2(N b − L)2

(cid:19)

− g

(cid:16) c
X

(cid:17) ∂c
∂L

1
X

(cid:18)

2 −

αDN c
2(N c − L)2

(cid:19)

−

(cid:90) b
X

c
X

αDN Xz
(N Xz − L)3 g(z)dz.

Notice that ∂b

∂L > 0, ∂c

∂L > 0, g ≥ 0, and
αDN b

3 −

2(N b − L)2 = 3 −

αDβL

2(L(β − 1))2 = 3 −

3αD
L

< 0

by assumption that liquidation repurchase price always ≥ 1. Additionally, the remaining integral
is always positive as the integrand is positive between the limits and g ≥ 0. Finally, E[R|Ft] ≥ 0
since (Xt) is a submartingale. Thus under the given conditions, ∂2ψ

∂L2 ≤ 0 as all terms are ≤ 0.

(cid:16)

c(L) < XR < b(L)

(cid:17)

= (cid:82) b/X

c/X g(z)dz > 0, then

Further supposing that either E[R|Ft] > 0 or P

∂2ψ
∂L2 < 0.

30

Notice that the 1

2 in the bound is related to the choice β = 3
2 .

Proposition 2

Proof. Easily veriﬁable by substitution, noting that factors of γ cancel in the integral limits.

Proposition 3

Proof. The speculator can at most buy back using all its ETH. At time t, this amount is the solution
∆t to the following

∆tD
Lt−1 + ∆t

+ Nt−1Xt − Lt−1 − ∆t = 0,

supposing there is no liquidation at time t. It is straightforward to verify the solution, giving the
lower bound:

∆t ≥

(cid:113)

(cid:16)

1
2

−

D2 − 4DLt−1 + 2DNt−1Xt + N 2

t−1X 2

t + D − 2Lt−1 + Nt−1Xt

(cid:17)

.

Note that if the speculator is not solvable at time t, then there is no real solution.

Proposition 4

Proof. As above, consider Xt+1 = XtRt+1. For notational simplicity, we drop subscripts as follows:
¯Nt
(cid:55)→ g, Rt+1 (cid:55)→ R,
P(At|Ft) (cid:55)→ P(A), P(Bt|Ft) (cid:55)→ P(B).

(cid:55)→ L, ∆ = Lt − Lt−1, c(Lt) (cid:55)→ c, b(Lt) (cid:55)→ b, gt

(cid:55)→ N , Xt

(cid:55)→ X, Lt

Suppose the ﬁrst condition is true. We have

∂ψ
∂L

=

≤

≤

DLt−1
L2

DLt−1
L2
DLt−1
L2

E[R|Ft] −

(cid:90) ∞

c
X

g(z)dz +

(cid:90) b
X

c
X

(cid:18)

3 −

αDN Xz
2(N Xz − L)2

(cid:19)

g(z)dz

E[R|Ft] − P(A ∪ B)

E[R|Ft] − κ−1.

Notice this is monotonic decreasing in L over the domain, so the critical point will be a bound for
the optimal value of L∗. Setting equal to 0, we have

Now suppose the second condition is true instead. We have

L∗ ≤ (cid:112)κDLt−1 E[R|Ft].

g(z)dz −

(cid:90) b
X

c
X

αDN Xz

2(N Xz − L)2 g(z)dz

∂ψ
∂L

=

≤

≤

DLt−1
L2

DLt−1
L2
DLt−1
L2

E[R|Ft] −

(cid:90) ∞

b
X

g(z)dz + 2

E[R|Ft] −

(cid:16)

P(A) − 2 P(B)

(cid:90) b
X

c
X
(cid:17)

E[R|Ft] − κ−1.

which delivers the desired result as above.

31

Proposition 5
Proof. By assuming TZ0 > τ , we have Z0 ≥ Zt∧τ . Applying Proposition 4 to Zt = D
Lt
Zt∧τ ≥
respectively as increasing and decreasing sequences in t starting from initial state as follows:

κLt∧τ −1r . Notice that the upper bound on Lt and the lower bound on Zt can be written

(cid:113) D

provides

Lt = (κDr)

2t−1
2t L

1
2t
0 .

Zt =

D
2t−1
2t L

(κDr)

.

1
2t
0

These have limits L∞ = κDr and Z∞ = 1

κr that also bound Lt and Zt respectively.

Proposition 6

Proof. For t − 1 < τ ,

D
E[Lt|Ft−1]

≤ E

(cid:20) D
Lt

(cid:21)

|Ft−1

≤

D
Lt−1

by Jensen’s inequality and the condition for τ > t − 1. Thus we have

E[Lt∧τ |Ft−1] ≥ Lt∧τ −1

and (Lt∧τ ) is a submartingale. (Zt∧τ ) is a supermartingale by condition of τ .

Applying Proposition 5, Lt∧τ is bounded above and Zt∧τ is bounded below. Thus they converge

almost surely by Doob’s martingale convergence theorem.

Proposition 7

Proof. The ﬁrst inequality follows from Proposition 5 and supermartingale properties.

Since Zt∧τ is supermartingale, we have Zt−1 ≥ E[Zt|Ft−1]. Assume (E[Rt+1|Ft]) is non-

decreasing for t < τ . Then subject to the stopping time τ ,

(cid:34)(cid:115)

E[Zt|Ft−1] ≥ E

D
κLt−1 E[Rt+1|Ft]

|Ft−1

(cid:118)
(cid:117)
(cid:117)
(cid:116)

(cid:115)

(cid:115)

≥

=

≥

D

(cid:104)

κLt−1 E

E[Rt+1|Ft]|Ft−1

D
κLt−1 E[Rt+1|Ft−1]

D
κLt−1 E[Rt|Ft−1]

(cid:35)

(cid:105)

(Apply Proposition 4)

(Jensen’s inequality)

(Tower property)

since E[Rt+1|Ft] ≥ E[Rt|Ft−1].

32

Lemma 1

Proof. For t − 1 < τ ∧ Tm,

E [|m − Zt||Ft−1] ≥ | E[m − Zt|Ft−1]|

≥ |m − Zt−1|,

by Jensen’s inequality and the condition for t − 1 < Tm that m − Zt−1 ≥ 0. Thus (cid:0)Z(cid:48)
non-negative submartingale.

t∧τ ∧Tm

(cid:1) is a

Proposition 8

Proof. Note for t < τ ∧ Tm, have Z∗
1
κr , Z(cid:48)

τ ∧Tm

(cid:17)

.

t ≤ m, and so Z(cid:48)∗

τ ∧Tm−1 ≤ m − 1

κr . Thus Z(cid:48)∗

τ ∧Tm

≤ max

(cid:16)

m −

Consider time t = τ ∧ Tm and note that optional stopping applies since Z is bounded. Denote
W := m − Zt, E := E[−W |Zt > m], and p := P(Zt ≤ m). From optional stopping, we recall that
m ≥ E[Zt] ≥ 1

κr , and so 0 ≤ E[W ] ≤ m − 1

κr . Then

E[W ] = E[W 1Zt≤m] − E[−W 1Zt>m]
1
κr

− (1 − p)E.

m −

≤ p

(cid:18)

(cid:19)

Combining with 0 ≤ E[W ], we have 0 ≤ p(m − 1

κr ) − (1 − p)E, which gives

p ≥

E
m − 1
κr + E

.

E
m− 1
κr +E

), p ≤ 1, and E[Z(cid:48)

t] = E[W 1Zt≤m] + E[−W 1Zt>m],

Then noting that (1 − p)E ≤ E(1 −

we have

E[Z(cid:48)∗

t ] ≤ p E[Z(cid:48)∗
1
κr

≤ m −

t−1] + (1 − p)E
(cid:32)

+ E

1 −

E
m − 1
κr + E

(cid:33)

κr )
κr + E
Notice further that given either of the following conditions

E(m − 1
m − 1

= m −

1
κr

+

.

κr − m

• 1

• 1

κr > m and E > 1
κr = m and E > 0
κr < m ad E ≥ 0,

• 1

then

0 ≤ (1 − p)E ≤

E(m − 1
m − 1

κr )
κr + E

≤ m −

1
κr

.

Thus, recalling we used t = τ ∧ Tm, we get the following result

E[Z(cid:48)∗

τ ∧Tm] ≤ 2

(cid:18)

m −

(cid:19)

.

1
κr

33

Theorem 1
Proof. Given Lemma 1 and Proposition 8 and noting E[Z(cid:48)
inequality.

τ ∧Tm

] ≤ E[Z(cid:48)∗

τ ∧Tm

], apply Doob’s maximal

Theorem 2

Proof. Apply Theorem 3.1 in Burkholder [1973], noting that supn
Jensen’s inequality.

E[Z(cid:48)

n∧τ ∧Tm

] ≤ E[Z(cid:48)∗

τ ∧Tm

] by

Theorem 3

Proof. For S1 ≤ t < S2, we have

E

(cid:20) D
Lt

(cid:21)

|Ft−1

≥

≥

D
E[Lt|Ft−1]
D
Lt−1

by Jensen’s inequality and the S1 condition E[Lt|Ft−1] ≤ Lt−1. Thus (ZS1∨t∧S2) is a submartingale
(though note that it can be a submartingale for more general stopping times than this).

L started at S1 and stopped S2 is a supermartingale (by deﬁnition).

Theorem 4

Proof. As above, consider Xt+1 = XtRt+1. For notational simplicity, we drop subscripts as follows:
¯Nt (cid:55)→ N , Xt−1 (cid:55)→ X (notice this is diﬀerent from previous usage), Lt (cid:55)→ L, ∆ = Lt − Lt−1,
c(Lt) (cid:55)→ c, b(Lt) (cid:55)→ b, and gt (cid:55)→ g.

Let ρ be (deterministic) variable representing the outcome of Rt, such that now we have the
outcome Xt = Xρ. And deﬁne h(ρ) = arg maxL ψ(ρ, L) = E[Yt+1|Ft]. By ﬁrst order condition,
∂
∂L ψ(ρ, h(ρ)) = 0. The assumptions on ψ provide unique maximum and fulﬁll conditions of the
implicit function theorem, which gives us ∂h
∂ρ (ρ) exists and

∂h
∂ρ

(ρ) = −

∂2
∂ρ∂L ψ(ρ, h(ρ))
∂2
∂L2 ψ(ρ, h(ρ))

.

Calculating derivatives using the Leibniz integral rule (recalling c, b are functions of L),

∂2ψ
∂ρ∂L

= g

(cid:19) c

Xρ2

(cid:18)

4 −

αDN c
2(N c − L)2

(cid:19)

− g

(cid:18) b
Xρ

(cid:19) b

Xρ2

(cid:18)

3 −

αDN b
2(N b − L)2

(cid:19)

(cid:18) c
Xρ
(cid:90) b
Xρ

+

c
Xρ

αDN Xz(N Xρz + L)
2(N Xρz − L)3

g(z)dz.

34

∂2ψ
∂L2 = −

2DLt−1 E[Rt+1]
L3
(cid:19) ∂c
∂L

(cid:18) c
Xρ

1
Xρ

− g

+ g

(cid:18) b
Xρ

(cid:19) ∂b
∂L

1
Xρ

(cid:18)

3 −

αDN b
2(N b − L)2

(cid:19)

(cid:18)

2 −

αDN c
2(N c − L)2

(cid:19)

−

(cid:90) b
Xρ

c
Xρ

αDN Xρz
(N Xρz − L)3 g(z)dz.

Notice that (and continuing with β = 3/2)

3 −

αDN b

2(N b − L)2 = 3 −

αDβL

2(L(β − 1))2 = 3 −

3αD
L

< 0,

by assumption that liquidation repurchase price always ≥ 1. And

αDN c
2(N c − L)2 ≤

1
2 αD(2αD + L − αD + L)
−2αD(2αD + L) + 2L(αD + L) + 2α2D2 + 2αDL + 2L2

=

=

≤

αD(αD + 2L)
4(αD + L)(2L − αD)

+

αD
3(2L − αD)

αD
12(αD + L)
1
12

+

αD
3(2L − αD)

.

This is ≤ 2 when L ≥ 27

46 αD. Thus under this condition

4 −

αDN c

2(N c − L)2 > 2 −

αDN c

2(N c − L)2 ≥ 0.

∂ρ∂L are non-negative and all terms of ∂2ψ
Note that all terms of ∂2ψ
(cid:16) b
(cid:16) c
Xρ
Xρ

∂L2 are non-positive. Given ρ ≥
∂L , and 2DLt−1 E[Rt+1]
b/X, we have g
are constant in ρ. Lastly, the numerator and denominator integrals can be rewritten respectively
as

are increasing in 1/ρ. Note also that ∂b

∂L , ∂c

and g

L3

(cid:17)

(cid:17)

1
ρ

(cid:90) b

c

αDN z(N z + L)
2(N z − L)3

g

(cid:19)

(cid:18) z
Xρ

dz and

(cid:90) b

c

αDN z
(N z − L)3 g

(cid:19)

(cid:18) z
Xρ

dz

2(N z−L)3 ≥ αDN z

and αDN z(N z+L)
(N z−L)3 given N z + L ≥ N c + L > 2, for which L > 8 is suﬃcient. And
so the terms in the numerator of |h(cid:48)(ρ)| are growing by a factor 1/ρ faster than the terms in the
denominator as ρ decreases, proving (2).

Next, note that under the condition 0 < ρ < 1,

b
Xρ2 =

βL
N Xρ2 =

db
dL

L
Xρ2 ≥

db
dL

1
Xρ

The last relation uses the fact that dc

Next note that for ρ ≤ L

1
Xρ2 ≥

c
dc
Xρ2 ≥
dL
dL ≤ 2αD+L
8 and c ≤ Xρz ≤ b, we have

dc
dL
2(αD+L) + 1 < 2, and so c > dc

1
Xρ

.

dL under the problem setup.

αDN Xz(N Xρz + L)
2(N Xρz − L)3

≥

αDN Xρz
(N Xρz − L)3 .

35

This is because the expression (1) simpliﬁes to N Xρz + L ≥ 2ρ, (2) to be true over the whole range
of z, we need N c + L ≥ 2ρ, and (3) ρ ≤ L

8 is suﬃcient for this. Thus

(cid:90) b
Xρ

c
Xρ

αDN Xz(N Xρz + L)
2(N Xρz − L)3

g(z)dz ≥

(cid:90) b
Xρ

c
Xρ

αDN Xρz
(N Xρz − L)3 g(z)dz

under these conditions.

Then note that all terms in the numerator of h(cid:48)(ρ) are greater than and grow faster in 1/ρ than
the comparable terms in the denominator. This leaves the ﬁrst term in the numerator, which is
constant in ρ. To get (3), then note that ε can be chosen such that for ρ = ε, the numerator and
denominator are equal.

We can derive the results for ∂h

∂n in essentially the same way. Alter the above dropping of
subscripts with Xt (cid:55)→ X, let n be a variable representing the realization of ¯Nt, and consider h as a
function of n. Note the following relevant derivatives.

∂b
∂n

= −

βL
n2 = −

b
n

∂c
∂n

= −

1
2n2

(cid:16)(cid:112)

α2D2 + 4αDL + L2 − αD + L

(cid:17)

= −

c
n

∂2ψ
∂n∂L

= g

(cid:18)

2 −

αDnc
2(nc − L)2

(cid:19)

− g

(cid:18) b
X

(cid:19) b
n

(cid:18)

3 −

αDnb
2(nb − L)2

(cid:19)

(cid:17) c
n

(cid:16) c
X
(cid:90) b
X

+

c
X

αDnXz(nXz + L)
2(nXz − L)3

g(z)dz.

And translating the following to the new notation

∂2ψ
∂L2 = −

2DLt−1 E[Rt+1]
L3

+ g

(cid:18) b
X

(cid:19) ∂b
∂L

− g

(cid:16) c
X

(cid:17) ∂c
∂L

1
X

(cid:18)

2 −

αDnc
2(nc − L)2

1
X
(cid:19)

(cid:18)

3 −

(cid:19)

αDnb
2(nb − L)2

−

(cid:90) b
X

c
X

αDnXz
(nXz − L)3 g(z)dz.

And by applying implicit function theorem, we get

∂h
∂n

(n) = −

∂2
∂n∂L ψ(n, h(n))
∂2
∂L2 ψ(n, h(n))

.

From here we can proceed with the same analysis using factors of 1

n instead of 1
ρ .

Theorem 5
Proof. For notational simplicity, drop subscripts Xt (cid:55)→ X, ¯Nt−1 (cid:55)→ N , Lt−1 (cid:55)→ L. And consider x
a realization of X as variable in h. Deﬁne the function f (X, n) = 1
h(X,n) where n represents the
realization of N . With probability 1, the following are true:

• h is concave in x and n because h(cid:48) is decreasing, as shown in the previous result.

36

• f is diﬀerentiable (wrt n and x) over domain using chain rule and implicit function theorem.

• f is convex: it’s the composition of 1/x and h, and since 1/x is convex and non-increasing

and h is concave, so is f (see Boyd and Vandenberghe [2009] 3.2.4).

• f is (strictly) decreasing (in n and x) since h is increasing.

• By assumption, we’ve restricted N X. The derivative of f at the minimum value exists and

is bounded.

• f is non-negative since h is non-negative.

• ∂f

∂n is (strictly) increasing in n. We have

f (cid:48)(x, n) = −

1

h(x, n)2 h(cid:48)(x, n),

where h(cid:48)(x, n) is derived in the previous proof using the implicit function theorem. h is
increasing in n and h(cid:48) is non-negative and decreasing in n. Thus h(cid:48)
h2 is decreasing in n, and
so − h(cid:48)

h2 is increasing.

• ∂h

∂n is increasing in x. This can be seen using the formulation at the end of the proof for
the previous result as terms in ∂2ψ
∂L2 grow slower in x (in magnitude) than terms in ∂2ψ
∂n∂L . In
particular, the ﬁrst term of ∂2ψ
∂L2 is decreasing in magnitude since L is increasing in x. And the
integral in ∂2ψ
∂L2 , as can be seen by comparing
the integrand numerators (a factor of x2 in ∂2ψ

∂n∂L increases faster in x than the integral in ∂2ψ

∂n∂L vs. a factor of x in ∂2ψ
∂L2 ).
∂n is (strictly) increasing in x This is because h is increasing in x and ∂h
increasing in x (previous bullet).

∂n is non-negative and

• ∂f

Note additionally that, from the system setup assumptions, all of the functions are appropriately

bounded.

Thus we can apply Theorem 3.1 in See and Chen [2008] to get

(cid:16)

Var

f (X, N s)|Ft−1

(cid:17)

(cid:16)

< Var

f (X, N u)|Ft−1

(cid:17)

.

Note that the variances exist because h = Lt is bounded, as shown in previous results. The
variances of Zs

t are then obtained by multiplying the above inequality by D2.

t and Zu

37

