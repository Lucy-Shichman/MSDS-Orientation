# Central Limit Theorem
The CLT states that as the number of trials "n" increases, a binomial distrubtion with probability "p" approaches a normal distribution.
This can be illustrated using Numpy's random.normal and random.binomial functions.
### Proof of Concept:
Here is a binomial distribution where 10 trials (n=10) with a probability of 0.5 are repeated 100 times:
![binomial_dist_small_n](https://github.com/Lucy-Shichman/MSDS-Orientation/assets/98109381/2ec56c28-4bc9-49d1-aca3-0574f27b7ad2)

Here is the same binomial, except with 10,000 trials (n=10,000):
![binomial_dist_large_n](https://github.com/Lucy-Shichman/MSDS-Orientation/assets/98109381/a3318903-eab0-41c3-9f89-7976e5da8403)
