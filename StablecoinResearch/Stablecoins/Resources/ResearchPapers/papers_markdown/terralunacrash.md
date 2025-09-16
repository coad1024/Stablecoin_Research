Anatomy of a Run: The Terra Luna Crash

Jiageng Liu1, Igor Makarov2, and Antoinette Schoar∗3

1MIT Sloan
2London School of Economics
3MIT Sloan, NBER and CEPR

Abstract

Terra, the third largest cryptocurrency ecosystem after Bitcoin and Ethereum,
collapsed in three days in May 2022 and wiped out $50 billion in valuation. At
the center of the collapse was a run on a blockchain-based borrowing and lending

protocol (Anchor) that promised high yields to its stablecoin (UST) depositors.

Using detailed data from the Terra blockchain and trading data from exchanges,

we show that the run on Terra was a complex phenomenon that happened across

multiple chains and assets. It was unlikely due to concentrated market manipu-

lation by a third party but instead was precipitated by growing concerns about

the sustainability of the system. Once a few large holders of UST adjusted their
positions on May 7th, 2022, other large traders followed. Blockchain technology
allowed investors to monitor each other’s actions and ampliﬁed the speed of the

run. Wealthier and more sophisticated investors were the ﬁrst to run and ex-

perienced much smaller losses. Poorer and less sophisticated investors ran later

and had larger losses. The complexity of the system made it diﬃcult even for in-

siders to understand the buildup of risk. Finally, we draw broader lessons about

ﬁnancial fragility in an environment where a regulatory safety net does not exist,

pseudonymous transactions are publicly observable, and market participants are

incentivized to monitor the ﬁnancial health of the system.

∗Jiageng Liu: E62-685, 100 Main Street, Cambridge MA 02138, USA. Email: jiageng@mit.edu.
Igor Makarov: Houghton Street, London WC2A 2AE, UK. Email: i.makarov@lse.ac.uk. Antoinette
Schoar: E62-638, 100 Main Street, Cambridge MA 02138, USA. Email: aschoar@mit.edu. We thank
seminar participants at LSE, MIT Sloan, Northwestern Kellogg, the 2nd Annual DeFi conference, and
the ICI–SNPI Conference. We also thank Aurelie Barthere and Christopher Rogers for helpful com-
ments and support with the Nansen data, and Jim Myers and Ramsha Ahmad for helpful comments
and support with Flipside data. We also thank Kaiko for access to their data.

1

The collapse of Terra in May 2022 was one of the most highly publicized events in
the crypto industry. Prior to the crash, Terra’s combined market capitalization was $50
billion, with an average daily trading volume of $1 billion, making it the third largest
ecosystem after Bitcoin and Ethereum. However, within three days of the crash, its
value plummeted to zero. This event marked the ﬁrst signiﬁcant run in crypto and
triggered a chain reaction that led to the collapse of several other prominent players,
including Celsius and Three Arrows, and ultimately contributed to the fall of FTX.

Our study of the Terra crash has two primary objectives. First, the crash provides a
unique opportunity to enhance our understanding of runs in the absence of regulatory
oversight or safety nets such as the Federal Reserve or FDIC deposit insurance. The
previous literature that has examined runs on traditional ﬁnancial institutions demon-
strates, among other things, that regulatory interventions alter the incentives of market
participants and can create coordinating events for a run, Iyer and Puri (2012) and Iyer
et al. (2016). Since Terra operated outside of the conventional regulatory framework,
such reliance on regulatory intervention was impossible. As a result, participants on
Terra should have had heightened incentives to monitor the health of the ecosystem
and exit if necessary. Blockchain data enables us to investigate in detail how and when
various market participants ran.

Our second objective is to extract broader insights on the economics of the ecosys-
tem that extend beyond Terra and apply to the entire crypto space. Cryptocurrencies
and decentralized ﬁnance (DeFi) aspire to build a new ﬁnancial architecture. Open
access for all users and observability of pseudonymous transactions on the blockchain
are among the central building blocks of this ecosystem. These features are frequently
regarded as ways to enable all participants to monitor the health of the network, en-
sure its stability, and promote greater ﬁnancial inclusion. However, we ﬁnd that the
Terra case revealed several signiﬁcant fault lines in the typical DeFi architecture that
exacerbate the inherent risks in the system and undermine the advertised beneﬁts.

Using detailed data from the Terra blockchain and trading data from oﬀ-chain cen-
tralized exchanges (CEX), we show that the run on Terra was a complex phenomenon
that happened across multiple chains and assets. At the center of the collapse was
Terra’s algorithmic stablecoin, UST, and a blockchain-based borrowing and lending
protocol, Anchor. UST was designed to serve as a stable medium of transactions on
the Terra blockchain. In economic terms, it was similar to dollar-denominated con-
vertible debt issued against Terra’s native cryptocurrency, LUNA. To incentivize users
to adopt UST, the Anchor protocol oﬀered highly subsidized yields to UST depositors,
which generated signiﬁcant inﬂows of deposits and led to a large increase in UST is-
suance. The newly issued UST were used to pay the interest on Anchor deposits and

1

fund other activities. However, as the amount of deposits skyrocketed, the level of sub-
sidies required became increasingly unsustainable. The Anchor protocol was therefore
exposed to signiﬁcant risks of insolvency, and its collapse had a domino eﬀect on the
entire Terra ecosystem.

Our analysis suggests that the run on Terra was not the result of targeted market
manipulation by a single entity, but rather stemmed from growing concerns about the
sustainability of the system. Once a few large holders of UST adjusted their positions
on May 7th, 2022, other large traders followed suit. Blockchain technology enabled
investors to closely monitor each other’s actions and ampliﬁed the speed of the run.
However, the complexity of the system put less sophisticated and poorer individuals
at greater informational disadvantage. We show that wealthier and more sophisticated
investors were the ﬁrst to run and experienced much smaller losses. Poorer and less
sophisticated investors not only ran later and had larger losses, but a signiﬁcant frac-
tion of them attempted to buy into the run, hoping to “buy the dip.” The system’s
complexity also made it diﬃcult even for insiders to accurately assess the buildup of
risk and adjust system parameters accordingly. Decentralized governance mechanisms
added ineﬃciencies to the system and further exacerbated the instability.

To understand the context of the crash, we brieﬂy need to lay out the design of the
Terra network. Terra was developed by TerraForm Labs (TFL), a company founded
in 2018 by Do Kwon and Daniel Shin. Like other smart contract blockchains such
as Ethereum, the central idea was to build diﬀerent applications and services on the
blockchain to attract a stable user base and generate fees for its cryptocurrency holders.
LUNA was the native cryptocurrency of Terra and derived its value from three main
factors. First, by delegating their coins to validators, LUNA holders could get a share
of Terra’s transaction fees and block rewards. Second, using LUNA, users could access
Terra applications which generated transaction demand. Finally, demand for LUNA
could result from investors speculating on its value.

In an attempt to increase transaction demand on Terra and provide a stable medium
of exchange, TFL introduced an algorithmic stablecoin, UST, which was pegged against
the dollar.1 UST was marketed as the ﬁrst genuine crypto-native stablecoin and was
a distinguishing feature of the Terra network.2 Unlike other major stablecoins such as
Tether or Circle, which are backed by oﬀ-chain liquid assets, e.g., treasuries, UST was
not supported by oﬀ-chain collateral but by a smart contract that allowed an exchange

1Terra also oﬀered a suite of other stablecoins pegged against other ﬁat currencies, like Korean

Won or Euro, but UST was by far the most prominent one.

2Dai could be considered another contender for a crypto-native stablecoin. However, its price
frequently de-pegged until it started using a basket of stablecoins backed by traditional assets to
support the peg.

2

of one unit of UST to $1 worth of LUNA and vice versa. The pegging mechanism relied
on traders taking advantage of an arbitrage opportunity that would present itself every
time UST lost its peg in either direction. For example, if the price of UST falls below
$1, arbitrageurs could buy UST at a price below $1 and convert it into $1 worth of
LUNA, and in the process, reduce the supply of UST and drive up its price. And vice
versa if the UST price is above $1.

In economic terms, UST was like inﬁnite maturity convertible debt with a face value
of $1 backed by LUNA. The main danger to the stability of the system was if users
suddenly stopped holding UST and converted them to LUNA. While conversion of
UST to LUNA reduces the UST supply, it also increases the LUNA supply and dilutes
existing holders of LUNA. If this increase in the LUNA supply is expected to lead to
a signiﬁcant decline in the LUNA price, then any LUNA holder would be better oﬀ
selling LUNA ahead of the conversion resulting in a so-called “death spiral” of both
UST and LUNA falling in tandem.

It would be tempting to conclude that any conversion of a signiﬁcant amount of
UST to LUNA must lead to a decrease in the LUNA price. But as in the case of
convertible debt, if investors are fully rational and understand that the outstanding
supply of UST is a claim on LUNA’s value, the conversion of UST to LUNA does
not have to have an impact on the LUNA price since the conversion would be already
priced in, see e.g., Glasserman and Nouri (2016), Pennacchi and Tchistyi (2019). Of
course, for LUNA to successfully back UST, there must be enough value in the Terra
system. Hence, one might expect that the instability of the system increases with the
amount of the outstanding UST supply.

To increase the adoption of UST, Terra developed a borrowing and savings protocol,
Anchor. Unlike other DeFi protocols where the lending yield is generated through
interest paid on borrowings, we show that both borrowing and lending rates on Anchor
were heavily subsidized.
In particular, holders of UST could deposit their UST at
Anchor at a stable 19.5% yield which was substantially higher than the yield on other
major stablecoins, and the net borrowing rate was consistently below the lending rate.
The high deposit rate attracted signiﬁcant deposit inﬂows, which were accompanied
by a strong run-up in the price of LUNA and large issuance of UST by TFL. The
proceeds from the sale of UST were used to pay the interest on loans on Anchor and
fund other activities. Initially, TFL was willing to provide these subsidies, likely with
the expectation that new users would continue to utilize the platform and generate
future revenues. But it became increasingly apparent that the level of subsidy could
not be sustained in the long run. By April 2022, the daily subsidy level had reached
$6 million, prompting the Terra community to pass a proposal to gradually decrease

3

the 19.5% interest rate to a more sustainable and market-driven level, starting on May
1, 2022.

Contemporary with these developments, there were additional indications of declin-
ing network fundamentals. First, following its peak value of $119.18 on April 5, 2022,
the value of LUNA experienced a decline in conjunction with a general downturn in the
value of cryptocurrencies, thereby diminishing the relative market valuation of LUNA
compared to UST. Second, during the latter half of April 2022, there was a substantial
decrease in the entry rate and an increase in the exit rate from Anchor.

Although it is not possible to assert with absolute certainty that the run on Terra
was inevitable, our analysis shows that by following unsustainable policies, the Terra
network was becoming increasingly fragile. In this situation, models such as Morris
and Shin (1998), Goldstein and Pauzner (2005), or Abreu and Brunnermeier (2003)
predict that even a small shift in fundamentals or common public signals can act as a
coordination mechanism and trigger a run by investors. In the context of cryptocurren-
cies, where the actions of agents on the blockchain are publicly observable and agents
can monitor and react to each other’s actions, the actions themselves can serve as a
coordination mechanism.

The ﬁrst signs of the run appeared on May 7, 2022, when two large addresses
withdrew 375M UST from Anchor. Following these withdrawals, the UST price began
to decrease, and other withdrawals from Anchor intensiﬁed. Despite TFL’s attempts to
stabilize the peg by purchasing UST, investors continued to withdraw their funds from
Anchor. The rate of withdrawals from Anchor intensiﬁed during the late hours of May
9, 2022, coinciding with the point at which the market capitalization of LUNA became
equal to the outstanding supply of UST. As a result, the value of UST plummeted to
$0.75. By the end of May 13, Anchor had fewer than 2 billion UST remaining, and the
value of UST had declined to below $0.2.

We document how diﬀerent types of investors behaved during the run and exited
from Terra. We exclude all smart contract addresses and classify the remaining ad-
dresses by the size of their pre-run balance on Anchor and observed levels of ﬁnancial
sophistication based on the history of their trades. To measure sophistication, we look
if an address had previously traded across several exchanges and used bridges to trans-
fer tokens to other blockchains. In addition, we compute the level of trading volume
divided by the balance in the account.

We show that large and more sophisticated investors were the ﬁrst to run, and ran
much more decisively, i.e., withdrew most of their coins conditional on running. We
also document that large and sophisticated traders eﬀectively used multiple avenues to
exit UST and LUNA. In contrast, less sophisticated and smaller wallets were late to

4

the run and sustained much larger losses. In fact, several especially smaller addresses
even bought UST on May 9 or 10, when for a short time, it looked like the price
was stabilizing at a level below $1, potentially in an attempt to “buy the dip.” These
addresses fared particularly badly at the end of the run.

Thus, although the prices of UST and LUNA, as well as trades of large wallets,
were publicly observable on the blockchain, it did not create a level playing ﬁeld for all
depositors. Our analysis indicates that similar to the ﬁndings of studies investigating
runs on traditional banks, e.g., Iyer and Puri (2012) and Iyer et al. (2016), wealthier
and sophisticated investors were able to leverage this information more eﬀectively and
run earlier.

The UST peg design adds an additional dimension how investors could exit UST,
by either selling UST at the market price or swapping UST for LUNA and then selling
LUNA at the market price. In the absence of frictions, the second option would deliver
In practice,
strictly higher proﬁts that increase with the size of the UST discount.
investors faced several frictions, in particular swap fees, price impact when selling
LUNA, and the risk of a delay between the time investors send their funds to an
exchange and when they are cleared for trading. We show that during the run, the
UST discount and the swap volume closely followed each other. As the UST discount
widened investors found it increasingly more proﬁtable to swap UST for LUNA and
In the period from May 7 to May 13, users
engage in the UST-LUNA arbitrage.
swapped UST worth $4.65 billion. As users swapped UST for LUNA, the price of
LUNA precipitously fell leading to increasing dilution which further depressed the
price of LUNA, and led to a dramatic “death spiral.”

Interestingly, we ﬁnd that Alameda Research, a cryptocurrency trading ﬁrm closely
aﬃliated with the FTX exchange, conducted the largest amount of UST-LUNA swaps
among Anchor depositors.
It seems that the swap fees and uncertainty about the
execution price of LUNA on exchanges discouraged most other Anchor depositors from
utilizing the native swap contract as an exit strategy. But Alameda Research, with
its advantageous access to the FTX exchange, had a competitive advantage over other
market participants.

We also analyze an earlier de-pegging incidence in May 2021 and show that it
foreshadowed the risks and economic mechanisms that were important during the May
2022 crash. Similar to the May 2022 crash, the de-pegging coincided with LUNA
market capitalization declining to a level close to the aggregate market value of UST
and investor withdrawals from Anchor. As in May 2022, withdrawals were concentrated
among wealthier investors, while low-wealth investors continued pouring their funds
into Anchor.

5

