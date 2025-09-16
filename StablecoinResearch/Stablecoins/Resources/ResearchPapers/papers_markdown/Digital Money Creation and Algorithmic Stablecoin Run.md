ABSTRACT

This version: December 30, 2023

Kanis Saengchote* and Krislert Samphantharak

Digital Money Creation and Algorithmic Stablecoin Run

Chulalongkorn Business School
and
University of California San Diego

Preprint not peer reviewed

This study examines the downfall of Iron Finance’s algorithmic stablecoin
in June 2021 and draws parallels with the TerraUSD (UST) collapse in May 2022.
Using  transaction-level  blockchain  data,  we  dissect  the  events  leading  to  Iron
Finance’s failure,  unveiling algorithmic  stablecoins’  inherent  vulnerabilities.  We
highlight the disproportionate impact on retail investors, a pattern also mirrored in
UST,  where  confidence  erosion  led  to  a  similar  destabilizing  ‘bank  run.’  Our
analysis  contributes  to  the  broader  understanding  of  the  fragility  of  DeFi
ecosystems and sheds light on the risks of adopting permissionless blockchains and
algorithmic stablecoins as payment infrastructures and forms of digital money.

*  Corresponding  author.  Chulalongkorn  Business  School,  Chulalongkorn  University,  Phayathai  Road,
thank  Unnawut
Pathumwan,  Bangkok  10330,  Thailand.
Leepaisalsuwanna for helping us understand how smart contracts and blockchain work and how to make
sense of blockchain data and Supakorn Phattanawasin for excellent research assistance. This paper was
previously circulated as “A DeFi Bank Run: Iron Finance, IRON Stablecoin, and the Fall of TITAN.”

Keywords: digital money, algorithmic stablecoin, DeFi, bank run, regulation

(email:  kanis@cbs.chula.ac.th).  We

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

ABSTRACT

Digital Money Creation and Algorithmic Stablecoin Run

Preprint not peer reviewed

This  study  examines  the  downfall  of  Iron  Finance’s  algorithmic
stablecoin in June 2021 and draws parallels with the TerraUSD (UST) collapse
in  May  2022.  Using  transaction-level  blockchain  data,  we  dissect  the  events
leading  to  Iron  Finance’s  failure,  unveiling  algorithmic  stablecoins’  inherent
vulnerabilities. We highlight the disproportionate impact on retail investors, a
pattern  also  mirrored  in  UST,  where  confidence  erosion  led  to  a  similar
destabilizing ‘bank run.’ Our analysis contributes to the broader understanding
of  the  fragility  of  DeFi  ecosystems  and  sheds  light  on  the  risks  of  adopting
permissionless  blockchains  and  algorithmic
stablecoins  as  payment
infrastructures and forms of digital money.

Keywords: digital money, algorithmic stablecoin, DeFi, bank run, regulation

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

0

1. Introduction

A stablecoin is a new, privately issued money. In a paper that relates stablecoins to pre-
Civil War U.S. private banknotes, Gorton, Ross, and Ross (2022) began by quoting Hyman
Minsky:  “Everyone  can  create  money;  the  problem  is  to  get  it  accepted.”  Thus,  stablecoin
issuers face two challenges. First, their mechanisms must ensure peg stability. Second, they
must create demand for their stablecoins.

Tokens, digital information created by developers, can be programmed to specify their
creation (minting), transfer, or destruction (burning). Typically, issuers can ‘guarantee’ token
creation  and  redemption  at  a  fixed  exchange  rate  (e.g.,  $1  per  unit),  classifying  them  as
stablecoins.  These  creations  and  redemptions  are  primary  market  transactions,  and  when
secondary market prices differ from the peg, arbitrage opportunities exist.

Stablecoins are digital tokens on blockchain networks. They are designed to peg their
exchange rates to currencies, drawing comparisons to traditional money. With the global reach
of  permissionless  blockchains,  stablecoins  issued  on  these  open  networks  promise  to
revolutionize  payments.  In  June  2019,  Facebook  unveiled  its  plan  to  create  Libra,  a  digital
currency  on  its  blockchain  network.1  The  rise  of  stablecoins  and  blockchain-based  digital
money alarmed monetary authorities, who are concerned about the potential impact on global
financial  stability  and  the  risks  of  ‘liquidity  runs’  that  stablecoin  issuers  face  (G7  Working
Group  on  Stablecoins,  2019;  ECB  Crypto-Assets  Task  Force,  2020;  Liao  and  Caramichael,
2022).

Preprint not peer reviewed

Stablecoins  that  require  self-issued  tokens  to  create/redeem  are  called  ‘algorithmic
stablecoins,’ and notable examples include TerraUSD (UST) on Terra and Frax on Ethereum.
Other issuers may back their stablecoins with off-chain assets (e.g., USD Coin, Tether, Pax
Dollar) or involve collateralized loans (e.g., Dai, Liquity USD) in the process (Li and Mayer,
2022; Lyons and Viswanath-Natraj, 2023). Brunnermeier, James, and Landau (2019) state that
money  issuers  offer  some  level  of  convertibility  to  other  payment  instruments,  and  reserve
backing helps maintain money’s value. Algorithmic stablecoins are fragile, as backing by self-
issued tokens is almost like no backing, making them more vulnerable to depeg.

Iron Finance is a decentralized finance (DeFi) protocol developed by an anonymous
team that issues IRON algorithmic stablecoin on Polygon.2 The protocol was short-lived: it
began on May 29, 2021, grew rapidly to almost $800 million by June 16, and collapsed on June
17,  in  under  three  weeks.  Its  similarity  to  money  and  banking  led  crypto  media  to  liken  its
demise to a ‘bank run.’3

1 See, for example, https://www.cnbc.com/2019/06/17/facebook-announces-libra-digital-currency-calibra-
digital-wallet.html.
2 For more details and discussions on decentralize finance (DeFi), see Schär (2020), Aramonte, Huang, and
Schrimpf (2021), and Carapella et al. (2022)
3 See, for example, https://www.coindesk.com/markets/2021/06/17/in-token-crash-postmortem-iron-finance-
says-it-suffered-cryptos-first-large-scale-bank-run/.

