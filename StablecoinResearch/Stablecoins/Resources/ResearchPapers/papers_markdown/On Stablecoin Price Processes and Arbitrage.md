On Stablecoin Price Processes and Arbitrage(cid:63)

Ingolf Gunnar Anton Pernice

Weizenbaum Institute, Berlin 10623, Germany

Abstract. This study applies the Caginalp & Balenovic (1999) model
for asset ﬂow dynamics to fully collateralized stablecoins. The analysis
provides novel insights on how trend-reversion and reactions to peg de-
viations work together to keep stablecoin prices close to the price they
are targeting. A ﬁxed-eﬀects panel regression indicates that the model’s
abstraction of trading motivations indeed ﬁts stablecoin price processes
well. The results convey ﬁrst indication that theoretic stablecoin mod-
els might beneﬁt from modeling price dynamics to switch between two
market regimes: one for day-to-day price formation and limited arbitrage
activity; and one for extraordinary market situations.

Keywords: stablecoins · arbitrage · price formation

1

Introduction

Stablecoins are being increasingly adopted as bridge to trade traditional cryp-
tocurrencies [4, 9, 40, 48], marketed as medium-of-exchange for decentralized ﬁ-
nance and smart contracts [41,42] and have recently been approved by US regu-
lators as payment method for federally chartered banks [1]. Increasing practical
relevance fosters the demand for understanding economic properties of such in-
struments. The majority of projects simply tokenize the asset their tokens are
stabilized against (e.g. the USD, EUR or gold) or store a third asset in the
respective amount [45]. Assuming that traders trust governance, collateral and
technology, and their trust is justiﬁed, there is little room for disagreement on
the token’s fundamental values. If there were any structured deviation, eﬃcient-
market theorists might argue that market participants would seize the resulting
opportunity of arbitrage, closing the gap [26].1 Stablecoin prices would then
merely reﬂect the value of the collateral and random noise. If, however, price
adjustments are restricted by incomplete arbitrage, interesting patterns might
emerge that reﬂect the trader’s decisions [10, 22]. This paper explores and quan-
tiﬁes such dynamics.

(cid:63) I thank Gunduz Caginalp for his invaluable input and enlightening conversations. I

also thank Martin Florian and Anna Almosova for their constructive feedback.

1 In a strict sense, arbitrage opportunities can be deﬁned as “investment strategy that
guarantees a positive payoﬀ in some contingency with no possibility of a negative
payoﬀ and with no net investment” [25, p.57]. In this paper the term is used in a
wider sense, describing the trader’s perceptions.

2

I.G.A. Pernice

My empiric approach is based on a recent theoretical approach from asset
pricing literature proposed ﬁrst in [18] and reﬁned by [14] which opens up asset
pricing to dynamic systems modeling known from thermodynamic physics. In
the following, the latter will be called the “Caginalp & Balenovic (1999) asset
ﬂow” (CBAF ) approach. In a nutshell, the authors model price determination
by abstracting trading decisions as ﬂows from asset-to-cash and vice versa. As
such, traders are abstracted as being driven by price trends and the deviation
of the asset’s market price from its fundamental value. Exploring theoretic ap-
proaches to the instability of price processes, a ﬁrst application to the ﬁeld of
cryptocurrencies has been attempted by [12]. Applying the CBAF model to sta-
blecoin arbitrage promises to oﬀer a convincing model for the interplay of trend
following and peg deviations. In contrast to most models for cryptocurrency pric-
ing, the above model requires few assumptions.2 Exploring early trading data
for 11 fully collateralized stablecoins, this study evaluates the appropriateness
of the intuitive trader abstraction adopted by the CBAF approach and oﬀers
insights into stablecoin price dynamics in general. My empirical setup couples
variables approximating trend-following with a measure for peg deviations in a
dynamic coin-ﬁxed-eﬀects (coin-FE) panel data regression. The study engages in
rigorous robustness checking by testing the models for the inﬂuence of seasonal
dummies, interaction terms for the direction of trends, sign of peg deviations
and diﬀerent parameters in data preprocessing. I ﬁnd a striking diﬀerence be-
tween results being based on data with—and without outlier treatment even for
merely truncating price changes exceeding 5 standard deviations. For data in-
cluding extreme price changes, the CBAF model approximates price formation
well. Deviations from the peg and trend following are strong determinants of
coming price changes. For outlier-free data, however, the eﬀects seem to blend
in with other price-determinants (the stablecoin’s token supply and Bitcoin’s
price volatilty). This result indicates that apart from very few occasions arbi-
trage acitivity is weak. This poses the questions, whether costs of arbitrage might
be prohibitive high except for extreme but rare market situations. It might be
considered to model price formation by switching between two regimes: a ﬁrst
one oﬀering proﬁts for large trades towards the peg, and a second one being
characterized by limited levels of arbitrage activity.

The paper is organized as follows: Section 2 outlines related work, Section 3
introduces the theoretic backgrounds, Section 4 discusses data and econometric
approach. Section 5 describes the results and Section 6 concludes the study.

2 Related Work

Studies investigating the asset class and its manifestations include [45], [19],
[43], [23] and [11]. The user perception in the adoption of stablecoins has been
studied in [34], while [6] analyzed the suitability of stablecoins as save-haven
investment. The relation between cryptocurrency prices and stablecoin trading

2 Compared with, for example, currency competition models [2, 27, 28, 47], game-

theoretic approaches [13] and consumer demand models [3, 5, 8].

On Stablecoin Price Processes and Arbitrage

3

has been focused on by [9], [4], [48] and [29]. Adopting a risk-oriented approach,
[35], [36] and [37] suggest theoretic models to study stability and resilience of
stablecoins. While the latter focuses on extreme events, [40] not only oﬀers a
theoretic model for day-to-day arbitrage but also provides, to my knowledge,
the ﬁrst extensive empirical analysis of the drivers of stablecoin prices. This
paper diﬀers in perspective and econometric approach: Instead of peg deviations,
this paper analyzes price processes and tests the CBAF model for applicability.
While [40] relies on a rich database, however, just for Tether, this paper adopts
a dynamic coin-FE panel data regression on market data for 11 stablecoins.

