1
2
0
2

r
a

M
2

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
2
5
1
2
0
.
6
0
9
1
:
v
i
X
r
a

(In)Stability for the Blockchain: Deleveraging Spirals and
Stablecoin Attacks

ARIAH KLAGES-MUNDT, Cornell University, Center for Applied Mathematics
ANDREEA MINCA, Cornell University, Operations Research & Information Engineering

March 3, 2021
Initial release: June 2019

We develop a model of stable assets, including non-custodial stablecoins backed by cryptocurrencies. Such
stablecoins are popular methods for bootstrapping price stability within public blockchain settings. We derive
fundamental results about dynamics and liquidity in stablecoin markets, demonstrate that these markets face
deleveraging feedback effects that cause illiquidity during crises and exacerbate collateral drawdown, and
characterize stable dynamics of the system under particular conditions. The possibility of such ‘deleveraging
spirals’ was first predicted in the initial release of our paper in 2019 and later directly observed during the
‘Black Thursday’ crisis in Dai in 2020. From these insights, we suggest design improvements that aim to
improve long-term stability. We also introduce new attacks that exploit arbitrage-like opportunities around
stablecoin liquidations. Using our model, we demonstrate that these can be profitable. These attacks may
induce volatility in the ‘stable’ asset and cause perverse incentives for miners, posing risks to blockchain
consensus. A variant of such attacks also later occurred during Black Thursday, taking the form of mempool
manipulation to clear Dai liquidation auctions at near zero prices, costing $8m.

1 INTRODUCTION
In 2009, Bitcoin [26] introduced a new notion of decentralized cryptocurrency and trustless trans-
action processing. This is facilitated by blockchain, which introduced a new way for mistrusting
agents to cooperate without trusted third parties. This was followed by Ethereum [31], which intro-
duced generalized scripting functionality, allowing ‘smart contracts’ that execute algorithmically
in a verifiable and somewhat trustless manner. Cryptocurrencies promise notions of cryptographic
security, privacy, incentive alignment, digital usability, and open accessibility while removing most
facets of counterparty risk. However, as these cryptocurrencies are, by their nature, unbacked by
governments or physical assets, and the technology is quite new and developing, their prices are
subject to wild volatility, which affects their usability.

A stablecoin is a cryptocurrency with an economic structure built on top of blockchain that aims
to stabilize the purchasing power of the coin. A true stablecoin, often referred to as the “Holy Grail
of crypto”, would offer the benefits of cryptocurrencies without the unusable volatility and remains
elusive. A more tangible goal is to design a stablecoin that maximizes the probability of remaining
stable long-term. If one can establish guarantees for the stability of such a stablecoin, this would be
a significant step toward forming a robust decentralized financial system and facilitating economic
adoption of cryptocurrencies.

Cryptocurrency volatility. Cryptocurrencies face difficult technological, usability, and regulatory
challenges to be successful long-term. Many cryptocurrency systems develop different approaches to
solving these problems. Even assuming the space is long-term successful, there is large uncertainty
about the long-term value of individual systems.

The value of these systems depends on network effects: value changes in a nonlinear way as
new participants join. In concrete terms, the more people who use the system, the more likely
it can be used to fulfill a given real world transaction. The success of a cryptocurrency relies on
a mass of agents–e.g., consumers, businesses, and/or financial institutions–adopting the system
for economic transactions and value storage. Which systems will achieve this adoption is highly

Ariah Klages-Mundt and Andreea Minca

1

uncertainty, and so current cryptocurrency positions are very speculative bets on new technology.
Further, cryptocurrency markets face limited liquidity and market manipulation. In addition, the
decentralized control and privacy features of cryptocurrencies can be at odds with desires of
governments, which introduces further uncertainty around attempted interventions in the space.
These uncertainties drive price volatility, which feeds back into fundamental usability problems.
It makes cryptocurrencies unusable as short-term stores of value and means of payment, which
increases the barriers to adoption. Indeed, today we see that most cryptocurrency transactions
represent speculative investment as opposed to typical economic activity.

Stablecoins. Stablecoins aim to bootstrap price stability into cryptocurrencies as a stop-gap

measure for adoption. Current projects take one of two forms:

• Custodial stablecoins rely on trusted institutions to hold reserve assets off-chain (e.g., $1

per coin). This introduces counterparty risk that cryptocurrencies otherwise solve.

• Non-custodial (or decentralized) stablecoins create on-chain risk transfer markets via

complex systems of algorithmic financial contracts backed by volatile cryptoassets.

We focus on non-custodial stablecoins and, more generally, the stable asset and risk transfer
markets that they represent. Non-custodial systems are not well understood whereas custodial
stablecoins can be interpreted using existing well-developed financial literature. Further, non-
custodial stablecoins operate in the public/permissionless blockchain setting, in which any agent
can participate. In this setting, malicious agents can participate in stablecoin systems. As we will
see, this can introduce new economic attacks.

1.1 Non-custodial (decentralized) stablecoins
The non-custodial stablecoins that we consider create systems of contracts on-chain with the
following features encoded in the protocol. We refer to these as DStablecoins.

• Risk is transferred from stablecoin holders to speculators. Stablecoin holders receive a form
of price insurance whereas speculators expect a risky return from a leveraged position.1
• Collateral is held in the form of cryptoassets, which backs the stable and risky positions.
• An oracle provides pricing information from off-chain markets.
• A dynamic deleveraging process balances positions if collateral value deviates too much.
• Agents can change their positions through some pre-defined process.

These systems are non-custodial (or decentralized) because the contract execution and collateral
are all completely on-chain; thus they potentially inherit all of the benefits of cryptocurrencies,
such as minimization of counterparty risk. DStablecoins are variants on contracts for difference,
which we describe next. The risk transfer typically works by setting up a tranche structure in which
losses (or gains) are borne by the speculators and the stablecoin holder holds an instrument like
senior debt.2 There are also other non-collateralized (or algorithmic) stablecoins–for a discussion of
these, see [4]. We don’t consider these directly in this paper; however, we discuss in Section 7 how
our model can accommodate these systems as well.

Contract for difference. Two parties enter an overcollateralized contract, in which the speculator
pays the buyer the difference (possibly negative) between the current value of a risky asset and its

1‘Leverage’ means that the speculator holds > 1× their initial assets but faces new liabilities.
2Intuitively, these are like collateralized debt obligations (CDOs) with the important addition of dynamic deleveraging
according to the rules of the protocol. As we will see, it is critical to understand deleveraging spirals as they affect the senior
tranches.

Ariah Klages-Mundt and Andreea Minca

2

value at contract termination.3 For example, a buyer might enter 1 Ether into the contract and a
speculator might enter 1 Ether as collateral. At termination, the contract Ether is used to pay the
buyer the original dollar value of the 1 Ether at the time of entry. Any excess goes to the speculator.
If the contract approaches undercollateralization (if Ether price plummets), the buyer can trigger
early settlement or the speculator can add more collateral.

Variants on contracts for difference. DStablecoins differ from basic contracts for difference in that
(1) the contracts are multi-period and agents can change their positions over time, (2) the positions
are dynamically deleveraged according to the protocol, and (3) settlement times are random and
dependent on the protocol and agent decisions. The typical mechanics of these contracts are as
follows:

• Speculators lock cryptoassets in a smart contract, after which they can create new stablecoins
as liabilities against their collateral up to a threshold. These stablecoins are sold to stablecoin
holders for additional cryptoassets, thus leveraging their positions.

• At any time, if the collateralization threshold is surpassed, the system attempts to liquidate

the speculator’s collateral to repurchase stablecoins/reduce leverage.

• The stablecoin price target is provided by an oracle. The target is maintained by a dynamic
coin supply based on an ‘arbitrage’ idea. Notably, this is not true arbitrage as it is based on
assumptions about the future value of the collateral.
– If price is above target, speculators have increased incentive to create new coins and sell

them at the ‘premium price’.

– If price is below target, speculators have increased incentive to repurchase coins (reducing

supply) to decrease leverage ‘at a discount’.

• Stablecoins are redeemable for collateral through some process. This can take the form of
global settlement, in which stakeholders can vote to liquidate the entire system, or direct
redemption for individual coins. Settlement can take 24 hours-1 week.

• Additionally, the system may be able to sell new ownership/decision-making shares as a last

attempt to recapitalize a failing system – e.g., the role of MKR in Dai (see [23]).

DStablecoin risks. DStablecoins face two substantial risks:
(1) Risk of market collapse,
(2) Oracle/governance manipulation.

Our model in this paper focuses on market collapse risk. We further remark on oracle/governance
manipulation in Section 7.

Existing DStablecoins. At the time of initial writing in 2019, major non-custodial stablecoins
included Dai, BitShares Market Pegged Assets (like bitUSD), and Steem Dollars. In the latter, Steem
market cap is essentially collateral; Steem Dollars can be redeemed for $1 worth of newly minted
Steem, and so redemptions affect all Steem hodlers via inflation. Since then, many new stablecoins
have arisen based on similar ideas by UMA, Reflexer, and Liquity, as well as endogenous collateral
stablecoins like Synthetix sUSD, Terra UST, and Celo Dollar (see [17] for further discussion). Notably,
unlike custodial stablecoins, Dai is not currently considered as emoney or payment method subject
to the Payment Services Directive in the European Union since there is no single issuer or custodian.
Thus it does not have AML/KYC requirements.

In an academic white paper, [6] proposed a variation on cryptocurrency-collateralized DStable-
coin design. It standardizes the speculative positions by restricting leverage to pre-defined bounds

3Intuitively, this is similar to a forward contract except that the price is only fixed in fiat terms while payout is in the units
of the underlying collateral.

Ariah Klages-Mundt and Andreea Minca

3

(a) NuBits trades at cents on the dollar.

(b) BitUSD has broken its USD peg.

Fig. 1. Depeggings in decentralized stablecoins.

using automated resets. A consequence of these leverage resets is that stablecoin holders are
partially liquidated from their positions during downward resets–i.e., when leverage rises above
the allowed band due to a cryptocurrency price crash. This compares with Dai, in which stablecoin
holders are only liquidated in global settlement. An effect of this difference is that, in order to
maintain a stablecoin position in the short-term, stablecoin holders need to re-buy into stablecoins
(at a possibly inflated price) after downward resets. Of the many designs, it is unclear which
deleveraging method would lead to a system that survives longer. This motivates us to study the
dynamics of DStablecoin systems.

Non-custodial stablecoins have now experienced a wide array of volatility events, failures, and
attacks. Since the initial release of this paper in 2019, Black Thursday in March 2020 saw massive
liquidation events result in a substantial depegging in Dai [22], mirroring our results in Sections 3-4,
and miner mempool manipulation that contributed to Dai liquidation auctions clearing at near zero
prices at a cost of $8m to the Maker system [5], mirroring attack surfaces we described in Section 6.
Prior to this, as discussed in [14], Nubits has traded at cents on the dollar since 2018 (Figure 1a), and
bitUSD and Steem Dollars have broken their USD pegs periodically (Figure 1b). Many additional
examples of stablecoin mechanism failures and exploitations occurred through the rest of 2020 (see
[17, 30]). Yet, the stablecoin space has remained heated with projects such as Dai growing rapidly
and many new contenders arising, including UMA, Reflexer, Celo, and Liquity. The work in this
paper has proven consequential for the progression of these projects (e.g., [19, 24]).

1.2 Relation to prior work
Stablecoins are active cryptocurrencies, for which pre-existing models do not understand how the
collateral rule enforces stability and how the interaction of different agents can affect stability.

With the notable exception of [6], rigorous mathematical work on non-custodial stablecoins
is lacking. They applied option pricing theory to valuing tranches in their proposed DStablecoin
design using advanced PDE methods. In doing so, they need the simplifying assumption that
DStablecoin payouts (e.g., from interest/fee payments and liquidations from leverage resets) are
exogenously stable with respect to USD. This may circularly cause stability. In reality, these payouts
are made in volatile cryptocurrency (ETH). From these ETH payments, stablecoin holders can

(1) Hold ETH and so take on ETH exposure,
(2) Use the ETH to re-buy into stablecoin, likely at an inflated price as it endogenously increases

demand after a supply contraction,

