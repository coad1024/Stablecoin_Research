Currency Stability Using Blockchain
Technology∗

Bryan Routledge†

Ariel Zetlin-Jones‡

12.26.2019

Abstract

To date, the volatility of most cryptocurrency prices has impeded their adoption as a
money. Actively stabilizing cryptocurrency prices with a policy of a peg is diﬃcult.
When a currency is not 100% backed, arbitrary speculative attacks on currencies can
arise from self-fulﬁlling expectations (as in Obstfeld (1996)). Building on Green and
Lin (2003), we derive the optimal conditional policy that considers traders in sequence
and adjusts the conversion rate based on demand-to-date. We show that such a policy
can eliminate the speculative attack since traders late in the sequence have a dominant
strategy not to speculate. We discuss how the conditional peg policy can be implemented
using smart contract blockchain environment such as Ethereum Network.

∗Thanks to Fahad Saleh for helpful comments. We are grateful for the ﬁnancial support of the PNC

Center for Financial Services Innovation at Carnegie Mellon University and The Ripple Foundation.

†Tepper School of Business, Carnegie Mellon University; routledge@cmu.edu.
‡Tepper School of Business, Carnegie Mellon University; azj@andrew.cmu.edu.

1

Introduction

A central component of most blockchain technologies is a token that can be used as a
method of payment. For some blockchains like Bitcoin, the token is a crypto-currency
and its use as a means of payment is its primary purpose. For other blockchains, the
token serves as a “utility token” to perform transactions on the blockchain. An Ether
token, for example, is a means of payment for computer processing on Ethereum Virtual
Machine, the runtime environment for smart contracts in Ethereum blockchain technology.
In either case, the conversion between crypto-currencies and between crypto-currencies and
government issued currencies is important. To date, existing crypto-currencies are simply
too volatile to be an eﬀective medium of exchange or a store of value. Figure 1 plots the
standard deviation of daily USD price changes of Bitcoin from January 2015 to December
2019. Relative to the Euro-Dollar exchange rate, the price of gold, or even the US stock
market, the volatility is an order of magnitude larger.

More generally, currency prices are volatile. Exchange rates ﬂuctuate far more than coun-
try diﬀerences in economic activity or aggregate price levels (Rogoﬀ (2001)). There is a
long history of currency issuers—historically, governments—following policies to stabilize
the price of their currency. Typically these policies involve using a “peg” to a more stable
currency like the U.S. dollar or commodity price like gold. To maintain the peg, the issuer
maintains a stock of reserves (dollars, gold) to redeem their currency at a ﬁxed rate. Cur-
rently, countries such as Qatar, Cuba, and Panama have pegged their exchange rate to the
U.S. dollar. Previously, Mexico and Argentina had pegged to the dollar but abandoned that
policy. For crypto-currencies, Tether has pegged their exchange rate to the U.S. dollar.

Currency stability, even with a policy of a peg is diﬃcult. When a currency is not 100%
backed, it is vulnerable to a speculative attack. If enough traders sell (short) the currency,
these traders can force a full depletion of the government’s foreign reserves leading to a
devaluation of the currency. This means that if each trader believes that enough other
traders will sell (short) the currency, then it is also optimal for each trader to short the
currency in the expectation of a devaluation. As a result, a change in traders’ beliefs alone
about the likelihood that others traders will speculate against the currency is suﬃcient
to induce a run on the currency. Obstfeld (1996) characterizes this mechanism for how
currency pegs can be subject to arbitrary speculative attacks.

The canonical “peg” policy uses a ﬁxed amount of foreign currency reserves, R, and redeems
domestic currency into foreign reserves at a ﬁxed exchange rate e. Should reserves be

exhausted, the currency ﬂoats at rate ef < e. The policy “works” as long as demand for
the foreign currency is not large (relative to R). The policy, however, permits equilibria
with speculative attacks. A single trader, who does not have a fundamental need for a
foreign currency, might choose to trade at e with the anticipation of unwinding the trade
at the ﬂoating rate, ef . The speculative proﬁt, net of a transaction cost t, is e/ef − t.
If this trader believes that all traders will demand redemption, then the trader rationally
anticipates that the currency will depreciate and demands redemption. This canonical
“peg” policy is “unconditional” in the sense that the conversion rate e does not depend on
demand (except of course, after reserves are exhausted).

In contrast, in this paper, we develop a new theory of optimal exchange rate pegs that are
less than 100% backed by foreign (U.S. dollar) reserves and are also immune to speculative
attacks. We do this based on the observation that the classical problem of speculative
attacks arises from the hoc restriction that exchange rate policy be unconditional. We derive
the optimal conditional policy that considers traders in sequence and adjusts the conversion
rate based on demand-to-date. We show that such a policy can eliminate the speculative
attack since traders late in the sequence have a dominant strategy not to speculate. Either
remaining reserves are suﬃciently large to cover possible remaining demand or reserves
are low but the oﬀered conversion rate is suﬃciently low that any further depreciation is
modest. In either case, speculating is not proﬁtable. Iterating on this logic, by backward
induction, speculating is a dominated strategy and there is no equilibrium that supports
a speculative attack. This optimal dynamic exchange rate policy captures much of the
stability of a pegged exchange rate while also being immune to speculative attacks. Our
framework builds on Green and Lin (2003) who use a dynamic liquidity redemption policy
to prevent the classic bank run in a banking model.

The model we develop is agnostic about the currencies involved. It applies equally well to
a government issued ﬁat currency or a blockchain crypto-currency. The particular impor-
tance of blockchain technology is two-fold. First, the new technology has spawned a large
number of coins. CoinMarketCap tracks the market capitalization (price times outstanding
currency) of 200 diﬀerent cryptocurrencies with a total market cap of approximately $200
billion. The ten largest each have a market capitalization over one billion dollars.1 Currency
stability is directly relevant for these blockchain-driven businesses. For many of the coins
like Bitcoin Cash, Ethereum’s Ether, Litecoin, price volatility is as large as Bitcoin (Figure
1); the exchange rate with US dollars is extremely volatile. Several crypto-currencies have
been designed with price stability as the objective. Tether, one of the largest coins (by

1As of December 29, 2019. https://coinmarketcap.com/.

2

market capitalization) with an exchange rate “peg” claims a one-for-one reserves in U.S.
dollars. But the exact mechanism Tether is using to maintain price stability is not trans-
parent and has lead to claims of market manipulation2. It is often hard to verify the reserve
holdings. Tether, for example, severed its relationship with its auditor in January 2018 and
then used $850 million (US dollar) of reserves to cover losses in a related company.3 Other
crypto-currencies that aim for price stability include Nubits, Dia, Basecoin. All of these
protocols feature collateral or reserves at 100% (or more). Others, at least on the surface,
appear to have no workable mechanism for stability other than the name.

Second, and perhaps more importantly, blockchain technology has the potential to credibly
implement complicated peg policies. Specifying and communicating a policy that depends
on real-time currency demand may not be easy. Moreover, conditional policies may appear
less credible since they are more complicated to monitor (think: “rules versus discretion”
as in Kydland and Prescott (1977)). “Smart Contracts,” such as those on the Ethereum
Network are rich state-contingent contracts that are credible since they are immutable and
enforced by an irreversible distributed-ledger blockchain technology. That is, they work
as unchangeable code that run on decentralized computer network outside the control of
the policy setting body. For tokens and currencies inside the Ethereum – so called ERC20
tokens – our conditional peg policy can be implemented with an Ethereum smart contract.
Implementing our policy “across ledgers,” such as a policy linking a cryptocurrency price to
US dollars is more challenging since the US dollars are not transferable inside the blockchain.
Interestingly, many central banks are considering digital or cryptocurrencies. The Marshall
Islands and Venezuela have issued an oﬃcial crypto currency (with limited success). To
date, these and none of the central bank seem to be on a common blockchain network
making that would facilitate an automated “smart contract” currency peg implementation.

What follows is a model without aggregate risk to outline the basic structure. We then
introduce aggregate risk where the population of traders is ﬁnite so fundamental demand
for foreign currency is stochastic. Here, we adapt the sequential-trader mechanism of Green
and Lin (2003) and solve explicitly in a three-person setting. For larger economies, Sec-
tion 4 characterizes some numerical examples. Finally in Section 5, we explore issues of
implementation using the Ethereum smart-contracting blockchain as a concrete example.

2Griﬃn and Shams (2018). https://www.bloomberg.com/graphics/2018-tether-kraken-trades/
3See New York State Attorney General Letitia James press release of April 25, 2019. https://on.ny.

gov/356dsbf.

3

2 A Model of Currency Crises without Aggregate Risk

In this section, we describe a theoretical model of currency crises in the spirit of Obstfeld
(1996) and Morris and Shin (1998). We demonstrate that the existence of an equilibrium
resembling a speculative attack is an artifact of an ad hoc restriction on the policy space.
When a government (or currency issuer) is permitted to use state-contingent policies to
defend an exchange rate peg, then the speculative attack equilibrium does not exist.

2.1 Model Environment

The model economy lasts for two periods and features a continuum of measure one of traders.
Each trader owns one unit of crypto-pesos. While we describe their ﬁat endowments at
crypto-pesos, for the purpose of our theory one may equivalently think of these as units
of paper currency. The economy features two goods: crypto-goods and foreign goods. We
normalize the price of the crypto-good to be 1 (in crypto-pesos) while the price of the foreign
good in period t = 0, 1 is et crypto-pesos.

Before the beginning of period 0, each trader is identical and has a privately observed,
uninsurable risk of being of type C or type F . Each trader learns their own type at the
beginning of period 0. With probability µF > 0, traders are of type F , whom we refer
to as foreign (consumption) traders, and care only about period 0 consumption of foreign
goods. With probability µC > 0, traders are of type C, whom we refer to as crypto traders,
and care only about period 1 consumption of a bundle of foreign and crypto-goods. Given
x units of crypto-pesos in period 1, we assume that a crypto trader’s preferences are such
that she will spend a portion λx > 0 of her crypto-pesos on crypto goods and a portion
(1 − λ)x of her crypto pesos on foreign goods netting her a total consumption bundle of
[(1 − λ)e1 + λ]x.