3

Stablecoin arbitrage and the CBAF model

Stablecoin arbitrage uses primary and secondary markets [40]. On the primary
market, coins are created and redeemed against collateral with the issuer. On
the secondary market, stablecoins are traded against ﬁat and cryptocurrencies.
If market prices deviate from the peg, arbitrage traders might decide to either
trade against peg deviations directly on the secondary market or involve the
stablecoin issuer. In the ﬁrst case, arbitrage traders simply trade towards the
peg. They would buy when prices are below—and sell when prices are above the
peg. In the second case, abstracting from technical details,3 arbitrage traders
would purchase coins from the markets and redeem them with the issuer when
prices are below the peg. When prices are above the peg, traders would ﬁrst
create coins with the issuer and subsequently sell them on secondary markets.

The CBAF approach as presented in [14] models traders as switching from
cash to asset or vice versa with a certain probability k. Variable k is modeled to
include motivations based on past price changes ζ1 and the market discount rel-
ative to the asset’s fundamental value ζ2. These components are modeled using
the trader’s memory with respect to price trends and deviations from fundamen-
tal values (c1 and c2) and their focus on these two respective components (q1
and q2). Core component of ζ1 is the relative price trend f (τ ) = 1
over
period τ on time scale τ0. ζ2 is constructed around deviations g(τ ) = Pa(τ )−P (τ )
of market price P (τ ) from fundamental value Pa. Thus, the two components can
be expressed as

dP (τ )
dτ

P (τ )

P (τ )

ζ1(t) = q1c1

(cid:90) t

−∞

−(t−τ )
c1

e

· f (τ ) dτ (1)

ζ2(t) = q2c2

(cid:90) t

−∞

−(t−τ )
c2

e

· g(τ ) dτ. (2)

Limiting k to values between 0 and 1, k is constructed as k = 1

2 + tanh(ζ1+ζ2)
.
For ζ1 and ζ2 equal to zero, the probability of ﬂows from cash to asset and vice
versa are thus equally likely. Demand D and supply S of the asset are modeled
using k and the fraction already invested into the asset B. Their relation can be
1−B
expressed as D = k(1 − B) and S = (1 − k)B and thus D
B . Prices P

S = k

1−k

2

3 Models for more complex stablecoins can be found e.g. in [35] and [36].

4

I.G.A. Pernice

are assumed to change logarithmic with excess demand, leading to

1
P

dP
dt

= δ · log

(cid:17)

− 1

(cid:16) D
S

= δ · log

(cid:16)

k
(1 − k)

1 − B
B

(cid:17)

(3)

with δ representing an amplitude that scales with time. For a deeper discussion
of the model and its applications see [14], [46], [14], [17], [16] and [12]. While
this paper will not be oﬀering estimates for the individual parameters, the study
gathers evidence supporting the basic intuition of the model: Under the eﬃcient
market hypothesis, ﬂuctuations of P (t) around the peg, assumed to equal Pa,
would merely be random.4 Obviously, in this case, neither of the two components
ought to be reﬂected in market data of stablecoins. If, however, evidence of ζ1 or
ζ2 is present, it is of considerable interest to understand how the two components
are jointly driving stablecoin prices.

4 Data & Econometric Approach

The following paragraphs will discuss data preprocessing and the economic ap-
proach for testing the applicability of the CBAF model.

Data was gathered from www.coingecko.com. Similar to www.coinmarketcap.

de the data provider currently crawls 382 cryptocurrency exchanges but of-
fers hourly data over a well-documented API for free.5 The full dataset com-
prises 19 cryptocurrencies. The sample includes projects that are listed at www.
coingecko.com, promise stability of their exchange rates in their whitepapers
and collateralize their tokens to at least 100%. The study considers designs that
use the asset-pegged-to as collateral but also includes tokens that use a third
asset, often a crypto-asset, in a quantity reﬂecting at least full collateralization.
Some of the 19 cryptocurrencies are quite young and immature. Shallow mar-
kets with low volumes and few trades per measurement period might in part
be driven by market microstructure eﬀects which could lead to biased regres-
sions. To reduce noise, this study thus excludes months for that the stablecoin
shows a market capitalization of under USD 10m or daily trading volumes of
under USD 1m. Coins have been dropped completely if the remaining dataset
included less then 24 · 31 hourly observations. This restricted the dataset to 11
stablecoins with 767 to 16970 trading hours leading to 101,243 observations in
total. Table 6 of Appendix 7.3 shows that the results hold as well if market
capitalization thresholds of USD 100m and USD 5m—and thresholds for daily
trading volumes of USD 50m and USD 50k are chosen. To understand the eﬀect
of extreme values on the estimated models, price changes diverging over 5 stan-
dard deviations (SD) from the mean have been truncated. Table 2 in Appendix
7.2 gives an overview over cutoﬀ points and the relative and absolute number

4 This study assumes that traders rightfully trust in the peg as a correct estimate of
the tokens fundamental value. This fails when doubts about the stablecoins collateral
or security arise.
5 As of 2020-08-17.

On Stablecoin Price Processes and Arbitrage

5

of classiﬁed outliers. The threshold was chosen deliberately high to correct only
the most extreme values. Such might have a disproportionate eﬀect on ordinary-
least-squares (OLS) regression results [7]. To make the estimated coeﬃcients
comparable, all variables apart from the dummies have been standardized based
on Z-scores X stand = X−µ(X)

, with mean µ(·) and standard deviation σ(·).

σ(X)