Price (USD)24h VolNuBits ChartsJan '15Jul '15Jan '16Jul '16Jan '17Jul '17Jan '18Jul '182015201620172018$0$0.500000$1.000Zoom1d7d1m3m1yYTDALLFromSep 24, 2014ToDec 12, 2018Market CapPrice (USD)Price (BTC)24h Volcoinmarketcap.comPrice (USD)24h VolbitUSD Charts17. Sep1. Oct15. Oct29. Oct12. Nov26. Nov10. Dec20162018$0.600000$0.800000$1.000Zoom1d7d1m3m1yYTDALLFromSep 12, 2018ToDec 12, 2018Market CapPrice (USD)Price (BTC)Price (BTS)24h Volcoinmarketcap.comAriah Klages-Mundt and Andreea Minca

4

(3) Convert the ETH to fiat, which requires waiting for block confirmations in an exchange
(possibly hours) during times when ETH is particularly volatile and paying costs for fiat
conversion (fees, potentially taxes). Notably, this is not available in all jurisdictions.

To maintain a DStablecoin position, stablecoin holders need to re-buy into DStablecoins at each
reset at endogenously higher price. Stablecoin holders additionally face the risk that the size of the
DStablecoin market collapses such that the position cannot be maintained (and so ends up holding
ETH). As no stable asset models exist to understand these endogenous effects, the analysis can’t be
easily extended using the traditional financial literature.4 Our focus in this paper is complementary
to understand these endogenous stable asset effects.

[20] studied the evolution of custodial stablecoins. A few works on stablecoins have also arisen
since the initial release of our paper. [16] described governance attack surfaces in non-custodial
stablecoins, which is extended with general models in [17]. [11] presented an analysis of credit risk
stemming from collateral type in the Maker system. And [8, 28] modeled stability in the Terra and
Celo stablecoins under different scenarios of Brownian motion without the endogenous market
feedback effects we study in this paper.

In the context of central counterparty clearinghouses, the default fund contributions, margin
requirements and participation incentives have been studied in, e.g., [7], [1], and [10]. The critical
question in this area is understanding the effects of a liquidation policy of a member’s portfolio in
the case of a significant event. The counterpart of this in a decentralized setting is understanding
the impact of DStablecoin deleveraging on system stability.

Stablecoin holders bear some resemblance to agents in currency peg and international finance
models, e.g., [25] and [12]. In these models, the market maker is essentially the government but is
modeled with mechanical behavior and is not a player in the game. For instance, in [12], devaluation
is modeled by a simple exogenous threshold rule: the government abandons the peg if the net
demand for currency breaches the threshold and is otherwise committed to maintaining the peg.
In contrast to currency markets, no agents are committed to maintaining the peg in DStablecoin
markets. The best we can hope is that the protocol is well-designed and that the peg is maintained
with high probability through the protocol’s incentives. The role of government is replaced by
decentralized speculators, who issue and withdraw stablecoins in a way to optimize profit. A fully
strategic model would be a complicated dynamic game–these tend to be intractable and, indeed, are
avoided in the currency peg literature in favor of a sequence of one period games. We enable a more
endogenous modeling of speculators’ optimization problems under a variety of risk constraints.
Our model is a sequence of one-period optimization problems, in which dynamic coupling comes
through the risk constraints.

DStablecoin speculators are similar to market makers in market microstructure models (e.g.,
[27]). Like classical market microstructure, we do have a multi-period system with multiple agents
subject to leverage constraints that take recurring actions according to their objectives. In contrast,
in the DStablecoin setting, we do not have a truly stable asset that is efficiently and instantaneously
available. Instead, agents make decisions that endogenously affect the price of the ‘stable’ asset and
affect the agents’ future decisions and incentives to participate in a non-stationary way. In turn,
the (in)stability results from the dynamics of these decisions.

Since the initial release of our paper in June 2019, [18] has described a complementary model of
non-custodial stablecoins related to the model in this paper. That paper explores a different model
of liquidation structure that affects speculator decision-making and applies martingale methods
to analytically characterize stability. In contrast, in this paper we derive stability results about a

4A secondary issue with their continuous model is that these systems are inherently discontinuous due to the discrete
nature of incorporating blockchain transactions into blocks. Thus resets can occur beyond the set thresholds.

Ariah Klages-Mundt and Andreea Minca

5

simpler model that is more amenable to simulations, which we perform, and demonstrate stablecoin
attacks that can arise from profitable bets against other agents.

1.3 This paper
We develop a dynamic model for non-custodial stablecoins that is complex enough to take into
account the feedback effects discussed above and yet remains tractable. Our model can be interpreted
as a market microstructure model in this new type of asset market.

Our model involves agents with different risk profiles; some desire to hold stablecoins and others
speculate on the market. These agents solve optimization problems consistent with a wide array of
documented market behaviors and well-defined financial objectives. As is common in the literature
on market microstructure and currency peg games, these agents’ objectives are myopic. These
objectives are coupled for non-myopic risk using a flexible class of rules that are widely established
in financial markets; these allow us to model the effects of a range of cyclic and counter-cyclic
behaviors. The exact form of these rules is selected and self-imposed by speculators to match their
desired responses and not part of the stablecoin protocol. Thus well-established manipulation of
similar rules as applied to traditional financial regulation is not a problem here. Our model goes
largely beyond a one-period model. We introduce this model with supporting rationale for design
choices in Section 2.

Using our model, we make the following contributions:
• We derive fundamental results about dynamics and liquidity in our model (Section3).
• We demonstrate that stablecoins face deleveraging feedback effects that may cause illiquidity

during crises and exacerbate collateral drawdown (Section 3.3).

• We characterize stable dynamics of the system under certain conditions that guarantee no
liquidity crash (Section 4) and show instability can occur in simulations outside of this setting
(Section 4.2).

• We simulate a wide range of market behaviors and find that speculator behavior has a large
effect on realized volatilities, but that stablecoin failure times are largely determined by
underlying asset movements (Section 5).

• We describe new attacks that exploit arbitrage-like opportunities around stablecoin liquida-

tions (Section 6).

We relate these results to historical stablecoin events and apply these insights to suggest design
improvements that aim to improve long-term stability. Based on these insights, we also suggest that
interactions between multiple speculators and attackers may be the most interesting relationships
to explore in more complex models.

2 MODEL
Our model couples a number of variables of interest in a risk transfer market between stablecoin
holders and speculators. The stablecoin protocol dictates the logic of how agents can interact with
the smart contracts that form the system; the design of this influences how the market plays out.
Many DStablecoin designs have been proposed. We set up our model to emulate a DStablecoin
protocol like Dai with global settlement, but the model is adaptable to different design choices.
Note that our model is formulated with very few parameters given the problem complexity.

Our model builds on the model of traditional financial markets in [2] but is new in design
by incorporating endogenous stablecoin structure. In the model, we assume that the underlying
consensus layer (e.g., blockchain) works well to confirm transactions without censorship or attack
and that the system of contracts executes as intended.

Agents. Two agents participate in the market.

Ariah Klages-Mundt and Andreea Minca

6

• The stablecoin holder seeks stability and chooses a portfolio to achieve this.
• The speculator chooses leverage in a speculative position behind the DStablecoin.
Stablecoin holders are motivated by risk aversion, trade limitations, and budget constraints. They
are inherently willing to hold cryptoassets. In the current setting, this means they are likely either
traders looking for short-term stability, users from countries with unstable fiat currencies, or users
who are using cryptocurrencies to move money across borders. In the future, cryptocurrencies
may be more accepted in economic exchange. In this case, stablecoin holders may be ordinary
consumers who face risk aversion and budgeting for required consumption.

Speculators are motivated by (1) access to leverage and (2) security lending to borrow against
their Ether holdings without triggering tax incidence or giving up Ether ownership. In order to
begin participating, speculators need to either have confidence in the future of cryptocurrencies,
think they can make money trading the markets, or face unusually high tax rates (or other barriers)
that make security lending cheaper than outright selling assets. The model in this paper focuses on
the first motivation. We propose an extension to the model that considers the second motivation.

Assets. There are two assets. For simplicity, we give these assets specific names; however, they

could be abstracted to other cryptocurrencies or outside of a cryptocurrency setting.

• Ether: high risk asset whose USD market prices 𝑝𝐸
• DStablecoin: a ‘stable’ asset collateralized in Ether whose USD price 𝑝𝐷
𝑡
Notably, a large DStablecoin system may have endogenous amplification effects on Ether price,
similarly to how CDOs affected underlying assets in the 2008 financial crisis. We discuss this further
in Section 7 but leave formal modeling of this to future work.

𝑡 are exogenous

is endogenous

There are several barriers for trading between crypto and fiat, which motivate our choice of assets.
Most crypto-fiat pairs are through Bitcoin or Ether, which act as a gateway to other cryptoassets.
Trading to fiat can involve moving assets between a number of exchanges and can take considerable
time to confirm on the blockchain. Trading to a stablecoin is comparatively simple. Trading to fiat
can also trigger more clear tax incidence. Additionally, some countries have imposed strict capital
controls on trading between fiat and crypto.

Model outline. At 𝑡 = 0, the agents have endowments and prior beliefs. In each period 𝑡:
(1) New Ether price is revealed
(2) Ether expectations are updated
(3) Stablecoin holder decides portfolio weights
(4) Speculator, seeing demand, decides leverage
(5) DStablecoin market is cleared

2.1 Stablecoin holder
The stablecoin holder starts with an initial endowment and decides portfolio weights to attain the
desired stability. The following table defines the agent’s state variables.

Variable Definition

¯𝑛𝑡
¯𝑚𝑡
wt

Ether held at time 𝑡
DStablecoin held at time 𝑡
Portfolio weights chosen at time 𝑡

The stablecoin holder weights its portfolio by wt. We denote the components as 𝑤 𝐸

𝑡 and 𝑤 𝐷
𝑡
Ether and DStablecoin weights respectively. The stablecoin holder’s portfolio value at time 𝑡 is

for

𝑡 + ¯𝑚𝑡 𝑝𝐷
Given weights, ¯𝑛𝑡 and ¯𝑚𝑡 will be determined based on the stablecoin clearing price 𝑝𝐷
𝑡 .

𝑡 + ¯𝑚𝑡 −1𝑝𝐷
𝑡 .

𝑡 = ¯𝑛𝑡 −1𝑝𝐸

A𝑡 = ¯𝑛𝑡 𝑝𝐸

Ariah Klages-Mundt and Andreea Minca

7

The basic results in Section 3 hold generally for any wt ≥ 0 (i.e., there is no shorting). In this
case, wt could be chosen, e.g., from Sharpe ratio optimization, mean-variance optimization, or
Kelly criterion (among others). In Sections 4 & 5, in order to focus on the effects of speculator
decisions, we simplify the stablecoin holder as exogenous with unit price-elastic demand. In this
case, DStablecoin demand is constant in dollar terms.

2.2 Speculator
The speculator starts with an endowment of Ether and initial beliefs about Ether’s returns and
variance and decides leverage to maximize expected returns subject to protocol and self-imposed
constraints. The following tables define variables and parameters for the speculator.

Variable Definition

𝑛𝑡
𝑟𝑡
𝜎 2
𝑡
L𝑡
Δ𝑡
˜𝜆𝑡

Ether held at time 𝑡
Expected return of Ether at time 𝑡
Expected variance of Ether at time 𝑡
Total stablecoins issued at time 𝑡
Change to stablecoin supply at time 𝑡
Leverage bound at time 𝑡

Parameter Definition

𝛾
𝛿
𝛽
𝛼
𝑏

Memory parameter for return estimation
Memory parameter for variance estimation
Collateral liquidation threshold
Parameter governing risk measure (inversely related to VaR)
Cyclicality parameter in risk constraint: pro- (𝑏 > 0) or counter-cyclic (𝑏 < 0)

2.2.1 Ether expectations. The speculator updates expected returns 𝑟𝑡 , log-returns 𝜇𝑡 (used for the
variance estimation), and variance 𝜎 2

𝑡 based on observed Ether returns as follows:

𝑟𝑡 = (1 − 𝛾)𝑟𝑡 −1 + 𝛾

𝑝𝐸
𝑡
𝑝𝐸
𝑡 −1

,

𝜇𝑡 = (1 − 𝛿)𝜇𝑡 −1 + 𝛿 log

𝑡 = (1 − 𝛿)𝜎 2
𝜎 2

𝑡 −1 + 𝛿

(cid:16) log

,

𝑝𝐸
𝑡
𝑝𝐸
𝑡 −1
𝑝𝐸
𝑡
𝑝𝐸
𝑡 −1

(1)

(cid:17) 2

.

− 𝜇𝑡

