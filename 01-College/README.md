# Data Structure and Algorithms

## Understanding data structures and algorithms

- How algorithms manipulate information contained within data structures.
- How data is arranged in memory.
- What the performance characteristics of particular data structures are?

### Data Structures

we will look at:

- fundamentals of the Python programming language from the perspective of data structures and algorithms 
- have the correct mathematical tools.

Another important aspect is an evaluation. Measuring the performance of algorithms requires an understanding of how the increase in data size affects operations on that data. When we are working on large datasets or real-time applications, it is essential that our algorithms and structures are as efficient as they can be.

Finally, we need a strong experimental design strategy. Being able to conceptually translate a real-world problem into the algorithms and data structures of a programming language involves being able to understand the important elements of a problem and a methodology for mapping these elements to programming structures.

#### Understanding the importance of algorithmic thinking

Imagine we are at an unfamiliar market and we are given the task of purchasing a list of items. We assume that the market is laid out randomly, each vendor sells a random subset of items, and some of these items may be on our list. Our aim is to minimize the price for each item we buy, as well as minimize the time spent at the market. One way to approach this problem is to write an algorithm like the following: a simple iterator, with a decision and an action:

1. Does the vendor have items that are on our list and the cost is less than a predicted 
cost for that item?
1. If yes, buy and remove from list; if no, move on to the next vendor.
2. If no more vendors, end.

we would need data structures to define and store in memory both the list of items we want to buy and the list of items the vendor is selling.we would need data structures to define and store in memory both the list of items we want to buy and the list of items the vendor is selling

There are several observations that we can make regarding this algorithm. Firstly, since the cost calculation is based on a prediction, we don't know what the real cost is. As such, we do not purchase an item because we underpredicted the cost of the item, and we reach the end of the market with items remaining on our list. To handle this situation, we need an effective way of storing the data so that we can efficiently backtrack to the vendor with the lowest cost.

Also, we need to understand the time taken to compare items on our shopping list with the items being sold by each vendor. It is important because as the number of items on our shopping list, or the number of items sold by each vendor, increases, searching for an item takes a lot more time. The order in which we search through items and the shape of the data structures can make a big difference to the time it takes to do a search. Clearly, we would like to arrange our list as well as the order we visit each vendor in such a way that 
we minimize the search time.

Also, consider what happens when we change the buy condition to purchase at the cheapest price, not just the below-average predicted price. This changes the problem entirely. Instead of sequentially going from one vendor to the next, we need to traverse the market once and, with this knowledge, we can order our shopping list with regards to the vendors we want to visit.

Obviously, there are many more subtleties involved in translating a real-world problem into an abstract construct such as a programming language. For example, as we progress through the market, our knowledge of the cost of a product improves, so our predicted average-price variable becomes more accurate until, by the last stall, our knowledge of the market is perfect. Assuming any kind of backtracking algorithm incurs a cost, we can see cause to review our entire strategy. Conditions such as high price variability, the size and shape of our data structures, and the cost of backtracking all determine the most appropriate solution. The whole discussion clearly demonstrates the importance of data structures and algorithms in building a complex solution.

