SoK: Stablecoin Designs, Risks,
and the Stablecoin LEGO

Shengchen Ling∗, Yuefeng Du∗, Yajin Zhou†, Lei Wu†, Cong Wang∗, Xiaohua Jia∗, Houmin Yan∗
∗City University of Hong Kong, †Zhejiang University

5
2
0
2

n
u
J

1
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
2
2
6
7
1
.
6
0
5
2
:
v
i
X
r
a

Abstract—Stablecoins have become significant assets in modern
finance, with a market capitalization exceeding USD 246 billion
(May 2025). Yet, despite their systemic importance, a comprehen-
sive and risk-oriented understanding of crucial aspects like their
design trade-offs, security dynamics, and interdependent failure
pathways often remains underdeveloped. This SoK confronts this
gap through a large-scale analysis of 157 research studies, 95
active stablecoins, and 44 major security incidents.

Our analysis establishes four pivotal insights: 1) stability is best
understood not an inherent property but an emergent, fragile
state reliant on the interplay between market confidence and
continuous liquidity; 2) stablecoin designs demonstrate trade-
offs in risk specialization instead of mitigation; 3) the widespread
integration of yield mechanisms imposes a “dual mandate” that
creates a systemic tension between the core mission of stability
and the high-risk financial engineering required for competitive
returns; and 4) major security incidents act as acute “evolu-
tionary pressures”, forging resilience by stress-testing designs
and aggressively redefining the security frontier. We introduce
the Stablecoin LEGO framework, a quantitative methodology
mapping historical failures to current designs. Its application
reveals that a lower assessed risk strongly correlates with
integrating lessons from past incidents. We hope this provides
a systematic foundation for building, evaluating, and regulating
more resilient stablecoins.

I. INTRODUCTION

Digital assets, particularly cryptocurrencies, offer a level of
transactional convenience that can surpass traditional systems.
However, the pronounced volatility of prominent cryptocurren-
cies like Bitcoin renders them unsuitable as stable mediums
of exchange. This limitation underscores the critical need
for stablecoins, which aim to facilitate seamless everyday
transactions by maintaining a stable value, thereby providing a
reliable store of value amidst market fluctuations and economic
turbulence.

Blockchain-based stablecoins have rapidly achieved a mar-
ket capitalization exceeding USD 246 billion, profoundly
influencing both the decentralized finance (DeFi) ecosystem
and its intersections with traditional financial systems. Yet,
despite this systemic importance,
the escalating frequency
of security incidents (most notably the Terra event, which
caused losses near USD 40 billion [1]) underscores an urgent
challenge. These developments mandate a rigorous, compre-
hensive understanding of stablecoin design architectures and
inherent risk profiles to inform safer practices and guide future
innovation.

While prior

research has systematically surveyed the
broader DeFi landscape [2], encompassing decentralized ex-
changes (DEXs) [3], yield aggregators [4], governance [5],

and security incidents [6], and while specific studies have
addressed stablecoins [7]–[10], these analyses often lack con-
temporary advancements or are confined by primarily eco-
nomic viewpoints. Consequently, a significant lacuna persists:
the absence of an integrated, interdisciplinary framework for
systematically understanding stablecoin design, quantifying
associated risks, and evaluating their ecosystem-wide impli-
cations.
Our work. This SoK confronts this lacuna directly. Grounded
in a large-scale analysis of 157 research studies, 95 operational
stablecoins, and 44 major security incidents, we deliver a
holistic systematization of the stablecoin ecosystem. Our work
is built upon four pivotal insights that challenge prevailing as-
sumptions and provide a new lens for understanding stablecoin
security.

Our analysis begins by establishing a foundational premise:
for a stablecoin, stability is an emergent and fragile state,
not an inherent property. Distinct from other DeFi tokens, a
stablecoin’s sole mission is peg stability. Our analysis reveals
this is not a static feature but an adaptive socio-technical
process. It relies fundamentally on two market-validated condi-
tions: sustained market confidence, earned through transparent
collateral and robust mechanisms, and effective convertibility
(liquidity) into its reference value.

This inherent fragility forces designers into a landscape of
difficult trade-offs, where we find that design choices result in
risk specialization rather than complete risk elimination.
Stablecoins typically manage certain key risks effectively (e.g.,
mitigating collateral volatility with fiat reserves) while im-
plicitly concentrating others (e.g., custodial and counterparty
risks). This risk specialization, evidenced by the ecosystem’s
near-even split between fiat- and crypto-backed paradigms,
creates critical points of failure that often demand centralized
governance, challenging the ethos of decentralization.

This landscape of risk specialization is further complicated
by a modern market demand: the integration of yield mech-
anisms. This imposes a “dual mandate” that systemically
breeds new risk. The integration of yield mechanisms, now
a mainstream feature (56.8% of stablecoins in our study),
transforms stablecoins from simple payment tools into com-
plex financial instruments. Fulfilling the mandate for high,
competitive returns (with 83.3% of yield-bearers exceeding
the US Treasury benchmark) necessitates high-risk financial
engineering, including significant reliance on derivatives and
external DeFi protocols. This introduces a fundamental tension
between the mission for stability and the strategies required for

high returns, creating new vectors for contagion and systemic
risk.

When these combined tensions culminate in real-world
incidents, the ecosystem’s evolutionary mechanic is laid bare:
security evolution is forged through trial-by-fire. Stable-
coins undergo a particularly acute evolutionary process driven
by security incidents. We find that technical exploits (e.g.,
code vulnerabilities) and economic attacks that stress-test peg
defenses act as stringent “evolutionary pressures.” These crit-
ical incidents are not merely failures; they are existential tests
that necessitate crucial adaptations and redefine the security
frontier for subsequent designs.

To translate these analytical insights into a robust evaluative
instrument, we introduce the Stablecoin LEGO framework.
This quantitative methodology, drawing an analogy from
the interlocking toy system, systematically deconstructs past
stablecoin failures to their root causes and maps these to
identifiable preventive and detective measures within extant
implementations. The outcome is a structured, weighted risk
score for individual stablecoins. The framework also incor-
porates the analysis of downstream impacts via token distri-
butions, facilitating a holistic comprehension of stablecoins’
pivotal role. Initial application to 11 stablecoins using this
framework enables the quantification of disparate risk profiles
and reveals how factors, such as the comprehensiveness of
security auditing, correlate with diminished assessed risk.

A. Contribution

Our contributions are summarized as follows:
1) A comprehensive systematization of knowledge of the
stablecoin landscape: We present the security-focused
SoK grounded in a large-scale, multi-source analysis of
157 prior studies, 95 active stablecoins1, and 44 major
security incidents.

2) Four pivotal insights into stablecoin definition, design,
and security: We challenge prevailing assumptions by
establishing that stability is an emergent property, design
is a trade-off in risk specialization, yield creates a dual
mandate with systemic risk implications, and security
evolution is driven by critical failures.

3) The Stablecoin LEGO framework: We propose a novel
quantitative methodology for evaluating stablecoin risk
by systematically mapping historical failure modes to
preventive and detective measures. This enables struc-
tured, repeatable risk assessment and supports continu-
ous ecosystem monitoring.

The SoK architecture is organized in Fig. 1. Specifically,
we examine previous studies for stablecoin definitions in
Section II, designs including collateral assets, stabilization
mechanisms, and yield mechanisms in Section III, security
risks in Section IV, and the Stablecoin LEGO framework
in Section V. All source code and calculation details are
published here 2.

1Our classification encompasses 95 active stablecoins. Specific sub-analyses

may focus on curated subsets for targeted investigation.

2https://github.com/stablecoin-sok

Fig. 1: The SoK architecture.

II. DEFINITION

Establishing a clear definition of “stablecoin” is founda-
tional to systematizing its security landscape. This section
delineates the research scope of this paper by dissecting how
stablecoins are characterized across academic, governmental,
and industry literature. From this comprehensive review, we
derive several noteworthy findings regarding the nature and
perception of stablecoins.

A. Methodology

Our selection criteria targeted a diverse range of research

sources to capture a holistic understanding of stablecoins:

• Academia (Google Scholar & Top Conferences): We
analyzed the top 100 Google Scholar results for “sta-
blecoin” (with over 20 citations) and relevant papers
from the last five years published in 34 leading academic
conferences across security, privacy, cryptography, net-
working, database, software engineering, programming
language, and system architecture [11].

• Governmental & Intergovernmental Bodies: We re-
viewed reports from the past five years issued by G20
member states’ financial authorities (e.g., central banks)
and key international financial organizations (i.e., IMF,
WB, BIS, FSB, FATF). Reports expressing non-official
views were excluded for rigor3.

• Industry (from Web3 Media): We examined stablecoin-
related articles and news from the past five years from
the top 5 Web3 media outlets (Cointelegraph, CoinDesk,
BeInCrypto, Crypto News, Decrypt), identified via web
traffic metrics (details in Appendix A2).

B. Result and Findings

This methodology yielded 157 research studies (56 aca-
demic, 81 governmental, 20 industry-focused), the definitions
from which are summarized in Appendix A. Our analysis
of this corpus reveals several key insights into the evolving
understanding of stablecoins.

3We exclude the studies that, although published by certain institutions,
have specially claimed irrelevance to official views. For instance, some IMF
reports claim that “the views expressed in Fintech Notes are those of the
author(s) and do not necessarily represent the views of the IMF, its Executive
Board, or IMF management.”

Section 1DefinitionSection 2DesignSection 3Security RiskActiveStablecoinsUpstream FactorDownstreamCompositionSection 4Stablecoin LEGOFrameworkTokenDistributionAcademia
Government
Industry

Academia
Government
Industry

t
n
u
o
m
a

h
c
r
a
e
s
e
R

40

20

0

’19 ’20 ’21 ’22 ’23 ’24
Year

t
n
u
o
m
a

h
c
r
a
e
s
e
R

20

10

0

’19 ’20 ’21 ’22 ’23 ’24
Year

Fig. 2: The year trend of the amount of prior stablecoin
research.

Underlying platform
Pegged asset
Stability requirement

0

50

100

Blockchain

DLT
The specified
Stable
Fixed/constant or close/near-constant/near-fixed

Public blockchain

Peg/tie/link/track

Unspecified
Minimize/lower/low/less/mitigate
Unspecified

Fiat currency

Unspecified

150
Crypto. tech.

Fig. 3: Stablecoin definitions in terms of underlying platform,
pegged asset, and stability requirement.

1) Finding 1: “Stablecoin” is a Contested and Developing
Term: A primary finding, consistently highlighted in govern-
mental and regulatory literature, is that “stablecoin” remains
an evolving, collective term lacking a universally agreed-upon
technical definition [12], [13]. Crucially, the term itself is not
an affirmation of achieved stability but is often employed as
a marketing label by market participants and authorities [12]–
[14]. Consequently, these assets may not always maintain their
peg and can exhibit risk profiles comparable to other volatile
cryptoassets [15].

2) Finding 2: Stablecoin Research Exhibits a Blooming
Trend with Shifting Focus: As illustrated in Fig. 2, the volume
of research publications surged from 2019, peaking in 2022.
Notably, while academic and governmental research output
saw a subsequent decline, industry-focused research and anal-
ysis appear to maintain a rising trajectory. This divergence
might suggest a recalibration period post-2022 (coinciding
with major stablecoin failures), with regulators and academics
perhaps adopting a more cautious, observational stance, while
the industry continues to innovate and explore new models,
potentially driven by persistent market demand or a search for
more resilient designs.

3) Finding 3: Definitional Diversity Underscores Stable-
coins as Adaptive Systems: Analysis of the collected defi-
nitions (Fig. 3) reveals significant heterogeneity across three
key descriptive dimensions:

• Underlying Platform: A vast majority of definitions
(82.28%) do not specify a particular platform type. Those

that do describe a spectrum from general Distributed
Ledger Technology (DLT) to more specific “blockchain”
or “public blockchain” technologies.

• Pegged Asset: Most definitions (71.52%) require a speci-
fied reference asset (which can include fiat currency, real-
world assets (RWAs), or other cryptoassets). A smaller
subset (14.56%) restricts this peg exclusively to fiat
currencies, while the remainder (13.92%) lack specificity.
• Stability Requirement: There is little consensus here.
Approximately half (53.80%) merely use the term “sta-
ble”, implying a desired state rather than a strict technical
criterion. Others employ verbs like “peg/tie/link/track”
(18.99%) or aim to “minimize/lower/mitigate” volatility
(15.82%). Only a small fraction (4.43%) explicitly de-
mand a fixed or near-fixed value, with the rest (6.96%)
not detailing the stability criterion.

The inherent vagueness in these common definitional com-
ponents, particularly regarding the “stability requirement”,
suggests an implicit acceptance of potential price fluctuations.
As noted by the Deutsche Bundesbank [16], the price of a
stablecoin is not perfectly correlated with its reference asset
due to supply and demand dynamics on trading platforms. This
underscores a crucial nature: stablecoins are better understood
as adaptive socio-technical systems rather than static monetary
instruments. Their stability is consequently a dynamic and
often fragile equilibrium, not an inherent, guaranteed property.

C. Research Scope

Given the definitional landscape, we establish our research

scope for this SoK as follows:
Broad definition. We acknowledge the widely accepted defini-
tion from the Financial Stability Board (FSB) [17], entrusted
by the G20: “A crypto-asset that aims to maintain a stable
value relative to a specified asset, or a pool or basket of
assets.”
Strict definition. While the FSB definition is encompassing,
significant regulatory and systemic risk concerns prioritize
stablecoins pegged to fiat currencies. These are perceived to
have a greater potential to become widely accepted means
of payment, thereby posing more immediate and substantial
monetary and financial stability risks [18], [19]. Therefore,
for the purpose of this SoK, we adopt a strict definition: “A
crypto-asset that aims to maintain a stable value relative to a
specified fiat currency, or a pool or basket of fiat currencies.”
This focused scope allows for a deeper and more coherent
analysis of the security risks pertinent to the most systemically
relevant class of stablecoins.

D. Similar Concepts

It is also noteworthy that analogous concepts exist within
the aforementioned stablecoin definitions which are prone to
confusion. However, in this paper, we intentionally exclude
these concepts, as they are either deliberately or incidentally
developed for distinct purposes and fall outside the scope of
the established community consensus on stablecoins.

Central Bank Digital Currency (CBDC). CBDC is usually
the digital form of central bank currency instead of third
parties, and may or may not adopt technologies like distributed
ledger or blockchain. CBDC would create a modern alternative
to stablecoins, as suggested by Deutsche Bundesbank [16].
Tokenized fund. A digital representation of an asset or owner-
ship right as a token on a blockchain [20]–[23], exemplified by
Franklin Templeton FOBXX [24] and BlackRock BUIDL [25].
This concept is excluded from this paper as it aligns more
closely with financial constructs regulated by securities laws
and primarily caters to the asset management and investment
sectors, and should be viewed as an alternative to secured
stablecoins or a supplement to CBDCs suggested by the Bank
of Russia [26].
Wrapped token. A digital asset that reflects the value of
another cryptocurrency from a different blockchain, such as
Wrapped BTC (WBTC) [27] on Ethereum, aiming at address-
ing the challenge of interoperability across blockchains [28]–
[30]. This concept is excluded from this paper as it primarily
functions as an interoperability solution rather than maintain-
ing value stability.
Bridged token. A digital asset
is bridged from one
blockchain to the other via a cross-chain bridge. Typical ex-
amples include USDC (Ethereum) - USDC.e (Optimism) [31].
It differs from a wrapped token in that it may have already
natively existed on the target blockchain before bridging, while
still excluded for the same reason.
Liquidity provider (LP) token. A token issued to liquidity
providers on AMM protocols, tracking individual shares to
the overall liquidity pool [32], [33]. We exclude it because
it primarily exists within the AMM system as an ownership
certificate, which can take other forms, such as NFTs.
Liquidity staking token (LST). Also known as liquidity
staking derivative (LSD), tokenized representations of staked
tokens [34], [35]. Typical examples include Lido stETH [36]
on Ethereum. We exclude it from this paper because they are
considered add-on derivatives of liquidity staking.

that

Insight 1: Distinct from multi-utility DeFi tokens, a
stablecoin’s sole objective is peg stability. As adaptive
socio-technical systems, this vital function fundamen-
tally relies on two vital, market-validated conditions: 1)
sustained market confidence, paramount due to absent
universal backing rules and earned through transparent
collateral and robust stabilization, and 2) effective
convertibility (liquidity) ensuring consistent exchange
for its reference value.

III. DESIGN

Fig. 4: The distribution of top 20 stablecoins regarding market
capitalization (in million USD).

combining collateralization with algorithmic adjustments to
pursue stability. We therefore adopt a multi-faceted approach
to classify and analyze stablecoin designs.

A. Methodology

To systematically understand stablecoin design, we identify
three primary attributes as classification criteria: 1) Collateral
Asset types, 2) Stabilization Mechanisms, and 3) native Yield
Mechanisms. Our analysis covers 95 existing stablecoins,
selected by market capitalization (over $10M from sources of
DefiLlama [37], CoinMarketCap [38], and CoinGecko [39]).
We verified features via official documentation and excluded
failed or inactive projects to focus on currently operational
designs (see Appendix B for the list).
Observation 1: Market Concentration. The stablecoin mar-
ket is highly concentrated: the top 5 (USDT, USDC, USDS,
USDe, DAI) constitute over 93% of total market capitalization,
and the top 20 represent 98% (Fig. 4). This underscores the
dominance of a few major stablecoins, consistent with the
Pareto Principle.
Observation 2: Motivations for Stablecoin Emergence.
Despite market concentration, new stablecoins continually
emerge, driven by diverse motivations beyond simple price
stability:

• Regional demand: catering to local economies with fiat-

pegged stablecoins (e.g., EURS for Euro).

• Ecosystem demand: providing native stablecoins for bur-
geoning blockchain ecosystems (e.g., Blast USDB).
• Decentralization focus: offering alternatives (e.g., Mak-
erDAO DAI) to centralized issuers like Tether, aiming to
mitigate counterparty risks.

• Stability innovation: introducing novel mechanisms, e.g.,
hedging strategies, to enhance price stability (e.g., Ethena
USDe).