Iron  Finance’s  failure  did  not  deter  algorithmic  stablecoins  issuers.  Frax  and  UST
continued  to  grow,  reaching  $2.9  billion  and  $18.8  billion  in  early  2022.  However,  UST’s
collapse on May 9, 2022, led to discussions of algorithmic stablecoin risks. For example, a
draft U.S. stablecoin bill in September 2022 sought to ban new algorithmic stablecoins for two

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

1

2.1 How IRON stablecoins work.

2. Iron Finance’s Algorithmic Stablecoin

years,4  while  the  EU  banned  algorithmic  stablecoins  in  its  2023  Markets  in  Crypto-Assets
Regulation (MiCA).5

Researchers  have  explored  UST’s  failure  theoretically  (Uhlig,  2022;  Badev  and
Watsky, 2023) and empirically (Briola et al., 2023; Liu, Makarov, and Schoar, 2023). While
Briola et al. (2023) stated that the fall of TerraUSD is very similar to Iron Finance, academic
evidence  on  Iron  Finance  is  limited  to  the  FEDS  Notes  by  Adams  and  Ibert  (2022).  We
contribute by documenting the collapse using transaction-level blockchain data.

To purchase IRON, Iron Finance’s algorithmic stablecoin, users must provide $1 worth
of USD Coin (USDC) and TITAN, a ‘governance token’ issued by Iron Finance. More details
on  this  will  be  provided  later.  However,  it  does  not  fully  rely  on  a  self-issued  token  and
incorporates USDC. The ratio of USDC per IRON created is called the Target Collateral Ratio
(TCR).

We provide an overview of Iron Finance, examining its tokens through a balance-sheet
perspective, and highlight the innate fragility of algorithmic stablecoins. We demonstrate how
the ‘death spiral’ (like TerraUSD) unfolded and show that sophisticated users were more likely
to exit, exit faster, and exit more profitably. Our work complements Liu, Makarov, and Schoar
(2023), who also use blockchain data and reach similar conclusions for TerraUSD. In addition,
we  highlight  the  potentially  confusing  and  distortionary  practice  of  ‘governance  token’
issuance and distribution.

Preprint not peer reviewed

Iron Finance also allows users to sell one unit of IRON in exchange for $1 worth of
USDC and TITAN. The ratio of USDC per IRON redeemed is called the Effective Collateral
Ratio (ECR). The smart contract looks up prices and determines the quantities of USDC and
TITAN  to  receive  and  send.  The  USDC  received  is  held  in  reserve  and  is  disbursed  upon
redemption. The process is shown in Figure 1.

4 https://www.bloomberg.com/news/articles/2022-09-20/house-stablecoin-bill-would-put-two-year-ban-on-terra-
like-coins
5 https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-
mica

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

2

Figure 1: IRON Stablecoins Minting and Redemption

Users send the smart contract a basket of tokens under the pre-specified rule to receive a stablecoin minted by the
smart contract. The smart contract can also redeem the stablecoin for a basket of tokens (potentially different from
those sent). The process is often referred to as burning. Stablecoins (and tokens generally) can only be minted and
burned in the originating smart contract. For Iron Finance, users are required to send USDC (another stablecoin)
and TITAN (Iron Finance’s governance token) to receive IRON (Iron Finance’s stablecoin), and the ratio of USDC
to one unit of IRON created (minted) is called the Target Collateral Ratio (TCR). Users can send IRON to receive
USDC  and  TITAN,  and  the  ratio  of  USDC  to  $1  worth  of  IRON  redeemed  (burned)  is  called  the  Effective
Collateral Ratio (ECR). Creation and redemption prices of IRON are fixed at $1 per unit in the smart contract,
and the algorithm will determine the amount of TITAN required in the transaction (hence algorithmic stablecoin).
Arbitrage opportunities exist when there are price discrepancies between IRON in primary and secondary markets.

Preprint not peer reviewed

6 The USDC used by Iron Finance is not native to the Polygon blockchain but is bridged across from the
Ethereum blockchain. It was not until October 2023 that Circle, the issuer of the ‘original’ USDC, offered
‘native’ USDC on the Polygon blockchain. Thus, the USDC used by Iron Finance is called the USD Coin (PoS)
(symbol: USDC.e), while Circle’s USDC is called the Native USDC (symbol: USDC). Both are distinct crypto
assets created in two separate smart contracts. As a comparison, USDC.e is like a depositary receipt (DR) of
USDC. In this paper, we refer to USDC.e as USDC for convenience.
7 Details of the codes can be found in the Treasury smart contract
https://polygonscan.com/address/0x376b9e0Abbde0cA068DeFCD8919CA73369124825#code and the
CollateralRatioPolicy smart contract
https://polygonscan.com/address/0xDE3BaA1e28740e7fDbdBf65E78efcb3aA994b110#code.
8 Frax is also designed in a similar way, also requiring USDC in addition to FXS (its governance token) to create
FRAX stablecoin. The collateral ratio is also adjusted depending on FRAX’s price on the open market and the
amount of FXS liquidity available. For algorithmic stablecoins with extreme design such as UST, the collateral
ratio is zero. The mechanism to decrease the reliance on external crypto assets to back issued stablecoins was
likely first used by the Saga protocol, and not using any external crypto asset to back at all was first used by the
Basis protocol. Both are discussed in Eichengreen (2019).

An extreme algorithmic stablecoin design (e.g., UST) relies solely on self-issued tokens
(LUNA). The incorporation of external assets like USDC in Iron Finance’s model can enhance
the credibility of its peg.6 The system requires less USDC per IRON if the price of IRON is
above $1 over time.7 Figure 2 shows that IRON traded above $1 in most periods (shaded blue),
so TCR (USDC sent) was always less than ECR (USDC received), relying less upon external
USDC.8

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

3

l

I

l
l

o
C

70%

