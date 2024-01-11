## 1.  Planting Trees

(a)

* [10,0,0,10]
* [10,15,10]

(b) let $f(i)$ to be the maximum number of using spots 1 to i
$\therefore f(0) = 0, f(1) = x_1, f(2) = max(x_1,x_2)$

(c) If the best way to plant trees using only spots 1 to i does not place a tree in spot i:
$$f(i) = f(i-1)$$

 (d) If the best way to plant trees using only spots 1 to i places a tree in spot i.
 $$f(i) = x_i + f(i-2)$$

 (e)

 ```python
 def f(n)
 mem = [None] * n
 mem[0] = 0
 men[1] = x1

for i in range(2, n):
    case_c = mem[i-1] # If the best way to plant trees using only spots 1 to i does not place a tree in spot i
    case_d = mem[i-2] + xi # If the best way to plant trees using only spots 1 to i places a tree in spot i.

    mem[i] = max(case_c, case_d)

return mem[n]
 ```

## 2. Maximum Subarray Sum Revisited

**Example:** given $[-2,1,-3,4,-1,2,1,-5,4]$, the maximum subarray sum is 6, the contiguous subarray is $[4,-1,2,1]$

**Review:** dis02 give an $\Omicron(n\log n)$ algorithm, this time use *dynamic programming* to come out an $\Omicron(n)$ algorithm.

```python
def mss(A):
    n = len(A)
    mem_mss = [None] * n
    mem_mss[0] = A[0]
    for i in range(1, n):
        mem_mss[i] = max(mem_mss[i-1]+A[i], A[i])
    
    return max(mem_mss)
```

**Runtime:** $\Omicron(n)$

## 2. Copper Pipes

**Example:** 

| lenth | 1 | 2 | 3 | 4 | 5  | 6  | 7  | 8  |
|------:|---|---|---|---|----|----|----|----|
| price | 1 | 5 | 8 | 9 | 10 | 17 | 17 | 20 |

The the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6).

$$f(n) = max \left\{
\begin{aligned}
    & f(n-1) + p_1 \\
    & f(n-2) + p_2 \\
    & \vdots \\
    & f(1) + p_{n-1} \\
    & p_n \\
\end{aligned}
\right.$$

**Runtime:** $\Omicron(n^2)$