In addition, we allow traders to convert crypto-pesos into foreign currency in period 0 (at
price e0), store the foreign currency until period 1, and convert back into crypto-pesos (at
price 1/e1) in period 1 as a form of speculation. We assume that this speculation bears a
ﬁxed cost t > 0 denominated in crypto-pesos. Formally, let dj
t denote the units of crypto-
pesos trader j requests to convert into foreign currency in period t, let dt = (dj
t )j∈[0,1], and
let (φ0(d0), φ1(d0, d1)) denote the fraction of crypto-pesos the trader is able to convert into
foreign currency in period 0 and period 1. (We deﬁne φt for given exchange rate policies
below.)

4

Since foreign traders only care about period 0 consumption, each such trader will always
submit dj
0 = 1. Crypto traders may wish to speculate by submitting a conversion request
of dj
0 > 0 depending on their perceptions of the path of exchange rates. Note that given
(et, φt), a crypto trader who submits conversion demand dj
0 in period 0 will enter period 1
with

1 = 1 − φ0(d0)dj
xj

0 +

φ0(d0)dj

0 − t1

[dj

0>0]

(1)

e0
e1

crypto-pesos (with 1 as an indicator function). The amount dj
1 reﬂects the un-coverted
crypto-pesos, 1 − φ0(d0)dj
0, the period 1 value of the crypto-pesos converted in period 0
φ0(d0)dj
(denominated in crypto-pesos), e0
0, less any transaction cost. Our assumption on
e1
preferences implies that such a trader will submit a conversion demand dj
1 in
period 1. Finally, we assume that foreign investors stand willing to convert crypto-pesos
into foreign currency at a ﬂoating price ef .

1 = (1 − λ)xj

Given a path of exchange rates e = (e0, e1), conversion rates φ = (φ0, φ1), and foreign
currency demands d = (d0, d1), each trader j ∈ [0, 1] has utility function of the form

(cid:40) u(e0φ(d0)dj
0)

U (dj

0; e, φ, d) =

(cid:16)(cid:2)(1 − λ)[φ1(d0, d1)e1 + (1 − φ1(d0, d1))ef ] + λ(cid:3) xj

u

(cid:17)

if j is of type F

if j is of type C

(2)

1

where xj

1 is given by (1).

2.2 Optimal Policy

We envision a policy maker that chooses an optimal exchange rate policy. We refer to the
policy maker as a government but this could be a currency board or a crypto-currency
issuer. The government has an initial endowment of R0 foreign reserves. The policy choice
is an exchange rate policy (e0(d0), e1(d0, d1), φ0(d0), φ1(d0, d1)) that specifyies exchange and
conversion rates in each period as a function of the relevant history. The exchange rate
policies must be feasible.

Deﬁnition 1: An exchange rate policy is feasible, if and only if for all dt,

(cid:90)

e0(d0)φ0(d0)

dj
0dj ≤ R0
(cid:90)

e1(d1)φ1(d0, d1)

dj
1dj ≤ R0 − e0(d0)φ0(d0)

(cid:90)

dj
0dj.

(3)

(4)

5

Optimal Policy with Limited Contingency Policies. Motivated by Obstfeld (1996),
we now place a restriction on the class of policies the government may consider and demon-
strate that under this restriction, the optimal exchange rate policy admits a speculative
attack equilibrium. Consider ﬁrst a government that defends an exchange rate peg—a ﬁxed
e0 in our model—until it runs out of reserves in which case it converts demand uniformly in
period 0 and allows the exchange rate to ﬂoat to ef in period 1. We refer to such a policy
as a limited contingency policy.

Deﬁnition 2: An exchange rate policy is a limited contingency policy if it satisﬁes

e0(d0) = ¯e0 ∀d0

φ0(d0) = 1 ∀d0 such that ¯e0

(cid:90)

dj
0dj ≤ R0

φ0(d0) = R0/[¯e0

(cid:90)

dj
0dj] ∀d0 such that ¯e0

(cid:90)

dj
0dj > R0.

(5)

(6)

(7)

We note two important observations about limited contingency policies. First, if the gov-
ernment is not able to defend the peg against a given level of foreign currency demand, then
it necessarily exhausts its supply of foreign reserves and allows the exchange rate to ﬂoat in
period 1 (or, for all such d0, it follows that φ1(d0, d1) = 0). Second, when the government is
not able to defend the peg, it treats all depositors who demand conversion equally. These
two features of limited contingency policies play a key role in allowing for the possibility of
speculative equilibria.

Consider next the problem of the government choosing among limited contingency exchange
rate policies to maximize the expected utility of the traders subject to feasibility constraints
and a no speculation constraint which ensures cypto traders prefer to submit a bid dj
0 = 0
rather than dj
In such a case, it is immediate that the government will choose
0 > 0.
φ0(d0) = φ1(d0, d1) = 1 when (cid:82) dj
1dj = (1 − λ)µC and will set ¯e0 and ¯e1 to
solve

0dj = µF and (cid:82) dj

max µF u (¯e0) + µCu ((1 − λ)¯e1 + λ)

subject to the feasibility constraints (3)-(4) and the speculation constraint,

u ((1 − λ)¯e1 + λ) ≥ u

[(1 − λ)¯e1 + λ]

(cid:18)

(cid:21)(cid:19)

− t

.

(cid:20) ¯e0
¯e1

(8)

(9)

Since the feasibility constraint (4) necessarily binds, if the no speculation constraint is slack,
an optimum exchange rate policy is characterized by the optimality condition,

u(cid:48)(¯e0) = u(cid:48)

(cid:18) R0 − µF ¯e0
µC

(cid:19)

+ λ

6

(10)

which implies ¯e0 = R0 + µCλ. To verify this value of ¯e0 is optimal, one need only verify the
feasibility and no speculation constraint, which yields the following proposition.

Proposition 1: Suppose µF < R0 and λ suﬃciently close to 1.4 Then the optimal limited
contingency policy satisﬁes

¯e0 = R0 + µCλ, ¯e1 =

1
1 − λ

(R0 − µF λ)

where ¯e1 is deﬁned for d1 such that (cid:82) dj

1dj = (1 − λ)µC.

Notice that as λ → 1, if traders believe that crypto traders will not speculate, then traders
should rationally anticipate an appreciation of the currency. As a result, a single crypto
trader will ﬁnd speculation to be an unproﬁtable strategy. Since each crypto trader’s best
response to the belief that other crypto traders will not speculate is to also not speculate,
no speculation is an equilibrium of the optimal limited contingency policy.

Moreover, note that when µF < R0, the government’s policy satisﬁes µF ¯e0 < R0 < ¯e0.
This inequality implies that while the government chooses a policy that will not exhaust
its reserves if no crypto traders demand currency in period 0, this limited contingency
policy will necessarily exhaust all of the government’s reserves if all crypto traders demand
conversion.

Consider then a crypto trader’s incentives to speculate when she believes all other crypto
traders will also speculate (choose dj
0 = 1). Under these beliefs, the crypto trader rationally
anticipates φ0(d0) = R0/¯e0 and φ1(d0, d1) = 0. As a result, her payoﬀs from not speculating
are given by u((1 − λ)ef + λ) and from speculating (with dj

0 = 1) are given by

(cid:18)

[(1 − λ)ef + λ]

u

(cid:20)

1 −

R0
¯e0

+

¯e0
ef

R0
¯e0

(cid:21)(cid:19)

− t

.

(11)

It follows that whenever (R0/ef ) − (R0/¯e0) ≥ t, the crypto trader will ﬁnd it optimal to
speculate. We have proved the following lemma.

Lemma 2: If Ro
gency policy admits an equilibrium where all crypto traders speculate.

R0+µC λ ≥ t (or ef is suﬃciently small), then the optimal limited contin-

ef − R0

We have shown that limited contingency policies suﬃce to deliver eﬃcient insurance ar-
rangements against traders uncertain needs for foreign currency. However, as in Obstfeld

4Formally, we require (R0 + µC λ)(1 − λ)/[R0 − µF λ] ≤ t.

7

(1996), such policies allow for too much volatility in exchange rates in the sense that they
also admit other equilibria. Note that if the ﬂoating exchange rate ef is suﬃciently small,
then small changes in ef would induce no change in the optimal exchange rate policy—its
solution under Proposition 1 is independent of the ﬂoating rate for such values. However,
under any equilibrium selection that admits the speculative equilibrium as an outcome (e.g.
under a sunspot selection criteria), the model would feature variation in the ﬂoating rate
price of crypto-pesos.

We now examine optimal policies without the ad hoc restriction on policy contingencies
and demonstrate that such polices can eliminate the possibility of speculative equilibrium.

Optimal Policy with Contingent Policies. Consider next the unrestricted problem
of choosing any feasible exchange rate policy to maximize ex ante expected utility of the
traders. Clearly, in an equilibrium in which only foreign traders submit demand for foreign
currency in period 0, the outcomes ¯e0 and ¯e1 from Proposition 1 are the same. The only
diﬀerence with arbitrarily contingent policies is that the government is not permitted to
change the period 0 exchange rate it oﬀers when total demand in period 0 diﬀers from µF .

For example, suppose that ef < R0 and consider the following policy5:

e0(d0) =

(cid:40)

R0 + µCλ if (cid:82) dj
if (cid:82) dj
ef

0dj = µF
0dj (cid:54)= µF

, e1(d1) =

(cid:40) 1

1−λ (R0 − µF λ)
ef

if (cid:82) dj
if (cid:82) dj

1dj = µC
1dj (cid:54)= µC

,

(12)

and

φ0(d0) =

(cid:40)

1 if (cid:82) dj
0 if (cid:82) dj

0dj = µF
0dj (cid:54)= µF

, φ1(d0, d1) =

(cid:26) 1 if (cid:82) dj

0dj = µF and (cid:82) dj

1dj = (1 − λ)µC

0 otherwise

.

(13)
Under this policy, if no crypto traders plan to speculate, Proposition 1 implies that each
crypto trader prefers not to speculate. Alternatively, if any fraction of crypto traders are
believed to speculate, then each crypto trader expects to receive u((1 − λ)ef + λ) should
she not speculate and u([(1 − λ)ef + λ][1 − t]) should she choose to speculate. Hence, the
policy trivially rules out alternative equilibria. More generally, there is a large class of
policies which implement the eﬃcient outcome in this economy while admitting a unique
(no speculation) equilibrium. We state this result in the following lemma.

5Given our results in Section 3, the reader should view the assumption ef < R0 as an innocuous sim-
plifying assumption for exposition that ensures the simple policy described in the text rules out speculative
equilibrium.

8

Lemma 3: There exist exchange rate policies (with arbitrary contingencies) that implement
the eﬃcient outcome.