• Financial innovation: incorporating new economic mod-
els, governance structures, or yield-bearing features (e.g.,
Sky USDS).

Building upon the strict definition of stablecoins (Sec-
tion II),
this section deconstructs their design landscape.
While a common initial categorization distinguishes between
collateralized stablecoins (backed by assets) and algorithmic
stablecoins (relying on dynamic mechanisms), this distinction
is not absolute. Many stablecoins employ hybrid approaches,

B. Collateral Asset

Collateral assets are fundamental to many stablecoin de-
signs, underpinning their purported value. Before analysis, we
clarify crucial distinctions: the pegged asset is the target value
(e.g., USD); the collateral asset backs the stablecoin; and the

USDT63.27%USDC25.48%USDS2.90%USDe2.16%DAI1.88%USD10.89%FDUSD0.67%USDtb0.60%PYUSD0.37%USD00.26%USDY0.24%TUSD0.20%SyrupUSDC0.19%USYC0.16%USDf0.16%USDD0.16%USDX0.15%RLUSD0.13%USDG0.12%Others6.19%51

most volatile class, with potential for drastic price swings.
To quantify this, we use the Price Standard Deviation (PSD):

45

51

s
n
i
o
c
e
l
b
a
t
S
#

40

20

0

2
Cryptocurrency
RWA

Fiatcurrency

s
n
i
o
c
e
l
b
a
t
S
#

40

20

24

18

13

7

Supplyadjustment
Liquidation

Emergency
Hedging

Implicit

s
n
i
o
c
e
l
b
a
t

S
#

15

10

5

16

17

14

11

5

6

6

6

Derivatives-drivenyield
Cashandcashequivalentyield
L1stakingreward
Nativeprotocolrevenue

Secondarytokenemission
ExternalDeFiyield
Third-partycustodianrevenue
Subsidizedfundfromcommunity

Fig. 5: Stablecoin distributions in terms of collateral asset, sta-
bilization mechanism, and yield sources (across yield-bearing
stablecoins).

purchase fund is the medium for acquiring the stablecoin, not
necessarily linked to its peg or collateral. We categorize col-
lateral into: 1) Fiat currency (or equivalents like government
treasuries), 2) Real-World Assets (RWA) (e.g., commodities,
real estate, stocks), and 3) Cryptocurrency (e.g., USDT, BTC,
ETH).
Collateralization Landscape. Our analysis of 95 operational
stablecoins reveals that all are, at least nominally, fully col-
lateralized (i.e., collateral value larger or equal to 100% of
outstanding supply). This suggests a strong market tendency
towards, or higher survival rate for, designs with explicit
full backing, where complex stabilization algorithms often act
as secondary or reinforcing measures. Among these, 45 are
primarily fiat-backed, 2 by RWA, and 51 by cryptocurrencies
(total exceeds 95 due to multi-collateral designs), indicating a
near-even split in preference between fiat and crypto-collateral
paradigms (Fig. 5).
Comparative Analysis of Collateral Types. We evaluated
USD (fiat), Gold (RWA), and Bitcoin (cryptocurrency) against
four key attributes (Table I), including volatility, redemption
efficiency, inflation resistance, and compliance. We recognize
that liquidity is paramount, with inflation and compliance risks
impacting this core tenet. This comparison reveals inherent
trade-offs: each asset type excels in some dimensions while
underperforming in others, underscoring that collateral choice
fundamentally dictates a stablecoin’s risk-return profile and
operational characteristics.

1) Volatility: Collateral asset volatility directly impacts a
stablecoin’s ability to maintain its peg. Highly volatile collat-
eral necessitates more aggressive stabilization mechanisms and
can undermine user confidence. While fiat currencies, particu-
larly the USD, are generally regarded as the most price-stable
collateral options, RWAs like gold exhibit moderate fluctuation
based on market dynamics. Cryptocurrencies represent the

P SD =

(cid:118)
(cid:117)
(cid:117)
(cid:116)

1
T

T
(cid:88)

t=1

(P (t) − µ)2,

(1)

where T is the observation period, P (t) is the asset price at
time t ∈ T , and µ is the mean price over T . We calculated
PSD using daily closing prices from Yahoo Finance for the
five-year period from March 25, 2020, to March 24, 2025.
Our analysis confirms that USD exhibits the lowest volatility,
whereas Bitcoin demonstrates the highest among the three
representative assets.

2) Redemption Efficiency: Redemption efficiency, which is
the ease and speed with which collateral can be converted
to meet redemption demands without adverse price impact,
is crucial for stablecoin trustworthiness. Fiat currencies of-
fer high global liquidity and accessibility. RWAs can face
logistical hurdles and slower conversion times. Cryptocur-
rencies present variable liquidity dependent on the specific
asset and prevailing market conditions, potentially stressing
stability during demanding redemption periods. We evaluate
this using a Redemption Efficiency Index (REI), grounded in
market microstructure theory, which amalgamates normalized
transaction costs and redemption delays:

REI = f ′ + d′,

(2)

where f ′, d′ are min-max normalized values (scaled to [0,1])
representing typical
transaction fees (in USD equivalents)
and redemption delays (in days) associated with converting
the collateral asset. A lower REI signifies higher efficiency.
Our analysis indicates Bitcoin offers the highest redemption
efficiency due to its near-instant, on-chain settlement capa-
bilities, while physical gold ranks lowest due to logistical
requirements. USD efficiency is high but typically subject to
banking system operational hours and settlement lags.

3) Inflation Resistance:

Inflation erodes the purchasing
power of assets used as collateral. Assets that can hedge
against inflation are therefore valuable for preserving a stable-
coin’s real value. While certain cryptocurrencies, particularly
those with capped supplies, are posited as inflation hedges, fiat
currencies directly lose purchasing power during inflationary
periods. RWAs like gold have a mixed historical record as
consistent inflation hedges.

We assess inflation resistance using the real return (r),
derived from the Fisher Equation: (1 + i) = (1 + r)(1 + π),
where i is the nominal return of the collateral asset and π
is the relevant annual inflation rate. For low inflation, this
approximates to:

r ≈ i − π.

(3)

We determine i by taking the median yield rate offered
by stablecoins in our dataset that are collateralized by the
respective asset
type (e.g., median yield of USD-backed
stablecoins for USD’s nominal return). This proxy reflects
the returns generated and passed on by stablecoin issuers

Volatility (PSD)

Redemption efficiency (REI)

Inflation resistance (r)

Compliance (J-Score)

USD (fiat currency)
Gold (RWA)
Bitcoin (cryptocurrency)

5.93
313.77
23413.08

0.9990
2.0000
0.0000

-4.25
5.89
5.78

21
21
13

TABLE I: Comparison of three collateral assets, where bold numbers are better ones.

utilizing that collateral. Our results show that gold and Bitcoin-
backed stablecoin models offer superior inflation resistance,
while USD-backed models demonstrate negative real returns,
reflecting an erosion of purchasing power.

4) Compliance: The regulatory treatment of collateral as-
sets across jurisdictions introduces significant, often unpre-
dictable, risk. While fiat currencies and traditional RWAs
like gold are generally accepted within established regulatory
frameworks in most G20 nations, cryptocurrencies navigate a
more complex and rapidly evolving legal landscape, impacting
their suitability and reliability as collateral.

To quantify this, we propose a Legal and Jurisdictional
Compliance Score (J-Score), a primarily qualitative aggrega-
tion:

N
(cid:88)

J =

wk · Ck,

(4)

k=1

where N is the number of G20 jurisdictions considered
(N=21), wk is the weight for jurisdiction k (here, wk = 1
for all, signifying equal weight), and Ck ∈ {0, 1} indicates
whether the collateral asset type is generally considered com-
pliant (1) or faces significant restrictions/lack of clarity (0)
for use in financial instruments or as a reserve asset within
that jurisdiction. A higher J-Score indicates broader regulatory
acceptance of the collateral type. Our analysis suggests that
Bitcoin, as a collateral type, faces compliance ambiguities
or restrictions in approximately 40% of G20 jurisdictions, a
higher percentage than for USD or Gold.
Discussion: Stablecoin Compliance. Beyond collateral, sta-
blecoins also face a rapidly evolving regulatory landscape
(e.g., EU’s MiCA, frameworks in Singapore, US’s STABLE
and GENIUS, Hong Kong Stablecoins Ordinance). The se-
curity implications of these diverse and emerging regulatory
demands warrant continuous investigation.

C. Stabilization Mechanism

Many stablecoins employ explicit mechanisms to actively
defend their peg. Our analysis (Fig. 5) shows that while over
half (53.68%) rely on an “implicit” mechanism (primarily
trust in the issuer and their reserves), others use active strate-
gies. Specifically, liquidation (18.95%) and supply adjustment
(25.26%) are prevalent, with hedging (13.68%) and emergency
features (7.37%) also utilized (total exceeds 100% as some
implement multiple mechanisms).

1) Liquidation: Liquidation mechanisms are foundational
to many collateralized stablecoins, enforcing solvency by
auctioning off undercollateralized positions. When volatile
collateral backing a debt position falls below a predetermined
threshold (the liquidation ratio), the system permits liquidators

Algorithm 1: Liquidation
Input: current_value, debt, liquidation_threshold,

discount, liquidation_rate

Output: seized or "Safe"

1 if current_value/debt < liquidation_threshold then
seized ← current_value × (1 − discount);
2
repay(debt × liquidation_rate);
return seized

4

3

5 return “Safe”

to repay a portion of the debt in exchange for seizing the
underlying collateral at a discount [40]–[42]. This process
inherently relies on over-collateralization, where the initial
collateral value significantly exceeding the minted stablecoin
value, to buffer against price declines. MakerDAO DAI is a
prominent example.

Considered a relatively robust approach,

liquidation is
widely adopted. MakerDAO DAI, one of the largest stable-
coins employing this, has navigated market volatility without
catastrophic failures of its core liquidation engine. A key
insight from Klages-Mundt et al. [8] is that such mecha-
nisms shift risk from a systemic “equity risk” (borne by
all token holders) to an “agent risk” (borne by individual,
over-collateralized vault owners). This design shares structural
similarities with borrowing/lending protocols, facilitating their
natural integration or evolution into stablecoin issuers (e.g.,
Aave GHO).

2) Supply Adjustment: This class of mechanisms aims to
stabilize price by algorithmically modulating the stablecoin’s
circulating supply, based on the economic principle that de-
creasing supply raises prices and vice-versa. While methods
vary from direct minting/burning of tokens to adjusting bor-
rowing interest rates to influence demand, they typically rely
on arbitrage incentives for market participants. USDD is a
notable example.

Theoretically, such mechanisms find grounding in concepts
like the Quantity Theory of Money: M · V = P · Q, where
adjusting money supply M is intended to influence the price
level P [7]. By algorithmically contracting supply when the
price is below peg (to induce scarcity) or expanding it when
above peg (to reduce premium), these systems attempt to
dynamically manage inflationary or deflationary pressures on
the stablecoin’s value.

In practice, however, stablecoins primarily reliant on en-
dogenous supply adjustments have a notable history of failure
(e.g., Terra UST, Neutrino USDN, Beanstalk BEAN, Haven
xUSD). A critical lesson from these incidents is their acute

Algorithm 2: Supply Adjustment
Input: current_supply, current_price, target_price,

adjustment_coefficient

Output: None
1 supply_change ←

current_supply × adjustment_coef f icient ×
(current_price − target_price);
2 if current_price > target_price then
3

mint(supply_change);

4 else
5

burn(abs(supply_change));

susceptibility to reflexive market dynamics and oracle un-
reliability. The adjustment processes can exhibit significant
lags, failing to respond adequately to rapid sentiment shifts
or well-capitalized attacks, creating death spirals. The specific
security risks inherent in these designs are further explored in
Section IV.

3) Hedging: Hedging strategies aim to neutralize the price
risk of volatile collateral by establishing offsetting positions
in derivative markets [43], [44]. Delta-hedging, for example,
seeks a “delta-neutral” position where the stablecoin issuer’s
net exposure to the collateral’s price movement is theoretically
zero. If minting a stablecoin against 1 ETH creates a +1 ETH
price exposure (positive delta), a corresponding short position
in an ETH perpetual contract of equivalent size would be taken
to neutralize this. Ethena USDe and Elixir deUSD exemplify
this approach.

A critical aspect of these designs is their operational de-
pendency on centralized exchanges (CEXs) for providing the
necessary derivative instruments and liquidity for hedging.
This introduces significant counterparty risk: the failure or
compromise of a CEX partner could jeopardize the hedge
and, consequently, the stablecoin’s backing. Furthermore, for
models like Ethena, where yield is partly generated from
derivative positions (e.g., funding rates, basis spreads), the
sustainability and security of these yields are also contingent
on the continuous, reliable functioning of these CEXs, creating
layers of external dependencies.

4) Emergency Mechanism: Acknowledging the limitations
of purely algorithmic responses in extreme scenarios, some
stablecoins incorporate emergency mechanisms. These can
include features to temporarily suspend core functions like
transfers or redemptions during severe market dislocations or
security incidents (e.g., Curve crvUSD, Paxos USDP). Another
approach involves maintaining segregated bailout reserves,
deployable via a trusted committee or governance vote to
recapitalize the system during a crisis (e.g., Gyroscope GYD,
dForce USX).

While intended as safety nets, such mechanisms inherently
introduce centralization and governance risks. The power to
invoke emergency actions often resides with a core team or a
small group of token holders, raising concerns about potential
abuse, or failure to act appropriately under pressure. These

includes

stablecoins

Stabilization Mechanism: This

mechanisms shift trust from fully autonomous code to human
judgment and intervention, introducing governance challenges
that extend beyond typical smart contract rule-based security
considerations.
5) Implicit
dominant
category (51/95)
lacking explicit,
algorithmically-defined stabilization protocols, relying instead
in the issuer’s ability and commitment
on users’
to maintain the peg,
reserve
typically through robust
management and redemption processes (e.g., USDT, USDC).
The “stability” here is an emergent property of this trust and
the perceived strength of off-chain backing. However, this
category exhibits extremes: from highly resilient, large-cap
stablecoins to smaller, more vulnerable ones where “implicit”
may equate to an absence of robust defenses, heightening
risks like rug pulls if issuer trust is misplaced.

trust

6) Discussion: Towards a Control-Theoretic View of Stabi-
lization: No single stabilization mechanism is flawless, thus
effective peg maintenance often requires judicious strategy
selection and scaling. Control theory finds extensive applica-
tions in financial markets, including monetary policy control,
portfolio optimization, trading and market making, and price
stabilization for exchange rates and commodities. Therefore,
we propose that stablecoin stabilization can be fruitfully mod-
eled as a control system. Price deviations from the peg act as
error signals, triggering corrective actions from stabilization
mechanisms (control inputs u) to counteract disturbances d
(e.g., market volatility) and guide the system state x (stable-
coin price P (t)) back to its target Ppeg. A general state-space
representation could be:

dP (t) = (AP (t) + BU (t))dt + σ(P (t))dW (t),

(5)

where U (t) is a vector of control inputs from mechanisms
like supply adjustment (us), liquidation (ul), etc. While a full
quantitative development is future work, this control-theoretic
perspective offers a powerful abstraction for analyzing the
dynamic interactions and potential optimality of combined
stabilization strategies.

Insight 2: The pursuit of stability forces choices that
result in risk specialization rather than comprehensive
risk elimination. This means designs typically manage
certain key risks effectively (e.g., reserve volatility in
a fiat-backed model) while implicitly accepting or con-
centrating other risks (like custodial and counter-party
risks in the same model), forming a trade-off evidenced
by the ecosystem’s near-even split between fiat-backed
(47.37%) and crypto-backed (53.68%) paradigms. This
risk concentration creates critical points of failure that,
in turn, demand centralized governance for decisive
action and accountability, directly challenging the ethos
of decentralization.

D. Yield Mechanism

Native yield offerings are a significant driver for stable-
coin adoption and innovation, positioning them as financial

64

32

16

8

4

2

)

%

(

e
t
a
r

d
l
e
i
Y

10

100

10000
1000
Market capitalization (million USD)

· · ·

160000

Fig. 6: The yield distribution of stablecoins paired by market
capitalization (log form due to imbalanced data).

products beyond simple payment tools. Our analysis consid-
ers yields directly provided by issuers, excluding third-party
protocol yields, across the 95 selected stablecoins.

1) Yield Rate Landscape: We present the relationship be-
tween reported yields and market capitalizations using a
log-log distribution (Fig. 6) for effective visualization. This
analysis reveals a distinct inverse correlation: stablecoins with
smaller market capitalizations tend to offer higher native
yield rates. We posit this reflects a common strategy among
emerging or smaller protocols to aggressively attract users and
compete for market share, often by offering premium returns
to incentivize early adoption. Quantitatively, our survey of
95 operational stablecoins indicates that 54 (56.84%) provide
native yield-bearing features. Notably, among these yield-
bearing stablecoins, 45 (constituting 83.33% of this subset)
offer annual percentage yields (APYs) exceeding 4.25%. This
threshold renders their offerings competitive with, or superior
to, traditional benchmarks of the US 10-year Treasury yield
(at the time of writing).

2) Yield Source Taxonomy and Findings: We identified 8
primary yield generation patterns: 1) Native protocol revenue,
2) Cash and cash equivalent yield (e.g., T-bills), 3) L1 stak-
ing rewards, 4) Derivatives-driven yield (e.g., basis trading,
funding rates), 5) External DeFi protocol yield, 6) Third-party
custodian revenue, 7) Community-subsidized funds, and 8)
Secondary token emissions. Our analysis (Fig. 5) reveals a
complex interplay between traditional financial models and
crypto-native risk appetites:
1. Dichotomy in Yield Generation: TradFi Roots with
Crypto-Native Risk Layers. The most prevalent yield sources
are anchored in traditional finance: “Cash and cash equivalent
yield” (utilized by 31.48% of yield-bearing stablecoins in our
study) and “Native protocol revenue” from fees (29.63%). This
reliance on established models suggests a market inclination
towards perceived sustainability. Yet,
in striking contrast,
the third most common source is “Derivatives-driven yield”
(25.93%), signaling a significant embrace of crypto-native
financial engineering with distinct risk profiles not found in
traditional monetary instruments.
2. Financialization Heightens Complexity and Systemic