To verify the applicability of the CBAF model, a linear panel regression in
conjunction with squared and cubed trend variables to model nonlinear rela-
tionships has been applied to exchange-traded funds [17] and stocks [15]. Now
this framework is applied to stablecoins by adjusting it slightly to the charac-
teristics of the dataset and adding a variety of robustness checks. Traditional
linear modeling might fail to pick up the complex relations in price formation.
In contrast to linear models, polynomials allow for very strong negative (posi-
tive) past returns to induce positive (negative) bounce-back eﬀects. Mixing up
relations between strong and weak price changes, simple auto-regressive price
regressions abstaining from the above step might miss potential information on
prices. As a remedy, following [15] and [17], this study includes variables to the
power into a ﬁxed-eﬀects panel data approach.6 To capture price trends, in ac-
cordance to [15], this paper uses a simple weighted aggregation of past price
changes. The prior might be expressed using prices P and smoothing factor s
over a look-back window d as

Tt =

1
k=1 esk

(cid:80)d

d
(cid:88)

k=1

(cid:16) Pt−k+1 − Pt−k
Pt−k

· esk(cid:17)

.

(4)

The smoothing term ensures that older observations of variable changes are en-
tering the sum with lower weights (s = −0.25 and d = 10). Trends in prices have
been shown to explain variation in future returns for cryptocurrencies in [20], [32]
and [30]. To calculate the distance D of market price P from the peg Pa, simply
Dt = Pt − Pa,t is formed. As control variables the token supply and Bitcoin’s
price-volatility7 are used. Regressions are formed denominating cryptocurrency
price changes as ∆P , the trend as T and peg deviations as D. Moreover ∆S
and ∆V BTC are the ﬁrst diﬀerences of token supply and Bitcoin’s price-volatility
, Z day
, Z month
respectively. Dummy variables include seasonal ones (Z hour
) and
t
t
others that account for the sign of the peg deviation (Z D>0
) and the direction
of the trend (Z T >0
). The unobserved coin eﬀect is denominated as ai while bt
gives the unobserved time eﬀect and the remaining residual errors are given as
uit. A parsimonious base-line regression can thus be based on unobserved-eﬀects
equation

t

t

t

∆Pi,t+1 =β2Ti,t + β3T 2

i,t + β4T 3
β5∆Si,t + β6∆V BTC + ai + bt + uit,

i,t + β5Di,t + β3D2

i,t + β4D3

i,t+

(5)

6 Robustness against multicollinearity among the regressors is ensured by checking
the respective Variance Inﬂation Factors (VIF) (compare Appendix 7.3 Table 3).
7 Controlling for the volatility of the second and third largest traditional cryptocur-
rencies by trading volume (Ether and Ripple) or for the Ethereum Gas price turned
out to yield insigniﬁcant coeﬃcients.

6

I.G.A. Pernice

while the full general regression is based on

∆Pi,t+1 =β2Ti,t + β3T 2

i,t + β4T 3

i,t + β7D3

i,t+

(6)

i,t + β5Di,t + β6D2
t + Z day

β8∆Si,t + β9∆V BTC
β11Ti,t · Z D>0

i,t + Z hour
+ β12Di,t · Z D>0

t

t

t + Z month
t
+ β13Di,t · Z T >0

t

+ β10Ti,t · Z T >0

t +

+ ai + bt + uit,

where t is the time- and i the coin index.

While two-way ﬁxed-eﬀects regression are applied to eliminate time and en-
tity eﬀects in the original framework [15, 17], recent research indicates that this
approach might lead to mostly uninterpretable coeﬃcients [31,38] and biased in-
ferences in most general applications [33]. This study thus settles on eliminating
ai by coin-ﬁxed-eﬀects but models common time eﬀects by including seasonal
dummies and control variables. Treatment of the Nickel bias and other issues
related to panel data regressions with long time series dimensions (e.g. het-
eroskedasticity, non-stationarity and serial correlation) are treated in line with
state-of-the-art approaches. For more information refer to Appendix 7.1.

5 Results

Table 1 supplies estimates of the coeﬃcients given in Equation 4. As suggested
by the applied asset pricing theory, not only current deviations from the peg but
also price trends show signiﬁcant relations with the coming hour’s price change.
Also, the adopted nonlinear regression framework has proven useful. Most of the
variables that are raised to the second and third power show high signiﬁcance
and our models explain roughly 20 % of the variance in the one-hour-ahead price
changes. However, coeﬃcient estimates vary with the way outliers are treated.
For the model based on data for which no outlier treatment has been imple-
mented (compare Column 1 Table 1), the polynomial of signiﬁcant coeﬃcients
for the estimated price change is (cid:100)∆P t+1 = −0.160Dt + 0.085D2
t . This
polynomial is displayed in Figure 1, which relates peg deviations and trends to
the coming hours price change. Even relative small peg deviations are associated
with moderate price changes. Large peg deviations, however, preceed extreme
price changes forcefully driving prices back to the peg. The coeﬃcients related to
price trends display nonlinearity as well and form (cid:100)∆P t+1 = −0.266Dt +0.178D3
t .
Weak price trends seem to be reverted, while stronger ones lead to trend fol-
lowing. In other words, series of consecutive strong price changes of the same
direction are prolonged. This might be a result of consecutive hours of price
jumps after large deviations. In comparison to price trends, but also all other
tested variables, the joint inﬂuence of the coeﬃcients for peg deviations seems
be the largest by far. Their inﬂuence is roughly symmetric for positive and neg-
ative price deviations. For the model based on data for which price changes
in excess of 5 SD have been truncated (Column 2 of Table 1), the joint esti-
mated eﬀect of price trends and peg deviations on coming price changes is dis-
played in Figure 2. For peg deviations, the polynomial of signiﬁcant coeﬃcients
is (cid:100)∆P t+1 = −0.259Dt + 0.046D2
t with roots roughly at −2.6, 0 and

t + 0.056D3

t − 0.417D3

On Stablecoin Price Processes and Arbitrage

7

Table 1. Coin-FE regression based on Equation 4.

Dependent variable:

∆Pt+1

Dt
D2
t
D3
t
Tt
T 2
t
T 3
t
∆St
∆V BTC
t

(1)