One might ask why the run was avoided in May 2021, but not in May 2022. A
critical factor appears to have been that the outstanding supply of UST was much
smaller in May 2021, which enabled TFL to function as a lender of last resort. We
show that nearly all UST-LUNA swaps were initiated by TFL, which presumably held
onto the newly swapped LUNA instead of selling it. Furthermore, as the recent SEC
lawsuit against TFL alleges, the peg was restored due to stabilization purchases of UST
by a third party, which has been identiﬁed as Jump Trading. But market participants
were unaware that TFL and Jump Trading were engaging in the stabilization of UST.
As a result, when participants saw the price re-pegging, they appear to have interpreted
it as a sign of the system’s stability. In contrast, in May 2022, traders were aware of the
fact that TFL was using funds held in LFG addresses to support the peg. They also
knew that the supply of UST and the amount of UST locked in the Anchor protocol
was signiﬁcantly larger than the amount available to support the peg. Thus, traders
might not have believed that the stabilization would succeed.

Our paper contributes to several diﬀerent strands of the literature. First, there is a
growing literature that examines the design and operation of stablecoins. For overviews
of diﬀerent design features and stabilization mechanisms, see for example, Eichengreen
(2019); Arner et al. (2020); Makarov and Schoar (2022); Gorton and Zhang (2021); and
Gorton et al. (2022) provide a comparative analysis of stablecoins and private money
creation during the wildcat banking period of 19th century United States.

d’Avernas et al. (2022) and Li and Mayer (2022) develop equilibrium models of the
underlying pegging mechanisms for stablecoin protocols and underscore that mech-
anisms lacking external collateral are vulnerable to run risks if signiﬁcant negative
demand shocks arise, even if they remain stable for small shocks. Lyons and Viswanath-
Natraj (2023) analyze the stability mechanisms of Tether and Dai. Uhlig (2022) pro-
poses a model of the Terra-Luna crash.

The pegging mechanism behind UST and LUNA is also related to the literature
that studies contingent convertibles, see Glasserman and Nouri (2016), Pennacchi and
Tchistyi (2019), and Hillion and Vermaelen (2004).

Second, our results are related to a vast literature on runs on ﬁnancial institutions,
see Brunnermeier and Oehmke (2013) for an excellent recent survey of this literature.
One part of this literature, starting with Bryant (1980) and Diamond and Dybvig
(1983), posits that bank runs can arise as sunspot phenomena because of the liquidity
mismatch and coordination problems among depositors. Another part emphasizes the
role of information asymmetry about bank fundamentals, see for example, Chari and
Jagannathan (1988) and Jacklin and Bhattacharya (1988). Following Morris and Shin
(1998), a growing body of literature explores the interaction between fundamentals

6

and strategic behavior by market participants as for example in Goldstein and Pauzner
(2005), Goldstein (2013), and Abreu and Brunnermeier (2003). In these models, agents
receive private and public signals about the strength of fundamentals. A common
public signal acts as an additional coordination event for agents’ actions.

A few recent empirical papers have analyzed the behavior of depositors during bank
runs using individual account information. Iyer and Puri (2012) and Iyer et al. (2016)
highlight the role that deposit insurance plays in mitigating a run as well as relation-
ships between depositors and the bank. These papers also highlight the importance of
depositor composition in accelerating a run. Looking at the run in the money market
mutual fund market following the Lehman crash, Schmidt et al. (2016) similarly analyze
coordination as a function of incomplete information and strategic complementarities
between investors.

Third, the pegging mechanism behind UST and LUNA has some resemblance to
the large literature in international ﬁnance on the causes and consequences of currency
crises in countries with ﬁxed exchange rates. A large body of initial research, commonly
referred to as “ﬁrst generation models”, emphasizes the role played by deteriorating
fundamentals as in Krugman (1979), Flood and Garber (1984), or Eichengreen et al.
(1994). A body of “second generation” models allows currency crises to arise from
speculative attacks that are potentially self-fulﬁlling, see for example Obstfeld (1996),
Chamley (2003), or Cukierman et al. (2004). In these models, there is typically an
equilibrium under which the peg is sustainable, and another under which the peg can
be broken if speculation is suﬃciently intense. For a comprehensive review of the
extensive literature on currency crises, see Lorenzoni (2014).

Finally, we also relate more broadly to the literature that has tried to model the
risk and value of cryptocurrencies such as Abadi and Brunnermeier (2018), Cong et al.
(2021); Kogan et al. (2021); Hu et al. (2019); Liu and Tsyvinski (2021), and the beneﬁt
to a platform of having a native token such as in Sockin and Xiong (2023); Li and Mann
(2018); Gryglewicz et al. (2021).

The rest of the paper is organized as follows. Section 1 describes the data used
in this study. Section 2 provides description of the Terra network and the design of
Terra’s algorithmic stablecoin. In Section 3, we provide an analysis of the economics
of Terra leading up to the run. Section 4 documents the run on UST and the collapse
of LUNA. In Section 5, we compare the interventions of TFL in the May 2022 crash
to the earlier de-pegging event in May 2021. Section 6 concludes.

7

1. Data

Our primary data source is the Terra blockchain. Like other permissionless cryp-
tocurrencies, the Terra blockchain is publicly available. However, the Terra data are
substantially more complex than say the Bitcoin data, which only record bitcoin trans-
fers from one account to another. The structure of Terra data is comparable to
Ethereum, since many transactions on Terra are not simply token transfers but the
inputs and outputs of smart contracts. One must parse the smart contract data to un-
derstand the Terra data successfully. The work is challenging because (1) each smart
contract has its own data structure, (2) smart contracts often rely on each other, and
(3) some transactions are not settled immediately but require a delay or resolution of
other conditions.

We are unaware of any data source that provides fully processed Terra data. In our
research, we work closely with two leading blockchain data analytics companies, Nansen
and Flipside.3 We learned from them how to process the blockchain transactions and
use their data to help with validating our data processing.

We use several data in our analysis. First, we use Terra token transfers from October
2021 to August 2022 that come from transaction logs. When a transaction is settled,
the blockchain records logs that contain the transfer, minting (creating), and burn-
ing (destroying) of tokens. The tokens include LUNA, Terra stablecoins, and CW20
standard tokens.4 To collect the logs, we run a Terra Classic node using data from
ChainLayer Quicksync that stores copies of blockchains to speed up synchronization.5
We use Terra Classic’s API to query the data in each block. We ﬁrst use the LCD
(Light Client Daemon) API to query transactions, fees, and the log of transactions.
Next, we parse the logs into structured data. We record the time of transfer, the source
account, the destination account, the token, and the transfer amount. For transactions
that require a delay or condition to settle, we use the RPC (Remote Procedure Call)
API to query the list of settlement events in each block.6

Second, we use genesis ﬁles from Terra’s online code repository.7 Genesis ﬁles are
snapshots of the blockchain state at each upgrade, i.e., each fork. When the Terra

3See https://flipsidecrypto.xyz/ and https://www.nansen.ai/.
4CW20 is the standard for fungible tokens on Terra such as aUST, bLUNA, and ANC. The data
do not cover transfers of NFTs that follow the CW721 standard. Both CW20 and CW721 standards
closely resemble the equivalent ERC20 and ERC721 standards on Ethereum. See https://github.c
om/CosmWasm/cw-plus/blob/main/packages/cw20/README.md for more detail.

5See https://www.chainlayer.io/quicksync/
6For example, LUNA un-delegation requires a 21-day delay. Spending from the community pool

requires approval of the on-chain governance.

7See https://github.com/terra-money/classic-mainnet.

8

developers release a major software upgrade, validators take a snapshot of the state of
the blockchain and resume from there. Therefore, a snapshot fully characterizes the
blockchain state before an upgrade. We collect ﬁve snapshots that date back to April
23, 2019 (Columbus-1), June 6, 2019 (Columbus-2), December 13, 2019 (Columbus-3),
October 3, 2020 (Columbus-4), and September 30, 2021 (Columbus-5). We reconstruct
the daily balances of UST, LUNA, and CW20 tokens since Columbus-5 by ﬁnding the
cumulative sum of token transfers and adding the initial balance.

Third, we use Flipside pre-processed data of speciﬁc transactions. These data
include (1) Terraswap, Astroport, and the Terra native swaps, (2) LUNA delegation
and un-delegation, (3) airdrops of ANC, MIR, and MINE, and (4) governance proposals
and voting records on both Terra and Anchor.

To link pseudonymous addresses with real-world entities we use Flipside and Nansen
address labels as well as labels obtained from searching online forums, social media, and
open-source code repositories. We also manually label some addresses by examining
their transaction logs and graphs. For example, centralized exchanges usually ask users
to specify their account number in deposit transactions, which makes it possible to
identify them in the data. We also identify unnamed smart contracts from transaction
logs. We collect their addresses from transactions that are smart contract instantiation
or execution.

We also use the Ethereum blockchain data. We parse transactions that correspond
to trades on the Curve pool between UST and other stablecoins, and trace UST and
LUNA bridge transfers between Terra and Ethereum blockchains.

Finally, we obtain exchange trading data from Kaiko, a leading data provider of
trading data on centralized exchanges. Kaiko provides data on minute-level order
book depths, tick-level trading records, and the minute-level funding rates of perpetual
futures. The data cover 19 exchanges and 131 trading pairs for UST, LUNA, ANC,
and MIR tokens.

Put together, our data cover 7.5 million blocks that contain 228 million transactions
from October 3, 2020, to May 15, 2022. One transaction can result in multiple logs on
the blockchain. We collect 657 million transaction logs. These logs cover 367 million
voting records of oracle prices, 109 million records of LUNA and UST transfers, and
162 million records of smart contract execution results (including 40 million records
of CW20 token transfers). Among these transactions, there are 5.4 million Anchor
transactions, 1.8 million native swap records, and 97 thousand bridge transfers from
Terra to Ethereum.

Our data cover 3.7 million addresses. Among them are 25 centralized exchanges
(CEXs), 864 trading pairs on 4 decentralized exchanges (DEXs), 10 inter-chain bridges,

9

58 DeFi protocols, 319 blockchain validators, 69 other entities including hedge funds
and venture capitals, 4,498 CW20 tokens, and 58,941 unnamed smart contracts.

2. Terra Network

In this section we lay out the evolution of the Terra blockchain and its main building
blocks. The architecture of Terra shared many features with other cryptocurrency
platforms such as Ethereum, which makes it an interesting object of study. Although
smaller than the Ethereum network, Terra’s smart contract platform enabled developers
to build a similar array of applications. The Terra blockchain was created with the
intention of supporting a decentralized ﬁnancial architecture with several key use cases,
ranging from borrowing and lending protocols to savings and trading applications. The
original network was named Terra but is currently referred to as TerraClassic. For ease
of reference, we continue to use the name Terra to describe the network.

The Terra network was developed by TerraForm Labs (TFL), a company started
by Do Kwon and Daniel Shin in 2018. TFL raised $32 million in seed capital from
a number of venture funds and some of the largest cryptocurrency exchanges such as
Binance and Huobi. In January 2019, TFL raised $62 million in an initial coin oﬀering
(ICO) by selling Terra’s native cryptocurrency, LUNA, at a price of $0.8 per LUNA.
The initial supply of LUNA was set to 1B, with seed and other investors receiving 188M
LUNA and TFL the rest. TFL used this initial allocation to provide block rewards to
validators and fund other projects.

The Terra blockchain was a proof-of-stake (PoS) blockchain built using the Cosmos’s
software development kit (SDK). In a PoS protocol, validators of transactions pledge
their coins, which can be forfeited if the validator fails to verify transactions promptly
or if their actions are found to be malicious. This process of pledging coins is known
as staking. Validators are rewarded with transaction fees and block rewards for their
services. Validators who stake a larger number of coins are more likely to be selected
to verify transactions and receive rewards. Users can delegate their coins to validators
and share the rewards with them.

The native token of the Terra network, LUNA, could be staked by users. Holders of
LUNA could delegate their tokens to validators of their choosing and receive rewards
in proportion to their stake. Staking LUNA also permitted holders to propose and vote
on governance proposals. One of the notable characteristics of the Terra blockchain was
that it provided a range of algorithmic stablecoins that were pegged to diﬀerent ﬁat
currencies. Among these stablecoins, TerraUSD (UST), pegged to the US Dollar, was
the most prominent. Unlike other major stablecoins such as Tether or Circle, which

10

were backed by oﬀ-chain liquid assets such as treasuries, UST was not supported by
oﬀ-chain collateral but by a smart contract that facilitated the exchange of one unit
of UST to $1 worth of LUNA and vice versa. Terra’s stablecoins became a distinctive
aspect of the Terra network. We describe them further in Section 2.1.

The applications on the blockchain beneﬁt from having a reliable stablecoin as a
medium of change and store of value, but they also drive the demand for the stablecoin.
Some of the more notable protocols built on the Terra network included (1) borrowing
and lending protocols like Anchor or Mars, (2) decentralized exchanges (DEX) such
as Astroport and Terraswap, (3) payment applications like Chai and Memepay, or (4)
the creation of synthetic assets that could track prices of stocks and other securities,
as in the Mirror protocol. One of the most widely used application on the Terra
platform was the Anchor protocol which provided lenders with a stable interest of
19.5%. We will describe its economics in more detail in Section 3.2. Another prominent
application on the Terra network was Chai, which was marketed as a mobile payment
app supported by the Terra blockchain. However, a recent SEC case against Terra
alleges that these payments were never processed on the blockchain and that Terra
fabricated fake transactions.8

The Terra blockchain also allowed for easy cross-chain transfers of assets, tokens
and data to other highly used blockchains. As a blockchain built on the Cosmos SDK,
it was interoperable with other blockchains built on the IBC (Inter-Blockchain Com-
munication) protocol.
In addition, Terra also facilitated interoperability with other
blockchain applications through the so-called bridges (a form of message passing pro-
tocol).9 Terra Shuttle bridge was the ﬁrst Ethereum bridge followed by the Wormhole
bridges that connected Terra with Solana, Ethereum, Binance Smart Chain, and oth-
ers. This interoperability became very important for Terra, since it allowed traders on
the Terra blockchain to access liquidity on DeFi apps on other blockchains, in partic-
ular the Curve protocol on Ethereum, which emerged as the DEX with the deepest
liquidity to trade an array of stablecoins including UST (in the UST/3CRV Curve meta
pool).10

In January 2022, Do Kwon announced the launch of the Luna Foundation Guard
(LFG) a non-proﬁt organization “to build reserves supporting the $/UST peg amid
volatile market condition”. This was prompted by concerns arising about price dislo-
cations of UST stemming from large trades or coordinated attacks on Curve and other

8See https://www.sec.gov/news/press-release/2023-32.
9These bridges operate as a decentralized, intermediary oracle network that observes and veriﬁes
messages on one chain (i.e., Terra) and relays them to the other chain (i.e., Ethereum). This solution
allows tokens to move between blockchains without relying on centralized exchanges.

10See https://resources.curve.fi/ for more detail.

11