For fixed memory parameters 𝛾, 𝛿 (lower memory parameter = longer memory), these are expo-
nential moving averages consistent with the RiskMetrics approach commonly used in finance [21].
For sufficiently stepwise decreasing memory levels and assuming i.i.d. returns, this process will
converge to the true values supposing they are well-defined and finite. In reality, speculators don’t
outright know the Ether return distribution and, as we will see in the simulations, the stablecoin
system dynamics occur on timescales shorter than required for convergence of expectations. Thus,
we focus on the simpler case of fixed memory parameters.

Note that 𝛾 ≠ 𝛿 may be reasonable. Current cryptocurrency markets are not very price efficient,
and so traders might reasonably take into account momentum when estimating returns while using
a wider memory for estimating covariance.

We additionally consider the case in which the speculator knows the Ether distribution outright
and 𝛾 = 𝛿 = 0. This is consistent with a rational expectations standpoint but ignores how the
speculator arrives at that knowledge.

Ariah Klages-Mundt and Andreea Minca

8

2.2.2 Optimize leverage: choose Δ𝑡 . The speculator is liable for L𝑡 DStablecoins at time 𝑡. At each
time 𝑡, it decides the number of DStablecoins to create or repurchase. This changes the stablecoin
supply L𝑡 = L𝑡 −1 + Δ𝑡 . If Δ𝑡 > 0, the speculator creates and sells new DStablecoin in exchange for
Ether at the clearing price. If Δ𝑡 < 0, the speculator repurchases DStablecoin at the clearing price.
Strictly speaking, the speculator will want to maximize its long-term withdrawable value. At time
𝑡, the speculator’s withdrawable value is the value of its ETH holdings minus collateral required for
any issued stablecoins: 𝑛𝑡 𝑝𝐸
𝑡 − 𝛽L𝑡 . Maximizing this is not amenable to a myopic view, however, as
maximizing the next step’s withdrawable value is only a good choice when the speculator intends
to exit in the next step.

Instead, we frame the speculator’s objective as maximizing expected equity: 𝑛𝑡 𝑝𝐸

𝑡 − E[𝑝𝐷 ]L𝑡 . In
this, the speculator expects to be able to settle liabilities at a long-term expected value of E[𝑝𝐷 ]. The
market price of DStablecoin will fluctuate above and below $1 naturally depending on prevailing
market conditions. The actual expected value is nontrivial to compute as it depends on the stability
of the DStablecoin system. For individual speculators with small market power, we argue that
E[𝑝𝐷 ] = 1 is a an assumption they may realistically make, as we discuss further below. This is
additionally the value realized in the event of global settlement.

We suggest that this optimization is a candidate for ‘honest’ behavior of a speculator as it is
consistent with the speculator acting on perceived arbitrage in mispricings of DStablecoin from
the peg. In essence, the speculator expects to increase (reduce) leverage ‘at a discount’ when 𝑝𝐷
is
𝑡
above (below) target. This is the typically cited mechanism by which these systems maintain their
peg and thus how the designers intend for speculators to behave. However, this assumes that 𝑝𝐷
is
𝑡
sufficiently stable/mean-reverting to $1 and so this behavior may not in fact be a best response.

Aggregate vs. individual speculators. In our model, the single speculative agent, which is not
a price-taker, is intended to reflect the aggregate behavior of many individual speculators, each
with small market power.5 In a normal liquid market, an individual speculator would be able to
repurchase DStablecoins at dollar cost and walk away with the equity. By maximizing equity, the
aggregate speculator considers its liabilities to be $1 per DStablecoin. This may turn out to be
untrue during liquidity crises as the repurchase price may be higher. In our model, speculator’s
don’t know the probability of crises and instead account for this in a conservative risk constraint.

Formal optimization problem. The speculator chooses Δ𝑡 by maximizing expected equity in the

next period subject to a leverage constraint:

max
Δ𝑡
s.t.

(cid:16)
𝑛𝑡 −1𝑝𝐸

𝑡 + Δ𝑡 𝑝𝐷

𝑡 (L𝑡 )

(cid:17)

− L𝑡

𝑟𝑡

Δ𝑡 ∈ F𝑡

where F𝑡 is the feasible set for the leverage constraint. This is composed of two separate constraints:
(1) a liquidation constraint that is fundamental to the protocol, and (2) a risk constraint that
encodes the speculator’s desired behavior. Both are introduced below.

If the leverage constraint is unachievable, we assume the speculator enters a ‘recovery mode’, in
which it tries to maximize its chances of returning to the normal setting. In this case, it solves the
optimization using only the liquidation constraint. If the liquidation constraint is unachievable, the
DStablecoin system fails with a global settlement.

Liquidation constraint: enforced by the protocol. The liquidation constraint is fundamental to
2.2.3
the DStablecoin protocol. A speculator’s position undergoes forced liquidation at time 𝑡 if either

5We propose to relax this simplification in follow-up work by considering the interaction of many speculators with longer
term strategic thinking.

Ariah Klages-Mundt and Andreea Minca

9

is revealed, 𝑛𝑡 −1𝑝𝐸

(1) after 𝑝𝐸
𝑡 < 𝛽L𝑡 . The speculator
𝑡
aims to control against this as liquidations can occur at unfavorable prices and are associated with
fees in existing protocols (we exclude these fees from our simple model, but they can be easily
added).

𝑡 < 𝛽L𝑡 −1, or (2) after Δ𝑡 is executed, 𝑛𝑡 𝑝𝐸

Define the speculator’s leverage as the 𝛽-weighted ratio of liabilities to assets6

The liquidation constraint is then 𝜆𝑡 ≤ 1.

𝜆𝑡 =

𝛽 · liabilities
assets

.

2.2.4 Risk constraint: self-imposed speculator behavior. The risk constraint encodes the speculator’s
desired behavior into the model. We assume no specific type for the risk constraint in our analytical
results, which are generic. For our simulations, we explore a variety of speculator behaviors via the
risk constraint. We first consider Value-at-Risk (VaR) as an example of a constraint realistically used
in markets. This is consistent with narratives shared by Dai speculators about leaving a margin of
safety to avoid liquidations. We then construct a generalization that goes well beyond VaR and
allows us to explore a spectrum of pro-cyclical and counter-cyclical behaviors encoded in the risk
constraint.

Manipulation and instability resulting from similar externally-imposed VaR rules is a well-known
problem in the risk management and financial regulatory literature (see e.g., [2]). This is of less
concern here as the precise parameters of the risk constraint are selected and self-imposed by
speculators to approximate their own utility optimization and are not part of the DStablecoin
protocol. Further, we consider constraints that go beyond VaR. We instead need to show that our
results are robust to a variety of risk constraints that speculators could select.

Example: VaR-based constraint. The VaR-based version of the risk constraint is

𝜆𝑡 ≤ exp(𝜇𝑡 − 𝛼𝜎𝑡 ),
where 𝛼 > 0 is inversely related to riskiness. This is consistent with VaR for normal and maximally
heavy-tailed symmetric return distributions with finite variance.

Let VaR𝑎,𝑡 be the 𝑎-quantile per-dollar VaR of the speculator’s holdings at time 𝑡. This is the
minimum loss on a dollar in an 𝑎-quantile event. With a VaR constraint, the speculator aims to
avoid triggering the liquidation constraint in the next period with probability 1 − 𝑎, i.e., P

(cid:16)
𝑛𝑡 𝑝𝐸

𝑡 +1 ≥

(cid:17)

𝛽L𝑡

≥ 1 − 𝑎. To achieve this, the speculator chooses Δ𝑡 such that

(cid:16)
𝑛𝑡 −1𝑝𝐸

𝑡 + Δ𝑡 𝑝𝐷

𝑡 (L𝑡 )

(cid:17)

(1 − VaR𝑎,𝑡 ) ≥ 𝛽L𝑡 .

This requires 𝜆𝑡 ≤ 1 − VaR𝑎,𝑡 , which addresses the probability that the liquidation constraint is
satisfied next period and implies that it is satisfied this period.

Define ˜𝜆𝑡 := exp(𝜇𝑡 − 𝛼𝜎𝑡 ). Then ˜𝜆𝑡 is increasing in 𝜇𝑡 and decreasing in 𝜎𝑡 . Further, the fatter
the speculator thinks the tails of the return distribution are, the greater 𝛼 will be, and the lesser ˜𝜆𝑡
will be, as we demonstrate next.

VaR constraint with normal returns. If the speculator assumes Ether log returns are (𝜇𝑡, 𝜎𝑡 ) normal,
2erf−1(2𝑎 − 1), which is positive

then VaR𝑎,𝑡 = 1 − exp (cid:16)
for appropriately small 𝑎, the VaR constraint is 𝜆𝑡 ≤ 1 − VaR𝑎,𝑡 = exp(𝜇𝑡 − 𝛼𝜎𝑡 ).

2𝜎𝑡 erf−1(2𝑎 − 1)

. Defining 𝛼 = −

𝜇𝑡 +

√

√

(cid:17)

6We choose this definition to simplify the model. The alternative definition 𝜆′ =
scaled from 0 to ∞. I.e., 𝜆′ = 1
1−𝜆 is monotonically increasing in 𝜆 for 0 ≤ 𝜆′ < 1.

assets

assets−𝛽 ·liabilities describes the same idea

Ariah Klages-Mundt and Andreea Minca

10

VaR constraint with heavy tails. If Ether log returns 𝑋 are symmetrically distributed with finite

mean 𝜇𝑡 and finite variance 𝜎 2

𝑡 , then for any 𝛼 > 1, Chebyshev’s inequality gives us

P(𝑋 < 𝜇𝑡 − 𝛼𝜎𝑡 ) ≤

1
2𝛼 2

.

For the maximally heavy-tailed case, this inequality is tight. Then for VaR quantile 𝑎, we can find
the corresponding 𝛼 such that 𝑎 = 1
2𝛼 2 . The log return VaR is 𝜇𝑡 − 𝛼𝜎𝑡 , which gives the per-dollar
VaR𝑎,𝑡 = 1 − exp(𝜇𝑡 − 𝛼𝜎𝑡 ). Then the VaR constraint is 𝜆𝑡 ≤ exp(𝜇𝑡 − 𝛼𝜎𝑡 ).

Generalized risk constraint. Similarly to [2], we can generalize the bound to explore a spectrum

of different behaviors:

ln ˜𝜆 = 𝜇𝑡 − 𝛼𝜎𝑏
𝑡 ,
where 𝛼 is an inverse measure of riskiness and 𝑏 is a cyclicality parameter. A positive 𝑏 means that
˜𝜆𝑡 decreases with perceived risk (pro-cyclical). A negative 𝑏 means that ˜𝜆𝑡 increases with perceived
risk (counter-cyclical).

2.3 DStablecoin market clearing
The DStablecoin market clears by setting demand = supply in dollar terms:
(cid:16) ¯𝑛𝑡 −1𝑝𝐸

𝑡 + ¯𝑚𝑡 −1𝑝𝐷

= L𝑡 𝑝𝐷

𝑡 (L𝑡 ).

𝑡 (L𝑡 )

𝑤 𝐷
𝑡

(cid:17)

The demand (left-hand side) comes from the stablecoin holder’s portfolio weight and asset value.
Notice that while the asset value depends on 𝑝𝐷
𝑡 does not. That is, the
stablecoin holder buys with market orders based on weight. This simplification allows for a tractable
market clearing; however, it is not a full equilibrium model.

𝑡 , the portfolio weight 𝑤 𝐷

We justify this choice of simplified market clearing with the following observations:
• The clearing is similar to constant product market maker model used in the Uniswap decen-

tralized exchange (DEX) [32].

• Sophisticated agents are known to be able to front-run DEX transactions [9]. As speculators
are likely more sophisticated than ordinary stablecoin holders, in many circumstances they
can see demand before making supply decisions.7

• Evidence from Steem Dollars suggests that demand need not decrease tremendously with
price in the unique setting in which stable assets are not efficiently available. Steem Dollars
is a stablecoin with a mechanism for price ‘floor’ but not ‘ceiling’. Over significant stretches
of time, it has traded at premiums of up to 15× target.

In most of our results, the time period context is clear. To simplify notation, in a given time 𝑡, we

drop subscripts and write with the following quantities:

Quantity
𝑥 := 𝑤 𝐷
𝑦 := 𝑤 𝐷
𝑧 := 𝑛𝑡 −1𝑝𝐸
𝑡

𝑡 ¯𝑛𝑡 −1𝑝𝐸
𝑡
𝑡 ¯𝑚𝑡 −1 − L𝑡 −1 𝑦 ≤ 0
𝑧 ≥ 0

