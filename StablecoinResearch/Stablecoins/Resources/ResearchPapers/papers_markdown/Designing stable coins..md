NUS RMI Working Paper Series – No. 2021-05
Designing Stable Coins

Yizhou CAO, Min DAI, Steven KOU,
Lewei LI and Chen YANG

April 2021

NUS Risk Management Institute
21 HENG MUI KENG TERRACE, #04-03 I3 BUILDING, SINGAPORE 119613

www.rmi.nus.edu.sg/research/rmi-working-paper-series

Designing Stable Coins∗

Yizhou Cao1, Min Dai2,3, Steven Kou2,3, Lewei Li1, and Chen Yang4

1FinBook, 148955, Singapore

2Risk Management Institute, National University of Singapore, 119613, Singapore

3Department of Mathematics, National University of Singapore, 119076, Singapore

4Department of Mathematics, ETH Z¨urich, 8092 Z¨urich, Switzerland

Abstract: Stable coins, which are cryptocurrencies pegged to other stable ﬁnancial assets

such as U.S. dollar, are desirable for payments within blockchain networks, whereby being

often called the “Holy Grail of cryptocurrency.” However, existing cryptocurrencies are too

volatile for these purposes. By using the option pricing theory, we design several dual-class

structures that oﬀer ﬁxed income stable coins (class A and A(cid:48) coins) pegged to a traditional

currency as well as leveraged investment instruments (class B and B(cid:48) coins). When combined

with insurance from a government, the design can also serve as a basis for issuing a sovereign

cryptocurrency.

JEL codes: G10, O30, E40.

Keywords: stable coins, ﬁxed income crypto asset, leveraged return crypto asset, smart

contract, option pricing.

∗Corresponding author: Min Dai, 10 Lower Kent Ridge Road, Singapore 119076. Tel: +65 6516 2754.

Email: matdm@nus.edu.sg.

1

1 Introduction

How to create a digital currency was a long-standing open problem for many years, due

to two main challenges: First, as people can easily copy music and movie ﬁles, how to prevent

people from copying digital currency token electronically? Secondly, how to avoid the double

spending problem in which a single digital currency token can be spent more than once to

settle liabilities. A revolution in FinTech was that the two problems can be solved by using

blockchains.

A blockchain is a decentralized (peer to peer) and distributed network that is used to

record, after miners’ veriﬁcation, all transactions which can be viewed by every users, thus

allowing people to verify and audit transactions in a transparent and inexpensive way. The

records cannot be easily altered retroactively.1 Furthermore, a blockchain conﬁrms with very

high probability that each unit of value was transferred only once, solving the double spending

problem without a trusted authority2. The ﬁrst blockchain was conceptualized in Nakamoto

(2008), and was implemented in 2009 as the core component of the ﬁrst cryptocurrency,

Bitcoin.

Another breakthrough came in late 2013 when Vitalik Buterin extends the idea of Bitcoin

to create the Ethereum platform on which people can write smart contracts. This is a very

important technology advance, as many types of clerk works, such as public notary, import

and export paper works, certain legal and accounting documentations, can be programmed as

smart contracts which can be tracked and executed automatically on the Ethereum platform.

The cryptocurrency generated and circulated on the Ethereum platform is Ether (with the

1In fact, any alternation of the records will trigger the alteration of all subsequent blocks, and unless there

is a collusion of majority users of the network, it is impossible to change the records.

2Even if an attacker has 10% success probability of ﬁnding the next block, in the standard 6 block veriﬁ-

cation scheme, the chance of the attacker will ever be successful in double spending is only about 0.0005914.

Note that the calculation 0.0002428 in Nakamoto (2008) was wrong and was corrected in a recent paper by

Grunspan and Perez-Marco (2018).

2

trading symbol ETH).

Currently, there are over 1000 crytocurrencies traded in exchanges; see, e.g, the list on

coinmarketcap.com. Some of them are based on public blockchains, such as Bitcoin and Ether,

and others on private blockchains, such as Ripple. In fact, one can buy crytocurrencies from

online exchanges or at ATM machines worldwide, just like buying standard ﬁnancial securities

or foreign currencies. All cryptocurrencies share three important features. First, a payment

from one user to another is processed in a decentralized way without any intermediary.

Second, all transaction records are stored in the networks and can be viewed by every user.

Third, they allow anonymous payments.

This paper attempts to design stable coins, which are cryptocurrencies pegged to other

stable ﬁnancial assets such as U.S. dollars, by using concepts from the option pricing theory.

Stable coins are desirable to be used as public accounting ledgers for payment transactions

within blockchain networks, and as crypto money market accounts for asset allocation in-

volving cryptocurrencies.

1.1 Stable Coins

One major characteristic (or drawback) of cryptocurrencies is their extreme volatility.

Figure 1 illustrates the price of Ether in U.S. dollars, ETH/USD, from October 1, 2017 to

February 28, 2018. During this period, ETH/USD has an annualized return volatility of

120%, which is more than 9 times that of S&P 500 during the same period (13%).

The extremely large volatility means that a cryptocurrency like ETH cannot be used as

a reliable means to store value. It is risky to hold the currency even for a single day due to

this ﬂuctuation. Even if retailers accept the cryptocurrency for payments, they may have to

exchange it immediately into traditional currencies to avoid risk.

A stable coin is a crypto coin that keeps stable market value against a speciﬁc index or

asset, most noticeably U.S. dollar. Stable coins are desirable for at least three reasons:

3

Figure 1: ETH/USD Price from 1 Oct 2017 to 28 Feb 2018

• They can be used within blockchain systems to settle payments. For example, lawyer or

accountants can exchange their stable coins generated by smart contracts automatically

for the services they provide within the system, without being bothered by the exchange

fees from a cryptocurrency to U.S. dollar, which can range from 0.7% to 5%.

• They can be used to form crypto money market accounts, for the purpose of doing asset

allocation for hundreds cryptocurrencies.

• They can be used by miners or other people who provide essential services to maintain

blockchain systems to store values, as it may be diﬃcult and expensive for them to

convert mined coins into traditional currencies.

However, as we can see, existing cryptocurrencies are too volatile to be served as stable coins.

In fact, how to create a good stable coin is called the “Holy Grail of Cryptocurrency” in the

media (Forbes, March 12, 2018, Sydney Morning Herald, Feb 22, 2018, Yahoo Finance, Oct

14, 2017)

There are four existing types of issuance of stable coins. The ﬁrst type is an issuance

backed by accounts in real assets such as U.S. dollars, gold, oil, etc. More precisely, these

stable coins represent claims on the underlying assets. For example, Tether coin is claimed

4

OctNovDecJanFebMar200400600800100012001400to be backed by USD, with the conversion rate 1 Tether to 1 USD (see Tether (2016)).

However, it is very diﬃcult to verify the claim that Tether has enough reserve in U.S. dollar,

especially on a daily basis.3 There are other tokens claimed to link to gold (e.g. Digix,

GoldMint, Royal Mint Gold, OzCoinGold, and ONEGRAM), although the claims are also

hard to verify. Recently in February 2018, the government of Venezuela issued Petro, a

cryptocurrency claimed to be backed by one barrel of oil.

The second type is the seigniorage shares system, which has automatic adjustment of the

quantity of coin supply: When the coin price is too high, new coins are issued; when the coin

price is too low, bonds are issued to remove tokens from circulation. A typical example of

this type is Basecoin (see Al-Naji (2018)). However, the diﬃculty of maintaining the right

balance of supply and demand of a stable coin is at the same level of diﬃculty faced by a

central bank issuing ﬁat currency.

The third type is an issuance backed by over-collateralized cryptocurrencies with auto-

matic exogenous liquidation. For example, one can generate $100 worth of stable coins by

depositing $150 worth of Ether. The collateral will be sold automatically by a smart contract,

if the Ether price reaches $110. One can also combine the idea of over-collateralization and

seigniorage by issuing more coins if the coin price is too high, and allow people to borrow

the coin, which gives borrower to buy back the coin if the coin price is too low, thus pushing

the price higher. Examples of this type include the DAI token issued by MakerDAO; see

MakerTeam (2017). A drawback of this type is the relative large collateral size.

The last type is government-backed stable coins. Besides Venezuela, other countries are

considering issuing cryptocurrencies, including Russia and China. Canadian government also

did Project Jasper involving the “CAD-coin”, in which a Blockchain network is built for

domestic interbank payment settlements. There is a virtual currency working group under

3 In fact, U.S. regulators issued a subpoena to Tether on December 6, 2017, on whether $2.3 billion of the

tokers outstanding are backed by U.S. dollars held in reserve (Bloomberg news, January 31, 2018).

5

the Federal Reserve System in U.S., which uses the “Fedcoin” internally. As commented

by Garratt (2016), “The goal is to create a stable (less price volatility) and dependable

cryptocurrency that delivers the practical advantages of Bitcoin even if this means involving

the central government and abandoning the Libertarian principles that many believe underlay

Bitcoin’s creation.”

There are several advantages of issuing stable coins by governments. They are cheaper to

produce than the cash in bills or coins, and they are never worn out. They can be tracked

and taxed automatically by the blockchain technology. They can facilitate statistical works,

such as GDP calculation and collecting consumer data. Furthermore, they can simplify legal

money transfers inside and outside blockchains. Finally, as pointed out by Bech and Garratt

(2017), the main beneﬁt of a retail central bank backed cryptocurrency is that it would have

the potential to provide the anonymity of cash. The ﬁrst countries that adopt stable coins

will likely see the inﬂow of money from people who want stable currencies on blockchains.

However, a main drawback of issuing stable coins purely by governments is the cost. More

precisely, does a government have enough expertise in maintaining a computer system, is a

government willing to put enough reserve to back up a stable coin fully, and how does a

government control supply and demand of a stable coin in a global anonymous blockchain

network (which can be quite diﬀerent from a ﬁat currency network)?

1.2 Our Contribution

We use the option pricing theory (c.f. Duﬃe (2010); Hull (2017); Ingersoll (1987); Jar-

row and Turnbull (1999); Shreve (2004)) to design several dual-class structures that oﬀer

entitlements to ﬁxed income stable coins (Class A coins) pegged to a traditional currency

as well as leveraged investment opportunities (Class B coins). The design is inspired by the

dual-purpose funds popular in the U.S. and China. More precisely, due to downward resets,

a vanilla A coin behaves like a bond with the collateral amount being reset automatically.

6

To reduce volatility, the vanilla A coin can be further split into additional coins, A(cid:48) and B(cid:48) .

Unlike traditional currencies, these new class A coins record all transactions on a blockchain

without centralized counterparties.

We show that the proposed stable coins have very low volatility; indeed the volatility

of class A(cid:48) coin is so low that it is essentially pegged to the U.S. dollar. Table 1 reports

the volatility of ETH, S&P 500 index, Gold price, U.S. Dollar index, class A and A(cid:48) coins,

respectively.

Table 1: Annualized Volatility of Our Stable Coins versus Common Market Indices