We view Lemma 3 as exchange rate policy analogue to the usefulness of suspension con-
tracts in the literature on bank runs beginning with Diamond and Dybvig (1983). In that
literature, the anticipation that the bank will suspend convertibility (of deposits to cash)
deposits provides patient depositors with the knowledge that their deposits are safe; the
anticipation of suspension, therefore, removes the incentives to run. In our model, the antic-
ipation that the government will abandon its peg (before conversion into foreign currency)
removes the incentives of crypto traders (those who do not truly require foreign currency)
to speculate into foreign currency.

3 Exchange Rate Policy with Aggregate Risk

In this section, we show that even when the government faces aggregate uncertainty over
fundamental demand for foreign currency, optimal exchange rate policies are immune to
ﬂuctuations driven purely by traders’ speculative motives. We show that the government
may eliminate the possibility of speculative equilibria even when its policies are required re-
spect some constraints that naturally arise in this environment, such as a form of sequential
service.

3.1 Model Environment with Aggregate Risk

The model environment is essentially the same as that in Section 2 except for two modiﬁ-
cations. First, we modify the number of traders so that there are J > 3 traders (instead
of a continuum of measure 1). As before, at the beginning of period 0, each trader learns
whether their type is C or F and µC > 0 and µF > 0 represent the probability that a given
trader is of each type.

This ﬁrst modiﬁcation implies that the model now features aggregate risk to the number
of crypto (and foreign) traders. One natural interpretation of this risk in our context
is that it reﬂects aggregate uncertainty in the fundamental demand for crypto-currencies.
Critically, this source of aggregate risk implies that after observing a large volume of foreign
currency demand (perhaps larger than expected), a government cannot determine whether
this demand reﬂects speculative demand in anticipation of a depreciation or a fundamental

9

shock to demand for (domestic) crypto-pesos. Our aim in the rest of this section is to analyze
the implications of this uncertainty for the robustness of the government’s optimally chosen
exchange rate policies.

Our second modiﬁcation changes the timing and information of actions in the game: we
assume that each trader j ∈ J chooses a strategy of foreign currency demand dj
0 ∈ {0, 1}
sequentially with the knowledge of the history of actions chosen by previous traders i < j.
As before, a choice of dj
0 = 0 reﬂects a choice by the trader to not demand foreign currency—
to not speculate—and a choice of dj
0 = 1 reﬂects a choice to demand foreign currency, or
speculate. Equivalently, we treat a reported demand dj
0 = 1 as a report that the trader is a
foreign trader and a reported demand dj
0 = 0 as a report that the trader is a crypto trader.

Given this timing and information modiﬁcation, it is natural to examine how optimal ex-
change rate policies perform when the government has to convert crypto-pesos into foreign
currency for traders sequentially. Below, we explicitly deﬁne policies that respect a sequen-
tial service constraint. We view this modiﬁcation as critical to examining the robustness of
our results given that the most straightforward policy to eliminate speculative attacks in
the model without aggregate risk exploited full knowledge of total foreign currency demand.

3.2 Optimal Policy

Since the government serves traders sequentially given a remaining stock of foreign currency
reserves and we will allow for history-contingent exchange rate policies, we may deﬁne an
exchange rate policy simply as plans for period 0 and period 1 exchange rates. To deﬁne
history-dependent exchange rate policies, we ﬁrst deﬁne the history of foreign currency
demands, Dj
0) for all j ∈ {1, . . . , J}. Then, an exchange rate policy is simply
a set of functions {(ej
0 ))j∈{1,...,J}, e1(DJ

0, . . . , dj
0(DJ

0 = (d1

0 )}.

Deﬁnition 3: An exchange rate policy satisﬁes sequential service if and only if for all j,
ej
0(DJ

0 ) is measurable with respect to Dj
0.

In other words, exchange rate policies satisfy sequential service as long as for each trader
j, the exchange rate they receive depends only on the trader’s reported foreign currency
demand and the reported demands of traders who have previously submitted demands to
the government.

Given an initial stock of foreign currency reserves and an exchange rate policy, the foreign
currency reserves remaining after the jth trader submits their demand in period 0, dj
0,

10

satisﬁes

Rj

0(Dj

0) = Rj−1

0

(Dj−1
0

) − dj

0ej

0(Dj

0).

(14)

Given a sequential service constraint, the government chooses an exchange rate policy to
solve the following program.

max E

J
(cid:88)

j=1

(cid:104)
0u(ej
dj

0(Dj

0)) + (1 − dj

0)u (cid:0)(1 − λ)e1(DJ

0 ) + λ(cid:1)(cid:105)

subject to the reserve transition equations, (14), the feasibility constraints

∀j ∈ {1, . . . , J} and Dj−1

0

,

0(Dj
ej

0) ≤ Rj−1

0

(Dj−1
0

)

∀DJ
0 ,

(1 − λ)e1(DJ
0 )

J
(cid:88)

j=1

(1 − dj

0) ≤ R0 −

J
(cid:88)

j=1

0ej
dj

0(Dj
0)

and the incentive constraints for crypto-traders,

(15)

(16)

(17)

∀Dj

0, E

(cid:104)

u (cid:0)(1 − λ)e1(DJ

0 ) + λ(cid:1)(cid:12)

(cid:12) Dj
0

(cid:105)

(cid:34)

≥ E

u

(cid:32)
(cid:104)

(1 − λ)e1( ˆDJ

0 ) + λ

(cid:34)

(cid:105)

0( ˆDj
ej
0)
e1( ˆDJ
0 )

− t

(cid:35)

Dj
0

(cid:35)(cid:33)(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

(18)

where the expectations in (18) are with respect to DJ
, 1, dj+1
and ˆDj
0

0, . . . , dj−1

0 = (d1

, . . . , dJ

0 ).

0

0 or ˆDJ

0 and where ˆDj

0 = (d1

0, . . . , dj−1

0

, 1)

If we conjecture (and later verify) that the incentive constraints are slack, then we may
solve for the optimal exchange rate policy by way of a straightforward backward induction
argument. In particular, for any DJ
0 and any
given level of foreign currency reserves remaining at the beginning of period one, R, the
optimal period one exchange rate e1(DJ

0). Then, for any DJ

0 , let Θ(DJ

0 ) = (cid:80)

j(1 − dj

0 ) solves

W (Θ(DJ

0 ); R) = max Θ(DJ

0 )u ((1 − λ)e + λ)

(19)

subject to the feasibility constraint, Θ(DJ
reserves beyond period 1, it is immediate that for all DJ

0 )(1 − λ)e ≤ R. Since there is no reason to retain
0 )(1 − λ)] and

