Abstract

This paper extensively reviews empirical literature on stablecoins, systematically

identifying key variables that could lead to depegging risks. Based on this, we construct

Stablecoin Depegging Risk Prediction

Yu-Fen Chiu
Department of Financial Engineering and Actuarial Mathematics, Soochow
University, Taiwan

Yi-Hsi Lee1
Department of Financial Engineering and Actuarial Mathematics, Soochow
University, Taiwan

Ming-Hua Hsiehc,
Department of Risk Management and Insurance, National Chengchi University,
Taiwan

Preprint not peer reviewed

predictive models using three machine learning algorithms (logistic regression, random

events. Our main subjects of study are the top four stablecoins in daily trading volume:

study is the first to incorporate sentiment indicators from news sources. The empirical

threshold  values,  we  adopt  a  dynamic  threshold  adjusted  for  trading  volume  as  the

indicated  in  the  literature,  significant  price  and  volume  fluctuations  of  mainstream

period covers from January 1, 2022, to December 31, 2023. The results show that, as

USDT, USDC, BUSD, and DAI. Unlike previous literature that used static depegging

cryptocurrencies  (BTC  and  ETH)  indeed  cause  stablecoin  depegging.  Furthermore,

criteria for depegging. In addition to traditional on-chain price and volume data, this

forest,  and  XGBoost)  that  can  accurately  and  timely  predict  stablecoin  depegging

measures  of  instability  from  past  literature  also  provide  longer-term  early  warning

   E-mail address: eclee@scu.edu.tw

1 Corresponding author.

1

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

reducing investment risks.

JEL classification: G12, G14, G15, G16

Keywords: Stablecoins, Depegging, Machine Learning

in this study did not show a significant early warning effect for our research subjects.

effects for stablecoin depegging. However, surprisingly, the sentiment indicators used

risk  of  stablecoin  depegging  and  make  corresponding  investment  decisions,  thereby

The models constructed in this study enable crypto asset investors to timely predict the

Preprint not peer reviewed

2

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

Abstract

This paper extensively reviews empirical literature on stablecoins, systematically

USDT, USDC, BUSD, and DAI. Unlike previous literature that used static depegging

forest,  and  XGBoost)  that  can  accurately  and  timely  predict  stablecoin  depegging

criteria for depegging. In addition to traditional on-chain price and volume data, this

threshold  values,  we  adopt  a  dynamic  threshold  adjusted  for  trading  volume  as  the

identifying key variables that could lead to depegging risks. Based on this, we construct

predictive models using three machine learning algorithms (logistic regression, random

events. Our main subjects of study are the top four stablecoins in daily trading volume:

Stablecoin Depegging Risk Prediction

Preprint not peer reviewed

The models constructed in this study enable crypto asset investors to timely predict the

risk  of  stablecoin  depegging  and  make  corresponding  investment  decisions,  thereby

effects for stablecoin depegging. However, surprisingly, the sentiment indicators used

period covers from January 1, 2022, to December 31, 2023. The results show that, as

indicated  in  the  literature,  significant  price  and  volume  fluctuations  of  mainstream

study is the first to incorporate sentiment indicators from news sources. The empirical

cryptocurrencies  (BTC  and  ETH)  indeed  cause  stablecoin  depegging.  Furthermore,

measures  of  instability  from  past  literature  also  provide  longer-term  early  warning

in this study did not show a significant early warning effect for our research subjects.

reducing investment risks.JEL classification: G12, G14, G15, G16

Keywords: Stablecoins, Depegging, Machine Learning,

1

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

1. Introduction

overall efficiency and acceptability of the crypto asset ecosystem.

Stablecoins  were  first  introduced  in  2014,  but  their  actual  application  and

The  rapid  development  of  crypto  assets  can  be  attributed  to  their  unique

widespread  application  of  crypto  assets.  Stablecoins  bridge  traditional  finance  and

importance in the market did not begin to significantly increase until 2017 with the rise

and  providing  a  haven  during  the  volatility  of  crypto  assets,  hereby  enhancing  the

of  stablecoins  lies  in  their  ability  to  provide  price  stability,  which  is  crucial  for  the

of the crypto asset market has led to a demand for stablecoins, a type of cryptocurrency

backed by traditional assets (such as fiat currency) or other crypto assets. The core value

technological characteristics and increasing market acceptance. However, the volatility

cryptocurrency markets, allowing funds to move more smoothly between the two areas

Preprint not peer reviewed

of USDT (Ante et al., 2023).    According to statistics from the CoinGecko platform1

value ranking. When considering the daily trading volume, USDT and USDC rank first

at the end of 2023, there are a total of 98 major circulating stablecoins in the market.

$7.8  billion)  respectively  among  cryptoassets.  This  sufficiently  demonstrates  the

The total market capitalization of stablecoins ranks fifth in the overall cryptocurrency

asset market value (approximately $135 billion). The two largest stablecoins, USDT

(with a trading volume of about $34 billion) and fourth (with a trading volume of about

market value of about $25.5 billion) respectively in the overall cryptocurrency market