Index

ETH

S&P 500 Gold

US$ Index Class A Coin Class A(cid:48) Coin

Volatility

120.49% 13.15% 9.44%

5.76%

2.37%

0.87%

Annualized volatility is calculated from 1 Oct 2017 to 28 Feb 2018.

The design of stable coins can be used alone in most cases, except in the case of Black

Swan events, when the underlying cryptocurrency suddenly drops close to zero within an

extremely short time period.4 Therefore, to be truly stable, stable coins need a guarantee in

Black Swan events.

A policy implication of this paper is that a public-private partnership may be formed to

issue stable coins backed by a government. More precisely, by designing a set of stable coins

using the option pricing theory via private market forces, the government only needs to back

up the stable coins in extreme cases of Black swan events, just like what the U.S. government

does for the FDIC insurance for private money market accounts in U.S.

4The intuition here is similar to that of the risk of the top tranche of a CDO contract. If the correlations

of all ﬁrms covered within the CDO are close to 1, then one ﬁrm’s default leads to almost all other ﬁrms’

default, resulting in a signiﬁcant drop of the top tranche value.

7

1.3 Literature Review

Although our design of stable coins is inspired by dual-purpose funds, it is diﬀerent from

dual-purpose funds in U.S. and China in the aspects shown in Panel A of Table 2. These

diﬀerences require a diﬀerent modeling, which is summarized in Panel B of Table 2.

Table 2: Contract and Model Comparison of Our Stable Coins and Dual-Purpose Fund in U.S. and China

Panel A: Contract Comparison

Payment Style

Payment Style

Reset

Lifespan

of A Share

of B Share

Barriers

Underlying

Asset

Stock/

Stock Index

No

Finite

Yes

Inﬁnite

Stock Index

Yes

Inﬁnite

USD denominated

cryptocurrency

Single payment

at wind-up date

Payments aﬀect

the underlying

asset but not

the exchange ratio

Payments aﬀect

the exchange ratio

but not the

underlying asset

Pricing Model

Black-Scholes PDE

Periodic PDE, constant upper barrier

Dual-Purpose

Fund in U.S.

Dividend

Dual-Purpose

Fund in China

Fixed Income

Our Vanilla

A and B Coins

Fixed Income

Panel B: Model Comparison

Dual-Purpose Fund in U.S.

Ingersoll (1976)

Jarrow and O’Hara (1989)

Dual-Purpose Fund in China

Dai, Kou, Yang, and Ye (2018)

Our Vanilla A and B Coins

Periodic PDE, time-dependent upper barrier

The dual-purpose funds in U.S. include those studied in Ingersoll (1976) and the prime and scores studied in Jarrow

and O’Hara (1989).

8

The blockchain technology behind cryptocurrencies can create signiﬁcant economic ben-

eﬁts in many applications. Cong and He (2018) showed that the blockchain technology can

provide and maintain “decentralized consensus”, which improves the functioning of the whole

system, reduces information asymmetry, and enhances competition. Yermack (2017) pointed

out that blockchains may oﬀer to corporation shareholders lower trading costs and more

visible ownership records and transfer of shares. Malinova and Park (2017) designed a ﬁnan-

cial market based on the blockchain technology that can give investors alternative ways of

managing the visibility of their holdings and trading intentions.

There are many papers and media articles discussed pros and cons of cryptocurrencies.

Using cryptocurrencies as a payment method has several beneﬁts. First, as pointed out in

Harvey (2016), the core innovation of cryptocurrencies like Bitcoin is the ability to publicly

verify ownership, instantly transfer the ownership, and to do that without any trusted in-

termediary. Therefore, cryptocurrencies reduce the cost of transferring ownership. Also, the

blockchain technology makes the ledger easy to maintain, reduces the cost of networking (see

Catalini and Gans (2016)), and is robust against attackers.5 The distributed ledger can result

in a fast settlement that reduces counterparty risk and improves market quality (see Khapko

and Zoican (2018)). Furthermore, since the transaction is recorded to the blockchain anony-

mously, cryptocurrencies help to protect the privacy of their users. The underlying technology

of cryptocurrencies may one day strengthen the menu of electronic payments options, while

the use of paper currency is phased out (see Rogoﬀ (2015)).

There are also some criticisms of cryptocurrencies. First, a payment system with cryp-

tocurrencies lacks a key feature, the conﬁdence that one can get his money back if he is

not satisﬁed with the goods he purchased. As pointed out in Grinberg (2011), Bitcoin is

5Indeed, an attacker needs to race with his CPU power against the whole system; if he fails behind in

the beginning, the probability of his catching up diminishes exponentially as the race goes on (see Nakamoto

(2008) and Grunspan and Perez-Marco (2018)).

9

unlikely to play an important role in the traditional e-commerce market, since consumers

typically do not care about the anonymity that Bitcoin provides; instead, they prefer a cur-

rency they are familiar with for most goods and services, and they want fraud protection.

Second, unlike government-backed systems, Bitcoin does not have identity veriﬁcation, audit

standards, or an investigation system in case something bad happens. For instance, one may

lose all his deposit in cryptocurrencies should his password get stolen, and there is no rem-

edy. Furthermore, Blockchain systems are not as trustworthy as they seem to be. Without

an intermediate, individuals are responsible for their own security precautions. Finally, it is

diﬃcult to value cryptocurrencies like Bitcoin6.

Here we want to point out that despite signiﬁcant drawbacks of cryptocurrencies, it is

generally agreed that the blockchain technologies are here to stay. However, blockchain

technologies automatically generate cryptocurrencies for the purpose of charging the services

provided by the system (such as fees incurred by all programming codes which are run on the

Ethereum network), crediting essential services to the system (such as the veriﬁcation services

provided by miners7), and of exchanging credits for services. Therefore, cryptocurrencies will

not disappear as long as blockchain technologies exist. Thus, designing suitable stable coins

is essential for the blockchain system to perform ﬁnancial functions eﬃciently and for doing

asset allocation across diﬀerent cryptocurrencies generated by diﬀerent blockchain systems.

In this regard, governments can provide an essential role in helping design a better ﬁnancial

ecosystem of blockchains.

6By considering the equilibrium in the case where Bitcoin is the only currency in the economy and the

case with two currencies, Garratt and Wallace (2018) found that the value of Bitcoin lies upon self-fulﬁlling

beliefs, and the set of beliefs that can be self-fulﬁlling needs to be huge.

7Easley, O’Hara, and Basu (2017) and Huberman, Leshno, and Moallemi (2017) study mining fees on the

Bitcoin system.

10

2 Product Design

In this section, we introduce the detailed design of our stable coin, including its cre-

ation/redemption and its cash ﬂow. We also point out several diﬀerences between the product

and the dual-purpose funds in U.S. and in China.

2.1 Vanilla Class A and B Coins

Our stable coin has a dual-class split structure which, combined with smart contract rules

and market arbitrage mechanism, provides the holders of each class with principal-guaranteed

ﬁxed incomes and leveraged capital gains, respectively. The Class A Coin behaves like a bond

and receives periodical coupon payments. The Class B Coin entitles leveraged participation

of the underlying cryptocurrency. Simply put, this split structure means that the holders

of Class B coins borrow capital from the holders of Class A coins and invest in a volatile

cryptocurrency. Furthermore, a set of upward and downward reset clauses is imposed, where

downward resets reduce default risk of Class B to protect Class A, and upward resets ensure

a minimum leverage ratio of Class B to make Class B attractive to leverage investors.

For illustration we choose ETH as the underlying cryptocurrency, and the initial leverage

ratio is set to 2.8 Class A and B coins can be created by depositing ETHs to a custodian

smart contract.9 Upon receiving two shares of underlying ETH at time t, the Custodian

contract will return to the depositor βtP0 of Class A and Class B coins each, where P0 is the

initial price of underlying ETH in USD at the inception of the coins (t = 0), and βt is the

8The design of a contract with a general initial leverage ratio is discussed in Appendix A.
9A custodian smart contract can perform multiple tasks that facilitate key mechanism of the system,

including: creation and redemption of the stable coin, safekeeping the underlying digital assets (e.g. ETH),

calculation of stable coins’ net values, and execution of Reset events. The deposited underlying cryptocurrency

is kept by the custodian smart contract, as collateral of the Class A and Class B coins issued by the contract.

Any user or member of the public can verify the collateral and coins issued through third party applications

such as Etherscan.io.

11

time-t conversion factor. We set β0 = 1, which means that two shares of ETH can initially

exchange for P0 shares of Class A and Class B each. The conversion factor βt changes only

on upward/downward resets or regular payout dates, and the change rule will be introduced

later. To withdraw ETH at time t, holders of Class A and Class B coins can send, e.g., βtP0

shares of Class A and Class B coins each to the Custodian contract, then the contract will

deduct the same amount of Class A and Class B coins, and return to the sender two ETHs.

For instance, if the initial ETH/USD price is 500 and βt = 1, then two shares of ETH can

create 500 shares of Class A coins and Class B coins each, and 500 shares of Class A and B

coins each can be redeemed into two shares of ETH. Figure 2 illustrates this split structure.

Figure 2: Class A and B, Initial Split. At time t, one share of Class A and B each invests $1 in ETH. The initial ETH

price is P0 = $500, and the prevailing conversion factor βt = 1. So two shares of ETH exchange for 500 shares of Class

A coins and 500 shares of Class B coins.

To describe the cash ﬂow of Class A and B coins, we introduce the net asset dollar values

of Class A and B coins, VA and VB. Thanks to the exchange between ETH and Class A/B

coins, the following parity relation holds at any time:

A + V t
V t

B =

2Pt
βtP0

,

(2.1)

where Pt is the prevailing price of underlying ETH in USD. The net asset value of Class A

12

coins at time t is deﬁned as

V t
A = 1 + R · vt,

(2.2)

where R is the daily coupon rate, and vt is the number of days from the inception, last reset,

or last regular coupon payout date. The above design ensures that the initial net asset values

of Class A and B coins are both equal to one dollar.

2.1.1 Regular Payout

Assume regular coupons are paid every T days. When vt− = T , i.e., V t−

A = 1 + RT , a

regular payout is triggered, then the holder of each Class A coin receives payment with dollar

value RT ,10 and the net asset value of Class A resets to $1, namely, V t+

A = 1. Since no cash

ﬂow occurs for Class B coin upon regular payout, the net asset value of Class B remains

unchanged, that is, V t−

B = V t+

B . Noting that the parity relation (2.1) always holds across

regular payout, we deduce that the conversion factor β experiences a jump upon regular

payout:

βt+ =

2Pt
2Pt − βt−P0RT

βt−.

For instance, assuming R = 0.02%, T = 100, and P0 = $500, a regular coupon payout occurs

at time t when Pt = $450 and βt− = 1, then Class A receives $0.02 coupon payment, and the

conversion ratio is reset to βt+ = 1.011, which indicates that two shares of ETH can exchange