Sign Interpretation
𝑥 ≥ 0 New DStablecoin demand available

|𝑦| = ‘free supply’ in DStablecoin market
Speculator value available to maintain market

L := L𝑡 −1
Δ := Δ𝑡
:= ˜𝜆𝑡
˜𝜆
w := wt

7This said, DEX mechanics differ slightly from our specific formulation. To make the model more realistic, stablecoin holders
could issue buy offers in token units instead of weights at the expense of greater model complexity.

Ariah Klages-Mundt and Andreea Minca

11

With Δ > 𝑦, which turns out to be always true as discussed later, the clearing price is

𝑝𝐷
𝑡 (Δ) =

𝑥
Δ − 𝑦

.

As the model is defined thus far, stablecoin holders only redeem coins for collateral through global
settlement. However, this assumption is easily relaxed to accommodate algorithmic or manual
settlements.

3 STABLE ASSET MARKET DYNAMICS
We derive tractable solutions to the proposed interactions and results about liquidity and stability.

3.1 Solution to the speculator’s decision
We first introduce some basic results about the speculator’s leverage optimization problem.

Solving the leverage constraint.

Prop. 1. Let Δmin ≥ Δmax be the roots of the polynomial in Δ

−𝛽Δ2 + Δ(cid:16) ˜𝜆(𝑧 + 𝑥) − 𝛽 (L − 𝑦)

(cid:17)

− ˜𝜆𝑧𝑦 + 𝛽L𝑦.

Assuming Δ > 𝑦,

• If Δmin, Δmax ∈ R, then [Δmin, Δmax] ∩ (𝑦, ∞) is the feasible set for the leverage constraint.
• If the roots are not real, then the constraint is unachievable.

[Link to Proof]

Setting ˜𝜆 = 1 gives the expression for the liquidation constraint alone.
The condition Δ > 𝑦 makes sense for two reasons. First, if Δ < 𝑦 then 𝑝𝐷

𝑡 < 0. Second, as we
show below, the limit limΔ→𝑦+ 𝑝𝐷
𝑡 = ∞. Thus, if we start in the previous step under the condition
Δ > 𝑦, then the speculator will never be able to pierce this boundary in subsequent steps. We
further discuss the implications of this condition later.

Solving the leverage optimization.

Prop. 2. Assume that the speculator’s constraint is feasible and let [Δmin, Δmax] ∩ (𝑦, ∞) be the

feasible region. Define 𝑟 := 𝑟𝑡 , let Δ∗ = 𝑦 +

√

−𝑦𝑟𝑥, and define
𝑥
Δ − 𝑦

− Δ.

𝑓 (Δ) = 𝑟 Δ

Then the solution to the speculator’s optimization problem is

• Δ∗ if Δ∗ ∈ [Δmin, Δmax] ∩ (𝑦, ∞)
• Δmin if Δ∗ < Δmin
• Δmax if Δ∗ > Δmax

[Link to Proof]

3.2 Maintenance condition for the stable asset market
The next result describes a bound to the speculator’s ability to maintain the market. This bound
takes the form of

(a lower bound on collateral) - (capital available to enter the market),

which must be sufficiently high for the system to be maintainable.

Ariah Klages-Mundt and Andreea Minca

12

Prop. 3. The feasible set for the speculator’s liquidation constraint is empty when
(cid:16) ˜𝜆(𝑥 + 𝑧) − 𝛽L𝑤 𝐷 (cid:17) 2

< 4𝛽 ˜𝜆L𝑥𝑤 𝐸

[Link to Proof]
In Prop. 3, 𝛽L𝑤 𝐷 ≥ 0 is interpreted as a lower bound on the capital required to maintain the
DStablecoin market into the next period (i.e., the collateral required for the minimum size of the
DStablecoin market), ˜𝜆 ∈ [0, 1], and 𝑥 + 𝑧 ≥ 0 is the capital available to enter the DStablecoin
market from both the supply and demand sides. The inequality then states that the difference
between the capital available to enter the market and the lower bound maintenance capital must be
sufficiently high for the market to be maintainable by the speculator. The constraint Δ < 𝑦 implies
that the case of the negative difference does not work.

3.3 Deleveraging effects, limits to market liquidity

Limits to the speculator’s ability to decrease leverage. The next result presents a fundamental limit
to how quickly the speculator can reduce leverage by repurchasing DStablecoins, given the modeled
market structure. Note that this limit applies even if the speculator can bring in additional capital.
The term −𝑦 = L (1 −𝑤 𝐷 ) represents the ‘free supply’ of DStablecoin available for exchange, which
can be increased by a positive Δ.

Prop. 4. The speculator with asset value 𝑧 cannot decrease DStablecoin supply at 𝑡 more than

Δ− :=

𝑧
𝑧 + 𝑥

𝑦.

Further, even with additional capital, the speculator cannot decrease the DStablecoin supply at 𝑡 by
more than 𝑦.

[Link to Proof]

Deleveraging affects collateral drawdown through liquidity crises. The result leads to a DStablecoin
market price effect from leverage reduction. This can lead to a deleveraging spiral, which is a feedback
loop in leverage reduction and drying liquidity. In this, the speculator repurchases DStablecoin
to reduce leverage at increasing prices as liquidity dries up as repurchase tends to push up 𝑝𝐷
if
𝑡
outside demand remains the same. At higher prices, more collateral needs to be sold to achieve
deleveraging, leaving relatively less in the system. Subsequent deleveraging, whether voluntary or
through liquidation, becomes more difficult as the price effects compound.

Whether or not a spiraling effect occurs will depend on the demand behavior of stablecoin
holders. The action of the stablecoin holder may actually exacerbate this effect: during extreme
Ether price crashes, stablecoin holders will tend to increase their DStablecoin demand in a ‘flight to
safety’ move. Table 1 illustrates an example scenario of a deleveraging spiral in a simplified setting
with constant unit demand elasticity and in which the speculator’s risk constraint is the liquidation
constraint. Similar results hold under other constant demand elasticities. The system starts in a
steady state. the Ether price declines trigger three waves of liquidations, forcing the speculator to
liquidate her collateral to deleverage at rising costs.

If Ether prices continue to go down,8 the deleveraging spiral is only fixed if (1) more money
comes into the collateral pool to create more DStablecoins, or (2) people lose faith in the system
and no longer want to hold DStablecoins, which can cause the system to fail. There is no guarantee
that (1) always happens.

8Ether price decline can further be facilitated by feedback from large liquidations, as discussed earlier.

Ariah Klages-Mundt and Andreea Minca

13

𝑡
0
1
2
3

Δ𝑡

𝑝𝐸
𝑡
85
83 −3.115
82 −4.105
−4.57
81

L𝑡
100.583
97.468
93.363
88.793

𝑝𝐷
𝑡
0.994
1.026
1.071
1.126

𝑛𝑡
1.8
1.761
1.708
1.644

Table 1. Example scenario of a deleveraging spiral.

This liquidity effect on DStablecoin price makes sense because the stablecoin (as long as it’s
working) should be worth more than the same dollar amount of ETH during a downturn because
the stablecoin comes with additional protection. If the speculator is forced to buy back a sizeable
amount of the coin supply, it will have to do so at a premium price.

One might think the spiral effect is good for stablecoin holders. As we explore in Section 6,
this can be the case for a short-term trade. However, as we will see, the speculator’s ability to
maintain a stable system may deteriorate during these sort of events as it has less control or less
willingness to control the coin supply. Deleveraging effects can siphon off collateral value, which
can be detrimental to the system in the long-term.

This suggests the question: do alternative non-custodial designs suffer similar deleveraging
problems? We compare to an alternative design described in [6]. In this design, the stablecoin is
restricted to pre-defined leverage bounds, at which algorithmic ‘resets’ partially liquidate both
stablecoin holder and speculator positions at $1 price. While this quells the price effect on collateral,
it shifts the deleveraging risk from speculator to stablecoin holder. The stablecoin holder is liquidated
at $1 price but, if they want to maintain a stablecoin position, they have to re-buy in to a smaller
market at inflated price. Of the many designs, it is unclear which deleveraging method would lead
to a system that survives longer.

Results explain real market data. A preliminary analysis of Dai market data suggests that our
results apply. Figure 2a shows the Dai price appreciate in Nov-Dec 2018 during multiple large
supply decreases. This is consistent with an early phase of a deleveraging spiral. Figure 2b shows
trading data from multiple DEXs over Jan-Feb 2019: price spikes occur in the data reportedly from
speculator liquidations [29]. This provides empirical evidence that liquidity is indeed limited for
lowering leverage in Dai markets. Further, as discussed in the next section, Dai empirically trades
below target in many normal circumstances.

Since releasing the initial version of this paper in June 2019, massive liquidation events around
Black Thursday in March 2020 provide additional strong evidence of deleveraging effects in the Dai
market. Figure 3a depicts a ∼ 50% ETH price cash on 12 Mar. 2020, which precipitated a cascade
of cryptocurrency liquidations. Figure 3b depicts the price effects of these liquidations on Dai
prices on DEXs. Speculators deleveraging during this event had to pay premiums of ∼ 10% and face
consistent premiums > 2% weeks into the aftermath. Concurrently, Maker was affected by global
mempool flooding on Ethereum. This additionally contributed to Dai liquidation auctions clearing
at near zero prices, which may in fact have amplified the deleveraging feedback effects. Altogether,
Dai traded at significant premiums over this time despite Maker being in a much riskier state in
terms of collateral and liquidations. See [15] and [5] for further discussion of this event.

4 STABILITY RESULTS
We now characterize stable price dynamics of DStablecoins when the leverage constraint is non-
binding. For this section, we make the following simplifications to focus on speculator behavior:

Ariah Klages-Mundt and Andreea Minca

14

(a)

(b)

Fig. 2. Model Results explain data from Dai market. (a) Dai deleveraging feedback in Nov-Dec 2018 (image
from coinmarketcap). (b) Dai normally trades below target with spikes in price due to liquidations (image
from dai.stablecoin.science).

(a)

(b)

Fig. 3. Black Thursday in March 2020. (a) ∼ 50% ETH price crash (image from OnChainFX). (b) liquidation
price effect on Dai DEX trades (image from dai.stablecoin.science).

• The market has fixed dollar demand at each 𝑡: 𝑤 𝐷

𝑡 A𝑡 = D. This is consistent with the
stablecoin holder having unit-elastic demand, or having an exogenous constraint to put a
fixed amount of wealth in the stable asset.

• Speculator’s expected Ether return is constant 𝑟𝑡 = ˆ𝑟 > 1. This means they always want to

fully participate in the market and is consistent with 𝛾 = 0.

This amounts to setting 𝑥 = D and 𝑦 = −L. Now the DStablecoin market clearing price is 𝑝𝐷
The leverage constraint (assuming L + Δ > 0) becomes

𝑡 = D
L𝑡

.

−𝛽Δ2 + Δ( ˜𝜆(𝑧 + D) − 2𝛽L) + L ( ˜𝜆𝑧 − 2𝛽 − 𝛽L) ≥ 0.

The speculator’s maximization objective becomes ˆ𝑟 Δ D

L+Δ − Δ, which gives

Δ∗ = −L +

√

LD ˆ𝑟 .

Market CapPrice (USD)24h VolDai Charts14. Nov18. Nov22. Nov26. Nov30. Nov4. Dec8. Dec12. DecJan '18May '18Sep '18$50M$60M$70M$0.960000$1.00$1.040Zoom1d7d1m3m1yYTDALLFromNov 12, 2018ToDec 12, 2018Market CapPrice (USD)Price (BTC)Price (ETH)24h Volcoinmarketcap.comAriah Klages-Mundt and Andreea Minca

15

While we prove a stability result in this simplified setting, we believe the results can be extended

beyond the assumption of constant unit-elastic demand.

4.1 Stability if leverage constraint is non-binding

Prop. 5. Assume 𝑤 𝐷

𝑡 A𝑡 = D (DStablecoin dollar demand) and 𝑟𝑡 = ˆ𝑟 (speculator’s expected Ether
return) remain constant. If the leverage constraint is inactive at time 𝑡, then the DStablecoin return is

𝑝𝐷
𝑡
𝑝𝐷
𝑡 −1

√︂ L
D ˆ𝑟

.

=