DEX or centralized exchanges like Binance. LFG was overseen by a governing council
including several TFL co-founders and the lead investors. LFG originally raised $1 bil-
lion through the sale of LUNA tokens, with Jump Trading and Three Arrows Capital
as the lead investors. It set up a pool of exogenous reserve assets (mostly denominated
in BTC) to support the stability mechanism for the UST stablecoin, UST. Through a
series of further LUNA sales and transfers from Terraform Labs LFG built a signiﬁcant
reserve pool. The audit report by JS Held conducted after the crash conﬁrms that as of
May 6th 2022, LFG held about 80,300 BTC, USDT 26 million, and USDC 24 million,
as well as minor allotments in a few other coins.11

Figure 1 shows the timeline of the main Terra events. Terra went through several
protocol upgrades, the so-called forks in the crypto parlance. Early upgrades were
mostly concerned with tweaking protocol parameters. Columbus-4 launched on Oct 3,
2020, allowed users to write and upload smart contracts that led to a rapid growth of
DeFi protocols. Columbus-5 launched on September 30, 2021, improved the interoper-
ability of Terra with other networks and changed the economics of UST-LUNA swaps.
Prior to Columbus-5, when LUNA was swapped for UST, 5% of LUNA was burnt and
the rest was sent to the community pool. Funds from the community pool were used
to ﬁnance various community projects. Starting from Columbus-5, all LUNA swapped
for UST have been burnt.

[Fig. 1 About Here]

2.1. Terra stablecoins

Starting in March 2020 Terra introduced a suite of algorithmic stablecoins pegged
against diﬀerent ﬁat currencies, the most prominent being UST which was pegged
against the US Dollar.12 Unlike custodial stablecoins such as Tether and Circle, which
are backed by non-crypto assets, UST was backed by LUNA via a peg mechanism that
is meant to incentivize traders to engage in arbitrage whenever the stablecoin deviates
from the peg.

At the core of the peg mechanism is a native swap smart contract that allows users to
exchange, say $1 worth of a stablecoin, UST, for the dollar-equivalent amount of LUNA,
and vice versa. Thus, when UST is traded above $1, users could buy LUNA, swap
LUNA for UST, which amounts to burning (destroying) LUNA and mint (creating)
new UST, and sell UST at a premium above $1, pocketing the diﬀerence as proﬁt. In

11See https://lfg.sg/audit/LFG-Audit-2022-11-14.pdf for the audit report.
12Others included TerraCNY (Chinese yuan), TerraEUR (euro), TerraBGP (British pound), Ter-

raJPY (Japanese yen), or TerraKWR (South Korean won).

12

contrast, when UST trades below $1, users could buy UST, burn UST to mint new
LUNA, and then sell LUNA with a proﬁt.

The LUNA price, necessary for the native swap to work, is supplied by an oracle of
oﬀ-chain centralized exchanges every 30 seconds.13 To prevent oracle price manipula-
tion, the fees associated with the native swap are designed to increase with the volume.
Without swap fees, a user could have done the following. Sell LUNA on oﬀ-chain ex-
changes to temporarily depress the price of LUNA. Then use the native swap contract
to swap a large quantity of UST for LUNA at a lower LUNA price, buy LUNA on
oﬀ-chain exchanges to bid up the LUNA price, and ﬁnally use the native swap contract
to swap back a large quantity of LUNA for more UST.

The swap fees have been set so that the on-chain liquidity provided by the native
swap stays below the liquidity of the oﬀ-chain exchanges used by the oracle. The swap
fees have decreased over time as the liquidity of the oﬀ-chain exchanges increased.
Initially, the Terra protocol allowed swapping $400 thousand per day with a 2% spread,
with the spread increasing if the volume exceeds the daily limit. The daily limit was
increased to $20 million in Feb 2021 (Terra proposal 36). Following the May 2021
de-pegging event, proposal 90 was passed to increase the daily limit to $135 million
and decrease the spread to 0.5%, and then to increase the daily limit to $293 million
in Feb 2022 (Terra proposal 185).

2.2. Viability of Peg Mechanism

For the peg mechanism to work it has to be that (1) the price of LUNA supplied
by oracles is accurate, (2) arbitrageurs have incentives to defend the peg, and (3) any
negative feedback from converting UST to LUNA on the price of LUNA is limited. To
understand the last condition, notice that if a swap of UST for LUNA, which decreases
the supply of UST and increases the supply of LUNA is expected to lead to a signiﬁcant
decline in the LUNA price then any LUNA holder would be better oﬀ selling LUNA
ahead of the swap resulting in a run on LUNA.

When do we expect condition (3) to hold? First imagine a situation where the
supply of UST is negligible relative to the market cap of LUNA. Here converting UST
into LUNA will only lead to small changes in the aggregate LUNA supply and thus the
expected dilution should be minimal and it would be reasonable to expect condition
(3) to hold. Now lets imagine the case where the supply of UST is more signiﬁcant
relative to the market cap of LUNA. Here the situation is more complicated and it can
be useful to draw an analogy with warrants that give their owners the right to buy

13Blockchain oracles are services that provide smart contracts with external information. They

serve as bridges between blockchains and outside data.

13

company stock at a prespeciﬁed price. Similar to UST, which increases the supply of
LUNA if converted, warrants are dilutive — when investors exercise their warrant, they
receive newly issued stock. To the extent that exercising warrants does not change the
total value of the ﬁrm, it would be tempting to conclude the stock price should decline
following warrant exercise. However, if investors are rational and understand that
outstanding warrants are a claim on the ﬁrm’s value then the exercising of warrants
would not have any impact on the stock price. But the price would decline at the time
that the warrants are issued.

Similarly, if Terra investors are rational and understand that UST is a claim on
LUNA, swapping even large quantities UST for LUNA could have no eﬀect on the
LUNA price. However, if Terra investors price LUNA without fully taking into account
the dilutive nature of UST, swapping large quantities of UST for LUNA is likely to
have a large impact on the price of LUNA. In the latter scenario, the states of the
world where the market cap of UST is close to that of LUNA are expected to be fragile
and prone to a run on LUNA.

The above discussion raises an important question of the determinants of the value
of LUNA. First, by staking LUNA, one gets a claim to the transaction fees on Terra
and the rights to decide on the future development of the network. This makes it
possible to express the value of LUNA as the sum of the discounted future transaction
fees, see Kogan et al. (2021) for details. Second, LUNA also gives access to the services
oﬀered on the Terra network, which creates transaction demand and with it validation
fees. Finally, demand for LUNA can be the result of investors speculating on its value.
The demand for UST can be broken down to the interest rate it oﬀers and transac-
tion demand. With their value pegged, stablecoins serve as a natural choice of collateral
and benchmark asset in the crypto space. Being native to the Terra network, UST faced
no direct competition from other stablecoins on Terra. However, on other chains like
Ethereum, UST had to compete with stablecoins like Tether, USDC, or Dai.

In what follows, we present evidence that shows that the main factor behind the
demand for LUNA was speculative demand and for UST was the artiﬁcially inﬂated
interest rate on Anchor.

3. Terra Prior to the Run

We now analyze the transaction ﬂow on Terra and their underlying economics
prior to the run. Like other (payment) platform businesses Terra aimed to provide a
suite of services that draw in users and generate fees for the token holders. If more
users participate on the blockchain, it becomes more attractive for users to be on the

14

network and for developers to create additional applications on the platform, which
in turn attract more users and so on. If these network externalities are expected to
be strong, start ups in the tech or social media industry often subsidize customer
acquisitions initially to achieve critical mass, after which the marginal value of new
customers should turn positive to justify the investments.

We show that one of the main attractions on Terra was a borrowing and lending
protocol, Anchor, which provided heavily subsidized deposit rates and drew many users
to the platform. While it might have originally been intended as a way to generate
network externalities, our analysis shows that users on the platform did not start
utilizing other services extensively, and instead the subsidies on Anchor remained the
main attractor to Terra. While the level of subsidy was unsustainable, the complex
structure of the subsidies, might have made it diﬃcult for many network participants
to understand their origin.

3.1. Network Structure and Transaction Volume

In this section, we provide an analysis of transaction volumes on the Terra network
using on-chain data. We focus on the period starting with the Columbus-5 fork on
September 30, 2021 and ﬁnished before the crash, on May 6, 2022. Our goal is to
understand how diﬀerent tokens and smart contracts were used on the Terra network
prior to the crash.

To compute volume, we treat any single address as a separate entity unless we
have information that several addresses belong to the same entity. As a result, our
calculation of the network volume is likely to be biased upwards since some entities
might control several addresses. The situation is not as severe as in the case of the
Bitcoin network where as Makarov and Schoar (2021) show one entity can control ten
and more million addresses. Being a account-based network like Ethereum, Terra has a
much smaller number of addresses than Bitcoin network. A typical entity on the Terra
network usually controls one or only a few addresses.

Some smart contracts like Nexus often adjust a position by rebalancing the whole
position. For example, in the following sample transaction, Nexus smart contract
adjust the amount borrowed from Anchor from 16,226,512 UST to 16,227,559 UST by
ﬁrst repaying the outstanding balance and then borrowing the new amount.14 The
net eﬀect is an increase in the borrowed position by 1,047 UST. Computing volume
simply as the sum of the two transfers would grossly overstate the real volume on the

14See https://finder.terra.money/classic/tx/e874a1d3824854bbdb4f8743f18484fdc07361

bc62538b10369c8dc9fe7a3faf.

15

network. Therefore, in our volume calculation, we ﬁrst net token transfers between
any two addresses that happened at the same time.

The aggregate UST and LUNA volumes during the pre-crash period are $360 and
$217 billion, respectively. The tokens with the next two largest volumes are aUST
and bLUNA, at $114 and $50 billion. As we explain in the next section the volume
in these coins is closely related to transactions related to Anchor. For this reason, in
what follows we only focus on the UST and LUNA volumes. Table 1 reports the total
volume of transactions for each token in detail.

Figure 2 we now show the decomposition of the trading volumes for UST (left
panel) and LUNA (right) between diﬀerent addresses on the Terra blockchain. We
classify addresses into broad groups that are associated with the main participants on
the blockchain. In particular, “Admin” addresses denote those of network administra-
tion accounts and Terra insiders, including the community pool, Terra’s native swap,
addresses for transaction fees and LFG wallets. “TFL” addresses are those used to
issue new UST and to defend the peg. “Anchor” denotes addresses through which
transactions belonging to the Anchor protocol are conducted, such as its yield service,
money market transactions, staking accounts and other operations related to Anchor.
“Other” captures the accounts of regular users on Terra including retail individual
traders, hedge funds and large traders. CEX, DEX, and Bridges signify the wallets of
these entities. And DeFi captures smart contracts of entities that are not CEX, DEX
or Bridges, for example NFT market places or crowdfunding platforms. For a more
detailed description of the categories, see Appendix Table 7.

The size of the node reﬂects the total volume of the category. Similarly, the edge
size between nodes is proportional to the volume between the two categories. The
number next to an edge shows the corresponding volume. For clarity, we show only
categories with at least $10 billion of total volume in the UST network and $5 billion
in the LUNA network, and edges with at least $1 billion of volume.

The left panel shows that Anchor was by far the most important protocol in the
UST network accounting for 46% of the total network volume. The decomposition of
ﬂows on the network also shows that the next two categories, centralized exchanges
(CEX) and decentralized exchanges (DEX), together account for 26% of the volume.
All unlabeled addresses are assigned to the ‘Other’ category, which contains addresses
of individual users on the network. We also see that the largest ﬂow between nodes
is between Anchor and Other, again highlighting the importance of Anchor on the
network.

Similarly, in the right panel we map transactions on the LUNA network. In this
case, we observe that CEX, DEX, and addresses aﬃliated with TFL and Admin ac-

16

counts account for 84% of aggregate volume. This ﬁnding indicates that the majority of
transactions utilizing LUNA are associated with trading on exchanges, which reinforces
the notion that a signiﬁcant portion of the demand for LUNA stems from speculative
activities.

[Fig. 2 About Here]

3.2. Anchor

The previous section shows that Anchor was the main attraction in the Terra net-
work. Its design shares many characteristics with other decentralized lending platforms
such lending and borrowing are automated by smart contracts, similar to Aave or Com-
pound on Ethereum. However, as we show in this section, while Aave or Compound
lending rates are ﬁnanced by borrowing rates, both lending and borrowing on Anchor
were heavily subsidized by TFL.

3.2.1. Lending

We will now discuss the mechanics of the smart contracts underlying the Anchor
protocol. The Anchor contract aggregates stablecoin deposits with matching denomi-
nations into a pool, which is called markets. Borrows are proceeded from this pool, and
interest gained from them is equally shared among all the units of stablecoin deposits.
Deposits can be withdrawn anytime, unless every stablecoin in a market is borrowed.
When an address lends to Anchor, it transfers, say 100 UST to the Anchor UST
market address. The Anchor UST market contract mints (issues) the appropriate
amount of aUST, and transfers it to the depositor’s address. The aUST token is a
claim on UST stored in Anchor. It is freely tradable and transferable. The conversion
rate between aUST and UST is only a function of time with the interest rate on the
Anchor UST deposit being embedded in the aUST/UST conversion rate. When the
address wants to withdraw its UST from Anchor, it sends aUST tokens back to the
Anchor UST market contract, which burns (destroys) the aUST and returns UST
along with interest. The interest on each aUST token is the diﬀerence between the
aUST/UST conversion rates at the time of the deposit versus withdrawal. The rate
was 1 when Anchor was launched in March 2021 and was 1.213 one year later in March
2022.

3.2.2. Borrowing

Borrowing on Anchor is over-collateralized. For the period we consider, Anchor
allowed two types of collateral, bLUNA and bETH. These types of bAssets are liquid,

17

tokenized representations of staked (bonded) assets in a PoS blockchain. Since the
native token in a PoS blockchain can be staked to earn a reward, it is more eﬃcient to
hold staked LUNA or ETH as collateral rather than their unstaked counterparts. The
main obstacle with using staked tokens as collateral is their illiquidity — staked tokens
can be unstaked only with a delay because the Terra network has a lockup period of
21 days.

The built-in delay serves an important function in a PoS protocol of providing val-
idators and delegators with proper incentives to verify transactions on the blockchain.
But by restricting the timely access to the token, the built-in delay reduces its collateral
value. One solution that emerged to the above problem, is to introduce a derivative
contract, which is a claim on the staked tokens and which can be freely traded in the
market. This was implemented by the Lido Liquid Staking Protocol in the form of
bAssets.15

When an address borrows UST from the Anchor UST market, it ﬁrst sends bLUNA
(bETH) as collateral to the Anchor bLUNA (bETH) Custody Contract, which then
records the address and the amount of collateral provided. The borrowing limit depends
on the value of the collateral and cannot exceed the maximum allowed loan-to-value
(LTV) ratio. The maximum LTV for bLUNA was initially set to 50%, then raised to
60% in July 2021, and to 80% in Feb 2022. Smilarly the LTV for bETH was raised
to 75% at the peak. Naturally, the borrowing limit ﬂuctuates with the oracle-reported
bAsset price. When the borrowing limit exceeds the maximum LTV the loan gets
liquidated. Liquidation is implemented via what is called a Liquidation Queue, where
liquidators bid in a ﬁrst-price auction for the right to liquidate the collateral and repay
the loan.