for 505.62 shares of Class A and 505.62 shares of Class B after the regular payout. This is

illustrated in Figure 3.

2.1.2 Upward Reset

An upward reset is triggered when the net asset value of Class B coins reaches the prede-

termined upper bound, denoted by Hu. On an upward reset time t, net asset value of both

10Payments are made in the form of underlying ETH from the Custodian contract. For instance, upon

regular payout, the holder of each Class A coin receives underlying ETH with amount RT
Pt

.

13

Figure 3: Class A and B, Regular Payout. After 100 days, the ETH price drops to $450, so that total investment of

one Class A coin and one Class B coin becomes $1.8, within which $1.02 belongs to Class A. A regular payout takes

place, and Class A receives $0.02 coupon payment. New exchange ratio: 2 shares of ETH now correspond to 505.62

(= 500 ×

2×450

2×450−500∗0.02 ) shares of Class A and 505.62 shares of Class B, yielding βt+ = 1.011.

classes resets to 1 USD, Class A and B’s holders will receive payments of value V t

A − 1 and

V t
B − 1, respectively, and conversion factor βt+ is reset to Pt/P0 so that after the upward reset

two shares of ETH can exchange for Pt share of class A and B. For instance, as illustrated in

Figure 4, after another 50 days, the ETH price grows to $760.96, so the net asset value of the

Class B grows to Hu ≡ $2, triggering an upward reset. The holders of Class A and B receive

payments with amount $0.01 and $1, respectively. Two shares of ETH now correspond to

760.96 shares of Class A and 760.96 shares of Class B, yielding βt+ = 1.52.

Figure 4: Class A and B, Upward Reset. After 50 days, the ETH price grows to $760.96, and Class B NAV grows to

$2, triggering an upward reset. Class A NAV equals $1.01, where $0.01 is 50-day accrued coupon. On this date, Class

A receives $0.01 coupon payment, and Class B receives $1 dividend payment. New exchange ratio: 2 shares of ETH

now correspond to 760.96 shares of Class A and 760.96 shares of Class B, yielding βt+ = 760.96/500 = 1.52.

14

2.1.3 Downward Reset

A downward reset is triggered when the net asset value of Class B coins reaches the

predetermined lower bound, denoted by Hd, On a downward reset time t, Class A holders

receive a payment with dollar value V t

A − Hd, and 1/Hd shares of Class A and B are merged

into one share of Class A and B, respectively, so that the net asset value of both classes

resets to $1. The conversion factor βt+ resets to Pt/P0, that is, two ETHs can exchange for

Pt shares of Class A and B after the reset. For instance, as illustrated in Figure 5, after

another 50 days, the ETH price drops to $479.40, so that the net asset value of Class B

drops to Hd ≡ $0.25, triggering a downward reset. Class A receives $0.01 coupon payment

and $0.75 principal payback, and then both classes undergo a 4:1 merger. Two shares of

ETH now correspond to 479.40 shares of Class A and 479.40 shares of Class B, yielding

βt+ = 479.40/500 = 0.96.

Under a black swan event, the net asset value of Class B coins V t

B is likely lower than

Hd or even becomes negative upon downward reset. In the case of V t

B > 0, we can simply

replace Hd by V t

B for the above description of cash ﬂow and operations on downward reset.

If V t

B ≤ 0, then both classes are fully liquidated, the holders of Class B receive nothing, and

the holders of Class A receive the payment V t

A − |V t

B|.

No arbitrage implies that the market prices of Class A and B coins also satisfy the parity

relation:

W t

A + W t

B =

2Pt
βtP0

,

where WA and WB are the market prices of the Class A and B coins, respectively. This has

an interesting implication: Suppose the demand of Class B coins is low, then the market

value of Class B coins would be low, and the above parity relation implies that the market

value of the Class A coins would be high.

Class A coin behaves like a bond. Although Class A has a ﬁxed coupon rate and its

15

Figure 5: Class A and B, Downward Reset. After another 50 days, the ETH price drops to $479.40, and Class B NAV

drops to $0.25, triggering an downward reset. Again, Class A NAV equals $1.01, where $0.01 is 50-day accrued coupon.

On this date, Class A receives $0.01 coupon payment, as well as $0.75 principal payback. Then, Class A and B each

undergo a 4:1 merger, so that both have NAV equal to $1. New exchange ratio: 2 shares of ETH now correspond to

479.40 shares of Class A and 479.40 shares of Class B, yielding βt+ = 0.96.

coupon payment is periodic and protected by the downward resets, its value is still volatile

on non-coupon dates. This is because the coupon rate is usually higher than the risk-free

rate, and on a downward reset, a portion of Class A coin will be liquidated, then the holder

of Class A will lose high coupons that would be generated from this portion. Therefore, a

potential downward reset will make the price of Class A volatile. We will propose two types

of more stable coins: A(cid:48) coins (Section 2.2) and A0 coins (see Appendix D).

2.2 Class A(cid:48) and B(cid:48) Coins

This extension splits Class A into two sub-classes: Class A(cid:48) and B(cid:48) . Both classes invest

in Class A coins. At any time, two Class A coins can be split into one Class A(cid:48) coin and one

Class B(cid:48) coin. Conversely, one Class A(cid:48) coin and one B(cid:48) coin can be merged into two Class

A coins. The split structure for Class A(cid:48) and B(cid:48) resembles that for Class A and B: Class

B(cid:48) borrows money from Class A(cid:48) at the rate R(cid:48) to invest in Class A. Here R(cid:48) is set to be close

to the risk-free rate r, whereas the rate R for Class A is generally much higher.

Class A(cid:48) and B(cid:48) resets when and only when Class A resets or gets regular payout. Class

16

Figure 6: Top Figure: What happens to Class A(cid:48) on a regular payout date of A. On regular payout dates for Class A

(per 100 days), 2 shares of A receives coupon payment $0.04, i.e. at daily rate 0.02%. $0.0082 is paid to A(cid:48) and $0.0318

to B(cid:48) . Middle Figure: Upward Reset of Class A(cid:48) . After 50 days, Class B’s net asset value grows to $2, triggering an

upward reset. Bottom Figure: Downward Reset of Class B(cid:48) . After another 50 days, Class B’s net asset value drops
17

to $0.25, triggering an downward reset.

A(cid:48) gets coupon at the rate R(cid:48) on regular payouts, upward and downward reset (provided that

the net asset value of Class B is positive then), and Class B(cid:48) gets coupon at the rate 2R − R(cid:48)

on upward reset. On downward resets, each share of both Class A(cid:48) and B(cid:48) is reduced to (V t

B)+

share, and Class A(cid:48) gets the value of the liquidated shares (i.e., 1 − (V t

B)+ shares). In the

extreme case where V t

B ≤ 0, then both Class A(cid:48) and B(cid:48) are fully liquidated, and A(cid:48) receives

its full net asset value 1 + R(cid:48)t, or the remaining total asset for A(cid:48) and B(cid:48) , 2(1 + Rt − |V t

B|),

whichever is smaller. Class A(cid:48) behaves like a money market account, except in extreme case,

when the underlying asset suddenly jumps (not smooth transit) to close to zero. Using the

same example as in Section 2.1, Figure 6 illustrates the cash ﬂow of Class A(cid:48) and B(cid:48) coins.

2.3 Diﬀerences from the Dual-Purpose Fund Contract

There are four main diﬀerences between our stable coin with dual-purpose funds in China.

First, in China a dual-purpose fund and its underlying fund share the same fund managers,

hence the fund managers re-scale the price of the underlying fund upon upward and downward

resets and regular payouts, in order to easily ensure the no arbitrage parity relation between

the dual-purpose fund and the underlying fund. Since we cannot change the underlying ETH

price, we instead change the exchange ratio of the shares between the underlying ETH and

Class A and B coins in our case, to maintain no-arbitrage across upward and downward resets

and regular payouts.

Second, for the dual-purpose funds, the upward reset is triggered by the underlying up-

crossing Hu while the downward reset is triggered by the net asset value of B share down-

crossing Hd. In contrast, for our stable coin, the triggering conditions of both upward and

downward resets are all based on the net asset value of Class B coins. This is because unlike

the re-scaled underlying fund price in China, the underlying ETH price is not so appropriate

as the net asset value of Class B to measure the leverage ratio of Class B.

Third, the underlying funds of Chinese dual-purpose funds incur management fees, whereas

18

the underlying ETH does not. Finally, the periodic payout of dual-purpose fund is annually

at a ﬁxed date (e.g. ﬁrst trading day of each year), while the periodic payout of our Class

A coins happens when a pre-speciﬁed time has passed from the last reset or payout event,

which reduces the frequency of payouts, making the coins more stable.

3 Valuation

This section is devoted to the valuation of coins described in Section 2, including Class A,

B, A(cid:48) , and B(cid:48) coins. We study their fair values in terms of a stochastic representation and

the corresponding partial diﬀerential equation (PDE) under the geometric Brownian motion

assumption.

3.1 Class A and B coins

Denote the relative price St = Pt/(βtP0). Let W t

A and W t

B be the market value of Class A

coins and B coins, respectively. Then the parity relation can be rewritten as W t

A + W t

B = 2St,

which allows us to focus on the valuation of Class A coins.

Since the future cash ﬂow of the coins depends on the cumulative time from last payment

(namely, last reset or last regular payout), rather than the calendar time, in the remaining

of this chapter we shall relabel the last payment time as 0, so that t ∈ [0, T ] denotes the

time from last payment. Denote by Hd(t) = 1

2 (1 + Rt) + 1

2 Hd and Hu(t) = 1

2 (1 + Rt) + 1

2 Hu

the downward reset barrier and the upward reset barrier (associated with St), respectively.

Hence the downward (upward) reset is triggered when St hits Hd(t) (Hu(t)). It is easy to

see Hd(t) ≤ St ≤ Hu(t) if St changes continuously. By design, S returns to 1 on every reset

date, and is reduced by 1

2 RT on every regular payout date.

Using the standard option pricing theory, the market value of Class A coins, W t

A ≡

19

WA(t, S), is given recursively as11

WA(t, S) = Et

(cid:34)
e−r(T −t)[RT + WA(0, ST − RT /2)] · 1{T <τ ∧η}

+ e−r(τ −t)[Rτ + WA(0, 1)] · 1{τ ≤T ∧η}

(3.1)

+ e−r(η−t)[Rη + 1 − |V η

B| + (V η

B)+WA(0, 1)] · 1{η≤T ∧τ }

(cid:35)

,

where r is the risk-free rate, random times τ and η represent the ﬁrst upward and downward

reset date from t, respectively (i.e., τ = inf{ξ ≥ t : Sξ ≥ Hu(ξ)} ≡ inf{ξ ≥ t : V ξ

B ≥ Hu} and

η = inf{ξ ≥ t : Sξ ≤ Hd(ξ)} ≡ inf{ξ ≥ t : V ξ

B ≤ Hd}), and Et is the expectation computed