Interconnectedness. The notable adoption of “Derivatives-
driven yield” (25.93%) and “External DeFi yield” (20.37%)
transforms stablecoins from mere payment tokens into actively
managed financial products. This evolution inherently breeds
complexity and new vectors for systemic risk. These strategies
create direct counterparty exposures to derivative providers
and critical dependencies on the operational security and
economic stability of external DeFi applications (e.g., Aave,
Curve). Such deep entanglement implies that failures in these
third-party services could trigger cascading solvency issues
across multiple stablecoins.
3. Unsustainable Yields Signal Structural Fragility in a
Market Segment. A significant portion of yield-bearing sta-
blecoins (22.22% combined) rely on inorganic and inherently
unsustainable sources: “Subsidized funds from community”
and “Secondary token emissions.” These are not revenue from
viable economic activity but are functionally marketing ex-
penses or temporary incentives. This indicates that a segment
of the market may be structurally fragile, reliant on bootstrap-
ping growth through mechanisms that are finite, potentially
masking underlying economic non-viability until subsidies
deplete or emission-based tokens devalue under pressure.

Insight 3: The integration of yield imposes a “dual
mandate” that reforges stablecoins from passive an-
chors into complex financial instruments. This trans-
formation is now mainstream: 56.84% stablecoins offer
yield, of which 83.33% provide returns exceeding the
US 10-year Treasury benchmark. Fulfilling this aggres-
sive yield mandate necessitates high-risk financial engi-
neering, evidenced by the significant reliance on deriva-
tives (25.93%) and external DeFi protocols (20.37%).
This tension between the mandate for stability and
the strategies required for high returns introduces a
web of market, counter-party, and contagion risks that
fundamentally redefines the asset’s evolutionary stakes.

IV. SECURITY RISKS

The systemic importance of stablecoins means their vulner-
abilities can trigger cascading failures. This section analyzes
the spectrum of security risks afflicting stablecoins, draw-
ing insights from an empirical study of real-world security
incidents detailed in Appendix C. Based on 44 significant
incidents, we present a statistical breakdown of their root
causes, categorizing them into three primary types: Price
Fluctuation, Smart Contract Issues, and Peripheral Factors.
Each cause is illustrated with a representative case study. The
incidents were selected based on two primary criteria:

• Loss exceeding $100K, collated from reputable sources
such as BlockSec Phalcon Explorer
[45], REKT
Database [46], SlowMist Hacked [47], ChainLight Lu-
mos [48], and Neptune Mutual database [49].

• Direct relevance to stablecoin failures, excluding inci-
dents where non-stablecoin projects failed due to external

27.27%

4.55%

25%

38.64%

6.82%

9.09%

PF - market volatility
PF - price manipulation
SCI - code vulnerability

SCI - flash loan
SCI - governance
PeF - rug pull

2.27%

4.55%

PeF - access control
PeF - impacted fund

Fig. 7: The cause distribution of historical security incidents
(where PF refers to price fluctuation, SCI refers to smart
contract issue, and PeF refers to peripheral factor).

stablecoin issues or merely incurred losses denominated
in stablecoins.

A. Price Fluctuation

As cryptoassets, stablecoins are inherently exposed to price
volatility, a primary concern for both users and attackers.
Such fluctuations can be organic, termed market volatility, or
maliciously induced, termed price manipulation. These can
manifest as gradual drifts, sudden crashes, or even single-
transaction shocks, often amplified by tools like flash loans
(further discussed in Section IV-B2).

1) Market Volatility: Market volatility tests a stablecoin’s

resilience across three interconnected stress points:

• Direct volatility of

the stablecoin itself, potentially

breaching its peg tolerance.

• Devaluation pressure on related protocol tokens (e.g.,

secondary governance tokens).

• Broad downward trends in the wider cryptocurrency

market (e.g., BTC).

Sustained market volatility can critically undermine a proto-
col’s design, implementation, and public confidence.
Case Study: Terra UST/LUNA. The algorithmic stable-
coin TerraUSD (UST) aimed for a $1 peg via an arbitrage
mechanism with its secondary token, LUNA, where 1 UST
was exchangeable for $1 worth of LUNA [1]. This design
effectively sacrificed LUNA to stabilize UST during de-peg
threats. However, significant sell pressure on LUNA triggered
a negative feedback loop, i.e., the “Death Spiral”, leading to
UST’s collapse in May 2022, despite prior academic discus-
sion of this vulnerability.

The sheer scale of the Terra/Luna collapse spurred extensive
quantitative modeling. However, a significant body of this
research concentrated on the broader financial and economic
repercussions, such as contagion effects across crypto mar-
kets [1], the market impact of public disclosures [50], [51],
flight-to-safety dynamics [52], and overarching devaluation
risks [53], [54]. A critical observation is that many of these
analyses, while valuable, often did not deeply simulate the
stabilization mechanism’s specific failure modes under duress,

a crucial aspect for understanding its security vulnerabilities
against economic attacks or cascading internal breakdowns.

Nevertheless, several studies offered more granular insights
into its failings. For instance, Uhlig [55] modeled the crash’s
progression, highlighting diverse agent behaviors concerning
convertibility during the crisis. Kurovskiy et al. [56] explored
why the arbitrage mechanism faltered, pinpointing the detri-
mental effects of floating redemption fees and critical deficien-
cies in collateral accessibility and liquidity, which are all key
parameters for mechanism resilience. From a more technical
simulation perspective, Calandra et al. [57] modeled Terra’s
transaction dynamics and specific de-peg triggers, providing
insights into the operational vulnerabilities that precipitated
the collapse.

2) Price Manipulation: Price manipulation attacks typi-
cally exploit control over a stablecoin’s (or its collateral’s)
reference price sources, which can be:

• Centralized sources: price dashboards (e.g., CoinMarket-
Cap [38]) and CEXs (e.g., Binance [58]). These are gen-
erally harder to manipulate but can suffer from reporting
lags or inter-exchange price inconsistencies.

• Decentralized sources: oracles (e.g., Chainlink [59]) and
DEXs (e.g., Uniswap [60]). Oracles can be vulnerable
if their feed sources lack sufficient decentralization or
robust validation. DEXs, especially AMM-based ones,
can amplify price swings if liquidity pools are shallow,
making them targets during periods of high volatility or
panic.

Case Study: BonqDAO BEUR. BEUR, an over-collateralized
stablecoin pegged to 1 EUR, allowed users to mint BEUR
against locked assets. Its vulnerability lay in a permissionless
price oracle where the last reported price feed for collateral
was considered the spot price. In February 2023, attackers
momentarily inflated the price of a collateral asset (WALBT)
via this oracle, minted an unearned excess of BEUR, and
subsequently halved BEUR’s price.

B. Smart Contract Issue

As blockchain-based applications, stablecoins inherit all
common smart contract vulnerabilities, while also present-
ing unique attack surfaces related to their specific economic
logic, governance structures, and interactions facilitated by
blockchain features like flash loans.

1) Code Vulnerability: Standard software flaws persist in
stablecoin contracts, including reentrancy, insufficient input
validation (e.g., Beanstalk, Prisma), and logic errors stemming
from “copy-paste” practices (e.g., Yearn). The impact of such
vulnerabilities is often direct and catastrophic.
Case Study: Cashio CASH. CASH stablecoins could be
minted against Saber LP and Arrow Protocol collateral. A
critical flaw in the mint function involved improper validation
of the Arrow account and no token matching. In March 2022,
an attacker exploited this by using worthless tokens to mint
approximately $53M in CASH, leading to the stablecoin’s
failure.

2) Flash Loan Attack: Flash loans, which are uncollateral-
ized loans borrowed and repaid within a single atomic trans-
action [61], [62], provide attackers with immense temporary
capital. While a neutral financial tool, they can be weaponized
to exploit vulnerabilities in a protocol’s economic logic, price
oracle dependencies, or governance mechanisms.
Case Study: Beanstalk BEAN. In April 2022, an attacker
leveraged a flash loan of over $1 billion (from Aave, Uniswap,
SushiSwap) to acquire enough governance tokens to pass
malicious Beanstalk Improvement Proposals (BIP18, BIP19).
These proposals authorized fund transfers to the attacker. The
entire sequence of loan acquisition, voting, proposal execution,
and loan repayment occurred within one transaction, resulting
in a $182 million loss and the de-facto failure of BEAN as a
stablecoin.

3) Governance Attack: Blockchain governance aims to
enable decentralized decision-making for protocol evolution
and safety [5], [63]. However, poorly designed, implemented,
or managed governance systems can introduce critical vul-
nerabilities, allowing attackers to manipulate outcomes for
malicious profit, with effects that are often hard to reverse.
Case Study: Mochi USDM. In November 2021, Mochi
exploited Curve’s governance by using its USDM stablecoin
thereby gaining
to acquire a large stake in CVX tokens,
disproportionate influence over Curve’s reward allocations.
This allowed Mochi to boost rewards for its own USDM pool,
attract significant liquidity, and subsequently drain $30 million
from this pool before abandoning the stablecoin.

C. Peripheral Factor

Beyond the aforementioned, a range of peripheral yet criti-

cal factors contribute to stablecoin security risks.

1) Rug Pull: A rug pull is an exit scam where project
founders or developers abruptly abandon the project after
attracting capital, leaving investors with worthless tokens [64],
[65]. This can occur in both centralized and ostensibly de-
centralized stablecoin projects, often by exploiting pre-set
vulnerabilities, centralized control points, or inadequate access
controls over protocol funds or liquidity pools.
Case Study: DEFI100. A BSC-based synthetic asset index
product, DEFI100 executed an apparent exit scam in May
2021. The project’s official website briefly displayed a mes-
sage “We lied to you, you can’t do anything with us” before
being taken offline.

2) Access Control: Compromised access control, often
involving private keys that represent ultimate authority over
contracts or funds, is a fundamental security threat [66]. The
security of admin keys, deployer wallets, and multi-signature
participants is paramount. Several major stablecoin losses trace
back to compromised operational security.
Case Study: Tether. In November 2017, Tether announced
that approximately 31 million USDT were illicitly removed
from its treasury wallet due to an external attack compromis-
ing access. Notably, despite this significant breach, USDT’s
market dominance was not fatally impacted in the long term,
highlighting complex market reactions to such incidents.

3) Impacted Fund: Stablecoins often rely on, or deposit
their reserves/collateral into, other DeFi protocols or custodial
solutions to generate yield or manage assets. The security of
these external dependencies is crucial; a failure in a third-
party application can directly impact the stablecoin’s backing
or solvency.
Case Study: Angle Protocol. The Angle Protocol held
$18M USDC in the Euler Protocol. When Euler was hacked
for $197M in March 2023, Angle Protocol’s funds on Eu-
ler were lost, rendering Angle’s stablecoin products under-
collateralized. Despite this, Angle Protocol has continued to
operate, maintaining a notable market share even today.

Insight 4: While all DeFi systems evolve, stablecoins
undergo a particularly acute evolutionary process, fo-
cusing on the core mission of improving peg stability.
Designs are thus forged through ongoing trial-and-
error, where market adoption, liquidity dynamics, and
critical incidents, with most notably technical flaws like
code vulnerabilities(38.64%) and economic stresses
from market volatility(27.27%), act as stringent “evo-
lutionary pressures”. Market feedbacks and security
(near)-incidents challenging peg integrity are pivotal.
They necessitate crucial adaptations to a stablecoin’s
peg mechanism for survival or expose fatal flaws caus-
ing failure, which then spurs broader re-evaluation of
stability models.

V. THE STABLECOIN LEGO FRAMEWORK

This section details the Stablecoin LEGO framework, our
proposed methodology for evaluating stablecoin resilience. We
will 1) present the architecture and scoring methodology of the
framework, and 2) demonstrate its practical utility by applying
it to real-world stablecoins, an analysis that yields crucial
findings regarding their systemic risks and structural integrity.

A. Motivation

A robust evaluation of stablecoins demands a framework
that addresses their inherent dual nature: they are simultane-
ously blockchain-based software and nascent monetary instru-
ments. Unlike traditional decentralized applications (DApps),
whose primary role is to provide a service or platform,
a stablecoin’s core objective is to maintain price stability
and function as a reliable digital representation of value.
Consequently, any rigorous assessment cannot be confined to
technical security audits alone; it must also incorporate ana-
lytical models from monetary theory and finance to scrutinize
the design, resilience, and economic viability of the stability
mechanism itself.
Background. Prior work has initiated the development of
stablecoin evaluation frameworks. For instance, Bluechip’s
SMIDGE framework [67] assesses stablecoins across broad di-
mensions but primarily offers high-level safety scores without
deep, systematic justification for its scoring logic. Similarly,
Moody’s Digital Asset Monitor [68] provides sophisticated

adopted for modeling complex socio-economic and financial
systems [69]–[74].
Formalization. The core of our model is a differential equa-
tion that describes the evolution of the stablecoin’s state,
S(t), over time. For the purpose of this model, S(t) can be
represented by a key indicator of its health and scale, such as
market capitalization. The state’s rate of change is governed by
influences from the Upstream (UP(t)), Downstream (DN(t)),
and its own internal dynamics:

The core of our model is a differential equation describing
the evolution of the stablecoin’s intrinsic state, S(t), over time.
For the purpose of this model, S(t) can be represented by
a key indicator of its health and scale, such as its market
capitalization or deviation from peg. The state’s rate of change
is governed by influences from Upstream risk factors (UP(t)),
Downstream ecosystem composition (DN(t)), and its own
internal dynamics and resilience mechanisms:

dS(t)
dt

= α · UP(t)
(cid:123)(cid:122)
(cid:125)
(cid:124)
External shocks

+ β · DN(t)
(cid:125)

(cid:123)(cid:122)
Ecosystem feedback

(cid:124)

+ f (S(t), params)
(cid:125)
(cid:123)(cid:122)
Internal dynamics

(cid:124)

(6)

where α and β are gain coefficients for upstream and down-
stream inputs, respectively. Our framework then focuses on
quantifying the UP(t) and DN(t) components based on empir-
ical data.

1) Upstream Risk Factors: The upstream component,
UP(t), quantifies the aggregate external risks facing a stable-
coin. We define the sources of these risks, termed Impact Ob-
jects, based on common causes of security incidents (detailed
in Section IV). To measure the severity of each object, we
assign it an Impact Degree, a composite score derived from
three facets: exposure index (accessibility of the vulnerable
component), impact nature (direct/indirect effect), and loss
form (e.g., fund loss vs. control loss), as specified in Table II.
These degrees function as risk weights. The total upstream
risk is the weighted sum of all impact objects:

UP(t) =

n
(cid:88)

k=1

wk · mk(t)

(7)

where for each impact object k, mk(t) is its quantified metric
(e.g., price deviation, audit status) and wk is the scalar weight
derived from its Impact Degree. Specific metrics and their
weighting rationale are in Table III.

2) Downstream Ecosystem Composition: The downstream
component, DN(t), captures the concentration and composi-
tion of a stablecoin’s holders and integrated protocols. This
determines the potential “blast radius” of a failure and the
pathways for contagion: it is critical to understanding how
the stablecoin “LEGO brick” interlocks with the broader DeFi
structure. A stablecoin’s distress can trigger chain reactions,
and identifying key dependencies is vital. Our analysis focuses
on the top 1000 addresses for each of the 11 stablecoins by
market capitalization (see Fig. 9 for the evaluated subset).
These typically represent over 75% of the total token supply
(while some over 99%). We identify and categorize these hold-
ers (e.g., centralized exchanges, DeFi protocols) using services

Fig. 8: An overview of the Stablecoin LEGO. The left-
hand side represents the upstream while the right-hand side
represents the downstream.

tracking of on-chain and off-chain events but concentrates
on financial market dynamics, giving less weight to the un-
derlying technical security and specific design choices of the
protocols.

While these initial frameworks provide a valuable starting
point, they generally do not offer a sufficiently granular or
compositional approach to risk. To fill this gap, we introduce
the Stablecoin LEGO framework, designed for systematic,
holistic, and compositional risk evaluation. The name is in-
tentional: complex stablecoins are rarely monolithic. Instead,
they are composed of interoperable building blocks (the “LE-
GOs”), such as collateral management systems, price oracles,
governance modules, and redemption mechanisms. Our frame-
work mirrors this reality. It provides a methodology to first
deconstruct a stablecoin into its fundamental components (the
internal LEGOs), then evaluate each “block” for its specific
technical risks and economic assumptions, and finally assess
the systemic risks that emerge from their internal composition
and external interactions.

B. Methodology

Our Stablecoin LEGO framework models a stablecoin as a
dynamic system of three interacting core elements, allowing
us to analyze how risks propagate through its ecosystem, as
illustrated in Fig. 8. These elements are:

• Upstream Risk Factors (UP(t)): External market forces
impose risks upon a
and security threat vectors that
stablecoin (e.g., market volatility, smart contract exploits).
• Stablecoin Intrinsic State (S(t)): The internal design
choices and active mechanisms that determine a stable-
coin’s inherent resilience and dynamic response to shocks
(e.g., collateralization ratio, governance responsiveness).
• Downstream Ecosystem Composition (DN(t)): The net-
work of applications, services, and holder concentrations
that build upon or rely on the stablecoin, creating path-
ways for feedback loops.

These components interact non-linearly, with feedback
loops playing a crucial role (e.g., a major downstream event
could trigger a crisis of confidence, impacting the stablecoin’s
intrinsic state and altering upstream market perception). To
capture these complex dynamics, we formalize our frame-
work using a System Dynamics Model, an approach widely

Peripheral factorRugpullAccess controlImpacted fundDeFi protocolDEX AMMLendingStablecoinYield farmingPrice fluctuationMarket volatilityPrice manipulationCode vulnerabilityFlash loan attackSmart contract issueGovernance attackCollateral assetStabilization mechanismBlockchainBridgeBlockchain infrastructure Whale/retailAsset managementExchangeImpact degree

Explanation

Exposure index

Impact nature

Loss form

