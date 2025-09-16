2
2
0
2

c
e
D
3
2

]

R
C
.
s
c
[

1
v
8
9
3
2
1
.
2
1
2
2
:
v
i
X
r
a

Designing Autonomous Markets for Stablecoin
Monetary Policy∗

Ariah Klages-Mundt†

Steﬀen Schuldenzucker‡

December 2022

Abstract

We develop a new type of automated market maker (AMM) that helps to
maintain stability and long-term viability in a stablecoin. This primary market
AMM (P-AMM) is an autonomous mechanism for pricing minting and redemption
of stablecoins in all possible states and is designed to achieve several desirable
properties. We ﬁrst cover several case studies of current ad hoc stablecoin
issuance and redemption mechanisms, several of which have contributed to recent
stablecoin de-peggings, and formulate desirable properties of a P-AMM that
support stability and usability. We then design a P-AMM redemption curve and
show that it satisﬁes these properties, including bounded loss for both the protocol
and stablecoin holders. We further show that this redemption curve is path
independent and has properties of path deﬁciency in extended settings involving
trading fees and a separate minting curve. This means that system health weakly
improves relative to the path independent setting along any trading curve and
that there is no incentive to strategically subdivide redemptions. Finally, we
show how to implement the P-AMM eﬃciently on-chain.

1

Introduction

The design of non-custodial stablecoins has faced several recent turning points, both
in the Black Thursday crisis in Dai and the recent churn of algorithmic stablecoins.
These have both pointed toward the importance of designing good primary markets
for stablecoins —i.e., mechanisms for pricing minting and redeeming of stablecoins.
The terminology here is borrowed from ETF market structure and contrasts “primary
market”, where shares of a fund are minted and redeemed for underlying assets, and
“secondary market”, where existing shares are traded for other assets (and where
ordinary exchange trading takes place). A primary market for a stablecoin helps to
maintain peg by allowing users to exchange stablecoins with the protocol near the
peg price, providing a means to arbitrage other markets back toward the peg value,

∗The design from this paper is implemented as part of the upcoming Gyroscope stablecoin system
under the name Dynamic Stability Mechanism (DSM). The source code will be made available later.
†Researcher at Superluminal Labs; in a separate capacity, a PhD student at Cornell University.
‡Researcher at Superluminal Labs

1

should they deviate. In a blockchain protocol, primary markets are automated; we
call the mechanism that controls mint and redeem prices the primary algorithmic
market maker (P-AMM) of the stablecoin. Every stablecoin design has a P-AMM, be
it intentionally designed or not.

Black Thursday in March 2020 saw a ∼ 50% crash in ETH in the day. This
triggered a deleveraging spiral, a short squeeze eﬀect that causes the price of Dai to
increase as borrowers need to buy it to reduce exposure. This was shown to amplify
collateral and liquidity drawdown and cause instability in Dai Klages-Mundt and
Minca (2021, 2022). This demonstrated fundamental problems around deleveraging,
liquidity, and scaling in stablecoins like Dai, in which supply depends on an underlying
market for leverage as opposed to a primary market.1

PSM: a primary market for Dai. Patching the deleveraging problem has been
a major topic since Black Thursday. Several approaches have been pursued, the most
prominent of which is the tethering of Dai to the custodial stablecoin USDC.2 This
takes the form of Maker’s peg stability module (PSM), which maintains exchangeability
of Dai with USDC via a protocol-held USDC reserve. The PSM in this way eﬀectively
becomes a primary market for minting and redeeming Dai, backed by USDC reserves.
The PSM has greatly enhanced the liquidity around Dai’s peg and its resilience to
deleveraging spirals, as evidenced in Figure 1a, which plots Dai price for days t since
the major ETH shocks of 12 March 2020 (w/o PSM) and 19 May 2021 (w/ PSM).
However, this has further exposed the scaling problem of the original Dai mechanism:
the leverage market doesn’t necessarily scale with demand. Since the May 2021
crisis, Dai backed by USDC has grown from 17% to now over 60% of the Dai supply
(Figure 1b). This arguably compromises the decentralization of Dai by importing the
custodial and regulatory risks of USDC.

Algorithmic Stablecoins. The problems with Dai, including its most recent USDC
centralization issue, has also motivated a wave of algorithmic stablecoins, which aim
to keep the stablecoin supply in line with demand algorithmically. Mostly, these
designs have either no or dubious degrees of asset backing. These designs have almost
universally experienced depegging events, as depicted in Figure 2 due to susceptibility
to downwards spirals arising from the lack of asset backing and ad hoc primary market
structure when under-reserved.

Algorithmic stablecoins are best understood in the context of currency peg models,
such as Morris and Shin (1998). In a simpliﬁed sense, these systems are backed by two
sources of value: (i) asset backing in a currency reserve and (ii) economic usage, an
intangible value that represents the demand to hold the currency as it unlocks access

1In this market, a speculator can post collateral and borrow Dai against this collateral to achieve
a risky leveraged position. As a result, the supply of Dai will depend on the demand for leverage,
which can and does plummet in a crisis.

2Two other notable approaches are using negative rates to equilibrate supply and demand at
the target (e.g., Rai) and using dedicated liquidity pools to smooth the eﬀects of deleveraging (e.g.,
Liquity and the solution proposed in Klages-Mundt and Minca (2022)). The former leads to questions
of liquidity and equilibrium participation under negative rate regimes, and the latter is not a full ﬁx
as it smooths but postpones spirals.

2

Figure 1 Eﬀects of the Dai PSM. (a) Dai price for days t since major ETH shocks
w/ and w/o the PSM, (b) The portion of Dai issued through the PSM has grown
> 3× since the May 2021 ETH shock.

(a)

(b)

Figure 2 The recent churn of algorithmic stablecoins.

3

Days since ETH Crash$0.90$0.95$1.00$1.05$1.101815129630-3-6-9-12-15-18DAI w/o PSMDAI w PSM% of Dai from PSMto an underlying economy. Supposing these two values are together great enough, a
currency peg is maintainable; otherwise, it is susceptible to breaking. A peg break
can also be triggered by a speculative attack that is proﬁtable for the attacker, akin
to the attack on the British pound on Black Wednesday.

Algorithmic stablecoins have encountered several fundamental problems, which
contribute challenges to primary market design. Many are under-reserved by design
while having no native economic usage, leading to many observed depeggings through
downwards spirals, often exhausting the asset backing. Further, the composition of
reserve assets that can be held on-chain are inherently risky. In some cases, these
assets are non-existent (e.g., Basis). In seigniorage shares–style designs (e.g., Terra
and Iron), the backing is eﬀectively the value of “equity shares”, which have an
endogenous/circular price with the expected growth of the system and can spiral
to zero Klages-Mundt et al. (2020). A better equipped limit case is a stablecoin
backed fully by a portfolio of exogenous, but risky and possibly illiquid, assets, which
could enter an under-reserve state if assets experience shocks. Any design that could
experience under-reserved states requires a good policy for how the protocol applies
reserve assets to maintain liquidity near the peg in sustainable ways, factoring in the
state of reserve backing. This challenge eﬀectively becomes the problem of designing
a primary market for the stablecoin.

1.1 This Paper

In this paper, we study the rigorous design of stablecoin primary markets with
these desirable properties. In particular, a well-designed curve will be able to adapt
shape/pricing autonomously to achieve these properties. Such a formulation will
require minimal intervention by governance, further limiting risks from governance
extractable value Lee and Klages-Mundt (Apr. 23, 2021). We make the following
contributions.

• We introduce our analysis framework of the redemption curve of a stablecoin
and conduct a case study of diﬀerent existing P-AMM designs (Section 2).

• We formulate the P-AMM desiderata (Section 3).

• We design a new P-AMM redemption curve implicitly (Section 4). The design
is parameterized by a virtual anchor point that captures system health and
redemption pressure. We specify the curve explicitly as a function of the anchor
point (Section 5) and we show that the anchor point is uniquely determined by
the current system state (Section 6), implying that the overall design is well-
deﬁned. We also establish that the shape of the redemption curve satisﬁes several
of our desiderata directly. Furthermore, we formulate a simpler redemption
curve that satisﬁes many, but not all, desiderata (Section 4.2 and Appendix B).

• We show that our P-AMM redemption curve is path independent and we prove
several path deﬁciency properties in an extended setting with trading fees and
minting. In particular, we show that system health weakly improves relative to
the path independent setting along any trading curve and there is no incentive

4

to strategically subdivide redemptions (Section 7).

• Finally we show that our P-AMM can be implemented eﬃciently on-chain.
Speciﬁcally, the implementation only requires a constant number of basic arith-
metic operations and at most two square roots to evaluate. The implementation
makes use of additional structural results (Section 8).

The result of this paper is an autonomously adapting P-AMM that satisﬁes the
desired properties throughout the possible state space. The P-AMM formulation
contains a few select hyperparameters, which can in principle be tuned by governance;
however, the desired properties stand over the entire parameter space. In particular,
if parameters are tuned, it does not need to happen on-the-ﬂy, thus still minimizing
reliance on governance intervention.

Note that the stablecoin peg target is implicitly $1. However, the mechanics remain
fully functional under any arbitrary target within a block. Through adapting this
implicit parameter, the system could also implement much more arbitrary monetary
policy while retaining desirable properties.

We make two important, but not contentious, assumptions in this work. First,
we exclude endogenous/circularly priced collateral by assuming that reserve assets
are exogenously priced. Second, we assume that the system has an accurate oracle
that provides the price of reserve assets in USD. The need for an oracle is inescapable
in a stablecoin that pegs to outside assets, so this is not an unusual assumption.
Since oracles can provide manipulation surfaces (see, e.g., Werner et al. (2021)), it is
important to incorporate other protective mechanisms; however, these are separate
from the P-AMM mechanism itself.

1.2 Primary Markets: Related Work

Our work is most closely related to currency peg models in international economics
(e.g., Morris and Shin (1998); Guimaraes and Morris (2007)) as well as models of
pegged money market mutual funds (e.g., Parlatore (2016)). Although these types of
models have been discussed and adapted recently in the context of stablecoins (e.g.,
Routledge and Zetlin-Jones (2021); Li et al. (2020)), there is no prior work building a
cryptocurrency mechanism that can adapt the lessons of good currency peg policies.
Our work constructs such a mechanism from ﬁrst principles that functions in a novel
way as an autonomous primary market for stablecoin issuance. For further academic
background on stablecoins, we refer to Klages-Mundt et al. (2020); Bullmann et al.
(2019); Pernice et al. (2019) and references therein.

For an overview of theory work on AMMs, we refer to Angeris and Chitra (2020);
Angeris et al. (2020); Capponi and Jia (2021). Further background and references
are available in Werner et al. (2021). Current AMMs resemble Uniswap Adams et al.
(2021) and Curve Egorov (2019), in which liquidity providers add pairs of assets to a
pool that quotes trading prices algorithmically depending on the state of the pool.
Such AMMs are secondary markets in which assets that already exist are traded. In
contrast, we develop a new type of AMM that plays the role of a primary market, in
which assets are minted and redeemed against the protocol itself. No existing work

5

Figure 3 Stylized primary market redemption curves.

(a)

(b)

analyzes such constructions for stablecoins.

A well-designed primary market for a stablecoin can be interpreted as an au-
tonomous version of open market operations, comparing with how central banks
interact with markets to shape monetary policy. See Appendix A for further dis-
cussion on this comparison. Designing an algorithmic primary market presents a
challenge akin to designing a rules-based monetary policy (i.e., a Taylor Rule; see,
e.g., Orphanides (2010)). However, rather than setting nominal interest rates in a
quasi-algorithmic way, as in normal central bank monetary policy, an algorithmic
primary market is setting prices in a programmatic way.

2 Primary Markets: Case Studies

In contrasting the shapes of primary market mechanisms, it will be useful to interpret
these as automated market makers (AMMs), which price the exchange of assets
algorithmically along a curve as a function of reserves and possibly other state
variables.3 Sometimes these are explicit AMM curves implemented by the protocol,
while other times we must factor in the eﬀects of several mechanisms to ﬁnd an
implicit AMM curve that describes the primary market. This AMM structure will
depend on the assets backing the system. In some cases, these assets are implicitly
backing the system, such as in seigniorage shares systems. Other times, they are a
portfolio of assets more explicitly. We will refer to this asset backing as the reserve
assets.

A primary market can be separated into two curves (possibly coinciding): a
minting curve and a redemption curve. These curves price the stablecoin in terms
of underlying reserve assets as a function of system state (e.g., level of redemptions
and reserve health). To illustrate, Figure 3a shows some stylized possible redemption
curves, plotted as a function of redemption level. An advanced redemption curve
might shift the curvature of the 2-d curve as other variables in the state change (e.g.,

3For recent background on AMMs, see Angeris and Chitra (2020), which focuses on constant
function market makers (CFMMs). However, primary markets will not ﬁt this category in general.

6

PriceRedemption LevelAll liquidity at $1Higher curvaturePriceRedemption LevelAll liquidity at $1……until liquidity is exhaustedFigure 4 Fei case study. (a) implicit redemption curve shape w/ and w/o direct
incentives. (b) depegging following large redemptions at launch.

(a)

(b)

reserve health). Note that, should the reserve assets backing the system be exhausted,
the redemption curve becomes ﬂat at $0, as depicted in Figure 3b.

USDC/USDT. Custodial stablecoins like USDC and USDT have ﬂat redemption
curves at ∼ $1. Note that this primary market has a large oﬀ-chain component, where
dollars are actually exchanged for stablecoins. Because of this oﬀ-chain component,
users must trust the issuer to maintain the primary market. There are various reasons
why this may not happen or may not be possible, including custodial and regulatory
risks as well as potential loss on risky reserve assets. Note that Dai’s PSM discussed
above essentially borrows USDC’s primary market by wrapping USDC, and so the
PSM redemption curve is similar.

In Basis-type designs, including Basis Cash and Empty Set Dollar, there is
Basis.
an implicit redemption curve for “coupons”, which promise to be redeemable for a
multiple of new stablecoins later. Often, these coupons also expire a certain time
after creation. However, since there is no asset backing of the system (all income
from selling newly minted stablecoins is disbursed to various stakeholders), there is
no redemption available for exogenous assets. In the event that stablecoin demand
and willingness to speculate on growth of the system deteriorates, the value of these
coupons circularly goes to zero, and the redemption curve becomes ﬂat at $0. As
seen in Figure 2, these systems did not maintain a peg both because of this solely
circular value structure and the lack of a supporting primary market mechanism.

Fei. The Fei stablecoin places reserve assets in a constant-product AMM pool. The
action akin to redemption is to sell Fei for ETH in this pool. At launch, this pool was
designed with a fee that grows quadratically in the amount of redemptions (“direct
incentives”). This has the eﬀect of distorting the implicit Fei redemption curve
into a poor shape (see Figure 4a) that essentially guarantees low primary market
liquidity during a supply contraction, leaving Fei holders entrapped once secondary

7

 $- $0.20 $0.40 $0.60 $0.80 $1.000%5%10%15%20%25%30%Redeem QuoteRedemption level (% of supply)Implicit Fei Redemption Curve, Reserve Ratio = 100%w/ Direct Incentivesw/o Direct Incentivesmarket liquidity dries up, even under good reserve health. Following the Fei launch
in Apricl 2021 and despite an eﬀectively high reserve ratio, the implicit redemption
curve was unable to handle the size of sought redemptions, leading the stablecoin to
deviate erratically from the peg (see Figure 4b).4

UST / Seigniorage Shares. The TerraUSD (UST) stablecoin was intended to be
backed by a seigniorage shares-style token, LUNA. UST was redeemable for newly
minted LUNA, inﬂating the supply of the latter. The redemption curve was intended
to be ﬂat at $1. However, since LUNA was an endogenous/circularly priced asset,
there was no guarantee that speculators’ demand would be enough to support its
UST backing. In Feb. 2022, a partial backing of Bitcoin was added. Despite this, in
May 2022, a downwards spiral was triggered, in which UST saw mass redemptions,
the Bitcoin reserve was exhausted, and the value of LUNA went to zero, removing
essentially all support from UST and allowing it to crash to mere cents on the dollar
(see Figure 5). This is a variation on the stylized redemption curve in Figure 3b.

3 Desiderata for P-AMM Design

A major missing piece in the current space is the rigorous design of stablecoin primary
markets developed from ﬁrst principles. As we’ve seen in the previous case studies,
the primary market design plays a large role in the stability of these systems. Up
until this paper, it is not well-speciﬁed what the desirable properties are in designing
these primary markets. We ﬁrst tackle this issue before continuing on the design of
our primary market automated market maker (P-AMM) redemption curves in the
remainder of this paper.

We strive for several desiderata in the design of a primary market mechanism that
has good properties from stability and usability perspectives. We separate these into
properties of the P-AMM within a block and more general properties.

Within a block, the following properties are desirable.

1. The relative collateralization (i.e., reserve ratio) of the protocol is guaranteed
to stay above a lower bound (unless this is impossible because of an exogenous
shock to reserve assets).

2. The P-AMM normally maintains a region of open market operations in which

the stablecoin price is ∼ $1.

3. The worst-case P-AMM redemption rate is lower bounded.

4. The P-AMM redemption curve is continuous and not too steep, unless this

would violate the other desiderata.

5. There is no incentive for redeemers to strategically subdivide redemptions.

4The direct incentive mechanism was later removed, shifting the implicit redemption curve to the
constant product curve visualized in Figure 4a. Later, Fei governance chose to forgo this implicit
redemption curve by oﬀering direct redemptions at $0.95.

8

Figure 5 UST case study. (a) following a downwards spiral, UST price near $0. (b)
LUNA price going to zero at the same time.

(a)

(b)

9

These desiderata are informed by results about currency peg models, in which
the shape of optimal monetary policies involve peg support up to a threshold and
reserve preservation past that. The ﬁrst property means that the loss for the protocol
is bounded, as the reserve is never exhausted in the operation of the P-AMM unless
all reserve asset prices exogenously go to zero. The second property means that the
stablecoin can support a possible equilibrium price at the dollar target. The third
property means that the loss for stablecoin holders who redeem is bounded.

The fourth property reduces risk for traders and incentives for potential speculative
attacks. Supposing the peg is not maintainable, the system can’t know what the
equilibrium price of the stablecoin will be. It only knows upper and lower bounds on
it, considering the target and the level of reserves. A continuous P-AMM enables the
new equilibrium price to be found along the curve and helps smooth ﬂows around it.
The fourth and ﬁfth properties are also motivated by usability: it is simpler for
traders to use when the pricing is continuous and predictable and strategy in optimal
order reporting is simple and minimized. As we will see, the ﬁfth property is related
to notions of path independence and path deﬁciency.

More generally, and across blocks, we desire the following properties.

6. Over many blocks, the reserve can only be exhausted over a long time period.

7. Over many blocks, a de-pegged stablecoin has a path toward regaining peg.

8. The P-AMM mechanism can be eﬃciently implemented and computed on-chain.

The sixth property ensures that the stablecoin’s asset backing persists well into
the future (e.g., speculative attacks on the system cannot exhaust the reserve). The
seventh property means that there are credible reasons why speculators could decide
to bet on re-pegging of the stablecoin during a crisis. The eighth property ensures
that the mechanism could be used under the severe computational restrictions of
real world smart contract systems (e.g., is not prohibitive in terms of gas fees on
Ethereum).

4 Redemption Curve Design

We now discuss our P-AMM design. We ﬁrst introduce the dynamical system
framework within which our design will take place. We then describe a greatly
simpliﬁed redemption curve design that satisﬁes all desiderata but one: its redemption
curve is not continuous but has a steep discontinuity. Finally, we introduce our actual,
more sophisticated continuous redemption curve design.

4.1 Dynamical System, Anchor Point

For the purpose of designing the P-AMM, we model the stablecoin system along three
dimensions: an outstanding stablecoin (SC) supply y, a total reserve value backing
the stablecoin b, and a level of stablecoin redemptions from the reserve x. These state
variables are summarized in the following table.

10

State Variable Deﬁnition

b
y
x

total reserve value (in USD)
outstanding SC supply
level of SC redemptions

We model the system as a dynamical system, in which x is the independent variable
that drives the system. Put another way, x will represent the “current point along
the trading path” of the P-AMM. We will also be interested in the reserve ratio
r(x) := b(x)/y(x), which describes the reserve value per outstanding stablecoin.5
Observe that y(x) = ya − x and b(x) = ba − R x
0 p(x0)dx0, where p(x0) is the marginal
redemption price oﬀered by the P-AMM at redemption level x0.

The dynamical system models P-AMM trades that occur within a single block.
At the beginning of the block, we will have initial conditions (x0, b0, y0). Here, x0
represents a measure of redemption history in previous blocks. Net redemptions
within the modeled block will increase x from x0. The ﬁnal P-AMM will evolve over
many blocks using this same intra-block model; however, x0 at the start of each
block will be computed as an exponentially time-discounted sum over all past SC
redemptions in previous blocks. For our analysis in this paper, we restrict ourselves
to the context of a single block, in which x0 is a ﬁxed initial condition. The initial
conditions are summarized in the following table.

Init. Condition Deﬁnition

x0
b0
y0

level of SC redemptions at block start
reserve value at block start (b0 = b(x0))
SC supply at block start (y0 = y(x0))

Note that we will generlaly not have x0 = 0 in practice. However, it will be useful
to reference a ﬁctitious initial condition that would describe a starting point of 0. We
call this the anchor point, which is formally the triplet

(0, ba, ya),

where ba = b(0) and ya = y(0). Many times, we will be interested in the reserve ratio
at the anchor point ra = ba/ya. Figure 6 visualizes what the reserve ratio curves will
look like as a function of x for various values of ra. As we will see, each curve will
have a unique anchor point ra, which corresponds to the starting point of the curve.
The pricing curve p is, in general, a function of ba and ya. We will see later that
the anchor point can be expressed in terms of the current state alone. With this in
mind, it will be analytically useful to deﬁne the evolution of the dynamical system in
terms of the current state (x, b, y) directly. Toward this, we will construct an abstract
pricing function ρ(x, b, y) that we will show is equivalent to the function p in case
b/y < 1; in the (trivial) case where b/y ≥ 1, we set ρ(x, b, y) = 1. The dynamical

5We will write b, y, x and r referring to the “current’ state of these variables. In contrast, we
will write b(x) etc for the value at some point of the driving variable x and based on other system
parameters.

11

Figure 6 Reserve ratio curves as a function of x for diﬀerent values of ra (starting
points) in the “normalized” case where ya = 1.

system is then described by the following system of ordinary diﬀerential equations:

db(x)
dx
dy(x)
dx

= −ρ(cid:0)x, b(x), y(x)(cid:1)

= −1.

(1)

Our P-AMM, conceptually speaking, solves the initial value problem deﬁned by
(x0, b0, y0) and the system (1). We then transition to the new state (x0 + X, b(x0 +
X), y(x0 + X)) = (x0 + X, b(x0 + X), y0 − X) and the redemption amount (which is
paid out to the redeemer) is b(x0 + X) − b0.

4.2 Simpliﬁed, Discontinuous Redemption Curve Design

We now discus a simpliﬁed P-AMM redemption curve as a pedagogical starting point.
This simpliﬁed curve has discrete price decay (i.e., the curve is discontinuous: a
portion of the curve is at $1 and another portion maintains a sustainable reserve
ratio) and is very simple to reason about. This will fullﬁl many desirable properties
except for continuity. We provide a semi-formal treatment here; see Appendix B for
the formal details.

To deﬁne the redemption curve, we assume that the anchor point (ba, ya) is ﬁxed
and given. We will discuss in Sections 6 and 8 how the anchor point can be chosen
based on the current state of the system. Assume WLOG ba < ya (i.e., ra < 1) since
otherwise, we always use the trivial redemption curve p(x) = 1. For simplicity of
analysis, we will for now disregard any trading fees that may be added to the P-AMM.
Our simpliﬁed redemption curve is illustrated in Figure 7 and deﬁned by the

following function:

p(x) :=

(1

rU := r(xU )

if x ≤ xU
if x > xU ,

12

0.00.20.40.60.81.0x (normalized)0.600.650.700.750.800.850.900.951.00r(x)Figure 7 Simpliﬁed redemption curve with discrete price decay.

Observe that r(xU ) can be computed from only ba, ya, and xU , so that p(x) is a
well-deﬁned function.

This redemption curve maintains a redemption price of 1 up until some redemption
pressure value xU ∈ [0, ya] and then drops the redemption price to the reserve ratio
below that value. From this point onwards, the reserve ratio will stay constant (this
is easy to see) and in particular, we will be able to provide redemptions at price rU ,
potentially until the whole SC supply has been redeemed.

The parameter xU is a dynamic parameter. Concretely, this means that, given a
speciﬁc value of this parameter, the shape of the redemption curve is ﬁxed. However,
the dynamic parameters itself depends on the state of the system. More in detail, it
is a function of the anchor point (ba, ya).

The choice of the parameter xU introduces a trade-oﬀ: when it is high, we
maintain a price of 1 for a long time (in terms of redemption pressure). This allows
the stablecoin to maintain the peg for longer, but the eventual redemption price rU
will be low. Lower xU values enable a higher eventual redemption price but weaken
the peg more quickly. To weigh this trade-oﬀ, we assume that two static parameters
are set externally (e.g., by the protocol’s governance system):

Parameter Deﬁnition

¯xU
¯θ

∈ [0, ∞] upper bound on xU (xU ≤ ¯xU )
∈ [0, 1] target reserve ratio ﬂoor

xU is then chosen such that the following conditions hold:
1. At any point x of the redemption curve, r(x) ≥ ¯θ, if this is possible, and r(x)
maximal otherwise. Equivalently, we want rU ≥ ¯θ if possible and rU maximal
otherwise.

2. xU ≤ ¯xU .
3. Among the xU values that satisfy these conditions, xU is chosen maximal.

13

Figure 8 Our redemption curve design with piecewise-linear price decay.

One can show that this is the case iﬀ

xU = min

¯xU , max

0, ya

!!

ra − θ
1 − θ

The static parameter ¯xU is optional and can be set to ∞ to turn oﬀ this feature.
In this case, the choice of xU will always create a situation where rU = min(ra, ¯θ),
i.e., we always choose the lowest acceptable eventual reserve ratio to maximize xU .
Setting ¯xU < ∞ makes the trade-oﬀ less extreme and allows rU > ¯θ when ba is large.
It is easy to see that the redemption curve design from this section satisﬁes our
desiderata 1.–3. from Section 3, but it obviously violates desideratum 4 (continuity).
This is undesirable for traders and it creates a potential target for speculative attacks
on the stablecoin price. This is why in the following, we discuss a continuous
redemption curve design.

4.3 Continuous Redemption Curve

To maintain continuity, we alter the design from the previous sub-section to receive
a three-piece-wise curve design. This requires some more sophisticated machinery.
Again, we assume in this section that an anchor point (ba, ya) is given.

We now parameterize the curve in terms of three dynamic parameters. Conceptu-
ally, the three dynamic parameters describe three regions of the P-AMM pricing curve
p as a function of x, as visualized in Figure 8. For a small redemption level x, the
P-AMM provides redemptions at $1 up until a redemption level xU is reached. In a
second region, the P-AMM pricing decays linearly with slope α as more redemptions
occur up until a redemption level xL. Then, in a third region, the P-AMM provides
redemptions at the new reserve ratio (reserve value per outstanding stablecoin),
which is fully sustainable for the entire remaining stablecoin supply. The dynamic
parameters are summarized in the following table.

14

𝑥𝑈Slope = 𝛼Redemptions 𝑥P-AMM price 𝑝$1𝑥𝐿

Dynamic Params Deﬁnition

α
xU
xL

decay slope of redemption curve
point at which redemption deviates from $1
point at which redemption stops decaying
at new reserve ratio

The resulting P-AMM pricing curve, as a function of x and parameterized by the
anchor point, is, in the case that ba < ya,

p(x; ba, ya) =






x ≤ xU

1,
1 − α(x − xU ), xU ≤ x ≤ xL
rL,

x ≥ xL

,

(2)

where rL = r(xL). In the other case that ba ≥ ya, we will simply set p(x) = 1.
Notice that the dynamic parameters α, xU , xL are, in fact, functions of the anchor
point (ba, ya). We discuss the rules by which the dynamic parameters are chosen in
Section 5.

We deﬁne three static parameters that constrain the shape of the curve and inform
the choice of the dynamic parameters. These are the only parameters that are set
externally. We deﬁne a lower bound ¯α to the linear decay slope α, an upper bound
¯xU to xU , and a target reserve ratio ﬂoor ¯θ. The target reserve ratio ﬂoor is the
minimum reserve ratio that the P-AMM curve can decay to, and it is the value of the
reserve ratio in the third region. In case that the initial reserve ratio b0/y0 is smaller
than θ, the P-AMM only oﬀers redemptions at the initial reserve ratio (i.e., xL = 0).
These parameters are summarized in the following table.

Parameter Deﬁnition

¯α
¯xU
¯θ

∈ (0, ∞) lower bound on decay slope (α ≥ ¯α)
∈ [0, ∞] upper bound on xU (xU ≤ ¯xU )
∈ [0, 1] target reserve ratio ﬂoor

Note that an implicit fourth static parameter is the target for the stablecoin price,
thus far assumed to be $1. In general, this could take diﬀerent values (and could
be changed over time by governance) to adjust monetary policy. The underlying
mechanics and our essential results would stay the same. In this paper, we are agnostic
to how the static parameters were set and consider them ﬁxed, but arbitrary. One
particularly useful choice is to set them proportional to the anchored outstanding SC
supply ya, which we believe would minimize the need for governance interaction as
the outstanding amount changes. We explore this option further in Section 8.

5 Calculation of Dynamic Parameters for a given anchor

point

We ﬁrst establish how to calculate the dynamic parameters of the redemption curve
when the anchor point (ba, ya) is given. Recall that this anchor point is a mathematical

15

modelling tool and is not known as a real quantity at any point in time. Instead, it
will be “reconstructed” from the current market state (see Section 6 below). Assume
for non-triviality that 1 > ba/ya > θ. Then the dynamic parameters are chosen as
follows.

• xL is chosen such that p(xL) = r(xL), i.e., the computed redemption price (in
the linear segment) equals the reserve ratio at this point. If xL is chosen like
this, all remaining stablecoin units could be redeemed at this price without
running out of reserves. xL is a function of (ba, ya), xU , and α. Note that r(xL)
is the lowest reserve ratio on the curve.6

• α and xU are chosen to guarantee that r(xL) ≥ θ while minimizing price decay.
• Among the (α, xU ) pairs satisfying the previous condition, we prioritize making
α as small as possible (but at least α), i.e., making price decay as mild as
possible in the linear part. If α = α, we then choose xU as large as possible
(but at most ¯xU) while always ensuring r(xL) ≥ θ.

This leads to the following equations (see Appendix C for details; let ∆a := ya −ba):

α = max(α, ˆα) where



ˆα =

,

ˆαH := 2 1−ra
ya
θ2
ˆαL := 1
2
ba−θ ya

ra ≥ 1+θ
2
ra ≤ 1+θ
2

,



xU = min(¯xU, ˆxU) where



q

ˆxU,h := ya −
ˆxU,l := ya − ∆a



ˆxU =

r

(ya − xU )2 −

xL = ya −
rL = 1 − α(xL − xU )

∆a

α

α∆a ≤ 1
2 ∆a
α ,
2α θ α∆a ≥ 1
θ − 1
2

2 θ2
2 θ2 .

6 Uniqueness of Reconstruction

We now move on to show that we can construct the anchor point (ba, ya) uniquely
from the current state (x, b, y), which proves that our dynamical system (1) is in fact
well-deﬁned. Recall that, in that dynamical system, ρ, which is a function solely of
the current state, ‘reconstructs’ p, which is also a function of the anchor point (ba, ya).
Our proof in this section is indirect: we show that that each state (x, b, y) can only
have arisen from one speciﬁc anchor point (see Section 8 for an explicit reconstruction
technique). Uniqueness of ya is trivial because y = ya − x, so ya = y + x; it remains

6One can show that r(xL) increases when α is increased (i.e., the reserve is protected when
redemption prices decay more steeply) and when xU is decreased (i.e., the reserve is protected when
the redemption price starts to decay earlier).

16

to show that ba is unique. We show that this is the case because, for ﬁxed x, the
reserve value

b(x; ba, ya) =

p(x0; ba, ya) dx0

Z x

0

is a strictly monotonic function of ba, whenever that state is non-trivial.7

Theorem 1. Fix values ya, θ, α, ¯xU and ﬁx some x ∈ [0, ya). Assume that xU and α
are chosen dependent on ba according to the rule described above. Let ba and b0
a be such
a/ya > θ).
) > θ (and in particular 1 > ba/ya, b0
that ba < b0
Then b(x; ba) < b(x; b0
a

a and 1 > r(x; ba), r(x; b0
a
).

The result is less immediate than it may seem at ﬁrst. While it is easy to see that
a lower ba leads to a lower value of b(x) when leaving the parameters α, xU ﬁxed, the
situation we consider here is diﬀerent. In particular, as we reduce ba, the parameters
α and xU will adjust according to propositions 4 and 5 to ensure our desiderata. A
priori, it might be the case that, through this adjustment, a lower value of ba leads to
a lower value of b(x) at some point x, but to a higher or the same value of b(x0) at
some other point x0. Theorem 1 proves that this is not the case: the whole reserve
value curve b( · ) is strictly monotonic in the anchor reserve value ba at all non-trivial
points.

We segment the space of (x, ba) pairs along all case distinctions we have made
so far. Speciﬁcally, we distinguish cases along the following dimensions. Note that
these cases deﬁne closed regions and overlap at their boundaries and that within the
intersection of any selection of these regions, the function b( · ) is smooth. Recall that
ra = ya/ba is the reserve ratio at the anchor point.

• Case I–III depending on the values of α and xU . Speciﬁcally, let α = max(ˆα, α),

write short ˆxU := ˆxU(α), and let xU = min(ˆxU, ¯xU), and deﬁne:

I

II

ˆα ≥ α and ˆxU ≥ ¯xU, so that α = α and xU = ¯xU.
ˆα ≥ α and ˆxU ≤ ¯xU, so that α = α and xU < ¯xU except in the equality
case.

III ˆα ≤ α, so that α < α except in the equality case and (in any case) xU = 0.

• Within case II, case II h, where α∆a ≤ 1

l, where α∆a ≥ 1

2 θ2 and thus ˆxU = ˆxU,l.

2 θ2 and thus ˆxU = ˆxU,h and case II

• Within case III, case III H, where ra ≥ 1+θ
2

and thus ˆα = ˆαH and case III

L, where ra ≤ 1+θ
2

and thus ˆα = ˆαL.

• Case i–iii depending on the value of x relative to xU and xL. Speciﬁcally,

deﬁne:

7Equivalently, the reserve ratio r(x) is strictly monotonic in ba, since it is a strictly monotonic
transformation of b(x) for ﬁxed x. In this section, we consider the static parameters θ, α, ¯xU ﬁxed
while the dynamic parameters α and xU take on values dependent on the anchor point as discussed
in Section 5.

17

i x ≤ xU

ii xU ≤ x ≤ xL

iii xL ≤ x

Note that only the distinction between case i–iii depends on x. In the following,
we will address cases by a sequence of letters, such as case II h ii. Note that
not all 36 potential combinations of these cases need to be addressed one-by-one.
Many of these cases are irrelevant or easy to handle. For instance, in case I, the
values of the parameters are known to be the constants (α, ¯xU) and thus we do not
have to distinguish the H/L or h/l cases. The following proposition helps us when
distinguishing the H/L and h/l cases. This will be useful for the proof of Theorem 1
Recall that all dynamic parameters we have deﬁned so far, like xL, are functions of
ba.

Prop. 1. In case II h and III H, xL = ya. In case II l and III L, rL = θ.

[Link to Proof]

The result allows us to exclude certain parts of the state space from the analysis
because there, the recovery rate is at most our deﬁned ﬂoor and thus the mechanism
deﬁnes that redemption must happen at the reserve ratio.

The result immediately implies that we do not need to consider cases II iii or III
iii because the recovery rate is at most our deﬁned ﬂoor and thus the mechanism
deﬁnes that redemption must happen at the reserve ratio.

Corollary 1. In case II iii and III iii, r(x) ≤ θ.

[Link to Proof]

Conceptually, we can visualize the function b(x; ba), with which Theorem 1 is
concerned, as a 3d surface. Figure 9a shows the surface of the reserve ratio as a
function of x and ba, where the diﬀerent regions partition the (x, ba) space.8 We have
chosen ya = 1 so that ba = ra (but in general b 6= r). Notice that, as mentioned
above, several of the regions can be essentially ignored. This is for two reasons: ﬁrst,
some of the lines separating diﬀerent cases fall into a part of the (x, ra) space where
the respective case is not relevant. For instance, in this example, the line separating
the H and L cases itself falls into region II, so that only case III L is present. In
contrast, the line separating cases h and l falls into region II, so that both cases II
h and II l are present. The second reason why distinctions between regions can be
ignored is that they fall along a certain ﬂat region of the surface that has zero area
in a projection of interest. This projection of interest is the 2-d (x, r) space. This
is visualized in Figure 9b, in which many r curves are plotted (in gray) for diﬀering
values of ra, which are the starting points of these curves. In this space, the region

18

Figure 9 Reserve ratio r as a function of the current redemption amount x and the
initial reserve ratio ra for the normalized case ya = 1. Due to normalization, we have
ra = ba. The parameters θ = 0.3, α = 0.8, and ¯xU = 0.3 were used. The ﬁgures also
depict xL and xU on the X axis as functions of ra

(a) 3d curve.

(b) 2d projection to the (x, r) plane.

Figure 10 Reserve ratio r as a function of the current redemption amount x and
the initial reserve ratio ra for ya = 1 and two choices of parameters.

(a) θ = 0.3, α = 0.5, ¯xU = 0.3. There is a
stretch where xL = 1.

(b) θ = 0.3, α = 1.3, ¯xU = 0.3. There is no
point where xL = 1.

19

boundaries are given by particular cases of r curves, as shown. Notice that the ﬂat
section of the 3-d surface mentioned above disappears in the 2d-projection.

In Figure 9, region III H does not exist and there is a stretch of ra values where
xL = 1. This, however, is not universally the case and depends on the parameters.
We illustrate two 3d curves r(x; ra) where this is and is not the case, respectively, in
Figure 10.

Using the region partition, we can prove Theorem 1. Our proof is by case
distinction over the diﬀerent regions. Observe that the function b(x, ba) is smooth
across any given region and we can compute the partial derivative of b(x, ba) with
respect to ba explicitly. The main challenge is to handle the adjustment in the dynamic
parameters that takes place as ba is varied.

[Link to Proof of Theorem 1]

7 Path Properties

Now that we’ve established that the P-AMM design is well-deﬁned and robust in
shape, we move on to show that it obeys many useful trading properties, including in
settings involving trading fees and a separate minting curve. We characterize these
in terms of path independence and path deﬁciency, which will lead us to two main
useful properties:

• There is no incentive for redeemers to strategically subdivide redemptions,

including in some settings with trading fees.

• In a wide array of settings involving a P-AMM with minting, redeeming, and
trading fees, the protocol itself is only better oﬀ in terms of the reserve ratio
curve no matter which trading path is realized.

7.1 Path Independence

We ﬁrst show that the P-AMM redemption curve, as developed thus far without
trading fees, is path independent within a block. This means that the end result of
any path of redemptions is the same for any given starting and ending point. On the
ground, this is useful for traders as they do not need to worry about how exactly they
use the P-AMM within a block: there is no incentive to split up redemptions into
smaller chunks or to merge many small redemptions into bigger units.

Theorem 2. (Path independence) Let S0 := (x0, b0, y0) be a state and let X, Y > 0
such that X + Y ≤ y0. Let the state SX result from redeeming X at S0, SX,Y from
redeeming Y at SX , and SX+Y from redeeming X + Y at S0. Let the paid-out amounts
be PX , PX,Y , and PX+Y respectively. Then the following hold.

1. PX + PX,Y = PX+Y

8Note that b(x; ba) = r(x; ba) · (ya − x), so that there is a simple 1:1 relationship between the
reserve value and the reserve ratio. We present the reserve ratio because we ﬁnd it more illustrative
of the diﬀerent phenomena.

20

2. SX,Y = SX+Y

[Link to Proof]

The theorem holds because the right-hand sides of (1) only depend on the current
state of the system and not, for instance, on the initial conditions or the speciﬁc
trading path that led to the current state. In the dynamical systems literature, this
property is also known as invariance under horizontal translations.

Note that the theorem only holds for redemptions immediately following each
other within the same block —the context of our model in this paper— as otherwise
we need to consider the time decay of the initial condition x0 across blocks as well as
exogenous changes to b and minting operations happening between two redemptions.
Additionally, if there are many traders using the P-AMM to redeem, there will at
times be an incentive to be earlier in the redemption queue.

7.2 Path Deﬁciency Properties with Minting and Fees

We next discuss two properties analogous to path deﬁciency in CFMMs (see Angeris
and Chitra, 2020) that holds in an extended setting with fees and the possibility of
minting tokens in addition to redemption (where minting occurs at the same or a
higher price than redemption). In this section, we provide an informal discussion of
these results. For a formal treatment, see Appendix D.

Our ﬁrst result is that, for any non-negative fee, trading along any trading path
(i.e., any sequence of mint and redeem operations) can only improve system health
compared to the net of the path. This property is important because it implies that
the system is robust even under (and, in fact, beneﬁts from) combinations of mint
and redeem operations, which may result from market volatility. We capture “system
health” by the reserve ratio r(x) at a given redemption level x. This is a function
of the anchor point (ba, ya) and the static parameters ¯xU, α, θ. We assume in the
following that these values are held ﬁxed.

Theorem 3 (Path Deﬁciency Vs. Netting, Informal). Consider any trading path
ending in redemption level x. Let r1 be the reserve ratio of the system after following
the trading path through its mint and redeem operations and let r0 := r(x) be the
reserve ratio at the net minting or redemption amount. Then r1 ≥ r0.

Our second result states that, in settings with a proportional fee, there is no
incentive for a trader to strategically subdivide a net redemption trade into a sequence
of diﬀerent trades. Note that, clearly, this may not be true when fees are non-linear
in the size of a trade.

Theorem 4 (Path Deﬁciency Vs. Subdivision, Informal). Assume that a non-negative
fee is taken proportional to the redemption amount. Then the following hold:

1. The system is path independent with respect to combinations of only redemption

(but not minting) operations even in the presence of fees.

21

2. An individual trader has no incentive to subdivide a net redemption within a

block into a combination of minting and redemption operations.

For traders, the previous theorem means that interacting with the mechanism
is straightforward. For the mechanism, it means that the mechanism cannot be
exploited by forming complex trading paths.

Note that there may still be strategic interaction between many traders, but these
considerations are limited and fairly simple (and can in fact be avoided with a batch
settlement of trades in the block, which is fundamentally possible if more diﬃcult to
implement). There can be an incentive for a given trader to get a redemption trade
in earlier than other redemption trades. There can also be an incentive for a given
trader to get a redemption trade in after any minting trades are settled. Note that
in many circumstances where this would matter, we are not likely to see mint and
redemption transactions in the same block, however, as a trader would likely get a
better price for one or the other on a secondary market. A further concern is whether
arbitrage trades, in which the net redemption is zero, are proﬁtable (e.g., a sandwich
attack around other trades). This is not endogenously proﬁtable from the P-AMM
structure alone since redemption prices are ≤ 1 while minting prices are ≥ 1.

8 Eﬃcient Implementation

We now discuss how to implement our mechanism on-chain. This section provides a
high-level overview. The formal details are presented in Appendix E. Appendix B.2
discusses the implementation of the simpliﬁed redemption curve with discrete price
decay.

The P-AMM can be operationalized as follows: we are given the current state of
the system (x, b, y), a redemption amount X, and we need to compute a redemption
amount B that the trader should receive in exchange for X units of the stablecoin.
To do this, the system constructs the anchor point (ba, ya) consistent with the
current state, constructs the redemption curve from this, and then integrates over
the redemption curve to compute the redemption amount.

Most of the implementation operates in a space normalized to ya = 1. This is
convenient because it allows the system to be conﬁgured in a way that is invariant under
scaling of the stablecoin supply. We therefore assume that the static parameters refer
to the normalized space. Speciﬁcally, we assume that the following static parameters
are given:

Parameter Deﬁnition

α1
¯xU,1
¯θ

∈ (0, ∞) lower bound on decay slope in normalized space
∈ [0, 1] upper bound on xU in normalized space
∈ [0, 1] target reserve ratio ﬂoor

Note that under the normalization, we assume that the anchor stablecoin supply
ya is 1, not the current supply y. Note also that the target reserve ratio ﬂoor is
not aﬀected by normalization. In Appendix E, we discuss the conversion between
normalized and non-normalized space in detail.

22

The implementation of the algorithm now proceeds as follows (see Algorithm 4 in
Appendix E). Assume WLOG that b/y ∈ (θ, 1) since otherwise, the behavior of the
P-AMM is trivial.

First, we can easily reconstruct ya = y + x. The algorithm then normalizes all
values to ya = 1; speciﬁcally, we consider the normalized state (x/ya, b/ya, y/ya) and
at the end of the algorithm, we will undo the normalization by scaling the computed
normalized redemption amount by ya. To simplify the exposition, assume in this
section WLOG that ya = 1 so that the original state and the normalized state are
the same and we don’t need to introduce any additional variables.

The algorithm now reconstructs the anchor reserve value ba consistent with the
current state. This is the most complex step of the algorithm. Recall that (ba, ya)
together with the static parameters determine the dynamic parameters and thus the
full redemption curve. We are looking for a ba such that

b = b(x; ba, ya = 1).

It follows from continuity that such a ba must exist and Theorem 1 implies that it is
unique, but the theorem provides no way of computing it eﬃciently. To do this, we
proceed in two steps:

1. First, we determine the region of (x, b, y) among the regions introduced in
Section 6. Recall that these regions depend on ba because they depend on the
dynamic parameters xU and α. The main insight that enables this step is that
the region of a state can still be determined eﬃciently even if ba is not known.
To enable this, the algorithm (pre-)computes certain ba values that separate
diﬀerent regions. We also show that (ba, ya) can be replaced by (b, y) when
computing certain speciﬁc thresholds.

2. Second, given the region, we determine ba. This is now relatively straightforward
by replacing the deﬁnitions of α and xU from propositions 4 and 5 as functions
of ba into the deﬁnition. Note that the region determines all case distinctions in
the deﬁnitions, so that the equation b = b(x; ba, ya) is smooth. In fact, it turns
out that this can be written as a polynomial equation of degree at most 2 in ba
and thus solved easily for each individual region.

With ba determined, we can compute α and xU and from this we compute

B = b − b(x + X; ba, ya).

Note that the involved integral can be computed easily because p is piecewise-linear
in x. We ﬁnally undo the normalization by returning ya · B.

Regarding computational cost, the algorithm can be implemented using only a
constant number of arithmetic operations (no loops) and at most two square roots.
While techniques like pre-computation and caching could be used to further speed up
the region detection step, their utility would have to be carefully traded oﬀ against
the cost of storage; our current implementation does not use these techniques.

23

9 Concluding Remarks

We have designed a desirable P-AMM redemption curve based on an anchored state
that codiﬁes how a stablecoin can sustainably adapt monetary policy to respond to
crisis events without external input. This can work to mitigate currency runs if the
stablecoin becomes under-reserved or, with some modiﬁcation to consider the liquid
reserve ratio, to mitigate bank run-like risks if the reserve contains illiquid assets. We
showed how this design satisﬁes desiderata 1–5 and 8 introduced in Section 3.

Desiderata 6 and 7 can be reasoned about considering how the anchored state
changes over time according to an exponentially time-discounted sum and using
desiderata 1–5. It is possible to show that desiderata 6 and 7 are satisﬁed formally.
We leave this as the starting point for a wider study of time evolution. In particular,
future work should also study how the P-AMM behaves under wider market reactions
and other stabilization mechanisms, including a model of exogenous random shocks
to reserve value.

The desiderata properties that the P-AMM achieves were informed by results
about optimal monetary policies in currency peg models and redemption policies in
bank run models. A natural follow-up question is how to optimally parameterize the
P-AMM. A ﬁrst step in this direction would be to adapt currency peg models to a
stablecoin setting with the general P-AMM shape deﬁning the monetary policy and
optimize the outcomes of the resulting game.

A remaining question is how one should optimally calibrate the P-AMM. This
would be best carried out using formal game-theoretic models of speculative attacks
on the P-AMM. An example of this type of attack involves an attacker who can take
an outside short position and try to proﬁt by triggering a de-peg of the stablecoin.
Models of these attacks would integrate the P-AMM, a secondary market, and a
shorting market, and is outside the scope of this paper. Models of speculative attacks
on ﬁat currencies, which informed the P-AMM desiderata in the ﬁrst place, may serve
as a good starting point; we discuss these in Appendix A.

Another avenue for future work is to explore alternative P-AMM designs that
may satisfy the desiderata. For instance, a P-AMM with a sigmoidal shape would
have further smoothness. However, such designs would likely present computational
issues on-chain, including both the raw number of computational steps required (i.e.,
gas requirements for on-chain execution) and ampliﬁcation of rounding errors arising
from ﬁxed point arithmetic.

References

H. Adams, N. Zinsmeister, M. Salem, R. Keefer, and D. Robinson. Uniswap v3 core.

Technical report, Technical report, 2021.

G. Angeris and T. Chitra. Improved price oracles: Constant function market makers.
In Proceedings of the 2nd ACM Conference on Advances in Financial Technologies,
page 80–91, 2020.

24

G. Angeris, A. Evans, and T. Chitra. When does the tail wag the dog? curvature

and market making. arXiv preprint arXiv:2012.08040, 2020.

D. Bullmann, J. Klemm, and A. Pinna. In search for stability in crypto-assets: are

stablecoins the solution? ECB Occasional Paper, (230), 2019.

A. Capponi and R. Jia. The adoption of blockchain-based decentralized exchanges:
A market microstructure analysis of the automated market maker. Available at
SSRN 3805095, 2021.

D. W. Diamond and P. H. Dybvig. Bank runs, deposit insurance, and liquidity.

Journal of political economy, 91(3):401–419, 1983.

M. Egorov. Stableswap-eﬃcient mechanism for stablecoin liquidity. Retrieved Feb, 24:

2021, 2019.

B. Guimaraes and S. Morris. Risk and wealth in a model of self-fulﬁlling currency

attacks. Journal of Monetary Economics, 54(8):2205–2230, 2007.

A. Klages-Mundt and A. Minca. (in) stability for the blockchain: Deleveraging spirals

and stablecoin attacks. Cryptoeconomic Systems, 2021.

A. Klages-Mundt and A. Minca. While stability lasts: A stochastic model of noncus-

todial stablecoins. Mathematical Finance, 2022.

A. Klages-Mundt, D. Harz, L. Gudgeon, J.-Y. Liu, and A. Minca. Stablecoins 2.0:
Economic foundations and risk-based models. In Proceedings of the 2nd ACM
Conference on Advances in Financial Technologies, pages 59–79, 2020.

L. Lee and A. Klages-Mundt. Governance extractable value, Apr. 23, 2021. URL

https://ournetwork.substack.com/p/our-network-deep-dive-2.

Y. Li, S. Mayer, et al. Managing Stablecoins: Optimal Strategies, Regulation, and
Transaction Data as Productive Capital. Ohio State University, Fisher College of
Business, Charles A. Dice Center . . . , 2020.

S. Morris and H. S. Shin. Unique equilibrium in a model of self-fulﬁlling currency

attacks. American Economic Review, pages 587–597, 1998.

A. Orphanides. Taylor rules. In Monetary Economics, pages 362–369. Springer, 2010.
C. Parlatore. Fragility in money market funds: Sponsor support and regulation.

Journal of Financial Economics, 121(3):595–623, 2016.

I. G. Pernice, S. Henningsen, R. Proskalovich, M. Florian, H. Elendner, and B. Scheuer-
mann. Monetary stabilization in cryptocurrencies–design approaches and open
questions. In 2019 Crypto Valley Conference on Blockchain Technology (CVCBT),
pages 47–59. IEEE, 2019.

B. Routledge and A. Zetlin-Jones. Currency stability using blockchain technology.

Journal of Economic Dynamics and Control, page 104155, 2021.

G. Selgin. Modeling the legend, or, the trouble with diamond and dybvig: Parts
i and ii. https://www.alt-m.org/2020/12/18/modeling-the-legend-or-the-
trouble-with-diamond-and-dybvig-part-ii/, 2020.

S. M. Werner, D. Perez, L. Gudgeon, A. Klages-Mundt, D. Harz, and W. J. Knotten-
belt. Sok: Decentralized ﬁnance (deﬁ). arXiv preprint arXiv:2101.08778, 2021.

25

Appendix

A Parallels with the monetary economics literature.

A well-designed primary market for a stablecoin can be interpreted as an autonomous
version of open market operations, comparing with how central banks interact with
markets to shape monetary policy. When new stablecoins are sold on the primary
market, the balance sheet is expanded, and when stablecoins are redeemed, the
balance sheet is contracted. The primary market design determines how much the
balance sheet changes, supposing all proceeds of the market go onto the balance
sheet.9 Notice here that the primary market mechanism essentially solves the scaling
issues that arise in leverage-based stablecoins, like Dai: the stablecoin is always able
to meet excess demand by expanding the balance sheet (it does not need to match
the demand of other agents in doing so).

The P-AMM can be compared to a variant on a crawling or managed ﬂoat system
for a currency peg. The monetary economics literature on these topics provides a
starting point to understand this design.

International monetary economics is concerned with balance of payments crises
(i.e., sudden changes in capital ﬂows). With a stablecoin as opposed to a national
currency, we’re less concerned with money ﬂows in/out of a country’s economy. The
analog for a stablecoin is with ﬂows in/out of the reserve and the level of economic
demand for use of the stablecoin as opposed to demand to speculate on the stablecoin.
Further, stablecoin monetary policy is simpliﬁed to targeting stability relative to the
target as opposed to further targeting growth of a national economy.

Speculative attacks on currency pegs are characterized in the global games lit-
erature (e.g., Morris and Shin (1998)). In these models, speculators can coordinate
to attack the currency while proﬁting from bets on currency devaluation. High
levels of coordination can force the government to abandon the peg. There is a
unique equilibrium in such games, shown in Morris and Shin (1998), given uncertainty
in common knowledge of fundamentals (e.g., faith in government policy, economic
demand, and health of reserves), which can lead to speculative attacks even when
fundamentals are strong.

The curvature of the P-AMM serves to deter speculative attacks by increasing
their cost in several ways. In large outﬂow settings, the curvature of f can allow
short-term (though not necessarily long-term) depreciation from the peg. This can be
interpreted as raising interest rates for new stablecoin holders. Akin to zero coupon
bonds bought at a discount, buyers expect to redeem for a higher price later. This is
supported by the fundamental value of the reserve, which, when healthy, tends to
shift the coordination equilibrium to $1 as outﬂows equilibrate.10 Compared to a

9Notably, many algorithmic stablecoins divert a share of primary market cash ﬂow to holders
of “equity” tokens —we consider such systems insolvent-by-design as they give away part of the
“seigniorage” income from purchases of newly minted stablecoins (typically via buybacks of “equity”
tokens), unlike a bank that maintains full asset-backing of deposits. This structure has contributed
to many experienced crises for these coins.

10While certain uncollateralized (or “implicit collateral”, see Klages-Mundt et al. (2020)) stablecoins

26

typical currency peg, the curvature of the P-AMM forces an attacking speculator to
redeem at deteriorating prices throughout the attack, after which the redemption rate
can bounce back. As a consequence, the crisis has to be stretched over long periods
of time, during which speculators incur the spread loss, to have a permanent eﬀect
on the peg and reserve health. Additionally, the funding rate for a short bet on the
stablecoin–a prime proﬁt source for a speculative attack–ought to take into account
the transparent shape of the P-AMM and state of the reserve. In settings that are
otherwise prime for speculative peg attacks (e.g., when reserve value per stablecoin
is much less than $1), the short funding rate ought to be very high to account for
the ease of causing short-term devaluations via the P-AMM shape, which serves to
further raise the costs of attack.

Lastly, we contrast with the bank run model in Diamond and Dybvig (1983). In
that model, the bank serves as insurance for two types of agents: one type who will
need to withdraw early and another type who will not, but without knowing which
is which ahead-of-time. Given the setup of the model, the bank is often prone to
bank runs that depletes the bank’s liquid assets. Speculative attacks on a stablecoin
can often be viewed in a similar way to a bank run. In this context, the stablecoin
design eﬀectively alters the assumptions of the Diamond-Dybvig model to deter
the undesirable bank run equilibrium (see Selgin (2020) for further discussion of
the following points). First, the curvature of the P-AMM reduces the redemption
rate of large withdrawals. One cause of fragility in the Diamond-Dybvig model is
requiring absolute liquidity out of bank deposits. Altering this structure can increase
robustness at relatively small costs in terms of stablecoin liquidity. Second, since a
liquid stablecoin is tradeable on secondary markets there is often no need to directly
redeem it in the primary market.11

Some qualitative results from the literature on speculative attacks on currencies
can be applied directly to the P-AMM setting. In particular, Routledge and Zetlin-
Jones (2021) analyzes a game theoretic model that is implicitly similar to the P-AMM
setting, in which a government or currency issuer tries to maintain an optimal exchange
rate peg while under-reserved. In this model, the optimal strategy involves the central
bank demonstrating commitment to devalue the currency if too many traders demand
redemption from reserves, which eliminates the speculative attack equilibrium and
stabilizes the exchange rate.

Although Routledge and Zetlin-Jones (2021) is written in the context of cryptocur-
rency stabilization, the model is most descriptive of traditional currency models, in
which the exchange rate is pegged to another currency that is held by the central bank
in reserves. The cryptocurrency setting is a little diﬀerent: (1) reserve assets may not
be the currency target, and (2) exchange rate policy needs to be encoded on-chain
in smart contracts as opposed to determined on-the-ﬂy by central bank governors.

also propose similar narratives as here, they do so without a fundamental force, such as from a
reserve, pushing coordination toward the $1 equilibrium. Accordingly, one may question whether the
stable equilibrium may really be $0 price in such cases.

11Similarly, digital commercial bank money does not need to be redeemed from the bank to use
but can be used as a means of payment directly. A stablecoin on a public interoperable blockchain
could be even more ﬂexibly used without requiring redemption.

27

However, after translating reserve asset values into the appropriate numeraire for
the peg and adjusting for the fact that these values follow a stochastic process, the
P-AMM setting can be adapted to the underlying model in Routledge and Zetlin-Jones
(2021). In this case, the P-AMM shape when under-reserved provides the means of
committing to stablecoin devaluation in the event of speculative attacks, which can
eliminate the speculative attack equilibrium.

B Simpliﬁed, Discrete Redemption Curve

In this section, we provide the formal details for the simpliﬁed price decay function
from Section 4.2 where prices decay discretely from 1 to the reserve ratio. This
discrete price decay form leads to much simpler calculations than the linear one
outlined in the main text of this paper. However, it has the disadvantage that price
decay happens abruptly, which creates risk for arbitrageurs and may also create an
opportunity for speculative attacks.

We ﬁrst describe the general design and the computation of dynamic parameters
(similar to Section 5) and we then discuss the implementation of the mechanism
(similar to Section 8).

B.1 Design and Dynamic Parameters

Recall that here, we use

p(x; ba, ya) :=

(1

rU := p(xU ; ba, ya)

if x ≥ xU
if x < xU ,

where xU is a dynamic parameter and rU is chosen such that rU = r(xU ) based on
the other parameters. The parameters fulﬁll the same role as in our linear price decay
mechanism where, however, the linear segment (and its parameter α) as well as the
lower cut-oﬀ point xL are missing.

Lemma 1. Let ba < ya. Then the following hold:

1. We have

b(x) =

(ba − x
ba − xU − rU · (x − xU )

if x ≥ xU
if x ≤ xU

2. If xU < ba, then rU = ba−xU
ya−xU

reserve is exhausted at a point x < ya.

and the reserve is never exhausted. Otherwise, the

3. In this case, we have rU ≥ θ iﬀ ba/ya ≥ θ and xU ≤ ba−θ ya

θ

, where θ = 1 − θ.

Proof.

1. This follows immediately by integration over p.

28

2. First assume xU < ba. By part 1 we have b(xU ) = ba − xU and further
y(xU ) = ya − xU , and rU = r(xU ) = b(xU )/y(xU ). By assumption, rU ∈ (0, 1)
and, since we redeem at the reserve ratio after the point xU , the reserve is never
exhausted. Now assume xU ≥ ba. Then, by part 1, we have b(ba) = 0 and by
assumption, ba < ya.

3. By part 2 and simple algebraic transformation, rU ≥ θ iﬀ xU ≤ ba−θ ya

. This is

only possible if ba/ya ≥ θ since otherwise, the right-hand side is negative.

θ

Let ¯xU be the (optional) ceiling value for xU . Then by the previous lemma the
maximal xU ≤ ¯xU that ensures rU ≥ θ (if possible, and rU maximal otherwise) is
xU = min(¯xU, ˆxU), where

ˆxU := max

0, ya

!

ra − θ
1 − θ

(3)

where we recall that ra := ba/ya. Note that we choose xU = 0 if ra < θ, so that in
this case, we redeem at the reserve ratio from the very beginning.

B.2

Implementation

To implement our mechanism (i.e., to deﬁne ρ(x, b, y)), we can perform a distinction
into diﬀerent regions like in sections 6 and 8, though the operation is much simpler
here. We only consider two dimensions with two cases each.

• Case I, where ˆxU ≥ ¯xU, and case II, where ˆxU ≤ ¯xU.
• Case i, where x ≤ xU and case iii, where x ≥ xU . There is no case ii.
For the implementation, we proceed analogously to Section 8. Reconstruction
of ba is greatly simpliﬁed in the discrete case because the range of possible values is
much restricted and, importantly, all relevant equations are linear and do not involve
either a square root or a square. First note that, as always, we can easily obtain
ya = y + x, so it only remains to reconstruct ba. Also recall that we only need to do
this when 1 > r = b/y > θ since we otherwise always redeem at 1 or r, respectively.
It is easy to see that, like in Theorem 1, b(x) (and equivalently r(x)) for a ﬁxed x is
strictly monotonic in ba whenever r > θ and thus, any such point has a unique ba
associated. Reconstruction of ba can now be done using a “trial and error” approach
as follows:

• (Case i) Let b0
a
• (Case I iii) Otherwise, ba = b + ¯xU +r · (x − ¯xU).12

= b + x and test if x ≤ xU (b0

a, ya). In this case, ba = b0
a

.

Correctness of the above reconstruction follows from uniqueness of ba and the fact
that the respective conditions hold in the respective cases. Correctness in case I

12This value is unimportant to calculate redemption amounts, though, and would not have to be
computed. This is because, since we’re in case iii, the redemption price will always be r = b/y for all
x0 ≥ x.

29

iii follows by solving the equation for b(x) from Lemma 1 for ba. Note that case II
iii does not need to be checked because, by choice of xU , we must have rU = θ in
this case. To compute a redemption amount, in case i, we have to now compute the
dynamic parameter xU using Equation 3 and then integrate over the redemption
curve, just like in the case with linear price decay. In case I iii, this is trivial and
we can simply compute X · r, where X is the amount of redeemed stablecoins. It is
obvious that the mechanism can be implemented using a constant number of basic
arithmetic operations.

C Detailed Calculation of Dynamic Parameters

We ﬁrst establish how to calculate the dynamic parameters of the redemption curve
from the anchor point (ba, ya). We do this as a series of technical lemmas that will be
used in our later results. We start by showing how to calculate b(x) in the simpliﬁed
context in which the dynamic parameters are known/ﬁxed. Recall though that, in
general, the dynamic parameters are functions of the current state (more precisely, of
the anchor point) and the static parameters. We then move on to derive results about
how to calculate the dynamic parameters in their general form. We prove additional
technical guarantees, which are not required for the purpose of this exposition, but
may be useful when implementing our methods, in Appendix G.

We now consider how the current state is connected to the anchor point. For y(x),
we simply have y(x) = ya −x. When α, xU , and xL are known and ﬁxed, it is simple to
calculate the function b(x). The next proposition speciﬁes how to do this. To state the
proposition, observe that the reserve ratio at x is r(x) = b(x)/y(x) = b(x)/(ya − x).
Observe that r(0) = ra = ba/ya. Note that r(ya) would be ill-deﬁned in this
sense since the denominator would be 0. We extend the deﬁnition continuously by
r(ya) := limx→ya r(x). This will be well-deﬁned for all relevant cases below.
Prop. 2. For ﬁxed α, xU , xL with xU ≤ xL we have

b(x) = ba −

Z x

0

p(x0)dx0 =






ba − x,
ba − x + α
2
rL(ya − x),

(x − xU )2, xU ≤ x ≤ xL

x ≤ xU

xL ≤ x,

where rL = r(xL). rL can be computed using the second case in the case distinction
alone.

[Link to Proof]

Recall that we have three static parameters α ∈ (0, ∞), ¯xU ∈ [0, ∞], and θ ∈ [0, 1].
θ deﬁnes a ﬂoor on the reserve ratio, if achievable, and α and ¯xU are bounds on the
respective parameter: we always have α ≥ α and xU ≤ ¯xU. Depending on the anchor
point (ba, ya) and constrained by these parameters, we choose values for the dynamic
parameters that determine the curve shape. Deﬁne an auxiliary function
(1,

(4)

pU (x) :=

x ≤ xU
1 − α(x − xU ), x ≥ xU .

30

Then the dynamic parameters xU , α, and xL are chosen according to the following
rule.

• For given xU and α, xL is chosen such that xL ∈ (xU , ya] and p(xL; ba, ya) =
r(xL; ba, ya), where both sides of this equation can be computed based on pU .
The values of the remaining parameters xU and α will be chosen such that such
a point exists (see Proposition 3 below). Note that the case xL = ya is not
pathological, but, as we will see, it occurs regularly. It is easy to see that, by
choice of xL, we have r(x) = p(x) = rL for all x ≥ xL, i.e., we redeem at the
reserve ratio beyond xL, and this is sustainable.

• xU and α are chosen such that 0 ≤ xU ≤ ¯xU, α ≥ α, xL exists, and rL ≥ θ, if
possible. It is easy to see that this is possible iﬀ ra > θ (one possible choice is
xU = 0 and α → ∞ as ra & θ). In the trivial case where this does not hold, we
set the marginal redemption price to constant ra.

• Among the admissible combinations of xU and α, the parameter values are
chosen such that ﬁrst, α is minimized among all possible α values and, second,
xU is maximized given this α. This implies that, if there are admissible solutions
and α < α, then we must have xU = 0. This follows from the fact that rL
increases if we reduce xU .

The rule by which xu and α are chosen in the third step encodes that, when
confronted with a trade-oﬀ between a not-too-steep price decay and a prolonged
support of the exact peg of $1, our mechanism prioritizes the former over the latter.
We argue that this is the appropriate trade-oﬀ in the interest of market stability for
the reasons outlined in Section 3. Note that the mechanism only applies trade-oﬀ
only applies within the limits set by the α and ¯xU static parameters.

Going forward, we will focus on the non-trivial case where ba < ya (otherwise
b > y at any point and the marginal price is constant at 1), ra > θ (otherwise the
marginal price is constant at ra = r(x) ∀x), and, where xU occurs as a parameter, we
assume ya ≥ xU (otherwise the system would be conﬁgured to redeem at price 1 for
all x and in particular will run out of reserves at some point since ba < ya).

The following proposition shows how to calculate xL based on xU and α and in
what settings such a point exists. This result also shows that a key tenet of the
primary market design will be choosing parameters such that xL exists as otherwise
the reserve can be exhausted. To make our formulas more compact, deﬁne the
following shorthands: let ∆a = ya − ba and yU = ya − xU ; let bL = b(xL).

Prop. 3. For given ﬁxed parameters xU , α, the following hold.
1. There exists a point xL ∈ [0, ya] where p(xL) = r(xL) iﬀ

α ≥ 2 ya − ba

(ya − xU )2 .

(5)

2. If (5) does not hold and xL := ∞ in the deﬁnition of p, then the reserve is
exhausted before all tokens have been redeemed. Formally, in this case, there is
x ∈ [0, ya) such that b(x) = 0.

31

3. If (5) holds, then xL is unique and

r

(ya − xU )2 −

xL = ya −
rL = 1 − α(xL − xU )
bL = (1 − α(xL − xU ))(ya − xL)

α

2

(ya − ba)

[Link to Proof]

Remark 1. From the previous proposition, we easily receive an analytical expression for
r(x) = b(x)/y(x) = b(x)/(ya −x). Observe that b(x) and r(x) are continuous functions
of x. Observe in particular that, for x ≥ xL, we have r(x) = rL(ya − x)/(ya − x) =
rL = p(x). Thus, after xL, the reserve ratio remains constant and the marginal
redemption price is the reserve ratio.

We now formalize the rule by which α and xU are chosen. Fix ya, ba, and θ. We
call a pair (α, xU ) admissible if xL exists and rL ≥ θ. We call xU admissible for α if
(α, xU ) is admissible and we call α admissible if there exists some xU such that (α, xU )
is admissible. Note that the set of xU admissible for α always form a closed interval
[0, ˆxU(α)] and the set of admissible α is also a closed interval [0, ˆα]. This follows from
monotonicity in (5), the fact that rL is monotonically decreasing in xU (as can be
seen from the formulas in Proposition 3), and closedness. Deﬁne ˆα and ˆxU(α) as
the interval bounds indicated above. In words, ˆα is the minimum α, disregarding α,
such that (α, xU = 0) is admissible and ˆxU(α) is the maximum xU , disregarding ¯xU,
such that (α, xU ) is admissible. By Proposition 3 we can see that ˆα always exists (if
ba/ya > θ) and is positive and for α ≥ ˆα, ˆxU(α) always exists.

We now choose the dynamic parameters α and xU as follows:
1. First let α = max(ˆα, α).
2. Then let xU = min(ˆxU(α), ¯xU).
Note that the upper bound ¯xU is essentially optional for our construction; we can
choose ¯xU = ∞ (or ¯xU = ya) to deactivate it. In this case, we always have xL = ya if
the θ bound on the reserve ratio is not binding.13 The lower bound α is also optional
and can be deactivated by setting α = 0. Note, however, that for α = 0, we will
always receive xU = 0. This is because then α = ˆα and it is easy to see that ˆxU(ˆα) = 0
(otherwise, we could have chosen ˆα smaller by strict monotonicity; see Proposition 3).
The following lemma will help us in our construction. Let θ = 1 − θ.

Lemma 2. If (5) holds, then rL ≥ θ iﬀ

α(ba − θ ya) − α θ xU −

α(ya − xU ) ≤ θ
1
2 θ2 ≥ 0.

or

[Link to Proof]

(TH)

(TL)

13This will be captured formally as cases II h and III H below.

32

We can interpret the distinction between the conditions (TH) and (TL) in terms
of whether or not the reserve ratio ﬂoor θ is binding. Observe ﬁrst that (TH) is
equivalent to 1 − α(ya − xU ) ≥ θ, and this implies that p(x) ≥ θ for all x and
independently of xL, including for the case xL = ya, where the redemption curve p
has no ﬁnal constant segment. In this case we say that θ is not binding. If (TH) does
not hold, then we need to choose xL < ya since otherwise the reserve ratio would
fall short of the ﬂoor θ; we say that θ is binding. Conceptually, if at least one of
(TH) or (TL) holds, the redemption price will always be at least ¯θ, conditional on
the assumptions at the beginning of this section (in particular, the system starts
with enough reserve capitalization). This is desirable as anyone can understand this
bounding (as well as other PAMM mechanics) ahead-of-time.

Armed with Lemma 2, we can now construct the values ˆα and ˆxU(α) for any α.

We begin with ˆα. Recall that θ = 1 − θ.

Prop. 4. We have

ˆαH := 2 1−ra
ya
θ2
ˆαL := 1
2
ba−θ ya
and ˆα is continuous in the other parameters.

ˆα =



,




ra ≥ 1+θ
2
ra ≤ 1+θ
2

,

[Link to Proof]

We continue with an explicit formula for ˆxU(α). Note that, due to the way in
which we choose our parameters, we only need to consider ˆxU(α). However, no
additional eﬀort is required to obtain a formula for general α.

Prop. 5. We have

ˆxU(α) =






q

ˆxU,h := ya −
ˆxU,l := ya − ∆a

2 ∆a
α∆a ≤ 1
α ,
2α θ α∆a ≥ 1
θ − 1

2 θ2
2 θ2 .

and ˆxU(α) is continuous in α and in the other parameters.

[Link to Proof]

The technical results in this section show how the dynamic parameters α, xU , and
xL can be calculated from the current state using the anchor point. In the following
sections, we will proceed with our analysis with these rules for choosing dynamic
parameters as given.

D A Formal Treatment of Path Deﬁciency under Minting

and Fees

D.1 Extension to Fees and Minting

The P-AMM in reality will take an extended form of the setup developed thus far. In
this extended form, the redemption curve will incorporate a trading fee and there

33

will be a separate minting curve for x that moves in the reverse direction. We will
now show how the desired properties –but not path independence directly– can be
retained in this extended form.

This extended form can no longer be modeled by a single dynamical system. In-
stead, diﬀerent diﬀerential equations describe the eﬀects of increasing x (redemptions)
as opposed to decreasing x (minting). Let γ(x, b, y) ≥ 0 be the trading fee that is
imposed on redemptions. And let ϕ(x, b, y) ≥ 1 be a function describing the marginal
price of minting a new stablecoin. Notice that ϕ(x, b, y) = 1 + ε is such a function for
any ε > 0.

In the extended form, redemption actions are described by the following slightly

altered form of (1):

db(x)
dx
dy(x)
dx

= −ρ(cid:0)x, b(x), y(x)(cid:1) + γ(cid:0)x, b(x), y(x)(cid:1)

= −1.

And minting actions are described by the diﬀerent set of diﬀerential equations:

db(x)
dx
dy(x)
dx

= −ϕ(cid:0)x, b(x), y(x)(cid:1)

= −1.

(6)

(7)

As the extended system evolves diﬀerently for diﬀerent directions of change in
x, we no longer have path independence. To see this, simply consider a closed path
in x, which returns to the same starting point in x-space, but will often not return
to the same starting point in (x, b, y)-space. However, there a generalization of path
independence, called path deﬁciency, which retains many of the useful properties we
desire.

D.2 Path Deﬁciency Properties

We next show two properties analogous to path deﬁciency in CFMMs (see Angeris and
Chitra (2020)). As the P-AMM is not a CFMM, we approach this slightly diﬀerently.
For our purposes, we will characterize path deﬁciency-like results in terms of reserve
ratio curves that can be encountered along a trading path. These reserve ratio curves
are deﬁned in previous sections and visualized in Figure 6. In particular, these reserve
ratio curves are functions arising from our original system (1) that map x to a reserve
ratio r(x) parameterized by an anchor point ra = ba/ya, where we assume ¯xU, α, and
θ are ﬁxed. Without loss of generality, we will take ya = 1 so that ra = ba.

Recall that each current state is associated with a single such reserve ratio curve.
While in the case of redemptions without fees, we always remain on this reserve ratio
curve, when we add in fees and a separate minting curve, we instead may shift reserve
ratio curves as we move along a path in x.
We start with the following deﬁnitions:

• R is the set of all reserve ratio curves,

34

• r ∈ R is some initial reserve ratio curve,
• C is the set of paths in [0, 1], i.e., C = {f : [0, 1] → [0, 1] | f is continuous},
• rf,r : [0, 1] → [0, ∞) is the function returning the reserve ratio at points along
the path f ∈ C starting at the initial point (cid:0)f (0), r(f (0))(cid:1) in (x, r)-space.
Notice that rf,r sweeps away the details of (6) and (7) but is easy to see is well-deﬁned
for a given f ∈ C.

Paths in the set C are interpreted as paths for the variable x. Note that we
consider paths for x within [0, 1]. The upper bound comes from the maximum amount
that can be redeemed. It is inherently possible for more supply to be minted than
ya, and so the lower bound could conceptually be passed in reality. It is possible to
extend the results by renormalizing the system to ya = 1.

The following lemma establishes that the anchor point ra is weakly increasing

along any trading path.

Lemma 3. Let r ∈ R such that r ≤ 1 and f ∈ C. Then ra
point for each state (x, r) along the path— is non-decreasing in t.

(cid:0)f (t), rf,r(t)(cid:1) —the anchor

[Link to Proof]

This enables our ﬁrst path deﬁciency-like result in the next theorem. Consider
that we start on an initial reserve ratio curve. Moving along this curve describes the
behavior of the original path independent system along a trading path, which we
proved various desirable properties about in the previous sections. The reserve ratio
curve that we are on –independent of where we are on it– is one good measure for
the health of the system as being on a higher curve is point-wise weakly better than
being on a lower curve. The following theorem establishes that the protocol health is
weakly increasing in this way along any trading path.14

Theorem 3 (formal). Let r ∈ R such that r ≤ 1. Then for all f ∈ C and for all
t ∈ [0, 1], we have r(cid:0)f (t)(cid:1) ≤ rf,r(t).

[Link to Proof]

We now turn to our second path deﬁciency-like result. The following theorem
shows that, in settings with a proportional fee, there is no incentive for a trader to
strategically subdivide a net redemption trade into a sequence of diﬀerent trades.

14These results parallel those of path deﬁciency in CFMMs (see Angeris and Chitra (2020)). To
draw the parallel further, these and potentially further path deﬁciency results for P-AMMs may
ψ ∈ R | (cid:0)f (t), rf,r(t)(cid:1) ∈
be expressed in terms of reachable sets of reserve ratio curves S(r) =

n

o

ψ for some t ∈ [0, 1] and for some f ∈ C
that weakly contract along a path. To illustrate, Lemma 3
would express that functions in this reachable set are point-wise lower bounded by r, and that
reachable sets do not expand along a path. This may be useful in expanded contexts, such as
involving discrete trades, in which it is not obvious that two valid paths can be concatenated into a
single valid path, or settings in which reserve ratio curves are not nicely represented by anchor points.

35

Theorem 4 (formal). Let γ(·) = ερ(·) for some 0 ≤ ε < 1 and let r ≤ 1 be the
initial reserve ratio curve. Then:

1. The redemption system described in (6) is path independent within a block.

2. An individual trader in the extended system described in Section D.1 has no

incentive to subdivide a net redemption within a block.

[Link to Proof]

E Details on Eﬃcient Implementation

In this section, we discuss how to implement our mechanism on-chain. To execute a
redemption using our mechanism, we are given the current state (x, b(x), y(x)) and we
need to ﬁnd ba and ya such that b(x; ba, ya) = b(x). We can then simply integrate the
curve of marginal redemption rates, starting at x, to execute a redemption; note that
integration can easily be done analytically using Proposition 2. Recall from Section 6
that ﬁnding ya is trivial because y(x) = ya − x, so ya = y(x) + x. The main challenge
is therefore to ﬁnd the appropriate ba. By strict monotonicity (Theorem 1), ba is
unique. The proofs for this section can be found in Appendix F.3. We prove additional
technical guarantees, which are not required for the purpose of this exposition, but
may be useful when implementing our methods, in Appendix G.

In this section, we assume that the parameters α and ¯xU scale in the anchored
amount of outstanding stablecoins ya (see also Section 4). More in detail, we assume
that ¯xU = ¯xU,1 · ya and α = α1/ya, where ¯xU,1 and α1 are parameters that can be
chosen arbitrarily and that correspond to the value of ¯xU and α for ya = 1. Choosing
the parameters like this is intuitive and economically meaningful because ¯xU,1 is now
the share of “initial” (anchored) outstanding stablecoins that can be redeemed at
dollar value and α1 is minimum decay in reserve ratio relative to the share of “initial”
outstanding stablecoins that have been redeemed. Note that the minimum reserve
ratio θ remains an absolute number and is not relative to ya. As these parameters ¯xU,1
and α1 are economically meaningful, we expect that they only need to be adjusted
rarely, so that governance interventions are minimized.

If we were working under the mild computational constraints of a regular machine,
our mechanism could be implemented in a straightforward way using bipartition.
Using this method, we can ﬁnd a ba ∈ [0, ya] such that b(x; ba, ya) = b(x) ± ε, where
ε is a chosen precision. This would require log(ya/ε) evaluations of b(x; ba, ya) in
the worst case. While this is computationally unproblematic for a regular machine,
this method is far too computationally expensive to be implemented on-chain: each
evaluation of b(x; ba, ya) (for a changing value of ba) requires the re-computation of
the dynamic parameters xU and α, and it requires computing up to two square roots
(for xL and potentially for xU ). Square roots can of course only be computed using
an iterative process, which is also computationally relatively expensive. The whole
computation then has to be repeated several times until the interval of possible ba
values is small enough.

36

Fortunately, we can implement our mechanism in a much more computationally
eﬃcient way that is amenable to implementation on-chain. Our method makes use
of precomputed data that only depends on the normalized parameters. More in
detail, we will show the following theorem. We can limit our view to states where the
reserve ratio r lies in the interval (θ, 1) as our mechanism otherwise simply yields a
redemption rate of r or 1, respectively.

Theorem 7. Given is a state (x, b, y) such that 1 > b/y > θ. Let ya = y + x. We
can ﬁnd the unique ba such that b = b(x; ba, ya) using a constant number of basic
arithmetic operations and at most one square root, together with precomputed data
that only depends on the parameters ¯xU,1, α1, and θ and is independent of the state
(x, b, y). Our precomputation can be performed using a constant number of basic
arithmetic operations and one square root, and it can be veriﬁed using a constant
number of arithmetic operations and without taking any square root.

Our method proceeds in three steps: in the precomputation step, we compute
the curves of form x 7→ b(x; ba, ya = 1) that mark the threshold between the diﬀerent
cases deﬁned in Section 6: the threshold between case I and II, case II and III, and
the thresholds between cases h and l and H and L, respectively. Note that these
computations in principle only need to do once as long as the parameters ¯xU,1, α1, θ
are kept the same.

In the second step and given a state (x, b, y), we use this precomputed information
to detect the region (such as II h i) into which this state falls. Since most of the work
has already been done in the precomputation step, this step only requires a constant
number of arithmetic operations and no square roots. Finally, once we know the
region, we solve an equation of degree 1 or 2 to compute the value of ba that leads to
b. This third step may involve a square root, depending on the region.

E.1 Normalization

Recall that the precomputed information only applies to the ya = 1 case. To use it in
the region detection step, we normalize all values to ya = 1. We then run all further
computations on this normalized version and scale the resulting ba back to the original
value of ya. Formally, we exploit the following scaling property. Throughout this
section, we denote the dynamic parameters as functions of the values on which they
depend. For example, we write α(ba, ya) for the value that the dynamic parameter α
would take according to Proposition 4 at a certain (ba, ya) combination.

Lemma 4. Assume that ¯xU and α are chosen relative to ya as described above. Let
ζ > 0. Then

b(ζx; ζba, ζya) = ζb(x; ba, ya).

[Link to Proof]

The lemma immediately implies that it is enough to be able to determine ba in

the normalized case where ya = 1.

37

Theorem 8. Assume that ¯xU and α are chosen relative to ya as described above. For
some given x, b, and ya, let ba,1 be such that b(x/ya; ba,1, 1) = b/ya. Let ba = ba,1ya.
Then b(x; ba, ya) = b.

Proof. This follows immediately from Lemma 4 for ζ = 1/ya.

By Theorem 8, it is enough to consider the case ya = 1. Otherwise, given some
state (x, b, y) we can consider the scaled state (x/ya, b/ya, y/ya) (where ya := y + x),
consider the resulting ba, and return ya ·ba. Despite our normalization, in the following,
we will usually use an explicit variable for ya in the interest of clarity of the exposition.

E.2 Precomputation Step

We now discuss our precomputation step. We use the following lemma to distinguish
between cases I, II, and III.

Lemma 5. Let z ≤ ya. Let yz := ya − z. Then ˆxU = z iﬀ

ba =

(ya − α
2 · y2
z
ya − θyz + θ2 · 1
2α

if 1 − αyz ≥ θ
otherwise.

[Link to Proof]

a , xh/l

U , bH/L
via Lemma 5 such that ˆxU = ¯xU for ya = 1 and α = α.
via Proposition 3 for bI/II
via Lemma 5 such that ˆxU = 0 for ya = 1 and α = α.

, ya = 1, α = α, and xU = ¯xU.

, αH/L)

a

a

, bh/l

, xI/II
L

, bII/III
a

Algorithm 1 Precomputation step
Input: α, ¯xU, θ
Output: P := (bI/II
a
1: Calculate bI/II
2: Calculate xI/II
3: Calculate bII/III
4: Let bh/l
a
5: Calculate xh/l
U
6: Let bH/L
7: Calculate αH/L via Proposition 4 for bH/L

via Proposition 5 for bh/l

:= ya − θ2 · 1
2·α

:= ya · 1+θ
2

L

a

a

a

.

a

a , ya = 1, and α = α.

and ya = 1.

Our precomputation step is depicted in Algorithm 1. It exploits Lemma 5 as
well as other relationships to calculate all relevant thresholds between cases I / II
/ III as well as those between cases h / l and and H / L. Each of these thresholds
is determined by a speciﬁc ba value. We also compute the dynamic parameters for
each of these ba values as far as it is necessary, so that any point along the respective
threshold curve for b(x) can be quickly evaluated. The following lemma tells us that
these threshold values can be used to determine in which of the diﬀerent regions we
are. As discussed above, we only need to consider the normalized case ya = 1.

38

Lemma 6. Fix ya = 1 and let ba ∈ [0, ya) be arbitrary. Let x ∈ [0, ya] and assume that
1 > b(x; ba)/y(x) > θ. Consider the precomputed values chosen like in Algorithm 1.
Then the following hold:

iﬀ we are in case I. (b) For bI/II
a
. (c) We have b(x; ba) ≥ b(x; bI/II

a

we have α = α,
) iﬀ we are in case

1. (a) We have ba ≥ bI/II
xU = ¯xU, and xL = xI/II
I.

L

a

2. (a) We have ba ≤ bII/III

a

and xU = 0. (c) We have b(x; ba) ≤ b(x; bII/III
are in case III.

a

iﬀ we are in case III. (b) For (bII/III

) we have α = α
, α = α, xU = 0, xL = 1) iﬀ we

a

3. Assume that we are in case II. (a) We have ba ≥ bh/l
a

iﬀ we are in case h. (b) For
U , and xL = ya. (c) We have b(x; ba) ≥ b(x; bh/l
a )

bh/l
a we have α = α, xU = xh/l
iﬀ we are in case h.

4. Assume that we are in case III. (a) We have ba ≥ bH/L

iﬀ we are in case
) we have α = αH/L, xU = 0, and xL = ya. (c) We have

a

H. (b) For (bH/L
b(x; ba) ≥ b(x; bH/L

a

a

) iﬀ we are in case H.

[Link to Proof]

Regarding the runtime properties of the precomputation step, we receive:

Prop. 6. Algorithm 1 only requires a constant number of basic arithmetic operations
and the computation of at most one square root. Furthermore, correctness of the
values computed by algorithm 1 can be veriﬁed using a constant number of basic
arithmetic operations and no square root.

[Link to Proof]

E.3 Region Detection

Lemma 6 provides a way to use the precomputed values to detect in which region
we are along the I-III and h/l and H/L dimension. This can be done based on only
the current state (x, b, y) and without any knowledge of ba. For example, to tell case
I and II apart, by part (1c) of the lemma, we only need to compare the value b(x)
(which we know) to the value b(x; bI/II
). This latter value can be easily computed
a
because we also know the values of xU , α, and xL corresponding to bI/II
by part
(1b) of the lemma. The same reasoning applies to the other items. Algorithm 2
formalizes this idea and adds an additional method that allows us to also tell case i–iii
apart. In eﬀect, Algorithm 2 allows us to fully reconstruct the region of a given point
(x, b, y) without knowledge of ba and only with a constant number of basic arithmetic
operations (and in particular without computing a square root).

a

Theorem 9. Algorithm 2 is correct and only requires basic arithmetic operations,
and only a constant number of them.

[Link to Proof]

39

Algorithm 2 Region detection. We use “emit” as a shorthand to denote that the
algorithm outputs that we are in a particular case without stopping execution of the
function.
Input: α, ¯xU, θ, (x, b, y) such that θ < b/y < 1 and ya := y + x = 1; P precomputed

using Algorithm 1

Output: The region in which (x, b) lies.
1: if b ≥ b(x; bI/II
Emit case I
2:
if x ≤ ¯xU then
Emit case i

3:

4:

a

, ya = 1, α = α, xU = ¯xU, xL = xI/II

) then

L

5:

6:

7:

8:

else if b/y ≤ 1 − α(x − ¯xU) then

Emit case ii

else

Emit case iii

a

end if

9:
10: else if b ≥ b(x; bII/III
Emit case II
11:
if b ≥ b(x; bh/l
Emit case h
if y − b ≤ α

14:

13:

12:

2 · y2 then

Emit case i

, ya = 1, α = α, xU = 0, xL = 1) then

a , ya = 1, α = α, xU = xh/l

U , xL = 1) then

15:

16:

17:

18:

19:

20:

21:

22:

23:

24:

25:

29:

30:

31:

32:

else

Emit case ii

end if

else

Emit case l
if b − θ y ≥ θ2
Emit case i

2α then

else

Emit case ii

end if

end if

26:
27: else
28:

Emit case ii
if b ≥ b(x; bH/L
Emit case H

a

else

Emit case L

end if

33:
34: end if

40

, ya = 1, α = αH/L, xU = 0, xL = 1) then

E.4 Reconstructing the value of ba
Given suﬃcient knowledge about the region, it is now conceptually straightforward
(though mathematically somewhat inconvenient) to reconstruct the precise value of
ba by solving a linear or quadratic equation. This is captured in Algorithm 3.

Theorem 10. Algorithm 3 is correct and only requires a constant number of basic
arithmetic operations together with at most one square root.

[Link to Proof]

E.5 Full Implementation

Algorithm 4 shows the full implementation of our redemption mechanism and il-
lustrates how our reconstruction algorithm is applied. We receive the following
consistency result, which states that going to some state and then performing re-
demption over some amount using Algorithm 4 is the same as going to the state
corresponding to the overall redemption amount directly. This is because Algorithm 4
correctly reconstructs the original anchor point (ba, ya) and then simply continues on
the corresponding curve of marginal redemption prices. This is another form of path
independence (see also Section 7). The proof is immediate by the preceding theorems
and is omitted.

Corollary 2. Fix values for α1, ¯xU,1, θ. Let ba, ya be such that 1 > ba/ya > θ. Let
x ∈ [0, ya] and let X ∈ [0, ya−x]. Let (x0, b0, y0) be the new state as of Algorithm 4 when
applied to the parameters, the state (x, b(x; ba, ya), y(x; ba, ya)), and the collection
of precomputed values as of Algorithm 1 for the parameters. Then x0 = x + X,
b0 = b(x + X; ba, ya), and y0 = y(x + X; ba, ya).

F Proofs

F.1 Technical Lemmas

Prop. 2.
Proof. The ﬁrst equality is just the deﬁnition. For the second equality, ﬁrst assume
that x ≤ xU . Then p(x0) = 1 ∀x0 ≤ x and thus the equality holds. For the second
case, we have

ba −

Z x

0

p(x0)dx0 = ba − xU −

Z x

xU

1 − α(x0 − xU )dx0

1 − αx0 dx0

Z x−xU

0

= ba − xU −
= ba − xU − (x − xU ) + α
2
= ba − x + α
2

(x − xU )2

(x − xU )2

41

Algorithm 3 Reconstruction of ba
Input: α, ¯xU, θ, (x, b, y) such that θ < b/y < 1 and ya := y + x = 1; the region of

(x, b)

Output: ba such that b(x, ba, ya = 1) = b
1: Let r = b/y.
2: if case i applies then
ba = b + x
3:
4: else if case I applies then
if case ii applies then
5:
ba = b + x − α
2

(x − ¯xU)2

6:

else

ba = ya − (ya − ¯xU)(1 − r) + 1
2α

end if

9:
10: else if case II applies then
11:

if case h applies then

(cid:16) 1
α · (1 − r) + 1

2 · y

Let ∆a := α
2 ·
ba = ya − ∆a

else

Let p0 := θ · ( θ
2α
Let d := θ2 · 2
Let ∆a := p0 −
ba = ya − ∆a

+ y)
α · (b − θ y)
d

√

end if

19:
20: else
21:

if case H applies then
Let ∆a := y−b
1− x2
y2
a

.

ba = ya − ∆a

else

Let p0 := 1
(y − b + θya)
2
Let q := (y − b)θya + 1
Let ∆a := p0 − pp02 − q
ba = ya − ∆a

4 θ2x2

7:

8:

12:

13:

14:

15:

16:

17:

18:

22:

23:

24:

25:

26:

27:

28:

(1 − r)2

. Now case iii applies.

. Now case ii applies.

(cid:17)2

. Now case l applies

. Now case III ii applies.

. Now case L applies.

end if

29:
30: end if

42

Algorithm 4 Full implementation of the redemption mechanism
Input: α1, ¯xU,1, θ, the current state (x, b, y), and a desired amount of redemptions
X ≤ y; the collection of precomputed values P calculated by Algorithm 1 for the
given parameters.

Output: A new state (x0, b0, y0) after the amount of X has been redeemed. The

diﬀerence b0 − b is paid out as the redemption amount.

1: x0 := x + X; y0 := y − X
2: if X = 0 then
b0 := b
3:
4: else if b/y ≥ 1 then
b0 := b − X
5:
6: else if b/y ≤ θ then
7:
8: else
9:

b0 := b − b/y · X

point.

10:

11:

12:

Let ba := ba,N · ya.
b0 := b(x + X; ba, ya)

13:
14: end if

Let ya := y + x. Let xN := x/ya, bN := b/ya, yN := y/ya.
Apply Algorithm 2 to (xN , bN , yN ) and P to determine the region of this

Apply Algorithm 3 to (xN , bN , yN ) and the region information computed in

the previous step to determine ba,N such that b(xN ; ba,N , ya = 1) = bN .

43

Finally, if xL ≤ x, we have

b(x) = b(xL) −

Z x−xL

0

rL dx0 = rL(ya − xL) − rL(x − xL) = rL(ya − x).

Prop. 3.
Proof. Consider the deﬁnition of pU (x), and the implied value for b(x), for the case
xU ≤ x ≤ ya. Let x0 = x − xU and assume ﬁrst that x < ya. We have

pU (x) = r(x)
1 − αx0 = ba − (xU + x0) + α/2x02

yU − x0
(yU − x0)(1 − αx0) = ba − xU − x0 + α

2 x02

α
2 x02 − αyU x0 + ya − ba = 0

x0 = yU ±

q

q

x = ya ±

U − 2/α(ya − ba)
y2
U − 2/α(ya − ba).
y2

⇔

⇔

⇔

⇔

⇔

Note that, if the discriminant is positive, then the “+” solution is > ya and thus not
acceptable for xL, so we only need to consider the “-” solution. Obviously, this exists
iﬀ (5) holds. Assuming that (5) does hold, we obviously have x ≤ ya and furthermore

⇔

x = ya −

yU −

q

q

U − 2/α∆a > xU
y2
U − 2/α∆a > 0,
y2

which is true because the radicand is < y2
U
Thus, this x serves the role of xL := x, and it is unique by the above.

because ∆a > 0 by our basic assumptions.

If for the above choice of xL we have xL < ya, then the identity p(xL) = r(xL)
follows by construction. Consider now the case where xL = ya. This is the case iﬀ
the above discriminant is 0, i.e., iﬀ α = 2 ya−ba
(ya−xU )2 . In this case, it is easy to see that
b(xL) = y(xL) = 0 and we can use L’Hospital’s rule to compute
= −1 + α(x − xU )
−1

ba − x + α/2(x − xU )2
ya − x
so the identity rL = p(xL) still holds.

rL = lim
x→ya

= lim
x→ya

b(x)
y(x)

The formulas for rL and bL now simply follow from the fact that rL = p(xL) and

bL = rL · y(xL).

Finally, consider the case where (5) does not hold and where we choose xL := ∞

to deﬁne p. Then by applying Prop. 2 to x := ya we receive

b(ya) = ba − ya + α
2
where the inequality is by the assumption that (5) does not hold. By continuity of b,
there exists x < ya such that b(x) = 0.

(ya − xU )2 < 0,

44

= 1−α(ya−xU ) = p(xL),

Lemma 2.
Proof. By Proposition 3 we have that rL ≥ θ iﬀ

⇔

⇔

⇔

or

1 − α

(cid:18)

yU −

1 − α(xL − xU ) ≥ θ
q

(cid:19)

U − 2/α∆a
y2

≥ θ

q

U − 2/α∆a ≥ αyU − θ
y2

α

αyU − θ ≤ 0
(cid:17)

y2
U − 2/α∆a

≥ (αyU − θ)2 .

α2 (cid:16)

The conclusion now follows via another simple algebraic transformation.

Prop. 4.
Proof. It is easy to see that the transition is continuous and thus well-deﬁned; more
in detail, in the edge case ra = 1+θ
2

, we have ˆαH = ˆαL = θ /ya.

By the discussion at the beginning of this section, we only need to consider xU = 0.
ˆα is the maximal α such that (5) holds and one of (TL) or (TH) hold (with xU = 0).
Note that (5) alone puts a bound on α and the right-hand side of (5) is equal to ˆαH
for xU = 0. Thus, whenever it is possible to choose α = ˆαH , this is minimal. We can
choose α = ˆαH if (TH) holds for ˆα, i.e., if

⇔

2

1 − ra
ya

· ya ≤ θ

ra ≥

1 + θ
2 .

The equivalence immediately follows from the deﬁnition of θ = 1 − θ. If this inequality
does not hold, then there is no α that satisﬁes both (5) and (TH). (observe that the
two limit α in diﬀerent directions!)
Assume next that ra ≤ 1+θ
2

. Then α must be chosen minimal such as to satisfy
(5) and (TL). The minimal α satisfying (TL) with xU = 0 is obviously ˆαL. It remains
to show that this also satisﬁes (5), i.e., that

1
2

⇔

⇔

≥ 2 ya − ba
y2
a

θ2
ba − θ ya
1
θ2
2
ra − θ
1
4 θ2 ≥ (1 − ra)(ra − θ).

≥ 2(1 − ra)

45

The equivalences are by deﬁnition of ra = ba/ya and straightforward transformation.
Let ζ = 1+θ
2 − ra. By assumption, ζ ≥ 0 and we have 1 − ra = θ /2 + ζ and
ra − θ = θ /2 − ζ. Thus, the above inequality is equivalent to

1

4 θ2 ≥ (θ /2 + ζ)(θ /2 − ζ) = θ2

4 − ζ 2,

which is obviously true.

Prop. 5.
Proof. We proceed similarly to Proposition 4. Again, it is easy to see that in the
edge case α∆a = 1
. We need to choose xU such as
to satisfy (5) and one of (TH) or (TL), this time without assuming xU = 0 of course.
(5) is equivalent to

2 θ2 we have ˆxU,h = ˆxU,l = ya − θ

α

xU ≤ ya −

s
2

∆a
α

.

If we can choose xU equal to the right-hand side such that (TH) is satisﬁed for

this choice, then this is optimal. This is the case if

s

2

∆a
α

α ·

≤ θ

α∆a ≤

1
2 θ2 .

⇔

If this does not hold, no xU satisﬁes both (5) and (TH).

Assume now that α∆a ≥ 1

holds iﬀ

2 θ2. We need to satisfy ((5) and) (TL). Clearly, (TL)
1
2α

θ2 = ya −

θ = ˆxU,l .

∆a
θ

1
2α

−

−

xU ≥

ba − θ ya
θ

It remains to check that xU = ˆxU,l satisﬁes (5). This is the case iﬀ

(cid:18)

(cid:18)

ya −

ya −

(cid:18) ∆a
θ

+

y2
U ≥ 2

∆a
α
∆a
α

∆a
θ
1
2α
(cid:18) ∆a
θ

−

(cid:19)(cid:19)2

1
2α

θ

(cid:19)2

− 2

θ

≥ 2

≥ 0

∆a
α
(cid:19)2

−

1
2α

θ

≥ 0,

which is obviously true. The last line follows using the binomial formulae since
2 ∆a
α

= 2 · 2 · ∆a

θ · 1

2α θ.

46

F.2 Main Results

Proposition 1.
Proof. In case II h, we have xU = ˆxU = ˆxU,h and thus (by the proof of Proposition 5)
Inequality (5) holds with equality. It follows immediately from Proposition 3 that
this implies xL = ya. Likewise in case III H. In case II l, xU = ˆxU = ˆxU,l and thus
(by the proof of Proposition 5) (TL) holds with equality. By the proof of Lemma 2,
this immediately implies rL = θ. Likewise for case III L.

Corollary 1.
Proof. By Proposition 1, since we’re in case II or III we have xL = ya or rL = θ. Since
we’re in case iii, xL ≤ x < ya and thus xL = ya is not possible. We must therefore
have rL = θ. And, again since x ≥ xL, r(x) = rL.

Theorem 1.
Proof. If S ⊆ [0, ya] × [0, ya] is a set of (ba, x) pairs, deﬁne the ba-interior of S as the
set {(ba, x) ∈ S | ∃ε > 0 : (ba + ε, x), (ba − ε, x) ∈ S}. It suﬃces to show the following:
for any point (ba, x) that lies within the ba-interior of any of the sets of pairs (ba, x)
deﬁned by the following (topologically closed) conditions, if r(x; ba) > θ, then we have

db(x; ba)
dba

> 0.

We will perform case distinction in such a way that this derivative always exists.
Assume that r(x; ba) > θ. The statement is easy to see in the following cases:
Case i: This case is trivial because here, b(x; ba) = ba − x and so db(x;ba)
= 1 > 0.
Case I ii and I iii: Here the statement follows immediately from Prop. 2 and
Prop. 3 Part 3. Note that whenever we are in case I, the parameters α = α and
xU = ¯xU are constant.

Case II iii and III iii: By Corollary 1, we do not need to discuss these cases.
It remains to show that the statement holds for case II ii and III ii, which requires
some calculation. We distinguish four cases: II h ii, II l ii, III H ii, and III L ii.
We combine Prop. 2 with Propositions 5 and 4, respectively, to compute the partial
derivatives.

dba

47

Case II h ii: Here we have xU = ˆxU,h and

db(x; ba)
dba

=

d
dba
= 1 + α

(cid:20)
ba − x + α
2

(x − ˆxU,h(ba))2

(cid:21)

2 · 2(x − ˆxU,h(ba)) · (−1) ·

= 1 − α(x − ˆxU,h(ba)) ·

d
dba

d
dba
s

ˆxU,h(ba)


2 ya − ba
α




ya −

= 1 − α(x − ˆxU,h(ba)) · (−1) ·

= 1 −

x − ˆxU,h(ba)
ya − ˆxU,h(ba) > 0.

1
2

q

1

2 ya−ba
α

· (−

2

α

)

The last equality is by deﬁnition of ˆxU,h(ba) and the inequality is because x < ya and
x, ya > ˆxU,h(ba) by assumption.

Case II l ii: Here we have xU = ˆxU,l and

d
dba

ˆxU,l(ba) =

d
dba

(cid:20)
ya −

∆a
θ

−

1
2α

(cid:21)

θ

=

1

θ

.

Thus,

⇔

= 1 − α(x − ˆxU,h(ba))

db(x; ba)
dba
p(x; ba) = 1 − α(x − ˆxU,h(ba)) > θ

> 0

1

θ

This is true because x ≤ xL by assumption and thus p(x) ≥ r(x) and we have r(x) > θ
by assumption.

Case III H ii: In this case we have xU = 0 and α = ˆαH (ba) and we have

db(x; ba)
dba

=

d
dba
= 1 +

= 1 +

= 1 −

ˆαH (ba)
2

(cid:21)

x2

(cid:20)
ba − x +
1
d
2 x2
dba
1
2 x2 · 2 ·
(cid:19)2
(cid:18) x
ya

> 0

ˆαH (ba)
1
(cid:19)
(cid:18)
y2
a

−

since x < ya.

Case III L ii: Here we have

d
dba

ˆαL(ba) =

1
2 · θ2 ·(−1) ·

(cid:16)

1

ba − θ ya

= −

(cid:17)2

1
2

(cid:16)

θ2

(cid:17)2

ba − θ ya

= − ˆαL(ba)

1

ba − θ ya

,

48

where the last equality is by deﬁnition of ˆαL(ba). Therefore, we have (writing just α
for ˆαL(ba) in the interest of brevity)

db(x; ba)
dba

= 1 +

(cid:18)

1
2 x2 ·
1
2 x2

1

(cid:19)

−α

ba − θ ya
1

.

ba − θ ya

= 1 − α ·

To see that this is positive, ﬁrst note that, by Proposition 1 and Proposition 3,
θ = rL = 1−αxL and thus xL = θ /α. Since we’re in case ii and we have r(x) > θ = rL,
we must have x < xL = θ /α and thus

1 − α ·

1
2 x2

1

ba − θ ya

> 1 − α ·

1
2

= 1 −

1

α

1
2

·

as required. This concludes the proof.

θ2
α2

1

ba − θ ya
θ2
ba − θ ya

= 1 −

1

α

· α = 0

Theorem 2.
Proof. Let (x0, b0, y0) be a solution to the initial value problem at S0. Note that
x0, b0, y0 are functions of x. Then the functions bX (x) := b0(X + x) (and analogously
for y) form the solution to the IVP at SX . To see this, note that they satisfy the
diﬀerential equations (because (x0, b0, y0) do and translation by X does not aﬀect
the derivatives) and they satisfy the initial values by choice of SX . We now have
bX,Y = bX (Y ) = b0(X + Y ) = bX+Y , and likewise for the other two. This is easy
to see for y because it is simply x plus a constant; however our argument does not
depend on this fact. Overall, SX,Y = SX+Y . For the redemption amounts, we now
have PX + PX,Y = (b0 − bX ) + (bX − bX,Y ) = b0 − bX,Y = b0 − bX+Y = PX+Y .

Lemma 3.
Proof. Separate into two cases: (i) when df
dt < 0. These
correspond to the x value increasing or decreasing respectively along the path f .
Suppose we are at the current state (f (t), rf,r(t)) and that this point is on the reserve
ratio curve ˆr ∈ R. In (i), x is increasing (redemption operation), and so (6) applies.
Taking derivative of r(x),

dt ≥ 0, and (ii) when df

dr
dx

=

db

dx y(x) + b(x)
y2(x)

= r(x) − ρ(x, b(x), y(x)) + γ(x, b(x), y(x))
y(x)

.

49

The derivative is greater (in this case less negative) when γ > 0. When γ = 0, we
have the system (1), and the reserve ratio follows ˆr(x).

In (ii), x is decreasing (minting operation), and so (7) applies. Taking derivative

of r(x),

dr
dx

= r(x) − ϕ(x, b(x), y(x))
y(x)

.

Since ϕ ≥ 1, we have ϕ ≥ ρ. And so the derivative is greater than the corresponding
derivative in (1), which would keep us on the reserve ratio curve ˆr.

In both cases, the path does not bring us to a region below ˆr in (x, r) space. Since
Theorem 1 gives us that ra (via ba) is monotonic in r, it must be non-decreasing
along this path.

Theorem 3 (formal).
Proof. From Lemma 3, we know that ra is weakly increasing along the path. Since
reserve ratio curves are point-wise non-decreasing in their parameter ra, the result
follows immediately.

Theorem 4 (formal).
Proof. This setup is equivalent to changing the RHS of (1) to (1 − ε)ρ(·), which
is a constant scaling. From linearity of integration, the only thing that changes
structurally about the system is the hyperparameters (static parameters), which can
be thought of as mapping in the following ways:

• a thus far implicit parameter specifying the $1 target 7→ (1 − ε) target,
• α 7→ (1 − ε)α,
• θ 7→ (1 − ε) θ.

A useful interpretation is that this scaling can be eﬀectively ‘reversed’ by normalizing
the system (in this case the redemption system in isolation) back to a $1 target. The
underlying hyperparameters eﬀectively shift slightly from the reverse scaling, but
we are left with the same underlying structure and machinery. Since we proved the
above results for all hyperparameter values –and it is simple to add in the thus far
implicit hyperparameter specifying the target through this normalization argument–
the results still stand even though the hyperparameters shift. In particular, we have
retained path independence for the redemption system in (6).

To show the second result of the theorem, we need to add in the minting process
as described in Section D.1. Consider a sole trader interacting with the system. If
they desire a net redemption from the protocol, then by the path independence of
the redemption curve, there is no incentive to subdivide the redemptions into several
smaller redemptions. The remaining possibility is that the trader subdivides the
net redemption into a sequence of redemptions and minting that nets to the desired

50

redemption. It is simple to see that this is not proﬁtable for two consecutive mint
and redeem trades since the integrands (1 − ε)ρ(·) ≤ ϕ(·) in this region (reserve ratio
≤ 1). In words, this is not proﬁtable because the trader must pay a non-negative
spread between minting and redeeming in backtracking in a path in x, and so it
is more proﬁtable not to backtrack (it is always better to cancel out a mint with
a redemption). From a simple induction then, the best option for the trader is to
choose the net redemption desired in aggregate.

F.3 Proofs regarding Implementation (Appendix E)

Lemma 4.
Proof. The lemma follows from the fact that all dynamic parameters and the input
and output of the function p scale in ζ. More in detail, the statement follows from
the following observations.

• We have α(ζba, ζya) = 1/ζ · α(ba, ya). To see this, note that ra(ζba, ζya) =
ra(ba, ya) and consider Proposition 4 to see that ˆα(ζba, ζya) = 1/ζ · ˆα(ba, ya).
Note further that α(ζya) = α1 · 1/(ζya) = 1/ζ · α(ya) by choice of α.

• Similarly, we have xU (ζba, ζya) = ζxU (ba, ya). To see this, note that ∆a(ζba, ζya) =
ζ∆a(ba, ya) and apply the preceding statement on α to Proposition 5 to receive
that ˆxU(ζba, ζya) = ζ ˆxU(ba, ya). Also note that ¯xU(ζya) = ¯xU,1ζya = ζ ¯xU(ya)
by choice of ¯xU.

• It is now easy to see that that xL(ζba, ζya) = ζxL(ba, ya) and rL(ζba, ζya) =
rL(ba, ya) using Proposition 3 and then one can directly verify the statement of
the lemma using Proposition 2.

Lemma 5.
Proof. We distinguish cases h and l. It is easy to see that

ˆxU,h = z

ˆxU,l = z

⇔

⇔

ba = ya −

α
2 y2

z

ba = ya − θyz + θ2 ·

1
2α

.

By plugging the above formulas for ba into the condition α∆a ≤ 1
cases h and l), we receive by simple algebraic transformations:

2 θ2 (which deﬁnes

Case h applies ∧ ˆxU,h = z
Case l applies ∧ ˆxU,l = z

⇒

⇒

1 − αyz ≥ θ
1 − αyz ≤ θ .

This implies the statement because exactly one of the cases on the right-hand side
(or both in case of equality) must be satisﬁed.

51

a

Lemma 6.
Proof. 1. First note that bI/II
always exists because for ba → 1, we will eventually
arrive in case I. By construction, both case I and II hold at bI/II
. Statement (a)
now follows by monotonicity of the choice of parameters. Statement (b) follows by
construction because case I applies at bI/II
. Statement (c) follows from statement (a)
because, by strict monotonicity (Theorem 1), b(x; ba) ≥ b(x; bI/II
The arguments for the other constructions are analogous.
and bH/L
The equations for bh/l
a
a

immediately result from Propositions 5 and 4,
respectively, by converting the conditions distinguishing their respecitive cases into
equalities.

) iﬀ ba ≥ bI/II

a

a

a

a

.

Prop. 6.
Proof. The statement regarding operations is obvious. The algorithm requires the
computation of one square root, in line 2. Note that no square root is required for the
computation of xh/l
because the calculation of ˆxU for case l can be applied by choice
U
of bh/l
a . Candidate values for these numbers can be easily veriﬁed without taking a
square root. To verify the only non-trivial value xI/II
, it is suﬃcient to check whether
p(x; bI/II
, ya = 1, α = α, xU = ¯xU) = r(x; bI/II
, ya = 1, α = α, xU = ¯xU), which does
a
not require a square root.

L

a

Theorem 9.
Proof. The statement regarding operations is obvious. Note in particular that output
values of the function b are only ever calculated while providing ﬁxed values for the
dynamic parameters α, xU , xL. Correctness of detection of cases I–III and h/l and
H/L immediately follows from Lemma 6.

It remains to show that cases i–iii are detected correctly. We go through the

diﬀerent cases one-by-one.

First assume that (x, b, y) lies in case I. Obviously we’re in case i iﬀ x ≤ xU = ¯xU.
Assume now that we are in case I but not in case I i. By choice of xL and deﬁnition
of the regions ii and iii, we are in region ii iﬀ r ≤ pU (x), where pU (x) is deﬁned in
(4). The expression pU (x) implicitly depends ba via the choice of α and xU . However,
since we are in region I, we know that α = α and xU = ¯xU. Furthermore, x ≥ xU
and thus pU (x) = 1 − α(x − ¯xU). Therefore, line 5 appropriately checks the condition
r ≤ pU (x).

Assume now that (x, b, y) does not lie in case I. Case iii is impossible in case II or
III by Corollary 1. Case i is further trivial in case III because xU = 0 in this case.
Thus, these cases do not have to be checked. It remains to correctly distinguish case
i and ii given that we are in case II.

52

Now assume that (x, b, y) lies in case II h. It lies in case i iﬀ x ≤ xU = ˆxU,h =
q
, where the last equality follows from Proposition 5 and the fact that we

ya −
are in case II h. It is easy to see that this is equivalent to

2 ∆a
α

∆a ≤

α
2 y2.

(8)

Line 14 checks this condition, but with ∆a = ya − ba replaced by ∆ := y − b. We show
that the two conditions are equivalent, given that we are in case II h. First, note that

∆a − ∆ = b − (ba − x) =

(0
α
2

(x − xU )2

in case i
in case ii.

In any case, ∆a − ∆ ≥ 0 and thus ∆ ≤ ∆a. Therefore, (8) implies line 14.
For the other direction, assume that (8) does not hold, so that ∆a > α

2 y2 and we

are in case ii. We have, via the above, that

∆ = ∆a −

α
2

(x − xU )2 = ∆a −

α
2

 r 2
α

!2

∆a − y

= ∆a −

> αy2 −

r 2
α

∆ay + α

2 y2

!

= α

r 2
α

∆ay −

α
2 y2

∆a − α
2 y2 = α

α

2 y2,

where the last line follows by assumption.

Assume ﬁnally that (x, b, y) lies in case II l. It lies in case i iﬀ x ≤ xU = ˆxU,l =
, where the last equality again follows from Proposition 5 and the fact

ya − ∆a
that we are in case II l. This is equivalent to

θ − θ

2α

Γa := ba − x − θ y ≥

θ2
2α

.

(9)

This follows by simple transformation, noting that θy − ∆a = Γa. Line 21 checks
this condition, but with Γa replaced by Γ := b − θ y. Again, we show that the two
conditions are equivalent, given that we are in case II l. For the ﬁrst direction of the
equivalence, note that Γa − Γ = ∆ − ∆a ≤ 0 and thus Γa ≤ Γ and (9) implies line 21.
and we

For the other direction, assume that (9) does not hold, so that Γa < θ2
2α

are in case ii. Observe that

x − xU = x − ya +

∆a
θ

+ θ
2α

=

1

θ

θ2
2α

!

+ ∆a − θy

=

1

θ

θ2
2α

!

− Γa

.

53

We thus have

Γ = Γa + ∆a − ∆ = Γa + α
2

(x − xU )2 = Γa + α
2θ2

!2

θ2
2α

− Γa

= Γa + θ2
8α
1
θ2
2 ·
2α

<

+

1
2

−

1
4 ·

Γa + α
2θ2
1
θ2
4 ·
2α

+

Γ2
a
θ2
2α

=

1
2
= θ2
2α

.

Γa + θ2
8α

+ α
2θ2

Γ2
a

Theorem 10.
Proof. The statement regarding operations is obvious. Towards correctness, all
calculations result from Propositions 2, 3, 4, and 5, by replacing the value of α
and xU (and xL in case of case I iii) into the equation for b(x) from Proposition 2.
Within each region, this yields a smooth equation (i.e., without a case distinction or
a maximum/minimum) that has degree 1 or 2 in ba can therefore be solved for ba
easily.

The only part that requires further discussion are the equations for ∆a in cases II
l ii and III L ii. These calculatinos result from a quadratic equation each, which has
two solutions (unless the radicand is zero). We show why the equation always has a
solution and only the respective chosen solution is possible as a choice of ∆a.
First consider case II l ii. Here we have α = α, xU = ˆxU,l = ya − ∆a
θ − 1

2α θ, and
2 θ2. Replacing this into the equation for b(x) in Proposition 2 for case ii

α∆a ≥ 1
yields the following.

b = ba − x + α
2

(cid:18)

x − ya +

∆a
θ

+

(cid:19)2

1
2α

θ

⇔

0 = ∆2

a − 2θ¯γ∆a +

2θ2
α

(y − b) + θ2γ2,

2α − y and ¯γ := θ

where γ := θ
algebraic transformation. Let p0 = θ¯γ and q = 2θ2
α
formula, the solutions to this equation are

+ y. The second line follows by straightforward
(y − b) + θ2γ2. By the quadratic

2α

∆a = p0 ±

q

p02 − q = p0 ±

√

d,

where d = θ2 2
(b − θ y) and the second equality again follows by simple algebraic
α
transformation. Note that d > 0 since, by assumption, b/y > θ, so the equation has
two distinct solutions. Algorithm 3 chooses the “−” solution. We show that the “+”
solution to the equation is not a feasible value of ∆a. To see this, assume towards
=: θ(γ + δ). Note that
γ +
a contradiction that ∆a = p0 +

2/α(b − θ y)

d = θ

q

√

(cid:18)

(cid:19)

54

δ > 0 because d > 0. Then

xU = ya −

∆a
θ

= ya − γ − δ −

−

θ
2α
θ
2α
+ y − δ −

= ya −

θ
2α

Therefore,

θ
2α

= x −

θ
α

− δ.

ρ(x) = 1 − α(x − xU ) = 1 − α( θ
α
= 1 − θ − αδ = θ −αδ < θ .

+ δ)

Contradiction to case ii and choice of xL.

Next consider case III L ii. We have α = 1
2

Again, replacing this into the equation from Proposition 2 yields:

θ2
ba−θ ya

and xU = 0, and ra ≤ 1+θ
2

.

b = ba − x +

1
2

1
2 ·

θ2
ba − θ ya
a − (y − b + θya)∆a + (y − b)θya +

x2

0 = ∆2

1
4 x2θ2

⇔

Let p0 = 1
2

(y − b + θya) and q = (y − b)θya + 1
4 x2θ2. Then
√

∆a = p0 ±

d,

where d := p02 − q = 1
4
towards a contradiction that ∆a = p0 +

√

d. Then

(cid:16)(b + x − θ ya)2 + θ2x2(cid:17). We trivially have d > 0.15 Assume

∆a ≥ p0 +

r 1
4

(b + x − θ ya)2

1
2

(b + x − θ ya)

=

= p0 +
1
2
1
2

=

(cid:16)
y − b + θya + b + x − θ ya

(cid:17)

(cid:16)
ya + θya − θ ya

(cid:17) =

1
2 · 2θya = θya.

For the ﬁrst equality, note that by assumption ba ≥ θ ya and b ≥ ba − x (since b arises
from ba by redeeming at a rate ≤ 1), so b + x ≥ ba ≥ θ ya, and thus the operand of
the square is non-negative.

Now, since ya − ba = ∆a ≥ θya, we equivalently have ba ≤ θ ya, i.e., ra ≤ θ.

Contradiction to non-triviality.

15Note that we trivially always have d ≥ 0. If d = 0, then x = 0 and we must have 0 = b + x − θya =

b − θy and thus b/y = θ; contradiction to the assumption of the algorithm.

55

G Additional Technical Guarantees

The following technical guarantees may be useful for implementation, e.g., to un-
derstand error conditions or the data types required to store certain values. They
are essentially redundant but stated explicitly here for additional clarity. Note that
numerical errors in any implementation can lead to slight violations of these properties
in practice even though they are mathematically guaranteed.

The following lemma shows that Proposition 3 can be safely used to store xL in

an unsigned integer of bounded width.

Lemma 7. Assume that ba < ya, ra > θ, and let xU ≤ ya and α > 0 be arbitrary.
Assume that Inequality (5) holds. Then the formula for xL in Proposition 3 is
well-deﬁned and 0 ≤ xL ≤ ya. Speciﬁcally, we have:

(ya − xU )2 −

r

(ya − xU )2 −

ya −

2

α
2

α

(ya − ba) ≥ 0

(ya − ba) ∈ [0, ya]

Proof. The ﬁrst inequality immediately follows from (5). Towards the second inequal-
ity, the expression is obviously ≤ ya. To see that it is ≥ 0, note that this is equivalent
to

⇔

r

ya ≥

(ya − xU )2 −
2

a ≥ (ya − xU )2 −
y2

α

2

(ya − ba)

α
(ya − ba)

and this inequality obviously holds since y2

a ≥ (ya − xU )2.

The following lemma shows that Proposition 5 can be safely used to store xU
in an unsigned integer of bounded width if α is chosen appropriately. We do not
consider the caps ¯xU and α explicitly here; these only make the bounds on xU tighter.

Lemma 8. Assume that ba < ya and ra > θ and let α ≥ ˆα be arbitrary where
ˆα is like in Proposition 4. Then for the formula for ˆxU in Proposition 5 we have
0 ≤ ˆxU(α) ≤ ya.

Proof. It follows immediately from the formulas that ˆxU,h(α) < ya ∀α > 0.

It remains to show that ¯xU(α) ≥ 0. By construction (see the proof of Proposition 4),
ˆxU(ˆα) = 0. Furthermore, ˆxU(α) is monotonically increasing in α. To see this, note
that the expressions ˆxU,h and ˆxU,l are both monotonically increasing as functions of
α. Continuity of ˆxU(α) (see Proposition 5) implies that ˆxU(α) as a whole must be
monotonically increasing.

Remark 2. In general (if α is not chosen according to Proposition 4 but is arbitrary),
2 θ2, so
we can have ˆxU(α) < 0. To see this, consider the limit α → 0. Then α∆a ≤ 1
ˆxU(α) = ˆxU,h = ya −

2 ∆a

q

α → −∞.

56

The following lemma shows that, to ensure that the boundary conditions of our
method hold, it is enough to check the reserve ratio b/y at the beginning of any
redemption.

Lemma 9. Consider Algorithm 4 and assume that θ < b/y < 1. Consider the values
ba and ya computed by the algorithm. Then also θ < ba/ya < 1.

Proof. By construction, if there is a ba with θ < ba/ya < 1 such that b(x; ba, ya) = b,
then the algorithm determines this ba and in particular it lies in the interval (θ, 1) as
required.

Existence (and, in fact, uniqueness) of this ba can be seen explicitly as follows. Fix
x and y and note that this ﬁxes ya = y + x. Consider the function f (ba) := b(x; ba, ya).
We need to show that there is a unique ba ∈ (θ ya, ya) such that f (ba) = b. This is
implied by the following facts: f is strictly monotonic in ba in the region of those ba
values where f (ba)/y ∈ (θ, 1) (see Theorem 1); f is continuous (see the propositions
in Appendix C); f (ba) → y for ba → ya; and f (ba) → θ y for ba → θ ya. We explicitly
prove the last two statements.

For ba → ya, ﬁrst note that we eventually have α = α and xU = ¯xU constant
(propositions 4 and 3) and furthermore xL → xU and rL → 1 (Proposition 3). Now,
via Proposition 2, it is easy to see that f (ba) → ya − x = y.

For ba → θ ya, the statement is trivial for x = 0, so assume x > 0. Observe that
α = ˆαL eventually and ˆαL → ∞ (Proposition 4), and furthermore xU = 0 eventually
(by choice of α or via Proposition 3) and these statements imply that xL → 0 (see
Proposition 3). Consider a ba suﬃciently close to θ ya such that all of the eventual
statements hold, α ≥ θ, and xL ≤ x, so that f (ba) = rLy. We show that16 rL = θ.
This can be seen by explicit calculation as follows. To simplify notation, assume
WLOG ya = 1. By Proposition 3 and xU = 0 we have rL = 1 − αxL, so the statement
is equivalent to showing αxL = θ. This statement is equivalent to

α

1 −

r

1 −

2

α

!

(1 − ba)

= θ

α − θ = α

r

1 −

2

α

(1 − ba)

(α − θ)2 = α2 − 2α (1 − ba)

θ2 − 2α (θ − (1 − ba)) = 0
(cid:17) = 0.
(cid:16)

θ2 − 2α

ba − θ

⇔

⇔

⇔

⇔

Recall now that α = ˆαL = 1
2

θ2
ba−θ

. The statement now clearly holds.

16This does not contradict Theorem 1 because that theorem only stated strict monotonicity of f
in the region of ba where f (ba)/y ∈ (θ, 1). We do not usually have strict monotonicity in the larger
region of ba where ba/ya ∈ (θ, 1).

57

Disclaimer. This paper is for general information purposes only.
It does not
constitute investment advice or a recommendation or solicitation to buy or sell any
investment and should not be used in the evaluation of the merits of making any
investment decision. It should not be relied upon for accounting, legal or tax advice or
investment recommendations. This paper may contain experimental code and technical
designs that may not be ready for general use. This paper reﬂects the current opinions
of the authors and is not made on behalf of Superluminal Labs or its aﬃliates and does
not necessarily reﬂect the opinions of Superluminal Labs, its aﬃliates or individuals
associated with Superluminal Labs. The opinions reﬂected herein are subject to change
without being updated.

58