under a risk-adjusted measure and under the initial condition St = S. For example, one can

assume that P follows a geometric Brownian motion under the risk-adjusted measure:

dPt = rPtdt + σPtdBt,

(3.2)

where Bt is a one-dimensional standard Brownian motion.12

The value of Class A coin can be determined as above in a recursive manner, since the

holders still get (certain shares of) Class A coin as well as coupons after reset or regular

payout. On the right hand side of (3.1), the ﬁrst term indicates that on the regular payout

date T , holders get coupon payment RT and a new Class A coin for which the time from

last payment returns to 0 and S is reduced by RT /2; the second term indicates that upon

upward reset time τ , holders get coupon payment Rτ and a new Class A coin for which the

time from last payment returns to 0 and S becomes 1; and the third term indicates that

upon downward reset time η, holders receive coupon payment Rη, withdrawal value 1 − |V η
B|,

11We denote x ∧ y = min{x, y}.
12If one assumes that complete hedging is possible, then the risk adjust measure is exactly the risk-neutral

measure. However, even if one does not use the complete hedging argument, the standard option pricing

theory using the rational expectations still gives the same dynamics, except that the risk free rate r is now

endogenously determined in equilibrium by other factors, e.g. an outside endowment process; see, e.g. Kou

(2002).

20

and (V η

B)+ shares of new Class A coin for which the time from last reset returns to 0 and S

becomes 1.

It is straightforward to estimate WA through (3.1) using Monte Carlo simulation, which is

also suggested by Adams and Clunie (2006) to deal with the complexities in fund contracts.

Due to the high volatility of the underlying cryptocurrency price, it is important to achieve

real-time calculation of WA. However, a simulation-based method is not so eﬃcient for this

purpose, since the cash ﬂow of Class A coins has an inﬁnite horizon and a weakly path-

dependent nature. Therefore, in the following we propose an eﬃcient PDE-based estimation

method to compute WA under the geometric Brownian assumption (3.2). Since there is no

overshoot by a diﬀusion process, VB always equals Hd on downward reset. Therefore, (3.1)

can be simpliﬁed to

WA(t, S) = Et

(cid:34)
e−r(T −t)(RT + WA(0, ST − RT /2)) · 1{T <τ ∧η}

+ e−r(τ −t)(Rτ + WA(0, 1)) · 1{τ ≤T ∧η}

(3.3)

+ e−r(η−t)(Rη + 1 − Hd + HdWA(0, 1)) · 1{η≤T ∧τ }

(cid:35)
.

It can be shown that WA is governed by the following periodic PDE with nonlocal terminal

and boundary conditions (see Appendix B):

−

∂WA
∂t

=

1
2

σ2S2 ∂2WA

∂S2 + rS

WA(T, S) = RT + WA(0, S −

∂WA
∂S
1
2

RT ),

− rWA,

0 ≤ t < T, Hd(t) < S < Hu(t)

(3.4)

Hd(T ) < S < Hu(T )

WA(t, Hu(t)) = Rt + WA(0, 1),

0 ≤ t ≤ T

WA(t, Hd(t)) = Rt + 1 − Hd + HdWA(0, 1),

0 ≤ t ≤ T.

(3.5)

(3.6)

(3.7)

It is easy to see that the terminal and boundary conditions (3.5) – (3.7) are directly related

with the cash ﬂow of Class A coins. Note that these conditions depend on the solution WA

itself. Such nonlocal terminal and boundary conditions make the PDE problem signiﬁcantly

21

diﬀerent from the classical Black-Scholes model, leading to challenges in both theory and

computation. On the theoretical aspect, due to the nonlocal conditions, the linkage between

the stochastic representation (3.3) and the PDE problem (3.4) – (3.7) is not straightforward,

and no analytical solution is available. On the numerical aspect, the nonlocalness makes

the problem nonlinear, which motivates us to propose an eﬃcient iterative procedure to ﬁnd

numerical solutions (see Appendix C).

3.2 Class A(cid:48) and B(cid:48) Coins

Denote by WA(cid:48) (t, S) and WB(cid:48) (t, S) the market prices of Class A(cid:48) and B(cid:48) coins, respec-

tively. Since two shares of Class A coin exchange for one A(cid:48) coin and one B(cid:48) coin, i.e.,

2WA(t, S) = WA(cid:48) (t, S) + WB(cid:48) (t, S), in the following we only discuss the valuation of Class

A(cid:48) coin. Under the risk-neutral pricing framework, WA(cid:48) (t, S) is given recursively as

(cid:34)
e−r(T −t)(R(cid:48)T + WA(cid:48) (0, ST − RT /2)) · 1{T <τ ∧η}

Et

+ e−r(τ −t)(R(cid:48)τ + WA(cid:48)(0, 1)) · 1{τ ≤T ∧η}

+ e−r(η−t) (cid:0)min{R(cid:48)η + 1 − (V η

B)+, 2(Rη + 1 + V η

B)+} + (V η

B)+WA(cid:48)(0, 1)(cid:1) 1{η≤T ∧τ }

(cid:35)
,

(3.8)

where τ and η are the ﬁrst upward and downward reset of Class A (or equivalently, Class

A(cid:48) and B(cid:48) ) after t, respectively. On downward reset, if V η

B > 0, Class A(cid:48) receives coupon R(cid:48)η,

1−V η

B shares of A(cid:48) is liquidated, and A(cid:48) receives the liquidation value; if R(cid:48)η−1

2 −Rη ≤ V η

B ≤ 0,

A(cid:48) is fully liquidated, and still receives full net asset value; otherwise, A(cid:48) is fully liquidated

and takes a loss by receiving 2(1 + Rη + V η

B)+ which is smaller than its net asset value 1 + Rη.

Recall that Class A will suﬀer a loss if V η

B < 0 on downward reset, therefore Class A(cid:48) is

safer than Class A since it can still recover its full net asset value in this case, provided

B ≥ R(cid:48)η−1
V η

2 − Rη; only when V η

B < R(cid:48)η−1

2 − Rη will Class A(cid:48) take a loss.

22

Assuming that Pt follows a geometric Brownian motion, it is easy to see that (3.8) reduces

to

(cid:34)
e−r(T −t)(R(cid:48)T + WA(cid:48) (0, ST − RT /2)) · 1{T <τ ∧η}

Et

+ e−r(τ −t)(R(cid:48)τ + WA(cid:48)(0, 1)) · 1{τ ≤T ∧η}

+ e−r(η−t) (cid:0)R(cid:48)η + 1 − Hd + HdWA(cid:48)(0, 1)(cid:1) · 1{η≤T ∧τ }

(cid:35)

.

Similar to the linkage between (3.3) and (3.4)-(3.7), we deduce that WA(cid:48)(t, S) satisﬁes the

following PDE:

1
2

∂WA(cid:48)
∂t

σ2S2 ∂2WA(cid:48)

−

=

∂S2 + rS
WA(cid:48)(T, S) = R(cid:48)T + WA(cid:48)(0, S −

∂WA(cid:48)
∂S
1
2

RT ),

− rWA(cid:48),

0 ≤ t < T, Hd(t) < S < Hu(t)

Hd(T ) < S < Hu(T )

WA(cid:48)(t, Hu(t)) = R(cid:48)t + WA(cid:48)(0, 1),

0 ≤ t ≤ T

WA(cid:48)(t, Hd(t)) = R(cid:48)t + 1 − Hd + HdWA(cid:48)(0, 1),

0 ≤ t ≤ T.

4 Numerical Examples

For illustration, we use Ethereum (ETH) as the underlying cryptocurrency, during the

period from 1 Oct 2017 to 28 Feb 2018.13 We further assume that the price is monitored on a

daily basis, and the upward and downward resets are performed according to the end-of-day

13The dual class structure of the stable coin is independent of the choice of underlying cryptocurrency;

however, the liquidity and popularity of the underlying price pair do impact the viability of the structure as

market arbitrage is important to ensure the structure trades as designed. In this paper, ETH/USD is used as

the underlying price pair, but other popular ERC20 tokens, such as EOS, ADA, paired with major ﬁat other

than USD, can also be considered.

23

prices. The default model parameters are given as follows.

R = 0.02% (7.3% p.a.)

R(cid:48) = 0.0082% (3% p.a.)

Hu = 2 Hd = 0.25

r = 0.0082% (3% p.a.)

σ = 0.0628 (120% p.a.)

T = 100.

4.1 Market Values of Class A and Class B

We ﬁrst compute the market values of Class A and Class B coins, based on the geometric

Brownian motion assumption and on the historical prices of ETH. Figure 7 shows that,

although Class A has a ﬁxed coupon rate, and its coupon payment is periodic and protected

by the resets, its value is still volatile on non-coupon dates. This should be compared to the

behavior of a junk bond, whose value is inﬂuenced by its issuer’s credit risk. In contrast, the

main risk of Class A is not credit risk, but the risk of a downward reset. On a downward

reset, a portion of Class A coins will be liquidated, so the investor will lose the value of future

coupons that would be generated from this portion. Therefore, an approaching downward

reset will pull down the value of Class A. This is illustrated in Figure 7 at the end of January:

as the downward reset approaches, the value of Class A also goes down, especially when the

model underestimates the ETH volatility (by setting σ = 0.0262 per day (annualized 0.5)).

Figure 8 shows the simulated paths from Class B coins. Note that Class B has upward

resets (on 24 Nov 2017, 17 Dec 2017, and 7 Jan 2018) with dividend payments $1.0846,

$1.0467, and $1.1106 and downward resets on (7 Jan 2018).

4.2 Market Value of Class A(cid:48) and B(cid:48)

We can see from Figure 9 that the market value of Class A(cid:48) coins is very stable during our

sample period, with a value close to 1, except for four downward jumps. These downward

jumps correspond to the coupon payment of Class A(cid:48) on the reset dates of Class A. If we

24

Figure 7: Simulated class A Market Value. σ = 0.0628 for the blue solid curve, σ = 0.0262 for the red dashed curve.

Parameters: R = 0.02%, Hd = 0.25, Hu = 2, T = 100, r = 0.0082% per day (3% per year). Upward reset takes place

on 24 Nov 2017, 17 Dec 2017, and 7 Jan 2018. Downward reset takes place on 5 Feb 2018.

Figure 8: Class B Market Value. σ = 0.0628 for the blue solid curve, σ = 0.0262 for the red dashed curve. Parameters:

R = 0.02%, Hd = 0.25, Hu = 2, T = 100, r = 0.0082% per day (3% per year). Upward reset takes place on 24 Nov

2017, 17 Dec 2017, and 7 Jan 2018. Downward reset takes place on 5 Feb 2018.

de-trend the value of Class A(cid:48) by its net asset value and consider WA(cid:48) − VA(cid:48) , it has an

annualized standard deviation of 5.4 × 10−5, which is much smaller than that of WA − VA

(0.0178). Even without de-trending, Class A(cid:48) has an annualized return volatility of 0.87%,