90%

80%

TCR

a
r
e
t
a

s
o
i
t
a
r

$1.00

$1.10

$0.70

$0.80

$0.90

110%

100%

e
c
i
r
p
N
O
R

8-Jun

7-Jun

2-Jun

3-Jun

6-Jun

4-Jun

5-Jun

15-Jun

16-Jun

11-Jun

14-Jun

12-Jun

13-Jun

TCR drop (IRON > $1)

9-Jun
10-Jun

2.2 Why do users need the IRON stablecoin?

1-Jun
31-May
30-May
29-May

Figure 2: Collateral Ratios During Normal Times

This figure plots the hourly Target Collateral Ratio (TCR) and Effective Collateral Ratio (ECR) between 8:00 am
on May 29 and 8:00 am on June 16. TCR determines the proportion of USDC necessary to mint IRON, while
ECR determines the proportion of USDC participants will receive upon IRON redemption. TCR is reduced if the
time-weighted average price of IRON over the last hour is greater than $1, and vice versa. ECR depends on the
ratio of USDC in the protocol to outstanding IRON. The shaded regions are buckets where the price of IRON is
above $1, likely to trigger a reduction in TCR (labeled TCR drop).

Preprint not peer reviewed

9 Recall that algorithmic stablecoins are created from self-issued tokens. Developers can issue tokens to
themselves at minimal cost. Do Kwon, the developer of the UST stablecoin stated in his 2018 blog post that “At
Terra we see seigniorage as fuel with the potential to make stable-coin applications fundamentally superior to
fiat-based counterparts. If we can find a way to bootstrap steady demand for Terra and capture healthy
seigniorage, Terra could finance fiscal spending of its own and subsidize its [decentralized application].”
https://medium.com/terra-money/scaling-seigniorage-a72356a118ae
10 In fact, many other stablecoins exist on many other blockchain networks. For example, in addition to
Ethereum and Polygon, USDC is also available on Algorand, Avalanche, Flow, Hedera, Solana, Stellar and
TRON. Tether USD (USDT) also supports tokens on many blockchains, and each blockchain network has its
own rules of engagement. Without necessary safeguards, users may wonder whether a USDC on Ethereum is
comparable to a USDC on Polygon (we also saw earlier that there are USDC.e and USDC on Polygon). Thus,
the modern competition of money and payment networks (especially on blockchain) is quite nuanced.

The  raison  d’être  for  stablecoins  in  DeFi  is  to  create  a  nominal  anchor  to  facilitate
payments  and  exchanges,  like  national  currencies.  Without  clear  monetary  authorities,  the
exchange rates for crypto assets (like Bitcoin or Ether) are unstable, making them unsuitable
for  payment  mediums  (Yermack,  2015;  Baur  and  Dimpfl,  2021).  In  addition,  stablecoin
competition is like competition in money or payment networks, as the issuer can benefit from
seigniorage if the face value (e.g., $1) of stablecoin in this form is less than its production cost.9
Profits from money creation are alluring, as Eichengreen (2019) affirms that “monopoly over
seigniorage is a source of political power.”

So, why do users need another stablecoin? After all, IRON borrows credibility from
USDC, so why not use USDC instead?10 If credit card issuers can attract customers with reward
points, stablecoin issuers can also reward their users with tokens. A popular protocol strategy

IRON

ECR

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

4

If Iron Finance were a financial institution, its market value balance sheet might look
like  Figure  3  Panel  A.  The  USDCs  received  are  assets,  the  issued  IRONs  are  debt-like
obligations  like  e-money,13  and  the  issued  TITAN  are  residual  claims  on  the  protocol,  like
equity. Iron Finance had no revenue model upon launch but could share profits with TITAN
holders.

to bootstrap demand is to ‘emit’ tokens to users interacting with their protocols.11 Codes can
be  written  to  emit  tokens  for  any  behavior,  such  as  providing  liquidity  in  decentralized
exchange  pools  (Lehar  and  Parlour,  2021),  lending  pools  (Saengchote,  2023),  or  freely
‘airdropped’  to  generate  marketing  interest  (Allen,  Berg,  and  Lane,  2023).  DeFi  reward
distributions are associated with terms such as ‘staking reward’ and ‘yield farming’ and can
lead to incentive distortion as users reach for yield (Saengchote, 2023).

Iron Finance rewards two users.12 First, it rewards users who provide liquidity in the
four  exchange  pools  involving  their  tokens  (IRON  and  TITAN),  as  they  are  not  traded  in
centralized exchanges like Binance. With deeper liquidity, swap prices have lower slippages
(Lehar  and  Parlour,  2021).  Second,  it  rewards  users  who  lock  TITAN  in  the  single-staking
contract. The staked TITANs have no economic function beyond reducing free float. Rather
than  emitting  governance  tokens,  TerraUSD  incentivizes  users  by  Anchor,  a  deposit  and
lending protocol  for  UST  with  heavily subsidized deposit rates (Liu, Makarov, and  Schoar,
2023).

Preprint not peer reviewed

11 In June 2020, the lending protocol on Ethereum called Compound began to reward users who deposited
(staked) collateral and borrowed tokens with COMP, its governance tokens. Unlike credit card points, COMP
can be sold freely and easily. Deposit and borrow activities in Compound rose sharply as a result. Saengchote
(2023) found that the net borrowing costs (inclusive of rewards) for many assets were negative, and many users
were recursively borrowing to engage in ‘leveraged yield farming’.
12 The distribution of the TITAN reward is managed by the ‘MasterChef’ smart contracts, originally developed
by SushiSwap, an Ethereum-based decentralized exchange protocol that distributed its governance token as
reward to attract users from Uniswap, the-then leading decentralized exchange protocol. Because blockchain
transparency, codes written in smart contracts can be easily forked by other developers. Even if codes can be
protected by software copyright, the anonymity of developers on permissionless blockchains can complicate
legal enforcements.
13 Gorton et al. (2022) refer to stablecoins as non-interest-bearing perpetuities with embedded put options to
redeem at par from the issuer”. Liu, Makarov, and Schoar (2023) refer to UST as “infinite convertible debt with
a face value of $1 backed by LUNA”. Here, IRON is backed by USDC and TITAN.

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