3.2.3. Anchor Rates

The Anchor lending rate was primarily a function of two main rates, target deposit
rate and threshold deposit rate.16 The target deposit rate, known as the Anchor rate,
was the rate, which the protocol attempts to achieve from the interest gained from the
borrowers. The threshold deposit rate served as a ﬂoor to the deposit rate triggering
a direct deposit rate subsidy from the yield reserve pool of Terra if the current deposit
rate is below this value.

When Anchor was originally launched, the Target Deposit Rate and the Threshold

15The Lido Protocol also allowed a second set of derivative contracts called stAssets. The diﬀerences
are not important for our purpose, but details can be found in Lido Terra Docs at https://docs.t
erra.lido.fi/introduction/tokens.

16https://docs.anchorprotocol.com/anchor-2/protocol/anchor-governance/modify-marke

t-parameters.

18

Deposit Rate were set at 20% and 18%, respectively, and later changed to 20.5% and
19.5%. Following widespread discussions that the 20% Anchor rate is unsustainable,
there was a series of proposal starting in March 2022 to lower the Anchor deposit rate.
Eventually, Anchor Proposition 20 was passed on March 23 and implemented on May
1st, 2022, which tied the deposit rate to the change in the yield reserve over a one
If the yield reserve is growing, the deposit rate would increase and
month period.
vice versa if the yield reserve is falling. The maximum amount the deposit rate could
change per month was set to 1.5%.17

On the other side of the Anchor platform, the annualized borrowing rate was an
increasing function of the proportion of outstanding loans to outstanding deposits and
given by the following formula:

2% + 42% ×

outstanding loans
outstanding deposits

and was adjusted every three hours.

Figure 3 shows the Anchor lending and borrowing rates from April 2021 when
Anchor was launched until the beginning of the crash on May 7, 2022. We can see
that the lending rate had been consistently around 20%. Comparing the lending and
borrowing rates shown in Figure 3, one can also see that the borrowing rate was often
below the lending rate. But this simple comparison does not reﬂect the full cost to a
borrower, since the borrowing rate does not include the opportunity cost of losing the
staking yield on the collateral that was required to borrow from Anchor.

[Fig. 3 About Here]

The LUNA staking yield comes from two main sources: (1) block rewards and
(2) airdrops. Block rewards are the sum of swap fees and gas fees, minus validator
commissions. Airdrops, a practice of giving away tokens to active members of the
blockchain community, is a popular marketing strategy in the crypto space to reward
participants and promote awareness of new tokens.

LUNA delegators received three main airdrops — ANC (Anchor native token),
MIR (Mirror native token), and MINE (Pylon native token). To compute the resulting
staking yield, we assume that delegators claim all available airdrops of the three tracked
tokens every week and sell them over that week for LUNA. Figure 4 left panel shows
the LUNA staking yield by source. Through most of 2021 LUNA block rewards were
stable but constituted less than 50% of the rewards from staking. The other half of
the rewards to staking came from the airdrops. The burning of LUNA for UST in

17https://twitter.com/anchor protocol/status/1507052921745256449?lang=en-GB.

19

the community pool in November 2021, which we describe in Section 3.2.4, lead to a
signiﬁcant increase in LUNA staking yield.

[Fig. 4 About Here]

To compensate borrowers for the opportunity cost of collateral, Anchor imple-
mented a subsidy scheme which distributed Anchor native token ANC to borrowers.
Anchor initially sent 87,000 ANC to all borrowers per day in proportion to their loan
balance. But following the May 2021 LUNA crash (see Section 5 for more detail) that
lead to a large number of liquidations over a span of four days and sharp decline in bor-
rowing activity, the rate was dynamically adjusted at 50% per week until it reached the
upper limit of 260,000 ANC per day on June 8 2021, and stayed at this level thereafter.
The right panel of Figure 4 shows the annualized ANC subsidy rate, where we
assume that borrows sell the daily ANC incentive at the market price. The subsidy
rate was as high as 300% when it was ﬁrst introduced. It led to a sharp rise in lending.
As more investors borrowed from Anchor, the subsidy rate declined slightly in May
2021, but still was around 80%. After the mini crash in May 2021, it increased again,
and then slowly decreased as borrowing activity recovered.

Figure 5 shows the net borrowing rate. To compute it, we assume that the borrower
takes a loan with the maximum LTV. This would be the case if users use intermediary
protocols like Nexus that are designed to be as eﬃcient as possible by constantly mon-
itoring the LTV and making sure that it stays below the level that triggers liquidation.
Standalone users typically choose lower LTVs. For these users, the opportunity cost of
borrowing are higher.

[Fig. 5 About Here]

Figure 5 reveals a striking fact that the net borrowing rate on Anchor has been
below the lending rate at all times. In other words, Anchor was never self-sustaining
but relied from signiﬁcant subsidies from TFL. This imbalance was primarily driven
by the deposit rate on Anchor having been set exogenously and artiﬁcially high. Early
on, the high deposit rate might have been intended as a marketing tool to attract
users to the Terra ecosystem. But our analysis suggests that these users did not start
generating more fees over time to support the high deposit rate.

In fact, many users took advantage of the low net borrowing rate by borrowing
funds from Anchor and immediately posting them back. We call these exploiting
loans. Figure 5 shows the share of exploiting loans among all loans. We can see that
the share of exploiting loans varies inversely with the diﬀerence between the lending
and the net borrowing rates, with the lowest value being 20% and often being as high

20

as 60%. In other words, participants engaged in exploiting loans more heavily when
the gains from this activity were greater.

3.2.4. Anchor Balance

The highly subsidized Anchor rates were very high even by the crypto standards.
Figure 6 shows the average lending rates on thee major stablecoins, USDT, USDC, and
DAI on Aave and Compound platforms, which are the main borrowing and lending
market places in the Ethereum network. We can see that the Aave and Compound
rates were around 2-3% in Jan-May 2022, which stand in stark contrast to the 20%
Anchor rate.

[Fig. 6 About Here]

Not surprisingly, the high Anchor rates were one of the main drivers for the demand
for UST and the Terra network in general. The left panel of Figure 7 plots the number
of new addresses on Terra each day from April 2021 until the crash in May 2022.
The lowest (blue) line of the graph indicates the number of addresses that start using
Anchor from the ﬁrst day that they are on the Terra blockchain. We interpret this as
a sign that the main attraction for these users was the opportunity to gain access to
the subsidized borrowing and lending rates on Anchor. The next lines plot users who
started using Anchor within a week, within a month, and more than a month to use
Anchor, and those that never used Anchor. These users are increasingly less likely to be
participating on Terra only for the yield on Anchor but might have a broader interest
in the ecosystem. The right panel shows the share of each group that eventually used
Anchor.

[Fig. 7 About Here]

Figure 7 shows that the number of new addresses on Terra and those that use
Anchor have been growing over time and that the majority of addresses that ever use
Anchor do so on their ﬁrst day. This dynamic supports the hypothesis that from the
date of its creation, Anchor has been one of the main attractions for new users on Terra
and the source of demand for UST.

In response to the increasing demand for UST, TFL signiﬁcantly expanded UST
supply. Figure 8 shows the aggregate supply of UST broken down by entities that
swapped LUNA for UST. The entities include TFL and Admin addresses, Anchor,
Bridges, CEX, DEX, and UST and LUNA locked in other DeFi protocols. The category
‘Other’ includes user accounts that are not part of the above categories.

21

[Fig. 8 About Here]

Recall that swapping LUNA for UST is the only way to create new UST. The top
panel of Figure 9 shows the daily amounts of UST and LUNA swapped along with the
cumulative net UST supply. The net volume is computed according to the following
formula: swap amount + fee amount - oﬀer amount, where swap amount + fee amount
are from LUNA for UST swaps and oﬀer amount is from UST for LUNA swaps. The
bottom panel shows the UST dollar price. We can see that except for May 19-25 and
January 27 when UST lost its peg, the volume of LUNA being swapped into UST
signiﬁcantly exceeds that of UST for LUNA swaps.

[Fig. 9 About Here]

The ﬁrst large increase in the supply of UST occurred in February–March 2021 when
the launch of Mirror protocol created a large increase in the demand for UST that led
to the UST price to be signiﬁcantly above $1. Because of the peg mechanism, these
large deviations presented arbitrage opportunities and led to LUNA being swapped for
UST. After March 2021, the supply of UST stayed around 2-2.5 billion until the next
fork, the Columbus-5 upgrade.

The Columbus-5 upgrade introduced an important change in the economics of the
Terra network. Prior to Columbus-5, only ﬁve percent of LUNA was burnt (destroyed)
and the rest was sent to the community pool. Starting from Columbus-5, all LUNA
swapped for UST were burnt. Terra Proposals 133 and 134 introduced by Terra founder
Do Kwon and passed on November 10, 2021, directed that the 88.675 million Pre-
Columbus-5 LUNA accumulated in the community pool should be swapped for UST.
The immediate eﬀect was a sharp increase in the supply of UST from 2.5 billion to 6.5
billion (which was placed in Admin accounts). The burning of the community pool also
had important implications for the LUNA staking yield. Figure 9 shows that burning
the community pool happened within a few days with volumes that far exceeded the
daily swap limit of $135 million set at that time. As a result, these swaps incurred very
large swap fees of 30% that were used to increase the LUNA staking yield to 10%, see
Figure 4.

The supply of UST continued to increase and reached 18.5 billion by the time of
the May 2022 crash. Figure 8 reveals that the majority of newly created UST ended
up in the Anchor protocol. Right before the crash, Anchor held around 12 billion UST
and the community account held another 3 billion.

The LUNA for UST swap fees after the burning of the community pool stayed
around 1%. Figure 9 bottom panel shows that while the UST price was consistently

22

above $1 during that period, the deviations were modest, typically within 25-50bp,
which precluded any trading gains from swapping LUNA to UST.

This raises a questions of who was swapping LUNA for UST. Table 4 documents the
top 26 addresses that swapped the highest amount of LUNA to UST. These addresses
swapped 90% of the aggregate volume of swaps of LUNA into UST. Table 4 shows that
except for the addresses of Terraswap route and Jump trading, the top 26 addresses
are all controlled by TFL.

3.2.5. Concentration of the Anchor Holdings

Considering the substantial amount of UST that was locked in the Anchor proto-
col, it is important to understand the concentration of Anchor deposits. The more
concentrated the funds on Anchor, the greater could be the potential impact could be
from a single large participant moving funds from Anchor and exiting Terra.

The left panel of Figure 10 plots the percentage of deposits that the top 10, 100 and
1000 users constitute on Anchor on a given day, we ﬁlter out intermediary addresses
fomr this analysis. We can see that the holdings were highly concentrated. Starting
from January 2022, the top 10 addresses controlled between 15% and 20%, the top
100 addresses between 30% and 40%, and the top 1000 addresses around 60%. These
numbers are similar to the concentration of bitcoin holdings and substantially higher
than the concentration of wealth among the US households, see Makarov and Schoar
(2021).

The right panel of Figure 10 shows the histogram of non-intermediary address
balances on May 6, 2022. Among the total 160 thousand addresses, there are 109
addresses with the balance above 10 million UST with the aggregate balance of 5 billion
UST, 1230 addresses with the balance between 1 and 10 million UST and the aggregate
balance of 3 billion UST, 10,397 addresses with the balance between 100 thousand and
1 million UST and the aggregate balance of 2.7 billion UST, 40,688 addresses with
the balance between 10 thousand and 100 thousand UST and the aggregate balance
of 1.3 billion UST, and 63,360 addresses with the balance between 1 thousand and 10
thousand UST and the aggregate balance of 236 million UST.

[Fig. 10 About Here]

3.2.6. Anchor Accounting

We now show what subsidy rates mean for the daily cashﬂows of the Anchor proto-
col. Figure 11 shows the cumulative Anchor inﬂows and outﬂows. The inﬂows include
the interests on the outstanding loans (blue line), the staking rewards produced by the

23

staked collateral LUNA (red line) or ETH (yellow line), and proportional fees charged
on the liquidated loans (green line). The outﬂows include the interests paid to de-
positors (gray line), and the buyback of ANC tokens from the Astroport DEX (teal
line). The solid black line shows that net cash ﬂows. We can see that starting from
December 2021 the outﬂows vastly outpaced inﬂows. The diﬀerence was made up by
the Anchor’s yield reserve. The yield reserve makes up the diﬀerence when the cash
ﬂow is negative and receives the overhead when the net cash ﬂow is positive.

The right panel of Figure 11 shows the balance of Anchor’s yield reserve. Since the
Anchor protocol was not self-sustaining, i.e. borrowing rates were not above lending
rates, the yield reserve was depleting most of the time. As a result, TFL had to top
up the balance of the yield reserve several times. the TFL ﬁrst injected $71 million in
July 2021 and LFG injected $510 million UST in Feb 2022 to the yield reserve. Both
injections were funded by swapping LUNA for UST.

[Fig. 11 About Here]

3.2.7. Anchor Governance

Like many other protocols on Terra, Anchor was set up as a decentralized au-
tonomous organization (DAO) with its own native governance token, ANC. Holders of
ANC could stake their tokens to vote or propose changes to the protocol, and their
voting power was proportional to the amount of ANC staked in the vote. ANC tokens
were designed to capture a portion of Anchor’s yield, scaling up linearly with the assets
under management.

However, this design generated a misalignment in objectives between ANC and
LUNA token holders. Maintaining a high and subsidized deposit rate on Anchor ben-
eﬁted ANC holders by driving demand to ANC, increasing assets under management,
and with it, the fees going to ANC holders. But as noted earlier, this also contributed
to the risks building up in the system and reduced the going concern of LUNA. ANC
holders did not fully internalize the negative impact on the survival of the system. This
misalignment became more pronounced when ANC holders had to decide whether to
reduce the subsidized deposit rate and bring it in line with the fees generated from bor-
rowing. This example illustrates one of the potential ineﬃciencies arising in a decen-
tralized governance system, where it becomes more challenging to reconcile competing
objectives between diﬀerent parts of the ecosystem. For a more detailed discussion of
DAOs and DeFi applications, see for example Makarov and Schoar (2022).

24

3.2.8. Anchor Entry and Exit Rates

Finally, we analyze how the participation of depositors and borrowers on Anchor
evolved over time. Our goal is to understand what factors aﬀected the growth of
Anchor. Figure 12 plots the number of depositors that enter or exit Anchor as a fraction
of the existing depositors on the previous day. The graph highlights that the depositor
inﬂow was very high originally when Anchor was introduced in March 2021. We also
see that periods of price increases of LUNA seem to be accompanied by more deposits
on Anchor. We also observe the sharp spike in entry rates in November 2021, which
is due to TFL minting lots of UST as discussed above. Similarly we see that the exit
rate spiked around the two prior de-pegging events in May 19-25 2021 and January 27,
2022. But exit rates dropped again after each of these events, and entry resumed, once
the peg was reestablished and market participants became more comfortable again.
Finally, we see that starting in April 2022, exit rates started accelerating and entry
dropped sharply. We interpret this dynamic as an indication that some traders started
having concerns about the sustainability of Anchor rates.