−0.160∗∗∗ (0.008)
0.085∗∗∗ (0.027)
−0.417∗∗∗ (0.046)
−0.266∗∗∗ (0.009)
−0.009 (0.023)

0.178∗∗∗ (0.053)
0.208∗∗∗ (0.077)

−0.070 (0.050)

Observations
R2
Adjusted R2
F Statistic
(df = 8; 101224)

101,243
0.200
0.200
3,162.209∗∗∗

(2)

−0.259∗∗∗ (0.008)
0.046∗∗∗ (0.006)
0.056∗∗ (0.023)
−0.184∗∗∗ (0.005)
−0.005 (0.008)
−0.011 (0.037)

0.394∗∗∗ (0.144)
−0.308∗∗∗ (0.089)

101,243
0.198
0.198
3,123.468∗∗∗

∗p<0.1; ∗∗p<0.05; ∗∗∗p<0.01
Note:
Variable denominations are given in Section 4 under Equation 4. Column (1) for
untreated- and column (2) for outlier free data. Standard errors given in brackets.

4

2

(cid:92)∆

P
t
+
1

0

-2
-4
-2

-1

0
Dt

1

-2
-1
0
Tt

1

2

2

0.6
0.4
0.2
0.0
-0.2
-0.4

(cid:92)∆

P
t
+
1

-2

-1

0
Dt

1

-2
-1
0
Tt

1

2

2

Fig. 1. Coeﬃcient
treated data

interplay for un-

Fig. 2. Coeﬃcient interplay for outlier-free
data

8

I.G.A. Pernice

1.8. The eﬀect of smaller peg deviations is in line with expectations: The relation
of peg deviations and the coming price change is positive for −2.6 ≤ D ≤ 0 and
negative for 0 ≤ D ≤ 1.8 and would thus lead to mean-reverting prices. For
positive deviations D > 1.8 and negative deviations D < −2.6, however, signs
turn and peg deviations are associated with price changes leading away from
the peg. The reason for this seemingly counter-intuitive result might be that the
majority (95.37%) of observed price changes lie within the 2 SD displayed in
Figures 1 and 2. Rather than avoiding rare but large errors from outliers, the
coeﬃcients seem to be optimized to ﬁt smaller ﬂuctuations around the peg. Not
only the results for peg deviations—but also price trends diﬀer. The latter, esti-
mated based on outlier free data, show a linear, negative relation to coming price
changes. In other words, series of price changes of equal sign revert soon. The
size of the coeﬃcients for trend and peg deviations are relatively low, though.
For instance, a peg deviation of 2 SD in negative direction is associated merely
with an increase in prices of 0.1 SD. A negative price trend of 1 SD is associ-
ated with an increase of prices of around 0.2 SD. Arbitrage is estimated to have
a very limited eﬀect in the outlier-free dataset. With coeﬃcients of 0.394 and
−0.308 respectively, the change in token supply and the change in the Bitcoin’s
price volatility seem to be equally important price determinants, at least. This
contrast is surprising, given that they are caused by the truncation of merely
363 of 101243 observations. Table 5 of Appendix 7.3 gives coeﬃcients for the
same model but complemented by dummy representations accounting for hours,
weekdays, months as well as interaction terms for the sign of the peg deviation
and the direction of the price trend. The results diﬀer only negligibly.

6 Conclusion

The stark contrast of the importance of peg deviations in the ﬁtted models
with—and without outlier treatment is striking. For data including extreme
price changes, peg deviations and trend dynamics seem to approximate price
formation well. For stablecoins, the intuitive CBAF approach to model trader
behavior might thus be seen as a good approximation for the determinants of
price changes. For outlier-free data, however, the eﬀects seem to blend in with
other price-determinants. Which is the right approach to take, when describing
stablecoin price dynamics? The above results pose the question of whether sta-
blecoin markets might not best be modeled as switching between two diﬀerent
regimes: one characterized by limited arbitrage, and one setting in when markets
require correction and promise proﬁts for large trades towards the peg. It might
be considered to adjust the CBAF model to stablecoin arbitrage by including a
certain threshold of tolerance to peg deviations. Future research might analyze
whether the above results are a consequence of the costs for arbitrage.

On Stablecoin Price Processes and Arbitrage

9

7 Appendix

7.1 Robustness

The dataset applied in this study combines 11 timeseries of diﬀering lengths
and might thus be described as an unbalanced timeseries panel. While a large
T dimension is generally beneﬁcial, simple panel data approaches might be mis-
speciﬁed. A ﬁrst issue is serial correlation. In most ﬁnancial time series prior
realizations aﬀect coming ones. Including lagged data might thus be useful to
capture serial correlation in the data - this is usually referred to as dynamic panel
modeling. Instead of including lagged data explicitly, in this study, the trend vari-
able is carrying auto-regressive information.8 Using simple ﬁxed-eﬀects models
jointly with lagged variables, however, induces the so-called Nickell bias as the
lagged variable causes endogeneity in the regressors [44]. As argued by [21, p.163],
including ﬁxed-eﬀects into dynamic speciﬁcations of panel data regressions, even
for simple OLS estimates, can mitigate the issue to some degree. Their coeﬃ-
cients, however, are still seriously biased for small T . In our case, including
coin-ﬁxed-eﬀects and considering that T is very large, Nickell’s bias should be
negligible.9 There are other issues known from time-series analysis, though. [49]
warned about relying on the above for inference for non-stationary data (which
might lead to spurious regression results) and suggested to check the error term
for heteroskedasticity, serial correlation and nonnormality. To counter this prob-
lem, this study ensures stationarity using the Levin-Lin-Chu unit root test [39].
As the test does not reject the presence of a unit root for token supply and
volatility, we take ﬁrst diﬀerences of these variables.