Exposure concerning basic blockchain, ecosystem, and trading rules.
Exposure concerning the protocol designs of specific applications, yet are publicly accessible,
e.g., from blockchain data, documentation, audit reports, and open-sourced code.
Exposure concerning secret information accessible only within a limited range, e.g., private keys.

Impact that can indirectly affect the stablecoin.
Impact that can directly affect the stablecoin.
Impact that can hybrid affect the stablecoin, i.e., directly and indirectly.

The loss is calculated in the form of the number of tokens.
The loss is calculated in the form of the price drop.
The loss is calculated as a consequence of the loss of control of the stablecoin protocol.

Notation

e1

e2

e3

i1
i2
i3

l1
l2
l3

TABLE II: The definitions of the impact degrees of the upstream risk factors, divided into 3 aspects, each demonstrating 3
levels of impact severity.

Quantification metrics

Impact degree

Impact object

Price fluctuation

Market volatility
Price manipulation

Price standard deviation in the past 5 years
Regular security auditing

Smart contract issue

Code vulnerability
Flash loan attack
Governance attack

Regular security auditing
Regular security auditing
Regular security auditing and token decentralization

Peripheral factor

Rug pull
Access control
Impacted fund

Regular security auditing and attestation report
Regular security auditing
Regular attestation report

(e1, i3, l2)
(e2, i3, l2)

(e2, i1, l3)
(e2, i1, l3)
(e2, i1, l3)

(e3, i1, l3)
(e3, i1, l3)
(e2, i1, l1)

TABLE III: The quantification metrics of the upstream for the impacted objects, performing in a weighted manner.

USDT
USDC
DAI
USDS
FDUSD
USDe
PYUSD
USDD
FRAX
TUSD
USDB

0

20

40

60

80

100

Exchange
Blockchain infrastructure

Asset management
Whale/retail

DeFi protocol

Fig. 9: The token distributions of the 11 stablecoins regarding
identity and ownership.

from Etherscan and BlockSec MetaSuite. The downstream
impact is thus represented by a vector of token shares held
by each category:

DN(t) = TokenShare(t)

(8)

C. Result

The application of our Stablecoin LEGO framework yields
the quantitative risk profiles (initial evaluation on 11 sta-
blecoins, Table IV). The upstream U P (t) score quantifies
inherent protocol and market risks (higher is riskier), while
the downstream DN (t) distribution reveals concentration,
indicating the nature of systemic risk. This section presents

our key findings by deconstructing these results through illus-
trative case studies and pattern analysis, demonstrating how
the framework provides a granular, data-driven view of the
stablecoin risk landscape.

1) Finding 1: Risk Is Not Monolithic: Our analysis reveals
that stablecoins fall into distinct risk archetypes defined by
their downstream composition. The LEGO framework’s value
lies in its ability to differentiate these risk profiles, as illus-
trated by the following cases.
Case Study 1: The DeFi-centric archetype (USDD). USDD
scores a moderately high Upstream risk of 13.25 but, more
critically, has a 98.1% downstream concentration in DeFi pro-
tocols. This profile is structurally reminiscent of past failures
like Terra UST. While its stabilization mechanism differs, its
near-total reliance on host DeFi ecosystems creates enormous
contagion risk. The framework flags this clearly: a vulnerabil-
ity in its stabilization logic (reflected in its Upstream score)
would hardly be contained. Its impact would be massively
amplified, threatening a cascading failure of the liquidity pools
and lending platforms that treat it as a foundational “LEGO
brick.” The framework thus identifies a critical concern: an
extreme dependency on the health and security of a few third-
party DeFi protocols.
Case Study 2: The exchange-centric archetype (FDUSD).
FDUSD presents a different risk profile. Its Upstream score of
12.89 is comparable to USDD’s, but its 96.7% concentration
on CEXs shifts the primary threat to custodial and counterparty
risk. The framework’s downstream analysis highlights that for
an FDUSD holder, the security of the stablecoin is less about
its on-chain mechanism and more about the solvency, security
practices, and regulatory standing of a single corporate entity

Stablecoin

Price
fluctuation

Smart contract
issue

Peripheral
factor

Total

Exchange

Asset
management

UP(t)

USDT
USDC
DAI
USDS
FDUSD
USDe
PYUSD
USDD
FRAX
TUSD
USDB

2.1583
2.1583
1.9833
0.0001
2.0417
1.5167
4.1583
2.1000
1.4583
2.2167
2.3347

3.7000
3.7000
3.4000
0.0000
3.5000
2.6000
3.7000
3.6000
2.5000
3.8000
4.0000

5.7101
5.6553
5.4750
2.5000
5.4803
4.3366
5.6553
5.6500
4.6875
3.3250
6.0000

12.7117
12.6570
11.7492
3.0940
12.8872
9.7278
14.8439
13.2500
9.3755
11.2278
14.1825

53.2682
14.6538
2.0564
0.0417
96.7493
8.4785
17.6987
1.2696
0.0165
3.9264
0.0000

4.4057
5.5597
3.3415
0.4356
0.0558
0.5660
9.9289
0.0054
0.2029
0.1905
0.0000

DN(t)
DeFi
protocol

0.6603
3.5957
25.0256
70.8696
0.0207
82.1671
1.3587
98.0634
53.1922
0.7820
12.0578

Blockchain
infrastructure

Whale/retail

6.6690
3.9556
6.3893
0.0000
0.0169
0.0634
0.1112
0.1439
14.8037
0.2251
0.0394

13.7521
47.6325
47.7420
28.6523
3.1495
8.7129
70.7349
0.5097
31.7717
94.2145
82.5321

TABLE IV: The evaluation results of 11 stablecoins under the Stablecoin LEGO framework.

(e.g., Binance). This recalls historical failures like exchange
collapses, where users’ assets were frozen or lost. Our frame-
work makes this abstract risk concrete and quantifiable.
Case Study 3: The whale-dominated archetype (TUSD).
TUSD, with an Upstream risk of 11.23 and a 94.2% concen-
tration in private whale wallets, exemplifies a third archetype.
The primary risk here is the centralization of power and market
stability. The framework reveals that the asset’s fate rests in the
hands of a few large, anonymous holders. This composition
makes it structurally vulnerable to a “bank run” scenario,
where a few entities exiting could collapse market confidence.
This insight goes beyond analyzing the protocol’s code to
assessing the real-world distribution of power over the asset.
2) Finding 2: Common Ecosystem-Wide Weaknesses: Our
analysis also reveals that the Peripheral factor (as defined in
Table III) is the principal driver of quantifiable risk across
almost all stablecoins. Specifically, this category typically ac-
counts for 40-50% of the total UP(t) risk for major stablecoins
like USDT (44.9%), USDC (44.7%), and DAI (46.6%), ex-
tending to 80.8% for USDS (with TUSD as the main exception
where “Smart Contract Issue” leads). This empirical finding
signifies a potential systemic misalignment between perceived
risk focal points (often core contract logic) and the primary
sources of measured upstream vulnerability. The persistently
high contribution indicates a critical gap in the efficacy or
scope of current industry safeguards for these foundational
operational and counterparty threats. This strongly suggests
a need for re-prioritizing risk management efforts and audit
focuses within the stablecoin ecosystem.

3) Discussion and Implications: The findings from our
framework have direct implications for key stakeholders in
the ecosystem.
For developers and security auditors: The results advocate
for a shift in focus from purely internal code security to a more
holistic, compositional risk analysis. For a DeFi-centric coin
like USDD, security audits must extend to the host protocols
it depends on. For all protocols, the high scores in “Peripheral
factors” signal an urgent need to bolster defenses around
oracles and governance, which are the very “connective tissue”
between LEGO bricks.
For investors and users: The LEGO framework transforms

the abstract notion of “risk” into a tangible choice between
different risk models. An investor can now consciously select
their exposure: the systemic contagion risk of DeFi-centric
assets,
the corporate counterparty risk of exchange-centric
coins, or the market manipulation risk of whale-dominated
tokens. Our framework argues there is no safest stablecoin in
absolute terms, only one whose risk profile best aligns with
an individual’s tolerance.
For Regulators: The framework provides a data-driven tool
for identifying and monitoring sources of systemic risk. The
quantifiable downstream concentration metrics (e.g., FDUSD’s
96.7% exchange concentration) can help pinpoint entities that
are “too big to fail” within the crypto ecosystem, enabling
more targeted oversight.

4) Limitations and Future Work: We acknowledge certain
limitations. The risk weights in our model are based on an
analysis of historical incidents; a formal sensitivity analysis
testing the framework’s robustness to different weightings
would be a valuable next step to further strengthen our
findings. Additionally, our model does not currently incor-
porate qualitative factors like a protocol’s age or reputation
(the “Lindy Effect”), which could be an avenue for future
research. We advocate for such evaluations to be an enduring
commitment for stablecoin integrity. To this end, we will
continue to advance the Stablecoin LEGO framework and
periodically update its results, contributing to the secure and
sustainable growth of the ecosystem.

VI. CONCLUSION

This SoK facilitates the understanding of stablecoins by
analyzing 157 research studies, 95 active stablecoins, and 44
major security incidents. We establish that stability is not an in-
herent property but a fragile equilibrium governed by risk spe-
cialization, i.e., design trade-offs that concentrate unmitigated
risks. This tension is now systemically exacerbated by a “dual
mandate” for both stability and high-risk yield. To assess these
dynamics, we introduce the Stablecoin LEGO framework, a
quantitative methodology for risk evaluation. Ultimately, this
work provides a rigorous foundation for building, analyzing,
and regulating stablecoins.

REFERENCES

[1] A. Briola, D. Vidal-Tomás, Y. Wang, and T. Aste, “Anatomy of a
stablecoin’s failure: The terra-luna case,” Finance Research Letters,
2023.

[2] S. Werner, D. Perez, L. Gudgeon, A. Klages-Mundt, D. Harz, and
W. Knottenbelt, “Sok: Decentralized finance (defi),” in Proceedings of
the 4th ACM Conference on Advances in Financial Technologies, ser.
AFT ’22. Association for Computing Machinery, 2023.

[3] J. Xu, K. Paruch, S. Cousaert, and Y. Feng, “Sok: Decentralized
exchanges (dex) with automated market maker (amm) protocols,” ACM
Comput. Surv., 2023.

[4] S. Cousaert, J. Xu, and T. Matsui, “Sok: Yield aggregators in defi,”
in 2022 IEEE International Conference on Blockchain and Cryptocur-
rency (ICBC), 2022.

[5] A. Kiayias and P. Lazos, “Sok: Blockchain governance,” in Proceedings
of the 4th ACM Conference on Advances in Financial Technologies, ser.
AFT ’22. Association for Computing Machinery, 2023.

[6] L. Zhou, X. Xiong, J. Ernstberger, S. Chaliasos, Z. Wang, Y. Wang,
K. Qin, R. Wattenhofer, D. Song, and A. Gervais, “Sok: Decentralized
finance (defi) attacks,” in 2023 IEEE Symposium on Security and
Privacy (SP), 2023.

[7] K. Ito, M. Mita, S. Ohsawa, and H. Tanaka, “What is stablecoin?: A
survey on its mechanism and potential as decentralized payment sys-
tems,” International Journal of Service and Knowledge Management,
2020.

[8] A. Klages-Mundt, D. Harz, L. Gudgeon, J.-Y. Liu, and A. Minca,
“Stablecoins 2.0: Economic foundations and risk-based models,” in
Proceedings of the 2nd ACM Conference on Advances in Financial
Technologies, ser. AFT ’20. Association for Computing Machinery,
2020.

[9] A. Klages-Mundt and A. Minca, “(In)Stability for the Blockchain:
Deleveraging Spirals and Stablecoin Attacks,” Cryptoeconomic Sys-
tems, 2021.

[10] Y. Potter, K. Pongmala, K. Qin, A. Klages-Mundt, P. Jovanovic,
C. Parlour, A. Gervais, and D. Song, “What drives the (in)stability of
a stablecoin?” in 2024 IEEE International Conference on Blockchain
and Cryptocurrency (ICBC), 2024.

[11] J. Niu, “Academic blockchain conference papers,” 2024, online at:

https://github.com/jianyu-niu/blockchain\_conference\_paper.

[12] F. S. Board, “Review of the fsb high-level recommendations of the reg-
ulation, supervision and oversight of “global stablecoin” arrangements
- consultative report,” 2022, online at: https://www.fsb.org/uploads/
P111022-4.pdf.

[13] ——, “High-level recommendations for the regulation, supervision and
oversight of global stablecoin arrangements - final report,” 2023, online
at: https://www.fsb.org/uploads/P170723-3.pdf.

[14] F. A. T. Force, “Fatf report to g20 on so-called stablecoins,” 2020,
at: https://www.fatf-gafi.org/content/fatf-gafi/en/publications/

online
Virtualassets/Report-g20-so-called-stablecoins-june-2020.html.

[15] Group of Seven,

International Monetary Fund, and Bank for
impact of global
https://www.tresor.economie.

International Settlements,
stablecoins,”
gouv.fr/Articles/5f8c26f2-a2cd-4685-ba82-fa9e4d4e5d67/files/
d10fb97f-a9a6-472b-842a-8b279e8863c4.

“Investigating the

online

2019,

at:

Bundesbank,

[16] D.
at:
ad932e0cc62044f541770fa9905beb6a/mL/2022-annual-report-data.
pdf.

online
https://www.bundesbank.de/resource/blob/905558/

“Annual

2022,”

report

2022,

[17] F. S. Board, “Regulatory issues of stablecoins,” 2019, online at: https:

//www.fsb.org/uploads/P181019.pdf.

[18] Financial Services and the Treasury Bureau and Hong Kong Mone-
tary Authority, “Consultation conclusions for legislative proposal to
implement regulatory regime for stablecoin issuers in hong kong,”
2024, online at: https://www.fstb.gov.hk/fsb/en/publication/consult/doc/
Stablecoin\_consultation\_conclusion\_e.pdf.

[19] F. S. Board, “G20 crypto-asset policy implementation roadmap - status

report,” 2024, online at: https://www.fsb.org/uploads/P221024-3.pdf.

“Breaking

[20] Deloitte,
ing
com/lu/en/Industries/investment-management/blogs/
breaking-down-barriers-with-new-building-blocks.html.

barriers
at:

blocks,”

online

2024,

down

with

new

build-
https://www.deloitte.

[22] EY-Parthenon, “How tokenization in asset management

is driving
meaningful opportunity,” 2023, online at: https://www.ey.com/en\_us/
insights/financial-services/tokenization-in-asset-management.

[23] KPMG, “Tokenization in financial services: Delivering value and trans-
formation,” 2024, online at: https://www.pwc.com/us/en/tech-effect/
emerging-tech/tokenization-in-financial-services.html.

[24] F. Templeton, “Franklin onchain u.s. government money fund,”
https://www.franklintempleton.com/investments/

2024,
options/money-market-funds/products/29386/SINGLCLASS/
franklin-on-chain-u-s-government-money-fund.

online

at:

launches
[25] BlackRock,
buidl,
ethereum network,”
on
https://securitize.io/learn/press/blackrock-launches-first-tokenized-
fund-buidl-on-the-ethereum-network.

“Blackrock
the

tokenized

online

2024,

first

its

fund,
at:

[26] B. of Russia, “Tokenised deposits,” 2023, online at: https://www.cbr.

ru/content/document/file/156453/review\_token\_e.pdf.

[27] WBTC, “Do more with your bitcoin,” 2024, online at: https://wbtc.

network/.

[28] Coinbase, “What is wrapped crypto?” 2024, online at: https://www.
coinbase.com/zh-cn/learn/your-crypto/what-is-wrapped-crypto.
[29] B. Academy, “What are wrapped tokens?” 2021, online at: https://

academy.binance.com/en/articles/what-are-wrapped-tokens.

[30] G. Caldarelli, “Wrapping trust for interoperability: A preliminary study

of wrapped tokens,” Information, 2022.

[31] O. Docs, “Using the standard bridge,” 2024, online at: https://docs.

optimism.io/builders/app-developers/bridging/standard-bridge.

[32] CoinMarketCap,
online

“Liquidity
at:

tokens),”
tokens
https://coinmarketcap.com/academy/glossary/

provider