[Fig. 12 About Here]

4. LUNA and UST Run

While we cannot say with certainty whether the run on UST was inevitable, our
analysis shows a pattern of events that closely resembles models of runs which highlight
the interaction of worsening fundamentals and strategic behavior by traders, such as
Morris and Shin (1998) or Goldstein and Pauzner (2005) and Goldstein (2013), Abreu
and Brunnermeier (2003). In these models agents receive private and public signals
about the strength of fundamentals. A common public signal acts as an additional
coordination device for agents’ actions. In the context of cryptocurrencies, since actions
of the agents on the blockchain are observable, agents can also monitor each others
actions and react to them.

Our analysis above documents a set of worsening fundamentals of the network over
the ﬁrst few months of 2022, which investors could have observed. These include the
balance of the Anchor yield reserve dropping as the subsidies to Anchor were becoming
increasingly harder to sustain, as well as the price of LUNA declining in line with a
general drop in cryptocurrency prices which reduced the relative market valuation of
LUNA versus UST outstanding. We show that already in April 2022, some investors
seem to have become concerned about the health of the network as evidenced by a
sharp decline in the entry rate an increase in the exit rate from Anchor.

25

Following a general decline in cryptocurrency prices the gap between the market
cap of LUNA and UST had been shrinking since mid-April. On May 7, the gap was
around $4 billion, as shown in Figure 13. It closed completely in the evening of May 9
and coincided with the time when the UST price plummeted to $0.75. As we discussed
in Section 4, if investors were fully rational and took into account the dilutive eﬀect of
UST on LUNA the crossing point would not necessarily play a signiﬁcant role for the
valuation of LUNA. However, if investors priced LUNA independently from UST and
the conversion of UST to LUNA has a negative eﬀect on the LUNA price, the crossing
point could serve as a salient synchronization event. The synchronization between the
market cap of LUNA and UST equalizing and the drop in the price of UST suggests that
it might have been another coordinating event for holders of UST. The discussions on
many social media sites indicate that many market participants viewed LUNA pricing
largely independent from the outstanding supply of UST. In their mind, the moment
the market capitalization of LUNA and UST crossed, is a signal that there was not
enough value in the LUNA network to support the value of all the UST outstanding.

[Fig. 13 About Here]

Finally, the beginning of the run coincided with the re-balancing of the UST-3Crv
pool, since TFL was planning to establish a new liquidity pool on Curve involving a
diﬀerent set of stable coins. While the re-balancing of the Curve pool is not an adverse
event, when fundamentals are weak, even an apparently innocuous event could serve as
a coordinating event for the run. All these were warning signs that should have made
market participants start paying attention to mounting risks on Terra.

4.1. The Timing of the Run

The ﬁrst signs of the run appeared on May 7, 2022, as has been reported in several
industry reports and on social media.18 On that day, two addresses dubbed wallet A
and B withdrew 400M UST from Anchor.19 The withdrawals were made in batches
and sent to Curve and Binance, which were the most liquid UST DEX and CEX
exchanges, respectively. The top two panels of Figure 14 show the exact timing of
these withdrawals. Wallet A was the ﬁrst to withdraw 45M UST around 5am UTC
and it sent the funds to Binance. Following this event, wallet B withdrew 175M UST
around noon and sent the funds to Ethereum using the Wormhole bridge, but did not

18See for example, an insightful report by Nansen at https://www.nansen.ai/research/on-chai

n-forensics-demystifying-terrausd-de-peg.

19The wallets A and B allegedly belong to Jane Street and Celsius, see https://twitter.com/Fr

ankResearcher/status/1630545591397670916.

26

make any trades at that time. Next, wallet A withdrew another 35M around 5pm,
and then another 20M around 8:30pm and 9:30pm, again sending all the funds to
Binance. Finally, at 21:48pm wallet A withdrew the last 85M and send them to Curve.
The bottom panel of Figure 14 shows the timing of all other Anchor deposits and
withdrawals on May 7. The deposits are colored in green and withdrawals in red. We
can see that starting from 12pm other large wallets started moving out of Anchor.

[Fig. 14 About Here]

Concurrent with an increase in Anchor withdrawals, the UST price on both Curve
and Binance began falling. The top panel of Figure 15 shows the swap transactions
price of UST against three major stablecoins, USDT, USDC, and DAI on May 7, 2022.
Swap transactions of UST into the other three stablecoins are colored in red, and swaps
into UST in green. The y-scale is logarithmic. The bottom panel of Figure 15 shows
the net signed volume and the deviation of the UST price from $1 in basis points.

Figure 15 highlight that during the day on May 7, swapping out of UST intensiﬁed,
leading to a gradual increase in the UST discount. The selling activity increased sharply
after 21:44pm, which is marked by the dashed gray line and corresponds to the moment
when TFL removed 150M UST from the UST-3Crv pool to send it to a new UST-4Crv
pool. This was a preplanned transition, since the new pool was supposed to go live on
Ethereum the week after. Terra together with FRAX, another algorithmic stablecoin
that was growing at the time, aimed to set up a separate Curve pool to create more
liquidity and generate higher yields for their stablecoins.

Note that the withdrawal of 150M UST from the UST-3Crv by itself is not an
adverse event for investors who are worried about the convertibility of UST into other
stablecoins because the amount of other stablecoins available to withdraw remains
unchanged. In fact, the removal of UST increases the UST price vis-a-vis other stable-
coins because it decreases the supply of UST relative to the supply of other stablecoins,
which is reﬂected in the small decrease in the UST discount immediately following the
event.

The withdrawal of 150M UST by TFL was followed as we describe above by wallet
A withdrawing 85M UST from Anchor and selling the whole amount on Curve in one
transaction. The immediate eﬀect of this trade was a widening of the UST discount to
80bp. This event was succeeded by a ﬂood of other large sales, in particular a trade
by wallet B, which sold 150M UST transferred to Ethereum earlier that day.
It is
interesting that while wallet B seemingly prepared for a possible sale earlier that day,
it only started actively selling its UST once other large traders started exiting and the
price dropped. As a result, the UST discount on Curve reached 250bp. In response,

27

TFL Curve bots started actively trading in an attempt to restore the peg. We see that
they partially succeeded by reducing the UST discount to 50bp for the rest of the day
on May 7.

[Fig. 15 About Here]

The UST discount on Curve was mirrored by that on Binance. The top panel of
Figure 16 shows the UST/USDT trades. Sell-initiated trades are marked in red and
buy-initiated ones in green. The y-scale is logarithmic. Similar to the Curve graph, the
bottom panel shows the net signed volume and the deviation of the UST price from $1
in basis points.

Comparing trades on Curve and Binance we can see that there were many more
trades on Binance, but they were smaller in size. Because of Curve’s pricing mechanism
large orders have smaller price impact on Curve than on Binance and therefore Curve
attracted larger traders. Another reason for the smaller trade size might be that
there were more retail investors on Binance, who usually trade in smaller quantities.
Interestingly, while the UST discounts on both exchanges were highly correlated, the
signed volume moved in the opposite direction. The cumulative net selling volume
on Curve was around 200M UST. This in in contrast to the net buying volume of
200M UST on Binance. Thus, the UST price and signed volume moved in the opposite
direction on Binance on May 7, which is contrary to what is normally observed in
many markets.20 This negative relation could realize, if sellers on Binance placed large
limit orders at the current price, which has been ﬁlled by buy market orders. The buy
market orders could have come either from “noise traders” who tried to “buy the dip”,
or from parties like TFL that tried to defend the peg.

[Fig. 16 About Here]

Finally, Figure 17 plots the evolution of the aggregate hourly balance of total de-
posits on Anchor and the price of UST in the week after May 7. It shows that investors
continued to withdraw funds from Anchor, but the UST price remained close to $1 un-
til the evening of May 9th. During that time, TFL and LFG tried to defend the peg
by a series of actions aimed at buying UST and support the price. The LFG audit
report documents that during this period TFL and LFG spent a total of about $2.5
billion (80,071BTC, 26,281,671USDT, and 23,555,590 USDC) on purchases of UST and
LUNA.21 Late on May 9, the withdrawals from Anchor accelerated and the UST price

20See for example, Evans and Lyons (2002), Chordia et al. (2002), Hasbrouck (1995) or Hendershott

and Menkveld (2014) or for crypto markets see Makarov and Schoar (2020)

21See the Audit Report by JS Heldt, Analysis – Terraform Labs’ and Luna Foundation Guard’s

Defense of the UST Price Peg, November 2022.

28

dropped precipitously to $0.75. It hovered between $0.2 and $0.9 for a few days before
completely imploding. By the end of May 13, less than 2B UST remained on Anchor
and the UST price fell below $0.2.

[Fig. 17 About Here]

4.2. Swapping of UST and LUNA

The UST peg design added an additional dimension to the investors’ strategy space.
Whenever the price of UST falls below $1, investors who no longer wish to hold it could
follow two main strategies. They could either (1) sell UST at the market price or (2)
could swap UST for LUNA for its nominal value and then sell LUNA at the market
price. In the absence of frictions, the second option would deliver them strictly higher
proﬁts, which increases with the size of the UST discount.

In practice, investors faced several frictions. First, as discussed in Section 2.2, to
prevent oracle price manipulation the native swap contract had built-in fees that were
designed to increase with the volume. Second, trades in both the LUNA and UST
markets were subject to price impact — a co-movement of prices in the direction of
trades. Finally, there could be a delay between the time investors send their funds
to an exchange and the time their funds are cleared for trading. This delay becomes
especially important if investors anticipate that other investors will sell their LUNA
holdings, which would result in a predictable decline in the future price of LUNA.

Figure 18 documents the trading activity in the native swap market from May 7,
2022 to May 13, 2022, when the convertibility between UST and LUNA got suspended.
The top panel plots the UST discount and the swap fees over time. The middle panel
shows the diﬀerence between the UST discount and the swap fees that measures the
attractiveness of swapping UST for LUNA over selling UST at the market price. The
diﬀerence can also be thought as an arbitrage spread from buying UST at the market
price, swapping it for LUNA, and selling LUNA at the market price. Finally, the
bottom panel shows the dollar amount of UST that were swapped in a given minute.

[Fig. 18 About Here]

Figure 18 shows that the UST discount, the swap fees, and swap volume closely
followed each other. As the UST discount widened investors found it increasingly more
proﬁtable to swap UST for LUNA and engage in the UST-LUNA arbitrage. In the
May 7–13 period, users swapped 7.42 billion UST worth $4.65 billion.

Table 5 shows the top 20 addresses that swapped the largest amount of UST over
the run period. The largest amounts were swapped by two unknown smart contracts

29

that arbitraged the relative price of UST and LUNA between Terra’s main DEX,
Astroport and the native swap contract. Alameda Research, a cryptocurrency trading
ﬁrm co-founded by Sam Bankman-Fried and closely linked to FTX exchange, swapped
the third largest amount. The case of Alameda Research is interesting because most
of the top addresses did not have exposure to Anchor and used swaps to perform the
UST-LUNA arbitrage. We estimate that out of 12 UST billion Anchor balances at
most 700 million UST were routed to the native swap with the majority of funds sent
to CEXs and DEXs. Out of the top 20 addresses in Table 5, only Alameda Research
and terra1. . . 4c2t held a balance on Anchor (311M and 73M UST, respectively). It
seems that the swap fees and uncertainty about the execution price of LUNA on CEXs
prevented most market participants from using the native swap contract as an escape
rout. But Alameda Research with its favorable access to the FTX exchange had an
advantage over other players and appears to have exploited it.

Figure 19 shows that as users swapped UST for LUNA, the price of LUNA precipi-
tously declined leading to a situation where the ever increasing amounts of LUNA were
swapped in exchange for UST. From May 11 to May 13, the LUNA supply increased
from less than 1 billion to 5.89 trillion, while the price of LUNA dropped from $50 to
$10−6. In economic terms, the falling price of LUNA meant that investors running from
UST into LUNA created increasing dilution and with it further depressed the price of
LUNA, which led to a dramatic “death spiral.”

[Fig. 19 About Here]

The enormous increase in the LUNA supply also had important implications for
Terra’s governance. Since Terra uses a system of one LUNA-one vote, owners of newly
issued LUNA de facto obtained control over the Terra network as they were diluting the
positions of existing holder of LUNA. To defend its dominant position in the network,
TFL swapped a large amount of UST for LUNA.

4.3. How Did Investors Run?

We ﬁnally study how investors ran and the magnitude of the losses they experienced
at the end of the run. Since one of the main premises of Terra and permissionless
blockchains more generally is the equal access and democratization of ﬁnance, we want
to evaluate how diﬀerent types of investors were able to exit through the run. An
important advantage of the observability of transactions on the blockchain is that we
can observe the transactions of individual investors over time. This information allows
us to infer investors characteristics such as wealth and sophistication. We can build
a proxy for investor wealth, since we observe the balance of each address prior to the

30

run. To sort investors according to their sophistication, we assume that the usage of
complex protocols (such as bridges) or complex strategies (such as using multiple CEX
and DEX) are signs of investor sophistication.

We ﬁrst analyze withdrawals from Anchor broken out by the size of the deposit
balance of addresses before the run, as of May 6th. We drop from the sample any
addresses held by intermediaries or large institutions and focus on individual addresses.
We also remove addresses with less than 100 UST in Anchor. Figure 20 shows a
stark gradation by size, with the largest addresses running ﬁrst and the smaller groups
lagging. The largest group, addresses with more than 10 million UST, withdrew their
funds on average much earlier and more decisively, so by the end of May 12 that group
In contrast, addresses with 1,000 to
had withdrawn almost 100% of their balance.
10,000 UST started running almost two days later and by the end of May 12 still had
about 50% of their balance still on Anchor. In fact, the smallest category, addresses
with below 1,000 UST on average kept adding deposits to Anchor until May 10th, after
which date they also started decreasing their balances. But by May 11 they still had
about 80% of their pre-run balances on Anchor.

[Fig. 20 About Here]

The total loss that diﬀerent depositors encountered not only depends on the speed
with which people ran but also how decisively they exited their holding. We see that
some people even added deposits during the early part of the run, maybe in a misun-
derstood attempt to “buy the dip”.

To calculate the total loss for each address we adopt the following strategy. We
calculate the USD value of each address’ token portfolio at the start of May 6 and
mark it to market. The portfolio covers UST, LUNA, aUST, bLUNA, bETH, and
ANC holdings. Then we calculate the USD value of inﬂows and outﬂows of these ﬁve
tokens over the days of the run, where we again mark every token transfer to market.
Since some addresses have token holdings outside of the Terra blockchain, such as
Ethereum bridges or CEX, we also regard any inﬂows before the ﬁrst outﬂow as part
of the initial balance, which we call the balance adjustment. Finally, we calculate the
ending balance at the end of May 13 and again mark it to market. We compute the
loss as:

(cid:18)

loss =

1 −

post-run USD balance + USD outﬂow − USD inﬂow + adjustment
pre-run USD balance + adjustment

