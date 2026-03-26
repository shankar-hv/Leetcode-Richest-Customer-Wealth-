# 💰 Richest Customer Wealth

## 📌 Problem Statement

You are given an `m x n` integer grid `accounts` where:

- `accounts[i][j]` represents the amount of money the **i-th customer** has in the **j-th bank**.

### 🎯 Goal:
Return the **maximum wealth** among all customers.

A customer's wealth is the **sum of money in all their bank accounts**.

---

## 🧠 Approach

1. Traverse each customer (row in the grid)
2. Calculate the sum of each row
3. Track the maximum sum
4. Return the maximum value

---

## 🧮 Examples

### Example 1
```
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
```

### Example 2
```
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
```

### Example 3
```
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
```

---

## ⚙️ Constraints

- `m == accounts.length`
- `n == accounts[i].length`
- `1 ≤ m, n ≤ 50`
- `1 ≤ accounts[i][j] ≤ 100`

---

## 💻 Python Code

```python
def maximumWealth(accounts: List[List[int]]) -> int:
  sums = 0
  s = []
  for i in accounts:
    sums = sum(i)
    s.append(sums)
            
  return max(s)

```

---

## ⚡ Optimized Version

```python
class Solution:
    def maximumWealth(self, accounts):
        return max(sum(customer) for customer in accounts)
```

---

## ⏱️ Complexity Analysis

- Time Complexity: `O(m × n)`
- Space Complexity: `O(1)`

---

## 🚀 Key Points

- Simple 2D array traversal
- Focus on row-wise summation
- Beginner-friendly problem
