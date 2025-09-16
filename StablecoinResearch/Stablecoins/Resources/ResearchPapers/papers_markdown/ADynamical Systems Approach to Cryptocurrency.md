8
1
0
2

y
a
M
8

]
F
M
.
n
i
f
-
q
[

1
v
3
4
1
3
0
.
5
0
8
1
:
v
i
X
r
a

A Dynamical Systems Approach to Cryptocurrency
Stability

Carey Caginalp,1,2∗

1Department of Mathematics, University of Pittsburgh, USA
301 Thackeray Hall, Pittsburgh PA 15260, USA
2Economic Science Institute, Chapman University
One University Drive, Orange CA 92866, USA

∗To whom correspondence should be addressed; E-mail: carey caginalp@alumni.brown.edu.

Recently, the notion of cryptocurrencies has come to the fore of public interest.
These assets that exist only in electronic form, with no underlying value, offer
the owners some protection from tracking or seizure by government or credi-
tors. We model these assets from the perspective of asset ﬂow equations devel-
oped by Caginalp and Balenovich, and investigate their stability under various
parameters, as classical ﬁnance methodology is inapplicable. By utilizing the
concept of liquidity price and analyzing stability of the resulting system of or-
dinary differential equations, we obtain conditions under which the system is
linearly stable. We ﬁnd that trend-based motivations and additional liquid-
ity arising from an uptrend are destabilizing forces, while anchoring through
value assumed to be fairly recent price history tends to be stabilizing.

Introduction

Blockchain technology enables large numbers of participants to make electronic transactions
directly without intermediaries, and has led, in recent years to a new form of payment, and
essentially to a new set of currencies called cryptocurrencies. During 2017 the spectacular nine-
fold rise in the price of Bitcoin focused the spotlight of public attention on cryptocurrencies
that evolved into a new asset class. Following the pattern of other nascent assets, speculators
dominated trading and pushed prices toward a bubble.

1

As with some other asset bubbles of the past, notably the dot-com frenzy of the late 1990s,

the emergence of a new technology clouded judgements about the basic value of the asset.

In almost all cases, unlike traditional equities, cryptocurrencies have no tangible value, and
even their creation is often shrouded in mystery (3). For Bitcoin, the creation of additional
units is relegated to a process termed mining, named after the old technology of mining gold.
In this electronic version, computing power is used to solve complex mathematical problems,
and once solutions are found, the miner is rewarded with some units of the cryptocurrency. It is
peculiar that this brand new technology is coupled with the organizational hierarchy of centuries
ago that featured the hegemony of gold miners and traders who held power over the economic
lives of people without any accountability. Thus, the advances in technology are coupled with
a regressive organizational structure. Major currencies such as the US dollar are controlled by
ofﬁcials appointed by elected representatives; assets such as common stocks are governed by a
board of directors that are elected by the shareholders whose rights are assured by law, albeit
through a circuitous process. Changes made by cryptocurrencies are often made at an ad hoc
meeting of the developers or miners, reminiscent of tribal chiefs meetings of more primitive
eras.

In certain types of securities, i.e. exchange-traded funds (ETFs), a certain group of traders
known as authorized participants have the capacity to demand the underlying shares, preventing
the price of the ETF from straying too far from its fundamental value. Securities held in a
brokerage account are insured up to a value of several million dollars by the federal government
against circumstances such as hacking or company insolvency.

Conversely, for cryptocurrencies, many of these rules have been lacking and a few have been
recently instituted. First, these cryptocurrencies have no underlying assets. Further, there exists
no mechanism by which one can redeem any value from a bank or other institution. Second,
even the country of residence (let alone a business address) of the creators is merely specu-
lative, making it unclear to which court one could possibly appeal in the case of a grievance.
The original ”developer” for Bitcoin, for example, is known only by a pseudonym. Third, the
individual investor has no inﬂuence over something as simple as the number of Bitcoins in
existence. Instead, these decisions are generally relegated to the heads of electronic Bitcoin
mining operations, whose interests may be disjoint from investors’. Bitcoin is currently set to
be capped at 21 million units, but there is no legal obstacle to prevent an increase at the whim
of the miners. Fourth, many individual investors and some academicians tacitly assume that
the laws and protections afforded by the purchase of securities through stock exchanges such as
NYSE must also apply to cryptocurrencies. Recently, the Securities and Exchange Commission
(SEC) has shuttered some initial coin offerings (ICOs) (4, 34) and announced future regulations
to attempt to inject more clarity into the marketplace. Finally, Bitcoin is vulnerable to hacking
or simply forgetfulness. Many holders of Bitcoin have their information stored in exchanges,
i.e. platforms that handle transaction and storage of the cryptocurrency. These are hijacked with
a disturbing regularity, and litigation can be pending years later, as in the infamous Mt. Gox
hacking of 2014 (27).

Cryptocurrencies offer both opportunities and risks to society. On the one hand, cryptocur-

2

rencies and technology underpinning them – if designed appropriately – could be used to make
transactions faster, safer and cheaper, alongside other societal beneﬁts (15,22). A less apparent
feature is that they can make it more difﬁcult (though not theoretically impossible; see (5, 18))
for totalitarian governments to expropriate savings, either directly or indirectly through cur-
rency inﬂation, thereby depriving savers of a large fraction of their assets. In this way, a proper
cryptocurrency could lead to greater economic freedom, and render more difﬁcult the ﬁnancing
of a dictatorship. Indeed, this can be modelled by a choice of two alternatives: either their home
currency or cryptocurrency that cannot easily be seized (20, 39).

The risks presented by existing cryptocurrencies are multi-faceted. The difﬁculty in tracing
transactions facilitate illicit activity and its ﬁnancing. A less obvious – and possibly the most
signiﬁcant – risk arises from the instability of prices of major cryptocurrencies. As the market
capitalization (number of units times the price of each unit) of the cryptocurrencies rises, there
is growing risk that a sharp drop in the price of a cryptocurrency could have a cascading effect
on other sectors of world economy, particularly if borrowing is involved. During the period
October 2017 to April 2018, the price of a Bitcoin unit rose from $6,000 to $20,000 and back
to $6,000. The market capitalization of all cryptocurrencies during that time period increased
from $170 billion to $330 billion, peaking together with Bitcoin in December 2017. While
attention is often focused on the rise and fall of the trading prices of these assets, the magnitude
of the problem of stability has increased signiﬁcantly during this six month period. As people
become more accustomed to using these instruments, the market capitalization may increase to
several trillion – i.e., a few percent of the $ 75 trillion Gross World Product – and many of the
challenges will be critical.

Generally, the features of a ﬁnancial instrument that might make it attractive to speculators
are undesirable to those who seek to use it as a currency in daily transactions. Speculators
see a greater opportunity in a volatile market, as they can use technical analysis and expertise to
proﬁt at the expense of the layperson. Conversely, large ﬂuctuations on a day-to-day basis create
obstacles for common purchases or the pricing of service contracts (38). Without stability in the
marketplace, the cryptocurrencies may simply become ”a mechanism for a transfer of wealth
from the late-comers to the early entrants and nimble traders” (7). Thus, a set of questions
of critical importance deals with the potential stability (or lack thereof) of Bitcoin or other
cryptocurrencies, which is the main topic of our paper.

The turbulence arising from the collapse of the housing bubble was a major challenge for
markets, but from a scientiﬁc perspective, it could be addressed largely with classical methods
(19, 32, 35). However, classical methods are not readily adaptable to studying cryptocurrencies,
as discussed below. We use a modern approach whereby an equilibrium price can be determined
and the stability properties established within a dynamical system setting (6,9,10,17,23,24, 28,
30, 35–37, 42).

3

1 Modelling prices and stability

Most of classical ﬁnance such as the Black-Scholes option pricing model has its origin in the
basic equation

1
P

dP = µdt + σdW

(1)

for the change in the relative price P −1dP in terms of the expected return, µ, the standard
deviation of the return, σ, and independent increments of Brownian motion, dW. It is widely
acknowledged that this equation does not arise from compelling microeconomic considerations,
nor empirical data. But rather, it is mathematically convenient and elegant for expressing and
proving theorems (see (11) for discussion). Much of risk assessment is based upon this model
with an increasing array of adjustments.

The limitations of this basic model are apparent, for example, if one examines the standard
deviation of daily relative changes in the S&P 500 index, which is typically around 0.75%.
This leads to the conclusion that a 4.5% drop is a sixth standard deviation event, i.e., it occurs
once every billion trading days, while empirical data shows it is on the order of a few times per
thousand (2).

Thus identifying risk on a large time scale based on the variance of a small time scale can

vastly underestimates risk.

Furthermore, the modeling of asset prices is generally based on the underlying assumption
of inﬁnite arbitrage. While there may be some investors who are prone to cognitive errors or bias
in assessing value, the impact of their trades will be marginalized by more savvy investors who
manage a large pool of money. Of course the inherent assumption is that there is some value to
an asset, based for example on the projection of the dividend stream, replacement value, etc.,
and that the shareholder has a vote that allows him ultimately to extract this value. For assets
such as US Treasury bills, the model works quite well, as the owner is assured of receiving a
particular dollar amount from the US at a speciﬁed time.

Herein lies the central problem for the application of classical theory to cryptocurrencies:
there is no underlying asset value, as noted above. Cryptocurrencies constitute the opposite end
of the market spectrum to US Treasury Bills, in which an arbitrageur can conﬁdently buy or sell
short based on a clear contract that will deliver a ﬁxed amount of cash at a predetermined time.
If fact, classical game theory would conclude that since everyone knows the structure of the
cryptocurrency, and understands that everyone else is also aware, then the price should never
deviate much from zero. Furthermore, classical ﬁnance expressed through (1) would suggest
that there is some measure of risk based on the historical average of σ, which will be less helpful
that it is for stock indexes as discussed above.

Our analysis begins with the fact that despite the absence of underlying assets or backing,
various groups have incentive to use it over traditional currencies. In particular there are large
groups who need to make transactions outside of the usual banking system. Among these
are (i) people with poor credit who cannot obtain a credit or even a debit card, (ii) citizens of
totalitarian countries who fear expropriation of their savings, (iii) citizens of countries with high

4

inﬂation and a much lower interest rate, (iv) people engaged in illicit activity, (v) people who
espouse utilizing a new idea or technology.

Collectively, these groups constitute a core ownership of cryptocurrencies, investing a sum
that gradually grows with familiarity (14, 16, 25). Meanwhile, the rising prices catch the at-
tention of speculators who provide additional cash into the system, but also bring motivations
inherent in speculation, namely momentum trading, or the tendency to buy as prices rise, and
analogously sell as prices fall (41).

We assume a single cryptocurrency and that the price is established by supply and demand
without inﬁnite arbitrage, and apply a modern theory of asset ﬂow (10). This alternative ap-
proach relies on the notion of liquidity price. The experimental asset markets presented a puzzle
to the economics community by demonstrating the endogenous price bubbles in which prices
soared well above any possible expectation of outcome (28). Caginalp and Balenovich (10)
observed that in addition to the trading price and fundamental value (deﬁned clearly by the ex-
perimental setup), there was an additional important quantity with the same units: the total cash
in the system divided by the number of shares. Denoting this by liquidity value or price, L, they
adapted earlier versions (8) of the asset ﬂow model.

This approach leads to a system of ordinary differential equations, as summarized below,
whereupon equilibrium points can be evaluated and their stability established as a function of
the basic parameters.

2 Modeling Cryptocurrency with Asset Flow Equations

For brevity, we ﬁrst present the full model which will be a nonlinear evolutionary system that is
based on (10) but with some key differences for cryptocurrencies. We can then consider simpler
models in which some features are marginalized by setting parameters to zero and obtaining
2 × 2 or 3 × 3 systems, enabling us to understand the key factors in stability.

We denote the trading price by P (t), the number of units by N (t), the amount of cash
available by M (t), and the liquidity price by L (t) = M (t) /N (t). With B as the fraction of
wealth in the cryptocurrency, i.e., B = N P/ (N P + M ), the supply and demand are given by
S = (1 − k) B, D = k (1 − B) respectively, where k is the transition rate from cash to the
asset. Using a standard price equation (42) we write

τ0

1
P

dP
dt

=

D
S

− 1.

It follows that B (1 − B)−1 = N P/M = P/L , so that the price equation is

τ0

1
P

dP
dt

=

k
1 − k

L
P

− 1 .

(2)

(3)

The variable k is assumed to be a linearization of a tanh type function and involves the motiva-
tions of the traders which are expressed through sentiment, ζ = ζ1 + ζ2 where ζ1 is the trend

5

component and ζ2 is the value component. This construct has been studied, for example, in
closed-end funds (1, 12, 13, 26) which frequently trade either at a discount or premium to their
net asset value. Writing the term k/ (1 − k) in terms of the ζ1 and ζ2 and linearizing we have
then

k
1 − k

˜=1 + 2ζ1 + 2ζ2

and the price equation is then

τ0

1
P

dP
dt

= (1 + 2ζ1 + 2ζ2)

L
P

− 1 .

(4)

(5)

One deﬁnes ζ1 through two parameters, c1, that expressed the time scale of the trend follow-

ing and q1 the amplitude of this factor, as

ζ1 (t) =

q1
c1

(cid:90) t

−∞

e−(t−τ )/c1

1
P (τ )

τ0

dP (τ )
dτ

dτ

(6)

Note that L and ζ1 are linear functions of one another, but we retain L as a variable so the system
is more easily generalized to incorporate a time-dependent L0. The valuation is more subtle for
a cryptocurrency. The only concept of value relates to fairly recent trading prices. The ﬁrst
purchase with Bitcoin was for two slices of pizza for 10,000 Bitcoins (29). The sense of value
at that time was probably much less than 2018 when people became accustomed to prices in the
thousands of dollars. We thus stipulate the deﬁnitions

Pa (t) =

ζ2 (t) =

q2
c2

1
c3
(cid:90) t

−∞

(cid:90) t

−∞

e−(t−τ )/c3P (τ ) dτ,

e−(t−τ )/c2

Pa (τ ) − P (τ )
P (τ )

dτ,

(7)

(8)

i.e., ζ2 represents the motivation to buy based on the discount from the perceived value of the
cryptocurrency. Finally, the liquidity will not be constant but will be the sum of the core group’s
capital L0 plus the additional amounts arriving from speculators that is correlated with the recent
trend:

L (t) = L0 +

L0
c

q

(cid:90) t

−∞

e−(t−τ )/c τ0
P (τ )

dP (τ )
dτ

dτ

(9)

We assume that L0 is constant, but one can easily adapt the model to include temporal changes
in L0 due to, for example, greater public acceptance of cryptocurrencies. By differentiating
(6-9) and combining the resulting equations with (5) we obtain the 5x5 system of ordinary

6

differential equations:

c3P (cid:48)

a = P − Pa,

c2ζ (cid:48)

2 = q2

Pa (t) − P (t)
Pa (t)

− ζ2,

τ0P (cid:48) = (1 + 2ζ1 + 2ζ2) L − P,
cL(cid:48) = 1 − L + q {(1 + 2ζ1 + 2ζ2) L − P } ,

c1ζ (cid:48)

1 = q1

(cid:18)

(1 + 2ζ1 + 2ζ2)

(cid:19)

− 1

− ζ1.

L
P

(10)

We ﬁnd a unique equilibrium at (P, Pa, L, ζ1, ζ2) = (1, 1, 1, 0, 0).
In other words, the only
steady-state of the system occurs when the price, the anchoring notion of fundamental value,
and liquidity price all coincide with the base liquidity value L0 (33). The time scale for price
adjustment will be short as markets adjust rapidly to supply/demand changes. Much longer
will be the time scale for observing the trend and reacting to under or over-valuation, and the
assessment of valuation anchored through weighted price averages. Moreover, one might expect
that the valuation is on an even longer time scale. Thus one expects three time scales such that
τ0 (cid:28) c, c1, c2 (cid:28) c3, which we can scale as c = c1 = c2 = 1, and we allow arbitrary τ0, c3 in the
analysis.









τ0P
c3Pa
L
ζ1
ζ2











=







−1
0
1 −1
0
−q
0
−q1
q2
−q2

1
0
q − 1
q1
0

2
0
2q

2
0
2q
2q1 − 1 2q1
−1

0

















P
Pa
L
ζ1
ζ2



.







(11)

Thus, the system is determined entirely by three parameters: q, the attention to trend; q1, a
measure of the inﬂuence of delay times; and q2, the inﬂuence of fundamental value, along with
the time parameters τ0 and c3. The question of stability can be investigated by calculating the
eigenvalues in the relevant parameter space, i.e. (q, q1, q2) ∈ R3
+ (the ﬁrst octant), along with
τ0 and c3. In particular, the main question is whether the maximal real part of the eigenvalues
is positive, leading to instability, or if they are all negative, yielding stability. One sees that
there is a double eigenvalue at λ = −1, and the other three eigenvalues remain negative if the
Routh-Hurwitz conditions (40) below are satisﬁed

1
τ0

+

1
c3

+ Q > 0,

(cid:18) Q
c3

+

1
τ0

+ 2

q2
τ0

+

1
τ0c3

(cid:19) (cid:18) 1
τ0

+

1
c3

(cid:19)

+ Q

>

1
c3τ0

.

(12)

where we have set Q = 1 − q − 2q1. A sufﬁcient set of conditions for (12) to hold is the

7

following:

1
c3
1
c3

+

+

1
τ0
1
τ0

> q + 2q1 =: K,

>

K
c3

− 2

q2
τ0

.

(13)

However, one can observe numerically that (13) are not necessary conditions to satisfy (12).
Also, if we set q2 = 0, we obtain the simpler condition

1
c3

+

1
τ0

> K

(14)

for stability, which we will see describes a simpler model that excludes valuation and the com-
ponent of investor sentiment associated with it. We sketch various cross-sections holding one
of these parameters constant and numerically computing eigenvalues across values of the other
two. Note in Figure 1 below that increasing q2 induces a stabilizing effect, while large K serves
to make the system less stable. We choose various values of τ0 and c3 in Figure 2.

This yields a number of results. First, as market participants focus greater attention to the
deviation of the asset from the acquired fundamental value driven from the liquidity price, there
is less room for prices to stray from equilibrium. In addition, for a ﬁxed q2, the asset would
experience stability given that K is large enough. Finally, for K large enough, one sees that we
have instability for a large range of q, i.e., if investors place too much emphasis on the relative
trend, the asset price becomes unstable. The shaded regions indicate the range of parameters
for which the system (11) is stable.

When we set q2 = 0, the model simpliﬁes somewhat, leaving a linear interface between
the regions of stability and instability. We then have the following theorem. We deﬁne Q :=
1 − q − 2q1.

Theorem 1 Consider the system (11). With q2 = 0, one has stability of the system (11) if and
only if

.

Q +

1
τ0

> 0

Proof. Setting q2 = 0, the necessary conditions become
(cid:19) (cid:18) 1
τ0

1
c3τ0

Q
c3

1
τ0

Q +

+

+

+

(cid:19)

(cid:18)

1
c2
3

> 0 and Q +

(15)

(16)

1
τ0

+

1
c3

> 0

We prove this is equivalent to Q + 1
τ0

> 0.

(i) Assume Q + 1
τ0

has

> 0. Then clearly the second inequality in (16) is satisﬁed. Also, one

1
τ0

+

Q
c3

+

1
c3τ0

+

1
c2
3

(cid:18)

=

Q +

(cid:19)

(cid:19) (cid:18) 1
c3

1
τ0

+

1
τ0

+

1
c2
3

> 0,

(17)

8

satisfying the ﬁrst inequality.

(ii) Suppose (16) holds. Then clearly

(cid:18)

0 <

Q +

1
τ0

+

(cid:19) 1
c3

1
c3

+

1
τ0

=

1
τ0

+

Q
c3

+

1
c3τ0

+

1
c2
3

,

(18)

implying (15).

3 The effect of liquidity with or without sentiment

In order to isolate the effect of liquidity, we eliminate the role of investor sentiment and value
by setting the associated parameters to zero. To this end, we are left with the system

τ0P (cid:48) = L − P,
cL(cid:48) = 1 + (q − 1) L − qP.

(19)

One readily calculates that there will be positive eigenvalues of the linearized system if and only
if q > 1 + c
In other words, in a system where only price and liquidity are relevant, a large
τ0
amplitude q of liquidity is destabilizing while a large time scale for the liquidity is stabilizing.
The stability is illustrated in the Figure 2.

Another nontrivial subcase is obtained from examining the full model (10) in the case where
we set the value component of the sentiment, ζ2, and the fundamental value equal to zero. We
then have the system of equations

τ0

c

c1

dP
dt
dL
dt
dζ1
dt

= (1 + 2ζ1) L − P

= 1 − L + q (1 + 2ζ1) L − qP

= q1 (1 + 2ζ)

L
P

− q1 − ζ1

(20)

One then observes that the only equilibrium point is L = P = L0 and ζ = 0. Recalling that

Q := 1 − q − 2q1, one has the following.

Theorem 2 The system (20) incorporating valuation and sentiment (with c := c1) is stable if
and only if

c
τ0
i.e. if the perturbations from trend and valuation sentiment are sufﬁciently small as a relative
comparison to the timescale of reaction with respect to price.

> 0,

Q +

(21)

9

Proof. By scaling, assume without loss of generality that c1 = c = 1; then we can linearize the
system as follows:


(cid:48)





=







P
L
ζ

−1/τ0
−q
−q1

1/τ0
q − 1
q1

2/τ0
2q
2q1 − 1









P
L
ζ





 =: A





 .

P
L
ζ

(22)

Leaving aside the eigenvalue of −1 that is present for all values of the parameters, the matrix

A has eigenvalues with positive real part if and only if

q + 2q1 > 1 +

1
τ0

.

(23)

After rescaling, this is the statement of the theorem.

Furthermore, we have either zero or two roots with positive real parts, so that we will have
a stable spiral for Q + c
< 0 for the equilibrium point
τ0
at (1, 1, 0). This matches our intuition from an economics perspective since one has instability
when q + 2q1 > 1 + c
, i.e., there will be stability if q + 2q1 < 1 regardless of c and τ0. For
τ0
q + 2q1 > 1, one sees that instability arises when c
is sufﬁciently small, i.e. traders are focused
τ0
on short term trends.

> 0 and an unstable spiral for Q − c
τ0

The analysis above clearly shows that the potential stability of a crypto-asset may be con-
tingent on several parameters that one may be able to inﬂuence. With this information, further
research may be useful to examine the correlations and ﬁt of these parameters with the effects
of news and government policy. A problem of future interest would be whether, and if so how,
governmental policy might be developed to diminish the volatility in cryptocurrencies. Another
alternative would be a decentralized cryptocurrency with a concrete value. A good index to
base this on would be either current or future gross world product (which could be estimated
via futures markets). For a nominal fee, holders of this currency would be able to demand a
basket of underlying currencies (such as dollar, euro, yen, etc.), which would keep the value of
such a currency relatively close to its true fundamental value.

References and Notes

References

1. S. Anderson, G. Born, Closed-End Investment Companies: Issues and An-

swers. Boston: Kluwer (2002).

2. G. Banjeri, A. Osipovich, Market rout shatters lull in volatility. The Wall
Street Journal. Available at https://www.wsj.com/articles/market-rout-shatters-
lull-in-volatility-1517875833 (2018).

10

3. Z. Bernard, Everything you need to know about Bitcoin,

its mysteri-
ous origins, and the many alleged identities of its creator. Available at
http://www.businessinsider.com/bitcoin-history-cryptocurrency-satoshi-
nakamoto-2017-12. Accessed April 9, 2018.

4. J.

SEC

Biggs,

at
https://techcrunch.com/2017/12/12/sec-shuts-down-munchee-ico/. Accessed
April 2, 2018.

down Munchee

ICO. Available

shuts

5. J. Bohannon, The bitcoin busts. Science 351, 1144-1146 (2016).

6. G. Caginalp, D. Porter, V. Smith, Financial bubbles: Excess cash, momentum,

and incomplete information. J Psychol. Financ. Mark. 2, 80–99 (2001).

7. C. Caginalp, G. Caginalp, Valuation, liquidity price, and stability of cryptocur-

rencies. Proc. Nat. Acad. of Sci. 115, 1131-1134 (2018).

8. G. Caginalp, B. Ermentrout, A kinetic thermodynamics approach to the psy-
chology of ﬂuctuations in ﬁnancial markets. Applied Mathematics Letters 3,
17-19 (1990).

9. G. Caginalp, D. Porter V. Smith V, Initial cash/asset ratio and asset prices: An

experimental study. Proc. Natl. Acad. Sci. 9,5 756–761 (1998).

10. G. Caginalp, D. Balenovich, Asset ﬂow and momentum: Deterministic and
stochastic equations. Phil. Trans. R. Soc. Lond. A 357, 2119–2133 (1999).

11. N. Champagnat, M. Deaconu, A. Lejay, S. Boukherouaa, An empirical anal-
ysis of heavy-tails behavior of ﬁnancial data: The case for power laws. HAL
archives-ouvertes (2013).

12. N. Chen, R. Kan, R, M. Miller, M, Are the discounts on closed-end funds a

sentiment index? J. Finance 48, 795-800 (1993).

13. N. Chopra, C. Lee, A. Shleifer, R. Thaler, Yes, discounts on closed-end funds

are a sentiment index. J. Finance 48, 801-808 (1993).

14. M. Clinch, G. Cutmore, Russia ﬁnance

cryptocurren-
rise. Avail-
https://www.cnbc.com/2017/10/13/russia-ﬁnance-chief-says-

cies are a “fact of
at
able
cryptocurrencies-bitcoin-are-a-fact-of-life.html. Accessed April 1, 2018.

chief
ignore their

life” and we shouldn’t

says

15. J. Cohen, Q&A: George Church and company on genomic sequencing,

blockchain, and better drugs. Science (2018).

16. D. Dinkins, Putin condemns Bitcoin, calls for Russian ban of digital currencies,
Available at https://cointelegraph.com/news/putin-condemns-bitcoin-calls-for-
russian-ban-of-digital-currencies. Accessed April 1, 2018.

17. T. Ehrig, J. Jost, Reﬂexive Expectation Formation. Presented at the meeting of

the American Economic Association in Chicago (2012).

11

18. M. Enserink, Evidence on trial. Science 351, 1128-1129 (2016).

19. E. Fama, Efﬁcient capital markets: a review of theory and empirical work. J.

Finance, 25, 383-417 (1970).

20. D. Geltner, T. Riddiough, S. Stojanovic, Geltner, D., Riddiough, T., & Sto-
janovic, S. (1996). Insights on the effect of land use choice: The perpetual op-
tion on the best of two underlying assets. J. of Urban Econ. 39, 20-50 (1996).

21. S. Gjerstad, V. Smith, Monetary policy, credit extension, and housing bubbles:

2008 and 1929, A J. of Politics and Society 21 (2009).

22. M. Hutson, Can bitcoin’s cryptographic technology help save the environment?

Science 2017.

23. R. Kampuis, Black Monday and the future of ﬁnancial markets. Homewood:

Irwin (1989).

24. J. Jost, J. Pepper, Individual optimization efforts and population dynamics: a
mathematical model for the evolution of resource allocation strategies, with
applications to reproductive and mating systems. Theory in Biosciences 127,
31-43 (2008).

25. S. Jung-a, E. Dunkley, Bitcoin slips as South Korea threatens to shut ex-
changes, Available at https://www.ft.com/content/75e13894-eba7-11e7-bd17-
521324c81e23. Accessed April 2, 2018.

26. C. Lee, A Shleifer, R. Thaler, Investor sentiment and the closed-end fund puz-

zle. J. Finance 48, 75-109 (1991).

27. R. Mcmillian, The inside story of Mt. Gox Bitcoin’s $460 million disaster.
Wired. Available at https://www.wired.com/2014/03/bitcoin-exchange/. Ac-
cessed April 1, 2018.

28. D. Porter, V. Smith., Stock market bubbles in the laboratory. Appl. Math. Fi-

nance 1, 111-128 (1994).

29. Someone in 2010 bought 2 pizzas with 10,000 bitcoins - which today would
be worth $100 million. Available at: http://www.businessinsider.com/bitcoin-
pizza-10000-100-million-2017-11. Accessed April 18, 2018.

30. M. Pring, Martin Pring on Market Momentum. Gloucester: Int. Inst. for Eco-

momic Research, Inc (1993).

31. D. Reid, A. Kharpal, Bitcoin suffers mystery ﬂash crash on popular cryptocur-
rency index. Available at https://www.cnbc.com/2017/10/10/bitcoin-price-
falls-after-russia-proposes-ban-on-exchanges.html. Accessed April 1, 2018.

32. R. Schiller, Irrational Exuberance. University Press: Princeton (2000).

33. H. Shefrin, A Behavioral Approach to Asset Pricing. Academic Press (2005).

12

34. J. Shieber, With markets going crypto-crazy, SEC chairman weighs in. Ac-

cessed April 2, 2018.

35. R. Schiller, The use of volatility measures in assessing market efﬁciency. J.

Finance 36,291-304 (1981).

36. V. Smith, L. Suchanek, A. Williams, Bubbles, crashes and endogenous ex-
pectations in experimental spot asset markets. Econometrica 56, 1119-1151
(1988).

37. S. Stojanovic, Computational Financial Mathematics using Mathematica.

Springer: New York (2003).

38. S. Stojanovic, Risk premium and fair option prices under stochastic volatility:
the HARA solutions. Comptes Rendus Mathematique 340, 551-556 (2005).

39. S. Stojanovic, Pricing and hedging of multi type contracts under multidimen-
sional risks in incomplete markets modeled by general Itˆo SDE systems. Asia-
Pac. Fin. Markets 13 (2006).

40. L. Surhone, M. Timpledon, S. Markseken, Routh-Hurwitz Stability Crite-
rion: Stable Polynomial, Linear Function, Time-Invariant System, Control Sys-
tem, Jury Stability Criterion, Euclidean Algorithm, Sturm’s Theorem, Routh-
Hurwitz Theorem. Betascript Publishing, 2010.

41. J. Tirole, On the possibility of speculation under rational expectations. Econo-

metrica 50, 1163-1182 (1982).

42. D. Watson, M. Getz, Price theory and its uses. Lanham: University Press of

America (1981).

Acknowledgments

N/A

Supplementary materials

N/A

13

Figure 1: Stability of the 5 × 5 system in the K − q2 plane for different values of the time
scales c3 and τ . Increasing c3 and decreasing τ0 increases the region of linear stability for the
equations.

14

Figure 2: Stability for our simpliﬁed model without the presence of fundamental value or sen-
timent. The system is stable in the shaded region for the parameters q and c
τ0

.

15