(cid:19)

×100%

(1)

31

Since we do not have reliable price data for some of the minor tokens, there are a
small number of addresses that have outliers in the losses. We winsorize the losses at
the 0.5th and the 99.5th percentiles.

We ﬁrst tabulate the average size of the loss by the pre-run size of the address in
Table 2. Losses decrease monotonically in size, with the addresses above 10 million
experiencing a 26% loss and the addresses above 1 million experiencing a 32% loss. In
contrast the smallest addresses with below 10,000 UST or even below 1,000 UST lost
an average of 60% and 76%, respectively.

Since size might be correlated with other characteristics, especially ﬁnancial sophis-
tication, we now analyze the percentage loss of an address as a function of size, ﬁnancial
sophistication, and the age of the address. Age is measured as the months since the
address was established. As discussed before, participants can set up new addresses if
they choose to. Therefore, the measure of age is probably a lower bound on the true
age of a participant. Some older participants might have set up new addresses which
means we might have attenuation in the age measure. Our measures of sophistication
are derived from observed prior transactions on the blockchain. In particular, we con-
struct (1) a measure of how many diﬀerent CEXs the address had used as a proxy for
arbitrage trading, (2) a dummy for whether the address had ever used a bridge, like
Wormhole or Shuttle, to move assets across blockchains, and ﬁnally (3) we measure
the trading activity as the volume of token inﬂows in US dollars divided by the token
balance in US dollars before the run.

Table 3 Column (1) shows the results from a multivariate regression of the percent-
age loss of an address over the period from May 6 to the end of May 13 on log size,
log age in months plus one on Terra, and our measures of sophistication. Column (2)
repeats the same regression but uses dummies for diﬀerent size bins instead of continu-
ous variable of log size. As in the descriptive statistics, there is a strongly negative and
signiﬁcant relationship between the balance at the beginning of the run and the loss
an address experienced. Columns (2) shows that the largest addresses with balances
above $10M had a 45% smaller loss compared to the smallest addresses with balances
below $1K.

Column (2) also shows the variation in losses that is explained by our measures
of ﬁnancial sophistication controlling for size. The ratio of trading volume divided by
the balance, the number of CEX used by an address and whether it ever used bridges
In contrast, log
have a large and signiﬁcant relation with the loss during the run.
age has a positive and signiﬁcant relationship with losses. While age of an address
is only a noisy proxy for whether the owner of the address is new to Terra Luna, it
suggests that older addresses might have been more willing to believe in the stability

32

of the system. This might be a reﬂection that their owners are more committed to the
ecosystem overall and thus did not want to destabilize it or they experienced the ﬁrst
crash in May 2021 and thus felt that they had seen stability in the system. But the
fact that the estimated coeﬃcient is positive on age also suggests that experience alone
is not the reason why some depositors fair better during the run. In other words, our
measures of sophistication appears to be distinct from just experience with Anchor or
the Terra ecosystem.

In Columns (3) to (8), we now analyze if the importance of sophistication measures
varies across the size distribution. For this purpose, we repeat the same speciﬁcation
but we break out addresses by the size of the balance before the run started. We use the
following size bins in UST: below 1,000, 1,000 – 10 thousand, 10 – 100 thousand, 100
thousand – 1 million, 1 – 10 million, and above 10 million UST. We see that across the
size distribution, addresses which score higher on sophistication as measure by the use of
bridges, a larger number of centralized exchanges or a higher fraction of trading volume
to balance, experienced smaller losses. Interestingly the importance of sophistication
seems higher for smaller and mid-sized addresses, while for the very largest addresses,
above $10M, none of the sophistication measures are signiﬁcant. Similarly, the positive
relationship between losses and the age of an address is signiﬁcant and comparable in
magnitude across addresses with diﬀerent balances. Thus independent of the size of
the balance, older addresses are more likely to experience losses since they tended to
run later. Again the exemption is the subsample of the very largest addresses, above
$10M, where we do not see a correlation between age and the size of the loss. The
results suggest that for the very largest addresses our metrics of sophistication do not
capture the diﬀerence in their trading strategies, most likely since they are all relatively
sophisticated and were aware of the changes on Terra. In addition, since this group
only includes 109 addresses, idiosyncratic diﬀerences may play a larger role here than
for the other subgroups.

In summary, our ﬁndings have important implications for understanding the risks
and beneﬁts of the open blockchain architecture in creating a level ﬁnancial playing
ﬁeld. Although information about prices and trades of large wallets on the Terra
blockchain was observable to all depositors, outcomes were highly uneven. The larger
losses experienced by smaller and less sophisticated depositors are not explained by
some depositors having unfair access to bank representatives or insiders, an issue that
has been highlighted for traditional banks, an issue that has been highlighted for tra-
ditional banks. For example, Iyer et al. (2016) shows that bank staﬀ or depositors
connected to bank insiders experienced smaller losses in a run. Instead, our results
suggest that many participants lacked the ability or founded too costly to process in-

33

formation in real time. As we have shown, many small depositors re-entered Anchor
to “buy the dip” while large wallets were withdrawing. Thus, open access and the
transparency of the blockchain do not compensate for diﬀerences in ﬁnancial literacy
and wealth and may even exacerbate them.

5. De-pegging Event in May 2021

As mentioned in Section 3.2.4, May 2022 was not the ﬁrst time UST de-pegged from
parity with the US dollar. Terra experienced a prior de-pegging event between May
19 and May 25, 2021.22 The comparison with the May 2022 crash is interesting since
it foreshadowed some of the risks and economic mechanisms that were important later
on. It also allows us to analyze why some of the interventions that TFL undertook to
stabilize the price of UST might have worked during the ﬁrst de-pegging event but not
during the crash in May 2022.

The de-pegging started on May 19 2021, when China announced a crackdown on
the use of cryptocurrencies, and the price of LUNA fell from $16 to $4. Many other
cryptocurrencies also experienced a drop in price at this time. The signiﬁcant drop
in the price of LUNA resulted in its market capitalization declining to a level close to
the aggregate market value of UST, as illustrated in Figure 21. As discussed before,
the market capitalization of the two coins approaching each other may not hold any
particular signiﬁcance for fully rational investors who up front factor in the potential
dilution from swapping UST into LUNA. But many investors appeared to have bought
into the narrative that this point signaled insuﬃcient value in LUNA to support the
value of UST, thereby serving as a strong indication to sell.

[Fig. 21 About Here]

The upper panel of Figure 22 documents swap transactions of UST against three
major stablecoins, USDT, USDC, and DAI, occurring between May 17th and May 29th,
2021, on the UST-3Crv pool. During the period of the ﬁrst de-pegging event, this was
the most liquid marketplace where UST could be exchanged for other stablecoins. The
bottom panel shows the net signed volume (blue) and the deviation of the UST price
from $1 in basis points (black).

[Fig. 22 About Here]

Similar to the later de-pegging event in May 2022, we initially see intensiﬁed selling
in particular by larger addresses. Between 19th and May 24th, investors sold a net value

22There was also a second smaller de-pegging on January 27, 2022. But this episode was short lived

and relatively minor.

34

of 25 million UST, resulting in a 10% discount on UST. In addition, we show that there
were four addresses, which purchased a combined 135 million UST during this period.
Had it not been for the aggressive support of UST by these addresses, the discount
on UST would have been signiﬁcantly greater.23 The swaps into UST initiated by the
four addresses are represented by blue triangles, while the swaps into UST initiated by
other addresses are represented by green circles. Swaps of UST into the other three
stablecoins are depicted by red circles.

In addition, we see that similar to the May 2022 crash, the decline in the UST price
coincided with investor withdrawals from Anchor. Figure 24 shows the outstanding
deposit balance in Anchor.

[Fig. 24 About Here]

When we decompose how diﬀerent participants ran, we see that as in the May
2022 crash, withdrawals were concentrated among wealthier investors, while low-wealth
investors continued pouring their funds into Anchor, see Figure 25.

[Fig. 25 About Here]

Lastly, we examine the eﬀectiveness of the native swap mechanism in safeguarding
the peg. When the price of UST drops below 1, the peg mechanism is designed to
incentivize arbitrageurs to purchase the discounted UST, swap it for LUNA, and receive
the equivalent of $1. First, we note that because of the swap fees, as in May 2022,
the swap spread closely tracked the UST discount restricting the ability of arbitrageurs
to participate in the mechanism, see Figure 23.
In fact, many participants in the
Terra ecosystem were worried at the time about the potential disincentive eﬀects of
the protocol design, and several articles on social media even blamed the de-pegging
event itself on the design of the on-chain redemption cap.24

But as discussed in Section 4.2, while the mechanism can support the price of UST,
it can also contribute to a death spiral if investors who swap UST for LUNA decide to
sell their LUNA holdings. Thus, it is important to understand as to why the run was
avoided in May 2021, but not in May 2022.

A critical factor appears to be that the outstanding supply of UST was much
smaller in May 2021, which enabled TFL to function as a lender of last resort. Table 6

23These

four

0x5dd09afc9ca51b46d6cda2189478b505ace7f37b,
0xe3bdda6413313ed58585e47441815e9662bdd818,
0x2747363d886c7fdcc5187217f1ca493922aa4940,
and 0xaf7bbcfb1c1f987e0ae409c684289b332a425254. They bought 66M, 33M, 19M, and 17M,
respectively.

addresses

are

24See, for example, https://medium.com/coinmonks/should-depositors-in-anchor-protoco

l-pay-attention-to-ust-de-peg-risk-8b59849d75bf.

35

displays the top 20 addresses that swapped the largest quantity of UST during the
de-pegging period. In contrast to May 2022, nearly all swaps were initiated by TFL,
which presumably held onto the newly swapped LUNA instead of selling it.

The lawsuit initiated by the SEC against TFL provides further insight into the
events. The SEC alleges that the peg was restored due to purchases of UST by a third
party, which has been identiﬁed as Jump Trading. Over the period of the run, between
May 23 through May 27, Jump made net purchases of over 62 million UST across at
least two crypto asset trading platforms. In return, Jump allegedly received allocations
of UST from TFL at a heavily discounted price of $0.4 to compensate them for the
stabilization trades.

If the SEC allegation is correct, the fact that market participants in May 2021 were
unaware that TFL and Jump Trading were engaging in the stabilization of UST could
be an additional important factor why the run was avoided in May 2021. When market
participants saw the price re-pegging, they interpreted it as a sign of the system’s
stability. In contrast, in May 2022, traders were aware of the fact that TFL was using
funds held in LFG addresses to support the peg. They also knew that the supply of
UST and the amount of UST locked in the Anchor protocol was signiﬁcantly larger
than the amount available to support the peg. Thus, traders might not have believed
that the stabilization would succeed.

6. Conclusion

This paper provides a detailed analysis of the run on Terra and identiﬁes the un-
derlying economic mechanisms and risks within the ecosystem that led to the crash.
We show that the signiﬁcant increase in UST issuances combined with the highly sub-
sidized deposit rates on Anchor created an unsustainable and fragile system. The price
of LUNA initially rose strongly with the rapid inﬂow of depositors to Anchor, but par-
ticipants may not have fully understood the underlying economics and not have priced
in the potential dilution from the outstanding supply of UST. Our analysis suggests
that the run on Terra was not due to targeted market manipulation by a single entity,
but rather emerged from increasing concerns regarding the viability of the system.

The run on Terra on May 7th began with a few large investors withdrawing their
UST deposits from Anchor and selling them on exchanges. We observe large diﬀerences
in the run behavior across sophisticated and less sophisticated investors, with the
latter group being much slower to run and often did not fully exit even conditional on
withdrawing some funds. Some of these participants even reinvested during the run in
an apparent attempt to “buy the dip.”

36

In contrast to traditional ﬁnancial institutions, blockchain and price data were
in principle observable to all investors. However, we ﬁnd that larger and more so-
phisticated investors withdrew their funds more quickly and decisively. These results
underscore the fact that observability and free access do not, by themselves, level the
playing ﬁeld for investors if there are signiﬁcant diﬀerences in their ability to process
and interpret information.

The highly subsidized deposit rate on Anchor made some observers compare the
economics of Terra-Luna to a Ponzi scheme. Our analysis does show that the Anchor
protocol was a major factor driving the strong demand for UST. It likely also con-
tributed to the high price of LUNA since UST was issued by converting LUNA into
UST. But it is important to note that unlike in a classical Ponzi scheme, the amount
of subsidies provided by TFL was recorded on the Terra blockchain and, in principle,
observable by all investors. However, it is unclear to what extent investors understood
the precarious nature of UST claims and the possible impact of UST conversion on
the LUNA price. By aggressively underplaying the risks building up in the system
on social media and other outlets, Terra insiders likely contributed to the hype about
the network.25 This highlights the limitation of transparency, especially for complex
systems like Terra-Luna. Ultimately, the sustainability of the DeFi ecosystem depends
on the ability of investors to make informed decisions and hold projects accountable
for their actions.

25https://markets.businessinsider.com/news/currencies/terra-usd-ust-luna-do-kwon-p

oor-critics-crypto-crash-2022-5

37

References

Abadi, J. and Brunnermeier, M. (2018). Blockchain economics. Technical report,

National Bureau of Economic Research.

Abreu, D. and Brunnermeier, M. K. (2003). Bubbles and crashes. Econometrica,

71(1):173–204.

Arner, D. W., Auer, R., and Frost, J. (2020). Stablecoins: risks, potential and regula-

tion.

Brunnermeier, M. K. and Oehmke, M. (2013). Bubbles, ﬁnancial crises, and systemic

risk. Handbook of the Economics of Finance, 2:1221–1288.

Bryant, J. (1980). A model of reserves, bank runs, and deposit insurance. Journal of

banking & ﬁnance, 4(4):335–344.

Calomiris, C. W. and Kahn, C. M. (1991). The role of demandable debt in structuring
optimal banking arrangements. The American Economic Review, pages 497–513.

Chamley, C. (2003). Dynamic speculative attacks. American Economic Review,

93(3):603–621.

Chari, V. V. and Jagannathan, R. (1988). Banking panics, information, and rational

expectations equilibrium. The Journal of Finance, 43(3):749–761.

Chordia, T., Roll, R., and Subrahmanyam, A. (2002). Order imbalance, liquidity, and

market returns. Journal of Financial economics, 65(1):111–130.

Cong, L. W., Li, Y., and Wang, N. (2021). Tokenomics: Dynamic adoption and

valuation. The Review of Financial Studies, 34(3):1105–1155.

Cukierman, A., Goldstein, I., and Spiegel, Y. (2004). The choice of exchange-rate
regime and speculative attacks. Journal of the European Economic Association,
2(6):1206–1241.

d’Avernas, A., Maurin, V., and Vandeweyer, Q. (2022). Can stablecoins be stable?
University of Chicago, Becker Friedman Institute for Economics Working Paper,
(2022-131).

Diamond, D. W. and Dybvig, P. H. (1983). Bank runs, deposit insurance, and liquidity.

Journal of political economy, 91(3):401–419.

38

