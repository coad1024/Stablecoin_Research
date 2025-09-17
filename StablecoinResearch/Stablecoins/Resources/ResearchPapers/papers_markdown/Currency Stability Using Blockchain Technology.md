Currency Stability Using Blockchain Technology

Bryan R. Routledge∗
Ariel Zetlin-Jones†

[February 15, 2018]

Abstract

Arbitrary speculative attacks on currencies can arise from self-fulﬁlling expectations. This is a
well-studied source of currency crises. In this paper, we show that blockchain distributed ledger
technologies, such as those which support Bitcoin and Ethereum, can be adapted to eliminate self-
fulﬁlling speculative attacks on a currency. We show how to develop a stable currency peg, such
as Pesos to Dollars, using a cryptocurrency. We show the peg is immune to speculative attacks
arising from self-fulﬁlling prophecies and estimate the size of reserves and transaction costs needed
to support the peg.

Our blockchain mechanism builds on the work of Green and Lin (2003) where bank runs in a Dia-
mond and Dybvig (1983) setting are credibly prevented with contracts that depend on the order at
which individuals arrive at the bank. We show that a similar idea can be used to credibly support
a ﬁxed exchange rate in the canonical setting of Obstfeld (1996). As in Green and Lin, the key to
the credible policy is that the policy depends in a rich way on the order in which people demand
to exchange domestic currency for foreign denominated assets. Through this mechanism, the policy
maker can provide exchange for those requiring foreign denominated assets and discourage exchange
with those seeking purely speculative proﬁt.

The diﬃculty with implementing a Green and Lin mechanism to defend a currency peg is that it
is complicated. Specifying, communicating, and implementing such policies in practice is diﬃcult.
Here, we use the technology of “smart contracts” to implement the peg. “Smart contracts” are
rich state-contingent contracts that are credible since they are veriﬁed and enforced credibly by an
irreversible technology.

The Ethereum Network is the largest (measured by market capitalization) of smart contracting
environments. We use the Ethereum protocol to develop a quantitative exercise to measure the size
of reserves and transaction costs needed to support a ﬁxed exchange peg.

∗Tepper School of Business, Carnegie Mellon University; routledge@cmu.edu.
†Tepper School of Business, Carnegie Mellon University; azj@cmu.edu.

References

Diamond, D. W., and P. H. Dybvig (1983): “Bank runs, deposit insurance, and liquidity,”

Journal of political economy, 91(3), 401–419.

Green, E. J., and P. Lin (2003): “Implementing eﬃcient allocations in a model of ﬁnancial

intermediation,” Journal of Economic Theory, 109(1), 1 – 23.

Obstfeld, M. (1996): “Models of currency crises with self-fulﬁlling features,” European economic

review, 40(3-5), 1037–1047.

2

