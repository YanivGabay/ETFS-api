# Testing yifinance

yifinance is a Python library that fetched data from yahoo finance.

we will try to use it, to show a list of best etfs by performance,
with more useful information in a table.


## Helpfull links

- [History Dataframe](https://github.com/ranaroussi/yfinance/wiki/Ticker#history)


Should add calculation of compound investing and effects.

adding this chat gpt example for now as reference

1. Understanding Cumulative Returns vs. Summed Percentages

### a. Summing Percentages is Incorrect for Cumulative Returns

When you sum individual annual percentages, you're adding them together without considering the effect of compounding. This method underestimates the actual growth of an investment over time.

**Example:**

- Year 1: +10%
- Year 2: +10%

**Summed Return:** 10% + 10% = 20%

**Actual Cumulative Return:**

\[
(1 + 0.10) \times (1 + 0.10) - 1 = 21\%
\]

As you can see, summing gives 20%, while the actual cumulative return is 21%.

### b. Cumulative Returns Account for Compounding

Cumulative returns are calculated by compounding each year's return, which means each year's return builds upon the previous year's growth.

**Formula:**

\[
\text{Cumulative Return} = \left( \prod_{i=1}^{n} (1 + r_i) \right) - 1
\]

Where:

- \( r_i \) = Return in year \( i \)
- \( n \) = Number of years

**Applying to Your Data:**

Let's calculate the cumulative return correctly using compounding. Here's how you can do it step-by-step.
```

## Installation


## Usage