As discussed earlier, we apply coin-FE panel regressions based on simple OLS-
estimation. As a consequence, several assumptions are to be ensured. Residuals
ought to display a mean of zero and be free of heteroscedasticity, cross-sectional,
and serial correlation. Breusch-Pagan Lagrange Multiplier tests and Pesaran
cross-sectional dependence tests are used to test for cross-sectional dependence
in the residuals. Additionally, Student’s t-tests have been applied to check the
residuals for a mean of zero. Breusch-Godfrey/Wooldridge tests have been ap-
plied to test for serial correlation. Breusch-Pagan tests are used for detecting
heteroskedasticity. While a deviation from zero for the residuals is strongly re-
jected, unfortunately, the remaining tests reveal heteroscedasticity, serial, and
also cross-sectional correlation. In other words, residuals are showing variance
clusters and are depending on their own- and even lags across coins. As a conse-
quence, the simple OLS estimator is biased. To still draw robust inferences from
the estimated model, spacial correlation consistent (SCC) estimators introduced
in [24] are used. The approach adapts Newey-West estimators to the panel set-
ting and leads to robust standard errors even in the presence of heteroscedasticity
and cross-sectional and serial correlation.

8 As discussed earlier, the trend-variable is constructed as a weighted average of a

certain number of past lags.

9 In fact, following [49], the bias for the ﬁxed-eﬀects estimator approaches zero with

rate 1/T.

10

I.G.A. Pernice

7.2 Preparatory Empirics and Descriptives

Table 1. Descriptives.

Peg Dev.

Projects

Obs.

σ Vol. Supply Min. Avg. Max.

16970 0.24 107.51 2067.48 -2.48 0.03 2.55
Tether
True-USD
16919 0.42 32.54 205.80 -4.18 0.05 4.29
Paxos Standard 16907 0.36 63.81 137.03 -3.55 0.03 3.61
16320 0.37 205.23 309.42 -3.48 0.08 3.90
USD-Coin
10358 0.56 30.23
USDK
28.56 -4.05 -0.28 4.76
41.78 -4.08 0.91 12.07
2.78
8195 1.10
Maker Dai
5226 0.21 56.76 135.18 -2.33 -0.02 2.28
HUSD
4466 0.16 208.15 176.59 -1.87 -0.01 1.84
Binance USD
15.91 -4.05 0.13 3.06
2869 0.62
Gemini Dollar
38.03 -2.76 1.33 15.37
2268 1.69
NUSD
52.48 -2.73 -0.09 1.39
767 0.40
MUSD

3.76
5.67
3.40

Data truncated at 5 standard deviations. Boundaries for market
capitalization and 24h trading volumes of USD 10m and USD 1m.
Obs. is the number of observations, σ the standard deviation. Vol.
is the 24h trading volume and Supply the token supply— both
in millions. Peg Dev. is the peg deviations scaled by factor 100.

Table 2. Outliers.

Cutoﬀ

Outliers as Deﬁned by Cutoﬀ

(in Std. Dev.) N

1
2
3
4
5
6
7
8
9
10

18839
4686
1563
683
363
192
104
52
32
26

%

18.6
4.63
1.54
0.67
0.36
0.19
0.1
0.05
0.03
0.03

Fraction of data classiﬁed as outliers. Data pre-
processing as in Table 1 of Appendix Section 7.2.

On Stablecoin Price Processes and Arbitrage

11

Table 3. Variance inﬂation factors.

St Dt D2

t D3

t V BT C
t

Tt T 2
t

T 3
t

Binance USD 2.00 1.52 1.48 1.99 2.01 1.51 1.61 1.95
3.33 2.31 6.12 4.77 3.63 1.40 1.28 1.52
Maker Dai
Gemini Dollar 1.32 2.13 1.28 2.15 1.45 2.07 1.31 2.22
4.26 1.56 2.11 2.03 4.32 1.52 1.91 1.98
HUSD
1.12 2.14 2.37 3.61 1.14 2.24 1.65 2.62
MUSD
1.51 6.96 31.12 17.00 1.30 1.97 1.23 1.82
NUSD
Paxos Standard 2.52 1.98 1.97 2.75 2.55 1.65 1.10 1.54
1.89 1.56 1.48 1.76 1.91 1.53 1.24 1.54
Tether
1.14 1.94 2.19 2.17 1.26 1.34 1.07 1.23
True-USD
1.67 2.14 2.48 2.25 1.99 1.28 1.23 1.47
USD-Coin
1.38 3.71 1.62 3.03 1.44 1.37 1.11 1.38
USDK

This table gives the variance inﬂation factors. Data preprocess-
ing as in Table 1 of Appendix Section 7.2. As all factors are
well below the rule of thumb value of 10, it is concluded that
the risk of multicollinearity is negligible. Variable denominations
are given in Section 4 under Equation 4.

Table 4. Unit root tests.

Pt

Dt

Tt
χ2 1717.89 723.38 1717.89 7.09
df
p

22.00 22.00
0.00
0.00

2.27
22.00 22.00 22.00
1.00
0.00 1.00

St V BT C
t

This table gives the results of the unit
root test for the data truncated at 5 stan-
dard deviations. Data preprocessing as in
Table 1 of Appendix Section 7.2. Variable
denominations are given in Section 4 un-
der Equation 4. Coeﬃcient’s standard er-
rors given in brackets.

12

I.G.A. Pernice

7.3 Robustness Checks

Table 5. Coin-FE regression.

Dependent variable:

∆Pt+1

(1)

(2)

Dt
D2
t
D3
t
Tt
T 2
t
T 3
t
∆St
∆V BTC
t
Z hour
t
Z day
t
Z month
t
D · Z D>0
t
D · Z T >0
t
T · Z D>0
t
T · Z T >0
t

−0.111∗∗∗ (0.010)
0.089∗∗∗ (0.027)
−0.472∗∗∗ (0.047)
−0.248∗∗∗ (0.012)
−0.010 (0.023)

0.162∗∗∗ (0.054)
0.202∗∗∗ (0.074)

−0.230∗∗∗ (0.014)
0.047∗∗∗ (0.007)
0.032 (0.025)
−0.180∗∗∗ (0.009)
−0.006 (0.009)
−0.015 (0.038)