5

Panel A: IRON creation and redemption

Figure 3: Overview of Iron Finance Protocol

This  figure  illustrates  the  schematics  of  how  different  tokens  in  Iron  Finance  are  created  (minted),  redeemed
(burned),  and  used  to  provide  a  decentralized  financial  service  (DeFi)  via  smart  contract  codes.  IRON  is  the
stablecoin,  TITAN  is  the  governance  token,  and  USDC  is  another  stablecoin  not  issued  by  the  Iron  Finance
protocol. Panel A presents IRON’s creation and redemption process from the protocol’s view of asset liabilities.
Panel B illustrates how IRON and TITAN can earn yield in the form of TITAN rewards, which in turn creates
demand for IRON and TITAN.

Preprint not peer reviewed

DeFi protocols tend to call their residual tokens ‘governance tokens.’ This is because
the  U.S.  Securities  and  Exchange  Commission  dictates  that  any  arrangement  with
characteristics of an ‘investment contract’ (The ‘Howey’ Test) are securities and are subject to

Panel B: The uses of TITAN and IRON

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

6

3.1 The collapse of the IRON stablecoin.

3. The Anatomy of the IRON Bank Run

This  section  analyzes  the  collapse  by  analyzing  aggregated  IRON  creations,
redemptions, and contract interactions (staking, unstaking, and token swapping). Token price
data is obtained from swap pools and supplemented with CoinGecko’s data API as necessary.

federal securities laws.14 Developers typically proceed without regulatory approval. Because
of  this,  TITAN’s  cash  flow  rights  are  unclear.  Instead,  developers  allow  holders  to  vote  on
future directions of the protocol (thus, governance), but voting rights and adherence to voting
results are not formalized like corporate laws.

The roles of IRON and TITAN are summarized in Figure 3 Panel B. Swap pools need
liquidity:  yield  farming  provides  liquidity  and  creates  demand  for  IRON  and  TITAN.  The
single-staking  contract  creates  demand  for  TITAN  and  reduces  selling  pressure.  Arbitrage
traders will restore the peg if IRON’s price deviates from $1. If TITAN’s price continues to
increase, the protocol mechanism remains intact.

When IRON trades below $1, arbitrageurs can buy IRON in the secondary market and
redeem it for USDC and TITAN at $1 per unit. The increased demand for IRON should restore
the  peg.  While  arbitrageurs  may  sell  TITAN  to  realize  profits  and  the  price  may  fall,  the
mechanism will work if TITAN remains in demand. Figure 2 shows a brief period of large
depeg (around -6%) on June 9, but the peg was shortly restored. Figure 4 shows that TITAN
dropped from $11.74 to $5.58 (-52%) but continued to increase afterward.

Preprint not peer reviewed

Instead, TITAN’s price rose rapidly. We used the Phillips et al. (2015) algorithm, which
Bouri  et  al.  (2019)  used  to  identify  bubbles  in  the  cryptocurrency  market,  and  found  that
TITAN experienced multiple bubble episodes over this period. This is likely because TITAN
is required to earn yield via the single-staking contract (that reduces free float) or used to create
IRON  to  earn  yield  in  the  stablecoin  USDC-IRON  liquidity  pools.  Generous  emission
schedules, even for stablecoin pairs, and rapid price appreciation made rewards more valuable
and reflexively made IRON and TITAN more sought after, like a flywheel.15

14 See the U.S. SEC Framework for “Investment Contract” Analysis of Digital Assets at
https://www.sec.gov/files/dlt-framework.pdf. Activities such as profit-sharing arrangements, dividend
distributions, or token buybacks can qualify as an investment contract.
15 See, for example, a recommendation made by Mark Cuban (a celebrity investor) on June 13, 2021.
https://blogmaverick.com/2021/06/13/the-brilliance-of-yield-farming-liquidity-providing-and-valuing-crypto-
projects/.

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

7

I

$0.00

TITAN

$50.00

$40.00

$10.00

$70.00

$30.00

$60.00

$20.00

Bubble

e
c
i
r
p
N
A
T
T

Figure 4: Bubble-like appreciation of TITAN

29-May31-May 2-Jun 4-Jun 6-Jun 8-Jun 10-Jun 12-Jun 14-Jun

This figure plots the hourly closing prices of TITAN computed from Iron Finance’s swap pools using on-chain
data between 8:00 am UTC on May 29 and 2:00 am UTC on June 16. The shaded regions are hourly buckets that
are stamped as bubbles using the methodology of Phillips et al. (2015), also used by Bouri et al. (2019). During
the 3-week window, there are multiple episodes of bubble-like price runups.

Preprint not peer reviewed

However,  around  9:00  am  on  June  16,  large  amounts  of  TITAN  and  IRON  were
withdrawn  from  swap  pools.  Figure  5  shows  that  the  magnitude  was  significant:  across  the
three pools containing IRON, 455.9 million were withdrawn in one day – the largest on record
– and 40% of the transactions had at least 1 million sizes. Because TITAN and IRON were
only  tradeable  in  these  pools,  the  liquidity  reduction  led  to  large  price  impacts  as  swaps
occurred. TITAN dropped from $63.74 to $33.51 (-47%) while IRON dropped to $0.911 (-
8.9%),  the  largest  depeg  so  far.  Briola  et  al.  (2023)  also  documented  UST  and  LUNA’s
“remarkable selling pressure” before TerraUSD’s collapse.

TITAN plummeted, and Iron Finance entered a ‘death spiral’. Figure 7 shows that from
5:00 am on June 16 to midnight, TITAN fell from $63.74 to $0.000000672, and its circulating
supply  increased  from  104.68  million  to  922.16  billion,  exceeding  the  intended  maximum
supply of 1 billion specified in the White Paper. By 6:00 am on June 17, the circulating supply
reached  34  trillion.  Iron  Finance  suspended  operation  until  5:00  pm  on  June  17.  Once  it
reopened, waves of redemptions resumed as IRON continued to trade below or close to $0.7467
(remaining USDC).