which is comparable to that of the short term U.S. treasury bill, 0.96% (912828K2 Govt,

from April 2015 to February 2018).

25

OctNovDecJanFebMar11.021.041.061.08OctNovDecJanFebMar0.40.60.811.21.41.61.82Figure 9: Market Value of Class A(cid:48) (red) and B(cid:48) (yellow), compared with Class A (blue). Annualized volatility of Class

A(cid:48) and B(cid:48) are 0.0087 and 0.0403, respectively. Parameters: R = 0.02% per day, Hd = 0.25, Hu = 2, R(cid:48) = 0.0082% (3%

per year), T = 100, σ = 120% per year, r = 0.0082% per day. Upward reset takes place on 24 Nov 2017, 17 Dec 2017,

and 7 Jan 2018. Downward reset takes place on 5 Feb 2018.

4.3 Black Swan Events

Assume that at time η, an extreme event happens, and there is a 80% sudden drop in the

ETH price. Assuming βη− = 1, Pη− = P0 = 500 (so that the relative price Sη− = 1), and P

suddenly drops to Pη = 100. Then the net asset value of Class A coins V η

A = 2Sη−·(1−80%) =

0.4, while the net asset value of Class A(cid:48) coins is V η

A(cid:48) = 2 · V η

A = 0.8. A downward reset is

triggered, Class A and Class A(cid:48) are fully liquidated, and they receive $0.4 and $0.8 payout,

respectively. Therefore, when a sudden drop in ETH price occurs, although both Class A

and A(cid:48) take a loss, A(cid:48) still recovers a larger value than A.

Now we assume that this kind of downward jump occurs in a jump diﬀusion model.

Speciﬁcally,

dPt/Pt− = rdt + σdBt + dJt,

where J is a compound Poisson process with constant intensity 0.2 (per 100 days) and

constant jump size −80%. Using simulation based on (3.1) and (3.8), we have at time 0,

WA(0, 1) = 0.888 and WA(cid:48) (0, 1) = 0.962; in contrast, if there is no jump risk (intensity

26

OctNovDecJanFebMar11.021.041.061.08WAWAWBequals 0), WA(0, 1) = 1.013, WA(cid:48) (0, 1) = 1.000. Therefore, the presence of extreme jump

risk has a smaller impact on Class A(cid:48) coins.

5 Conclusion

Stable coins, which are cryptocurrencies pegged to other stable ﬁnancial assets, are desir-

able for blockchain networks to be used as public accounting ledgers for payment transactions

and as crypto money market accounts for asset allocation involving cryptocurrencies, whereby

being often called the “Holy Grail of cryptocurrency.” However, existing cryptocurrencies,

such as Bitcoins, are too volatile for these purposes. By using option pricing theory, this

paper designs, for the ﬁrst time to our best knowledge, several dual-class structures that

oﬀer entitlements to either ﬁxed income stable coins (class A funds) pegged to a traditional

currency or leveraged investment opportunities (class B funds). The design is inspired by the

dual-purpose funds popular in the U.S. and China. Unlike traditional currencies, the new

class A funds record all transactions on a blockchain without centralized counterparties. By

using the option pricing theory, we show that the proposed stable coins indeed have very low

volatility. Indeed, the class A coin has a volatility comparable to that of the exchange rate of

world currencies against U.S. dollar, and the class A(cid:48) coin essentially is pegged to U.S. dollar.

When combined with insurance from a government, the design can also serve as a basis for

issuing a sovereign cryptocurrency.

References

Adams, A. T., and J. B. Clunie (2006): “Risk Assessment Techniques for Split Capital

Investment Trusts,” Annals of Actuarial Science, 1, 7–36.

Al-Naji, N. (2018): “Basecoin: A Price-Stable Cryptocurrency with an Algorithmic Central

Bank,” http://www.getbasecoin.com/basecoin_whitepaper_0_99.pdf.

27

Bech, M. L., and R. Garratt (2017):

“Central Bank Cryptocurrencies,” https:

//papers.ssrn.com/abstract=3041906.

Catalini, C., and J. S. Gans (2016): “Some Simple Economics of the Blockchain,” NBER

Working Paper, http://www.nber.org/papers/w22952.

Cong, L. W., and Z. He (2018): “Blockchain Disruption and Smart Contracts,” To Appear

in Review of Financial Studies.

Dai, M., S. Kou, and C. Yang (2017): “A Stochastic Representation for Nonlocal Parabolic

PDEs with Applications,” Working Paper.

Dai, M., S. Kou, C. Yang, and Z. Ye (2018): “The Overpricing of Leveraged Products:

A Case Study of Dual-Purpose Funds in China,” Working Paper.

Duffie, D. (2010): Dynamic Asset Pricing Theory: Third Edition. Princeton University

Press.

Easley, D., M. O’Hara, and S. B. Basu (2017): “From Mining to Markets: The Evolution

of Bitcoin Transaction Fees,” Working Paper.

Garratt, R. (2016): “CAD-coin versus Fedcoin,” R3 Report.

Garratt, R., and N. Wallace (2018): “Bitcoin 1, Bitcoin 2, ...: An Experiment in

Privately Issued Outside Monies.,” Economic Inquiry, forthcoming.

Grinberg, R. (2011): “Bitcoin: An Innovative Alternative Digital Currency,” https://

papers.ssrn.com/abstract=1817857.

Grunspan, C., and R. Perez-Marco (2018): “Double Spend Races,” Working Paper.

Harvey, C. R. (2016): “Cryptoﬁnance,” https://papers.ssrn.com/abstract=2438299.

28

Huberman, G., J. Leshno, and C. Moallemi (2017): “Monopoly without a Monopolist:

An Economic Analysis of the Bitcoin Payment System,” Working Paper.

Hull, J. C. (2017): Options, Futures, and Other Derivatives. Pearson Education.

Ingersoll, J. E. (1976): “A Theoretical and Empirical Investigation of the Dual Purpose

Funds: An Application of Contingent-claims Analysis,” Journal of Financial Economics,

3, 83–123.

Ingersoll, J. E. (1987): Theory of Financial Decision Making. Rowman & Littleﬁeld.

Jarrow, R. A., and M. O’Hara (1989): “Primes and Scores: An Essay on Market Imper-

fections,” The Journal of Finance, 44, 1263–1287.

Jarrow, R. A., and S. M. Turnbull (1999): Derivative Securities: The Complete In-

vestor’s Guide. Thomson Learning.

Khapko, M., and M. Zoican (2018): “Smart Settlement,” https://papers.ssrn.com/

abstract=2881331.

Kou, S. G. (2002): “A Jump Diﬀusion Model for Option Pricing,” Management Science,

48, 1086–1101.

MakerTeam (2017): “The Dai Stablecoin System,” https://makerdao.com.

Malinova, K., and A. Park (2017): “Market Design with Blockchain Technology,” https:

//papers.ssrn.com/abstract=2785626.

Nakamoto, S. (2008): “Bitcoin: A Peer-to-Peer Electronic Cash System,” https://

bitcoin.org/bitcoin.pdf.

Rogoff, K. (2015): “Costs and Beneﬁts to Phasing out Paper Currency,” NBER Macroe-

conomics Annual, 29(1), 445–456.

29

Shreve, S. E. (2004): Stochastic Calculus for Finance II. Springer Science Business Media.

Tether (2016): “Tether: Fiat Currencies on the Bitcoin Blockchain,” https://tether.to/

wp-content/uploads/2016/06/TetherWhitePaper.pdf.

Yermack, D. (2017): “Corporate Governance and Blockchains,” Review of Finance, 21(1),

7–31.

30

Online Supplement

Designing Stable Coins

A Product Design with General Split Ratio

In Section 2, we have described a speciﬁc product design where Class A is stable relative

to USD as target ﬁat currency and Class B has initial leverage as 2 (α = 1). In addition,

transaction cost in creation and redemption is omitted.

In this section, a general case is

discussed.

Dual-class coins can be created by depositing underlying cryptocurrency to the Custodian

contract. Upon receiving underlying cryptocurrency of amount MC, the Custodian contract

will return to the sender certain amount of Class A and Class B coins. Such amount CA and

CB can be calculated by:

CB =

MCP0βt (1 − c)
1 + α

,

CA = αCB,

(A.1)

where c is the processing fee of the smart contract, α is a positive number to determine the

ratio of A and B, and P0 is the recorded price of underlying cryptocurrency in target ﬁat

currency at last reset event, and βt is the conversion factor set as 1 at inception and its

behaviour is detailed later in Section A.1 to A.2.

Holders of Class A and Class B coins can withdraw deposited underlying cryptocurrency

at any time by performing a redemption. To do this, the user will send αC amount of Class

A coins and C amount of Class B coins to the Custodian contract. The contract will deduct

Class A and Class B coins, and return to the sender MC underlying cryptocurrency, where

MC can be calculated by:

MC =

C (1 − c) (1 + α)
βtP0

.

(A.2)

The net value of coins are calculated based on the coupon rate, the elapsed time from

last reset event, and the latest underlying cryptocurrency price in target ﬁat currency fed to

A–1

the system. In particular:

V t
A = 1 + R · vt,

V t
B = (1 + α) ·

Pt
βtP0

− α · V t
A,

(A.3)

where R is the daily coupon rate, vt is the number of days from last reset event, and Pt is

the current price of underlying cryptocurrency in target ﬁat currency. Note that at all time

Qt

A = αQt

B , where Qt

A and Qt

B are the total amount of Class A and Class B coins. The

implied leverage ratio is

Lt

B =

Pt
βtP0

·

1 + α
V t
B

Note that at inception or after contingent resets, above simply reduces to L0

B = 1 + α.

A.1 Regular Payout

A regular payout is triggered when vt− = T . Upon regular payout:

1. Total amount of both classes coin remain unchanged, Qt+

A = Qt−

A and Qt+

B = Qt−

B

2. Net asset value of Class A reset to 1 USD

3. Class A holder will receive certain amount of underlying cryptocurrency from the Cus-

todian contract. Such amount for each Class A coin is UA = V t
A−1
Pt

4. Conversion factor βt+ = βt− ·

(1+α)Pt

(1+α)Pt−αβt−P0(V t

A−1)

Total value in the system is unchanged after reset:

UA · Pt · Qt−

A + Qt+

A · V t+

A + Qt+

B · V t+

B

= (cid:0)V t−

A − 1(cid:1) · Qt−

A + Qt−

A · 1 + V t−

B · Qt−

B

=V t−

A · Qt−

A + V t−

B · Qt−
B .

A–2

A.2 Contingent Upward Reset

An upward reset is triggered when V t
B

(cid:62) Hu. Upon upward reset:

1. Total amount of both classes coins remain unchanged, Qt+

A = Qt−

A and Qt+

B = Qt−
B .

2. Net asset value of both classes reset to 1 target ﬁat currency.

3. Both classes’ holders will receive certain amount of underlying cryptocurrency from the