[Link to Proof]
Supposing that D ≈ L (i.e., the previous price was close to the $1 target) and the constraint is
inactive, Prop. 5 tells us that the DStablecoin behaves stably like the payment of a coupon on a
bond.

Consider estimators for DStablecoin log returns ¯𝜇𝑡 and volatility ¯𝜎𝑡 computed in a similar way
to Ether expectations in Eq. 2.2.1. When the leverage constraint is non-binding, DStablecoin log
returns remain ¯𝜇𝑡 ≈ 0, the contribution to volatility at time 𝑡 is ln 𝑝𝐷
− ¯𝜇𝑡 ≈ 0, and the DStablecoin
𝑡
𝑝𝐷
𝑡 −1
tends toward a steady state with stable price and zero variability. The next theorem formalizes this
result to describe stable dynamics of price and the volatility estimator under the condition that the
system doesn’t breach the speculator’s leverage threshold.

Theorem 1. Assume 𝑤 𝐷

𝑡 A𝑡 = D (DStablecoin demand) and 𝑟𝑡 = ˆ𝑟 (speculator’s expected Ether
return) remain constant. Let L0 = D and ¯𝜇0, ¯𝜎0 be given. If the leverage constraint remains inactive
through time 𝑡, then

L𝑡 = D ˆ𝑟

2𝑡
−1
2𝑡

,

(1 − 𝛿)𝑡 ¯𝜇0 − 𝛿 (1−𝛿)𝑡 −2−𝑡
2−𝑡 (cid:16) ¯𝜇0 − 1
2𝑡 ln ˆ𝑟

2(1−𝛿)−1 ln ˆ𝑟,
(cid:17)
,

if 𝛿 ≠ 1/2
if 𝛿 = 1/2

¯𝜇𝑡 =





¯𝜎 2
𝑡 =

(cid:205)𝑡

𝑘=1(1 − 𝛿)𝑡 −𝑘𝛿
𝑘=1 2−𝑘−1 (cid:16)

2−𝑡 (cid:205)𝑡





(cid:16)

(1 − 𝛿)𝑘 ¯𝜇0 − (1−𝛿)𝑘 −2−𝑘+1 (1−𝛿)

2(1−𝛿)−1
(cid:17) 2

+ 2−𝑡 ¯𝜎 2
0,

(cid:17) 2

ln ˆ𝑟

+ (1 − 𝛿)𝑡 ¯𝜎 2
0,

if 𝛿 ≠ 1/2

if 𝛿 = 1/2

(𝑘/2 − 1) ln ˆ𝑟 − ¯𝜇0

Further, assuming the constraint continues to be inactive and that 𝛿 ≤ 1
exponentially to the steady state L𝑡 → D ˆ𝑟 , ¯𝜇𝑡 → 0, ¯𝜎 2

𝑡 → 0.

2 , the system converges

[Link to Proof]
Notice that if the leverage constraint in the system is reached, we can still treat the system as a
reset of ¯𝜇0 and ¯𝜎0 when we reach a point at which the constraint is no longer binding. While the
system subsequently remains without a binding constraint, we again converge to a steady state
starting from the new initial conditions.

Interest rates and trading below $1. A consequence of Theorem 1 is that the DStablecoin will
trade below target during times in which Ether expectations are high. This is empirically seen in
Figure 2b. An interest rate charged to speculators can balance the market (the ‘stability fee’ in Dai).
This can temper expectations by effectively reducing 𝑟 in Theorem 1. In the stable steady state,
setting the interest rate to offset the average expected ETH return will achieve the price target.
However, this is practically difficult as 𝑟 changes over time and is difficult to measure accurately. It
also depends on holding periods of speculators. It is an open question how to target these fees in a
way that maintains long-term stability.

Ariah Klages-Mundt and Andreea Minca

16

(a) Histogram of DStablecoin returns when leverage
constraint is binding vs. non-binding with constant ˆ𝑟 .

(b) Heat map of volatility under different speculator
𝛾 = 𝛿 memory parameters.

Fig. 4. DStablecoin volatility, 10k simulation paths of length 1000.

4.2 Instability if leverage constraint is binding
When the speculator’s leverage constraint is binding, DStablecoin price behavior can be more
extreme. We argue informally that this can lead to high volatility in our model. The probability
distribution for the leverage constraint to be binding in the next step has a kink at the boundary of
the leverage constraint. In particular, it becomes increasingly likely that the leverage constraint is
binding in a subsequent step due to deleveraging effects described previously. Note that feedback
of large liquidations on Ether price, if added to the model, will add to this effect.

We show such instability computationally in Figure 4a in simulation results. In this figure, the
shape of the inactive histogram reflects the speculator’s willingness to sell at a slight discount
when the leverage constraint is non-binding due to the constant ˆ𝑟 assumption.

We relax this assumption in Figure 4b, which shows the effects on volatility of different speculator
memory parameters. This figure is a heat map/2D histogram. A histogram over 𝑦-values is depicted
in the third dimension (color: light=high density, dark=low density) for each 𝑥-value. Each histogram
depicts realized volatilities across 10k simulation paths using the simulation setup introduced in the
next section and the given memory parameter (𝑥-value). Horizontal lines depict selected percentiles
in these histograms. The dotted line depicts the historical level of Ether volatility for comparison.
In Figure 4b, volatility is bounded away from 0 even in non-binding leverage constraint scenarios;
the distance increases with the memory parameter. This happens because 𝑟 updates faster with a
higher memory parameter. As the speculator’s objective then changes at each step, the steady state
itself changes. Thus we expect some nonzero volatility, although it remains low in most cases.

In not-so-rare cases, however, volatility can be on the order of magnitude of actual Ether volatility
in these simulations. As seen in Figure 5, this result is robust to a wide range of choices for the
speculator’s risk constraint. This suggests that DStablecoins perform well in median cases, but are
subject to heavy tailed volatility.

5 SIMULATION RESULTS
We now explore simulation results from the model considering a wide range of choices for the
speculator’s risk constraint. Unless otherwise noted, the simulations use the following parameter
set with a simplified constant demand assumption (D = 100) and a t-distribution with df=3 to
simulate Ether log returns. This carries over the simplified model from Section 4, although other
choices are also amenable to simulation. Cryptocurrency returns are well known for having very

−0.10−0.050.000.050.100.150.20Log return10−210−1100101102103DensityDStablecoin Returns by Constraint ActivityActiveInactive0.10.20.3Memory Parameter0.000.010.020.030.040.05Volatility (Daily)DStablecoin Volatility vs. Memory ParameterEther volatility70 percentile95 percentileAriah Klages-Mundt and Andreea Minca

17

heavy tails. This choice gives us these heavy tails with finite variance. Note, however, that this
doesn’t capture path dependence of Ether returns. We instead assume Ether returns in each period
are independent. We run simulations on 10k paths of 1000 steps (days) each. This is enough time
to look at short-term failures and dynamics over time. The simulation code is available with full
details at https://github.com/aklamun/Stablecoin_Deleveraging.

Parameter Value

𝑛0
𝑟0
𝜇0
𝜎0
𝛾 = 𝛿
𝛽
𝛼
𝑏

Rationale
4x initial collateralization > typical Dai level
400
Historical daily Ether mult. return 2017-2018
1.00583
0.00162
Historical daily Ether log return 2017-2018
0.027925 Historical daily Ether volatility 2017-2018
0.1
1.5
∼ 1.28
1

∼ Recommended value [21]
Threshold used in MakerDAO’s Dai
Value assuming normal distr. + 𝑎 = 0.1
Consistent with VaR constraint

Note that our simulations study daily movements. We choose this time step to examine these
systems under reasonable computational requirements. More realistic simulations might study
intraday movements. One plausible scenario of a Dai freeze is if the price feed moves too far too
fast instraday, so that speculators don’t have enough time to react before liquidations are triggered
and keepers (who perform actual liquidations) are unable to handle the avalanche of liquidations.
As the price feed in Dai faces an hourly delay in the price feed, hourly time steps are a natural
choice for follow-up simulations. This said, daily time steps can actually be reasonable due to a
behavioral trend in Dai data: most Dai speculators realistically don’t track their positions with very
high frequency as supported by overall high liquidation rates.

5.1 Speculator behavior affects volatility
We compare DStablecoin performance under the following speculator behaviors encoded in the
risk constraint.

Name
Speculator risk constraint
VaRN.1 VaR using 𝑎 = 0.1 + normality assumption
VaRN.01 VaR using 𝑎 = 0.01 + normality assumption
VaRM.1 VaR using 𝑎 = 0.1 + heavy-tailed assumption
VaRM.01 VaR using 𝑎 = 0.01 + heavy-tailed assumption

AC1
AC2
RN

Anti-cyclic constraint, 𝑏 = −0.5, 𝛼 = 0.01
Anti-cyclic constraint, 𝑏 = −0.5, 𝛼 = 0.02
Risk neutral, only faces liquidation constraint

Figure 5 compares the effects on volatility of these behavioral constraints under various Ether
return distributions. These figures are heatmaps/2D histograms similar to that in Figure 4b. The
results suggest that DStablecoins face significant tail volatility (on the order of Ether volatility)
even under comparatively ‘nice’ assumptions on Ether return distributions, such as with significant
upward drift (Figure 5b) and a normal distribution (Figure 5c). Figure 7 depicts relative (% difference)
mean-squared difference of simulated volatility for the different risk management methods vs. a
risk neutral speculator. The mean-squared difference is large, suggesting that the speculator’s risk
management method has a large effect on volatility.

The results suggest how speculator behavior can affect DStablecoin volatility within the model.
Stricter cyclic risk management (e.g., VaR) on the part of the (single) speculator can lead to increased
DStablecoin volatility without improving the safety of the system. Whether countercyclic (setting
constraint to increase leverage during downturns) or cyclic (setting constraint to decrease leverage

Ariah Klages-Mundt and Andreea Minca

18

(a) Ether returns∼ t-distr(df = 3, 𝜇 = 0)

(b) Ether returns∼ t-distr(df = 3, 𝜇 = 𝑟0)

(c) Ether returns∼ normal(𝜇 = 0)

Fig. 5. Heatmaps of DStablecoin volatility for different speculator risk management behaviors.

during downturns), the resulting DStablecoin volatility is connected with how narrow the feasible
region for the constraint becomes. A risk neutral speculator, which has the widest feasible region
for the constraint, leads to the lowest volatility. Stricter risk management serves to reduce the
feasible region. Note that these results may be different if there are multiple types of speculators,
for instance some that are cyclic and others that are countercyclic.

Figure 4b further suggests that a higher speculator memory parameter (lower memory) tends to
increase volatility in typical cases. This makes sense as high memory parameters can lead to noise
chasing on the part of the speculator. Note that keeping the speculator’s expected Ether returns
and variance constant is equivalent to setting a static risk constraint.

5.2 Stable asset failure is dominated by collateral asset returns
We define the DStablecoin’s failure (or stopping) time to be either (1) when the speculator’s
liquidation constraint is unachievable or (2) when the DStablecoin price remains below $0.5 USD.
In these cases, a global settlement would be reasonable, leaving DStablecoin holders with Ether
holdings with high volatility in subsequent periods.

Figure 6 compares the effects on failure time of these behavioral risk constraints. The stopping
time distributions appear comparable across a wide range of selections for the speculator’s risk
constraint. They are additionally comparable across the memory parameters studied above. Figure 7
depicts relative mean-squared difference of simulated stopping times for the different risk manage-
ment methods vs. a risk neutral speculator. In calculating the mean-squared difference, we only

VaRN.1VaRN.01VaRM.1VaRM.01AC1AC2RNSpeculator Risk Management0.000.010.020.030.040.050.060.070.08Volatility (Daily)DStablecoin Volatility vs. Risk ManagementEther volatility70 percentile95 percentileVaRN.1VaRN.01VaRM.1VaRM.01AC1AC2RNSpeculator Risk Management0.000.010.020.030.040.050.060.070.08Volatility (Daily)DStablecoin Volatility vs. Risk ManagementEther volatility70 percentile99 percentileVaRN.1VaRN.01VaRM.1VaRM.01AC1AC2RNSpeculator Risk Management0.000.010.020.030.040.050.060.070.08Volatility (Daily)DStablecoin Volatility vs. Risk ManagementEther volatility70 percentile95 percentileAriah Klages-Mundt and Andreea Minca

19

(a) Ether returns∼ t-distr(df = 3, 𝜇 = 0)

(b) Ether returns∼ normal(𝜇 = 0)

Fig. 6. Heatmaps of DStablecoin failure times for different speculator risk management behaviors.

