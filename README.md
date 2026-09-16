# Lorenz Curve & Gini Coefficient from Scratch

A small practice project implementing the **Lorenz curve** and **Gini coefficient**
from first principles using NumPy, then applying them to three different kinds
of data: synthetic income data, financial market data, and macroeconomic
(cross-country) data.

## Background

The **Lorenz curve** plots the cumulative share of a population (x-axis)
against the cumulative share of some quantity they hold — income, wealth,
trading volume, etc. (y-axis). A perfectly equal distribution is the 45°
diagonal; the more the curve sags below it, the more concentrated the
quantity is among a few units.

The **Gini coefficient** is a single number summarizing that gap:

```
Gini = 1 - 2 * (area under the Lorenz curve)
```

It ranges from 0 (perfect equality) to 1 (maximum inequality).

## Requirements

```
pip install numpy matplotlib yfinance wbdata --break-system-packages
```

## Key takeaways

- A Gini coefficient is only meaningful for quantities that represent a
  genuine "share of a total" (income, volume, GDP). Applying it to a raw
  price *level* over time is mathematically possible but not very
  economically meaningful — trading volume or absolute returns are more
  natural stand-ins when working with market data.
- When pulling data from an external API (World Bank, Yahoo Finance), always
  check whether the result includes non-target rows that shouldn't be
  counted — e.g. World Bank aggregates like "World" or "OECD members" mixed
  in with individual countries — before running any statistics on it.
- `np.insert()` and most other NumPy functions return a **new array** rather
  than modifying in place; forgetting to reassign the result is a common,
  silent source of bugs.