Custodian contract. Such amount for each Class A coin is UA = V t
A−1
Pt
Class B coin is UB = V t
B−1
Pt

.

and for each

4. Conversion factor βt+ is reset to Pt/P0.

Total value in the system is unchanged after reset:

UA · Pt · Qt

A + UB · Pt · Qt

B + Qt+

A · V t+

A + Qt+

B · V t+

B

= (cid:0)V t

A − 1(cid:1) · Qt

A + (cid:0)V t

B − 1(cid:1) · Qt

B + Qt

A · 1 + Qt

B · 1

=V t

A · Qt

A + V t

B · Qt

B .

A.3 Contingent Downward Reset

A downward reset is triggered when V t
B

(cid:54) Hd. Upon downward reset:

1. Total amount of Class B coins is reduced to Qt+

B = Qt−

B · (V t

B)+.

2. Total amount of Class A coins is reduced to Qt+

A = Qt+

B · α.

3. Net Value of both classes reset to 1 target ﬁat currency.

4. Class A holders will receive certain amount of underlying cryptocurrency from the

Custodian contract. Such amount of each Class A coin is: DA = V t
DA = V t

if V t

B/α

B < 0

A+V t
Pt

A−V t
B
Pt

if V t

B ≥ 0, and

5. Conversion factor βt+ is reset to Pt/P0.

A–3

Total value in the system is unchanged after reset:

A + Qt+

A + Qt+

B · V t+

B

DA · Pt · Qt−
(cid:104)(cid:0)V t

A − V t
B

=

(cid:1) · 1V t

A · V t+
B≥0 + (cid:0)V t

A + V t

B/α(cid:1) · 1V t

B<0

(cid:105)

· Qt−

A + Qt+

B · α · 1 + Qt+

B · 1

=V t

A · Qt−

A − (V t

B)+ · Qt−

B · α − (V t

B)− · Qt−

B + Qt−

B · (V t

B)+ · α + Qt−

B · (V t

B)+

=V t

A · Qt−

A + V t

B · Qt−
B .

Note above used the fact Qt−

A = Qt−

B · α.

In the absence of arbitrage, the following price parity shall hold

α · W t

A + W t

B = α · V t

A + V t

B ,

where W t

A is the current price of Class A in target ﬁat currency, and W t

B is the current price

of Class B in target ﬁat currency.

B Derivation of the Pricing Equation

Using contract design under general split ratio α > 0, similar to (3.1), the value of Class

A coins is described by the stochastic representation

(cid:34)

WA(t, S) = Et

e−r(T −t)(RT + WA(0, ST − αRT /(1 + α))) · 1{T <τ ∧η}

+ e−r(τ −t)(Rτ + WA(0, 1)) · 1{τ ≤T ∧η}

(B.1)

+ e−r(η−t)(Rη + 1 − |V η

B| + (V η

B)+WA(0, 1)) · 1{η≤T ∧τ }

(cid:35)

.

Note that (B.1) becomes (3.1) when α = 1. In this section, under the geometric Brownian

motion assumption, we show that (B.1) deﬁnes a unique bounded function WA, which is

exactly the solution to the PDE problem (3.4) – (3.7) when α = 1. We denote vs and Ys as

the time from last regular payout or reset and the number of A shares at time s, respectively.

Starting from an initial value 1, Y is reduced by a factor of Hd on every downward reset

A–4

dates (thanks to the geometric Brownian motion assumption), reﬂecting the partial payback

of Class A principal. In this remaining of this section, we focus on the right limit process St+,

which is still denoted as St for simplicity of notations. Further denote ζi, τi, and ηi as the

i-th regular payout date, upward reset date, and downward reset date after t, respectively.

From the construction of contract, we have

dSt = rStdt + σStdBt,

Sζi = Sζi− −

α
α + 1

Rvζi−, Sτi = Sηi = 1, vτi = vηi = vζi = 0,

where B is a Brownian motion under the risk-neutral measure.

First, we derive the following proposition, which expresses the stochastic representation

(B.1) into a non-recursive form.

Proposition 1. Equation (B.1) deﬁnes a unique solution WA(t, S) for 0 ≤ t ≤ T , Hd(t) ≤

S ≤ Hu(t), which can be written as

WA(t, S) = E(t,S,1)

t

(cid:34)

(cid:88)

ζi≥t

e−r(ζi−t)Yζi−RT +

e−r(τi−t)Yτi−Rvτi−

(cid:88)

τi≥t

e−r(ηi−t)Yηi−(Rvηi− + 1 − Hd)

(cid:35)
,

+

(cid:88)

ηi≥t

(B.2)

where E(u,s,y)

t

and Yt− = y.14

is the Q-expectation computed under the initial condition vt− = u, St− = s,

Proof of Proposition 1. Without loss of generality we prove the case T = 1. We prove this

theorem in three steps.

14If t and S are such that t is a regular payout or downward/upward reset date, the right hand side of (3.1)

is viewed as the value of the time-t payment plus the expectation with the value of state variables immediately

after the jump (if applicable) as time-t starting values.

A–5

Step 1: To see that WA given by (B.2) satisﬁes (B.1), note that (B.2) implies

WA(t, S) = Et,S,1

t

(cid:34)

(cid:88)

t≤ζi<τ1∧η1

e−r(ζi−t)Yζi−R + e−r(τ1−t)Yτ1−Rvτ1− · 1{τ1<η1}

+ e−r(η1−t)Yη1−(Rvη1− + 1 − Hd) · 1{η1<τ1}

+ e−r(τ1∧η1−t)Yτ1∧η1E

(0,1,Yτ1∧η1 )
τ1∧η1

(cid:32)

(cid:88)

ξi≥τ1∧η1

e−r(ζi−τ1∧η1) Yζi−
Yτ1∧η1

R

+

+

(cid:88)

τi>τ1∧η1

(cid:88)

ηi>τ1∧η1

e−r(τi−τ1∧η1) Yτi−
Yτ1∧η1

Rvτi−

e−r(ηi−τ1∧η1) Yηi−
Yτ1∧η1

(Rvηi− + 1 − Hd)

(cid:33)(cid:35)
,

where E(u,s,y)

τ1∧η1 denotes the conditional expectation computed at time τ1∧η1 with (v, S, Y )τ1∧η1 =

(u, s, y). As a result,

E

(0,1,Yτ1∧η1 )
τ1∧η1

(cid:34)

(cid:88)

ξi≥τ1∧η1

e−r(ζi−τ1∧η1) Yζi−
Yτ1∧η1

R +

(cid:88)

+

ηi>τ1∧η1

e−r(ηi−τ1∧η1) Yηi−
Yτ1∧η1

(Rvηi− + 1 − Hd)

e−r(τi−τ1∧η1) Yτi−
Yτ1∧η1

Rvτi−

(cid:88)

τi>τ1∧η1
(cid:35)(cid:35)

= E(0,1,1)
0

(cid:34)

(cid:88)

ξi≥0

e−rζiYζi−R +

(cid:88)

τi≥0

e−rτiYτi−Rvτi−

(cid:35)
e−rηiYηi−(Rvηi− + 1 − Hd)

(cid:88)

+

ηi≥0

= WA(0, 1),

where the ﬁrst equality follows from the Markov property of (v, S, Y ) and the fact that time

0 cannot be an interest payment date given (v, S, Y )0 = (0, 1, 1). Plugging this equation into

A–6

the previous equation, we get

WA(t, S) = E(t,S,1)

t

(cid:34)

(cid:88)

t≤ζi<τ1∧η1

e−r(ζi−t)Yζi−R + e−r(τ1−t)Yτ1−Rvτ1− · 1{τ1<η1}

(cid:35)
+ e−r(η1−t)Yη1−(Rvη1− + 1 − Hd) · 1{η1<τ1} + e−r(τ1∧η1−t)Yτ1∧η1WA(0, 1)

= E(t,S,1)
t

(cid:34)

(cid:88)

ζi<τ1∧η1

e−r(i−t)R + e−r(τ1−t)R(τ1 − (cid:98)τ1(cid:99) + WA(0, 1)) · 1{τ1<η1}

+ e−r(η1−t)(R(η1 − (cid:98)η1(cid:99)) + 1 − Hd + HdWA(0, 1)) · 1{η1<τ1}

(cid:35)

by the deﬁnition of v, Y , and ζ. This yields (B.1).

Step 2: Next we show that any solution WA satisfying (B.1) is a bounded function of (t, S)

in 0 ≤ t ≤ 1, Hd(t) ≤ S ≤ Hu(t). Indeed,

WA(t, S) = E(t,S,1)

t

(cid:34)

(cid:88)

1≤i<τ ∧η

e−r(i−t)R + e−r(τ −t)

R(τ − (cid:98)τ (cid:99))

(cid:32)

+ WA(0, 1)) · 1{τ <η}