(lp

2024,
liquidity-provider-tokens-lp-tokens.

[33] B. Academy,

“What
at:

are

liquidity

tokens?”
https://academy.binance.com/en/articles/

pool

(lp)

2022,
what-are-liquidity-pool-lp-tokens.

online

[34] K. Gogol, Y. Velner, B. Kraner, and C. Tessone, “Sok: Liquid staking
tokens (lsts),” 2024. [Online]. Available: https://arxiv.org/abs/2404.
00644

[35] S. Scharnowski and H. Jahanshahloo, “The economics of liquid staking
derivatives: Basis determinants and price discovery,” Available at SSRN
4180341, 2024.

[36] Lido, “What is steth?” 2024, online at: https://help.lido.fi/en/articles/

5230610-what-is-steth.

[37] DefiLlama, “Stablecoins market cap,” 2024, online at: https://defillama.

com/stablecoins.

[38] CoinMarketCap, “Today’s cryptocurrency prices by market cap,” 2024,

online at: https://coinmarketcap.com/.

[39] CoinGecko, “Stablecoins by market capitalization,” 2024, online at:

https://www.coingecko.com/en/categories/stablecoins.

[40] K. Qin, L. Zhou, P. Gamito, P. Jovanovic, and A. Gervais, “An
empirical study of defi liquidations: incentives, risks, and instabilities,”
in Proceedings of the 21st ACM Internet Measurement Conference, ser.
IMC ’21. Association for Computing Machinery, 2021.

[41] D. Perez, S. M. Werner, J. Xu, and B. Livshits, “Liquidations: Defi on
a knife-edge,” in Financial Cryptography and Data Security. Springer
Berlin Heidelberg, 2021.

[42] K. Qin, J. Ernstberger, L. Zhou, P. Jovanovic, and A. Gervais, “Miti-
gating decentralized finance liquidations with reversible call options,”
in Financial Cryptography and Data Security.
Springer Nature
Switzerland, 2024.

[43] L. Clewlow and S. Hodges, “Optimal delta-hedging under transactions

costs,” Journal of Economic Dynamics and Control, 1997.

[44] F. Black and M. Scholes, “The pricing of options and corporate

liabilities,” Journal of Political Economy, 1973.

[45] B. Phalcon, “Security incidents,” 2024, online at: https://app.blocksec.

com/explorer/security-incidents.

[46] De.Fi, “Top crypto hacks - rekt database,” 2024, online at: https://de.

fi/rekt-database.

[47] SlowMist, “Slowmist hacked,” 2024, online at: https://hacked.slowmist.

io/.

[48] ChainLight, “Illuminating the shadows of web3 hacks,” 2024, online

at: https://lumos.chainlight.io/.

[49] N. Mutual, “Defi and cryptocurrency hacks,” 2024, online at: https:

//neptunemutual.com/hack-database/.

[21] KPMG, “Digital assets - tokenisation,” 2023, online at: https://kpmg.
com/ie/en/home/insights/2023/05/digital-assets-tokenisation.html.

[50] R. Ahmed, I. Aldasoro, and C. Duley, “Par for the course: Public
information and stable coin runs,” Available at SSRN 4554248, 2023.

[51] ——, Public information and stablecoin runs. Bank for International

[78] R. K. Lyons and G. Viswanath-Natraj, “What keeps stablecoins stable?”

Settlements, Monetary and Economic Department, 2024.

Journal of International Money and Finance, 2023.

[52] K. Anadu, P. Azar, M. Cipriani, T. M. Eisenbach, C. Huang, M. Lan-
doni, G. La Spada, M. Macchiavelli, A. Malfroy-Camine, and J. C.
Wang, “Runs and flights to safety: Are stablecoins the new money
market funds?” FRB of Boston Supervisory Research & Analysis Unit
Working Paper No. SRA, pp. 23–02, 2023.

[53] B. Eichengreen, M. T Nguyen, and G. Viswanath-Natraj, “Stablecoin
devaluation risk,” WBS Finance Group Research Paper, 2023.
[54] J. Liu, I. Makarov, and A. Schoar, “Anatomy of a run: The terra luna
crash,” National Bureau of Economic Research, Tech. Rep., 2023.
[55] H. Uhlig, “A luna-tic stablecoin crash,” National Bureau of Economic

Research, Tech. Rep., 2022.

[56] G. Kurovskiy and N. Rostova, “How algorithmic stablecoins fail,”

Technical Report, SNB BNS, Tech. Rep., 2023.

[57] F. Calandra, F. P. Rossi, F. Fabris, M. Bernardo et al., “Making
algorithmic stablecoins more stable: The terra-luna case study,” 2024,
online at: https://hdl.handle.net/11368/3076358.

[58] Binance, “Markets overview,” 2024, online at: https://www.binance.

com/en/markets/overview.

[59] C. Foundation, “Link the world,” 2024, online at: https://chain.link/.
[60] U. Labs, “Swap anytime, anywhere.” 2024, online at: https://app.

uniswap.org/.

[61] K. Qin, L. Zhou, B. Livshits, and A. Gervais, “Attacking the defi
ecosystem with flash loans for fun and profit,” in Financial Cryptog-
raphy and Data Security. Springer Berlin Heidelberg, 2021.

[62] Q. Xia, Z. Huang, W. Dou, Y. Zhang, F. Zhang, G. Liang, and C. Zuo,
“Detecting flash loan based attacks in ethereum,” in 2023 IEEE 43rd
International Conference on Distributed Computing Systems (ICDCS),
2023.

[63] Y. Liu, Q. Lu, L. Zhu, H.-Y. Paik, and M. Staples, “A systematic
literature review on blockchain governance,” Journal of Systems and
Software, 2023.

[64] Z. Lin, J. Chen, J. Wu, W. Zhang, Y. Wang, and Z. Zheng, “Crpwarner:
Warning the risk of contract-related rug pull in defi smart contracts,”
IEEE Transactions on Software Engineering, 2024.

[65] F. Cernera, M. L. Morgia, A. Mei, and F. Sassi, “Token spammers,
rug pulls, and sniper bots: An analysis of the ecosystem of tokens in
ethereum and in the binance smart chain (BNB),” in 32nd USENIX
Security Symposium (USENIX Security 23). USENIX Association,
2023.

[66] R. Sandhu and P. Samarati, “Access control: principle and practice,”

IEEE Communications Magazine, 1994.

[67] Bluechip, “Evaluating stablecoin safety: The smidge framework,”
https://assets.ctfassets.net/0x04pt0ewi4n/

2022,
6gAVu3Hfubtr00Dbn1xnfe/e40990c30b18e41a40f642f270a2907a/
Bluechip\_Framework.pdf.

online

at:

[68] Moody’s, “Digital asset monitor,” 2023, online at: https://www.moodys.

com/web/en/us/innovation/digital-asset-monitor.html.

[69] I. J. Martinez-Moyano and G. P. Richardson, “Best practices in system

dynamics modeling,” System Dynamics Review, 2013.

[70] M. J. Radzicki, “System dynamics and its contribution to economics
and economic modeling,” System dynamics: Theory and applications,
pp. 401–415, 2020.

[71] T. Nguyen, S. Cook, and V. Ireland, “Application of system dynamics
to evaluate the social and economic benefits of infrastructure projects,”
Systems, 2017.

[72] M. Passarella, “A simplified stock-flow consistent dynamic model of
the systemic financial fragility in the ‘new capitalism’,” Journal of
Economic Behavior & Organization, 2012.

[73] K. D. John, “Linking economic modeling and system dynamics: A
basic model for monetary policy and macroprudential regulation,” in
30th International Conference of the System Dynamics Society, July,
2012, pp. 22–26.

[74] P. M. Senge, “A system dynamics approach to investment-function

formulation and testing,” Socio-Economic Planning Sciences, 1980.

[75] Y. Cao, M. Dai, S. Kou, L. Li, and C. Yang, “Designing stablecoins,”

SSRN, 2024.

[76] C. T. Ba, R. G. Clegg, B. A. Steer, and M. Zignani, “Investigating
in the ethereum stablecoin ecosystem through
[Online]. Available:

shocking events
temporal multilayer graph structure,” 2024.
https://arxiv.org/abs/2407.10614

[77] K. Duan and A. Urquhart, “The instability of stablecoins,” Finance

Research Letters, 2023.

[79] I. Fiedler and L. Ante, “Stablecoins,” in The emerald handbook
Emerald

on cryptoassets: investment opportunities and challenges.
Publishing Limited, 2023, pp. 93–105.

[80] L. Ante, I. Fiedler, J. M. Willruth, and F. Steinmetz, “A systematic
literature review of empirical research on stablecoins,” FinTech, 2023.
[81] Y. Ma, Y. Zeng, and A. L. Zhang, “Stablecoin runs and the centraliza-

tion of arbitrage,” Available at SSRN 4398546, 2023.

[82] Y. Guan, Y. Yu, T. Sharma, K. Qin, Y. Wang, and Y. Wang, “Examining
user perceptions of stablecoins: Understandings and risks,” in Posters
at the Symposium on Usable Privacy and Security (SOUPS), 2023.

[83] B. Mizrach, “Stablecoins: Survivorship,

transactions costs and
exchange microstructure,” 2023. [Online]. Available: https://arxiv.org/
abs/2201.01392

[84] B. Ł˛et, K. Soba´nski, W. ´Swider, and K. Włosik, “What drives the
popularity of stablecoins? measuring the frequency dynamics of con-
nectedness between volatile and stable cryptocurrencies,” Technological
Forecasting and Social Change, 2023.

[85] A. Kosse, M. Glowka, I. Mattei, and T. Rice, “Will the real stablecoin

please stand up?” BIS Papers, 2023.

[86] C. Bertsch, Stablecoins: Adoption and fragility.

Sveriges Riksbank,

2023.

[87] C. Catalini, A. de Gortari, and N. Shah, “Some simple economics of
stablecoins,” Annual Review of Financial Economics, vol. 14, no. 1,
pp. 117–135, 2022.

[88] Y. Li and S. Mayer, “Money creation in decentralized finance: A
dynamic model of stablecoin and crypto shadow banking,” Fisher
College of Business Working Paper, no. 2020-03, p. 030, 2022.
[89] B. N. Thanh, T. N. V. Hong, H. Pham, T. N. Cong, and T. P. T. Anh,
“Are the stabilities of stablecoins connected?” Journal of Industrial
and Business Economics, vol. 50, no. 3, pp. 515–525, 2023.

[90] A. Klages-Mundt and A. Minca, “While stability lasts: A stochastic
model of noncustodial stablecoins,” Mathematical Finance, vol. 32,
no. 4, pp. 943–981, 2022.

[91] L. W. Cong, Y. Li, and N. Wang, “Token-based platform finance,”

Journal of Financial Economics, 2022.

[92] A. d’Avernas, V. Maurin, and Q. Vandeweyer, “Can stablecoins be sta-
ble?” University of Chicago, Becker Friedman Institute for Economics
Working Paper, no. 2022-131, 2022.

[93] M. M. Bojaj, M. Muhadinovic, A. Bracanovic, A. Mihailovic,
M. Radulovic, I. Jolicic, I. Milosevic, and V. Milacic, “Forecasting
macroeconomic effects of stablecoin adoption: A bayesian approach,”
Economic Modelling, 2022.

[94] J. Morgan, “Systemic stablecoin and the defensive case for central bank
digital currency: A critique of the bank of england’s framing,” Research
in International Business and Finance, 2022.

[95] G. B. Gorton, E. C. Klee, C. P. Ross, S. Y. Ross, and A. P. Vardoulakis,
“Leverage and stablecoin pegs,” National Bureau of Economic Re-
search, Tech. Rep., 2022.

[96] G. Baughman, F. Carapella, J. Gerszten, and D. Mills, “The stable in
stablecoins,” Board of Governors of the Federal Reserve System, Tech.
Rep., 2022.

[97] G. Y. Liao and J. Caramichael, “Stablecoins: Growth potential and
impact on banking,” Board of Governors of the Federal Reserve
System, Tech. Rep., 2022.

[98] P. Bains, A. Ismail, F. Melo, and N. Sugimoto, Regulating the crypto
International

ecosystem: the case of stablecoins and arrangements.
Monetary Fund, 2022.

[99] W. Bolt, V. Lubbersen, and P. Wierts, “Getting the balance right:
Crypto, stablecoin and cbdc,” De Nederlandsche Bank Working Paper,
2022.

[100] L. Ante, I. Fiedler, and E. Strehle, “The influence of stablecoin
issuances on cryptocurrency markets,” Finance Research Letters, 2021.
[101] D. G. Baur and L. T. Hoang, “A crypto safe haven against bitcoin,”

Finance Research Letters, 2021.

[102] L. T. Hoang and D. G. Baur, “How stable are stablecoins?” The

European Journal of Finance, 2024.

[103] L. Ante, I. Fiedler, and E. Strehle, “The impact of transparent money
flows: Effects of stablecoin transfers on the returns and trading volume
of bitcoin,” Technological Forecasting and Social Change, 2021.
[104] K. Jarno and H. Kołodziejczyk, “Does the design of stablecoins impact

their volatility?” Journal of Risk and Financial Management, 2021.

[105] C. Catalini and A. de Gortari, “On the economic design of stablecoins,”

[130] R.

B.

of

India,

Available at SSRN 3899499, 2021.

[106] C. Li and Y. Shen, “The potential impacts and risks of global stable-

coins,” China Economic Journal, 2021.

[107] I. G. A. Pernice, “On stablecoin price processes and arbitrage,” in
Financial Cryptography and Data Security. FC 2021 International
Workshops: CoDecFin, DeFi, VOTING, and WTSC, Virtual Event,
March 5, 2021, Revised Selected Papers 25. Springer, 2021, pp. 124–
135.

[108] W. Zhao, H. Li, and Y. Yuan, “Understand volatility of algorithmic
stablecoin: Modeling, verification and empirical analysis,” in Financial
Cryptography and Data Security. FC 2021 International Workshops.
Springer Berlin Heidelberg, 2021.

[109] Y. Potter, J. Kim, Y. Kim, and D. Song, “The trilemma of stablecoin,”

Available at SSRN 3917430, 2021.

[110] A. Moin, K. Sekniqi, and E. G. Sirer, “Sok: A classification framework
for stablecoin designs,” in Financial Cryptography and Data Security.
Springer International Publishing, 2020.

[111] J. Cheng, “How to build a stablecoin: certainty, finality, and stability
through commercial law principles,” Berkeley Bus. LJ, 2020.
[112] C. Jeger, B. Rodrigues, E. Scheid, and B. Stiller, “Analysis of
stablecoins during the global covid-19 pandemic,” in 2020 Second
International Conference on Blockchain Computing and Applications
(BCCA), 2020.

[113] A. Lipton, A. Sardon, F. Schär, and C. Schüpbach, “From tether to
libra: Stablecoins, digital currency and the future of money,” 2020.
[Online]. Available: https://arxiv.org/abs/2005.12949

[114] A. Lipton, A. Sardon, F. Schär, and C. Schüpbach, “11. stablecoins,
digital currency, and the future of money,” Building the New Economy,
vol. 30, 2020.

[115] G.-J. Wang, X. yu Ma, and H. yu Wu, “Are stablecoins truly diver-
sifiers, hedges, or safe havens against traditional cryptocurrencies as
their name suggests?” Research in International Business and Finance,
2020.

[116] M. Bellia and S. Schich, “What makes private stablecoins stable?”

Available at SSRN 3718954, 2020.

[117] F. van Echelpoel, M. T. Chimienti, M. Adachi, P. Athanassiou, I. Bal-
teanu, T. Barkias, I. Ganoulis, D. Kedan, H. Neuhaus, A. Pawlikowski
et al., “Stablecoins: Implications for monetary policy, financial stability,
market infrastructure and payments, and banking supervision in the
euro area,” ECB Occasional Paper, Tech. Rep., 2020.

[118] J. Frost, H. S. Shin, and P. Wierts, “An early stablecoin? the bank
of amsterdam and the governance of money,” De Nederlandsche Bank
Working Paper, 2020.

[119] D. W. Arner, R. Auer, and J. Frost, “Stablecoins: risks, potential and

regulation,” 2020.

[120] M. Mita, K. Ito, S. Ohsawa, and H. Tanaka, “What is stablecoin?: A
survey on price stabilization mechanisms for decentralized payment
systems,” in 2019 8th International Congress on Advanced Applied
Informatics (IIAI-AAI), 2019, pp. 60–66.

[121] E. L. Sidorenko, “Stablecoin as a new financial instrument,” in Digital
Springer International Pub-

Age: Chances, Challenges and Future.
lishing, 2020.

[122] A. Berentsen and F. Schär, “Stablecoins: The quest for a low-volatility
cryptocurrency,” The economics of Fintech and digital currencies, pp.
65–75, 2019.

[123] A. Moin, E. G. Sirer, and K. Sekniqi, “A classification framework
for stablecoin designs,” 2019. [Online]. Available: https://arxiv.org/
abs/1910.10098

[124] B. Eichengreen, “From commodity to fiat and now to crypto: what
does history tell us?” National Bureau of Economic Research, Tech.
Rep., 2019.

[125] D. Bullmann, J. Klemm, and A. Pinna, “In search for stability in crypto-
assets: are stablecoins the solution?” Available at SSRN 3444847, 2019.
[126] B. of Governors of the Federal Reserve System, “Financial stability
report, november 2024,” 2024, online at: https://www.federalreserve.
gov/publications/files/financial-stability-report-20241122.pdf.
2024,”

2024,
https://www.federalreserve.gov/publications/files/

[127] ——,
online
financial-stability-report-20240419.pdf.

“Financial
at:

stability

report,

april

[128] B. de France, “What are crypto-assets and stablecoins?” 2024, online
at: https://www.banque-france.fr/en/aide-faq/Payment\%20instruments.
[129] B. of Russia, “Stablecoins: regulators’ attitude to them around the
globe,” 2024, online at: https://www.cbr.ru/eng/press/event/?id=18828.

“Decentralised
2024,

finance:
online

Implica-
https:

for

system,”

financial

tions
//website.rbi.org.in/web/rbi/-/publications/rbi-bulletin/
decentralised-finance-implications-for-financial-system-23232.
[131] H. K. M. Authority, “Regulatory regime for stablecoin issuers
in hong kong,” 2024, online at: https://www.hkma.gov.hk/eng/
data-publications-and-research/publications/quarterly-bulletin/2024/
09/.

at:

[132] B. of Korea, “Payment and settlement systems report 2023,” 2024,
online at: https://www.bok.or.kr/eng/bbs/E0000866/view.do?menuNo=
400223\&nttId=10086690.
“Chile:
Fund,

[133] I. M.

Selected

issues,”

online

2024,

at:

https://www.imf.org/en/Publications/CR/Issues/2024/02/06/
Chile-Selected-Issues-544442.

[134] B. of Governors of the Federal Reserve System, “Financial stability
report october 2023,” 2023, online at: https://www.federalreserve.gov/
publications/files/financial-stability-report-20231020.pdf.
stability

2023,
https://www.federalreserve.gov/publications/files/

[135] ——,
online
financial-stability-report-20230508.pdf.

“Financial
at:

report,

2023,”

may

[136] B. of England, “Regulatory regime for systemic payment systems
using stablecoins and related service providers,” 2023, online at:
https://www.bankofengland.co.uk/paper/2023/dp/regulatory-regime-
for-systemic-payment-systems-using-stablecoins-and-related-service-
providers.
de
real

[137] B.
the
banque-france.fr/en/publications-and-statistics/publications/
stablecoins-and-financing-real-economy.

of
https://www.

“Stablecoins
2023,

and
online

economy,”

financing

France,

the

at:

[138] D. Bundesbank, “Monthly report – april 2023,” 2023, online at:

https://www.bundesbank.de/en/publications/reports/monthly-reports/
monthly-report-april-2023-744244.

[139] B. of Canada, “Financial system review—2023,” 2023, online at: https:
//www.bankofcanada.ca/2023/05/financial-system-review-2023/.

[140] B. C. do Brasil, “Financial

stability report,” 2023, online at:

https://www.bcb.gov.br/content/publications/financialstabilityreport/
202304/fsrFullRep.pdf.

[141] S. A. R. Bank,

online
https://www.resbank.co.za/content/dam/sarb/what-we-do/

at:
financial-stability/A\%20Primer\%20on\%20Stablecoins.pdf.

stablecoins,”

“A primer

2023,

on

[142] H. K. M. Authority, “Conclusion of discussion paper on crypto-assets
and stablecoins,” Hong Kong Monetary Authority, Tech. Rep., 2023.
and
report
https://www.bok.or.kr/cdnFileSrc/eng/

2022,”
d8d8296302324465a1730aea88a919b9/1/filedown.pdf.

of Korea,
2023,

“Payment
at:

settlement

[143] B.

systems

online

[144] R. B. of Australia, “Payments system board annual report – 2023,”
2023, online at: https://www.rba.gov.au/publications/annual-reports/
psb/2023/pdf/psb-annual-report-2023.pdf.

[145] B. for International Settlements, “Bis annual economic report 2023,”

2023, online at: https://www.bis.org/publ/arpdf/ar2023e.pdf.

[146] H. K. M. A. Bank for International Settlements, “Project dynamo:
Catalysing innovation for sme growth,” 2023, online at: https://www.
bis.org/publ/othp68.pdf.

[147] B. for International Settlements, “The crypto ecosystem: key elements
and risks,” 2023, online at: https://www.bis.org/publ/othp72.pdf.
[148] F. S. Board, “The financial stability implications of multifunction
intermediaries,” 2023, online at: https://www.fsb.org/

crypto-asset
uploads/P281123.pdf.

[149] I. M. F. Financial Stability Board, “Imf-fsb synthesis paper: Poli-
cies for crypto-assets,” 2023, online at: https://www.fsb.org/uploads/
R070923-1.pdf.

[150] F. S. Board, “The financial stability risks of decentralised finance,”

2023, online at: https://www.fsb.org/uploads/P160223.pdf.

[151] B. of Governors of

the Federal Reserve System, “Money and
payments: The u.s. dollar
transforma-
tion,” 2022, online at: https://www.federalreserve.gov/publications/
files/financial-stability-report-20240419.pdf.

in the age of digital

report,

“Financial
at:

[152] ——,
online
financial-stability-report-20221104.pdf.
report

[153] ——,
online
financial-stability-report-20220509.pdf.

“Financial
at:

stability
2022,
https://www.federalreserve.gov/publications/files/

november

2022,”

stability
2022,
https://www.federalreserve.gov/publications/files/

- may

2022,”

[154] M. Adachi, P. B. P. Da Silva, A. Born, M. Cappuccio, S. Czák-Ludwig,
I. Gschossmann, A. Pellicani, M. Plooij, G. Paula, and S.-M. Philipps,
“Stablecoins’ role in crypto and beyond: functions, risks and policy,”
Macroprudential Bulletin, vol. 18, 2022.

[155] B. of Canada, “Financial system review—2022,” 2022, online at: https:
//www.bankofcanada.ca/2022/06/financial-system-review-2022/.

[156] B. C. do Brasil, “Financial

stability report,” 2022, online at:

https://www.bcb.gov.br/content/publications/financialstabilityreport/
202211/fsrFullRep.pdf.

[178] ——,

“Monthly

report

–

april

2021,”

2021,

online

at:

https://www.bundesbank.de/en/publications/reports/monthly-reports/
monthly-report-april-2021-864102.

[179] B. of Canada, “Financial system review—2021,” 2021, online at: https:
//www.bankofcanada.ca/2021/05/financial-system-review-2021/.
[180] T. I. F. W. Group, “Ifwg car working group position paper on
https://www.resbank.co.za/en/

crypto
home/publications/publication-detail-pages/media-releases/2021/
IFWG-CAR-Working-Group-position-paper-on-crypto-assets.

assets,”

online

2021,

at:

[157] B. of Russia, “Tokenised deposits,” 2022, online at: https://www.cbr.

[181] B.

ru/collection/collection/file/43513/en\_2q\_3q\_2022.pdf.
“Global

banking

India,

of

[158] R. B.

2022,
https://website.rbi.org.in/web/rbi/-/publications/

developments,”

online
global-banking-developments-21576.

at:

[159] B.

of Korea,
online

“Financial
at:

stability

2022),”
https://www.bok.or.kr/cdnFileSrc/eng/