0.392∗∗∗ (0.142)
−0.304∗∗∗ (0.089)
−0.0003 (0.001)
−0.001 (0.001)

−0.063 (0.051)
−0.0003 (0.0003)
−0.0002 (0.0003)
−0.003∗∗∗ (0.0003) −0.006∗∗∗ (0.001)
−0.018∗∗∗ (0.002)
−0.003∗∗ (0.001)
0.003∗∗∗ (0.001)
0.0001 (0.001)

−0.006 (0.009)
−0.011 (0.007)
−0.005 (0.008)
0.009 (0.007)

Observations
R2
Adjusted R2
F Statistic
(df = 15; 101217)

101,243
0.208
0.208
1,769.824∗∗∗

101,243
0.200
0.199
1,681.830∗∗∗

∗p<0.1; ∗∗p<0.05; ∗∗∗p<0.01
Note:
This table gives the results of a coin-FE regression for the full model
speciﬁed in Equation 4. Variable denominations are given in Section
4 under Equation 4. Column (1) for untreated- and column (2) for
outlier free data. Coeﬃcient’s standard errors given in brackets.

On Stablecoin Price Processes and Arbitrage

13

)
1
1
0
.
0
(

∗
∗
∗
2
5
2
.
0
−

)
1
1
0
.
0
(

)
7
0
0
.
0
(

∗
∗
∗
9
0
1
.
0

∗
∗
∗
4
3
1
.
0
−

)
5
0
0
.
0
(

1
0
0
.
0

)
5
0
0
.
0
(

5
0
0
.
0

)
9
1
0
.
0
(

3
1
0
.
0

)
2
0
0
.
0
(

∗
∗
∗
9
1
0
.
0

)
5
8
0
.
0
(

∗
∗
7
0
2
.
0
−

)
5
0
0
0
.
0
(

1
0
0
.
0

)
5
0
0
0
.
0
(

∗
1
0
0
.
0
−

)
1
0
0
.
0
(

)
6
0
0
.
0
(

)
5
0
0
.
0
(

)
6
0
0
.
0
(

)
5
0
0
.
0
(

∗
∗
∗
5
3
0
.
0

∗
∗
∗
6
1
0
.
0

∗
∗
∗
3
0
0
.
0
−

∗
∗
∗
7
3
0
.
0
−

∗
∗
∗
7
1
0
.
0
−

)
8
0
0
.
0
(

∗
∗
∗
5
9
0
.
0
−

)
7
1
0
.
0
(

∗
1
3
0
.
0
−

)
3
4
0
.
0
(

)
8
0
0
.
0
(

∗
∗
∗
0
1
1
.
0
−

∗
∗
∗
4
8
1
.
0
−

)
5
1
0
.
0
(

1
0
0
.
0
−

)
2
2
0
.
0
(

∗
∗
∗
5
4
1
.
0

)
1
4
0
.
0
(

9
5
0
.
0

)
4
4
0
.
0
(

7
2
0
.
0
−

)
2
0
0
0
.
0
(

4
0
0
0
.
0

)
3
0
0
0
.
0
(

)
1
0
0
.
0
(

)
2
0
0
0
.
0
(

∗
4
0
0
0
.
0
−

∗
∗
∗
1
0
0
.
0
−

∗
∗
∗
0
1
0
.
0
−

)
1
0
0
.
0
(

2
0
0
0
0
.
0
−

)
1
0
0
.
0
(

∗
∗
∗
2
0
0
.
0
−

)
1
0
0
.
0
(

1
0
0
.
0
−

)
9
1
0
.
0
(

)
5
1
0
.
0
(

∗
∗
∗
2
2
1
.
0

∗
∗
∗
6
6
3
.
0
−

)
5
2
0
.
0
(

∗
8
4
0
.
0

)
3
1
0
.
0
(

)
1
1
0
.
0
(

∗
∗
∗
6
7
1
.
0
−

∗
∗
∗
9
2
0
.
0
−

)
0
8
1
.
0
(

)
9
4
1
.
0
(

∗
∗
∗
5
7
7
.
0

∗
∗
∗
0
7
6
.
0
−

)
1
0
0
.
0
(

4
0
0
0
.
0

)
1
0
0
.
0
(

∗
∗
2
0
0
.
0
−

)
1
0
0
.
0
(

3
0
0
0
.
0

)
3
1
0
.
0
(

)
9
0
0
.
0
(

)
3
1
0
.
0
(

)
9
0
0
.
0
(

∗
∗
∗
9
3
0
.
0

∗
∗
∗
2
3
0
.
0
−

∗
∗
∗
8
3
0
.
0
−

∗
∗
∗
9
2
0
.
0

)
1
5
0
.
0
(

9
2
0
.
0

)
5
2
0
.
0
(

)
5
7
0
.
0
(

)
2
9
0
.
0
(

)
4
1
0
.
0
(

)
2
4
0
.
0
(

∗
∗
∗
1
5
4
.
0

∗
∗
∗
1
3
3
.
0
−

∗
∗
∗
1
9
2
.
0
−

∗
∗
∗
6
0
2
.
0
−

∗
∗
∗
8
1
1
.
0
−

)
6
6
0
.
0
(

∗
∗
∗
3
7
2
.
0

)
1
9
0
.
0
(

4
1
0
.
0

)
3
0
0
0
.
0
(

5
0
0
0
0
.
0

)
3
0
0
0
.
0
(

)
4
0
0
0
.
0
(

∗
∗
∗
1
0
0
.
0
−

∗
∗
∗
1
0
0
.
0
−

)
9
6
0
.
0
(

∗
∗
5
5
1
.
0
−

)
2
0
0
.
0
(

)
2
0
0
.
0
(

)
1
0
0
.
0
(

)
1
0
0
.
0
(

∗
∗
∗
6
0
0
.
0

∗
∗
∗
6
0
0
.
0
−

∗
∗
∗
6
0
0
.
0
−

∗
∗
∗
3
0
0
.
0

)
4
(

)
3
(

)
2
(

)
1
(

:
e
l
b
a
i
r
a
v

t
n
e
d
n
e
p
e
D

t

1
+
P
∆

.
s
e
l
u
r

n
o
i
t
c
i
r
t
s
e
r

k
a
e
w
r
o

t
c
i
r
t
s

h
t
i
w
t
e
s
a
t
a
d

n
o

d
e
s
a
b

l
e
d
o
m

l
l
u
f

r
o
f

n
o
i
s
s
e
r
g
e
r
E
F
-
n
i
o
C

.
6

e
l
b
a
T

t

D

2t
D

3t
D

t
T

2t
T

3t
T

t

S
∆

C
T
B
t
V
∆

r
u
o
h
Z

t

y
a
d
Z

t

h
t
n
o
m
Z

t

0
>
D
Z

0
>
T
Z

t

t

0
>
D
Z

0
>
T
Z

t

t

·

·

D

D

·

·

T

T

t
e
s
a
t
a
d
e
h
T

.
)
4
d
n
a