Fig. 7. Relative mean-squared difference (MSD) of simulated volatility and stopping time for given speculator
strategy vs. risk neutral strategy. Different lines represent different output (volatility or stopping time) and
different return distribution assumptions for the simulations.

include cases in which the failure is realized within the simulation. The mean-squared difference
is small (1-2 orders of magnitudes smaller than for volatility), providing additional evidence that
the stopping time is largely independent of the speculator’s risk management. In particular, a
large proportion of failure events would not have been prevented by different speculator risk
management within the model.

DStablecoin failure probabilities appear to be dominated by Ether returns as opposed to spec-
ulator behavior. The results suggest that DStablecoins may not be long-term stable, even under
comparatively ‘nice’ assumptions for Ether return distributions. To avoid failure, they would
essentially rely on more speculator capital entering the system during downturns.

VaRN.1VaRN.01VaRM.1VaRM.01AC1AC2RNSpeculator Risk Management02004006008001000Stopping Time (Days)DStablecoin Stopping Time vs. Risk Management20 percentile5 percentileVaRN.1VaRN.01VaRM.1VaRM.01AC1AC2RNSpeculator Risk Management02004006008001000Stopping Time (Days)DStablecoin Stopping Time vs. Risk Management5 percentile1 percentile0.0010.010.1110100VaRN.1VaRN.01VaRM.1VaRM.01AC1AC2Relative MSD vs. RN (log scale)Speculator Risk ManagementSimulation Mean-Squared Difference vs. Risk-Neutral Vol, tdistr(μ=0)Vol, tdistr(μ=r0)Vol, normal(μ=0)Stop, tdistr(μ=0)Stop, tdistr(μ=r0)Stop, normal(μ=0)Volatility OutputsStopping Time OutputsAriah Klages-Mundt and Andreea Minca

20

𝑡
0
1
2
3

𝛿 + 𝜀

𝑝𝐸
𝑡
85
85
82
82 −1.083

+1

D𝑡
100
101
101
99.917

Δ𝑡

0.502
−8.716

L𝑡
100.583
101.085
92.369
92.369

𝑝𝐷
𝑡
0.994
0.999
1.093
1.082

𝑛𝑡
1.8
1.806
1.690
1.689

Table 2. Example scenario of a profitable bet on liquidations.

6 STABLECOIN ATTACKS
Attacking a DStablecoin is different than traditional currency attacks. The focus is not on breaking
the willingness of the central bank to maintain a peg. It instead involves manipulating the interaction
of agents. We show that stablecoin design can enable profitable trades against stability that attack
the system. These come from the existence of profitable trades around liquidations and the ability
of miners to reorder and censor transactions to extract value.

6.1 Expanded Model: Adding an Attacker
We consider an expanded model under the fixed outside demand setting of the previous section. In
the expansion, we consider an attacker, who can speculatively enter/exit the DStablecoin market.
The attacker can buy 𝛿 dollar-value of DStablecoin at some time 𝑡 with the goal of selling it at a later
time 𝑠 for 𝛿 + 𝜀. These occurrences change the demand structure: D𝑡 = D + 𝛿, D𝑠 = D − (𝛿 + 𝜀).

6.2 Profitable bets on liquidations
Table 2 illustrates an example scenario for a profitable bet on liquidations. The attacker injects
𝛿 = 1 in demand at 𝑡 = 1, which acquires 1.0008 DStablecoins at 𝑝𝐷
1 . In 𝑡 = 3, after the liquidation,
the attacker is then able to extract 𝛿 + 𝜀 = 1.083 from selling the DStablecoin. This yields a return
of 8.3%. This is akin to a short squeeze on existing speculators. It takes advantage of the fact that
liquidations occur at DStablecoin market rate, which in turn affects the market rate.
≤ 𝛿
𝑝𝐷
𝑜

. Choosing
𝛿 = 4.5, 𝜀 = 0.59 (not optimal) yields a return of 13%. The attacker could also spread out 𝛿 over a
longer period of time to achieve lower purchase prices.

The attacker can do better by choosing 𝛿, 𝜀 to maximize 𝜀 subject to 𝛿+𝜖
𝑝𝐷
2

From a practical perspective, the optimization is sensitive to misestimation of demand elasticity.
While Dai has hit prices as high as $1.37 historically (source: coinmarketcap), it hasn’t typically
reached prices above $1.09. Thus smaller bets (relative to supply) may be safer. Regardless, these
can be large opportunities in large systems. In addition, outside of this model, real implementations
create arbitrage of 5 − 13% to automate liquidations.

6.3 Attacks

Attack 1: An attacker bets on an ETH decline and manipulates the market to trigger and profit
from spiraling liquidations. This uses the short squeeze-like trades in the previous example. It can
also be supplemented with a bribe to miners to freeze collateral top-ups. The attacker could also
enter as a new speculator at the high DStablecoin prices after the attack and thus leverage up at a
discount. Outside of the model, the attack may have a negative effect on the long-term DStablecoin
demand due to the induced volatility. This can be further beneficial to the attacker, who can then
also deleverage in the future at a discount.

Attack 2: The attacker is also a miner and reorganizes the recent transaction history (such as
by initiating a fork) to be on the receiving end of arbitrage oppotunities from liquidations. For

Ariah Klages-Mundt and Andreea Minca

21

instance, following an ETH decline, the miner could trigger and profit from spiraling liquidations.
In a fork, the attacker creates a new timeline that inherits the ETH price trajectory (via oracle
transactions). The attacker can then censor speculator transactions (e.g., collateral top-ups) to trigger
new liquidations and extract profit around all liquidations, which are guaranteed in the timeline. If
the stablecoin system is large, the miner extractable value can be large (and is additive with other
sources of extractable value). This creates the perverse incentive for miners to perform this attack
if the attack rewards are greater than lost mining rewards. This is similar to the time-bandit attack
in [9].

In Attack 1, the attacker takes on market risk as the payoff relies on a future ETH decline
and liquidation. It is a speculative attack that can induce volatility in the stablecoin. In Attack
2, the attacker’s payoffs are guaranteed if the attack fork is successful. These payoffs incentivize
blockchain consensus attack. A possible equilibrium is for miners to collude and share this value.
These attacks occur in a permissionless setting, in which agents can enter/exit at any time with
a degree of anonymity. While in traditional finance, market manipulation rules can be enforced
legally, in decentralized finance, enforcement is only possible to the extent that it can be codified
within the protocol and incentive structure. We leave to future study a full exploration of these
incentive structures in a game theoretic setting based on foundations for blockchain forking models
set in, e.g., [3].

Since the initial release of this paper, this attack surface around stablecoin liquidations was
exploited in related ways to Attack 2. In Attack 2, a miner reorganizes the recent history to extract
profit from arbitrage opportunities from liquidations. In reality on Black Thursday, mempool
manipulation contributed to the clearing of $8m of Dai liquidation auctions at near zero prices [5].

Mitigations. We discuss some preliminary ideas toward mitigating attack potential. Liquidations
could be spread over a longer time period. This could potentially lessen deleveraging spirals by
smoothing demand and increase the costs to a forking attack. However, it presents a trade-off in that
slow liquidations come with higher risks to the stablecoin becoming under-collateralized. We also
suggest tying oracle prices and DEX transactions to recent block history so that a reorganization
attack can’t easily inherit price and exchange history. Practically, however, this may be difficult to
tune in a way that’s not disruptive as small forks happen normally.

7 DISCUSSION
In general, it is impossible to build a stablecoin without significant risks. As speculators participate
by making leveraged bets, there is always an undiversifiable cryptocurrency risk. However, a
stablecoin can aim to be an effective store of value assuming the cryptocurrency market as a whole
is not undermined. In this case, it is conceivable to sustain a dollar peg if the stablecoin survives
transitory extreme events. That is, to achieve long-term probabilistic stability, a stablecoin should
maintain a high probability of survival.

Failure risks. DStablecoins are complex systems with substantial failure risks. Our model demon-
strates that they can work well in mild settings, but may have high volatility outside of these
settings. As we explore in this paper, the market can collapse due to feedback effects on liquidity
and volatility from deleveraging effects during crises. These effects can exacerbate collateral draw-
down. Surviving these events may rely on bringing in increasing amounts of new capital to expand
the DStablecoin supply during such crises. In these events speculators may not always be willing
and able to take these new risky positions. Indeed, there are may examples of speculative markets
drying up during extreme market movements. As we explore below, continued stability during

Ariah Klages-Mundt and Andreea Minca

22

these events additionally relies on new capital entering the system in a well-behaved manner as
profitable attacks are possible.

As suggested by our simulations, stablecoin holders face the direct tail risk of cryptocurrencies.
If the market loses liquidity, there is no guarantee that forced liquidation of speculators’ collateral
will be possible within reasonable pricing limits. Further, volatile cryptocurrency markets can, in
unlikely events, move too fast for speculators to adapt their positions. In these cases, stablecoin
holders can only truly rely on the cryptocurrency value from global settlement.

Remark on oracle risks. The DStablecoin design also relies on trusted oracles to provide real
world price data, which could be subject to manipulation. In MakerDAO’s Dai, for instance, oracles
are chosen by MKR token holders, who vote on system parameters. This opens a potential 51%
attack, in which enough speculators buy up MKR tokens, change the system to use oracles that they
manipulate, and trigger global settlement at unfavorable rates to stablecoin holders while pocketing
the difference themselves when they recover their excess collateral. A hint of manipulation in
oracles or large acquisitions of MKR could potentially trigger market instability issues on its own.
Note that Dai has protections from oracle attacks.9 First, there is a threshold of maximum price
change and an hourly delay on new prices taking effect. This means that emergency oracles have
time to react to an attack. Second, at current prices 51% of MKR is substantially more expensive
than the ETH collateral supply. However, this second point does not have to be true in general–at
least unless Dai holders otherwise bid up the price of MKR for their own security. The value of
MKR is linked to expectations around Dai growth as fees paid in the system are used to reduce
MKR supply. At some point, the expectation may not be enough to lift MKR value above collateral
on its own. This raises the question of whether fees should be used to reduce MKR supply at all.
Alternatively, MKR value could be completely based on the potential value of a 51% attack, which
may also grow with Dai growth, and the value of fees could be put to different uses, as we discuss
further below.

A good fee mechanism may quell deleveraging spirals. Dai imposes fees on speculators when
they liquidate positions (e.g., liquidation penalty, stability fee, penalty ratio). These can amplify
deleveraging effects by increasing deleveraging costs and disincentivizing new capital from entering
the system during crises. An alternative design with automatic counter-cyclic fees could enhance
stability by reducing feedback effects. For instance, fees could be collected while the system is
performing well, but these fees could be removed (or made negative) automatically during liquidity
crises in order to limit feedback effects and remove disincentives to bringing new capital into the
system.

Speculators in Dai can pay back liabilities at any time and come and go from the system, which
raises concerns about herd behavior in crises. A herd trying to deleverage can trigger a deleveraging
spiral. Dynamic fees tuned to inflow/outflow could additionally disincentivize herd behavior to
deleverage at the same time.

An alternative ‘collateral of last resort’ idea in Dai. In Dai, MKR serves a certain ‘last resort’ role
in addition to governance. If there is a collateral shortfall, then new MKR is minted and sold to
cover Dai liabilities making up the shortfall. This may not always be possible as the MKR market
can similarly face illiquidity and the market cap may not be high enough to cover shortfalls. In
some settings, MKR holders might actually have an incentive to trigger a global settlement early
before MKR would be inflated. A Dai shutdown would have some effect on the price of MKR, but
the cost may be small if MKR holders expect a successful relaunch of Dai after the crisis. An early
shutdown is not ideal for Dai holders, as they will want to hold the stable asset for longer during

9Though it is notable that most MKR is reputedly held by just a few individuals within the MakerDAO team.

Ariah Klages-Mundt and Andreea Minca

23

extreme events. In addition to incentive alignment being unclear in MKR’s ‘last resort’ role, the
invocation of the role only helps cover the aftermath of a crisis (an existing shortfall) as opposed to
quelling the effects that cause the crises.

We propose an alternative ‘last resort’ role of governance tokens that instead aims to quell
deleveraging spirals. This could be achieved by automatically positioning the MKR supply as
system collateral against which Dai can be minted to expand supply in crises. To illustrate, if there
is a massive deleveraging by speculators, leading to excess demand for Dai and an inflated Dai
price, then new Dai could be automatically minted against the MKR supply as collateral to help
balance the market. In this way, a deleveraging spiral is damped: should a new wave of speculator
deleveraging be triggered, it will not compound the price effect from the past wave. System fee
revenue could also be put to this use.