report

(june

2022,
ad2da7c8401aa9466909e63d0e24eda3/1/filedown.pdf.

[160] B. Indonesia, “Project garuda: Navigating the architecture of digital
rupiah,” 2022, online at: https://www.bi.go.id/en/rupiah/digital-rupiah/
Documents/White-Paper-CBDC-2022\_en.pdf.

[161] R. B. of Australia, “Stablecoins: Market developments, risks and reg-
ulation,” 2022, online at: https://www.rba.gov.au/publications/bulletin/
2022/dec/stablecoins-market-developments-risks-and-regulation.html.
stability
2022,
https://www.rba.gov.au/publications/fsr/2022/apr/

[162] ——,
online
global-financial-environment.html.

“Financial
at:

review –

2022,”

april

[163] ——, “Payments system board annual report – 2022,” 2022, on-
line at: https://www.rba.gov.au/publications/annual-reports/psb/2022/
payments-system-regulation-and-policy-issues.html.
stability
2022,
october
https://www.rba.gov.au/publications/fsr/2022/oct/

[164] ——,
online
box-a-financial-stability-risks-from-crypto-assets.html.

“Financial
at:

review –

2022,”

[165] M. Adachi, P. B. P. Da Silva, A. Born, M. Cappuccio, S. Czák-Ludwig,
I. Gschossmann, A. Pellicani, M. Plooij, G. Paula, and S.-M. Philipps,
“Stablecoins’ role in crypto and beyond: functions, risks and policy,”
Macroprudential Bulletin, 2022.

[166] A. Born and J. M. V. Simón, “A deep dive into crypto financial risks:
stablecoins, defi and climate transition risk,” Macroprudential Bulletin,
2022.

[167] E. C. Bank, “The international role of the euro,” 2022, online at: https:

//www.ecb.europa.eu/pub/pdf/ire/ecb.ire202206~6f3ddeab26.en.pdf.

[168] I. M. Fund,

“United

kingdom: Financial
and

sector

stability
and market

program-financial
technology,
https://www.imf.org/en/Publications/CR/Issues/2022/04/07/United-
Kingdom-Financial-Sector-Assessment-Program-Financial-Stability-
and-Managing-516279.

managing
2022,

transitions,”

assessment
institutional,
at:
online

[169] ——, “Review of the method of valuation of the sdr,” 2022, on-
line at: https://www.imf.org/en/Publications/Policy-Papers/Issues/2022/
05/16/Review-of-the-Method-of-Valuation-of-the-SDR-517967.
[170] B. for International Settlements, “Prudential treatment of cryptoasset

exposures,” 2022, online at: https://www.bis.org/bcbs/publ/d545.pdf.

[171] ——, “Bis annual economic report 2022,” 2022, online at: https://www.

bis.org/publ/arpdf/ar2022e.pdf.

[172] F. S. Board, “Regulation, supervision and oversight of crypto-asset
activities and markets - consultative document,” 2022, online at: https:
//www.fsb.org/uploads/P111022-3.pdf.

de México,
online

2021,
at:
publicaciones-y-prensa/reportes-sobre-el-sistema-financiero/\%
7B18265301-01FF-CE2A-F381-19BB9DCB1E4B\%7D.pdf.

“Reporte

de

estabilidad

financiera,”
https://www.banxico.org.mx/

[182] R. B. of Australia, “Financial

stability review – april 2021,”
https://www.rba.gov.au/publications/fsr/2021/apr/

online

2021,
regulatory-developments.html.

at:

[183] ——, “Payments system board annual report – 2021,” 2021, on-
line at: https://www.rba.gov.au/publications/annual-reports/psb/2021/
retail-payments-regulation-and-policy-issues.html.
2021,
stability
https://www.rba.gov.au/publications/fsr/2021/oct/

“Financial
[184] ——,
online
at:
regulatory-developments.html.

review –

october

2021,”

for
Fund,

International

International Mon-
[185] Bank
digital
etary
currencies
at:
https://www.imf.org/en/Publications/Policy-Papers/Issues/2021/07/09/
Central-bank-digital-currencies-for-cross-border-payments-461850.

Settlements,
Bank,
payments,”

and World
cross-border

“Central

online

2021,

bank

for

assets

and virtual

[186] F. A. T. Force, “Updated guidance for a risk-based approach
service providers,” 2021,
at: https://www.fatf-gafi.org/content/fatf-gafi/en/publications/

to virtual
online
Fatfrecommendations/Guidance-rba-virtual-assets-2021.html.
[187] R. B. of Australia, “Financial stability review – october 2020,”
2020, online at: https://www.rba.gov.au/publications/fsr/2020/oct/pdf/
04-regulatory-developments.pdf.

asset

[188] ——, “Bulletin – september 2020,” 2020, online at: https://www.rba.
gov.au/publications/bulletin/2020/sep/pdf/bulletin-2020-09.pdf.

[189] Bank for

International Settlements and World Bank, “Payment
inclusion in the fintech era,” 2020, online at:

aspects of financial
https://documents1.worldbank.org/curated/en/230091592918282222/
pdf/Payment-Aspects-of-Financial-Inclusion-in-the-Fintech-Era.pdf.

[190] F. S. Board, “Regulation, supervision and oversight of “global sta-
blecoin” arrangements - final report and high-level recommendations,”
2020, online at: https://www.fsb.org/uploads/P131020-3.pdf.

[191] ——, “Addressing the regulatory, supervisory and oversight challenges
raised by “global stablecoin” arrangements - consultative document,”
2020, online at: https://www.fsb.org/uploads/P140420-1.pdf.

[192] F. A. T. Force, “12 month review of

assets

virtual

-
fatf-gafi.org/content/fatf-gafi/en/publications/Fatfrecommendations/
12-month-review-virtual-assets-vasps.html.

vasps,”

online

2020,

and

revised fatf
at:

standards
https://www.

[193] B. of Governors of the Federal Reserve System, “Financial stability
report, november 2019,” 2019, online at: https://www.federalreserve.
gov/publications/files/financial-stability-report-20191115.pdf.
2019,

[194] D.
at:
27ee3319784c2cf0ff6c880926869b36/mL/2019-annual-report-data.
pdf.

online
https://www.bundesbank.de/resource/blob/826458/

Bundesbank,

“Annual

2019,”

report

[173] ——, “Assessment of risks to financial stability from crypto-assets,”

[195] ——,

“Monthly

report

-

july

2019,”

2019,

online

at:

2022, online at: https://www.fsb.org/uploads/P160222.pdf.

[174] B. of Governors of the Federal Reserve System, “Financial stability
report,” 2021, online at: https://www.federalreserve.gov/publications/
files/financial-stability-report-20211108.pdf.

[175] B. of England, “Regulatory regime for systemic payment sys-
tems using stablecoins and related service providers,” 2021, online
at: https://www.bankofengland.co.uk/paper/2021/new-forms-of-digital-
money.

[176] D. Bundesbank, “Monthly report - september 2021,” 2021, online at:

https://www.bundesbank.de/en/publications/reports/monthly-reports/
monthly-report-september-2021-875896.

[177] ——,

“Monthly

report

–

july

2021,”

2021,

online

at:

https://www.bundesbank.de/en/publications/reports/monthly-reports/
monthly-report-july-2021-869518.

https://www.bundesbank.de/en/publications/reports/monthly-reports/
monthly-report-july-2019-802236.

[196] R. B. of Australia,

“Cryptocurrency: Ten years on,” 2019,
https://www.rba.gov.au/publications/bulletin/2019/jun/

online
cryptocurrency-ten-years-on.html.

at:

“Financial
[197] ——,
online
at:
regulatory-developments.html.

stability
2019,
https://www.rba.gov.au/publications/fsr/2019/oct/

review –

october

2019,”

[198] ——, “Payments system board annual report - 2019,” 2019, on-
line at: https://www.rba.gov.au/publications/annual-reports/psb/2019/
pdf/2019-psb-annual-report.pdf.

[199] E. C. Bank, “Stablecoins – no coins, but are they stable?” 2019,
online at: https://www.ecb.europa.eu/press/intro/publications/pdf/ecb.
mipinfocus191128.en.pdf.

[200] G. Kaur, “Stablecoins 101: What are crypto stablecoins, and how do
they work?” 2024, online at: https://cointelegraph.com/learn/articles/
stablecoins-101-what-are-crypto-stablecoins-and-how-do-they-work.

“From digital

IDA,
regulated

[201] Q.
of
2024,
from-digital-currency-to-legal-tender/.

stablecoins

online

at:

currency to legal
driving

role
in
payments,”
real-world
https://www.quinlanandassociates.com/

tender: The

[202] Visa, “Visa onchain analytics dashboard,” 2024, online at: https:

//visaonchainanalytics.com/.

[203] X. Soares and R. Glenn, “What is a stablecoin? a beginner’s guide,”

2024, online at: https://beincrypto.com/learn/what-is-a-stablecoin/.

[204] S. Chartered and Z. Markets, “Stablecoins: The first ‘killer app’,”
2024, online at: https://www.sc.com/en/corporate-investment-banking/
stablecoins/.
[205] A. Hertig, “What

is a stablecoin?” 2024, online at: https://www.

coindesk.com/learn/what-is-a-stablecoin.

[206] Castle Island Ventures, Brevan Howard Digital, and Visa Crypto,
“Stablecoins:the emerging market story,” 2024, online at: https://
castleisland.vc/writing/stablecoins-the-emerging-market-story/.

[207] Chainalysis,

“The 2024 geography of

crypto report,” 2024,
online at: https://www.chainalysis.com/wp-content/uploads/2024/10/
the-2024-geography-of-crypto-report-release.pdf.
report,”

crypto

spring

online

2024,

2024

“The

at:

[208] ——,

https://go.chainalysis.com/rs/503-FAP-074/images/The\%20Crypto\
%20Spring\%20Report.pdf.

[209] CCData, “Stablecoins & cbdcs report,” 2024, online at: https://ccdata.

io/reports/stablecoins-cbdcs-report-february-2024.

[210] S. Standard, “Stablecoin standard announces operational, transparency,
stablecoins globally,” 2024, online
https://www.stablecoinstandard.com/news/stablecoin-standard-

and product
at:
announces-operational-transparency-and-product-standards-for-
stablecoins-globa.

standards

for

[211] PwC and S. D. Foundation, “Enhancing the social handprint of financial
service providers: Using blockchain to foster financial
inclusion,”
2023, online at: https://www.pwc.com/us/en/services/digital-assets/
blockchain-financial-inclusion.html.

“Pwc

[212] PwC,
online
global-crypto-regulation-report-2023.html.

2023,
https://www.pwc.com/gx/en/about/new-ventures/

regulation

2023,”

crypto

global

report

at:

[213] Decrypt, “What are stablecoins and how do you use them?” 2023,

online at: https://decrypt.co/resources/stablecoins.

[214] PwC,

“Pwc
global
2022,” 2022, online
global-cbdc-index-and-stablecoin-overview-2022.html.

cbdc
overview
at: https://www.pwc.com/sg/en/publications/

stablecoin

index

and

[215] KPMG and A. Digital,

online
at:
investing-in-digital-assets.html.

“Investing in digital

assets,” 2022,
https://kpmg.com/cn/en/home/insights/2022/10/

[216] Stellar and Wirex, “The future of money: Cryptocurrency adop-
tion in 2021,” 2021, online at: https://wirexapp.com/blog/post/
2021-the-year-of-crypto-0250.

[217] C. I. Ventures, “Crypto dollars: The story so far,” 2020, online at:
https://castleisland.vc/writing/crypto-dollars-the-story-so-far/.
[218] Semrush, “Traffic analytics,” 2024, online at: https://www.semrush.

com/analytics/traffic/.

Media

URL

CoinTelegraph
CoinDesk
BeInCrypto
Cryptonews
Decrypt
CoinGape
Crypto News
Bitcoin.com News
The Crypto Basic
U.Today
The Block
Bitcoinist
CryptoSlate
CryptoPotato
Blockworks
BlockBeats
Bitcoin Magazine
NewsBTC
Foresight News
Crypto Daily

https://cointelegraph.com/
https://www.coindesk.com/
https://beincrypto.com/
https://cryptonews.com/
https://decrypt.co/
https://coingape.com/
https://crypto.news/
https://news.bitcoin.com/
https://thecryptobasic.com/
https://u.today/
https://www.theblock.co/
https://bitcoinist.com/
https://cryptoslate.com/
https://cryptopotato.com/
https://blockworks.co/
https://www.theblockbeats.info/
https://bitcoinmagazine.com/
https://www.newsbtc.com/
https://foresightnews.pro/
https://cryptodaily.co.uk/

Visits

235.6M
232.4M
124.0M
64.3M
62.0M
46.1M
42.7M
41.2M
39.0M
35.5M
29.1M
23.5M
20.4M
18.3M
17.3M
13.8M
13.2M
12.9M
12.6M
11.3M

TABLE V: The visits count of Web3 medias.

No.

Country/
Organization

Department

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

11

12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27

Canada
USA
UK
France
Germany
Italy
Japan
Brazil
Russia
India

China

Bank of Canada
The Federal Reserve
Bank of England
Banque de France
Deutsche Bundesbank
Banca d’Italia
Bank of Japan
Banco Central do Brasil
Bank of Russia
Reserve Bank of India
People’s Bank of China,
Hong Kong Monetary Authority
South African Reserve Bank
Banco de México
Central Bank of Argentina
Türkiye Cumhuriyet Merkez Bankası
Bank of Korea
Bank Indonesia
Reserve Bank of Australia
Saudi Central Bank
European Central Bank
∗∗

South Africa
Mexico
Argentina
Türkiye
South Korea
Indonesia
Australia
Saudi Arabia
European Union
African Union
International Monetary Fund (IMF)
World Bank (WB)
Bank for International Settlements (BIS)
Financial Stability Board (FSB)
Financial Action Task Force (FATF)
Group of Seven (G7)

APPENDIX

Total

#

3
9
2
2
6
0
0
2
3
2

4

2
1
∗
0
3
1
13
0
5
∗∗
6
2
8
10
3
1
81

A. Stablecoin Definition

1) Prior Research Dataset: The stablecoin definitions are
from academic papers (Table VII), governmental reports (Ta-
ble VIII, IX), and industry reports (Table X).