and  USDC,  rank  third  (with  a  market  cap  of  about  $95  billion)  and  seventh  (with  a

with  the  pegged  currency  through  various  design  structures  (d’Avernas  et  al.,  2021;

Although the primary goal of stablecoins is to maintain the stability of their price

importance of stablecoins in the cryptocurrency ecosystem.

1 https://www.coingecko.com/ and https://www.coingecko.com/en/categories

2

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

which  has  yet  to  return  to  its  pegged  value.  Additionally,  the  market-representative

stablecoins such as BUSD, DAI, USDT, USDC, and the cryptocurrency BTC. These

challenges to market participants. Furthermore, past research and reports on stablecoins

Gadzinski  et  al.,  2023;  Hafner  et  al.,  2023;  Jarno  &  Kołodziejczyk,  2021;  Lyons  &

USDT,  USDC,  and  BUSD  have  also  experienced  brief  depegging  due  to  financial

transparency issues and the collapse of Silicon Valley Bank. (De Blasis et al., 2023)

Viswanath-Natraj,  2023),  in  recent  years,  stablecoins  have  frequently  deviated  from

UST value collapse in 2022 (Uhlig, 2022), and the USDR depegging event in 2023,

found  that  the  depegging  of  stablecoin  UST  could  even  lead  to  instability  in  other

cases  and  articles  show  the  potential  instability  of  stablecoins  and  pose  serious

their pegged value, including the IRON depegging event in 2021 (Clements, 2021), the

have primarily focused on studies of (in)stability, often mentioning the term 'depegging',

Preprint not peer reviewed

stablecoins and systematically identify key variables that could lead to depegging risks.

timely and effective financial risk management system is crucial for the stability of the

the flaws or vulnerabilities in the issuance and operational framework of stablecoins. A

stablecoin depegging, which in the short term can help in the early response to crypto

financial  ecosystem,  particularly  evident  in  the  still-developing  crypto  asset  and

high-quality  stablecoins  is  a  key  challenge  in  crypto  finance  (S&P  Global,  2023).

repeatedly  shocked  the  DeFi  ecosystem,  showing  that  developing  and  maintaining

Before this, there is an urgent need for a timely and effective early warning model for

asset investment decisions; in the long term, it can aid in understanding and monitoring

Despite  being  called  stablecoins,  their  instability  or  depegging  events  have

To  this  end,  this,  the  paper  aims  to  extensively  review  empirical  literature  on

decentralized finance (DeFi) markets (Giokas et al., 2023).

but without providing a concrete definition.

3

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

facilitating more timely and effective detection of depegging states.

The main contributions of this article are twofold: (1) While previous stablecoin

The remainder of the paper is structured as follows: Section 2 reviews the relevant

risks of stablecoin depegging, thereby enhancing the resilience of the stablecoin system.

instability measures and Sentiment Indicators into the study of stablecoin depegging,

These variables include on-chain price and volume data, as well as instability measures

participants in the stablecoin ecosystem by enabling them to effectively respond to the

investigation into the specific phenomenon of stablecoin depegging. This article seeks

risk  indicators  to  form  an  automated,  integrated  quantitative  model.  This  benefits

to concretely define depegging and develop predictive models for it. (2) It introduces

and sentiment indicators proposed in the literature. Furthermore, it integrates multiple

research has primarily focused on the (in)stability of stablecoins, there has been limited

Preprint not peer reviewed

dimensional table based on Metrics (divided into Pricing/Returns, Market Cap/Supply,

analyzing the research subjects of each document. For the selection of research subjects,

articles. Their study encompassed the top twenty stablecoins at that time, statistically

examine academic literature related to stablecoins up to May 2022. Ultimately, from a

stablecoins.  They  employed  a  systematic  literature  review  (SLR)  methodology  to

Trading  Volume,  and  Blockchain  Transaction)  and  Time  Interval  (Minutes,  Hourly,

literature  on  stablecoins.  Section  3  describes  the  data  and  models  used.  Section  4

pool of 2,957 articles, they filtered out 22 peer-reviewed English academic empirical

they used a list sorted by the top twenty market capitalizations. They created a two-

Ante et al. (2023) serves as an excellent starting point for a literature review on

presents the empirical analysis results. Finally, Section 5 concludes.

2. Literature Review

4

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

study  were  predominantly  the  top  five  by  market  value  at  the  time  of  publication,

stablecoins with (non-crypto) macroeconomic factors. The primary data frequency in

Daily, and Blocks) as well as Data Source (Market data aggregators, Cryptocurrency

their surveyed empirical literature was Daily, with the main data source being Market

Pricing/Returns, Market Cap/Supply, and Trading Volume. Moreover, the subjects of

empirical  literature.  Ultimately,  they  categorized  the  22  empirical  articles  into  three

exchanges,  Blockchain  explorers,  and  Blockchain  nodes/clients)  to  consolidate  the

Data  Aggregators.  The  empirical  Metrics  (variables)  primarily  focused  on

which surveys empirical academic literature, provides a solid foundation for choosing

interrelation  of  stablecoins  and  crypto  markets;  and  Cluster  3:  The  relationship  of

main  clusters:  Cluster  1:  The  stability  and  volatility  of  stablecoins;  Cluster  2:  The

mainly pegged to the US dollar and backed by cash or related collateral. This article,

Preprint not peer reviewed

viewpoint. They found that stablecoins differ in their capacity to maintain stable market

being the most effective. These funds ensure full backing by the reference currency and

research targets, selecting explanatory variables, acquiring data sources, and deciding

Kołodziejczyk  (2021),  utilizing  Bullmann  et  al.  (2019)'s  stablecoin  classification,

categorization of current stablecoins into four major types: (1) Tokenized Funds, (2)

depend heavily on a trusted custodian for collateral. The study indicates that simpler

Central  Bank  (2019)  utilized  the  Crypto-cube  Framework  to  allow  for  the

values,  with  tokenized  funds,  typically  fiat-collateralized  and  often  backed  by  USD,

the  design  of  their  stabilization  mechanisms.  Bullmann  et  al.  (2019)  and  European

Off-chain  Collateral,  (3)  On-chain  Collateral,  and  (4)  Algorithmic.  Jarno  &

analyzing  20  stablecoins  includes  the  various  stablecoin  types  from  the  investor’s

The literature suggests that the (in)stability of stablecoins is intrinsically linked to

on data frequencies.

5

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

above  literature  explores  the  stability  of  stablecoins  from  the  perspective  of  pre-

collateral management is centralized or decentralized. They further propose an agent-

variables such as demand shock, demand volatility, fees, and the price of collateral. The

characteristics,  face  varying  impacts  on  their  prices  when  subjected  to  changes  in

mechanisms of five types of stablecoins to ensure stability and minimize risks. Their

simulation results indicate that different types of stablecoins, based on their inherent

issuance stability mechanism design, while other studies investigate post-issuance price

tokenized  fund  designs  outperform  more  complex  stablecoin  structures  in  reducing

dimensions:  the  endogeneity  or  exogeneity  of  stablecoin  collateral  and  whether  the

based  model  that  employs  simulations  to  assess  the  collateral  and  its  management

dynamics  models  of  specific  stablecoins  and  their  stability  maintenance  through

volatility.  Hafner  et  al.  (2023)  categorize  stablecoins  into  four  types  based  on  two

Preprint not peer reviewed

cryptocurrencies, i.e., Bitcoin, Ether, XRP, and Litecoin, which differ across individual

different types of stablecoins, suggesting that any model predicting depegging must be

conditions  (Wang  et  al.,  2020).  Grobys  et  al.  (2021)  observe  Bitcoin's  volatility

increases  in  Bitcoin’s  trading  volume  and  returns  following  transfers  of  stablecoins

stablecoins  but  also  note  the  issuance  size  does  not  significantly  impact  the  effect.

Arbitrage (Lyons & Viswanath-Natraj, 2023; Pernice, 2021). Both pre-issuance design

investors  (Baur  &  Hoang,  2021),  with  their  effectiveness  fluctuating  with  market

stablecoin  issuances  of  USD  1  million  or  more  on  the  return  of  four  major

exceeding USD 1 million. Similarly, Ante et al. (2021b) demonstrate the influence of

significantly  influencing  stablecoin  volatility.  Ante  et  al.  (2021a)  analyze  notable

and  post-issuance  arbitrage  strategies  underscore  the  varied  stability  effects  across

While  stablecoins  are  not  consistently  stable,  they  act  as  a  haven  for  Bitcoin

individually tailored for each type.

6

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

model,  examines

the  directional  overflow  between  stablecoins  and  other

the  prices  of  other  crypto  assets;  instead,  a  surge  in  stablecoin  issuances  appears  to

Additionally, Griffin & Shams (2020), Wei (2018), and Grobys & Huynh (2022) all

significant  price  fluctuation  within  a  single  day.  Kristoufek  (2021),  utilizing  a  VAR

principally  investigate  the  relationship  between  Tether,  the  operator  of  USDT,  and

cryptocurrencies. The researcher reports no substantial proof of stablecoins boosting

Bitcoin–specifically  Tether's  effect  on  Bitcoin.  Griffin  &  Shams  (2020)  observe

acquisitions, typically seen after market declines. In contrast, Wei (2018) uses a VAR

detect  declines  in  Bitcoin's  price  as  a  response  to  surges  in  USDT—a  statistically

model and notes no influence of USDT issuances on ensuing Bitcoin profits, yet records

substantial rises in Bitcoin prices during the 2017 ‘crypto boom’, subsequent to USDT

a significant effect on Bitcoin's trading volumes. Furthermore, Grobys & Huynh (2022)

Preprint not peer reviewed

selecting explanatory variables (feature variables) in constructing models to predict the

differs among them. They ascertain that the fluctuations of major stablecoins like USDT

the "major cryptocurrency market" (primarily Bitcoin (BTC) and Ethereum (ETH)), as

coincide with rises in prices of other crypto assets, suggesting a surge in demand. Thanh

and  USDC  sway  the  stability  of  relatively  smaller  stablecoins,  with  USDT's  pricing

(in)stability,  with  few  proposing  a  theoretically  grounded  threshold  for  depegging.

et al. (2023)  study  the interrelation among major stablecoins and note that volatility

well as the price influence relations among "different stablecoin markets" (mainly the

impact  of  USDT  and  USDC  on  other  stablecoins),  assist  in  forming  the  basis  for

Reviewing  existing  literature  reveals  that  most  focus  on  measuring  or  defining

These explorations of the price interaction between the "stablecoin market" and

exerting influence on the prices of other stablecoins.

depeggings.

7

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

standard deviation.

In  setting  the  depegging  threshold,  literature  often  adopts  practical  viewpoints,

to determine the fractional integration order (d) range. Hoang & Baur (2021) test for

definition, there are additional methods: Grobys et al. (2021) and Grobys (2021) use

with  OHLC  data.  Kwon  et  al.  (2023)  employ  two  measures:  price  deviation  and

Beyond  traditional  standard  deviation  of  returns  for  instability  measurement  or

stablecoins' daily returns to 0.1% and the corresponding benchmark stablecoin's return

1:1  fiat-pegged  stablecoins  as  an  example  to  illustrate  various  literature  settings  for

Rogers & Satchell (1991)’s method, calculating realized annualized daily volatilities

absolute  and  relative  stability  by  comparing  the  standard  deviation  of  individual

subjective determinations, or empirical distribution statistical definitions. Here, we use

downward price deviation. They define stability using the local whittle estimator (LWE)

Preprint not peer reviewed

trading data. While Kwon et al. (2023) propose equilibrium conditions and upper/lower

for thresholds. The most convincing definition of a depegging threshold might be from

as depegging, i.e., prices below $0.9 or above $1.1. Cintra & Holloway (2023) suggest

bounds for five types of stablecoins, they do not provide a concrete calculation method

determination article like S&P Global (2023) considers a price variation exceeding 10%

empirical  distribution  statistical  literature,  such  as  Duan  &  Urquhart  (2023),  using

perspective,  literature  like  Giokas  et  al.  (2023)  uses  the  traditional  forex  market

where prices below $0.97 or above $1.03 are considered depegged (Nicolle, 2023). In

movement  exceeding  1.2%,  i.e.,  prices  below  $0.988  or  above  $1.012.  Subjective

histograms  of  hourly  data  for  major  stablecoins,  depegging  is  defined  as  a  price

significant instability thresholds (akin to the concept of depegging). From a practical

using 5% as the threshold for hourly data and 1% for daily data to minimize noise in

standard, recognizing a price change exceeding 3% of the pegged price as depegging,

8

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

exceeds the upper threshold of its pegged price).

In the literature reviewed above, there has been no consideration of sentiment

there are also discussions on upward depegging (where the market price of a stablecoin

a  Kaiko  cryptocurrency  research  institution,  its  research  report  argues  that  due  to

trading  volumes  should  have  tighter  depegging  thresholds  and  vice  versa.  In  the

thresholds  should  differ  (Carey,  2023).  It  proposes  a  dynamic  threshold  formula

varying  market  trading  volumes  of  different  stablecoins,  individual  depegging

Maynard  Keynes,  reflects  market  driving  forces  of  emotion.  Keynes  suggested  that

indicators. A fear and greed index, with roots tracing back to the 1930s ideas of John

the market price of a stablecoin falls below the lower threshold of its pegged price), but