Figure 6 shows the hourly activities of IRON. For June 9, while the depeg was followed
by a small wave of IRON sales and redemptions (Panel A), IRON’s circulating supply was still
increasing  (Panel  B).  However,  the  depeg  of  June  16  was  followed  by  massive  sales  and
redemptions, plunging circulating supply from a high of 781.83 million to 15.94 million in just
two days.

Because  blockchain  transactions  are  transparent,  transactions  of  large  users  may  be
overinterpreted. DeFi users can react to non-material information and unintentionally trigger a
run (Saengchote, Putniņš, and Samphantharak, 2023).

Figure 5: Withdrawals from Iron Finance-Linked Swap Pools

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

8

0

M

i
l
l
i

s
n
o

400

500

300

200

100

n
u
J
-
8

n
u
J
-
9

n
u
J
-
1

n
u
J
-
5

n
u
J
-
2

n
u
J
-
6

n
u
J
-
4

n
u
J
-
3

n
u
J
-
7

n
u
J
-
1
1

n
u
J
-
0
1

n
u
J
-
4
1

n
u
J
-
8
1

n
u
J
-
5
1

n
u
J
-
3
1

n
u
J
-
6
1

n
u
J
-
2
1

n
u
J
-
7
1

y
a
M
-
9
2

y
a
M
-
1
3

y
a
M
-
0
3

TITAN-IRON

USDC-IRON SushiSwap

USDC-IRON QuickSwap

This figure plots the daily withdrawals from the three swap pools for IRON between May 28 and June 18. The
three pools are the TITAN-IRON SushiSwap, the USDC-IRON SushiSwap, and the USDC-IRON QuickSwap
pools. Units reported are millions of IRONs aggregated between midnight UTC of each day.

Preprint not peer reviewed

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

9

I

I

(

0

m

i
l
l
i

50

)
n
o

-50

150

100

-200

-100

-250

-150

4-Jun

$0.40

$1.00

$1.10

$0.60

$0.50

$0.70

$0.90

$0.80

$0.30

$0.911

$0.939

IRON sold

e
c
i
r
p
N
O
R

t
n
u
o
m
a
N
O
R

29-May 1-Jun

B: IRON circulating supply

A: IRON sale and redemption waves

7-Jun 10-Jun 13-Jun 16-Jun

Figure 6: IRON Stablecoin Run

This figure plots the hourly activities of Iron Finance extracted from on-chain data between 8:00 am UTC on May
29 and 2:00 am UTC on June 18. Panel A plots the hourly price of IRON computed from Iron Finance’s swap
pools and the amount of IRON sold (red positive bars) via swap pools and redeemed (grey negative bars) to the
protocol in exchange for USDC and TITAN. Panel B plots the hourly circulating supply of IRON (which can be
interpreted as outstanding currency or debt, depending on the viewpoint) and hourly price.

Preprint not peer reviewed

7-Jun 10-Jun 13-Jun 16-Jun

0
29-May 1-Jun

IRON circulating supply

IRON redeemed

t
n
u
o
m
a
N
O
R

IRON price

IRON price

e
c
i
r
p
N
O
R

$0.911

781.83

$0.509

$0.939

$0.50

$0.90

$0.40

$1.10

$0.80

$1.00

$0.70

$0.60

$0.30

15.94

4-Jun

700

200

100

300

400

800

500

900

600

)
n
o

i
l
l
i

m

(

I

I

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

10

I

I

i
l
l
i

)
n
o

m
$
(

4-Jun

1-Jun

$30.00

$33.51

$63.74

$60.00

$70.00

$80.00

$40.00

$50.00

$20.00

29-May

e
c
i
r
p
N
A
T
T

t
n
u
o
m
a
N
A
T
T

A: TITAN sale and redemption waves

Figure 7: Governance Token Inflation Spiral

50
40
30
20
10
0
-10
-20
-30
-40
-50

This figure plots the hourly activities of Iron Finance extracted from on-chain data between 8:00 am UTC on May
29 and 2:00 am UTC on June 18. Panel A plots the hourly closing prices of TITAN computed from Iron Finance’s
swap pools and the amount of TITAN sold (red positive bars) via swap pools and redeemed (grey negative bars)
to the protocol and USDC in exchange for IRON. Panel B plots the hourly circulating supply of TITAN (which
can be interpreted as outstanding government securities or outside money, depending on the viewpoint) and hourly
price. The circulating supply is reported using a log scale on the primary axis.

Preprint not peer reviewed

1
29-May 1-Jun 4-Jun 7-Jun 10-Jun 13-Jun 16-Jun

10-Jun 13-Jun 16-Jun

B: TITAN circulating supply

Net TITAN supply

TITAN redeemed

t
n
u
o
m
a
N
A
T
T

100,000,000

e
c
i
r
p
N
A
T
T

TITAN price

TITAN price

34,595,316

10,000,000

TITAN sold

1,000,000

100,000

117.40

10,000

$50.00

$10.00

$80.00

$30.00

$70.00

$60.00

$40.00

$10.00

$20.00

1,000

63.74

$0.00

$0.00

7-Jun

100

)
n
o

10

i
l
l
i

m