2) Top Web3 Media: The top Web3 media list, shown in
Table V, is determined by the total visits in the recent 2 years
(December 2022 - November 2024), according to Semrush
Traffic Analytics [218].

B. Existing Stablecoins

The list of 95 active stablecoins with a market capitalization

exceeding $10M (May 2025) is shown in Table XI, XII.

TABLE VI: The numbers of the stablecoin-related reports from
G20 members and relevant international financial organiza-
tions since 2019. ∗ No English version for the websites and
publication. ∗∗ The central bank related institutions have not
yet established. Note that the sum exceeds 81 due to several
inter-institution cooperation works.

C. Security Incidents

The dataset of stablecoin security incidents with losses

exceeding $100K are detailed in Table XIII.

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
11

12
13
14

15
16
17

18
19
20
21

22

23
24
25
26
27

28
29

30

31

32

33

34
35
36
37
38
39
40

41
42
43

44
45

46

47
48
49
50
51
52
53
54
55
56

No.

Research source

Year

Blockchain

Pegged asset

Stability

2024
2024
2024
2023
2023

Unspecified
Public blockchain
Unspecified
Unspecified
Unspecified

Unspecified
Stable financial assets
Unspecified
Fiat currencies or assets that are relatively stable
National currency

Minimize price fluctuations
Pegged
Pegging
Maintain a peg
Lower volatility

Yujin Potter et al. (ICBC) [10]
Yizhou Cao et al. (SSRN) [75]
Cheick Tidiane Ba et al. (arXiv) [76]
Kun Duan et al. (Finance Res. Lett.) [77]
Richard K. Lyons et al.
nance) [78]
Ingo Fiedler et al. (Emerald) [79]

(J.

Int. Money Fi-

2023

Unspecified

Lennart Ante et al. (FinTech) [80]

2023

Unspecified

(Technol. Forecast. Soc.

Yiming Ma et al. (SSRN) [81]
Yongqi Guan et al. (SOUPS Poster) [82]
Bruce Mizrach (arXiv) [83]
Blanka Ł˛et et al.
Change) [84]
Anneke Kosse et al. (BIS) [85]
Christoph Bertsch (Riksbank) [86]
Christian Catalini et al.
Econ.) [87]
Ye Li et al. (SSRN) [88]
Binh Nguyen Thanh et al. (J. Ind. Bus. Econ.) [89]
Ariah Klages-Mundt et al. (Math. Financ.) [90]

