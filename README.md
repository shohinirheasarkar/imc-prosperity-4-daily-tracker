# imc-prosperity-4-daily-tracker

algorithmic trading — imc prosperity 4  
documenting my journey learning to trade!

---

## daily log

| day | date | concepts explored | action items | strategy ideas | backtest results |
|-----|------|-----------------|--------------|----------------|-----------------|
| 1 | 2025-03-30 | order books, market making, mean reversion, options, delta, black-scholes, implied vol | read a past writeup (done), write a notebook to do exploratory data analysis (done) | none yet, still exploring | none yet |
| 2 | 2025-03-31 | — | — | — | tired, taking the day off |
| 3 | 2025-04-01 | — | — | — | busy, taking the day off |
| 4 | 2025-04-02 | pair trading, arbitrage, market-taking, cointegration, following bots, cross-year data analysis, rolling mean, deviation analysis | update master strategy notes (done), complete tutorial eda notebook (done) | emeralds: market make around 10000. tomatoes: mean revert around rolling mean (w=200), threshold ±4.76 | emeralds: 3 price levels only (9996, 10000, 10004). tomatoes: deviation std=4.76, mean=0.03 — strong local mean reversion confirmed |
| 5-7 | 2025-04-03 to 2025-04-05 | — | — | — | mia, taking time off |
| 8 | 2025-04-12 | TradingState structure, order submission format, position limits, traderData persistence, market taking vs making, reversion speed analysis | write and submit trader.py (done) | emeralds: market make at 9998/10002 up to position limit 80. tomatoes: mean revert w=200 threshold ±4.0 order size 10, market take on signal | first submission uploaded — awaiting results |

---

## to-do for next session

- [ ] read & understand the full prosperity wiki thoroughly
- [ ] review current algo strategies and identify improvements
- [ ] read: https://github.com/MarkBrezina/Ctrl-Alt-DefeatTheMarket/blob/main/README.md
- [ ] check performance results from first submission and interpret logs
- [ ] tune tomato order size and threshold based on results
- [ ] confirm position limits from wiki for future rounds

---

## strategy notes

**market making**
- for stable products, post bids slightly below mid and asks slightly above mid, collect the spread
- the tighter and more stable the spread, the better this works
- watch for products with low price deviation — good market making candidates
- example: emeralds hover at exactly 10000 with only 3 price levels — textbook market making

**market taking / directional trading**
- if you can predict the next price move (via regression, rolling mean, or a signal), hit existing orders aggressively
- combine with market making: make in normal conditions, take when price is extreme
- for mean reversion, market taking is preferred — speed matters when median reversion time is only 13 timestamps

**mean reversion**
- if a price historically hugs a mean, buy when it dips below and sell when it rises above
- check visually with a rolling mean overlay — if the price keeps snapping back, mean reversion is viable
- implied volatility can mean-revert too (e.g. round 4 coconut coupons from past competitions)
- compute deviation from rolling mean — std of deviation is your trading threshold
- example: tomatoes deviation std~4.0, mean=0.03 — buy when deviation < -4.0, sell when deviation > +4.0
- median reversion time for tomatoes: 13 timestamps — very fast, trade aggressively

**pair trading / arbitrage**
- find two products with a structural or statistical relationship
- track the spread between them over time — if stable historically, trade deviations back toward the mean
- strongest when there is a fundamental reason for the relationship (e.g. basket = sum of components)
- cointegration is the formal statistical test for whether the relationship is stable
- you never know for certain the spread will revert — it is a probabilistic bet, not a guarantee

**following bots**
- watch which bots are consistently profitable and what they trade
- if a bot reliably buys lows and sells highs, mirror their actions
- small changes in bot behavior can be leading signals (e.g. dolphin sightings in prosperity 2023)

**cross-year data**
- check public github repos from past prosperity competitions for recycled price series
- run correlations between last year's symbols and this year's — r² near 1 is a massive edge
- if found, use a dp algorithm to optimally extract value given position limits and spread costs

**general principles**
- always ask: what is the source of edge here? if you can't explain it, it's probably noise
- prefer simple, explainable strategies over complex ones — less risk of overfitting on limited data
- build a backtester early — it multiplies your ability to test ideas quickly
- position limits change the optimal strategy — always factor them into your planning
- in a competition, your risk tolerance should match your standing — protect a lead, take risk when chasing

---

## concepts

| concept | status |
|---------|--------|
| order books | in progress |
| market making | in progress |
| mean reversion | in progress |
| rolling mean / deviation analysis | done |
| arbitrage / pair trading | in progress |
| traderData / state persistence | done |
| position limits | done |
| black-scholes | not started |
| implied volatility | not started |
| delta hedging | not started |
| dynamic programming for trading | not started |
| cointegration | not started |

---

## rounds

| round | products | strategy | pnl | status |
|-------|----------|----------|-----|--------|
| tutorial | tomatoes (tg01), emeralds (tg02) | emeralds: market make @ 9998/10002 limit 80. tomatoes: mean revert w=200 threshold ±4.0 size 10 | awaiting results | submitted |
| 1 | — | — | — | not started |

---

## resources

- [imc prosperity](https://prosperity.imc.com)
- [prosperity wiki](https://imc-prosperity.notion.site)
- [black-scholes — wikipedia](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
- [prosperity 2023 — stanford cardinal writeup](https://github.com/ShubhamAnandJain/IMC-Prosperity-2023-Stanford-Cardinal)
- [ctrl-alt-defeatthemarket writeup](https://github.com/MarkBrezina/Ctrl-Alt-DefeatTheMarket/blob/main/README.md)

---

*started 2025-03-30*
