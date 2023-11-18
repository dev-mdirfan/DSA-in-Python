# Channa Sir Notes

## Day 1

(14-10-22)

- **Elon Musk :** First Principle of thinking all about you break down your all assumptions to lowest possible level of thinking and then build their solution up their. That is -
  - Understand problem better
  - then get brute force solution out of it which is kind of explain by the problem itself.
  - And then start reasoning what are the function need, what are functionality you need and then based on that you decide what kind of data structure are helpful and what kind of design techniques are helpful. (Ask Yourself)

- You don't need to know lot of things to be a very good problem solver but you need to ask good questions and to answer to that questions you need concepts
- But if you are good problem solver and their are bunch of people around you, who know lot of things about those concepts. When ask those questions they give better answer.
- Don't take short-cuts. Use this first principle approach every time.

|S.No|Question|Solution|
|---|---|---|
|1.||**[Python](/)**, **[C++](/)**, **[Java](/)**|

### Question 7

|S.No|Question|
|---|---|
|**7.**|**[567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)**|

#### Solution in Python

- Here, we have two string **s1** and **s2**.
- s2's substring contain permutation of s1.

**Algorithm :**

```algorithm
for each substring s of len k in s2         // O(n)
    if s in a permutation of s1            // O(n2) 
        return True
return False
```

- Here, In above approach `n-k+1` substring are generated which take linear time.

```py

```