Uses of limited fee revenue. Dai produces limited fee revenue, most of which rewards MKR
investors. There is additionally a Dai savings rate that rewards Dai holders using fee revenue and
serves as another tool to balance the Dai market (e.g., to boost demand for Dai when the price is
below target). There is an inherent trade-off in using fee revenue, however. A Dai savings rate uses
this revenue to improve stability in relatively normal settings in which a higher fee itself serves to
balance the market. Alternatively, fee revenue can be channeled to an emergency fund that lessens
the severity of crises–for instance as suggested above. These fees and their potential uses can be
incorporated into our model to compare the effects of different design choices.

Stablecoin risk tools. Our results suggest tools and indicators that can warn about volatility in
DStablecoins. We can find proxies for the free supply, estimate the price impact of liquidations,
and track the entrance of new capital into speculative positions. We can connect this information
with model results to estimate the probability of liquidity problems given the current state. This
information is also useful in valuing token positions in these systems (e.g., Dai, MKR, and the
speculator’s leveraged position).

Some exchanges have bundled select stablecoins into a single market that ensures 1-to-1 trad-
ing (e.g., [13]). In this case, exchanges are essentially providing insurance to their users against
stablecoin failures. These arrangements could lead to a run on exchanges in the event that some
stablecoins fail. It is unclear if these exchanges are subject to regulation to protect users against this,
and it is further unclear if such regulations would be sufficient to account for risks in stablecoins.
Our model provides insight into the risks (to exchanges and users) if such arrangements in the
future include non-custodial stablecoins.

Future directions. We suggest expansions to our model to explore wider settings.
• Incorporate more speculator decisions, such as locking and unlocking collateral and holding
different assets, accommodating speculators with security lending motivation. This makes the
speculator’s optimization problem multi-dimensional. In this expanded setting, speculators
may make more long-term strategic decisions considering whether tomorrow they would
have to buy back stablecoins and at what price.

• Consider multiple speculators with different utility functions who participate in the DStable-
coin market. In this expanded setting, we can consider the conditions under which new
capital may enter the system and formally study the economic attack described above and
the effects of external incentives.

• Incorporate additional assets, such as a custodial stablecoin that faces counterparty risk. This
would allow us to study long-term movements between stablecoins in the space and learn
about systemic effects that could be triggered by counterparty failures. This is further relevant
in evaluating systems like Maker’s multi-collateral Dai. However, this comes with a trade-off

Ariah Klages-Mundt and Andreea Minca

24

of a new counterparty risk that is very hard to measure. In particular, it’s not just custodian
default risk, but also risk of targeted interventions on centralized assets. Such interventions
(e.g., from a government who wants to shut down Dai) could be highly correlated with
cryptocurrency downturns as that is when the system is naturally weakest.

• Incorporate endogenous feedback of liquidations on Ether price, which becomes relevant if
the DStablecoin system becomes large relative to the Ether market. This is similarly important
for endogenous collateral stablecoins like Synthetix sUSD and Terra UST, in which a system
equity-like asset is used as collateral (see [17]).

Additionally, our existing model can be adapted to analyze DStablecoins with different design
characteristics. For instance,

• DStablecoins with more general collateral settlement, in which stablecoin holders can in-
dividually redeem stablecoins for collateral. This is possible, for instance, in bitUSD and
Steem Dollars, and more recently in Celo Dollars. In this case, the stablecoin acts as a perpet-
ual option to redeem collateral, and stablecoin volatility will be additionally related to the
settlement terms.

• DStablecoins without speculator agents (e.g., Steem Dollars, in which the whole marketcap
of Steem acts as collateral, or Celo Dollars, in which Celo reserves act as collateral). In these
systems, stablecoin issuance is automated with the rest of the protocol. Our model can be
adapted by removing speculator decisions and modeling the growth of collateral from block
rewards and growth of stablecoin from other processes.

• Some non-collateralized algorithmic stablecoins. We believe this setting can also be inter-
preted in our model by thinking of implicit collateral that ends up describing user faith in
the system (see [17]). The underlying mechanics would be similar, simply recreating ‘out of
thin air’ the value of the underlying asset as opposed to building on top of the value of an
existing asset. The stability of the system ultimately still relies on how people perceive this
value over time similarly to how perceived value of Ether changes.

ACKNOWLEDGMENTS
We thank David Easley, Steffen Schuldenzucker, Christopher Chen, Akaki Mamageishvili, Peter
Zimmerman, Sergey Ivliev, Tomasz Stanczak, Sid Shekhar, as well as the participants of the ECB
P2P Financial Systems (2019) workshop, Crypto Valley Conference (2019), and Crytpo Economics
Security Conference (2019) for their valuable feedback. This paper is based on work supported
by NSF CAREER award #1653354. AK thanks Lykke, Binance, and Amherst College for additional
financial support.

REFERENCES
[1] Hamed Amini, Damir Filipović, and Andreea Minca. 2015. Systemic risk and central clearing counterparty design.

Swiss Finance Institute Research Paper 13-34 (2015).

[2] Christoph Aymanns and J Doyne Farmer. 2015. The dynamics of the leverage cycle. Journal of Economic Dynamics and

Control 50 (2015), 155–179.

[3] Bruno Biais, Christophe Bisiere, Matthieu Bouvard, and Catherine Casamatta. 2019. The blockchain folk theorem. The

Review of Financial Studies 32, 5 (2019), 1662–1715.

[4] Blockchain.com. 2019. The state of stablecoins. Technical Report. https://www.blockchain.com/ru/static/pdf/

StablecoinsReportFinal.pdf.

[5] Blocknative. 2020. Evidence of Mempool Manipulation on Black Thursday: Hammerbots, Mempool Compression, and

Spontaneous Stuck Transactions. https://www.blocknative.com/blog/mempool-forensics

[6] Y Cao, M Dai, S Kou, L Li, and C Yang. 2018. Designing stable coins. Duo Network Whitepaper, https:// duo.network/

papers/ duo_academic_white_paper.pdf (2018).

[7] Agostino Capponi, W Cheng, and Jay Sethuraman. 2017. Clearinghouse default waterfalls: Risk-sharing, incentives,

and systemic risk. Incentives, and Systemic Risk (August 30, 2017) (2017).

Ariah Klages-Mundt and Andreea Minca

25

[8] cLabs. 2019. An analysis of the stability characteristics of Celo. Technical Report. https://celo.org/papers/Celo_Stability_

Analysis.pdf.

[9] Philip Daian, Steven Goldfeder, Tyler Kell, Yunqi Li, Xueyuan Zhao, Iddo Bentov, Lorenz Breidenbach, and Ari Juels.
[n.d.]. Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability.
In 2020 IEEE Symposium on Security and Privacy (SP). 566–583.

[10] Darrell Duffie, Martin Scheicher, and Guillaume Vuillemey. 2015. Central clearing and collateral demand. Journal of

Financial Economics 116, 2 (2015), 237–256.

[11] Alex Evans. 2019. A Ratings-Based Model for Credit Events in MakerDAO.
[12] Bernardo Guimaraes and Stephen Morris. 2007. Risk and wealth in a model of self-fulfilling currency attacks. Journal

of Monetary Economics 54, 8 (2007), 2205–2230.

[13] Huobi. 19 Oct. 2018. Announcement on the launch of HUSD solution on Huobi Global. https://huobiglobal.zendesk.

com/hc/en-us/articles/360000170601.

[14] Ariah Klages-Mundt. 14 Dec. 2018. The state of stablecoins–update 2018. https://link.medium.com/8rZUYg1c16.
[15] Ariah Klages-Mundt. 6 Apr. 2020. Insights from modeling stablecoins. https://link.medium.com/FLOZ5dbd16.
[16] Ariah Klages-Mundt. Nov. 14, 2019. Vulnerabilities in Maker: oracle-governance attacks, attack DAOs, and

(de)centralization. https://link.medium.com/VZG64fhmr6

[17] Ariah Klages-Mundt, Dominik Harz, Lewis Gudgeon, Jun-You Liu, and Andreea Minca. 2020. Stablecoins 2.0: Economic
Foundations and Risk-based Models. In Proceedings of the 2nd ACM Conference on Advances in Financial Technologies.
59–79.

[18] Ariah Klages-Mundt and Andreea Minca. 2020. While Stability Lasts: A Stochastic Model of Stablecoins. arXiv preprint

arXiv:2004.01304 (2020).

[19] Matteo Leibowitz. 12 Sep 2019. Addressing popular MakerDAO criticisms. The Block. https://www.theblockcrypto.

com/post/39595/addressing-preston-byrnes-makerdao-criticisms

[20] Alex Lipton, Thomas Hardjono, and Alex Pentland. 2018. Digital trade coin: towards a more stable digital currency.

Royal Society open science 5, 7 (2018), 180155.

[21] Jacques Longerstaey. 1996. RiskMetrics—technical document. Technical Report. J.P. Morgan.
[22] MakerDAO. 12 Mar 2020. Black Thursday response thread. https://forum.makerdao.com/t/black-thursday-response-

thread/1433.

[23] MakerDAO. 2017. The Dai stablecoin system. Technical Report. https://makerdao.com/whitepaper/Dai-Whitepaper-

Dec17-en.pdf.

[24] MakerDAO. 2020. Awesome MakerDAO. https://github.com/makerdao/awesome-makerdao
[25] Stephen Morris and Hyun Song Shin. 1998. Unique equilibrium in a model of self-fulfilling currency attacks. American

Economic Review (1998), 587–597.

[26] Satoshi Nakamoto. 2009. Bitcoin: A peer-to-peer electronic cash system. Technical Report. https://bitcoin.org/bitcoin.pdf.
[27] Maureen O’hara. 1997. Market microstructure theory. Wiley.
[28] Nicholas Platias and Marco DiMaggio. 2019. Terra money: stability stress test. Technical Report. https://agora.terra.

money/t/stability-stress-test/55.

[29] Kenny Rowe. 21 Feb 2019. https://twitter.com/kennyrowe/status/1098639092332412929.
[30] Sam M Werner, Daniel Perez, Lewis Gudgeon, Ariah Klages-Mundt, Dominik Harz, and William J Knottenbelt. 2021.

SoK: Decentralized Finance (DeFi). arXiv preprint arXiv:2101.08778 (2021).

[31] Gavin Wood. 2014. Ethereum: A secure decentralised generalised transaction ledger. Technical Report. Ethereum project

yellow paper.

[32] Yi Zhang, Xiaohong Chen, and Daejun Park. 2018. Formal specification of constant product (xy= k) market maker model
and implementation. Technical Report. https://github.com/runtimeverification/verified-smart-contracts/blob/uniswap/
uniswap/x-y-k.pdf.

A DERIVATION OF RESULTS

Prop. 1.

Proof. In each period 𝑡, we determine the leverage constraint by setting ˜𝜆 = 𝜆 and solving for
from the market clearing, we have the following equation for Δ:

Δ. Using the formulation of 𝑝𝐷
𝑡

˜𝜆

(cid:16)
𝑧 + Δ

(cid:17)

𝑥
Δ − 𝑦

= 𝛽 (L + Δ).

Ariah Klages-Mundt and Andreea Minca

26

Given Δ > 𝑦, this transforms to the quadratic equation for Δ

−𝛽Δ2 + Δ(cid:16) ˜𝜆(𝑧 + 𝑥) − 𝛽 (L − 𝑦)

(cid:17)

− ˜𝜆𝑧𝑦 + 𝛽L𝑦 = 0.

This is a downward facing parabola. The speculator’s leverage constraint is satisfied when the
polynomial is positive. The roots, if real, bound the feasible region of the speculator’s constraint.
Due to the requirement that Δ > 𝑦, the feasible set is given by [Δmin, Δmax] ∩ (𝑦, ∞). When there
□
are no real roots, the polynomial is never positive, and so the constraint is unachievable.

Prop. 2.

Proof. By Prop. 1, [Δmin, Δmax] ∩ (𝑦, ∞) is indeed the feasible region. Incorporating the market

clearing, the speculator decides Δ in each period 𝑡 by solving

max

(cid:16)
𝑧 + Δ

𝑟

(cid:17)

𝑥
Δ − 𝑦

− L − Δ

s.t.

Δ ∈ [Δmin, Δmax] ∩ (𝑦, ∞)