0 , e(DJ

W (Θ(DJ

0 ); R) = Θ(DJ

0 )u

(cid:18) R
Θ(DJ
0 )

0 ) = R/[Θ(DJ
(cid:19)

+ λ

.

(20)

We proceed in similar fashion to deﬁne the government’s value function in period 0 for each
possible trader’s position, j. This value function depends on the remaining reserves of the
government, R, and the total number of previous reports where traders reported that they

11

are crypto traders, Θ(Dj−1
). We omit the dependence of Θ on Dj−1
The government’s value function in period 0 for trader j then satisﬁes

0

0

to simplify notation.

V j
0 (Θ; R) = max
e≤R

µF

(cid:104)

u(e) + V j+1

0

(Θ; R − e)

(cid:105)

+ µCV j+1

0

(Θ + 1; R)

(21)

with the convention V J+1

0

(Θ; R) = W (Θ; R).

The program described by (19)-(21) is straightforward to solve given functional forms for
preferences and a given J either analytically or computationally. Next, we focus our analysis
to an economy featuring exactly three traders to highlight theoretically certain features of
the optimal exchange rate policy and traders’ incentives to speculate (or not). Below, we
examine more general economies computationally.

3.3 The Three Trader Economy

Consider a sample economy where J = 3. Analysis, detailed in Appendix A reveals the
following optimal policy.

Proposition 4: Suppose J = 3 and u(c) = − exp(−αc). Then,

log D

−

R
3

e1
0(R) =

e2
0(Θ; R) =

2
3α
R
2 + Θ
R
1 + Θ
e1(Θ; R) = 1[Θ≥1]

e3
0(Θ; R) =

−

1 + Θ
α(2 + Θ)

(cid:20)
µF exp

log

(cid:18)

−αλ

Θ
1 + Θ

(cid:19)

(cid:21)
+ µC exp (−αλ)

+

Θ
1 + Θ
R
Θ(1 − λ)

λ

+ 1[Θ=0]ef

where D is a function of the fundamental parameters µC, µF , λ and α that satisﬁes D ≤ 1.

It is straightforward to show that as µC → 1, the period 0 exchange rates satisfy ej
0 →
(R + 2λ)/3. For a relatively high fraction of crypto-traders, then, the government’s optimal
policy “pegs” the exchange rate for traders in period 0. Note also that e3
0(0; R) = R so that
in the case where traders 1 and 2 both report they are foreign, the government is prepared
to exhaust its remaining reserves for the ﬁnal trader in case she also reports she is a foreign
In this case, the government is prepared to abandon its policy for period 1 and
trader.
allow the exchange rate to ﬂoat.

We now demonstrate that this policy is immune to purely speculative equilibria. Our
approach mirrors that used by Green and Lin (2003) to demonstrate that bank runs do

12

not occur under the optimal liquidity insurance arrangement with ﬁnitely many traders
in the canonical bank-run model of Diamond and Dybvig (1983). Formally, we will show
by way of a backward induction argument that independent of the actions of the ﬁrst two
traders, trader 3 always prefers to report her type (foreign or crypto trader) truthfully and
therefore does not speculate. This result implies that when trader 2 is a crypto trader and
must decide whether to report truthfully or not, she knows that independent of her report,
the probability trader 3 reports she is a crypto trader is equal to the objective probability
that trader 3 is a crypto-trader which is equal to µC. Given these objective probabilities,
we show that independent of the ﬁrst trader’s report, trader 2 always prefers to report
truthfully and therefore does not speculate when she is a crypo-trader. A similar result
holds for trader 1.

This backward induction argument implies that when the government implements the opti-
mal policy described in Proposition 4, the game (among traders) has a unique equilibrium
in which only foreign traders demand foreign currency in period 0. In this sense, the optimal
policy is immune to speculative equilibria.

To show these results, we begin by considering the incentives of trader 3 when she is a crypo-
trader (given our preference structure, a foreign trader will always report she is foreign and
submit a demand for foreign currency in period 0). Truth-telling, or choosing d3
0 = 1 for
this trader is a dominant strategy if and only if for all Θ and R

(1−λ)e1(Θ+1; R)+λ ≥ (cid:2)(1 − λ)e1(Θ; R − e3

(cid:124)

(cid:123)(cid:122)
Consump. per Crypto-Peso

0(Θ; R)) + λ(cid:3)
(cid:125)

(cid:20)

(cid:124)

e3
0(Θ; R)
e1(Θ; R − e3
0(Θ; R))
(cid:123)(cid:122)
Spec. Proﬁt

(cid:21)

− t

. (22)

(cid:125)

Since trader 3 is last, there is no residual uncertainty about the total number of foreign and
crypto-traders. As a result, this trader simply compares the payoﬀ she will receive from
reporting truthfully to that of lying or speculating. The left-hand side of (22) represents the
consumption (of foreign and crypo-goods) of the last trader if she does not speculate where
she understands that the period 1 exchange rate will be given by e1(Θ + 1; R). The right-
hand side represents her period 1 consumption payoﬀ per unit of crypto-pesos multiplied
by her speculative proﬁt. Notice that this trader recognizes that by mis-representing her
type, she inﬂuences the period 1 exchange rates. In particular, if Θ = 0 so that the ﬁrst two
traders have reported that they are foreign traders, trader 3 recognizes that by mis-reporting
her type, the government simply reduces the exchange rate.

Using the optimal policies from Proposition 4, one may show that (22) holds when Θ ≥ 1

13

if and only if

R
1 + Θ

+ 1 ≥ −t

(cid:20) R
1 + Θ

+ 1 −

(cid:21)

1
1 + Θ

and holds when Θ = 0 if and only if

R + λ ≥

(cid:104)

(1 − λ)ef + λ

(cid:105) (cid:20) R

(cid:21)
ef − t

.

(23)

(24)

Notice that as λ → 1, (23) requires (R + Θ)(1 + t) + 1 ≥ 0 which always holds while (24)
requires

1 + t ≥ R

.

(25)

(cid:21)

(cid:20) 1
ef − 1

The inequality (25) places a lower bound on the ﬂoating rate that we will impose at R = R0
to guarantee the third trader always prefers to report truthfully. Notice that the lower
bound in (25) necessarily lies below the upper bound on ef implied by the assumption in
Lemma 2.

Consider next the incentives of trader 2 to speculate or not when she is a crypto-trader.
These incentives depend critically on the reported type of trader 1 along with the remaining
reserves available to the government. When trader 1 reports she is a crypto-trader, trader
2 will prefer to report she is a crypto-trader when

µF u

(cid:104)
(1 − λ)e1(2; R0 − e3

(cid:105)
0(2; R0)) + λ

+ µC u [(1 − λ)e1(3; R0) + λ]

(cid:32)

≥ µF u

(cid:104)
(1 − λ)e1(1; R0 − e2

0(1; R0) − e3

0(1; R0 − e2

(cid:105)
0(1; R0))) + λ

(cid:34)

e1(1; R0 − e2

0(1; R0 − e2

0(1; R0)))

e2
0(1; R0)
0(1; R0) − e2

(cid:32)

+ µC u

(cid:104)
(1 − λ)e1(2; R0 − e2

(cid:105)
0(1; R0)) + λ

(cid:34)

e2
0(1; R0)
e1(2; R0 − e2

0(1; R0))

(cid:35)(cid:33)

− t

.

(cid:35)(cid:33)

− t

(26)

On both the left-hand and right-hand side of (26), the probabilities represent the objective
probability that trader 3 is a foreign or crypto-trader. If trader 2 reports truthfully and
does not demand foreign currency, then she faces risk in the period 1 exchange rate she
will receive arising from the possible reports of trader 3. The same is true when trader
2 speculates although in this case the trader also bears risk in her speculative proﬁts.
Substituting for the optimal policy rules, we may compute this incentive constraint as a

14

function of fundamentals and the reserves of the government R0:6

µF u

(cid:18) 1
R0 +
3
(cid:32)(cid:20) 1
3
(cid:32)(cid:20) 1
3

+ µCu

≥ µF u

R0 +

(cid:19)

λ

+ µCu

(cid:18) 1
3

(cid:19)

R0 + λ

2
3

1
3

1
α

log B +

(cid:21) (cid:34)
λ

1
2

R0 +

1
3

1
α

log B + λ

1

(1 − λ) (cid:2) 1
3 R0 + 1
3
(1 − λ) (cid:2) 1
1

1

3

1

3 R0 − 2

α log B(cid:3)
α log B − 1
2 λ
α log B(cid:3)
3 R0 − 2

1

3
1
α log B

3 R0 + 1

3

(cid:21) (cid:34)

(cid:35)(cid:33)

− t

(cid:35)(cid:33)

− t

(27)

where B = µF exp(−αλ/2) + µC exp(−αλ). Notice that by the concavity of u(·), to show
(27) holds, it suﬃces to show that u (cid:0) 1
3 λ(cid:1) is larger than the utility the trader receives
from the probability weighted average consumption the trader receives from speculating. In
Appendix A, we show that as λ → 1, this suﬃcient condition is equivalent to the requirement
that

3 R0 + 2

R0 +

≥ −t

R0 +

log B

− t

+ µC

.

(28)

(cid:20) 1
3

1
3

1
α

(cid:21)

(cid:104) µF
2

(cid:105)

1
3

2
3

In Appendix A, we use similar logic to show that, a suﬃcient condition to ensure that
truth-telling is a dominant strategy for trader 2 when trader 1 has reported she is a foreign
trader is

1
2

R1 +

1
2

λ ≥ µF

(cid:32)
(cid:104)
(1 − λ)ef + λ

(cid:105)

(cid:34) R1

(cid:35)(cid:33)

− t

2 − 1
2α log D
ef
(cid:21) (cid:34)

+µC

(cid:32)(cid:20) R1
2

+

1
2α

log D + λ

(1 − λ) (cid:2) R1
R1
2 + 1

2 − 1
2α log D

2α log D(cid:3)

(29)

(cid:35)(cid:33)

− t

where again D is the same positive constant from Proposition 4.

If indeed the suﬃcient conditions (23), (24), (28), and (29) hold, then we may determine the
incentive constraint for the ﬁrst trader. Towards this end, the expected utility associated
with truthful reporting for Trader 1 is given by

U tt = µ2

Cu ((1 − λ)e1(3; R0) + λ)
+µF µCu (cid:0)(1 − λ)e1
+µCµF u (cid:0)(1 − λ)e1
F u (cid:0)(1 − λ)e1
+µ2

(cid:0)2; R0 − e2
(cid:0)2; R0 − e3

(cid:0)1; R0 − e2

0(1; R0)(cid:1) + λ(cid:1)
0(2; R0)(cid:1) + λ(cid:1)

0(1; R0) − e3

0(1; R0 − e2

0(1; R0))(cid:1) + λ(cid:1) .

(30)

6Recall that in this case we assume the ﬁrst trader reports she is a crypto-trader and therefore the

government has not used up any reserves for the ﬁrst trader.

15

The expected utility associated with speculation is given by

U spec = µ2

C u

(cid:32)

(cid:104)
(1 − λ)e1(2; R0 − e1

(cid:105)
0(R0)) + λ

(cid:34)

e1
0(R0)
e1(2; R0 − e1

0(R0))

(cid:35)(cid:33)

− t

(cid:32)

(cid:32)

+ µF µC u

+ µC µF u

(cid:104)
(1 − λ)e1(1; R0 − e1

0(R0) − e2

0(0; R0 − e1

(cid:105)
0(R0))) + λ

(cid:104)
(1 − λ)e1(1; R0 − e1

0(R0) − e3

0(1; R0 − e1

(cid:105)
0(R0))) + λ

(cid:34)

(cid:34)

(cid:32)

+ µ2

F u

(cid:105)
(cid:104)
(1 − λ)ef + λ

(cid:34) e1

0(R0)
ef

(cid:35)(cid:33)

− t

e1(1; R0 − e1

0(0; R0 − e1

0(R0)))

e1(1; R0 − e1

0(1; R0 − e1

0(R0)))

e1
0(R0)
0(R0) − e2
e1
0(R0)
0(R0) − e1

(cid:35)(cid:33)

− t

(cid:35)(cid:33)

− t

(31)

In Appendix A, we show that as λ → 1, a suﬃcient condition for U tt ≥ U spec is given by

R0
3

+

1
3

1
α

log B +

1
2

≥ − tp2

(cid:20) R0
3

+ 1 +

1
3

1
α

(cid:21)

log D

− tµF p

− tpµF

(cid:20) R0
3

+

1
2

+

1
3

1
α

(cid:21)

log D

+ µ2
F

log D +

(cid:20) R0
3
(cid:34) R0

+ 1 +

1
1
3
α
1
3 − 2
α log D
3
ef

(cid:21)

log C

1
α

1
2
(cid:35)

− t

.

(32)

With these conditions in hand, we then have the following result.

Theorem 5: For λ and µC in a neighborhood of λ = µC = 1 and 1 + t ≥ R0[ 1
optimal policy in Proposition 4 admits a unique equilibrium with no speculative trade.

ef − 1], the

The proof is immediate given the suﬃciency conditions, (23), (24), (28), (29), and (32). The
two limits play independent, but complementary roles in the proof of Theorem 5. Notice
from Proposition 4 that as λ → 1, e1(Θ; R) → ∞ as long as R > 0. Whenever Θ > 0,
the government’s optimal policy retains reserves into period 1 so that in any such state
crypto traders expect the exchange rate to actually appreciate from their opportunity to
trade in period 0 until period 1. This expected appreciation reduces their incentives to
speculate since they expect to end up with a negative holding of crypto-pesos after bearing
the transaction costs of speculating.

This logic fails, however, in the state where all traders report they are foreign traders—an
event which occurs with strictly positive probability in the ﬁnite trader economy. As a
result, a crypto-trader in an early position, such as the ﬁrst trader, may expect to earn
speculative proﬁts from a depreciation in the event that traders 2 and 3 happen to be
foreign traders. As µC → 1, the likelihood of this proﬁtable event tends to 0, though, and
the losses the trader earns in other states of the economy dominate leading the trader to
prefer not to speculate.

As we show next, by of numerical simulations, however, these limiting results are not par-
ticularly special. That is, we show that in many cases, the optimal exchange rate policy is
dominant strategy incentive compatible even if on average, the optimal policy features no
appreciation between periods 0 and period 1.

16

4 Large, Finite Economies

The model presented so far has focussed on the period-zero exchange rate of sequential
trader j, ej
0, relative to the period one exchange rate e1. The optimal policy consider-
ing the trades that have happened prior to j’s arrival sets ej
0 such that speculative trade
across ej
0 and e1 is an iteratively dominated strategy. We are aiming towards a strategy
we can implement on a blockchain. So the real-time dynamics of rates throughout period
zero are interesting.
In particular, does the stochastic path of rates within period zero,
e0,1 , ..., ej
, ..., eJ
0 and period one rate e1 allow for speculative trade. Here we explore
this with a numerical example.

0, ej+1

0

To solve for the optimal exchange rate policy, we solve recursively the dynamic program
of the policy maker speciﬁed in equations (20) and (21). As above, this does not include
any no-speculation constraints – we can check to see if they are slack in the optimal policy.
There are three state variables relevant to the optimal policy. The environment here has a
ﬁnite horizon, so the policy depends on trader order, j ∈ {1, ..., J}. Next, at trader j, the
policy depends on the behavior of the people who have arrived before j. It turns out, and
this is easy to see by inspecting equations (20) and (21), that the behavior prior to j’s arrival
is captured by the number of prior traders that are type C, Θj ∈ {0, 1, ..., j − 1}, and the
level of reserves available, R ∈ [0, R0]. Solving this numerically is straightforward. Of the
state variables, only reserves needs to be approximated numerically with a grid and linear
interpolation. Finally, we also assume the ﬂoating rate is suﬃciently low that the optimal
policy exchange rate is higher. This implies that reserves are allocated to the traders and,
in this setting, no additional reserves are incoming.

The parameters of the simulation are arbitrary – this is too stylized an example to calibrate.
Here, traders have CRRA preferences with (mild) constant relative risk aversion of 0.75. We
consider J = 100 traders. Consistent with the spirit of our setting, most are are expected
to be type C with µC = 0.85 and µF = 1 − µC = 0.15. To make the example interesting,
we need the currency board’s initial level of reserves to be sensible. If reserves are too low,
particularly with respect to date one demand, then it is not feasible to support the exchange
rate. Given the speciﬁc preferences in equation (2), this translates to initial reserves that
are above the expected intrinsic demand from the type C, i.e., R > JµC(1 − λ). The JµC is
the expected number of C people and 1 − λ is the strength of their preference for the foreign
currency. For our choice of R, here we happen to use R = 2, this implies a λ close to one.
Here we use λ = 0.97. Similarly, if the reserves are too high, akin to one-for-one backing,
then there is no worry of speculative trade. Again, roughly, we need reserves not to be large

17

with respect to total expected demand JµF + µC(1 − λ). This leads to a calibration where
e1 is not mechanically large relative to ej
0.

Figure 2 summarize the simulations. The vertical axis is the exchange rate (e). The
horizontal axis is the position of the trader arrivals (j and with j=J+1 as e1). With a
ﬁnite number of traders, our setting has aggregate risk as in Section 3, so the exchange rate
oﬀered to j is ex ante stochastic. Here we simulate paths the economy (100 paths) with
draws that assigns each trader j to C with probability µC or F with probability µF . The
solid and thick line is the mean across simulations. The shaded regions show the 25 – 75
percentile range (darker red) and the 10 – 90 percentile range (lighter red). As a boundary,
the top line is the exchange rate policy that would result in the (unlikely) event all traders
were C. Similarly, the bottom line is the case all traders are F .

0

Figure 2 highlights a few elements of the model. First note the exchange rate is, on average,
ﬂat. There is no trend that will tempt a type C trader to sell at ej
0 in hopes of repurchasing
later at an expected lower value of ej+n
or e1. In fact, in this example we do not need a
particularly large value for the transaction cost to rule out speculation. Here, the expected
value of the speculative trade is close to zero. Given the variance of such a trade is not zero,
risk aversion, in addition to any transaction cost, dissuades speculation. The red bands in
Figure 2 highlight the variance of the exchange rate policy. The exchange rate reacts to
traders reporting C or F . Notice that the reaction of the optimal exchange rate to a trader
j’s type is stronger when j is larger. That is, as the uncertainty resolves about the number
of C traders, Θ, the optimal policy allocates reserves more aggressively between the two
types.

To see how the backward induction approach rules out a speculative attack equilibrium, see
Figure 3. Here, across all four panels, the draws of all the simulations are identical. The
ﬁgure highlights how the optimal policy reacts to trader reports. In Figure 3, panel (a), the
reports of traders j = 10, 11, 12 are set to C (top line) or type F (bottom line). For the
bottom line where three type F has been reported, the optimal policy has depreciated the
exchange rate in response to this unusual (given µF = 0.15) event. Note that path of the
exchange rate from j = 13 and forward is ﬂat and will not support proﬁtable speculation.
Panels (b), (c), and (d) are analogous but move the position of the traders we set. For panel
(d), when the traders j = 80, 81, 82 are set to F the exchange rate devaluation is stronger
(compare with panel (a)). Starting at j = 80, the sting of three F types is a much larger

18

fraction of the remaining traders to come. Hence the larger reaction.

5

Implementation Discussion

The model environment we have presented is not speciﬁc to the currencies involved. How-
In
ever, the conditional exchange rate policy is well suited to some blockchain settings.
particular, some blockchains facilitate “smart contracts.” The smart contracts are not legal
contracts that require court enforcement. Instead, the smart contracts are scripts and as-
sociated data (or states) that are stored and executed on a distributed platform. They are
contracts in that they are credible enforced by an irreversible distributed-ledger blockchain
technology. Since our conditional peg policy depends on real-time currency demand, it may
be hard to communicate, make credible, and monitor. So implementing the policy via a
smart contract would help.

The Ethereum Network is the largest (measured by market capitalization) blockchain setting
with a smart contracting environment. Ethereum is also Turing-complete meaning it oﬀers a
rich set of possible contracts. The coding environment for Ethereum, “Solidity,” is an object-
oriented language that is designed for the distributed setting – executed code has to yield
the same result for everyone on the distributed network who might update the blockchain.
One important standardized object is the ERC20 tokens.7 ERC20 tokens have standard
properties of an asset in that they can be owned and transferred. Of course, whether or
not these assets serve as a currency is separate issue. ERC20 tokens are typically the
“coins” that are created and sold when a new blockchain-related business on the Ethereum
Network does a “Initial Coin Oﬀering” (ICO). Often these tokens of the ICO are like
tickets that give access to the soon-to-be-created service or application. Filecoin, as an
example, is used to rent ﬁle storage space.8 The standardization means these tokens can
span contracts that otherwise have diﬀerent authors and distinct businesses. That is, we
can write a contract/script that exchanges one ERC20 token for another (or for Ether, the
primary cryptocurrency on Ethereum’s network) even if we are unrelated to the contracts
that created the coins.

Creating and deploying a smart contract to implement our conditional peg policy is, in

7The term “ERC20” stands for Ethereum Request For Comments with 20 to distinguish it from other

standards discussions.

8It is a separate and interesting question as to why these businesses are choosing to use a separate
token for access as opposed to just pricing in terms of, say, Ethereum’s Ether. Presumably, some motive
for the “pre-sale” of tokens is capital structure (Davydiuk, Gupta, and Rosen (2019)). Other motives are
coordination and commitment in the industrial organization of the business (Lee and Parlour (2019), Li and
Mann (2018), and Goldstein, Gupta, and Sverchkov (2019)).

19

principle, straightforward. Imagine we were using a stock of Ether reserves, R, to support
an ERC20 coin using a policy function calculated as in the Section 4. Our smart contract
script would allow users to exchange their ERC20 coin for Ether at the rate ej
0(Θj) with
j as an index of the trader and Θj tracking the state variable of how many ERC20 trades
have occurred prior to j.9 The Ethereum protocol facilitates transparency. The underlying
Solidity code can be published and it is straightforward to check that the published source
code matches the compiled code deployed on the blockchain.10 Similarly, the protocol
facilitates commitment by making contracts immutable.11

The key to eliminating speculative attacks is that traders are in a known queue. In ej
0(Θj),
the j is the trader’s known place in the queue and condition their decision on their location.
One standard solution for ordering is to code the “ordering” as a separate function in
the contract. Traders ﬁrst transaction is to “join” the queue. The order the transactions
appear on the blockchain creates the observable queue prior to trading.12 From Figure 2,
note that traders earlier in the queue face less uncertainty about the exchange rate. So a
worry with letting a “join” transactions create the queue is that traders have an incentive to
inﬂuence their position in the queue. On Ethereum, they can do this using the transaction
cost.13 Alternatively, assigning each trader to a (pseudo)random place in the queue, as
happens in the simulations in Section 4, is not straightforward. The distributed nature of
Ethereum requires scripts to be deterministic – any computer can run/re-run the smart
contract code will yield the same result. Generating pseudo-random numbers in smart
contracts is a challenge in many settings – gambling, for example – and there are a variety
of possible solutions.14 We leave the exact implementation to future work but it is not an
insurmountable task.

ERC20 tokens and Ether currency are both intrinsic to the Ethereum Network. Ownership

9We omit the many “user interface” details like functionality to quote a price prior to trade.
10This is done via a “hash” of the code. See

https://tokenmint.io/blog/how-to-verify-ethereum-smart-contracts-source-code.html.
11A “self-destruct” function that would remove the contract would need to be explicitly incorporated into

the published source code.

12Ordering transactions in a blockchain is a key outcome of the consensus protocol. Transactions are
ordered in blocks and blocks are ordered in a chain. A node processing transactions (a “miner”) orders
transactions when constructing a block. Diﬀerent miners can receive transactions in diﬀering orders. Usually
this does not matter as only a single minder will create a valid block, update the blockchain, and miners
work on new blocks. When (nearly) simultaneous blocks occur, this lack of consensus about ordering is
called a fork. Ethereum has a sophisticated set of rules for resolving these classes. For more on consensus in
blockchains see: Biais, Bisiere, Bouvard, and Casamatta (2019) and Ebrahimi, Routledge, and Zetlin-Jones
(2019).

13Users submitting transactions and calls to smart contracts on Ethereum pay a transaction cost (“gas”).

Setting a high “gas limit” can increase the priority of the transaction.

14See Ahmed (2019) for one example.

20

and control is entirely contained on the Ethereum blockchain. In this setting, our condi-
tional peg policy is implementable on the same blockchain (with the complications we noted
above). With assets outside the blockchain – dollars, pesos, gold – this is obviously not the
case. Even with cryptocurrencies like Bitcoin and Ethereum that use unconnected separate
blockchains, implementing a conditional peg policy cannot be done entirely with a smart
contract. The extra step that is needed is a legal framework that links the dollars to the
blockchain. In the Ethereum setting, for example, this would consist of issuing an ERC20
token that is a legal claim to the oﬀ-chain dollars. This transaction is the blockchain analog
of creating an asset-backed security. Once created, the ERC20 token serves as the reserve
currency in a smart contract. Interestingly, much of the active development of blockchain
technology is at the boundary between assets and the blockchain. For example, the Aus-
tralian Stock Exchange is developing blockchain for securities settlement and. Ripple and
Inter-Ledger-Protocol standards look to link payments across blockchains. An interesting
policy question for central banks creating new digital currencies is how interoperable they
should be with existing blockchains.

6 Conclusion

We have shown that the classical problem of speculative attacks against an under-collateralized
currency peg arises from an hoc restriction that exchange rate policy be unconditional. We
have shown that the optimal conditional policy that considers traders in sequence adjusts
the conversion rate based on demand-to-date. The optimal conditional policy eliminates
the speculative attack since traders late in the sequence have a dominant strategy not to
speculate.

A signiﬁcant concern with the optimal conditional policy we derive is the required degree
of trust that it requires. Speciﬁcally, one must believe that policymakers will abide by
the speciﬁed, complicated policy (ex post).
Implementing this policy using blockchain-
based smart contracts removes the scope for moral hazard by the policymaker and therefore
persuades individuals that the speciﬁed conditional policy will actually be implemented. In
this context, the key value of blockchain is in its ability to generate trust that policies will
be implemented as speciﬁed by policymakers.

21

References

Ahmed, S. (2019): “Niguez Randomity Engine — How to generate random numbers in Ethereum?
— Secure generation and usage of pseudo-random numbers on the Ethereum Blockchain,”
Whitepaper http://bit.ly/RNG-Scheich.

Biais, B., C. Bisiere, M. Bouvard, and C. Casamatta (2019): “The blockchain folk theorem,”

The Review of Financial Studies, 32(5), 1662–1715.

Davydiuk, T., D. Gupta, and S. Rosen (2019): “De-crypto-ing signals in initial coin oﬀerings:

Evidence of rational token retention,” Carnegie Mellon University Working Paper.

Diamond, D. W., and P. H. Dybvig (1983): “Bank runs, deposit insurance, and liquidity,”

Journal of political economy, 91(3), 401–419.

Ebrahimi, Z., B. Routledge, and A. Zetlin-Jones (2019): “Getting Blockchain Incentives

Right,” Carnegie Mellon University Working Paper.

Goldstein, I., D. Gupta, and R. Sverchkov (2019): “Initial coin oﬀerings as a commitment

to competition,” University of Pennsylvania Working Paper.

Green, E. J., and P. Lin (2003): “Implementing eﬃcient allocations in a model of ﬁnancial

intermediation,” Journal of Economic Theory, 109(1), 1 – 23.

Griffin, J. M., and A. Shams (2018): “Is Bitcoin Really Un-Tethered?,” University of Texas

Working Paper.

Kydland, F. E., and E. C. Prescott (1977): “Rules rather than discretion: The inconsistency

of optimal plans,” Journal of political economy, 85(3), 473–491.

Lee, J., and C. A. Parlour (2019): “Consumers as Financiers: Crowdfunding, Initial Coin

Oﬀerings and Consumer Surplus,” University of California-Berkeley, Working Paper.

Li, J., and W. Mann (2018): “Initial coin oﬀerings and platform building,” George Masson

University Working Paper.

Morris, S., and H. S. Shin (1998): “Unique Equilibrium in a Model of Self-Fulﬁlling Currency

Attacks,” American Economic Review, 88(3), 587–597.

Obstfeld, M. (1996): “Models of currency crises with self-fulﬁlling features,” European economic

review, 40(3-5), 1037–1047.

Rogoff, K. (2001): “Why not a global currency?,” American Economic Review, 91(2), 243–247.

22

A Analysis of the Three Trader Economy

A.1 Proof of Proposition 4

In this section, we solve the ﬁnite trader model when there are 3 traders with utility function
u(c) = − exp(−αc). We solve the model using backward induction in closed form. The value of the
currency board of entering period 1 with reserves R and θ crypto-traders to be paid is

W (θ, R) = θu

(cid:19)

+ λ

.

(cid:18) R
θ

where we have used the fact in period 1, the government always uses up all of its resources,
ore1(θ; R) = R

θ(1−λ) .

Period 0 exchange rates for the 3rd Trader. Suppose 2 traders have already arrived, θ of them
have reported they are crypto-traders, and the government has R reserves outstanding.
If the
trader reports she is a crypto-trader, then the currency board pays nothing out and obtains utility
W (θ + 1, R). If the trader reports she is foreign, then the currency board chooses e3
0(θ; R) to solve

Assuming the resource constraint (e ≤ R) is slack, this maximization requires e3

0(θ; R) to satisfy

max
e≤R

u(e) + W (θ, R − e).

or

u(cid:48)(e) = u(cid:48)

(cid:18) R − e
θ

(cid:19)

+ λ

,

e3
0(θ; R) =

R
1 + θ

+

θ
1 + θ

λ.

Note, e3

0(θ; R) ≤ R as long as λ ≤ R. We may deﬁne a value function for the government as

V3(θ, R) = µF [u(e3

0(θ; R)) + W (θ, R − e3

0(θ; R))] + µCW (θ + 1, R).

Using the optimal policy, e3

0(θ; R), we ﬁnd

V3(θ, R) = µF (1 + θ)u

(cid:19)

(cid:18) R + θλ
1 + θ

+ µC(1 + θ)u

(cid:18) R + (1 + θ)λ
1 + θ

(cid:19)

.

Period 0 exchange rates for the 2nd trader. We ﬁnd e2

0(θ; R) as the solution to

max
e≤R

u(e) + V3(θ, R − e).

Using the solution to V3(θ, R), we may ﬁnd e2

0(θ; R) as the exchange rate that satisﬁes
(cid:18) R − e + (1 + θ)λ
1 + θ

+ µCu(cid:48)

(cid:19)

(cid:19)

.

(cid:18) R − e + θλ
1 + θ

u(cid:48)(e) = µF u(cid:48)

23

Given CARA utility, this implies

exp(−αe) = µF exp

−α

(cid:18)

(cid:20) R + λθ
1 + θ

−

e
1 + θ

(cid:21)(cid:19)

(cid:18)

+ µC exp

−α

(cid:20) R + (1 + θ)λ
1 + θ

−

e
1 + θ

(cid:21)(cid:19)

.

Solving for e, we conclude

e2
0(θ; R) =

R
2 + θ

−

1 + θ
α(2 + θ)

(cid:20)
µF exp

log

(cid:18)

−αλ

(cid:19)

θ
1 + θ

+ µC exp (−αλ)

.

(cid:21)

As above, we may deﬁne a value function for the government facing the 2nd trader in period 0:

V2(θ, R) = µF [u(e2

0(θ; R)) + V3(θ, R − e2

0(θ; R))] + µCV3(θ + 1, R).

Period 0 exchange rates for the 1st trader. We ﬁnd e1

0 as the solution to

max
e≤R

u(e) + V2(0, R − e).

Note that

e2
0(0; R) =

R
2

−

1
2α

log [µF + µC exp(−αλ)] .

If we let C denote the constant,

C = µF + µC exp(−αλ)

then e2

0(0; R) = R/2 − 1

2α log C and R − e2

0(0; R) = R

(cid:20)

V2(0, R) = µF

u

(cid:18) R
2

−

1
2α

(cid:19)

log C

+ V3

0,

+

log C

+ µCV3(1, R).

2 + 1
(cid:18)

2α log C. Then
(cid:19)(cid:21)

R
2

1
2α

Using the closed form for V3(θ, R), V2 satisﬁes

(cid:20)

V2(0, R) =µF

u

1
2α

−

(cid:18) R
2
(cid:20)
2µF u

+ µC

(cid:19)

log C

+ µF u

(cid:19)

(cid:18) R + λ
2

+ 2µCu

+

(cid:18) R
2
(cid:18) R
2

1
2α

(cid:19)

log C

+ µCu

(cid:18) R
2

+

1
2α

(cid:19)(cid:21)

log C + λ

(cid:19)(cid:21)

+ λ

.

The optimal exchange rate policy satisﬁes

u(cid:48)(e1

0) =

d
dR

ˆV2(0, R − e1

0),

or

u(cid:48)(e1

0) =µF

(cid:20) 1
2

u(cid:48)

(cid:18) R − e1
0
2

log C

−

1
2α
(cid:18) R − e1
0 + λ
2

(cid:19)

+

1
2

µF u(cid:48)

(cid:19)

+ µCu(cid:48)

(cid:18) R − e1
0
2
(cid:18) R − e1
0
2

(cid:20)
µF u(cid:48)

+ µC

+ λ

.

(cid:19)

log C

+

1
2

µCu(cid:48)

(cid:18) R − e1
0
2

+

1
2α

(cid:19)(cid:21)

log C + λ

+

1
2α

(cid:19)(cid:21)

24

Using the functional form of u(·), the optimal policy satisﬁes

exp(−αe1

0) = exp

(cid:18)

−α

(cid:20) R − e1
0
2

(cid:21)(cid:19) (cid:26)

µF

(cid:20) 1
2

C

1
2 +

1
2

µF C

−1
2 +

1
2
(cid:19)

−1
2 exp (−αλ)

(cid:21)

µCC

(cid:21)
+ µC exp (−αλ)

.

(cid:20)
µF exp

(cid:18)

−α

+ µC

λ
2

Let D denote the constant,

D = µF

(cid:20) 1
2

C

1
2 +

1
2

µF C

−1
2 +

1
2

µCC

−1
2 exp (−αλ)

(cid:21)

(cid:20)
µF exp

(cid:18)

−α

+ µC

+ µC exp (−αλ)

.

(cid:21)

(cid:19)

λ
2

Since C = µF + µC exp(−αλ), it follows that

D = µF B

1

2 + µC

(cid:20)
µF exp

(cid:18)

−

αλ
2

(cid:19)

(cid:21)
+ µC exp(−αλ)

.

Then,

or

−αe1

0 = −

αR
2

+

αe1
0
2

+ log D

e1
0 =

R
3

−

2
3α

log D.

We have shown

e1
0(R) =

R
3

−

2
3α

log D

e2
0(θ; R) =

e3
0(θ; R) =

e1(θ; R) =

−

R
2 + θ
R
1 + θ
R
θ(1 − λ)

+

1 + θ
α(2 + θ)

θ
1 + θ

λ

.

(cid:20)
µF exp

log

(cid:18)

−αλ

(cid:19)

θ
1 + θ

+ µC exp (−αλ)

(cid:21)

We also have the transition function for reserves. Let R0
i (θ) denote the reserves left to the government
when the ith trader arrives in period 0 and θ previous traders have declared they are crypto-traders.
Then,

R0
R0

1 = R0
2(θ) = R0 − (1 − θ)e1
0

and, remaining reserves at the third person depend on the speciﬁc history since it is possible that
0(R0) (cid:54)= e2
e1

0(1; R0). We have

R0

3(θ) =






R0
R0 − e1
R0 − e2
R0 − e1

0(R0)
0(1; R0)
0(R0) − e2

0(0; R0 − e1

0(R0))

if θ = 2
if θ1 = 0 and θ2 = 1
if θ1 = 1 and θ2 = 0
if θ = 0

25

Notice, as µC → 1 (so that all agents are crypto with high probability), we ﬁnd

e1
0(R) →

R + 2λ
3

, e2

0(1; R) →

R + 2λ
3

, e3

0(2; R) =

R + 2λ
3

and in this sense the exchange rate is “pegged.”

A.2 Proof of Theorem 5

Incentives for the 3rd Trader. The incentive constraint when θ ≥ 1 requires

(1 − λ)e1(θ + 1; R) + λ ≥ (cid:2)(1 − λ)e1(θ; R − e3

0(θ; R)) + λ(cid:3)

(cid:20)

e3
0(θ; R)
e1(θ; R − e3

0(θ; R))

(cid:21)

− t

where

Hence,

and

e1(θ; R) =

R
θ(1 − λ)

and e3

0(θ; R) =

R + θλ
1 + θ

.

R − e3

0(θ; R) = R −

R + θλ
1 + θ

=

θ(R − λ)
1 + θ

e1(θ; R − e3

0(θ; R)) =

R − λ
(1 + θ)(1 − λ)

.

These results imply the incentive constraint may be re-written as

R
1 + θ

+ λ ≥

(cid:20) R − λ
1 + θ

+ λ

(cid:21) (cid:20) (R + θλ)(1 − λ)

(cid:21)

− t

.

R − λ

We show that as λ → 1 this incentive constraint necessarily holds. Taking limits of both sides
(assuming R (cid:54)= 1, we have

R
1 + θ

+ 1 ≥ −t

Multiplying by 1 + θ and simpliﬁng, we have

(cid:20) R
1 + θ

+ 1 −

1
1 + θ

(cid:21)

.

(R + θ)(1 + t) + 1 ≥ 0

which holds for any R ≥ 0, θ ≥ 1 and t ≥ 0. When θ = 0, we require

(1 − λ)e1(1; R) + λ ≥

(cid:20)
(1 − λ)e3

0(0; R) + λ

(cid:21)

e3
0(0; R)
ef

− t (cid:2)(1 − λ)ef + λ(cid:3) .

Since e1(1; R) = R/(1 − λ) and e3

0(0; R) = R, this constraint requires

As λ → 1, this condition requires

Rλ + λ + t[(1 − λ)ef + λ] ≥ λ

R
ef

1 + t ≥ R

(cid:21)

(cid:20) 1
ef − 1

.

26

Since this should hold for all R and R is necessarily (weakly) decreasing in the sequence of traders,
is suﬃces to impose

1 + t ≥ R0

(cid:21)
(cid:20) 1
ef − 1

.

We then have for all R and θ that for λ suﬃciently close to 1, the last trader has a dominant strategy
to report truthfully.

Incentives for the 2nd Trader. Suppose ﬁrst that trader 1 is a crypto-trader so that θ = 1. The
incentive constraint is

µF u (cid:2)(1 − λ)e1(2; R0 − e3

(cid:18)

≥ µF u

+ µCu

(cid:2)(1 − λ)e1(1; R0 − e2
(cid:18)
(cid:2)(1 − λ)e1(2; R0 − e2

0(2; R0)) + λ(cid:3) + µCu [(1 − λ)e1(3; R0) + λ]
(cid:20)
0(1; R0))) + λ(cid:3)

0(1; R0) − e3

0(1; R0 − e2
(cid:20)

0(1; R0)) + λ(cid:3)

e2
0(1; R0)
e1(2; R0 − e2

0(1; R0))

e2
0(1; R0)
0(1; R0) − e3

0(1; R0 − e2

0(1; R0)))

e1(1; R0 − e2

(cid:21)(cid:19)

− t

.

(cid:21)(cid:19)

− t

To simplify this constraint, note ﬁrst that one may show

e1(2; R0 − e3

0(2; R0)) =

e1(3; R0) =

1
3(1 − λ)
1
3(1 − λ)

[R0 − λ] ,

R0.

Hence, the left-hand side of the incentive constraint is simply

µF u

(cid:18) 1
3

R0 +

(cid:19)

2
3

λ

+ µCu

(cid:19)

R0 + λ

.

(cid:18) 1
3

Second, note that

e2
0(1; R0) =

1
3

R0 −

2
3

1
α

log B

where B is a constant that satisifes

(cid:18)

B = µF exp

−

1
2

(cid:19)

αλ

+ µC exp(−αλ).

Then, one may show

1
3

R0 +

1
(1 − λ)
1
(1 − λ)

1
1
α
3
(cid:20) 1
3
(cid:20) 1
3

0(1; R0 − e2
e3

0(1; R0)) =

e1(1; R0 − e2

0(1; R0) − e3

0(1; R0 − e2

0(1; R0))) =

e1(2; R0 − e2

0(1; R0)) =

27

log B +

λ,

1
2
1
α
1
α

R0 +

R0 +

1
3
1
3

(cid:21)

λ

,

1
2

log B −

(cid:21)

.

log B

Using these results, we may re-write the right-hand side of the incentive constraint as

µF u

(cid:18) 1
R0 +
3
(cid:32)(cid:20) 1
3
(cid:32)(cid:20) 1
3

+ µCu

≥ µF u

R0 +

(cid:19)

λ

+ µCu

(cid:18) 1
3

(cid:19)

R0 + λ

2
3

1
3

1
α

log B +

(cid:21) (cid:34)

1
2

λ

R0 +

1
3

1
α

log B + λ

1

3

1

(1 − λ) (cid:2) 1
3 R0 + 1
(1 − λ) (cid:2) 1

3 R0 − 2

α log B(cid:3)
α log B − 1
2 λ
α log B(cid:3)
3 R0 − 2

1

3

1

1

3 R0 + 1

3

3
1
α log B

(cid:35)(cid:33)

− t

(cid:35)(cid:33)

− t

(cid:21) (cid:34)

Using the concavity of u(·), it suﬃces (to prove the incentive constraint holds) to show

1
3

R0 +

2
3

λ ≥ µF

(cid:20) 1
3

R0 +

1
3

1
α

log B +

(cid:21) (cid:34)

1
2

λ

+ µC

(cid:20) 1
3

R0 +

1
3

1
α

log B + λ

(cid:21) (cid:34)

3

1

1

(1 − λ) (cid:2) 1
3 R0 + 1
(1 − λ) (cid:2) 1

3 R0 − 2

α log B(cid:3)
α log B − 1
2 λ
α log B(cid:3)
3 R0 − 2

1

1

3

1

3 R0 + 1

3

3
1
α log B

− t

(cid:35)

(cid:35)

− t

Using tedious, but straightforward algebra, one may show that as λ → 1, the right hand side tends
to

−t

R0 +

log B(1)

− t

(cid:20) 1
3

1
3

1
α

(cid:21)

1 + µC
2

.

Hence, the necessary inequality condition (as λ → 1) requires

1
3

R0 +

2
3

≥ −t

(cid:20) 1
3

R0 +

1
3

1
α

(cid:21)

log B(1)

− t

1 + µC
2

or

1 + µC
2
Since B → µF exp(−α/2)+µC exp(−α) as λ → 1, limλ→1 B ≥ exp(−α). It follows that −t log B/3α ≤
t/3. Since t/2 ≥ t/3, for all R0,

(1 + t)R0 + t

log B.

≥ −

1
α

1
3

t
3

1
3

(1 + t)R0 + t

1
2

+

tµC
2

≥ t

1
3

≥ −

t
3

1
α

log B

so that the required incentive constraint holds for all R0, α.

Suppose next that Trader 1 is foreign so that θ = 0. The incentive constraint is
0(1; R1)) + λ(cid:3) + µCu [(1 − λ)e1(2; R1) + λ]
(cid:20) e2

µF u (cid:2)(1 − λ)e1(1; R1 − e3

(cid:21)(cid:19)

(cid:18)

≥ µF u

(cid:2)(1 − λ)ef + λ(cid:3)

(cid:18)

+ µCu

(cid:2)(1 − λ)e1(1; R1 − e2

− t

0(0; R1)
ef
0(0; R1)) + λ(cid:3)

(cid:20)

e2
0(0; R1)
e1(1; R1 − e2

0(0; R1))

(cid:21)(cid:19)

− t

As above, we use the optimal exchange rate policies to express the incentive constraint in terms of

28

reserves and fundamentals. Note that

e1(1; R1 − e3

0(1; R1))

[R1 − λ] ,

1
2(1 − λ)
1
2(1 − λ)

e1(2; R1) =

R1,

so that the left-hand side of the incentive constraint is

µF u

(cid:18) 1
2

R1 +

(cid:19)

1
2

λ

+ µCu

(cid:19)

R1 + λ

.

(cid:18) 1
2

Similarly, letting the constant C satisfy C = µF + µC exp(−αλ),

e2(0; R1)

R1
2

e1(1; R1 − e2

0(0; R1)) =

−

1
2α
1
1 − λ

log C,
(cid:20) R1
2

+

(cid:21)

log C

.

1
2α

Then the right-hand side of the incentive constraint is

(cid:32)

(cid:2)(1 − λ)ef + λ(cid:3)

µF u

(cid:34) R1

2 − 1
2α log C
ef

(cid:35)(cid:33)

− t

+ µCu

(cid:32)(cid:20) R1
2

+

1
2α

(cid:21) (cid:34)

log C + λ

We proceed as in the previous case and prove

(1 − λ) (cid:2) R1
R1
2 + 1

2 − 1
2α log C

2α log C(cid:3)

1
2

R1 +

λ

1
2
(cid:32)

≥ µF

(cid:2)(1 − λ)ef + λ(cid:3)

(cid:34) R1

2 − 1
2α log C
ef

(cid:35)(cid:33)

− t

+ µC

(cid:32)(cid:20) R1
2

+

1
2α

(cid:21) (cid:34)

log C + λ

(1 − λ) (cid:2) R1
R1
2 + 1

2 − 1
2α log C

2α log C(cid:3)

(cid:35)(cid:33)

− t

(cid:35)(cid:33)

− t

As λ → 1, straightforward algebra reveals that this inequality holds if

1
2

R1 +

1
2

≥ µF

(cid:34) R1

2 − 1
2α log C
ef

(cid:35)

(cid:20)

− t

+ µC

−t

(cid:18) 1
2

R1 +

1
2

1
α

(cid:19)

(cid:21)

log C

− t

.

Noting that − log C ≤ α (as λ → 1), we have

RHS ≤ µF

(cid:34) R1

(cid:35)
2 + 1
ef − t

2

(cid:20)

+ µC

−t

(cid:18) 1
2

R1 −

(cid:19)

(cid:21)

− t

.

1
2

The incentive constraint holds, therefore, as long as

R1
2

(cid:104)
1 −

(cid:105)
µF
ef + µCt

+

1
2

−

1
2

µF
ef + t

(cid:20)

1 −

1
2

(cid:21)

µC

≥ 0.

Note that if

1 −

µF
ef + µCt ≥ 0,

29

then

1
2

−

1
2

µF
ef + t

(cid:20)

1 −

1
2

(cid:21)

µC

≥ 0.

Hence, suppose the ﬁrst inequality holds (which is a restriction on µC given t, ef that holds whenever
µC → 1). Then, at R1 = 0, the inequality holds and raising R1 relaxes the incentive constraint.
Hence, for all R1 ∈ [0, R0] the inequality must also hold.

Incentives for the 1st Trader. Given truthful reporting is dominant for traders 2 and 3, the ex-
pected utility associated with truthful reporting for Trader 1 is given by

Cu ((1 − λ)e1(3; R0) + λ) + µF µCu (cid:0)(1 − λ)e1

(cid:0)2; R0 − e2

U tt = µ2
+ µCµF u (cid:0)(1 − λ)e1

0(1; R0)(cid:1) + λ(cid:1)
(cid:0)1; R0 − e2

(cid:0)2; R0 − e3

0(2; R0)(cid:1) + λ(cid:1) + µ2

F u (cid:0)(1 − λ)e1

0(1; R0) − e3

0(1; R0 − e2

0(1; R0))(cid:1) + λ(cid:1) .

The expected utility associated with speculation is given by

(cid:18)

U spec = µ2

Cu

(cid:2)(1 − λ)e1(2; R0 − e1

0(R0)) + λ(cid:3)

(cid:20)

+ µF µCu

+ µCµF u

(cid:18)
(cid:2)(1 − λ)e1(1; R0 − e1
(cid:18)
(cid:2)(1 − λ)e1(1; R0 − e1

(cid:18)

(cid:2)(1 − λ)ef + λ(cid:3)

+ µ2

F u

(cid:20) e1

0(R0)
ef − t

0(R0) − e2

0(0; R0 − e1

e1
0(R0)
e1(2; R0 − e1

0(R0))
0(R0))) + λ(cid:3)

(cid:21)(cid:19)

− t

(cid:20)

(cid:20)

0(1; R0 − e1

0(R0))) + λ(cid:3)

0(R0) − e3
(cid:21)(cid:19)

e1(1; R0 − e1

0(0; R0 − e1

0(R0)))

e1(1; R0 − e1

0(1; R0 − e1

0(R0)))

e1
0(R0)
0(R0) − e2
e1
0(R0)
0(R0) − e1

(cid:21)(cid:19)

(cid:21)(cid:19)

− t

− t

Tedious algebra reveals that

U tt = µ2

Cu

(cid:18) R0
3

(cid:19)

+ λ

+ µF µCu

(cid:18) R0
3

+ µCµF u

(cid:18) R0
3

+

(cid:19)

2
3

λ

+ µ2

F u

1
α

+

+

1
3
(cid:18) R
3

(cid:19)

log B + λ

1
3

1
α

log B +

(cid:19)

1
2

λ

and

U spec = µ2

Cu

+ µF µCu

+ µCµF u

(cid:18)(cid:20) R0
3
(cid:18)(cid:20) R0
3
(cid:18)(cid:20) R0
3

+ λ +

+ λ +

+

1
2

λ +

1
3
1
3

(cid:21) (cid:20)

log D

log D +

1
α
1
α
1
1
α
3
(cid:20) e1
0(R0)
ef − t

log D

e1
0(R0)
e1(2; R0 − e1
1
2
(cid:21) (cid:20)

log C

1
α

(cid:21) (cid:20)

e1(1; R0 − e1
(cid:21)(cid:19)

(cid:21)(cid:19)

− t

0(R0))

e1(1; R0 − e1
e1
0(R0)
0(R0) − e1

(cid:18)

(cid:2)(1 − λ)ef + λ(cid:3)

+ µ2

F u

e1
0(R0)
0(R0) − e2

0(0; R0 − e1

0(R0)))
(cid:21)(cid:19)

0(1; R0 − e1

0(R0)))

− t

(cid:21)(cid:19)

− t

30

where

(cid:18)

B = µF exp

−

(cid:19)

αλ
2

+ µC exp(−αλ)

C = µF + µC exp(−αλ)

We know that U tt ≥ u (cid:0) R
convex combination of speculative consumption. Hence, it suﬃces to prove that

α log B + 1

3 + 1

3

1

2 + µCB
2 λ(cid:1) and that U spec is bounded above by the utility of the

D = µF C

1

R
3

+

≥ µ2
C

1
2

λ

1
log B +
3
(cid:20) R0
3

+ λ +

1
3

1
α

+ µF µC

+ µCµF

(cid:20) R0
3
(cid:20) R0
3

+ λ +

+

1
2

λ +

+ µ2
F

(cid:2)(1 − λ)ef + λ(cid:3)

(cid:21)

− t

(cid:21) (cid:20)

log D

1
3

log C

0(R0))
(cid:21) (cid:20)

e1
0(R0)
e1(2; R0 − e1
1
1
α
2
(cid:21) (cid:20)

log D +

1
α
1
1
e1(1; R0 − e1
α
3
(cid:21)
(cid:20) e1
0(R0)
ef − t

log D

.

e1(1; R0 − e1
e1
0(R0)
0(R0) − e1

e1
0(R0)
0(R0) − e2

0(0; R0 − e1
0(R0)))
(cid:21)

0(1; R0 − e1

0(R0)))

− t

(cid:21)

− t

As λ → 1, this inequality tends towards

R0
3

+

1
3

≥ −tµ2
C

1
2

1
log B +
α
(cid:20) R0
3
(cid:20) R0
3

+ 1 +

− tµCµF

(cid:21)

log D

− tµF µC

1
3

1
α

+

1
2

+

1
3

1
α

(cid:21)

+ µ2
F

log D

1
3

1
α

+ 1 +

(cid:20) R0
3
(cid:34) R0
3 − 2
1
α log D
3
ef

log D +

(cid:35)

− t

.

(cid:21)

log C

1
2

1
α

or

R0
3

(cid:20)

1 −

µ2
ef + t (cid:0)1 − µ2
F
(cid:20)
µ2
C

1 +

(cid:18)

F

1
3

1
α

+ t

(cid:21)

(cid:1)

+

1
3

1
α

(cid:19)

log D

+ µCµF

log B +

1
2

+

µ2
F
ef

2
3

1
α

log D

(cid:18) 3
2

+

2
3

1
α

log D +

(cid:19)

(cid:21)

≥ 0

+ µ2
F

log C

1
2

1
α

Using the fact that C 1

2 ≥ D ≥ B ≥ exp(−α), the above inequality holds as long as

R0
3

(cid:20)

1 −

µ2
ef + t (cid:0)1 − µ2
F

F

(cid:21)

(cid:1)

+

1
6

−

2
3

µ2
F
ef + t

(cid:20) 2
3

µ2

C +

1
3

µCµF + µ2
F

(cid:21)

≥ 0.

Notice, this inequality is necessarily satisﬁed as µC → 1.

31

Figure 1: Daily Volatility

The 30-day (rolling) standard deviation of daily USD price changes of

Bitcoin, Euro, S&P500 stock, Gold.

32

02468Standard Deviation of Daily Returns (Percent)Jul-15Jul-16Jul-17Jul-18Jul-19BTC-USEUR-USGold-USS&P500Source: Coinbase, FRBofG;  Date:2015.2.14 - 2019.12.25Figure 2: Policy Simulation

Simulated path of exchange rate through J = 100 traders in period 0

and period 1 (J=101). The solid black line is the mean path. The 25 –

75 and 10 – 90 percentile range is shown in red. The upper line is the

(unlikely) realization of all C-type traders (who do not demand foreign

reserves in date 0). The lower line is the path of all F -type traders (who

demand foreign reserves).

33

0.000.250.500.751.000255075100Trader Positionexchange rateFigure 3: Policy Simulation

(a)

(b)

(c)

(d)

Simulated path of exchange rate through J = 100 traders in period 0 and period 1 (J=101). The solid black

line is the mean path. The 25 – 75 and 10 – 90 percentile range is shown in red. The simulations in all four

panels have identical draws of the C and F types except as follows: In Panel (a), traders j = 10, 11, 12 are

modiﬁed to be either type C (top line) or type F (bottom line). The other panels modify traders similarly

but at diﬀerent points, (b) j = 30, 21, 32, (c) j = 60, 61, 62, and (d) j = 80, 81, 82.

34

0.10.20.30255075100Trader Positionexchange rate0.10.20.30255075100Trader Positionexchange rate0.10.20.30255075100Trader Positionexchange rate0.10.20.30255075100Trader Positionexchange rate