literature, the focus on depegging direction is primarily on downward depegging (where

inversely proportional to monthly trading volume, arguing that stablecoins with higher

Preprint not peer reviewed

importance alongside other technical analyses (BitDegree, 2023; Tambe & Jain, 2023).

investment or caution. The index's modern incarnation began with CNN Money's 2012

investor behavior. A fear and greed index uniquely gauges market sentiment, reflecting

Bitcoin sentiment in the volatile crypto landscape, highlighting its interpretability and

psychology and the notion that optimism (greed) and pessimism (fear) guide financial

market  behaviors  are  influenced  by  'animal  spirits'—spontaneous  impulses  driving

assesses not prices or volumes but the overall mood, influencing investor behavior and

sentiment. This tool, crucial in understanding market psychology, particularly mirrors

trading  discussions,  illustrating  how  market  confidence  or  uncertainty  influences

collective  emotions  like  fear  or  greed  in  financial  markets,  especially  in  crypto.  It

version  for  traditional  markets,  but  its  conceptual  foundation  lies  in  behavioral

decisions.  Over  time,  this  concept  evolved,  making  fear  and  greed  key  elements  in

decision-making.  Traders  use  it  to  compare  personal  beliefs  with  broader  market

9

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

in

volatility  spillovers,  underlining

the  significance  of  sentiment  contagion

Although  the  fear  and  greed  index  has  been  applied  in  empirical  analysis  of

dominant  cryptos.  This  study  utilized  a  decomposed  and  partial  connectedness

relationships.  It  highlighted  a  strong  correlation  between  investor  sentiment  and

literature  in  the  crypto  context.  Wang  et  al.  (2024)  found  a  U-shaped  pattern  was

participants  and  regulators,  enriching  the  sentiment  analysis  and  market  dynamics

understanding crypto market fluctuations. This offers valuable insights for both market

framework to unravel the intricate web of interconnectedness and bi-directional causal

risk  within  the  cryptocurrency  domain,  particularly  focusing  on  bitcoin  and  12

early stages. Lin et al. (2023) explored the interplay of investor sentiment and market

traditional investments, its application in the cryptocurrency asset market is still in the

identified between the crypto fear and greed index and the price synchronicity of major

Preprint not peer reviewed

between fear sentiment and Bitcoin prices, with both negative and positive interactions

cryptocurrencies like Bitcoin, Ethereum, Litecoin, and Monero. This pattern, emerging

Bitcoin's classification as a new asset class, speculative investment, currency, or a safe

window Granger causality test, identified significant shifts in these interactions before

observed  in  various  subperiods.  The  study's  approach,  involving  a  bootstrap  rolling

investor fear on Bitcoin prices, especially in the context of the COVID-19 pandemic,

ramifications of the COVID-19 pandemic and contributes to the ongoing debate about

investor  sentiment  in  the  cryptocurrency  market,  revealing  complex  patterns  and

from  intraday  data  suggests  a  complex,  non-linear  interaction  between  collective

and during the pandemic. This adds to the growing body of literature on the financial

was  scrutinized  (Gaies  et  al.,  2023).  The  research  revealed  a  non-constant  causality

haven.  Collectively,  these  studies  underscore  the  nuanced  and  dynamic  nature  of

investor sentiment and cryptocurrency price movements. Furthermore, the impact of

10

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

stablecoins have not yet incorporated the fear and greed indicator.

As empirical literature unveils more findings, it also inspires the development of

development  currently.  Before  these  models  are  fully  established,  an  early  warning

cryptocurrency assets is still in its infancy. As of now, empirical research analyses on

stablecoins  will  be  crucial  for  investors  making  decisions  in  cryptocurrency  asset

(1998),  Kwon  et  al.  (2023)  propose  a  game-theoretical  model  that  establishes

equilibrium conditions for five different types of stablecoin mechanisms under various

understanding the evolving landscape of digital assets. The application of the FGI in

interactions  that  challenge  traditional  market  theories  and  offer  new  insights  for

theoretical model literature. Building on the theoretical groundwork of Morris & Shin

model  or  system  capable  of  timely  and  effectively  predicting  the  depegging  of

economic states. The theoretical models for stablecoins are still in the initial stages of

Preprint not peer reviewed

stablecoin category on the CoinGecko platform2  (as of December 31, 2023). We chose

However, with the exception of DAI, which is an on-chain collateralized stablecoin, the

top five stablecoins are USDT, USDC, FDUSD, BUSD, and DAI. However, since data

USDT, USDC, BUSD, and DAI. All of them are stablecoins pegged to the US dollar.

excluded  from  the  study.  Therefore,  the  final  subjects  chosen  for  this  research  are

for FDUSD is only available from July 26, 2023, and the data period is too short, it is

This  paper  selects  the  research  subjects  by  24-hour  trading  volume  from  the

investments and for issuers to understand the flaws in their stablecoins.

2 CoinMarketCap. (2023, December 31). Stablecoins ranking. Retrieved from

https://www.coingecko.com/en/categories/stablecoins
11

3. Methodology

3.1. Data

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

January 1, 2022, to December 31, 20236.

rest are off-chain collateralized stablecoins.

The empirical variables of this study mainly comprise two categories: on-chain

Analytics (ADA)’s data begins on May 17, 2022, initially daily but changed to hourly

from  April  2,  2023.  Due  to  varying  frequencies  and  start  periods  of  different  data

sources, we used daily frequency data for modeling, setting the research period from

trading  volume,  along  with  derived  explanatory  (feature)  variables.  The  latter  data

AlternativeMe's data frequency is daily, starting from February 1, 2018. Alpha Data

transaction  data  and  sentiment  indicators.  The  data  source  for  the  former  is

frequencies include daily and hourly, with data collection starting from January 1, 2018.

sources  are  AlternativeMe4  and  Alpha  Data  Analytics5.  CoinMarketCap's  data

CoinMarketCap3, covering transaction data like pricing/returns, market cap/supply, and

Preprint not peer reviewed

may be derived from OHLC data, and Threh represents the threshold value. Regarding

the settings of P and Thresh, our study adopts Carey (2023) 's definition but differs in

Thresh)  depegging,  thus  utilizing  a  bilateral  depegging  marker  that  considers  both

which we first need to define depegging, essentially setting the label variable Y. The