Eichengreen, B. (2019). From commodity to ﬁat and now to crypto: what does history

tell us? Technical report, National Bureau of Economic Research.

Eichengreen, B., Rose, A. K., and Wyplosz, C. (1994). Speculative attacks on pegged
exchange rates: an empirical exploration with special reference to the european
monetary system.

Evans, M. D. and Lyons, R. K. (2002). Order ﬂow and exchange rate dynamics. Journal

of political economy, 110(1):170–180.

Flood, R. P. and Garber, P. M. (1984). Collapsing exchange-rate regimes: some linear

examples. Journal of international Economics, 17(1-2):1–13.

Glasserman, P. and Nouri, B. (2016). Market-triggered changes in capital structure:

Equilibrium price dynamics. Econometrica, 84(6):2113–2153.

Goldstein, I. (2013). Empirical literature on ﬁnancial crises: Fundamentals vs. panic.

The evidence and impact of ﬁnancial globalization, pages 523–34.

Goldstein, I. and Pauzner, A. (2005). Demand–deposit contracts and the probability

of bank runs. the Journal of Finance, 60(3):1293–1327.

Gorton, G. B., Ross, C. P., and Ross, S. Y. (2022). Making money. Technical report,

National Bureau of Economic Research.

Gorton, G. B. and Zhang, J. (2021). Taming wildcat stablecoins. University of Chicago

Law Review, 90.

Gryglewicz, S., Mayer, S., and Morellec, E. (2021). Optimal ﬁnancing with tokens.

Journal of Financial Economics, 142(3):1038–1067.

Hasbrouck, J. (1995). One security, many markets: Determining the contributions to

price discovery. The journal of Finance, 50(4):1175–1199.

Hendershott, T. and Menkveld, A. J. (2014). Price pressures. Journal of Financial

economics, 114(3):405–423.

Hillion, P. and Vermaelen, T. (2004). Death spiral convertibles. Journal of Financial

Economics, 71(2):381–415.

Hu, A. S., Parlour, C. A., and Rajan, U. (2019). Cryptocurrencies: Stylized facts on a

new investible instrument. Financial Management, 48(4):1049–1068.

39

Iyer, R. and Puri, M. (2012). Understanding bank runs: The importance of depositor-
bank relationships and networks. American Economic Review, 102(4):1414–1445.

Iyer, R., Puri, M., and Ryan, N. (2016). A tale of two runs: Depositor responses to

bank solvency risk. The Journal of Finance, 71(6):2687–2726.

Jacklin, C. J. and Bhattacharya, S. (1988). Distinguishing panics and information-
based bank runs: Welfare and policy implications. Journal of political economy,
96(3):568–592.

Kogan, L., Fanti, G., and Viswanath, P. (2021). Economics of proof-of-stake payment

systems.

Krugman, P. R. (1979). Increasing returns, monopolistic competition, and international

trade. Journal of international Economics, 9(4):469–479.

Li, J. and Mann, W. (2018). Digital tokens and platform building.

Li, Y. and Mayer, S. (2022). Money creation in decentralized ﬁnance: A dynamic model
of stablecoin and crypto shadow banking. Fisher College of Business Working Paper,
(2020-03):030.

Liu, Y. and Tsyvinski, A. (2021). Risks and returns of cryptocurrency. The Review of

Financial Studies, 34(6):2689–2727.

Lorenzoni, G. (2014).
nomics, 4:689–740.

International ﬁnancial crises. Handbook of international eco-

Lyons, R. K. and Viswanath-Natraj, G. (2023). What keeps stablecoins stable? Journal

of International Money and Finance, 131:102777.

Makarov, I. and Schoar, A. (2021). Blockchain analysis of the bitcoin market. Technical

report, National Bureau of Economic Research.

Makarov, I. and Schoar, A. (2022). Cryptocurrencies and decentralized ﬁnance (deﬁ).

Technical report, Brookings Papers on Economic Activity.

Morris, S. and Shin, H. S. (1998). Unique equilibrium in a model of self-fulﬁlling

currency attacks. American Economic Review, pages 587–597.

Obstfeld, M. (1996). Models of currency crises with self-fulﬁlling features. European

economic review, 40(3-5):1037–1047.

40

Pennacchi, G. and Tchistyi, A. (2019). On equilibrium when contingent capital has a
market trigger: A correction to sundaresan and wang journal of ﬁnance (2015). The
Journal of Finance, 74(3):1559–1576.

Schmidt, L., Timmermann, A., and Wermers, R. (2016). Runs on money market

mutual funds. American Economic Review, 106(9):2625–2657.

Sockin, M. and Xiong, W. (2023). Decentralization through tokenization. The Journal

of Finance, 78(1):247–299.

Uhlig, H. (2022). A luna-tic stablecoin crash. Technical report, National Bureau of

Economic Research.

41

Figures

Figure 1: Terra timeline. This ﬁgure shows the timeline of major events in the development of the
Terra Luna network. Blue markers represent the launch of various protocols. Gray markers indicate
major network upgrades, also known as hard forks. The depeg event is marked in red.

Figure 2: Network volume of UST (left) and LUNA (right). This ﬁgure shows the largest
nodes in the Terra Luna network by transaction volume and the ﬂow of volume between nodes. The
size of the node reﬂects the total volume that ﬂows through the category. The (grey) edge size between
nodes is proportional to the volume between the two nodes. The numbers next to an edge show the
corresponding volume. Deﬁnitions of the entity groups are in the text. We only show categories with
at least $10 billion of total volume in the UST network and $5 billion in the LUNA network, and
edges with at least $1 billion of volume.

42

Figure 3: Anchor gross rates. This ﬁgure shows the daily APR of lending and borrowing on
Anchor before subsidies by TFL and collateral yield. The annual deposit rate was set at 19.5%. The
annualized borrowing rate was set as an increasing function of the proportion of outstanding loans to
outstanding deposits. The series are smoothed with 7-day rolling averages.

Figure 4: Anchor borrowing costs and incentives. The left ﬁgure shows the opportunity cost
of LUNA collateral broken out by the source of the yield on LUNA tokens. The two main sources are
block rewards and airdrops, which are token allocations to reward participants. To value the airdrops
we assume a borrower sells weekly token airdrops during the week after receiving them. The right
panel shows the annualized subsidy rate on Anchor, which was distributed to borrowers via ANC,
Anchor native token. The series are smoothed with 7-day rolling averages.

43

Figure 5: Anchor net rates and exploiting loans. This ﬁgures shows the daily APR of lending
(blue line) and borrowing (red line) on Anchor after considering the opportunity cost of the collateral
and the ANC subsidy. We assume borrowers use the minimum permitted amount of collateral by the
LTV limit and sell ANC subsidies after receiving them. The dashed line shows the proportion of loans
from Anchor that are posted back to Anchor as deposits. The series are smoothed with 7-day rolling
averages.

Figure 6: Stablecoin rates on competing platforms. The ﬁgure compares the lending rates on
Anchor, Compound, and Aave from May 2021 to the end of May 2022. The rates on Compound and
Aave are the average rates of Tether (USDT), USD Coin (USDC), and Dai. The series are smoothed
with 7-day rolling averages.

44

Figure 7: New Terra addresses and time to joining Anchor. This ﬁgure shows the number of
new addresses on TerraUSD each day, broken out by how soon they start using Anchor. The lowest
blue line are users who start using Anchor immediately on their their ﬁrst day, then next group are
those who start using it within a week, etc. The gray ribbon shows the addresses who joined the
network but never used Anchor. The series are smoothed with 7-day rolling averages. The right panel
shows the share of each group that eventually used Anchor.

Figure 8: UST supply by entity. This Figure breaks out the aggregate supply of UST by the
types of entities that held them. Deﬁnitions of the entity groups are in the text.

45

Figure 9: UST-LUNA swap volume and UST price. The top panel shows the daily amount
of UST and LUNA swapped (left axis) along with the cumulative net UST supply (right axis). The
net volume is computed as: swap amount + fee amount - oﬀer amount. The bottom panel shows the
UST dollar price.

Figure 10: Concentration of Anchor deposits. The left panel plots the percentage of deposits
held by the top 10, 100 and 1000 users on Anchor on a given day between May 2021 and May 2022. The
right panel plots the histogram of the number of wallets by size of deposits on Anchor before the run
on May 6, 2022. We exclude addresses that are exchanges, smart contracts, or other intermediaries.

46

Figure 11: Cash ﬂow decomposition on Anchor. The left panel shows the daily inﬂows (positive)
and outﬂows (negative) on Anchor in billion UST broken out by their sources. Inﬂows include the
interest on outstanding loans (blue), the staking rewards produced by the staked LUNA as collateral
(red) or ETH as collateral (yellow), and proportional fees charged on the liquidated loans (green).
Outﬂows include the interest paid to depositors (gray), and the buyback of ANC tokens from the
Astroport DEX (teal). The black line plots the daily net cashﬂow. The right panel shows the balance
of the Anchor’s yield reserve address, as well as two waves of UST injections by TFL and LFG into
the address.

Figure 12: Entry and exit rates of Anchor users. This ﬁgure plots the number of depositors
that enter or exit Anchor as a fraction of the existing depositors on the previous day. The series are
smoothed with 7-day rolling averages.

47

Figure 13: LUNA and UST market capitalization during the run. This ﬁgure shows the
circulating market capitalization of UST (blue) and LUNA (orange) in billions of US dollars from
May 1 to May 15, 2022.

Figure 14: Anchor ﬂows on May 7, 2022. The top two panels show the exact timing of the
withdrawals by Wallet A and Wallet B from Anchor which constitute the beginning of the run. The
bottom panel shows the timing of all other Anchor deposits (green) and withdrawals (red) on May 7.
The y-axis denotes the size of each trade in millions of US dollars.

48

Figure 15: UST-3Crv swap transactions. The top panel shows the UST swap transac-
tions price against three major stablecoins, USDT, USDC, and DAI on May 7, 2022. Swap
transactions of UST into the other three stablecoins are in red, and swaps into UST in green.
The y-scale is logarithmic. The bottom panel shows the net signed volume (blue) and the
deviation of the UST price from $1 in basis points (black).

Figure 16: Binance UST/USDT trades. The top panel shows the UST/USDT trades
on May 7, 2022. Sell-initiated trades are in red and buy-initiated ones in green. The y-scale
is logarithmic. The bottom panel shows the net signed volume (blue) and the deviation of the
UST price from $1 in basis points (black).

49

Figure 17: Anchor outﬂows. This ﬁgure shows the outstanding deposit balance in Anchor (black
line, left axis) and the price of UST (red line, right axis) during the run in May 2022.

Figure 18: Swap arbitrage. This ﬁgure shows the trading activity on the native swap market. The
top panel plots the UST discount and the swap fees over time. The middle panel shows the diﬀerence
between the UST discount and the swap fees, which is a measure for the attractiveness of swapping
UST for LUNA over selling UST at the market price. The bottom panel shows the dollar amount of
UST that were swapped in a given minute.

50

Figure 19: LUNA death spiral. This ﬁgure shows and the circulating supply (black line, left axis)
and the price (orange line, right axis) of LUNA during the run, both in log scales. The convertibility
between LUNA and UST was suspended on May 13.

Figure 20: Anchor outﬂows by size. The left panel shows withdrawals from Anchor over the day
of May 7 2022, broken out by the size of the deposit balance of addresses as of May 6th, before the
run. The sample excludes any addresses held by intermediaries or large institutions and focuses on
individual addresses. We also remove addresses with less than 100 UST in Anchor. The right panel
shows the same analysis over the period from May 6 to May 14, 2022.

51

Figure 21: LUNA and UST Market Capitalization. This ﬁgure shows the circulating market
capitalization of UST (blue) and LUNA (orange) in billions of US dollars from October 2020 to May
2022.

Figure 22: UST-3Crv swap transactions. The top panel shows the UST swap
transactions price against
three major stablecoins, USDT, USDC, and DAI on May
Swap transactions of UST into the other three stablecoins are in red,
17–29, 2021.
and swaps into UST in green and blue. The blue triangles are swaps into UST by
four addresses: 0x5dd09afc9ca51b46d6cda2189478b505ace7f37b, 0xe3bdda6413313ed58585e47441815e9662bdd818,
0x2747363d886c7fdcc5187217f1ca493922aa4940, and 0xaf7bbcfb1c1f987e0ae409c684289b332a425254. The y-scale
is logarithmic. The bottom panel shows the net signed volume (blue) and the deviation of the
UST price from $1 in basis points (black).

52

Figure 23: Swap arbitrage, May 2021. This ﬁgure shows the trading activity on the native swap
market. The top panel plots the UST discount and the swap fees over time. The middle panel shows
the diﬀerence between the UST discount and the swap fees, which is a measure for the attractiveness
of swapping UST for LUNA over selling UST at the market price. The bottom panel shows the dollar
amount of UST that were swapped in a given minute.

53

Figure 24: May 2021 De-pegging event. This ﬁgure shows the outstanding deposit balance in
Anchor (black line, left axis) and the price of UST (red line, right axis) during the run in May 2021.

Figure 25: Anchor May 2021 outﬂows by size. The ﬁgure shows withdrawals from Anchor over
the period of the ﬁrst de-pegging event, May 17 to 28, 2021, broken out by the size of the deposit
balance of addresses as of May 17th, 2021. The sample excludes any addresses held by intermediaries
or large institutions and focuses on individual addresses. We also remove addresses with less than 100
UST in Anchor.

54

Tables

Token

Volume ($ billion) Transaction count

UST
LUNA
aUST (Anchor UST deposit)
bLUNA (Anchor bonded LUNA)
ANC (Anchor token)
bETH (Anchor bonded ETH)
Astroport ANC-UST LP
Terraswap ANC-UST LP
ASTRO (Astroport token)
VKR (Valkyrie token)
SD (Stader token)
MIR (Mirror token)
Astroport ASTRO-UST LP
PSI (Nexus token)
MINE (Pylon token)

359.638
216.698
114.507
49.569
13.161
9.214
5.983
5.068
3.988
3.795
2.578
2.446
1.236
1.077
1.065

20272983
9540155
1581845
1548061
2983677
191050
177590
170849
1348552
737877
95102
867647
238299
1175289
593806

Table 1: Token volume. This table reports the volume (in billion US dollars) and the
transaction count of the top 15 tokens on the Terra Luna network from September 30, 2021
to May 6, 2022. The volume is collected from transaction logs of type “transfer” and “send”
in the network. We net any transfer of the same token between the same counterparties at
the same time. The USD price is the closing price of the token on the day of transfer. The
transaction count is the number of transactions that contain that token.

55

Full sample

Pre-run balance

(1)
159669
59.31
4.56
1.26
0.30

<1K
(2)
43885
76.49
4.06
0.99
0.21

10K 100K
(4)
(3)
40688
63360
46.29
60.05
5.01
4.43
1.49
1.24
0.36
0.28

1M 10M >10M
(6)
(5)
1230
10397
31.85
36.74
6.10
5.58
1.50
1.60
0.60
0.47

(7)
109
26.58
6.92
1.48
0.65

Exited

(8)
78859