3
n
m
u
l
o
C
(

s
n
o
i
t
c
i
r
t
s
e
r

a
t
a
d
r
e
k
a
e
w
r
o

)
2
d
n
a

1
n
m
u
l
o
C
(

r
e
t
c
i
r
t
s
h
t
i
w
4
n
o
i
t
a
u
q
E

f
o
n
o
i
t
a
m

i
t
s
e

e
h
t

r
o
f

s
t
l

u
s
e
R

k
0
5

d
n
a
m
0
5

f
o

s
e
m
u
l
o
v

g
n
i
d
a
r
t

r
o
f

s
d
l
o
h
s
e
r
h
t

d
n
a
—
D
S
U
m
5

d
n
a
m
0
0
1

f
o

s
d
l
o
h
s
e
r
h
t

n
o
i
t
a
z
i
l
a
t
i
p
a
c

t
e
k
r
a
m
h
t
i
w

d
e
t
c
i
r
t
s
e
r

s
i

)
4
(

d
n
a

)
2
(

n
m
u
l
o
c

d
n
a

-
d
e
t
a
e
r
t
n
u

r
o
f

)
3
(

d
n
a

)
1
(

n
m
u
l
o
C

.
4

n
o
i
t
a
u
q
E
r
e
d
n
u

4

n
o
i
t
c
e
S

n
i

n
e
v
i
g

e
r
a

s
n
o
i
t
a
n
m
o
n
e
d

i

e
l

b
a
i
r
a
V

.

D
S
U

.
s
t
e
k
c
a
r
b

n
i

n
e
v
i
g

s
r
o
r
r
e

d
r
a
d
n
a
t
s

s
’
t
n
e
i
c
ﬃ
e
o
C

.
a
t
a
d

e
e
r
f

r
e
i
l
t
u
o

r
o
f

9
6
1
.
0

∗
∗
∗
8
4
0
.
4
3
9
,
1

0
4
1
.
0

∗
∗
∗
7
3
1
.
6
4
5
,
1

8
4
2
.
0

∗
∗
∗
8
6
2
.
1
0
4
,
1

9
2
2
.
0

∗
∗
∗
2
7
3
.
1
6
2
,
1

2
R
d
e
t
s
u
j
d
A

c
i
t
s
i
t
a
t
S

F

14

I.G.A. Pernice

References

1. Oﬃce of the Comptroller of the Currency federally chartered banks and thrifts
may participate in independent node veriﬁcation networks and use stablecoins
for payment activities. https://www.occ.gov/news-issuances/news-releases/
2021/nr-occ-2021-2.html, accessed: 2021-01-07

2. Almosova, A.: A note on cryptocurrencies and currency competition (1792)
3. Almosova, A.: A monetary model of blockchain (2018)
4. Ante, L., Fiedler, I., Strehle, E.: The inﬂuence of stablecoin issuances on cryp-

tocurrency markets. Finance Research Letters p. 101867 (2020)

5. Athey, S., Parashkevov, I., Sarukkai, V., Xia, J.: Bitcoin pricing, adoption, and

usage: Theory and evidence (2016)

6. Baumöhl, E., Vyrost, T.: Stablecoins as a crypto safe haven? not all of them! (2020)
7. Belsley, D.A., Kuh, E., Welsch, R.E.: Regression diagnostics: Identifying inﬂuential

data and sources of collinearity, vol. 571. John Wiley & Sons (2005)

8. Biais, B., Bisiere, C., Bouvard, M., Casamatta, C., Menkveld, A.J.: Equilibrium

bitcoin pricing. Available at SSRN (2018)

9. Bianchi, D., Iacopini, M., Rossini, L.: Stablecoins and cryptocurrency returns: Ev-

idence from large bayesian vars. Available at SSRN (2020)

10. Britten-Jones, M., Neuberger, A.: Arbitrage pricing with incomplete markets. Ap-

plied Mathematical Finance 3(4), 347–363 (1996)

11. Bullmann, D., Klemm, J., Pinna, A.: In search for stability in crypto-assets: are

stablecoins the solution? ECB Occasional Paper (230) (2019)

12. Caginalp, C.: A dynamical systems approach to cryptocurrency stability. arXiv

preprint arXiv:1805.03143 (2018)

13. Caginalp, C., Caginalp, G.: Establishing cryptocurrency equilibria through game

theory. Mathematics (AIMS), Forthcoming (2019)

14. Caginalp, G., Balenovich, D.: Asset ﬂow and momentum: deterministic and
stochastic equations. Philosophical Transactions of the Royal Society of London.
Series A: Mathematical, Physical and Engineering Sciences 357(1758), 2119–2133
(1999)

15. Caginalp, G., Desantis, M.: Stock price dynamics: nonlinear trend, volume, volatil-
ity, resistance and money supply. Quantitative Finance 11(6), 849–861 (2011)
16. Caginalp, G., DeSantis, M.: Nonlinear price dynamics of s&p 100 stocks. Physica

A: Statistical Mechanics and its Applications p. 122067 (2019)

17. Caginalp, G., DeSantis, M., Sayrak, A.: The nonlinear price dynamics of us equity

etfs. Journal of econometrics 183(2), 193–201 (2014)

18. Caginalp, G., Ermentrout, G.: A kinetic thermodynamics approach to the psychol-
ogy of ﬂuctuations in ﬁnancial markets. Applied Mathematics Letters 3(4), 17–19
(1990)

19. Clark, J., Demirag, D., Moosavi, S.: Sok: Demystifying stablecoins. Available at

SSRN 3466371 (2019)

20. Corbet, S., Eraslan, V., Lucey, B., Sensoy, A.: The eﬀectiveness of technical trading
rules in cryptocurrency markets. Finance Research Letters 31, 32–37 (2019)
21. Croissant, Y., Millo, G., et al.: Panel data econometrics with R. Wiley Online

Library (2019)

22. Delbaen, F., Schachermayer, W.: The mathematics of arbitrage. Springer Science

& Business Media (2006)

23. Dell’Erba, M.: Stablecoins in cryptoeconomics from initial coin oﬀerings to central

bank digital currencies. NYUJ Legis. & Pub. Pol’y 22, 1 (2019)

On Stablecoin Price Processes and Arbitrage

15

24. Driscoll, J.C., Kraay, A.C.: Consistent covariance matrix estimation with spatially
dependent panel data. Review of economics and statistics 80(4), 549–560 (1998)

25. Dybvig, P.H., Ross, S.A.: Arbitrage. In: Finance, pp. 57–71. Springer (1989)
26. Fama, E.F.: Random walks in stock market prices. Financial analysts journal 51(1),

75–80 (1995)

27. Fernández-Villaverde, J., Sanches, D.: Can currency competition work? Journal of

Monetary Economics 106, 1–15 (2019)

28. Garratt, R., Wallace, N.: Bitcoin 1, bitcoin 2,....: An experiment in privately issued

outside monies. Economic Inquiry 56(3), 1887–1897 (2018)

29. Griﬃn, J.M., Shams, A.: Is bitcoin really untethered? The Journal of Finance

75(4), 1913–1964 (2020)

30. Grobys, K., Ahmed, S., Sapkota, N.: Technical trading rules in the cryptocurrency

market. Finance Research Letters 32, 101396 (2020)

31. Hill, T.D., Davis, A.P., Roos, J.M., French, M.T.: Limitations of ﬁxed-eﬀects mod-

els for panel data. Sociological Perspectives 63(3), 357–369 (2020)

32. Hudson, R., Urquhart, A.: Technical trading and cryptocurrencies. Annals of Op-

erations Research pp. 1–30 (2019)

33. Imai, K., Kim, I.S.: On the use of two-way ﬁxed eﬀects regression models for causal

inference with panel data. Unpublished paper: Harvard University (2019)

34. Kimmerl, J.: Understanding users’ perception on the adoption of stablecoins-the

libra case. In: PACIS. p. 187 (2020)

35. Klages-Mundt, A., Harz, D., Gudgeon, L., Liu, J.Y., Minca, A.: Stablecoins 2.0:
Economic foundations and risk-based models. In: Proceedings of the 2nd ACM
Conference on Advances in Financial Technologies. pp. 59–79 (2020)

36. Klages-Mundt, A., Minca, A.: (in) stability for the blockchain: Deleveraging spirals

and stablecoin attacks. arXiv preprint arXiv:1906.02152 (2019)

37. Klages-Mundt, A., Minca, A.: While stability lasts: A stochastic model of stable-

coins. arXiv preprint arXiv:2004.01304 (2020)

38. Kropko, J., Kubinec, R.: Why the two-way ﬁxed eﬀects model is diﬃcult to inter-

pret, and what to do about it. Available at SSRN 3062619 (2018)

39. Levin, A., Lin, C.F., Chu, C.S.J.: Unit root tests in panel data: asymptotic and

ﬁnite-sample properties. Journal of econometrics 108(1), 1–24 (2002)

40. Lyons, R.K., Viswanath-Natraj, G.: What keeps stablecoins stable? Tech. rep.,

National Bureau of Economic Research (2020)

41. Misc.: Centre whitepaper. https://www.centre.io/pdfs/centre-whitepaper.

pdf, visited on 2018-11-30
Stably

42. Misc.:

whitepaper.

stably-public-documents/whitepapers/Stably+Whitepaper+v6.pdf
visited on 2018-07-16

https://s3.ca-central-1.amazonaws.com/
(2018),

43. Moin, A., Sekniqi, K., Sirer, E.G.: Sok: A classiﬁcation framework for stablecoin

designs. In: Financial Cryptography (2020)

44. Nickell, S.: Biases in dynamic models with ﬁxed eﬀects. Econometrica: Journal of

the econometric society pp. 1417–1426 (1981)

45. Pernice, I.G., Henningsen, S., Proskalovich, R., Florian, M., Elendner, H., Scheuer-
mann, B.: Monetary stabilization in cryptocurrencies–design approaches and open
questions. In: 2019 Crypto Valley Conference on Blockchain Technology (CVCBT).
pp. 47–59. IEEE (2019)

46. Porter, D.P., Smith, V.L.: Stock market bubbles in the laboratory. Applied math-

ematical ﬁnance 1(2), 111–128 (1994)

47. Schilling, L., Uhlig, H.: Some simple bitcoin economics. Tech. rep., National Bureau

of Economic Research (2018)

16

I.G.A. Pernice

48. Wang, G.J., Ma, X.y., Wu, H.y.: Are stablecoins truly diversiﬁers, hedges, or safe
havens against traditional cryptocurrencies as their name suggests? Research in
International Business and Finance p. 101225 (2020)

49. Wooldridge, J.M.: Introductory econometrics: A modern approach. Nelson Educa-

tion (2016)

