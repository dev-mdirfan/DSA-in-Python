# Time Complexity Of A Computer Program

- [Time Complexity Of A Computer Program](#time-complexity-of-a-computer-program)
  - [What is Time complexity and What is its need?](#what-is-time-complexity-and-what-is-its-need)
  - [Which way do you think is better?](#which-way-do-you-think-is-better)
  - [Why is it so important?](#why-is-it-so-important)
- [2. How to Calculate Running Time?](#2-how-to-calculate-running-time)


## What is Time complexity and What is its need?

Let us take one example, suppose your friend picked a number between 1 to 1000 and he told you to guess the number. If your guess is correct he will tell you that it is correct, otherwise, if your guess is bigger than his number he would tell you that it's 'too big and if it is smaller than his number then he would tell you that it is ‘too small. Here are some ways by which we could find the number.

- We can guess each number from 1 to 1000, and see if it is correct.
- Otherwise, We can pick the middle number, if he says ‘too big’ then we know for sure that the number is on the left side so we can discard the right side, similarly if he says ‘too small’ we can discard the left side. We can repeat the same process until he says it's correct.

## Which way do you think is better?

As you might have guessed correctly, the 2nd way is actually way better than the first way. In the worst case, the 1st way would take 1000 guesses before we get the correct number ( if the number is 1000 ), while the 2nd way would only take 10 guesses in the worst case ( this is because at every guess we discard one of the halves).

Later you would see that the time complexity of the first way is __O(n)__ and that of the second way is __O(log n)__.

As we saw from the above example there can be multiple approaches to solving the same problem. The same applies to computer programming. For every approach (algorithm) the time taken, amount of space used, and computational power might be different. Therefore there has to be a way by which we can distinguish these different approaches (algorithms) and choose the one which is the most efficient.

In this article, we are going to speak about how we can choose the best algorithm based on the time taken by an algorithm to execute. But how do we compare the algorithms which are written in two __different languages__, running on two __different machines__? This is exactly why the concept of time complexity was introduced. But __`what is time complexity`__?

By definition, Time complexity is the time taken by an algorithm/program to run as a function of the length of the input.

## Why is it so important?

- It can clearly distinguish between two different algorithms based on their efficiency.
- It’s independent of the machine on which the algorithm is run.
- We can get a direct correlation with the length of the input.

__Note:__ It’s important to note here that time complexity __doesn’t really measure the actual time__ taken by an algorithm to run ( Since that kind of depends on the programming language, processing power etc.). It calculates the __execution time of an algorithm__ in terms of the algorithms and the inputs.

# 2. How to Calculate Running Time?

As we know the running time of an algorithm can depend on various factors such as the architecture of the computer (32 or 64-bit), single or multiple processors, read and write speed, configuration of the machine, input etc.

But for simplicity, we are just going to take input as a variable and keep the rest of the factors constant. Basically, we are going to assume our machine to have the following features:

(Single Processor, 32 bits, sequential execution, takes 1 unit of time for arithmetic and logical operations).