Address count
Percent loss
Age in months
No. of CEXs
Used Bridges?

Table 2: Summary statistics: individual addresses. This table reports the summary
statistics for individual addresses prior to the run. We report the number of addresses, the
percentage loss in the deposits on the address over the period of the run from May 6 to 13,
Age in month is the number of months the address has been on the Terra blockchain, N of
CEX is the number of centralized exchanges an address has traded with over the time of
its existence, Used Bridges is a dummy for whether the address ever used Terra Shuttle or
Wormhole Bridges. In Column (1) we show the full sample and in the remaining columns
we break out the sample by the balance in the address on the day before the run.

56

Full sample

Balance subgroup

Percent loss

<1K
(3)

10K 100K
(5)
(4)

1M
(6)

10M >10M
(7)

(8)

(2)

(1)
-6.00
(0.05)

log balance

Size[1K-10K]

Size[10K-100K]

Size[100K-1M]

Size[1M-10M]

Size[>10M]

log(volume/balance)

log age

No. of CEXs used

Used bridges?

Constant

R2
N

1.10
(0.09)
5.74
(0.16)
-4.39
(0.10)
-3.02
(0.22)
105.30
(0.44)
0.12
159669

-15.24
(0.24)
-27.98
(0.27)
-37.00
(0.43)
-41.97
(1.11)
-47.08
(3.67)
1.30
(0.09)
5.63
(0.16)
-4.68
(0.10)
-3.72
(0.22)
72.04
(0.28)
0.12
159669

3.57
(0.16)
6.26
(0.31)
-4.80
(0.24)
-3.33
(0.49)
67.86
(0.49)
0.03
43885

0.85
(0.16)
5.95
(0.26)
-5.48
(0.17)
-4.48
(0.36)
58.12
(0.41)
0.02
63360

-1.97
(0.21)
5.18
(0.30)
-3.75
(0.17)
-2.29
(0.40)
47.06
(0.48)
0.02
40688

-3.92
(0.39)
5.67
(0.53)
-2.44
(0.28)
-2.49
(0.70)
37.47
(0.89)
0.03
10397

-0.25
(1.08)
6.29
(1.36)
-2.81
(0.76)
-4.71
(2.01)
28.74
(2.43)
0.02
1230

-1.27
(3.73)
0.41
(3.58)
1.93
(2.49)
-8.01
(6.04)
29.75
(7.28)
0.02
109

Table 3: Percentage loss of Anchor depositors. This table reports the results from a
regression of the loss in the value of an address experienced over the period of the run, from
May 6 to May 13, on the size of the balance of the address before the run and measures of
the ﬁnancial sophistication of traders. Columns 1 and 2 report use the full sample. Columns
3 to 8 report subsamples by the size of the address.

57

Address

Volume ($B) Transaction count Address label

terra10kjnhhsgm4jfakr85673and3aw2y4a03598e0m
terra1cymh5ywgn4azak74h4gsrnakqgel4y9ssersvx
terra1dtzfwgzt8xa70zkm8gqzwz0n4zrqtngdpqejx5
terra17p4mqd7yl9m0r7cfv0nf9s9zae3d3gm4tmyg2a
terra13h0qevzm8r5q0yknaamlq6m3k8kuluce7yf5lj
terra1t8szgklntcwxyfyﬂucuq895gpjr8wn6tsqxye
terra1v49w0m38fe87edhqdv30w96wq0pz6u6548q9gj
terra1lewnh53gt0hzgjejrtwdz8q7dennz09s6ds4k2
terra14tlthgtg6ep6xnqptyg8dp3gcq4jxvgqmskwkd
terra14ny376fe7hys2zqxwc87zp2achp9tju5q6jul4
terra1g5dmf4qpmdrcw77d3ty6djrgujt8r2n3lgyknj
terra1nexqdq252acp09m9eler7jhg9kd3rqfzkek9r0
terra1mer7nd843n5g3v37xxtd3hude6t5rf4cq3mnae
terra12qmfcxy8kahwt44tn4aq4t6kdmtyer38xnrh7m
terra19qx5xe6q9ll4w0890ux7lv2p4mf3csd4qvt3ex
terra1qy36laaky2ns9n98naha2r0nvt3j7q3fpxfs2e
terra1zz2nf34fjkjygkg0kplkrr29ycxarmct6kafvj
terra1e028300g5kaef05vycatgz8tnrvmwmfstafk52
terra1g9p9c5hjw4m3v9l65lmxt2g89vheashp6yfukm
terra13vpm23s7rw5gqp9ckhqngjesxcuzatytknqpfg
terra1tdu6f7nﬀenxw7aahumtjklnzfcdw24k8836q5
terra1anllr0tt8r2my88kp6kmdwdnewnja5246djj99
terra1r3mdl2q46mx5z8y8d6enm35t6g76wqtn43008u
terra13u3p30c2tn9m8dmru6mfyhmqs379qm43vrx7l7
terra10zzfuednzhkmwn4tqks2mukstr02r5jklpmh2f
terra1zd46n9v45lsqsxrcje3ke6ejlxm7nhtqr2dlgq
terra189rgutrsul7dm47u5h4y7hsraxnr9q4dk2fhjs
terra1q9cs4d4x67u6yvsaswecf0usp2rygdnmrﬂzfj

2.71
2.06
1.76
0.61
0.51
0.49
0.48
0.48
0.48
0.48
0.48
0.48
0.47
0.46
0.43
0.42
0.42
0.41
0.40
0.40
0.40
0.40
0.40
0.39
0.39
0.39
0.18
0.11

9462

prop 44 swap/burn address
LFG/TFL Burning Wallet
Jump

171
23749
36083
26607 TFL bot/UST Peg Defender
reserve funder (LFG)
22368 TFL bot/UST Peg Defender
21393 TFL bot/UST Peg Defender
21943 TFL bot/UST Peg Defender
21293 TFL bot/UST Peg Defender
21401 TFL bot/UST Peg Defender
21801 TFL bot/UST Peg Defender
21465 TFL bot/UST Peg Defender
21209 TFL bot/UST Peg Defender
21079 TFL bot/UST Peg Defender

109878 Terraswap route swap

5000
13455
12871
12441
12478
12385
12271
12359
12545
12290
12473
20140
3527

LFG reserve address
delegator(TFL)
Jump/TFL swap addr
Jump/TFL swap addr
delegator(TFL)
Jump/TFL swap addr
delegator(TFL)
Jump/TFL swap addr
delegator(TFL)
delegator(TFL)
Jump/TFL swap addr
Jump/TFL swap addr
bLUNA Core - Rewards Dispatcher

Table 4: Top LUNA for UST swap addresses. This table reports the list of top
addresses that swapped the largest amount of LUNA for UST.

Address

Vol (UST M) Vol ($M) Transaction count Address label

terra1cjjwzcer7qpx4uj9s70fcdwpz9lecrqsxmmtun
terra139y02s9urkkyesukndrqdjmqj7gkk5dltd05v8
terra1hz0q2qgsgetaqwxds95angslxfyvkpzcfr4j9z
terra14yzejwu639x5ntud98zsnl6caejqmns2vvfhs4
terra1ead9mwsw4efs64z4vz4sq2vp28q4wdsp3swpk4
terra1yvu32he5xprd5yea8dmagalaluases0z3x7dlv
terra1wlfagw79h0tushlz7uhvg3kxg5qq6zeg6axazf
terra14tlthgtg6ep6xnqptyg8dp3gcq4jxvgqmskwkd
terra1w92zvqhrplwalnj6ke7n28jfqp8fwsdjlajyvc
terra1zdm0cayj9y0vsvt4x60zp9eq9nh2uwxuht7jw0
terra1jus3ldxzjx4d42vzzw7yj5nzu2ghm6yz8k4c2t
terra1wl5pwfj6zuqra2rhjs9eyufke3a0fjdckafxfu
terra1nexqdq252acp09m9eler7jhg9kd3rqfzkek9r0
terra14ny376fe7hys2zqxwc87zp2achp9tju5q6jul4
terra12qmfcxy8kahwt44tn4aq4t6kdmtyer38xnrh7m
terra1mer7nd843n5g3v37xxtd3hude6t5rf4cq3mnae
terra1lewnh53gt0hzgjejrtwdz8q7dennz09s6ds4k2
terra1t8szgklntcwxyfyﬂucuq895gpjr8wn6tsqxye
terra17p4mqd7yl9m0r7cfv0nf9s9zae3d3gm4tmyg2a
terra1g5dmf4qpmdrcw77d3ty6djrgujt8r2n3lgyknj
terra1v49w0m38fe87edhqdv30w96wq0pz6u6548q9gj

687
446
314
133
119
122
86
97
83
78
90
96
83
81
81
81
81
80
80
81
80

449
276
154
82
70
68
66
62
57
55
54
51
50
50
49
49
49
49
48
48
48

19122
6513

unknown smart contract 12
unknown smart contract 5

157 Alameda Research
278 UST/LUNA arbitrageur
134 UST/LUNA arbitrageur
184 UST/LUNA arbitrageur
2793 UST/LUNA arbitrageur

649 TFL bot/UST Peg Defender

2173 UST/LUNA arbitrageur
7323 UST/LUNA arbitrageur
1607 UST/LUNA arbitrageur
304 UST/LUNA arbitrageur
526 TFL bot/UST Peg Defender
504 TFL bot/UST Peg Defender
518 TFL bot/UST Peg Defender
516 TFL bot/UST Peg Defender
518 TFL bot/UST Peg Defender
505 TFL bot/UST Peg Defender
506 TFL bot/UST Peg Defender
529 TFL bot/UST Peg Defender
498 TFL bot/UST Peg Defender

Table 5: Top LUNA for UST swap addresses during the May 2022 Terra run.
This table reports the list of top addresses that swapped the largest amount of LUNA for UST
over the period of the run, from May 7 to May 13.

58

Address

Vol (UST M) Transaction count Address label

terra189rgutrsul7dm47u5h4y7hsraxnr9q4dk2fhjs
terra14ny376fe7hys2zqxwc87zp2achp9tju5q6jul4
terra1lewnh53gt0hzgjejrtwdz8q7dennz09s6ds4k2
terra1mer7nd843n5g3v37xxtd3hude6t5rf4cq3mnae
terra1pemrznzc6kup38n294nd5q39k2c8qhl6lthet4
terra1hsh3ve4vrqnluccws9gwh5sg4jchuc352md2kw
terra1nexqdq252acp09m9eler7jhg9kd3rqfzkek9r0
terra1v49w0m38fe87edhqdv30w96wq0pz6u6548q9gj
terra12qmfcxy8kahwt44tn4aq4t6kdmtyer38xnrh7m
terra1g5dmf4qpmdrcw77d3ty6djrgujt8r2n3lgyknj
terra17p4mqd7yl9m0r7cfv0nf9s9zae3d3gm4tmyg2a
terra1t8szgklntcwxyfyﬂucuq895gpjr8wn6tsqxye
terra1cgq04kwfpckhlxvw3uw2ug43a5xur3shaxcl8e
terra14tlthgtg6ep6xnqptyg8dp3gcq4jxvgqmskwkd
terra1m3cxucxdkg2p8h7fk3ztwrwqw0fjnr07yxwvuf
terra1pm37tvmac8khvfr500fzvuj7z0pu73d6mphepy
terra1x04xgtwlw72gtfzrq7nfwmr6eexla8ecljw28z
terra1m2rylkksr05r3z7myzhldz59x9j0c5ﬀagzd5y
terra1d6yuxj62qefw8wwmmskmfm8503g59fxdrr0z8s
terra10jycqs3qn6vlxkacqm9lyhzadwk0p03a6de8jm

63
9
8
8
8
8
7
7
7
7
7
7
7
7
5
5
4
3
2
1

11536

Jump/TFL swap addr
214 TFL bot/UST Peg Defender
180 TFL bot/UST Peg Defender
201 TFL bot/UST Peg Defender

4988 UST/LUNA arbitrageur
4713 UST/LUNA arbitrageur

180 TFL bot/UST Peg Defender
180 TFL bot/UST Peg Defender
168 TFL bot/UST Peg Defender
163 TFL bot/UST Peg Defender
164 TFL bot/UST Peg Defender
160 TFL bot/UST Peg Defender

2649 UST/LUNA arbitrageur

149 TFL bot/UST Peg Defender

1909 UST/LUNA arbitrageur
1743 UST/LUNA arbitrageur
2 TFL market making
1281 UST/LUNA arbitrageur
1185 UST/LUNA arbitrageur
393 UST/LUNA arbitrageur

Table 6: Top LUNA for UST swap addresses during the May 2021 de-pegging
event. This table reports the list of top addresses that swapped the largest amount of LUNA
for UST over the period of the May 2021 de-pegging event, from May 19 to May 27.

59

Appendix I

TFL

CEX

Name Description
Admin Addresses of network administration accounts and Terra insiders.
This category includes addresses of the community pool, Terra’s na-
tive swap, the transaction fee collector, the native swap fee collector,
LUNA staking master account, the Proposal 44 swap address, TFL’s
main wallet, LFG’s main wallet, TFL and Do Kwon’s shadow wal-
lets, TFL’s salary distribution wallet, TFL’s market marker wallet,
and LFG’s reserve address.
Addresses that TFL, LFG, and Jump used to issue UST and defend
the peg.
Addresses of centralized exchanges are regular wallets that belong
to a traditional cryptocurrency exchange. CEXs hold custody of
cryptocurrencies. We cover 25 known exchanges: Binance, Bitﬁnex,
Bithumb, Bitkub, Bitrue, Bittrex, Bkex, Bybit, Coinex, Coinone,
Coinspot, Cryptex, Crypto.com, FTX, Gate.io, Gopax, Hotcoin,
Huobi, Kraken, Kucoin, LBank, MEXC, Newton, Upbit, Whitebit.
We also identify some unknown exchanges by their transaction pat-
terns and label them as CEXs.
Addresses of decentralized exchanges are smart contracts that allow
traders to trade between pairs of tokens. Each token pair is a smart
contract address. We cover trading pairs on Astroport, Terraswap,
Loop, and Prism.

DEX

Anchor Addresses that belong to Anchor, including Anchor’s UST money
market account, Anchor’s UST yield reserve, bLUNA and bETH stak-
ing accounts, Anchor’s loan liquidation auctioneer, the ANC incen-
tive payment account, the ANC airdrop account, the ANC repurchase
acount, Anchor’s community pool, and Anchor’s governance staking
account.

Bridge Addresses that connect Terra to other blockchains, including Worm-
hole and Shuttle bridges that connect to Ethereum. Terra users can
send tokens to these bridges, and they issue tokens on Ethereum.
Smart contract addresses that are not DEXs, bridges, or Anchor. This
includes crowdfunding platforms, NFT marketplaces, and arbitrage
bots.

DeFi

Other Addresses of regular users on the blockchain, include hedge funds,
venture capitals, blockchain validators, and all unnamed regular ac-
counts on Terra.

Table 7: Categories of Terra addresses. This table reports the categories of Terra
addresses in Figure 2 and their descriptions.

60