+ e−r(η−t)(R(η − (cid:98)η(cid:99)) + 1 − Hd + HdWA(0, 1)

· 1{η<τ }

(cid:33)

(cid:35)

≤ E(t,S,1)
t

(cid:34)

(cid:88)

1≤i<τ ∧η

e−r(i−t)R

(cid:35)
+ e−r(τ ∧η−t)(R + max{WA(0, 1), 1 − Hd + HdWA(0, 1)})

≤

e−rR
1 − e−r + (R + max{WA(0, 1), 1 − Hd + HdWA(0, 1)}) := K.

Note that the right hand side does not depend on t or S.

Step 3: To see the uniqueness, for any WA satisfying (B.1), by deﬁning the ﬁrst interest

A–7

payment time θ1 = τ1 ∧ η1 ∧ 1, we get

WA(t, S) = E(t,S,1)

t

(cid:34)

(cid:32)

e−r(θ1−t)

(R + WA(0, Sθ1− − αR/(1 + α))) · 1{θ1<τ1∧η1}

+ (R(θ1 − (cid:98)θ1(cid:99)) + WA(0, 1)) · 1{θ1=τ1}

(cid:33)(cid:35)

+ (R(θ1 − (cid:98)θ1(cid:99)) + 1 − Hd + HdWA(0, 1)) · 1{θ1=η1}

= E(t,S,1)
t

(cid:34)

(cid:32)

e−r(θ1−t)

R · 1{θ1=ζ1} + Rvθ1− · 1{θ1=τ1}

+ (Rvθ1− + 1 − Hd) · 1{θ1=η1} + Yθ1WA(vθ1, Sθ1)

(cid:33)(cid:35)
.

Therefore,

WA(t, S)

= E(t,S,1)
t

(cid:34)(cid:32)

(cid:88)

ζi≤θ1

e−r(ζi−t)Yζi−R +

(cid:88)

τi≤θ1

e−r(τi−t)Yτi−Rvτi−

e−r(ηi−t)Yηi−(Rvηi− + 1 − Hd) + e−r(θ1−t)Yθ1WA(0, Sθ1)

(cid:33)(cid:35)
.

(cid:88)

+

ηi≤θ1

By plugging the expression for WA(0, 1) into the right hand side and using the Markov

property, one gets

WA(t, S) = E(t,S,1)

t

(cid:34)(cid:32)

(cid:88)

ζi≤θ1

e−r(ζi−t)Yζi−R +

(cid:88)

τi≤θ1

(cid:33)

e−r(τi−t)Yτi−Rvτi−

(cid:88)

+

ηi≤θ1

e−r(ηi−t)Yηi−(Rvηi− + 1 − Hd)

+ e−r(θ1−t)Yθ1E

(vθ1 ,Sθ1 ,Yθ1 )
θ1

(cid:34)(cid:32)

(cid:88)

θ1<ζi≤θ2

e−r(ζi−θ1) Yζi−
Yηi

R

+

+

(cid:88)

θ1<τi≤θ2

(cid:88)

θ1<ηi≤θ2

e−r(τi−θ1) Yτi−
Yθ1

Rvηi−

e−r(ηi−θ1) Yηi−
Yθ1

(Rvηi− + 1 − Hd) + e−r(θ2−θ1) Yθ2
Yθ1

WA(vθ2, Sθ2)

(cid:33)(cid:35)(cid:35)
.

A–8

Thus,

WA(t, S)

= E(t,S,1)
t

(cid:34)(cid:32)

(cid:88)

ζi≤θ2

e−r(ζi−t)Yζi−R +

(cid:88)

τi≤θ2

e−r(τi−t)Yτi−Rvτi−

e−r(ηi−t)Yηi−(Rvηi− + 1 − Hd) + e−r(θ2−t)Yθ2WA(vθ2, Sθ2)

(cid:33)(cid:35)
.

(cid:88)

+

ηi≤θ2

Repeating this for N times, we get

WA(t, S) = E(t,S,1)

t

(cid:34)

(cid:88)

t≤ζi≤θN

e−r(ζi−t)Yζi−R +

(cid:88)

t≤τi≤θN

e−r(τi−t)Yτi−Rvτi−

(cid:88)

+

t≤ηi≤θN

e−r(ηi−t)Yηi−(Rvηi− + 1 − Hd) + e−r(θN −t)YθN WA(vθN , SθN )

(B.3)

(cid:35)
,

where θN denotes the N -th interest payment time. Thanks to the boundedness of WA, we

have

0 ≤ lim
N →∞

E(t,S,1)
t

(cid:104)
e−r(θN −t)YθN WA(vθN , SθN )

(cid:105)

≤ K ·

lim
N →∞

E(t,S,1)
t

e−r(θN −t)(cid:105)
(cid:104)

= 0.

Here, to see the last equality, it suﬃces to note that (1) for two consecutive regular payouts

ζi, ζi+1, we have ζi+1 − ζi ≥ T , therefore Et,S,1

t

consecutive upward resets τi, τi+1, we have Et,S,1

t

(cid:2)e−r(ζi+1−ζi)(cid:3) ≤ e−rT := K1 < 1; (2) for two
(cid:2)e−r(τi+1−τi)(cid:3) = E0,1,1

[e−rτ1] := K2 < 1; (3)

0

for two consecutive downward resets ηi, ηi+1, we have Et,S,1

t

(cid:2)e−r(ηi+1−ηi)(cid:3) = E0,1,1

0

[e−rη1] :=

K3 < 1. Consequently, for k ≥ 1, we have

Et,S,1
t

(cid:104)

e−r(θ3k+3−θ3k)(cid:105)

≤ K1 ∧ K2 ∧ K3 < 1,

since there must be two regular payouts, upward resets or downward resets in θ3k, . . . , θ3k+3.

Therefore,

Et,S,1
t

(cid:104)

e−r(θ3k+3−t)(cid:105)

≤ ert · (K1 ∧ K2 ∧ K3)k → 0, as k → ∞,

A–9

and the claim follows from the monotonicity of (θk). Therefore, by sending N → ∞, we infer

that the right hand side of (B.3) converges to (B.2). This shows that any WA is equal to the

right hand side of (B.2), which gives the uniqueness of WA satisfying (B.1).

Theorem B.1. WA is the unique classical solution15 to the following partial diﬀerential

equation on {(t, S) : 0 ≤ t < T, Hd(t) < S < Hu(t)}

−

∂WA
∂t

=

1
2

σ2S2 ∂2WA

∂S2 + rS

WA(T, S) = RT + WA(0, S −

∂WA
∂S
α
1 + α

− rWA,

0 ≤ t < T, Hd(t) < S < Hu(t)

(B.4)

RT ),

Hd(T ) < S < Hu(T )

WA(t, Hu(t)) = Rt + WA(0, 1),

0 ≤ t ≤ T

WA(t, Hd(t)) = Rt + 1 − Hd + HdWA(0, 1),

0 ≤ t ≤ T.

(B.5)

(B.6)

(B.7)

Proof of Theorem B.1. Proposition 1 shows that we can rewrite (B.1) in a non-recursive form

as

WA(t, S) = E(t,S,1)

t

(cid:34)

(cid:88)

ζi≥t

e−r(ζi−t)Yζi−RT +

e−r(τi−t)Yτi−Rvτi−

(cid:88)

τi≥t

(cid:35)
e−r(ηi−t)Yηi−(Rvηi− + 1 − Hd)

,

+

(cid:88)

ηi≥t

where E(u,s,y)

t

is the Q-expectation computed under the initial condition vt− = u, St− = s,

and Yt− = y. So it remains to show that WA given as (B.2) is the unique classical solution to

(3.4) – (3.7). We prove this result based on the stochastic representation result for nonlocal

PDE, i.e. Corollary 3.1 in Dai, Kou, and Yang (2017), and in the following we ﬁrst establish

a connection between this theorem and (1).

We ﬁrst transform St to a process Xt ∈ [0, 1]:

Xt = Γ(vt, St) =

S − Hd(vt)
Hu(vt) − Hd(vt)

.

15By classical solution we mean WA ∈ C 1,2(Q)∩C(Q\D), where Q = {(t, S) : 0 ≤ t < T, Hd(t) < S < Hu(t)}

and D = {T } × {Hd(T ), Hu(T )}.

A–10

For X, the lower and upper limit becomes 0 and 1, respectively. X can be interpreted as the

relative distance of S to the lower limit Hd in [Hd(t), Hu(t)]. Under this transform, by Ito’s

formula, we have

where

dXs = b(vs, Xs)ds + σ(vs, Xs)dBs,

b(v, x) = r(x − 1) −

α
1 + α

R
Hu(t) − Hd(t)

+

rHu(t)
Hu(t) − Hd(t)

,

σ(v, x) =

σHd(t)
Hu(t) − Hd(t)

.

Besides, after this transform, the deﬁnition τi, ηi and ζi becomes

τi = inf{s > τi−1 : Xs− ≥ 1}, ηi = inf{s > ηi−1 : Xs− ≤ 0}

ζi = inf{s > ζi−1 : vs− = T, Xs− ∈ (0, 1)}.

On these dates, the change of X is described as

Xζi = Xζi−, Xτi = Xηi =

1 − Hd(0)
Hu(0) − Hd(0)

,

and on ηi, we have

Yηi = HdYηi−,

due to the reduction in the number of shares.

Now denote O = (0, 1),

g(x) =

1 − Hd(0)
Hu(0) − Hd(0)

· 1x=0,1(x)

˜νt,x = δ0,g(x)(ds, dz)

¯ν(t, x) = Hd · 1x=0(x) + 10<x≤1(x)

θi = inf{s > θi−1 : Xs− = 0 or Xs− = 1 or vs− = T }

x = Γ(t, S)

˜WA(t, x) = WA(t, S).

A–11

Also, the payouts of Class A coins at regular payout or reset dates can be expressed as

˜h(vθi−, Xθi−, ¯ν(Xθi−), where ˜h(v, x, u) = 1 − u + Rv. Using the above deﬁnitions, WA deﬁned

in (B.2) can be expressed as

˜WA(t, x) = Ex
t





(cid:88)

θi≥t

e−r(θi−t)Yθi−


˜h(vθi−, Xθi−, ¯ν(Xθi−))

 .

where Ex

t means the expectation calculated under Xt− = x, vt− = t and Yt− = 1. Then,

Corollary 3.1 in Dai, Kou, and Yang (2017) shows that ˜WA is the unique classic solution to

−

∂ ˜WA
∂t

−

1
2

σ2(t, x)

∂2 ˜WA
∂x2 − b(t, x)

∂ ˜WA
∂x

= 0

˜WA(T, x) = RT + ˜WA(0, g(x))

˜WA(t, 0) = 1 − ¯ν(0) + Rt + ¯ν(0) ˜WA(0, g(0))

˜WA(t, 1) = Rt + ˜WA(0, g(1))

in [0, T ) × (0, 1)

(B.8)

in (0, 1)

on [0, T ]

on [0, T ].

(B.9)

(B.10)

(B.11)

By reverting the transform (t, s) (cid:55)→ (t, x) =

(cid:16)

t,

s−Hd(t)
Hu(t)−Hd(t)

(cid:17)

, we conclude that WA deﬁned in

(B.1) is the unique classical solution to (3.4) – (3.7).

C Numerical Procedure for the Pricing Equation

We propose an iterative algorithm to obtain a numerical solution of the periodic parabolic

terminal-boundary value problem (3.4) – (3.7).

Algorithm 1

1. Set the initial guess W (0)

A = 0.

A–12

2. For i = 1, 2, · · · : Given W (i−1)

A

, solve for W (i)

A , the solution to the equation

− rWA

0 ≤ t < T, Hd(t) < S < Hu(t)

−

=

∂WA
∂t

σ2S2 ∂2WA

1
2
WA(1, S) =RT + W (i−1)

A

∂S2 + rS

∂WA
∂S
1
2

(0, S −

RT )

WA(t, Hu(t)) =Rt + W (i−1)

A

(0, 1)

WA(t, Hd(t)) =Rt + 1 − Hd + HdW (i−1)

A

(0, 1)

Hd(t) < S < Hu(t)

0 ≤ t ≤ T

0 ≤ t ≤ T.

3. If ||W (i)

A − W (i−1)

A

|| < tolerance, stop and return W (i)

A ; otherwise set i = i + 1 and go

to step 2.

The following theorem ensures the convergence of Algorithm 1.

Theorem C.1. The sequence (W (k)

A )k≥1 deﬁned in Algorithm 1 is monotonically increasing,

and it converges to WA uniformly.

Proof of Theorem C.1. We follow the notations in Section B. From the proof of Theorem

B.1, it suﬃces to consider the sequence ( ˜W (k)

A ) deﬁned via the transformed equation (B.8) –

(B.11) by iteration with ˜W (0)

A = 0. Indeed, once we show that ( ˜W (k)

˜WA, by reverting the transform (t, s) (cid:55)→ (t, x) =

(cid:16)

t,

s−Hd(t)
Hu(t)−Hd(t)

A ) converges uniformly to
(cid:17)

, we have that (W (k)

A ) also

converges uniformly to WA, which establishes the theorem. We shall do it in the following

two steps.

Step I. First, we show that the solution ˜W (k)

A (t, x) can be stochastically represented as

˜W (k)

A (t, x) = Ex
t





(cid:88)

e−r(θi−t)Yθi−


˜h(vθi−, Xθi−, ¯ν(Xθi−))

 .

t≤θi≤θk

Indeed, for k = 1, by Feynman-Kac representation for diﬀusion processes, the equation

σ2(t, x)

−

=

1
2

∂ ˜WA
∂t
˜WA(T, x) =RT

∂2 ˜WA
∂x2 + b(t, x)

∂ ˜WA
∂x

− r ˜WA

0 ≤ t < T, 0 < x < 1

˜WA(t, 1) =Rt

˜WA(t, 0) =Rt + 1 − Hd

A–13

0 < x < 1

0 ≤ t ≤ T

0 ≤ t ≤ T.

has a unique classical solution ˜W (1)

A ∈ C1,2(Q) ∩ C(Q\D), which can be represented as

˜W (1)

A (t, x) = Ex
t

(cid:104)

e−r(θ1−t)Yθ1−

(cid:105)
˜h(vθ1−, Xθ1−, ¯ν(Xθ1−))

.

This establishes the claim for k = 1. Now assume that this claim has been established for

k = i, i > 1. Then we have





Ex
t

(cid:88)

e−r(θj −t)Yθj −


˜h(vθj −, Xθj −, ¯ν(Xθj −))


t≤θj ≤θi+1

(cid:104)

= Ex
t

e−r(θ1−t)Yθ1−

e−r(θ1−t)E

+ Ex
t

(cid:105)
˜h(vθ1−, Xθ1−, ¯ν(Xθ1−))


vθ1 ,Xθ1 ,Yθ1
θ1

(cid:88)



θ1<θj ≤θi+1

e−r(θj −θ1)Yθj −


˜h(vθj −, Xθj −, ¯ν(Xθj −))






(cid:104)

= Ex
t

e−r(θ1−t)Yθ1−

˜h(vθ1−, Xθ1−, ¯ν(Xθ1−)) + e−r(θ1−t)Yθ1

˜W (i)

(cid:105)
A (vθ1, Xθ1)

,

where the last equality is from the Markov property and time-homogeneity of (v, X, Y ). On

the other hand, from the Feynman-Kac representation, the equation

−

=

∂ ˜WA
∂t

σ2(t, x)

1
2
˜WA(T, x) =RT + ˜W (i)

A (0, g(x))

∂2 ˜WA
∂x2 + b(t, x)

∂ ˜WA
∂x

− r ˜WA

0 ≤ t < T, 0 < x < 1

˜WA(t, 1) =Rt + ˜W (i)

A (0, g(1))

˜WA(t, 0) =Rt + 1 − Hd + Hd ˜W (i)

A (0, g(0))

0 < x < 1

0 ≤ t ≤ T

0 ≤ t ≤ T.

has a unique classical solution, ˜W (i+1)

A

, which can be represented as

˜W (i+1)
A

(t, x) = Ex
t

(cid:34)
e−r(θ1−t)Yθ1−

˜h(vθ1−, Xθ1−, ¯ν(Xθ1−))

+ e−r(θ1−t)Yθ1

˜W (i)

A (vθ1, Xθ1)

(cid:35)
.

Therefore,

˜W (i+1)
A

(t, x) = Ex
t





(cid:88)

e−r(θj −t)Yθj −


˜h(vθj −, Xθj −, ¯ν(Xθj −))

 ,

t≤θj ≤θi+1

A–14

and the claim is proved by induction.

Step II. Next we prove the uniform convergence of ( ˜W (k)

A ) to ˜WA. To see this,

| ˜W (k)
A (t, x) − ˜WA(t, x)|
(cid:12)
(cid:12)
(cid:12)
Ex
(cid:12)
t
(cid:12)
(cid:12)


e−r(θk−t) (cid:88)

θj >θk

=

e−r(θj −θk)Yθj −

(cid:12)

(cid:12)
(cid:12)
˜h(vθj −, Xθj −, ¯ν(Xθj −))
(cid:12)

(cid:12)
(cid:12)

≤ ¯K ·

sup
(t,x)∈[0,T )×(0,1)

e−r(θk−t)(cid:105)
(cid:104)

,

Ex
t

where ¯K is as deﬁned in the proof of Proposition 1.

We claim that the right hand side converges to 0. Suppose this claim is proved, we then

have the uniform convergence of ( ˜W (k)

A ) in [0, T ) × (0, 1). Using the terminal and boundary

conditions of the equation for ˜W (k)

A , ( ˜W (k)

A ) also converges uniformly on [0, T ] × [0, 1].

we have ζi+1 − ζi ≥ T , therefore Ex
t

To verify the claim, it suﬃces to note that (1) for two consecutive regular payouts ζi, ζi+1,
(cid:2)e−r(ζi+1−ζi)(cid:3) ≤ e−rT := K1 < 1; (2) for two consecutive
(cid:2)e−r(τi+1−τi)(cid:3) = Eg(1)

[e−rτ1] := K2 < 1; (3) for two

upward resets τi, τi+1, we have Ex
t

0

consecutive downward resets ηi, ηi+1, we have Ex
t

(cid:2)e−r(ηi+1−ηi)(cid:3) = Eg(0)

0

[e−rη1] := K3 < 1.

Consequently, for k ≥ 1, we have

(cid:104)

e−r(θ3k+3−θ3k)(cid:105)

Ex
t

≤ K1 ∧ K2 ∧ K3 < 1,

since there must be two consecutive regular payouts, upward resets or downward resets in

θ3k, . . . , θ3k+3. Therefore,

sup
(t,x)∈[0,T )×(0,1)

(cid:104)

e−r(θ3k+3−t)(cid:105)

Ex
t

≤ ert · (K1 ∧ K2 ∧ K3)k → 0, as k → ∞,

and the claim follows from the monotonicity of (θk).

D Class A0 and A1 Coins

In this extension, each Class A coin is split into one Class A0 coin and one Class A1 coin.

On the next coupon payment date or reset date t, Class A1 receives the coupon payment

A–15

for Class A, and then Class A1 is terminated. Class A0 is then split into Class A0 coin and

Class A1 coin, until the next reset when Class A1 receives payment and A0 is split again, so

on and so forth. At any time, the quantity of Class A0 and A1 maintains 1:1. At any time,

the value of Class A1 equals the expected discounted value of Class A’s next payment on

the next reset or coupon payment date. The value of Class A0 equals the diﬀerence between

values of Class A and A1. Using the same example as in Section 2.1, Figure 10 illustrates

the cash ﬂow of Class A0 and A1 coins.

By contract design, the coupon of Class A1 is delivered in the form of the underlying

cryptocurrency, whose value in USD may subject to volatile changes due to the high volatility

of ETH. In contrast, the coupon of Class A0 is paid in the form of Class A1 coins, whose

value in USD is much less volatile compared to ETH. Therefore, Class A0 is more suitable for

investors with lower risk tolerance or are less active on the market; upon receiving Class A1

coins as coupon, they have a relatively longer period of time to liquidate the coins before its

value changes noticeably. In contrast, Class A1 is more suitable for investors who are willing

to take certain degree of risk and are more active on the market; so that upon receiving the

underlying cryptocurrency, they can monitor the market actively and spot a good opportunity

to liquidate the underlying cryptocurency.

Under the risk-neutral pricing framework, the market value WA1(t, S) of Class A1 coin is

given as

(cid:34)

Et

e−r(ζ−t)RT · 1{ζ≤τ,η} + e−r(τ −t)Rτ · 1{τ <η,ζ}

+ e−r(η−t)(Rη − (V η

B)−)+ · 1{η<τ,ζ}

(cid:35)

,

where the ﬁrst regular payout time ζ, the ﬁrst upward reset time τ and the ﬁrst downward

reset time η are deﬁned as before. On a downward reset, if V η

B > 0, A1 gets the coupon

payment Rη; if V η

B ≤ 0, A1 only gets a part of the coupon (Rη + V η

B)+ < Rη.

By assuming that Pt follows a geometric Brownian motion, WA1 is the unique solution of

A–16

Figure 10: Top Figure: Class A0 receives no coupon. Class A1 receives all the coupon payment. After the coupon

payment, Class A1 is terminated, and 1 Class A0 is split into 1 new Class A0 and Class A1. Middle Figure: Upward

Reset of Class A0. After 50 days, Class B’s net asset value grows to $2, triggering an upward reset. Bottom Figure:

After another 50 days, Class B’s net asset value drops to $0.25, triggering a downward reset.

A–17

the following PDE

−

∂WA1
∂t

=

1
2

σ2S2 ∂2WA1

∂S2 + rS

∂WA1
∂S

− rWA1,

0 ≤ t < T, Hd(t) < S < Hu(t)

WA1(T, S) = RT,

WA1(t, Hu(t)) = Rt,

WA1(t, Hd(t)) = Rt,

Hd(T ) < S < Hu(T )

0 ≤ t ≤ T

0 ≤ t ≤ T.

Finally, the value of Class A0 coin is calculated as WA0 = WA − WA1.

Figure 11: Market Value of Class A0 compared to Class A. Annualized volatility of Class A0 is 0.0254. Parameters:

R = 0.02%, Hd = 0.25, Hu = 2, T = 100, σ = 120% per year, r = 0.0082% (3% per year). Upward reset takes place on

24 Nov 2017, 17 Dec 2017, and 7 Jan 2018. Downward reset takes place on 5 Feb 2018.

Figure 11 shows the simulated path for the prices of class A0, the principal only part of

A. A0 has an annualized standard deviation of 0.0412 for α = 1, as compared to that of WA,

which is 0.0531. Note that A0 is still volatile. To make A0 more stable, one can increase

the split ratio between A and B from 1:1 to a higher split ratio α : 1, (α > 1), resulting in a

lower leverage ratio for class B which in turn leads to a lower risk for Class A and Class A0,

because the risk of downside resets is lower. Figure 12 illustrates the price of A0 with α = 2.

Class A0 has an annualized standard deviation of 0.0156 for α = 2, as compared to that of

WA, which is 0.0571. Note that with α = 2, the net asset value of B is 3St − 2(1 + Rvt),

making B more sensitive to S.

A–18

OctNovDecJanFebMar11.021.041.061.08WAWA0Figure 12: Market Value of Class A0 (principal only class) compared to Class A, where the split ratio between Class

A and B coins is 2:1. Annualized volatility of Class A is 0.0125. Parameters: R = 0.02 per day, Hd = 0.25, Hu = 2,

T = 100, σ = 120% per year, r = 0.0082% (3% per year). Upward reset takes place on 24 Nov 2017, 17 Dec 2017, and

7 Jan 2018. Downward reset takes place on 5 Feb 2018.

A–19

OctNovDecJanFebMar11.021.041.061.08WAWA0