that we extend the marker to include both downward (P < Thresh) and upward (P >

depegging marker is determined jointly by P (Price) and Thresh (Threshold), where P

This  study  aims  to  construct  a  predictive  model  for  stablecoin  depegging,  for

2022, to ensure a sufficient quantity of depegging labels. For any missing values in this indicator prior

6 Although Alpha Data Analytics' data starts from May 17, 2022, this study begins from January 1,

scenarios. Specifically, the label Y can be expressed as follows:

to May 17, 2022, they are imputed by backfilling with the values from that date.

4 https://alternative.me/crypto/fear-and-greed-index/

5 https://adalytica.io/crypto-fear-and-greed-index

3 https://coinmarketcap.com/api/

12

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

monthly  is the

classification problem.

monthly, where  𝑉𝛼

𝑇ℎ𝑟𝑒𝑠ℎ𝐷 = 1 ― 10/𝑉𝛼

0,         otherwise.

monthly  and  𝑇ℎ𝑟𝑒𝑠ℎ𝑈 = 1 + 10/𝑉𝛼

  To effectively predict the depegging of stablecoins, this paper employs relevant

predictive  variables  (features)  from  literature.  These  include  the  rate  of  change  in

at 1/3, following the optimal setting suggested by Carey (2023). Based on the definition

price for the period. Moreover, Thresh is a dynamic threshold value calculated based

of  Y,  the  predictive  models  we  aim  to  develop  in  this  study  belong  to  a  binary

on  the  rolling  monthly  cumulative  trading  volume  (Trading  Volume).  Specifically,

trading price and volume, market information change rate, sentiment indicators, and

rolling windows sum of trading volume over a 30-day window. The exponent α is set

where    𝑃𝐿  represents  the  lowest  price  for  the  period,  and  𝑃𝐻  is  the  highest

𝑌 = { 1,  if 𝑃𝐿 ≤  𝑇ℎ𝑟𝑒𝑠ℎ𝐷 or 𝑃𝐻 ≥  𝑇ℎ𝑟𝑒𝑠ℎ𝑈

Preprint not peer reviewed

current transaction prices and volumes, providing insights into the fluctuations in price

supply of tokens, and total supply of tokens. This calculation provides an understanding

prediction of when and how stablecoins might deviate from their pegged values, which

day trading volume percentage changes, offering a comprehensive view of the market's

and volume of cryptocurrency assets. The trading price change rate includes metrics

such  as  the  1-hour,  24-hour,  7-day,  and  30-day  trading  price  percentage  changes.

current  market  data,  encompassing  aspects  such  as  market  capitalization,  circulating

price variables. By analyzing these factors, the paper aims to provide a more accurate

Additionally, the trading volume change rate encompasses the 24-hour, 7-day, and 30-

is crucial for understanding their stability and reliability in the cryptocurrency market.

The  rate  of  change  in  market  information  is  calculated  by  comparing  past  and

The  variation  in  trading  price  and  volume  is  calculated  by  comparing  past  and

trading activity over various time frames.

13

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

rate in circulating supply is tracked over different time frames, including 24-hour, 7-

and 30-day market capital percentage changes. These measures help in assessing the

of  the  market  overview  of  cryptocurrency  assets  over  a  given  period.  Market

understanding  the  liquidity  and  availability  of  a  cryptocurrency  in  the  market.  Total

monitored  over  24-hour,  7-day,  and  30-day  periods.  This  information  is  vital  for

day,  and  30-day  circulating  supply  percentage  changes.  This  data  is  crucial  for

supply. The market capitalization change rate includes metrics like the 24-hour, 7-day,

short-term  and  long-term  shifts  in  the  market  value  of  cryptocurrencies.  Circulating

capitalization  is  determined  by  multiplying  the  latest  trade  price  by  the  circulating

supply refers to the approximate number of coins currently in circulation. The change

any  coins  that  have  been  verifiably  burned.  The  change  rate  in  total  supply  is  also

supply represents the approximate total amount of coins currently in existence, minus

Preprint not peer reviewed

as variables: the Fear and Greed Index, the Sentiment Index, and the Awareness Index.

is  methodically  employed  to  identify,  extract,  and  quantify  the  emotional  states  of

natural language processing, text analysis, and computational linguistics. This approach

this rapidly developing financial field. The study utilizes three key emotional indicators

cryptocurrency sector. Such analysis is vital for comprehending investor behavior in

investors,  providing  an  in-depth  perspective  of  the  emotional  landscape  in  the

Analytics. Each of these indices plays a crucial role in offering a nuanced understanding

these  metrics  provide  a  comprehensive  view  of  the  cryptocurrency  market's

gauging  the  overall  scale  and  potential  future  supply  of  a  cryptocurrency.  Together,

The  former  comes  from  AlternativeMe,  while  the  latter  two  are  from  Alpha  Data

performance and trends, aiding investors and analysts in making informed decisions.

In the realm of financial markets, sentiment analysis leverages the capabilities of

of investor sentiment and market dynamics.

14

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

Fear and Greed Index is designed to capture the nuances of market dynamics by

Trends  data,  where  an  increase  in  specific  Bitcoin-related  queries  signals  prevailing

the market, which forms 10% of the index. The remaining 10% is derived from Google

is  dedicated  to  assessing  market  momentum  and  volume.  Social  media  engagement,

particularly  on  Twitter,  contributes  15%  to  the  index.  Surveys,  conducted  in

to 100. Scores from 0 to 24 indicate a state of Extreme Fear, 25 to 46 suggest Fear, 47

market emotions. The Fear and Greed Index encapsulates the prevailing sentiment in

Fear and Greed Index allocates 25% of its weight to Bitcoin's volatility. Another 25%

the Bitcoin market, distilling complex data into a straightforward meter ranging from 0

integrating several key factors into a cohesive analysis, with a specific focus on Bitcoin.

to 54 represent a Neutral stance, 55 to 75 signify Greed, and 76 to 100 denote Extreme

collaboration with strawpoll.com, also account for 15%7. The dominance of Bitcoin in

Preprint not peer reviewed

given topic to the total volume of publications. This metric is also scaled from 0 to 100,

as a continuous indicator of the level of media focus and investor interest in a particular

within the range of 0 to 30 are indicative of a state of Fear, scores from 30 to 70 are

with positive values indicating a rise in awareness and investor attention. Unlike the

Index is measured as the ratio of media publications that are specifically focused on a

sentiment score, the awareness metric does not have a classified range, but rather serves

considered  Neutral,  and  scores  from  70  to  100  are  interpreted  as  Greed.  Awareness

Greed. This index serves as a concise tool for understanding investor sentiment in the

Sentiment  Index  generates  a  sentiment  score  on  a  scale  from  0  to  100.  Scores

cryptocurrency market.

7 Currently paused.

topic.

15

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

view of the asset's volatility in the market.

Drawing  on  the  extensive  research  in  past  empirical  academic  literature  on

In  predicting  the  depegging  of  stablecoins,  the  model  is  customized  to  include

on the methodologies of Grobys (2021) and Rogers & Satchell (1991), which measures

of  downward  price  movements.  These  methods  collectively  offer  a  comprehensive

actual  daily  price  fluctuations.  The  second  method,  price  deviation,  as  proposed  by

primary literature as predictive variables for depegging. In this paper, three measures

variables specific to the stablecoin being analyzed, as well as to BTC and ETH. For

are utilized to calculate volatility indicators. The first is realized daily volatility, based

downward price deviation, also by Kwon et al. (2023), specifically quantifies the extent

in(stability), we also utilize these studies to compute measures of in(stability) from the

Kwon et al. (2023), assesses the deviation from a set benchmark or average price. Lastly,

Preprint not peer reviewed

model considers either its numerical variable or its categorical classification. A similar

USDT, BTC, and ETH, along with 15 variables for volatility indicators specific to these

classifications  for  the  Fear  and  Greed  Index  and  Sentiment  Index,  along  with  a

integrates  27  variables  for  the  rate  of  change  in  market  information  concerning  the

and cryptocurrencies. These indicators, encompassing both numerical and categorical

into two groups. The first includes numerical variables for the Fear and Greed Index,

data, are used selectively. For example, when applying the Fear and Greed Index, the

approach is adopted for the Sentiment Index. Thus, sentiment indicators are divided

instance, predicting the depegging of USDT involves 21 variables related to the rate of

Sentiment  Index,  and  Awareness  Index.  The  second  group  comprises  categorical

change  in  trading  price  and  volume  for  USDT,  BTC,  and  ETH.  The  model  also

The model also employs sentiment indicators that are relevant to both stablecoins

currencies.

16

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

particularly for stablecoin depegging scenarios.

inputted into machine learning algorithms for modeling.

In total, the study utilizes 66 variables: 21 numeric variables for the rate of change

is meticulously chosen to provide an in-depth analysis of the factors influencing the

numerical variable for the Awareness Index. This dual approach, blending quantitative

in  trading  price  and  volume,  27  numeric  variables  for  the  rate  of  change  in  market

depegging  of  stablecoins  in  the  cryptocurrency  market.  Table  1  summarizes  the

and 15 numeric variables for volatility indicators. This comprehensive set of variables

information, 2 numeric (categorical) and 1 numeric variable for sentiment indicators,

variables  are  lagged  by  one  period  to  correspond  with  label  variable  Y  and  are  then

and qualitative data, enhances the understanding of market dynamics in cryptocurrency,

definitions of the feature (predictive) variables used in this paper. All feature (predictive)

Preprint not peer reviewed

17

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

in

of

type

Data

Rate

Rate

name

price

price

price

7-day

change

1-hour

30-day

change

trading

trading

trading

trading

trading

volume

volume

24-hour

24-hour

category

Variable

Numeric

Numeric

Numeric

Numeric

Numeric

Numeric

Numeric

Variable

Description

and volume

trading  price

percentage change

percentage change

percentage change

percentage change

percentage change

percent_change_7d

percent_change_1h

percent_change_24h

percent_change_30d

volume_ percent_change_7d

volume_percent_change_30d

volume_percent_change_24h

7-day trading price percentage

Table 1   Feature (predictive) variable

Preprint not peer reviewed

today's market capital )).

ln(30 ― day market capital

today's market capital )).

today's market capital )).

ln(7 ― day market capital

ln(24 - hour market capital

circulating_supply_percent_change

market_cap_ percent_change_30d

market_cap_percent_change_24h

market_cap_percent_change_7d

24-hour  circulating  supply

24-hour  market

percentage change

information

percentage

percentage

percentage

percentage

calculated

calculated

calculated

calculated

Numeric

Numeric

Numeric

Numeric

volume

change

change

change

trading

change

change

30-day

market

30-day

market

market

capital

capital

capital

7-day

_24h

by

by

by

by

of

in

is

is

is

is

18

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

).

is

is

by

by

_7d

type

Data

_30d

name

7-day

supply

supply

30-day

change

change

24-hour

category

Variable

Numeric

Numeric

Numeric

Variable

calculated

calculated

circulating

circulating

percentage

percentage

Description

total_supply_percent_change_24h

circulating_supply_percent_change

circulating_supply_percent_change

ln(7 ― day circulating supply

today's circulating supplyl )).

today's circulating supplyl ).
ln(30 ― day circulating supply

today's circulating supplyl )
ln(24 ― hour circulating supply

Preprint not peer reviewed

today's total supplyl )).

ln(24 ― hour total supply

today's total supplyl )).

ln(30 ― day total supply

today's total supplyl)).

ln(7 ― day total supply

Fear_and_Greed_Index_Alternative

total_supply_percent_change_30d

total_supply_percent_change_7d

Sentiment_classification_ADA

Fear and Greed Index category

7-day  total  supply  percentage

Sentiment  Index  value  from

Awareness  Index  from  Alpha

30-day total supply percentage

Fear and Greed Index value

from Alpha Data Analytics

_Category_AlternativeMe

Fear_and_Greed_Index

Alpha Data Analytics

from AlternativeMe

from AlternativeMe

Awareness_ADA

Sentiment_ADA

calculated  by

calculated  by

Data Analytics

percentage

indicators*

Sentiment

Sentiment

calculated

category

Numeric

Numeric

Numeric

Numeric

Numeric

change

change

change

Ordinal

Ordinal

supply

Index

total

Me

by

is

is

is

19

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

type

Data

name

𝜎 𝑡 =

lowest

category

Variable

Numeric

Numeric

𝑙𝑛 𝑃𝐿
𝑃𝑂

𝑙𝑛 𝑃𝐻
𝑃𝑂

𝑙𝑛 𝑃𝐻
𝑃𝐶

Variable

indicators

Volatility

Description

+ 𝑙𝑛 𝑃𝐿
𝑃𝐶

Price_Deviation_5d

Price_Deviation_30d

𝑡=0 (𝑃𝑐 ― 1)2
𝑇

outlined by Kwon et al.

highest  price;  𝑃𝐿:

price;  𝑃𝐶: close price.

Realized_Daily_Volatility

set to a duration of 5 days.

outlined by Grobys (2021).

Referring to the methodology

Referring to the methodology

(2023).  𝜎 𝑡 = ∑𝑇―1

where  𝑃𝐶: close price;  𝑇  is

where  𝑃𝑂:  open  price;  𝑃𝐻:

Preprint not peer reviewed

*: The Fear and Greed Index by AlternativeMe and the Sentiment Indicators by Alpha Data Analytics,

latter primarily aids users in understanding the state of the indicator. Additionally, from a data analysis

in addition to their original numerical data, also have corresponding categorical status markers. The

perspective, converting numerical variables into ordinal scales often helps reduce the impact of

fluctuations within numerical ranges on the predictive effectiveness of the target variables.

𝑡=0 (𝑚𝑖𝑛(𝑃𝑐 ― 1,0))2
𝑇

𝑃𝐶: close price;  𝑇  is set to a

Downward_Price_Deviation_30d

(2023),  the  variable  𝑇  is  set

(2023),  the  variable  𝑇  is  set

Downward_Price_Deviation_5d

Referring to the methodology

Referring to the methodology

Referring to the methodology

outlined  by  Kwon  et  al.

outlined  by  Kwon  et  al.

outlined  by  Kwon  et  al.

to a duration of 30 days.

to a duration of 30 days.

duration of 5 days.

  where

Numeric

Numeric

Numeric

(2023).

𝜎 𝑡 =

∑𝑇―1

20

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

3.2. Methods

3.2.1. Predictive Models

the approach to handling imbalanced data.

In our understanding, currently, there are only two pieces of literature that have

This  part  is  divided  into  three  subsections.  The  first  subsection  explains  the

Cintra  &  Holloway  (2023).  The  former  employs  a  combination  of  machine  learning

changepoint  detection  (BOCD)  method.  Cintra  &  Holloway  (2023)  noted  that  the

methods  to  build  their  predictive  model.  The  latter  adopts  the  Bayesian  online

predictive  models  adopted  in  this  study.  The  second  subsection  describes  the

empirical  results  of  BOCD  indicate  that  its  predictions  are  relatively  sensitive  to

performance evaluation metrics used for the models. Finally, the last subsection details

developed predictive models for the depegging of stablecoins: Giokas et al. (2023) and

Preprint not peer reviewed

Regression model is a classic model commonly used in both traditional statistics and

interpretable  results.  Finally,  XGBoost  is  a  frequently  winning  predictive  model  in

machine learning, serving as a baseline for performance evaluation. Random Forest, a

parameter settings. Therefore, this study adopts machine learning approach for model

construction. In this paper, three machine learning methods are employed to develop

tree-based classic model, includes Decision Trees and offers the advantage of easily

used for predicting the outcomes of a categorical dependent variable based on one or

Logistic regression, a fundamental statistical analysis method, which is primarily

The  reason  for  choosing  these  three  models  is  mainly  because  the  Logistic

the predictive model, including logistic regression, random forest, and XGBoost

learning  competitions.  The  following  briefly

development and advantages of these methods.

3.2.1.1.Logistic regression

many  machine

introduces

the

21

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

data mining. (Cox, 1958).

As described by (Kleinbaum et al., 2010), logistic regression is appreciated for its

among predictors and the linearity of independent variables with respect to log odds.

likelihood  estimation  technique  for  more  accurate  parameter  estimation  have

function  (Hosmer  Jr  et  al.,  2013).  The  logistic  model  operates  by  estimating  the

understanding  of  underlying  assumptions,  including  the  absence  of  multicollinearity

more predictor variables. This technique extends the concept of linear regression into

Further  advancements  in  logistic  regression,  such  as  the  adoption  of  the  maximum

logistic  regression  is  to  model  the  probability  of  a  binary  outcome  using  a  logistic

significantly enhanced its robustness (Aldrich and Nelson, 1984). The core principle of

simplicity and interpretability. Despite its straightforward nature, it requires a thorough

the realm of classification, making it a pivotal tool in the field of machine learning and

Preprint not peer reviewed

sampled subsets of the data. This incorporation of randomness diversifies the individual

Forest utilizes a collection of decision tree classifiers, each trained on distinct, randomly

probability that a given instance falls into a particular category, which is fundamentally

algorithm in machine learning (Breiman, 2001). This algorithm is particularly effective

decision trees. It then aggregates the predictions from each tree through majority voting,

(Chen et al., 2020). To improve predictive accuracy and enhance robustness, Random

particularly effective in situations where the dependent variable is dichotomous, such

with  the  class  receiving  the  majority  of  votes  being  selected  as  the  final  prediction

for  handling  large,  high-dimensional  datasets  and  widely  used  for  feature  selection

different  from  the  linear  approach  of  predicting  continuous  values.  This  approach  is

As an extension of decision trees, Random Forest is a powerful ensemble learning

as in medical diagnosis, election outcomes, or credit scoring.

3.2.1.2.Random forest

22

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

(2019).

3.2.1.3.eXtreme Gradient Boosting (XGBoost)

hallmark of well-performing machine learning models (Strobl, 2007).

A notable benefit of Random Forests is their minimal need for data preprocessing,

maximize efficacy and curb overfitting, as detailed by Probst, Wright, & Boulesteix

a low bias similar to individual decision trees but with reduced variance, which is a

enabling them to retain high accuracy even when handling incomplete datasets. Similar

including the number of constituent trees and their growth limit, remains essential to

to their decision tree counterparts, Random Forests utilize criteria such as the Gini index

collective learning approach. Nonetheless, the careful calibration of model parameters,

(Cutler et al., 2012). This ensemble approach typically results in a model that maintains

and entropy for split decisions but surpass them in preventing overfitting thanks to their

Preprint not peer reviewed

the predicted outcomes and the actual results. XGBoost integrates regularization terms

within its framework, a crucial feature that effectively prevents the common pitfall of

techniques, has gained significant traction in the field of data science. This algorithm

overfitting, which is a frequent challenge in machine learning models. This balance of

including  large,  high-dimensional  datasets  (Chen  &  Guestrin,  2016).  XGBoost  is

further enhanced by its implementation of randomization techniques, which not only

designed to optimize an objective function, thereby reducing the discrepancy between

precision  and  generalization  ensures  that  XGBoost  maintains  high  accuracy  and

stands  out  for  its  efficiency  and  effectiveness  in  handling  a  variety  of  data  types,

wide  range  of  applications,  from  small  to  large-scale  problems.  This  flexibility  is

XGBoost  is  an  advanced  machine  learning  model  based  on  gradient  boosting

The scalability is one of the key strengths of XGBoost to make is suitable for a

robustness across a spectrum of predictive tasks (Budholiya et al., 2022).

23

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

3.2.2. Performance metrics

on knowledge discovery and data mining (pp. 785-794).

This  paper  employs  a  machine  learning  model  for  a  binary  classification  task,

status  as  a  powerful  and  reliable  tool  in  the  arsenal  of  machine  learning  techniques

attributes of XGBoost, along with ongoing research and development, underscore its

reduce overfitting but also increase training speed. Moreover, XGBoost's approach to

with  a  specific  focus  on  predicting  stablecoin  depegging  events.  The  predictive

research, offering insights into optimal model tuning for specific applications. These

tree boosting system. In Proceedings of the 22nd acm sigkdd international conference

(Bentéjac et al., 2021).Chen, T., & Guestrin, C. (2016, August). Xgboost: A scalable

handling tree complexity and regularization parameters has been a subject of extensive

performance of the model is rigorously evaluated using a confusion matrix, which is an

Preprint not peer reviewed

accurately predicts the absence of a depegging event. These categorizations are pivotal

matrix  categorizes  the  predictions  into  four  distinct  outcomes:  True  Positives  (TP),

Negatives  (FN),  representing  scenarios  where  the  model  fails  to  identify  an  actual

Positives (FP), denoting cases where the model predicts depegging inaccurately; False

in  computing  various  performance  metrics,  each  offering  unique  insights  into  the

depegging  event;  and  True  Negatives  (TN),  reflecting  situations  where  the  model

essential tool in the assessment of classification models. As depicted in Table 2, this

indicating  instances  where  the  model  correctly  predicts  a  depegging  event;  False

model's ability to predict depegging events accurately

Table 2   Confusion matrix

Actual undepeg

Predict depeg

Actual depeg

TP

FP

24

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

𝑇𝑃

FN

TN

𝑇𝑃 + 𝑇𝑁

Aaccuracy =

Predict undepeg

𝑇𝑃 + 𝐹𝑃  and indicates

evaluated  cases,  Accuracy

significantly outweighs the other.

is  mathematically  expressed  as

the cost of false positives is high. It is calculated as  Precision =

In the context of predicting stablecoin depegging events, the accuracy of the model

Precision, or the positive predictive value, is particularly crucial in scenarios where

plays a pivotal role. Defined as the proportion of true results (both TP and TN) in all

the  proportion  of  predicted  depegging  events  that  were  correctly  identified.  In  the

general overview of its effectiveness across all classifications. High accuracy indicates

it  may  not  always  be  sufficient,  especially  in  imbalanced  datasets  where  one  class

a model that reliably distinguishes between depegging and non-depegging events, but

context of stablecoin markets, a high precision means that when the model predicts a

𝑇𝑃 + 𝑇𝑁 + 𝐹𝑃 + 𝐹𝑁.  This  metric  reflects  the  model's  overall  correctness,  providing  a

Preprint not peer reviewed

that considers both precision and recall. It is particularly useful when there is a need to

depegging event, it is likely to be correct, minimizing the risk of false alarms that could

severe consequences, such as in financial risk management. It highlights the model's

measures the model's ability to correctly identify actual depegging events. High recall

depegging,  the  F1  score  provides  a  more  nuanced  understanding  of  the  model's

find  a  balance  between  the  reliability  of  positive  predictions  (precision)  and  the

effectiveness in capturing all relevant depegging occurrences, ensuring that significant

importance of not missing actual positive cases (recall). In the domain of stablecoin

is essential in situations where missing an actual depegging event (a FN) could have

Recall, also known as sensitivity, is expressed as  Recall =

performance, especially when dealing with imbalanced datasets.

The F1-score, calculated as  F1 - score = 2 ×

lead to unnecessary market reactions.

𝑇𝑃 + 𝐹𝑁. This metric

Precision × Recall
Precision + Recall

events are not overlooked.

, is a balanced metric

𝑇𝑃

25

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

𝑇𝑁

𝑇𝑁 + 𝐹𝑃,  quantifies  the  model's

Lastly,  Specificity,  calculated  as  Specificity =

predictions of stability in the volatile cryptocurrency market.

primary indicator for model selection during the empirical analysis in Section 4.

Accuracy, Precision, Recall, F1-score, and Specificity are common performance

The  Synthetic  Minority  Over-sampling  Technique  (SMOTE)  is  a  widely  used

which involves issues of imbalanced data, Precision and Recall are more appropriate

performance evaluation metrics. Moreover, as this paper considers these two metrics

approach  to  address  the  challenge  of  imbalanced  datasets  in  machine  learning.

equally important, the F1-score, which harmonizes both, is uniformly adopted as the

ability to correctly identify non-depegging events. High Specificity indicates that the

evaluation metrics for binary classification models. This paper will reveal these five

model  is  effective  in  recognizing  true  negatives,  which  is  crucial  in  avoiding  false

metrics for the models built, but given that the main focus of this study is on depegging,

3.2.3. Synthetic Minority Over-sampling Technique (SMOTE)

Preprint not peer reviewed

synthetic samples for the minority class rather than simply replicating existing samples.

This innovative approach is key in mitigating the overfitting issue commonly associated

example,  (Han  et  al.,  2005)  introduced  a  variation  of  SMOTE  that  focuses  on  the

significantly outweighs the number of observations in another, leading to poor model

only adds diversity to the data but also maintains critical information, often lost when

synthetic  samples  along  the  line  segments  joining  these  neighbors.  This  method  not

with  duplicating  minority  class  samples.  The  technique  involves  selecting  a  random

Imbalanced  data  refers  to  situations  where  the  number  of  observations  in  one  class

point  from  the  minority  class,  identifying  its  k-nearest  neighbors,  and  then  creating

SMOTE  is  distinct  from  traditional  oversampling  methods  in  that  it  generates

Additional  studies  have  expanded  on  the  foundational  work  of  SMOTE.  For

performance, especially for the minority class (Chawla et al., 2002).

the majority class is undersampled.

26

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

4. Empirical Analysis

widely recognized and built upon in subsequent research.

developments and challenges in the field since the inception of SMOTE.

The significance of SMOTE extends to various applications where the minority

The data in this study are daily frequency data, spanning from January 1, 2022, to

the  minority  class.  (Fernández  et  al.,  2018)  provides  a  comprehensive  review  of  the

December 31, 2023. The stablecoins studied include USDT, USDC, BUSD, and DAI.

class holds particular importance, such as in fraud detection and rare disease diagnosis.

2008) proposes an adaptive synthetic sampling method to shift the learning bias towards

borderline examples of the minority class. Another noteworthy contribution, (He et al.,

Its effectiveness in balancing datasets without compromising on data integrity has been

Preprint not peer reviewed

prices for four major circulating stablecoins and two major cryptocurrencies (BTC and

the data from the source do not contain any unreasonable values. Regarding the average

impact  stablecoin  stability.  Table  3  presents  the  descriptive  statistics  of  the  closing

Additionally, literature indicates that two major cryptocurrencies, BTC and ETH, may

pegged  price  of  $1.  Additionally,  the  standard  deviation  (STD)  indicates  varying

ETH). Judging by the range of minimum (Min) and maximum (Max) values in the table,

decimal  places,  the  average  value  of  the  stablecoins  may  not  necessarily  equal  their

value of stablecoins (Mean), it can be seen that unless the value is rounded to three

degrees of volatility among different stablecoins.

Table 3   Descriptive statistics

Stablecoins

Number

Symbol

Record

Token

1.0077

1.0001

0.0007

1.0003

1.0000

0.9959

1.0001

USDT

Mean

Ｍax

STD

25%

75%

50%

Min

730

of

T

27

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

T

of

730

730

730

730

Min

DAI

25%

75%

50%

STD

ETH

BTC

Ｍax

577.4

993.6

Mean

USDC

BUSD

0.9998

1891.3

1.0002

1.0000

1.0000

0.9996

1.0002

0.9739

1.0001

0.0011

1791.0

1561.8

0.9980

2044.7

0.9999

0.9715

1.0005

1.0001

0.9999

0.9999

8332.1

0.0011

0.0006

1.0008

3829.6

1.0023

1.0037

Token

Record

Symbol

35074.0

21529.6

15787.3

27272.5

47686.8

Number

Cryptoassets

730 28528.7

Panel  A  of  Figure  1  shows  that  the  price  trends  of  the  four  major  circulating

ETH, as referenced in Panels B and C of Figure 1. Interestingly, the trends of different

in  the  literature,  the  clustering  of  price  volatility  for  stablecoins  may  stem  from  the

stablecoins exhibit different clustering of volatility during various periods. As indicated

significant downward impact on the prices of major cryptocurrencies, such as BTC and

Preprint not peer reviewed

custodian bank, SVB. However, during the same period, USDT and BUSD showed the

stablecoins are not necessarily the same during different periods. For example, during

deviated downward from its pegged price of $1 due to the bankruptcy of its collateral

stablecoins  exhibit  varying  price  trends.  Moreover,  when  individual  stablecoins

opposite trend. This indicates that the state of the mainstream cryptocurrency market

the significant crypto market downturn in May 2022, the price of USDT notably fell

(especially the major ones: BTC and ETH) impacts the stablecoin market, but different

its pegged price of $1. Additionally, in March 2023, the price of USDC substantially

below the pegged price of $1, while the price of BUSD was significantly higher than

encounter specific situations, they show different patterns in their price trends due to

their substitutability.

28

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

Panel B   The closing price of BTC

Panel A   The closing price of stablecoins

Preprint not peer reviewed

Panel C   The closing price of ETH
Figure 1   The closing price of stablecoins and major cryptoassets

that USDC and DAI have higher standard deviations than USDT and BUSD, Table 4

monthly  trading  volume  of  each  individual  stablecoin,  the  results  in  Table  4  are

somewhat counterintuitive compared to those in Table 3. Although Table 3 indicates

the  depegging  threshold  defined  in  this  paper  dynamically  changes  according  to  the

Table 4 shows the depegging statistics for four major circulating stablecoins. Since

29

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

14

16

730

730

168

730

730

193

DAI

Token

2.19%

1.92%

USDT

USDC

BUSD

Record

26.44%

23.01%

Symbol

Number of

Number of

Depeg Ratio

Depeg Event

Table 4   Depegging statistics

depegging rates compared to USDT and BUSD.

The depegging ratios shown in Table 4 highlight another issue. Due to the varying

number of depegging events for each stablecoin and the definition based on dynamic

shows the opposite in terms of the depegging ratio, with USDC and DAI having lower

threshold values, the depegging points in time for each stablecoin may differ. Therefore,

Preprint not peer reviewed

sets having depegging ratios close to the overall population, stablecoins like USDC and

predict the depegging of stablecoins for the subsequent day. The methodology involves

based  split"  but  instead  utilizes  stratified  random  sampling  based  on  Label  Y.  This

DAI exhibit depegging ratios below 10%. To address the data imbalance, SMOTE is

approach ensures that the structure and label proportions in the train and test datasets

(Xs)  for  each  observation.  We  structure  data  processing  methodology  to  accurately

are consistent with those in the full dataset. Furthermore, despite training and testing

adjusting  the  dependent  variable  for  a  one-day  forward  prediction,  necessitating  a

dataset shift by one day. The feature set includes 66 variables, either all numeric or a

in this study, the division of the train dataset and test dataset does not employ a "time-

Regarding the correspondence between label variables (Y) and feature variables

applied for USDC and DAI, which exhibit lower depegging rates.

mix of 64 numeric and 2 categorical variables.

30

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

, ensuring

𝑋𝑖 ― 𝑋min
𝑋max ― 𝑋min

data scale and distribution uniformity.

normalization using a min-max scaling approach, defined as  𝑋𝑖 =

To address missing values, a forward-fill strategy substitutes missing data points

This data processing and preparation strategy is designed to enhance the predictive

with  the  preceding  value.  Where  the  preceding  value  is  unavailable,  a  backward-fill

tuning is the F1 score, which is ideal for imbalanced classification scenarios. Higher F1

approach  is  employed,  using  subsequent  data  to  fill  gaps.  For  categorical  features,

employs  2-fold  cross-validation,  dividing  the  dataset  for  iterative  training  and

performance of the model, particularly in stablecoin depegging prediction. The study

validation. In terms of model performance evaluation, setting the verbose option to 2

provides detailed progress updates. The performance metric for model hyperparameter

especially sentiment indicators, label encoding is applied. Numerical variables undergo

Preprint not peer reviewed

it is evident that the classic logistic Regression model generally performs poorly, while

the main indicator of model performance. The F1-score, being the harmonic mean of

as effective as the best-case scenario in correctly identifying true positives. From this,

Negatives), benefiting the practical operability of the models, we use the F1-score as

the balance between precision and recall is average. This means the model is only half

Random Forest and XGBoost show good predictive effectiveness. Further examining

three different machine learning algorithms. As described in 3.2.2 Performance metrics,

precision and recall, ranges from 0 to 1, with 1 as the best possible score and 0 as the

models to effectively balance Type I Error (False Positives) and Type II Error (False

worst. An F1-score of 0.5 indicates a moderate level of performance, suggesting that

considering  the  nature  of  "depegging"  in  this  study  and  the  desire  for  the  predictive

Table 5 presents the results of predictive models built for four stablecoins using

scores indicate better model performance.

31

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

Toekn

Model

Ratio*

Symbol

SMOTE

Random Forest

Logistic Regression BUSD

Accuracy Precision Recall

Table 5   Model performance

types of stablecoins, as noted in the literature.

analysis shows that the F1-scores for DAI, an on-chain collateralized stablecoin, are

nonlinear models are more effective in predicting dynamic depegging events. Further

(USDT, USDC, and BUSD), which almost all have F1-scores above 0.75. This could

but all results for Random Forest and XGBoost consistently exceed 0.5, implying that

the Precision and Recall metrics, Logistic Regression exhibits significant fluctuations,

relatively lower (0.571) compared to the other three off-chain collateralized stablecoins

be due to the differences in the price stability effects inherent in the design of different

Preprint not peer reviewed

previous empirical literature, major cryptocurrencies (like BTC and ETH) are shown to
32

significant  it  is  as  a  predictive  variable  for  stablecoin  depegging.  Consistent  with

for  the  models  outlined  in  Table  5.  The  higher  the  frequency  of  a  feature,  the  more

Table 6 presents a count statistic of the top ten most important feature variables

*:  After  hyperparameter  tuning,  the  optimal  choice  for  the  SMOTE  ratio  is  determined  to  be  0.6.

Conversely, for stablecoins like BUSD and USDT, with higher depegging ratios, SMOTE is not applied.

Logistic Regression USDC

Logistic Regression USDT

Logistic Regression DAI

F1 Score Specificity

Random Forest

Random Forest

Random Forest

XGBoost

XGBoost

XGBoost

XGBoost

BUSD

BUSD

USDC

USDC

USDT

USDT

0.667

0.928

0.405

0.571

0.994

0.929

0.735

0.869

0.921

0.788

0.982

0.806

0.776

0.982

0.897

0.886

0.962

0.982

0.933

0.744

0.891

0.812

0.947

0.667

0.829

0.758

0.913

0.783

0.571

0.988

0.167

0.939

0.762

0.667

0.837

0.784

0.994

0.214

0.531

0.792

0.994

0.333

0.921

0.857

0.773

DAI

DAI

0.94

0.69

0.78

0.75

0.75

0.25

0.88

0.75

NA

NA

NA

NA

NA

NA

0.5

0.6

0.5

0.5

0.8

0.6

0.6

0.6

0.6

0.6

0.6

1

1

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

5

1

3

4

5

4

2

Rank

Count

Feature

BTC_Realized_Daily_Volatility

USDT_Realized_Daily_Volatility

BTC_volume_percent_change_30d

ETH_market_cap_percent_change_24h

ETH_total_supply_percent_change_30d

Table 6   Aggregation of feature importance

sentiment indicators incorporated in this study.

surprisingly,  the  consolidated  count  in  Table  6  does  not  include  any  of  the  three

have  a  spillover  effect  on  stablecoins,  especially  in  terms  of  supply  and  market  cap

Price  Deviation,  are  indicative  in  predicting  stablecoin  depegging.  However,

in past literature, such as Realized Daily Volatility, Price Deviation, and Downward

fluctuations. Additionally, it is notable that longer-term instability measures proposed

Preprint not peer reviewed

from news sources, a first in this area of research. Empirical analysis from January 1,
33

USDC, BUSD, and DAI. The study utilizes a novel approach by incorporating dynamic

depegging  thresholds  based  on  trading  volume  and  integrating  sentiment  indicators

prediction, focusing on the top four stablecoins in terms of daily trading volume: USDT,

This  paper  presents  a  comprehensive  analysis  of  stablecoin  depegging  risk

BUSD_Downward_Price_Deviation_30d

BTC_volume_percent_change_24h

ETH_volume_percent_change_30d

BUSD_Realized_Daily_Volatility

ETH_Realized_Daily_Volatility

5. Conclusion

BUSD_Price_Deviation_30d

BUSD_Price_Deviation_5d

USDT_Price_Deviation_5d

BTC_percent_change_24h

ETH_percent_change_24h

14

13

12

15

11

10

8

3

4

3

3

3

3

3

6

7

4

3

3

3

3

3

9

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

existing literature.

stablecoin depegging might not be as pronounced as expected.

Interestingly,  our  results  also  highlight  that  stablecoin  type  plays  a  role  in

Our  predictive  models,  developed  using  logistic  regression,  random  forest,  and

investor sentiment is a critical aspect of cryptocurrency markets, its direct impact on

depegging events. However, sentiment indicators, despite their theoretical relevance,

predicting stablecoin depegging events. The models indicate that traditional on-chain

2022,  to  December  31,  2023,  demonstrates  the  significant  influence  of  major

cryptocurrency price and volume fluctuations on stablecoin depegging, aligning with

XGBoost  machine  learning  algorithms,  reveal  the  complexity  and  challenges  in

did  not  show  significant  predictive  power  in  our  models.  This  suggests  that  while

data such as price, volume, and market capitalization changes are crucial for predicting

Preprint not peer reviewed

the importance of considering the underlying collateralization mechanism in stablecoin

non-linear relationships and interactions between various variables. The use of SMOTE

for  addressing  imbalanced  data  sets  enhances  the  models'  ability  to  predict  rare

depegging  risk,  with  on-chain  collateralized  stablecoins  like  DAI  showing  different

factors  influencing  stablecoin  depegging,  requiring  sophisticated  models  to  capture

XGBoost outperformed the logistic regression model. This indicates the complexity of

depegging patterns compared to off-chain collateralized stablecoins. This underscores

depegging events, which is crucial for effective risk management in the crypto asset

risk  assessment.  The  inclusion  of  major  cryptocurrencies  (BTC  and  ETH)  in  the

analysis further illustrates the interconnected nature of the crypto asset market, where

In  terms  of  model  performance,  non-linear  models  such  as  random  forest  and

movements in major cryptocurrencies can significantly impact stablecoins.

market.

34

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

of cryptocurrencies.

for regulatory bodies, financial institutions, and cryptocurrency platforms. This

Overall, this paper contributes to the understanding of stablecoin depegging risks

ecosystem. As stablecoins continue to bridge traditional finance and cryptocurrency

The study’s implications extend beyond individual investors to the broader financial

markets, understanding their stability and risk factors becomes increasingly important

indicators and consider the impact of major cryptocurrencies. While the study advances

tools for better risk assessment and investment decision-making in the volatile world

the field, the limited predictive power of sentiment indicators and the varying effects

based on the type of stablecoin suggest that further research is needed to refine these

models. The findings have practical implications for crypto asset investors, providing

by developing predictive models that combine traditional on-chain data with sentiment

Preprint not peer reviewed

research provides a foundation for developing more robust risk management strategies

and regulatory frameworks, contributing to the overall stability and growth of the

Ante, L., Fiedler, I., & Strehle, E. (2021a). The impact of transparent money flows: Effects of

Ante, L., Fiedler, I., Willruth, J. M., & Steinmetz, F. (2023). A Systematic Literature Review

Bentéjac, C., Csörgő, A., & Martínez-Muñoz, G. (2021). A comparative analysis of gradient

Aldrich, J. H., & Nelson, F. D. (1984). Linear probability, logit, and probit models (No. 45).

Baur, D. G., & Hoang, L. T. (2021). A crypto safe haven against Bitcoin. Finance Research

Ante, L., Fiedler, I., & Strehle, E. (2021b). The influence of stablecoin issuances on

stablecoin transfers on the returns and trading volume of Bitcoin. Technological

boosting algorithms. Artificial Intelligence Review, 54, 1937-1967.

cryptocurrency markets. Finance Research Letters, 41, 101867.

of Empirical Research on Stablecoins. FinTech, 2(1), 34-47.

Forecasting and Social Change, 170, 120851.

crypto asset market.

Letters, 38, 101431.

References

Sage.

35

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

stability

321-357.

prices/fear-and-greed-index

stablecoins the solution? E. C. Bank. https://bit.ly/3nqGKhC

Provision on Curve Finance. arXiv preprint arXiv:2306.10612.

University-Computer and Information Sciences, 34(7), 4514-4523.

Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5-32.

diagnostic system for effective prediction of heart disease. Journal of King Saud

https://research.kaiko.com/insights/defining-depegs-a-new-metric-for-stablecoin-

Minority Over-sampling Technique. Journal of Artificial Intelligence Research, 16,

data classification based on machine learning methods. Journal of Big Data, 7(1), 52.

Budholiya, K., Shrivastava, S. K., & Sharma, V. (2022). An optimized XGBoost based

Clements, R. (2021). Built to fail: The inherent fragility of algorithmic stablecoins. Wake

Bullmann, D., Klemm, J., & Pinna, A. (2019). In search for stability in crypto-assets: are

Chen, R. C., Dewi, C., Huang, S. W., & Caraka, R. E. (2020). Selecting critical features for

Carey, R. (2023). Defining Depegs: A New Metric for Stablecoin Stability. Kaiko Research.

BitDegree. (2023). Crypto Fear and Greed Index. https://www.bitdegree.org/cryptocurrency-

Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic

Cintra, T. N., & Holloway, M. P. (2023). Detecting Depegs: Towards Safer Passive Liquidity

Preprint not peer reviewed

European Central Bank. (2019). Stablecoins – no coins, but are they stable? European Central

De Blasis, R., Galati, L., Webb, A., & Webb, R. I. (2023). Intelligent design: stablecoins (in)

Duan, K., & Urquhart, A. (2023). The instability of stablecoins. Finance Research Letters,

Fernández, A., Garcia, S., Herrera, F., & Chawla, N. V. (2018). SMOTE for learning from

d’Avernas, A., Bourany, T., & Vandeweyer, Q. (2021). Are stablecoins stable? Working

Cutler, A., Cutler, D. R., & Stevens, J. R. (2012). Random forests. Ensemble machine

Gadzinski, G., Castello, A., & Mazzorana, F. (2023). Stablecoins: Does design affect

Cox, D. R. (1958). The regression analysis of binary sequences. Journal of the Royal

imbalanced data: progress and challenges, marking the 15-year anniversary. Journal

stability and collateral during market turbulence. Financial Innovation, 9(1), 85.

Statistical Society Series B: Statistical Methodology, 20(2), 215-232.

stability? Finance Research Letters, 53, 103611.

of artificial intelligence research, 61, 863-905.

learning: Methods and applications, 157-175.

Forest L. Rev. Online, 11, 131.

Bank. https://bit.ly/3yUYkfE

52, 103573.

Paper.

36

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

75(4), 1913-1964.

Finance Research Letters, 47, 102644.

of Economics and Finance, 67, 101924.

a-deep-dive-into-valuation-and-depegging

Journal of Empirical Finance, 64, 207-223.

comparative analysis. arXiv preprint arXiv:2308.07041.

cryptocurrency market. Quantitative Finance, 21(8), 1267-1279.

Global, S. P. (2023). Stablecoins: A Deep Drive into Valuation and Depegging.

Giokas, Y., Hocking, P., Chapcak, M., & Catala, P. (2023). Digital Asset Monitor.

investors’ fear and greed sentiment and Bitcoin prices. The North American Journal

Gaies, B., Nakhli, M. S., Sahut, J.-M., & Schweizer, D. (2023). Interactions between

https://www.spglobal.com/en/research-insights/featured/special-editorial/stablecoins-

Han, H., Wang, W. Y., & Mao, B. H. (2005, August). Borderline-SMOTE: a new over-

Griffin, J. M., & Shams, A. (2020). Is Bitcoin really untethered? The Journal of Finance,

Grobys, K., Junttila, J., Kolari, J. W., & Sapkota, N. (2021). On the stability of stablecoins.

Hafner, M., Pereira, M. H., Dietl, H., & Beccuti, J. (2023). The four types of stablecoins: A

Grobys, K. (2021). When the blockchain does not block: on hackings and uncertainty in the

Grobys, K., & Huynh, T. L. D. (2022). When Tether says “JUMP!” Bitcoin asks “How low?”.

Preprint not peer reviewed

Jarno, K., & Kołodziejczyk, H. (2021). Does the design of stablecoins impact their volatility?

He, H., Bai, Y., Garcia, E. A., & Li, S. (2008, June). ADASYN: Adaptive synthetic sampling

Kwon, Y., Pongmala, K., Qin, K., Klages-Mundt, A., Jovanovic, P., Parlour, C., Gervais, A.,

Kleinbaum, D. G., Klein, M., Kleinbaum, D. G., & Klein, M. (2010). Introduction to logistic

Hoang, L. T., & Baur, D. G. (2021). How stable are stablecoins? The European Journal of

Kristoufek, L. (2021). Tethered, or Untethered? On the interplay between stablecoins and

Hosmer Jr, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). Applied logistic regression

intelligent computing (pp. 878-887). Berlin, Heidelberg: Springer Berlin Heidelberg.

approach for imbalanced learning. In 2008 IEEE international joint conference on

sampling method in imbalanced data sets learning. In International conference on

& Song, D. (2023). What Drives the (In) stability of a Stablecoin? arXiv preprint

neural networks (IEEE world congress on computational intelligence) (pp. 1322-

major cryptoassets. Finance Research Letters, 43, 101991.

regression. Logistic regression: a self-learning text, 1-39.

Journal of Risk and Financial Management, 14(2), 42.

Finance, 1-17. https://bit.ly/3yUn87B

(Vol. 398). John Wiley & Sons.

arXiv:2307.11754.

1328). IEEE.

37

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

discovery, 9(3), e1301.

digital-dollars-are-a-calculated-risk

attacks. American Economic Review, 587-597.

International Money and Finance, 131, 102777.

sentiment? Finance Research Letters, 56, 104177.

prices. The Annals of Applied Probability, 504-512.

and WTSC, Virtual Event, March 5, 2021, Revised Selected Papers 25,

for random forest. Wiley Interdisciplinary Reviews: data mining and knowledge

and Data Security. FC 2021 International Workshops: CoDecFin, DeFi, VOTING,

2023/12/15 from https://www.bloomberg.com/news/newsletters/2023-11-09/crypto-s-

Lyons, R. K., & Viswanath-Natraj, G. (2023). What keeps stablecoins stable? Journal of

Lin, X., Meng, Y., & Zhu, H. (2023). How connected is the crypto market risk to investor

Nicolle, E. (2023). Crypto’s Digital Dollars Are a Calculated Risk. Bloomberg. Retrieved

Morris, S., & Shin, H. S. (1998). Unique equilibrium in a model of self-fulfilling currency

Rogers, L. C. G., & Satchell, S. E. (1991). Estimating variance from high, low and closing

Probst, P., Wright, M. N., & Boulesteix, A. L. (2019). Hyperparameters and tuning strategies

Pernice, I. G. A. (2021). On stablecoin price processes and arbitrage. Financial Cryptography

Strobl, C., Boulesteix, A. L., Zeileis, A., & Hothorn, T. (2007). Bias in random forest variable

Preprint not peer reviewed

Wang, G.-J., Ma, X.-y., & Wu, H.-y. (2020). Are stablecoins truly diversifiers, hedges, or safe

Wei, W. C. (2018). The impact of Tether grants on Bitcoin. Economics Letters, 171, 19-22.

Wang, J.-N., Liu, H.-C., & Hsu, Y.-T. (2024). A U-shaped relationship between the crypto

Thanh, B. N., Hong, T. N. V., Pham, H., Cong, T. N., & Anh, T. P. T. (2023). Are the

importance measures: Illustrations, sources and a solution. BMC bioinformatics, 8(1),

fear-greed index and the price synchronicity of cryptocurrencies. Finance Research

stabilities of stablecoins connected? Journal of Industrial and Business Economics,

https://www.forbes.com/advisor/in/investing/cryptocurrency/fear-and-greed-index-

havens against traditional cryptocurrencies as their name suggests? Research in

Tambe, N., & Jain, A. (2023). Fear And Greed Index For Crypto.

International Business and Finance, 54, 101225.

Uhlig, H. (2022). A luna-tic stablecoin crash.

Letters, 59, 104763.

50(3), 515-525.

crypto/

1-21.

38

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4700764