(Annu. Rev. Financ.

Lin William Cong et al. (JFE) [91]
Adrien d’Avernas et al. (SSRN) [92]
Martin M. Bojaj et al. (Econ. Model.) [93]
Jamie Morgan (RIBAF) [94]

2023
2023
2023
2023

2023
2023
2022

2022
2022
2022

2022
2022
2022
2022

Blockchain
Unspecified
Distributed ledger
Distributed ledger

Unspecified
Unspecified
Unspecified

Unspecified
Unspecified
Unspecified

Unspecified
Unspecified
Blockchain
Unspecified

Gary B. Gorton et al. (NBER) [95]

2022

Unspecified

Harald Uhlig (NBER) [55]
Garth Baughman et al. (Fed) [96]
Gordon Y. Liao et al. (Fed) [97]
Parma Bains et al. (IMF) [98]
Wilko Bolt et al. (DNB) [99]

Lennart Ante et al. (Finance Res. Lett.) [100]
Dirk G. Baur et al. (Finance Res. Lett.) [101]

2022
2022
2022
2022
2022

2021
2021

Unspecified
Unspecified
Distributed ledger
Unspecified
Unspecified

Unspecified
Unspecified

Lai T. Hoang et al. (Eur. J. Finance) [102]

2021

Unspecified

Lennart Ante et al. (TFSC) [103]

2021

Public blockchain

Ariah Klages-Mundt et al. (CES) [9]

2021

Public blockchain

Fiat currencies like the dollar or physical assets
like gold
Other assets, most often the U.S. dollar but also
other fiat currencies or physical assets, such as
gold
$1 (fiat)
A specific asset
Fiat assets and other stores of value
An underlying asset, e.g., the US dollar, precious
metals
A specified peg
Unspecified
A reference asset (typically the US dollar)

Pegged

Peg their value

Stable
Anchored (fixed value)
Maintain price stability
Pegged

Maintain a stable value
Stable
Trade at par

Fiat currency
Another asset
Unspecified

Unspecified
An official currency
Various currencies and commodities
A reference asset (typically a fiat currency such as
the US$)
Fiat currency

Unspecified
Real-world asset
An external reference, typically the U.S. dollar
Specified asset(s)
Fiat currency(ies), commodity(ies), cryptoasset(s),
or a combination
Less volatile assets or currencies
Other (relatively) stable assets such as gold or the
US dollar
Currencies or assets that are (relatively) stable
such as the US dollar
Non-volatile values, most commonly a fiat cur-
rency
Unspecified

price/purchasing

Maintain a stable price
Have stable value
Stabilize
power
Unspecified
Maintain a peg
One-to-one peg
Stabilised

Maintain a constant dollar
price
Unspecified
Maintain its peg
Peg their value
Maintain a stable value
Maintain a stable value

Pegged
Pegged

Pegged

Peg

the

Stabilize
power
Minimize fluctuations

purchasing

Financial

et

al.

Jarno

(J. Risk

Klaudia
Manag.) [104]
Christian Catalini et al. (SSRN) [105]
Cangshu Li et al. (CEJ) [106]
Ingolf G. A. Pernice (FC Workshop) [107]
Wenqi Zhao et al. (FC Workshop) [108]
Yujin Kwon et al. (SSRN) [109]
Amani Moin et al. (FC) [110]
Ariah Klages-Mundt et al. (AFT) [8]

Jess Cheng (BBLJ) [111]
Makiko Mita et al. (IJSKM) [7]
Clemens Jeger et al. (BCCA) [112]

Alexander Lipton et al. (arXiv) [113]
Alexander Lipton et al. (Building the New Econ-
omy) [114]
Gang-Jin Wang et al. (RIBAF) [115]

Mario Bellia et al. (SSRN) [116]
Fiona van Echelpoel et al. (ECB) [117]
Jon Frost et al. (DNB) [118]
Douglas W. Arner et al. (BIS) [119]
Makiko Mita et al. (IIAI-AAI) [120]
E. L. Sidorenko (ISCDTE) [121]
Aleksander Berentsen et al. (VoxEU.org) [122]
Amani Moin et al. (arXiv) [123]
Barry Eichengreen (NBER) [124]
Dirk Bullmann et al. (ECB) [125]

2021

Unspecified

Unspecified

2021
2021
2021
2021
2021
2020
2020

2020
2020
2020

2020
2020

Unspecified
Public blockchain
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified

Distributed ledger
Unspecified
Unspecified

Unspecified
Unspecified

2020

Unspecified

2020
2020
2020
2020
2019
2019
2019
2019
2019
2019

Unspecified
Unspecified
Unspecified
Unspecified
Blockchain
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified

A reference asset, typically the U.S. Dollar
Legal tender or other assets
Unspecified
External assets
Unspecified
Some reference point, such as USD
Unspecified

A reference asset or basket of assets
Stable assets or major fiat currencies
Fiat currencies, gold or even another cryptocur-
rency
A target quote currency
A target quote currency

A fiat currency (e.g., USD and CNY) or a com-
modity (e.g., precious metals such as gold and
silver)
Unspecified
Currency(ies)
Assets or fiat currencies
Fiat currencies or other assets
Another currency
Underlying asset (national currency, gold, oil, etc.)
Unspecified
Some reference point
Official numeraire
Unspecified

Maintain stability
Relatively stable price
Close to the price
Minimize the volatility
Provide a stable value
Stable
Stabilize
power
Stabilize the price
Peg
Maintain a stable value

price&purchasing

Low price volatility
Low price volatility

Low-volatility

Unspecified
Minimise fluctuations
Maintain a stable value
Tied
Lower volatility
Low volatility
Minimise price volatility
Stable
Maintain a peg
Minimise fluctuations

TABLE VII: Stablecoin definitions from academic papers. Note that all descriptions in the last three columns are directly
quoted from the original text, except for the “Unspecified”s.

No.

Research source

Year

Blockchain

Pegged asset

The Federal Reserve [126]
The Federal Reserve [127]
Banque de France [128]

2024
2024
2024

Unspecified
Unspecified
Cryptographic tech.

Bank of Russia [129]

2024

Unspecified

Reserve Bank of India [130]
Hong Kong Monetary Authority [131]
Financial Services and the Treasury Bureau,
and Hong Kong Monetary Authority [18]

Bank of Korea [132]
International Monetary Fund [133]
The Federal Reserve [134]
The Federal Reserve [135]
Bank of England [136]
Banque de France [137]
Deutsche Bundesbank [138]

Bank of Canada [139]
Bank of Russia [26]

Banco Central do Brasil [140]
South African Reserve Bank [141]
Hong Kong Monetary Authority [142]
Bank of Korea [143]
Reserve Bank of Australia [144]

Bank for International Settlements [145]
Bank for International Settlements and Hong
Kong Monetary Authority [146]
Bank for International Settlements [147]
Financial Stability Board [148]
Financial Stability Board and International
Monetary Fund [149]
Financial Stability Board [13]
Financial Stability Board [150]
The Federal Reserve [151]
The Federal Reserve [152]
The Federal Reserve [153]
European Central Bank [154]
Bank of Canada [155]

2024
2024
2024

2024
2024
2023
2023
2023
2023
2023

2023
2023

2023
2023
2023
2023
2023

2023
2023

2023
2023
2023

2023
2023
2022
2022
2022
2022
2022

ledger

Unspecified
Blockchain
Decentralised
distributed
or similar tech.
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified
Public blockchain
Unspecified

Unspecified
Unspecified

Unspecified
Unspecified
Unspecified
Unspecified
Unspecified

Unspecified
Unspecified

Blockchain
Unspecified
Unspecified

Unspecified
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified

Banco Central do Brasil [156]

2022

Unspecified

Bank of Russia [157]

2022

Unspecified

Reserve Bank of India [158]

2022

Unspecified

Bank of Korea [159]
Bank Indonesia [160]
Reserve Bank of Australia [161]
Reserve Bank of Australia [162]

2022
2022
2022
2022

Unspecified
Unspecified
Unspecified
Unspecified

Reserve Bank of Australia [163]

2022

Unspecified

Reserve Bank of Australia [164]

2022

Unspecified

European Central Bank [165]

2022

Unspecified

European Central Bank [166]

2022

Unspecified

European Central Bank [167]

2022

Unspecified

International Monetary Fund [168]
International Monetary Fund [169]
Bank for International Settlements [170]
Bank for International Settlements [171]
Financial Stability Board [172]
Financial Stability Board [12]
Financial Stability Board [173]

The Federal Reserve [174]
Bank of England [175]
Deutsche Bundesbank [176]
Deutsche Bundesbank [177]

2022
2022
2022
2022
2022
2022
2022

2021
2021
2021
2021

Unspecified
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified

Distributed ledger
Unspecified
Unspecified
Distributed ledger

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
11
12
13
14

15
16

17
18
19
20
21

22
23

24
25
26

27
28
29
30
31
32
33

34

35

36

37
38
39
40

41

42

43

44

45

46
47
48
49
50
51
52

53
54
55
56

57

National currency or another reference asset
National currency or another reference asset
A benchmark asset (gold, the euro, the dollar, a group
of currencies, etc.)
Fiat currency and other assets (gold, other commodities,
cryptocurrencies, etc.) or a basket thereof
A numeraire like fiat currency or gold
Certain asset(s), typically fiat currencies
Fiat currencies and other types of assets

Stability

Maintain a stable value
Maintain a stable value
More stable value

Pegged

Maintain a fixed face value
Maintain a stable value
Unspecified

Pegged
Maintain a stable value
Maintain a stable value
Maintain a stable value
Maintain a stable value
Stable

Reserve assets, such as a fiat currency or a commodity Maintain a stable value
Specific currencies, such as the U.S. dollar
National currency or another reference asset
National currency or another reference asset
Fiat currency
Fiat currency
Government currencies, asset backing, and crypto to-
kens
Fiat currency
Another asset (fiat currency, precious metals, etc.) or a
basket of various assets
A predefined asset or an asset basket
A specified asset, or a pool or basket of assets
A specified asset, or a pool or basket of assets
Reserve assets, including currencies and commodities
A specified unit of account or store of value, such as a
national currency or commodity
A specified asset, or a pool or basket of assets
A specified asset (typically USD), or a pool or basket
of assets
A specified asset, or a pool or basket of assets
A specified asset, or a pool or basket of assets
A specified asset, or a pool or basket of assets

Peg
Maintain a stable value
Maintain a stable value
Achieve price stability
Maintain a stable value

Maintain a stable value
Maintain a stable value
Maintain a stable value

Maintain a stable value
Maintain a stable value

Unspecified
Maintain a stable value

A specified asset, or a pool or basket of assets
A specified asset, or a pool or basket of assets
One or more assets
National currency or another reference asset
National currency or another reference asset
Official currency(ies) or other assets
National currency in most cases

One or more assets (such as sovereign currencies or
another asset that is not traded in a cryptocurrency
trading environment)
Various assets (fiat currency, precious metals and oth-
ers) or a basket of various assets
A specified asset (typically US dollars), or a pool or
basket of assets
A specific asset (usually a fiat currency)
A commodity or currency
A specified unit of account or store of value
Fiat currencies (particularly the US dollar) or other
assets (such as gold)
One or more fiat currencies or assets (e.g. the US dollar
or gold)
Another asset or a basket of assets – commonly a fiat
currency (e.g. the US dollar) or a common store of
value (e.g. gold)
One or several official currencies or other assets (in-
cluding crypto-assets)
One or several currencies or other assets (including
crypto-assets)
Typically a single fiat currency (or a basket of fiat
currencies)
Usually a fiat currency
A stable reference asset
A specified asset, or a pool or basket of assets
A specified asset, or a pool or basket of assets
A specified asset, or a pool or basket of assets
A specified asset, or a pool or basket of assets
A specified asset (typically US dollars), or basket of
assets
National currency or other reference asset or assets
Government-sponsored or ‘fiat’ currencies
A reference value
A reference value

Maintain a stable value
Maintain a stable value
Peg
Maintain a stable value
Maintain a stable value
Maintain a stable value
Less volatile than other cryp-
toassets
Linked

Maintain a stable value

Maintain a stable value

Stabilize the value
Relatively stable
Maintain a stable value
Maintain a stable value

Maintain a stable value

Minimise price volatility

Maintain a stable value

Maintain a stable value

Minimise price volatility

Maintain stable value
Pegged
Maintain a stable value
Maintain a stable value
Maintain a stable value
Maintain a stable value
Maintain a stable value

Maintain a stable value
Peg
Stabilised
Be as stable in value as pos-
sible
Minimise major fluctuations

Deutsche Bundesbank [178]

2021

Distributed ledger

Another unit of value

TABLE VIII: Stablecoin definitions from governmental institution reports, including government agencies and international
organizations. Note that all descriptions in the last three columns are directly quoted from the original text, except for the
“Unspecified”s.

No.

Research source

Year

Blockchain

Pegged asset

58
59

60
61
62
63
64

65
66

67

68

69
70
71
72
73
74
75
76

77

78

79

80

81

Bank of Canada [179]
South African Reserve Bank [180]

Banco de México [181]
Reserve Bank of Australia [182]
Reserve Bank of Australia [183]
Reserve Bank of Australia [184]
Bank for International Settlements, Interna-
tional Monetary Fund, and World Bank [185]
Financial Action Task Force [186]
Reserve Bank of Australia [187]

2021
2021

2021
2021
2021
2021
2021

2021
2020

Unspecified
Unspecified

Distributed registry
Unspecified
Unspecified
Unspecified
Unspecified

Unspecified
Unspecified

Reserve Bank of Australia [188]

2020

Unspecified

Bank for International Settlements and World
Bank [189]
Financial Stability Board [190]
Financial Stability Board [191]
Financial Action Task Force [192]
Financial Action Task Force [14]
The Federal Reserve [193]
Deutsche Bundesbank [194]
Deutsche Bundesbank [195]
Reserve Bank of Australia [196]

2020

Unspecified

2020
2020
2020
2020
2019
2019
2019
2019

Unspecified
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified
Unspecified

Reserve Bank of Australia [197]

2019

Unspecified

Reserve Bank of Australia [198]

2019

Unspecified

European Central Bank [199]

2019

Unspecified

Financial Stability Board [17]

2019

Unspecified

Group of Seven,
Fund, and Bank for
ments [15]

International Monetary
International Settle-

2019

Distributed ledger

A basket of assets
Another asset (typically a unit of currency or commod-
ity) or a basket of assets
Unspecified
A specified asset or pool of assets
Unspecified
One or more currencies or assets
A specified asset, or a pool or basket of assets

Some reference asset or assets
Another asset, typically a unit of currency or a com-
modity
A widely used unit of account (such as the US dollar)
or a common store of value (such as gold)
Currency/ies

A specified asset, or a pool or basket of assets
A specified asset, or a pool or basket of assets
Reference assets
Some reference asset or assets
An underlying asset or basket of assets
Unspecified
Often an existing currency (or basket of currencies)
Unit of account (often the US dollar) or a common
store of value (such as gold)
Another asset, typically a unit of currency or a com-
modity
A reference asset (such as a sovereign currency or gold)
or a basket of assets
Currency(ies), securities&commodities, crypto-assets,
and future expectations
Another asset (typically a unit of currency or commod-
ity) or a basket of assets
Fiat currencies

Stability

Less volatile
Maintain a stable value

Minimize fluctuation
Maintain a stable value
Maintain a stable value
Maintain a stable value
Maintain a stable value

Maintain a stable value
Maintain a stable value

Minimise price volatility

Minimise fluctuations

Maintain a stable value
Maintain a stable value
Maintain a stable value
Maintain a stable value
Tied
Maintain a stable value
Have a stable value
Minimise price volatility

Maintain a stable value

Minimise price volatility

Minimise price fluctuations

Maintain a stable value

Achieve stable value

including government agencies and
TABLE IX: (Cont’d) Stablecoin definitions from governmental
international organizations. Note that all descriptions in the last three columns are directly quoted from the original text,
except for the “Unspecified”s.

institution reports,

No.

Research source

Year

Blockchain

Pegged asset

Stability

Cointelegraph [200]
IDA and Quinlan&Associates [201]
Visa [202]
BeInCrypto [203]

2024
2024
2024
2024

Blockchain
Distributed ledger
Blockchain
Unspecified

2024

Unspecified

Fiat currencies
Fiat currency values
Unspecified
Another asset, such as gold, fiat currency, or another
cryptocurrency
A national currency or other reference rate

Offer price stability
Ensure close alignment
Maintain a stable value
Maintain
a
value
Maintain a stable value

set

(near-constant)

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
11
12

13
14
15
16

17
18
19
20

Standard Chartered and Zodia Mar-
kets [204]
CoinDesk [205]
Castle Island Ventures and Brevan
Howard Digital [206]
Chainalysis [207]
Chainalysis [208]
CCData [209]
Stablecoin Standard [210]
PwC and Stellar Development Founda-
tion [211]
PwC [212]
Moody’s [68]
Decrypt [213]
PwC [214]

KPMG and Aspen Digital [215]
Bluechip [67]
Stellar and Wirex [216]
Castle Island Ventures [217]

2024
2024

2024
2024
2024
2024
2023

2023
2023
2023
2022

2022
2022
2021
2020

Unspecified
Public blockchain

Another asset class, such as a fiat currency or gold
Fiat currency

Keep a stable, steady value
Unspecified

Unspecified
Unspecified
Unspecified
Blockchain
Unspecified

Unspecified
Blockchain
Unspecified
Unspecified

Unspecified
Unspecified
Unspecified
Public blockchain

Unspecified
Typically U.S. dollar
Another currency, commodity, or financial instrument
Fiat or e-money
Fiat currencies, commodities or other crypto assets

Unspecified
Pegged
Pegged
Unspecified
Price stability

Unspecified
Fiat currencies
Fiat currency
An asset considered to have a stable value (for instance,
a fiat currency or precious metals)
Unspecified
Unspecified
A stable asset
Sovereign currencies

Unspecified
Pegged
Pegged
Minimise volatility

Unspecified
Unspecified
Mitigate the price volatility
Track the return of sovereign cur-
rencies

TABLE X: Stablecoin definitions from industry reports. Note that all descriptions in the last three columns are directly quoted
from the original text, except for the “Unspecified”s.

No.

Project

Stablecoin

Market
cap

Pegged
asset

Collateral asset

Stabilization mecha-
nism

Tether
Circle
Sky

Ethena Labs

MakerDAO
World Liberty Fi-
nancial
First Digital Labs
Ethena Labs
PayPal
Usual

USDT
USDC
USDS

USDe

DAI
USD1

FDUSD
USDtb
PYUSD
USD0

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

11
12
13
14

Ondo Finance
TrueUSD
Maple Finance
Hashnote

USDY
TUSD
SyrupUSDC
USYC

$580M
$494M
$456M
$390M

$152,797M USD
$61,523M USD
USD
$7,007M

Fiat currency
Fiat currency
Cryptocurrency

Implicit
Implicit
Liquidation
Emergency

and

$5,216M

USD

Cryptocurrency

Hedging

$4,539M
$2,152M

$1,628M
$1,443M
$904M
$635M

USD
USD

USD
USD
USD
USD

USD
USD
USD
USD

Cryptocurrency
Fiat currency

Liquidation
Implicit

Fiat currency
Fiat currency
Fiat currency
Fiat currency

Fiat currency
Fiat currency
Cryptocurrency
Fiat currency

Implicit
Implicit
Implicit
Implicit

Implicit
Implicit
Liquidation
Implicit

15

Falcon Finance

USDf

$384M

USD

Cryptocurrency

16
17

18
19

20

21

22
23
24
25
26
27
28

29

30
31
32
33

34
35
36

37
38
39

40
41

42

43
44
45
46
47
48

49

50
51
52

53
54
55
56

USDD
Stables Labs

Ripple
Global Dollar Net-
work
Resolv Labs

Aave

Blast
M0
Circle
OpenEden
Avalon Labs
Level
Elixir

USDD
USDX

RLUSD
USDG

USR

GHO

USDB
M
EURC
USDO
USDa
lvlUSD
deUSD

$376M
$373M

$310M
$278M

$259M

$250M

$244M
$237M
$235M
$227M
$201M
$184M
$184M

Curve Finance

crvUSD

$168M

A7A5
Stasis
Paxos
Aster

Agora
Anzen
Resupply

Berachain
Inverse Finance
Reservoir

Paxos
Frax Finance

A7A5
EURS
USDL
USDF

AUSD
USDz
reUSD

HONEY
DOLA
rUSD

USDP
frxUSD

Bucket Protocol

BUCK

Avant
Cygnus Finance
Anchored Coins
Binance
Abracadabra
Felix

Lista

Web 3 Dollar
Gemini
Overnight Finance

avUSD
cgUSD
AEUR
BUSD
MIM
feUSD

lisUSD

USD3
GUSD
USD+

Transfero
Mountain Protocol
Banking Circle
Societe Generale

BRZ
USDM
EURI
EURCV

$143M
$140M
$137M
$137M

$126M
$122M
$120M

$88M
$79M
$75M

$72M
$68M

$65M

$62M
$60M
$58M
$57M
$55M
$51M

$50M

$49M
$49M
$48M

$48M
$47M
$47M
$46M

USD
USD

USD
USD

USD

USD

USD
USD
EUR
USD
USD
USD
USD

USD

RUB
EUR
USD
USD

USD
USD
USD

USD
USD
USD

USD
USD

USD

USD
USD
EUR
USD
USD
USD

USD

USD
USD
USD

BRL
USD
EUR
EUR

Liquidation,
hedging, and supply
adjustment
Supply adjustment
Hedging

Cryptocurrency
Cryptocurrency

Fiat currency
Fiat currency

Implicit
Implicit

Cryptocurrency

Hedging

Cryptocurrency

Cryptocurrency
Fiat currency
Fiat currency
Fiat currency
Cryptocurrency
Cryptocurrency
Cryptocurrency

Cryptocurrency

Fiat currency
Fiat currency
Fiat currency
Cryptocurrency

Fiat currency
RWA
Cryptocurrency

Cryptocurrency
Cryptocurrency
Fiat currency, RWA,
and cryptocurrency
Fiat currency
Fiat currency

Cryptocurrency

Cryptocurrency
Fiat currency
Fiat currency
Cryptocurrency
Cryptocurrency
Cryptocurrency

Cryptocurrency

Cryptocurrency
Fiat currency
Cryptocurrency

Fiat currency
Fiat currency
Fiat currency
Fiat currency

Liquidation and sup-
ply adjustment
Implicit
Supply adjustment
Implicit
Implicit
Liquidation
Supply adjustment
Hedging

adjustment

Supply
and emergency
Implicit
Implicit
Implicit
Supply
and hedging
Implicit
Supply adjustment
Supply
and liquidation
Implicit
Supply adjustment
Supply adjustment

adjustment

adjustment

Emergency
Implicit

Liquidation and sup-
ply adjustment
Hedging
Implicit
Implicit
Implicit
Supply adjustment
Liquidation and sup-
ply adjustment
Liquidation and sup-
ply adjustment
Implicit
Implicit
Implicit

Implicit
Implicit
Implicit
Implicit

Yield
rate

N/A
N/A
6.5%

4%

N/A
N/A

N/A
N/A
N/A
10%

4.35%
N/A
10.1%
Not
men-
tioned
9.4%

20%
8.23%

N/A
N/A

8%

4.23%

13.5%
4.32%
N/A
3.9%
5%
10.72%
5.79%

1.1%

8.63%
N/A
3.7%
5.9%

N/A
15.7%
21.77%

N/A
8.75%
8.5%

N/A
7.15%

27.21%

7.99%
4.25%
N/A
N/A
17.68%
16.93%

Yield source

Native protocol revenue, cash and cash
equivalents yield, and external DeFi pro-
tocol yield
L1 staking reward, derivatives-driven
yield, and third-party custodian revenue

Cash and cash equivalents yield, and
secondary token emission
Cash and cash equivalents yield

Native protocol revenue
Cash and cash equivalents yield

Derivatives-driven yield and external
DeFi protocol yield

Community-subsidized fund
Derivatives-driven
community-subsidized fund

yield

and

L1 staking reward and derivatives-driven
yield
Community-subsidized fund

Third-party custodian revenue
Cash and cash equivalents yield

Cash and cash equivalents yield
Native protocol revenue
External DeFi protocol yield
Derivatives-driven yield and third-party
custodian revenue
Native protocol revenue

Cash and cash equivalents yield

Cash and cash equivalents yield
Derivatives-driven yield and secondary
token emission

Third-party custodian revenue
Native protocol revenue and secondary
token emission

Native protocol revenue
Community-subsidized fund

Derivatives-driven yield, external DeFi
protocol yield, and cash and cash equiv-
alents yield
Not mentioned

Derivatives-driven yield
Cash and cash equivalents yield

External DeFi protocol yield
Native protocol revenue

6.86%

Not mentioned

Not mentioned

Native protocol
revenue, derivatives-
driven yield, and external DeFi protocol
yield

Cash and cash equivalents yield

4.4%
N/A
16.21%

N/A
4.5%
N/A
N/A

TABLE XI: The list of active stablecoins with a market capitalization exceeding $10M (as of May 2025).

No.

Project

Stablecoin Market

57

58
59
60
61
62
63
64
65
66
67
68

69
70
71

72
73

74
75

76

77
78
79

80

81
82
83
84
85
86
87

88
89
90
91
92
93
94
95

f(x)

Rings
Liquity
Tether
Celo
Hive
StraitsX
Plume
Liquity
Monerium
MNEE
Angle

Hex Trust
Synthetix
Gyroscope

BiLira
StandX

River
Noon

Angle

Electronic Dollar
GMO Trust
Aegis

Yala

dForce
Solayer
PT Rupiah Token
Alchemix
Frankencoin
GMO Trust
Orby

StablR
Youves
Moneta
WSPN
JUST
StraitsX
defi.money
Anzens

fxUSD

scUSD
LUSD
EURT
CUSD
HBD
XUSD
pUSD
BOLD
EURe
MNEE
USDA

USDX
sUSD
GYD

TRYB
DUSD

satUSD
USN

EURA

EUSD
ZUSD
YUSD

YU

USX
sUSD
IDRT
alUSD
ZCHF
GYEN
USC

EURR
uUSD
USDM
WUSD
USDJ
XSGD
MONEY
USDA

cap

$46M

$42M
$41M
$40M
$35M
$34M
$34M
$29M
$28M
$27M
$26M
$26M

$25M
$24M
$24M

$24M
$23M

$23M
$22M

$22M

$21M
$19M
$18M

$16M

$15M
$15M
$14M
$14M
$13M
$13M
$12M

$11M
$11M
$11M
$11M
$10M
$10M
$10M
$10M

Pegged
asset

Collateral asset

Stabilization mecha-
nism

Cryptocurrency

Emergency

Yield
rate

12.1%

8.2%
N/A
N/A
N/A
20%
N/A
N/A
7.94%
N/A
N/A
5.53%

N/A
N/A
11.56%

N/A
8.46%

20.57%
7.38%

Implicit
Supply adjustment
Implicit
Supply adjustment
Supply adjustment
Implicit
Implicit
Supply adjustment
Implicit
Implicit
Supply adjustment

adjustment

Implicit
Implicit
Supply
and emergency
Implicit
Hedging and emer-
gency
Liquidation
Hedging

Supply adjustment

4.31%

Implicit
Implicit
Hedging and supply
adjustment
Liquidation and sup-
ply adjustment

Emergency
Implicit
Implicit
Implicit
Liquidation
Implicit
Liquidation

Implicit
Liquidation
Implicit
Implicit
Liquidation
Implicit
Liquidation
Implicit

4.3%
N/A
11%

9.43%

8%
3.99%
N/A
N/A
4.175%
N/A
0%

N/A
14%
N/A
N/A
N/A
N/A
26.90%
N/A

Cryptocurrency
Cryptocurrency
Fiat currency
Cryptocurrency
Cryptocurrency
Fiat currency
Cryptocurrency
Cryptocurrency
Fiat currency
Fiat currency
Cryptocurrency

Fiat currency
Cryptocurrency
Cryptocurrency

Fiat currency
Cryptocurrency

Cryptocurrency
Fiat currency and
cryptocurrency
Cryptocurrency

Cryptocurrency
Fiat currency
Cryptocurrency

Cryptocurrency

Cryptocurrency
Fiat currency
Fiat currency
Cryptocurrency
Cryptocurrency
Fiat currency
Cryptocurrency

Fiat currency
Cryptocurrency
Fiat currency
Fiat currency
Cryptocurrency
Fiat currency
Cryptocurrency
Fiat currency

Yield source

L1 staking reward and derivatives-driven
yield
External DeFi protocol yield

Community-subsidized fund

Native protocol revenue

Third-party custodian revenue, native
protocol revenue, and external DeFi pro-
tocol yield

Not mentioned

L1 staking reward and derivatives-driven
yield
protocol fees
Derivatives-driven yield, and cash and
cash equivalents yield
Cash and cash equivalents yield, ex-
ternal DeFi protocol yield, and native
protocol revenue
Not mentioned

Derivatives-driven yield

Native protocol revenue, external DeFi
protocol yield, and cash and cash equiv-
alents yield
Community-subsidized fund
Cash and cash equivalents yield

Community-subsidized fund

Native protocol revenue and secondary
token emission

Secondary token emission

Native protocol revenue

USD

USD
USD
EUR
USD
USD
USD
USD
USD
EUR
USD
USD

USD
USD
USD

TRY
USD

USD
USD

EUR

USD
USD
USD

USD

USD
USD
IDR
USD
CHF
JPY
USD

Euro
USD
USD
USD
USD
SGD
USD
USD

TABLE XII: (Cont’d) The list of active stablecoins with a market capitalization exceeding $10M (as of May 2025).

No.

Project

Stablecoin

Blockchain

Year

Loss

Root cause

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44

Terra
Neutrino
Beanstalk
BonqDAO
Cashio
DEFI100
Mochi
Tether
UwU Lend
Angle Protocol
Deus Finance
Prisma Finance
Defrost Finance
Elephant Money
Yearn Finance
Platypus Finance
Haven Protocol
Origin Protocol
True Seigniorage Dollar
Abracadabra Money
Deus Finance
Seneca
XSURGE
Nirvana
Raft
Deus Finance
Zunami Protocol
Hope Finance
Acala
Minterest
Hubble Protocol
PalmSwap
bDollar
UPFI Network
Anzen Finance
PolBase Cash
SperaxUSD
TheStandard.io
Kujira Network
Safe Dollar
Linear Finance
Iron Finance
Elephant Money
Abracadabra Money

UST
USDN
Bean
BEUR
CASH
D100
USDM
USDT
sUSDe
EURA&USDA
DEI
mkUSD
H2O
TRUNK
yUSDT
USP
xUSD
OUSD
TSD
MIM
DEI
senUSD
xUSD
NIRV
R
DEI
UZD
HOPE
aUSD
mUSDY
USDH
USDP
BDO
UPFI
USDz
PBC
USDs
PAXG
USK
SDO
LUSD
IRON
TRUNK
MIM

Terra
Waves
Ethereum
Polygon
Solana
BSC
Ethereum
Ethereum
Ethereum
Ethereum
Fantom
Ethereum
Avalanche
BSC
Ethereum
Avalanche
Haven
Ethereum
BSC
Ethereum
BSC, Arbitrum
Ethereum, Arbitrum
BSC
Solana
Ethereum
Fantom
Ethereum
Arbitrum
Polkadot
Mantle
Solana
BSC
BSC
BSC
Base
Ethereum
Arbitrum
Arbitrum
Kujira
Polygon
BSC
BSC
BSC
Ethereum

2022
2022
2022
2023
2022
2021
2021
2017
2024
2023
2022
2024
2022
2022
2023
2023
2021
2020
2021
2024
2023
2024
2021
2022
2023
2022
2023
2023
2022
2024
2022
2023
2022
2024
2024
2021
2023
2023
2023
2021
2023
2020
2023
2022

$40B
Market fluctuation
$200M Market fluctuation
$182M Flash loan attack and governance attack
$120M Price manipulation
Code vulnerability
$53M
Rug pull
$32M
Rug pull and governance attack
$30M
Access control
$31M
Price manipulation
$23M
Impacted fund
$18M
Flash loan attack and price manipulation
$13M
Code vulnerability
$12M
Flash loan attack, access control, and price manipulation
$12M
Flash loan attack
$12M
Code vulnerability
$11M
Price manipulation
$8.5M
Code vulnerability
$8.2M
Code vulnerability
$8.0M
Governance attack
$7.1M
Code vulnerability
$6.5M
Code vulnerability
$6.3M
Code vulnerability
$6.0M
Flash loan attack
$5.6M
Flash loan attack
$3.5M
Flash loan attack
$3.3M
Flash loan attack and price manipulation
$3.0M
Flash loan attack and price manipulation
$2.2M
Rug pull
$1.9M
Code vulnerability
$1.6M
Flash loan attack and code vulnerability
$1.5M
Price manipulation
$1.3M
Code vulnerability
$900K
Price manipulation
$730K
Code vulnerability
$521K
Code vulnerability
$500K
Rug pull
$354K
Code vulnerability
$300K
Price manipulation
$290K
Code vulnerability
$260K
Flash loan attack
$248K
Code vulnerability
$212K
Code vulnerability
$170K
Price manipulation
$165K
Price manipulation
$111K

TABLE XIII: Existing security incidents of stablecoins with losses exceeding $100K.