This optimization is solvable in closed form by maximizing over critical points. Maximizing the

objective is equivalent to maximizing

𝑓 (Δ) = 𝑟 Δ

𝑥
Δ − 𝑦

− Δ.

We first consider the case of Δ approaching 𝑦 from above and show that this boundary is not

relevant in the maximization. The limit is

lim
Δ→𝑦+
To see this, note that L𝑡 −1 = ¯𝑚𝑡 −1 ≥ 𝑤 𝐷
𝑡 ¯𝑚𝑡 −1, we must
have Δ < 0. Thus the sign of the term that tends to infinity is negative. The limit is −∞ because
the price for the speculator to buy back DStablecoins goes to ∞.

𝑡 ¯𝑚𝑡 −1, and so in order to have L𝑡 = 𝑤 𝐷

𝑓 (Δ) = −∞.

To find the critical points of 𝑓 , we set the derivative equal to zero:

𝑑 𝑓
𝑑Δ

= −

Δ2 − 2Δ𝑦 + 𝑦 (𝑟𝑥 + 𝑦)
(Δ − 𝑦)2

= 0

Assuming Δ ≠ 𝑦, the solutions are the roots to the quadratic Δ2 + −2𝑦Δ + 𝑦 (𝑟𝑥 + 𝑦) = 0. Notice that
the axis of this parabola is at Δ = 𝑦. When there are two real solutions, then exactly one of them
will be > 𝑦. Given 𝑦 ≤ 0 and 𝑥 ≥ 0 and noting 𝑟 ≥ 0, a real solution always exists and the relevant
critical point is

Δ∗ = 𝑦 +

−𝑦𝑟𝑥 .

√

If it is feasible, Δ∗ is the solution to the speculator’s optimization problem. If Δ∗ is not feasible,

then we need to choose along the boundary. The possible cases are as follows.

Suppose Δ∗ < Δmin. Then Δmin is feasible since Δ∗ > 𝑦 implies Δmin > 𝑦. Since 𝑓 is monotone

decreasing to the right of Δ∗, 𝑓 (Δmin) > 𝑓 (Δmax), and so Δmin is the solution.

Suppose Δ∗ > Δmax. By our assumption that the constraint is feasible, we have that Δmax is
feasible. Since 𝑓 is monotone decreasing to the left of Δ∗ on the feasible region, 𝑓 (Δmax) > 𝑓 (Δmin),
□
and so Δmax is the solution.

Ariah Klages-Mundt and Andreea Minca

27

Prop. 3.

Proof. The speculator’s leverage constraint is unachievable when the quadratic has no real

solutions or when all real solutions are < 𝑦. The first case occurs when

(cid:16) ˜𝜆(𝑧 + 𝑥) − 𝛽 (L − 𝑦)

(cid:17) 2

+ 4𝛽 (− ˜𝜆𝑧𝑦 + 𝛽L𝑦) < 0.

Noting that 𝑦 = −𝑤 𝐷 L and L − 𝑦 = L (2 − 𝑤 𝐷 ) and expanding and simplifying terms yields

𝛽 ˜𝜆L

(cid:16)2𝑧𝑤 𝐷 + 2𝑥 (2 − 𝑤 𝐷 )

(cid:17)

− (𝛽L𝑤 𝐷 )2 >

(cid:16) ˜𝜆(𝑥 + 𝑧)

(cid:17) 2

Completing the square by subtracting 4𝛽 ˜𝜆L𝑥 (1 − 𝑤 𝐷 ) from each side then gives the result.

□

Prop. 4.

𝑡 = −Δ 𝑥

Proof. Setting 𝑧 = −Δ𝑝𝐷
Note that ¯𝑚𝑡 = L𝑡 , and so 𝑦 = L (𝑤 𝐷 − 1) = −𝑤 𝐸 L ≤ 0. The term 𝑤 𝐷

Δ−𝑦 gives the lower bound Δ− := 𝑧

𝑡 ¯𝑚𝑡 −1 presents a lower
bound on the size of the DStablecoin market in the next step from the demand side, and so the
speculator can’t decrease the size of the market faster than 𝑦, even with additional capital beyond 𝑧.
As shown above, Δ → 𝑦+ coincides with 𝑝𝐷
𝑡 → ∞. The speculator pays increasingly large amounts
□
to buy back more DStablecoins as liquidity dries in the market.

𝑧+𝑥 𝑦 > 𝑦.

Prop. 5.

Proof. With inactive constraint, L𝑡 =

√

LD ˆ𝑟 , 𝑝𝐷

𝑡 = D√

L D ˆ𝑟 =

√︃ D

L ˆ𝑟 , and 𝑝𝐷

𝑡
𝑝𝐷
𝑡 −1

√︃ D
L ˆ𝑟
D
L

=

√︃ L

D ˆ𝑟 . □

=

Theorem 1.

Proof. It is straightforward to verify L𝑡 = D ˆ𝑟

2𝑡
−1
2𝑡 by induction using L𝑡 =

√

L𝑡 −1D ˆ𝑟 . Then

𝑝𝐷
𝑡
𝑝𝐷
𝑡 −1

√︂ L𝑡 −1
D ˆ𝑟

=

=

√︄

D ˆ𝑟

2𝑡 −1−1
2𝑡 −1
D ˆ𝑟

(cid:16) 2𝑡 −1

−1
2𝑡 −1 −1

(cid:17)

1
2

= ˆ𝑟

= ˆ𝑟 −2−𝑡 .

And so ln 𝑝𝐷
𝑡
𝑝𝐷
𝑡 −1

= −2−𝑡 ln ˆ𝑟 .
Next, as ¯𝜇𝑡 = (1 − 𝛿) ¯𝜇𝑡 −1 + 𝛿 ln 𝑝𝐷
𝑡
𝑝𝐷
𝑡 −1

, it is straightforward to verify by induction that

¯𝜇𝑡 = (1 − 𝛿)𝑡 ¯𝜇0 − 𝛿 ln ˆ𝑟

𝑡
∑︁

𝑘=1

2−𝑘 (1 − 𝛿)𝑡 −𝑘 .

Ariah Klages-Mundt and Andreea Minca

28

Case I:. 𝛿 = 1/2. The series in ¯𝜇𝑡 becomes

𝑡
∑︁

𝑘=1

2−𝑘 (1 − 𝛿)𝑡 −𝑘 =

𝑡
∑︁

𝑘=1

2−𝑘 2−(𝑡 −𝑘) =

𝑡
∑︁

𝑘=1

2−𝑡 =

𝑡
2𝑡

.

Then we have ¯𝜇𝑡 = 2−𝑡 (cid:16) ¯𝜇0 − 1
L’Hopital’s rule. Thus ¯𝜇𝑡 → 0 as 𝑡 → ∞.

2𝑡 ln ˆ𝑟

(cid:17). The first term → 0 since 0 ≤ 𝛿 < 1. The second term → 0 by

The contributing term to volatility at time 𝑡, after substituting and simplifying terms, is

ln

𝑝𝐷
𝑡
𝑝𝐷
𝑡 −1

− ¯𝜇𝑡 =

𝑡/2 − 1
2𝑡

ln ˆ𝑟 − 2−𝑡 ¯𝜇0.

Then DStablecoin volatility evolves according to

𝑡 = (1 − 𝛿) ¯𝜎 2
¯𝜎 2

𝑡 −1 + 𝛿

(cid:16) ln

(1 − 𝛿)𝑡 −𝑘𝛿

(cid:16) ln

(cid:17) 2

− ¯𝜇𝑡

(cid:17) 2

− ¯𝜇𝑘

+ (1 − 𝛿)𝑡 ¯𝜎 2
0

𝑝𝐷
𝑡
𝑝𝐷
𝑡 −1
𝑝𝐷
𝑘
𝑝𝐷
𝑘−1

2−(𝑡 −𝑘)𝛿

(cid:16) 𝑘/2 − 1
2𝑘

ln ˆ𝑟 − 2−𝑘 ¯𝜇0

(cid:17) 2

+ 2−𝑡 ¯𝜎 2
0

2−(𝑡 −𝑘)𝛿2−2𝑘 (cid:16)

(𝑘/2 − 1) ln ˆ𝑟 − ¯𝜇0

(cid:17) 2

+ 2−𝑡 ¯𝜎 2
0

2−𝑘−1 (cid:16)

(𝑘/2 − 1) ln ˆ𝑟 − ¯𝜇0

(cid:17) 2

+ 2−𝑡 ¯𝜎 2
0 .

𝑡
∑︁

𝑘=1

=

=

=

𝑡
∑︁

𝑘=1
𝑡
∑︁

𝑘=1
𝑡
∑︁

𝑘=1

= 2−𝑡

The second line follows from straightforward induction. As 𝑡 → ∞, the series converges from
exponential decay. Then both terms → 0 because of the factor of 2−𝑡 . Thus ¯𝜎 2

𝑡 → 0.

Case II:. 𝛿 ≠ 1/2. The series in ¯𝜇𝑡 is a geometric progression

𝑡
∑︁

𝑘=1

2−𝑘 (1 − 𝛿)𝑡 −𝑘 =

𝑡
∑︁

(1 − 𝛿)𝑡 (cid:16)2(1 − 𝛿)

(cid:17) −𝑘

𝑘=1
(1 − 𝛿)𝑡 (cid:16)2(1 − 𝛿)−1 − 2−𝑡 −1(1 − 𝛿)−𝑡 −1(cid:17)
1 − 2(1 − 𝛿)−1

(1 − 𝛿)𝑡 − 2−𝑡
2(1 − 𝛿) − 1

=

=

Then we have ¯𝜇𝑡 = (1 − 𝛿)𝑡 ¯𝜇0 − 𝛿 (1−𝛿)𝑡 −2−𝑡

2(1−𝛿)−1 ln ˆ𝑟 , which converges to 0 as 𝑡 → ∞.

The contributing term to volatility at time 𝑡, after substituting and simplifying terms, is

ln

𝑝𝐷
𝑡
𝑝𝐷
𝑡 −1

− ¯𝜇𝑡 = (1 − 𝛿)𝑡 ¯𝜇0 −

(1 − 𝛿)𝑡 − 2−𝑡 +1(1 − 𝛿)
2(1 − 𝛿) − 1

ln ˆ𝑟 .

Ariah Klages-Mundt and Andreea Minca

29

The DStablecoin volatility evolves according to

¯𝜎 2
𝑡 =

=

𝑡
∑︁

𝑘=1
𝑡
∑︁

𝑘=1

(1 − 𝛿)𝑡 −𝑘𝛿

(cid:16) ln

𝑝𝐷
𝑘
𝑝𝐷
𝑘−1

(cid:17) 2

− ¯𝜇𝑘

+ (1 − 𝛿)𝑡 ¯𝜎 2
0

(1 − 𝛿)𝑡 −𝑘𝛿

(cid:16)

(1 − 𝛿)𝑘 ¯𝜇0 −

(1 − 𝛿)𝑘 − 2−𝑘+1(1 − 𝛿)
2(1 − 𝛿) − 1

(cid:17) 2

ln ˆ𝑟

+ (1 − 𝛿)𝑡 ¯𝜎 2
0 .

Note that because (1 − 𝛿) ≥ 1/2, we have

|(1 − 𝛿)𝑡 − 2−𝑡 +1(1 − 𝛿)| ≤ (1 − 𝛿)𝑡 + 2−𝑡 +1(1 − 𝛿)

≤ 2(1 − 𝛿)𝑡 .

Thus we have

¯𝜎 2
𝑡 ≤ (1 − 𝛿)𝑡

𝑡
∑︁

(cid:16)

𝛿
(1 − 𝛿)𝑘

(1 − 𝛿)𝑘 ¯𝜇0 +

2(1 − 𝛿)𝑘
2(1 − 𝛿) − 1

(cid:17) 2

ln ˆ𝑟

+ (1 − 𝛿)𝑡 ¯𝜎 2
0

(1 − 𝛿)𝑘𝛿

(cid:16) ¯𝜇0 +

2
2(1 − 𝛿) − 1

(cid:17) 2

ln ˆ𝑟

+ (1 − 𝛿)𝑡 ¯𝜎𝑡
0.

= (1 − 𝛿)𝑡

𝑘=1
𝑡
∑︁

𝑘=1

As 𝑡 → ∞, the series converges from exponential decay. Then both terms → 0 because of the factor
of (1 − 𝛿)𝑡 . Thus ¯𝜎 2
□

𝑡 → 0.