(

I

I

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

11

3.2 The microstructure of the Iron Finance run.

This section uses address-level data to investigate how users reacted to the collapse.
We analyze (1) whether the user exited IRON, (2) if exiting, then how fast, and (3) how they
exited (redeeming versus selling IRON). We conjecture that sophisticated participants are more
likely to exit, exit faster, and redeem their stablecoins rather than selling.16

Overall,  42,074  unique  addresses  interacted  with  Iron  Finance,  and  27,532  (65.4%)
exited within two days of the run. The summary statistics are reported in Table 1. On average,
users who exited before June 20 were larger, had longer time on protocol, were more likely to
begin as minter, and were more likely to mint than buy, suggesting they are more sophisticated.

We estimate a logistic model of exit on proxies of sophistication and report the results
in Table 4. Column 1 suggests that sophisticated addresses are significantly more likely to exit.
The marginal effects for large addresses are 13.4%, and for minters, 12.6%. For each day of
experience, the address is 0.5% more likely to exit. All effects are statistically significant at the
1% level. In Column 2, we replace the minter indicator with the share of IRON minted due to
high correlation, and the result remains similar.

To  proxy  for  user  sophistication,  we  consider  (1)  address  size  (large  addresses
transacted more than 50,000 IRON), (2) time on the protocol (measured in days), (3) how IRON
was first acquired (minting versus buying), and (4) proportion of IRON acquired by minting
versus buying. Small addresses are like retail investors; users with a longer time on protocol
likely have more experience; minting IRON is more complicated than buying. As reported in
Table  1  Panel  B,  these  proxies  are  not  significantly  correlated,  except  for  began  as  minter,
which is highly correlated with % IRON minted.

Preprint not peer reviewed

Next,  for  those  who  exited  by  June  20,  we  estimate  a  logistic  redemption  model  on
proxies of sophistication and report the results in Columns 3 and 4. Sophisticated addresses are
more likely to exit via redemption than sales, which can be more profitable because the token
basket is likely worth more than the depegged price. The marginal effects for large addresses
are 7.6% and for minter 15.0%. For each day of experience, the address is 0.37% more likely
to exit via redemption.

Although the transparency of blockchain can, in principle, allow everyone to see and
engage equally under the same rules, our evidence suggests that retail investors are, in practice,
disadvantaged. Combined with the findings of Liu, Makarov, and Schoar (2023) that large and
sophisticated users suffered smaller losses, the results point to the necessity of regulation and
coordination mechanisms to ensure money stability.

Finally, we regress reaction time on proxies of sophistication and report the results in
Table 3. Sophisticated addresses reacted faster. The average is 19.1 hours, so large addresses
reacted more than 34% faster. Addresses that exited via redemption reacted more slowly than
sales. It is possible that users who sold IRON preferred a complete exit, as IRON can be sold
for USDC but redeemed for a basket of USDC and TITAN, which needs to be sold again.

16 There are various ways of classifying sophistication. For example, Liu, Makarov, and Schoar (2023) classify
addresses based on usage of complex protocols (such as bridges) or complex transaction strategies.

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

12

Panel B: Correlation

p50
877
0
4.06
1
1

p5
6.20
0
0.21
0
0

Table 1: Summary statistics

Panel A: All users (N = 42,074)

Mean
42,067
5.69%
5.95
16.6%
11.9%

p95
58,776
0
19.59
1
1

Std Dev
1,247,119
23.2%
6.09
35.4%
32.4%

Size of IRON interaction (unit)
Large address (> 50k)
Time on protocol (days)
Began as minter
% IRON minted (vs bought)

This  table  reports  summary  statistics  of  addresses  that  interacted  with  Iron  Finance.  There  are  42,074  unique
addresses,  27,532  of  which  reacted  within  two  days  of  the  run.  Panel  A  reports  the  summary  statistics  of  all
addresses. We aggregate the IRON interactions for each address between the protocol’s inception and 8:00 am on
June 16 and classify large addresses as those with cumulative interactions of more than 50,000 IRON. Time on
the protocol (in days) is calculated as the first date and time an address minted or bought IRON until 8:00 am on
June 16 as a proxy for experience. We also classify whether the first IRON acquisition is minting or buying and
calculate the share of IRON minted (rather than bought) relative to all IRON acquired. Panel B reports correlation
coefficients between the variables in Panel A. Panel C restricts the sample to those who have reacted by either
selling or redeeming IRON before June 20 and calculated the same statistics as Panel A, with the addition of
reaction time, calculated as hours between 8:00 am on June 16 to the time they first reacted, the method used for
the first reaction (IRON sale or redemption), and the share of IRON sold relative to all exit modes. Panel D reports
the summary statistics for those who did not react by midnight on June 20.

Preprint not peer reviewed

Size of IRON interaction (unit)
Large address (> 50k)
Time on protocol (days)
Began as minter
% IRON minted (vs bought)
Reaction time (hours)
First exit as minter
% IRON redeemed (vs sold)

Size of IRON interaction (unit)
Large address (> 50k)
Time on protocol (days)
Began as minter
% IRON minted (vs bought)

Std Dev
1,516,816
25.6%
6.13
39.6%
37.6%
14.15
38.6%
37.6%

Time on protocol (days)
Began as minter
% IRON minted (vs bought)

p95
78,622
1
20.16
1
100%
42.34
1
100%

Mean
54,593
7.1%
6.30
19.5%
20.9%
19.05
19.2%
19.6%

Panel D: Users who did not exit by June 20 (N = 14,542)

Panel C: Users who exited before June 20 (N = 27,532)

p50
1,495
0
4.56
1
100%
16.57
1
100%

p5
46.98
0
0.22
0
0%
1.86
0
0%

Std Dev
378,435
17.3%
5.98
31.4%
29.7%

Mean
18,352
3.1%
5.29
11.1%
11.1%

p95
25,025
0
18.83
1
1

Large
address
0.1869
0.1215
0.1563

p5
0.91
0
0.19
0
0

p50
229
0
2.97
1
1

Began as
minter

Time on
protocol

0.0547
0.0506

0.8584

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

13

Constant

(1)
Exit

(2)
Exit

Began as minter

Dependent Variable

(4)
Redeemer

(3)
Redeemer

Time on protocol (days)

% IRON minted (vs bought)

Large address (> 50k IRON)

0.599***
(0.06)
0.023***
(0.00)

0.365***
(0.05)
0.029***
(0.00)

Table 2: Logistic models of sophisticated addresses

0.468***
(0.05)
0.026***
(0.00)
0.885***
(0.04)

0.668***
(0.06)
0.023***
(0.00)
0.607***
(0.03)

This table reports the results of logistic models to classify addresses during the stablecoin run. In Columns 1 and
2, the dependent variable is an indicator variable for addresses that reacted during the window of 8:00 am on June
16 to midnight on June 20. Large addresses had cumulative interactions of more than 50,000 IRON between the
protocol’s inception in May and 8:00 am on June 16 (pre-run). Time on protocol (in days) is calculated as the first
date and time an address minted or bought IRON until 8:00 am on June 16. An address is classified as minter if
the first interaction is minting and the share of IRON minted (rather than bought) is calculated relative to all IRON
acquired. The analysis of the minter indicator variable and % IRON minted are conducted separately because of
the high correlation between the two coding schemes. In Columns 3 and 4, the dependent variable is whether the
address exited via IRON redemption (hence redeemer), and the analysis is conditional on the address reacting
before  midnight  on  20  June.  Standard  errors  are  computed  using  the  Huber-White  procedure  and  reported  in
parenthesis. Stars correspond to the statistical significance level, with *, **, and *** representing 10%, 5%, and
1%, respectively.

Preprint not peer reviewed

0.012***
(0.00)
-2.04***
(0.00)

0.008***
(0.00)
0.349***
(0.03)

Observations
Pseudo R-squared

0.988***
(0.03)

-1.93***
(0.02)

27,532
0.0334

42,074
0.0212

27,532
0.0469

42,074
0.0168

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

14

(1)

(2)

Began as minter

First exited as redeemer

Time on protocol (days)

Large address (> 50k IRON)

% IRON minted (vs purchased)

Table 3: OLS model of reaction time

-6.61***
(0.26)
-0.222***
(0.01)

-6.66***
(0.26)
-0.214***
(0.01)
-1.44***
(0.21)
9.35***
(0.28)

This  table  reports  the  results  of  OLS  regressions  of  reaction  time  (in  hours)  on  address  characteristics.  Large
addresses had cumulative interactions of more than 50,000 IRON between the protocol’s inception in May and
8:00 am on June 16 (pre-run). Time on protocol (in days) is calculated as the first date and time an address minted
or bought IRON until 8:00 am on June 16. An address is classified as minter if the first interaction is minting and
the share of IRON minted (rather than bought) is calculated relative to all IRON acquired. An address is classified
as redeemer if the first reaction is redemption, and the share of IRON redeemed (rather than sold) is calculated
relative  to  all  IRON  exited.  In  Column  1,  address  characteristics  are  coded  as  indicator  variables  (minter,
redeemer), and in Column 2, they are coded as continuous variables (% IRON minted, % IRON redeemed). The
analyses  are  conducted  separately  because  of  the  high  correlation  between  the  two  coding  schemes.  Standard
errors  are  computed  using  the  Huber-White  procedure  and  reported  in  parenthesis.  Stars  correspond  to  the
statistical significance level, with *, **, and *** representing 10%, 5%, and 1% respectively.

Preprint not peer reviewed

-0.024***
(0.00)
0.102***
(0.00)
19.5***
(0.13)

Observations
Adjusted R-squared

% IRON redeemed (vs sold)

19.4***
(0.12)

27,532
0.083

27,532
0.089

Constant

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

15

4. Conclusion

even over a short span.

may not be the best payment infrastructures or forms of digital money.

bubble-like (Brunnermeier and Niepelt, 2019) and thus inherently fragile.

Such is the nature of permissionless blockchains and algorithmic stablecoins, which

loath to embrace algorithmic stablecoins. This is not surprising, as they rely on users

Iron Finance is not the first to fail. Eichengreen (2019) discussed the Basis stablecoin

While digital money can potentially transform trade and commerce, policymakers are

(similar to UST) and expressed concerns about its viability and the potential for a ‘self-

believing that self-issued tokens are valuable, making algorithmic stablecoins themselves

potentially anonymous developers. These developers may issue governance tokens with no

unregulated networks, there is a likelihood of another algorithmic stablecoin emerging from

cash flow rights (to avoid violating U.S. securities laws) as a reward to bootstrap demand for

their protocols.18 As large users take profits, blockchain transparency may catalyze a run,

reinforcing spiral’ leading to its collapse.17 Because permissionless blockchains are open,

leaving retail investors to bear the brunt of the damages.19 History is likely to repeat itself,

Preprint not peer reviewed

17 Its white paper is titled “A Price-Stable Cryptocurrency with an Algorithmic Central Bank”. Despite being
backed by high-profile investors, Basis never launched due to regulatory concerns, such as unregistered sale of
securities and compliance with transfer restrictions to accredit investors. They decided to shut down and return
investors’ capital in December 2020. (See https://www.basis.io/). However, Basis’s design inspired Empty Set,
another algorithmic stablecoin protocol launched in August 2020, and an anonymous team of developers forked
Basis’ code and launched as Basis Cash at the end of November 2020
(https://www.coindesk.com/tech/2020/11/30/basis-cash-launch-brings-defunct-stablecoin-into-the-defi-era/).
Both Empty Set and Basis Cash already failed by the time Iron Finance launched.
18 In February 2023, U.S. SEC brought charges against Terraform Labs and Do Kwon, the team behind
TerraUSD failed to register LUNA and UST as securities and thus violated U.S. securities law. In December
2023, U.S. District Judge Jed Rakoff in Manhattan agreed with the SEC and said there was “no genuine dispute”
that Terraform Labs’ crypto assets (including LUNA and the UST stablecoin) were securities under U.S. law
(https://www.reuters.com/legal/terraform-labs-sold-unregistered-securities-us-judge-rules-sec-case-2023-12-
28/).
19 Governance token emission in some protocols is in thousands or tens of thousands percentage points when
annualized. For example, OlympusDAO employs the single-staking contract (reduce free float) and distributes
staking yield of 7,000% by minting its governance token, leading to crypto media comparing it to a Ponzi
scheme (https://www.coindesk.com/policy/2021/12/05/olympus-dao-might-be-the-future-of-money-or-it-might-
be-a-ponzi/). It also inspired protocols forks that distribute yields of more than 621,000%
(https://coinmarketcap.com/academy/article/a-deep-dive-into-the-eight-most-popular-ohm-forks).
OlympusDAO spearheaded the ‘DeFi 2.0’ wave in late 2021, which was roughly equivalent to “doing whatever
it took”, including incurring recursive leverage, to maximize yield disbursed as governance tokens with no cash
flow rights. Many of these DeFi 2.0 protocols suffered because of the UST collapse in May 2022. By the end of
2022, ‘real yield’ emerged as new DeFi narrative, calling for yield “generated from tangible sources of revenue
and are not solely reliant on inflationary token emission”
(https://www.binance.com/en/research/analysis/emergence-of-real-yield).

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

16

and Steel.

REFERENCES

illusion. BIS Quarterly Review, 21.

w26300). National Bureau of Economic Research.

The Terra-Luna case. Finance Research Letters, 51, 103358.

Brunnermeier, M. K. and Niepelt, D. (2019). On the equivalence of private and public

Allen, D., Berg, C., & Lane, A. (2023). Why airdrop cryptocurrency tokens?. Journal of

Carapella, F., Dumas, E. J., Gerszten, J., Swem, N., & Wall, L. D. (2022). Decentralized

Bouri, E., Shahzad, S. J. H., & Roubaud, D. (2019). Co-explosivity in the cryptocurrency

Brunnermeier, M. K., James, H., & Landau, J. P. (2019). The digitalization of money (No.

Badev, A. and Watsky, C. (2023). Interconnected defi: ripple effects from the terra collapse.

Adams, A., & Ibert, M. (2022). Runs on Algorithmic Stablecoins: Evidence from Iron, Titan,

Briola, A., Vidal-Tomás, D., Wang, Y., & Aste, T. (2023). Anatomy of a Stablecoin’s failure:

market. Finance Research Letters, 29, 178-183.
https://doi.org/10.1016/j.frl.2018.07.005

money. Journal of Monetary Economics, 106, 27-41.
https://doi.org/10.1016/j.jmoneco.2019.07.004

Finance and Economics Discussion Series, (2023-044), 1-39.
https://doi.org/10.17016/feds.2023.044

Business Research, 163, 113945. https://doi.org/10.1016/j.jbusres.2023.113945
Aramonte, S., Huang, W. and Schrimpf, A. (2021). DeFi risks and the decentralisation

Baur, D. G. and Dimpfl, T. (2021). The volatility of bitcoin and its role as a medium of
exchange and a store of value. Empirical Economics, 61(5), 2663-2683.
https://doi.org/10.1007/s00181-020-01990-5

Preprint not peer reviewed

Johnson, H. G. (1969). Inside Money, Outside Money, Income, Wealth, and Welfare In
Monetary Theory. Journal of Money, Credit and Banking, 1(1), 30–45.
https://doi.org/10.2307/1991375

nancial stability, market infrastructure and payments, and banking supervision in the
euro area. Occasional Paper Series 247, European Central Bank.

International Finance Discussion Papers 1334. Washington: Board of Governors of
the Federal Reserve System, https://doi.org/10.17016/IFDP.2022.1334

finance (defi): transformative potential & associated risks. Finance and Economics
Discussion Series, 2022(057), 1-33. https://doi.org/10.17016/feds.2022.057

Technical report, Committee on Payments and Market Infrastructures, Bank for
International Settlements.

stablecoin and crypto shadow banking. SSRN Electronic Journal.
https://doi.org/10.2139/ssrn.3757083

Eichengreen, B. (2019). From commodity to fiat and now to crypto: what does history tell us?

Liao, G. Y., & Caramichael, J. (2022). Stablecoins: Growth potential and impact on banking.

Li, Y. and Mayer, S. (2022). Money creation in decentralized finance: a dynamic model of

G7 Working Group on Stablecoins (2019). Investigating the impact of global stablecoins.

Liu, J., Makarov, I., & Schoar, A. (2023). Anatomy of a Run: The Terra Luna Crash (No.

Gorton, G. B., Ross, C. P., & Ross, S. Y. (2022). Making money (No. w29710). National

ECB Crypto-Assets Task Force (2020). Stablecoins: Implications for monetary policy,

Lehar, A. and Parlour, C. (2021). Decentralized exchanges. SSRN Electronic Journal.

(No. w25426). National Bureau of Economic Research.

w31160). National Bureau of Economic Research.

https://doi.org/10.2139/ssrn.3905316

Bureau of Economic Research.

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

17

https://doi.org/10.2139/ssrn.4163038

Currency, 31-43. https://doi.org/10.1016/b978-0-12-802117-0.00002-3

Uhlig, H. (2022). a luna-tic stablecoin crash. SSRN Electronic Journal.

Phillips, P., Shi, S., & Yu, J. (2015). testing for multiple bubbles: historical episodes of

Saengchote, K., Putniņš, T., & Samphantharak, K. (2023). Does defi remove the need for

Lyons, R. K. and Viswanath-Natraj, G. (2023). What keeps stablecoins stable?. Journal of

Yermack, D. (2015). Is bitcoin a real currency? an economic appraisal. Handbook of Digital

Saengchote, K. (2023). Decentralized lending and its users: insights from compound. Journal

International Money and Finance, 131, 102777.
https://doi.org/10.1016/j.jimonfin.2022.102777

of International Financial Markets Institutions and Money, 87, 101807.
https://doi.org/10.1016/j.intfin.2023.101807

exuberance and collapse in the s&amp;p 500. International Economic Review, 56(4),
1043-1078. https://doi.org/10.1111/iere.12132

trust? evidence from a natural experiment in stablecoin lending. Journal of Behavioral
and Experimental Finance, 40, 100858. https://doi.org/10.1016/j.jbef.2023.100858
Schär, F. (2020). decentralized finance: on blockchain- and smart contract-based financial
markets. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.3571335

Preprint not peer reviewed

This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4710515

18

