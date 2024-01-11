## 1. Longest Conmmon Subsequence

**Input:** two array $A$ and $B$, whose length is $n$ and $m$.
**Output:** the longest common subsequence, if they do not share any common element, return 0.

(a) subproblem: $f(i,j)$ the length of the longest common subsequence for $A[:i]$ and $B[:j]$

(b) recurrence relation:
$$f(i,j) =  \left\{
\begin{aligned}
    & f(i-1,j-1) + 1 \quad \text{if }A[i] == B[i] \\
    \\
    & max(f(i,j-1),f(i-1,j)) \quad \text{else}
\end{aligned}
\right.$$

base case: $f(i,j) = 0, \text{if } i==0 \text{ or } j==0$

(c)
**Memories:** $\Omicron(nm)$
**Runtime:** $\Omicron(nm)$

(d)
bottom up order will reduce memory space into $\Omicron(2min(n,m))$, which we only store 2 row or 2 colum.

## 2. Set Cover

Ask to find the fewest number of sets to cover every elements in universe.

Given $m$ subsets and the universe has $n$ elements.

(a) naive solution: there are $2^n-1$ possible subsets for universe. Means worst $m==2^n$
And also $2^m$ possible ways to pick from $\{ S_1,\cdots, S_m\}$
And each combination takes $\Omicron(n\cdot m)$ to add and check.
so total runtime is $\Omicron(n \cdot m \cdot 2^m) = \Omicron(n\cdot 2^n \cdot 2^{2^n})$

(b) DP:
subproblem: $f(T,i)$ return the fewest number of sets to cover all elements in T using only sets $\{S_1,\cdots, S_i \}$. We need $f(U,m)$
$$f(T,i) = min\left\{
\begin{aligned}
    & f(T \backslash \{S_i\}, i-1) + 1, \text{ if use } S_i, \text{ takes } \Omicron(n)\\
    \\
    & f(T, i-1), \text{ if do not use } S_i, \text{ takes } \Omicron(1)
\end{aligned}
\right.
$$

(c)
**Memory space:** $\Omicron(m \cdot 2^n)=\Omicron(2^n\cdot 2^n)$, can be optimized into $\Omicron(2^n)$ from bottom up.
**Runtime:** $\Omicron(n \cdot m \cdot 2^n) = \Omicron(n\cdot 2^n\cdot 2^n)$

## 3. Finding More Counterexamples

In order to clarify we can't use greedy but DP algorithm.

(a) For the traveling salesman problem，first sort the adjacency list of each vertex by the edge weights. Then,run DFS $N$ times starting at a different vertex $u = 1,2,..N$ for each run.Every time we encounter a back edge, check if it forms a cycle of length N, and if it does then record the weight of the cycle. Return the minimum weight of any such cycle found so far.

* When the lightest weight edge are not in the total minimum weight path, this algorithm failed.

(b) For the Longest Increasing Subsequence problem， consider this algorithm: Start building the LIS with the smallest element in the array and go iterate through the elements to its right in order. Every time we encounter an element $A[i]$ that is larger than the current last element in our LIS, we add A[i] to the LIS.

* Failed When the smallest element are not in LIS. 

## 4. Ballon Popping Problem

(a)
subproblem: $f(i,j)$ return the maximum noise to popping ballon $A[i:j]$, we want $f(0,n)$
$$ \therefore
f(i,j) = \underset{k\in(i,j)}{max}(f(i,k) + f(k,j) + noisy(k-1,k,k+1))
$$

(b)
**Memory space:** $\Omicron(n^2)$
**Runtime:** $\Omicron(n^3)$


## 1. LP Basics

The canonical form of a linear program is
$$\begin{aligned}
    \text{minimize } & c^Tx \\
    \text{subject to } & Ax \geq b \\
    & x \geq 0
\end{aligned}
$$

(i) if the object is maximization: $\text{max }c^Tx \to \text{min }(-c)^Tx $
(ii) if we have constraint $Ax \leq b$ : $\to -Ax \geq b$
(iii) if $Ax = b$: $\to Ax\geq b \text{ and } -Ax \geq -b$
(iv) if $x \leq 0$: $\to z = -x \text{ and } z\geq 0$, replace all $x$ with $-z$.
(v) if $x\in \mathbb{R}$: replace $x$ with $x^+ - x^- \text{ and } x^+,x^- \geq 0$

## 5. Taking the Dual

The dual of the canonical LP is

$$\begin{aligned}
    \text{maximize } & b^Ty \\
    \text{subject to } & A^Ty \geq c \\
    & y \geq 0
\end{aligned}
$$

Construct the blow linear program into dual:
$$\begin{align}
    \text{max } 4x_1 & +7x_2 \\
    x_1+2x_2 & \leq 10 \\
    3x_1+x_2 & \leq 14 \\
    2x_1+3x_2 & \leq 11 \\
    x_1,x_2 & \geq 0
\end{align}
$$

**Naive way:**

1. multiply (2) (3) (4) with $y_1,y_2,y_3 \geq 0$ and then add them together

$$\Rightarrow
(y_1+3y_2+2y_3)x_1+(2y_1+y_2+3y_3)x_2 \leq 10y_1+14y_2+11y_3
$$

2. if we set

$$\begin{aligned}
    (y_1+3y_2+2y_3) & \geq 4 \\
    (2y_1+y_2+3y_3) & \geq 7 \\
\end{aligned}$$

$$
    \Rightarrow 4x_1  +7x_2 \leq 10y_1+14y_2+11y_3
$$

3. now we have the dual

$$\begin{aligned}
    \text{min } 10y_1+14y_2+ & 11y_3 \\
    y_1+3y_2+2y_3 & \geq 4 \\
    2y_1+y_2+3y_3 & \geq 7 \\
    y_1,y_2,y_3 & \geq 0
\end{aligned}
$$

**Using Matrix wey:**
Primal:
$$\begin{aligned}
max \begin{bmatrix} 4 & 7 \end{bmatrix} & \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \\
\begin{bmatrix}
    1&2\\3&1\\2&3
\end{bmatrix} \begin{bmatrix}
    x_1\\x_2
\end{bmatrix} & \leq \begin{bmatrix}
    10\\14\\11
\end{bmatrix} \\
x_1,x_2 &  \geq 0
\end{aligned}
$$

Dual:
$$\begin{aligned}
min \begin{bmatrix} 10&14&11 \end{bmatrix} & \begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix} \\
\begin{bmatrix}
    1&3&2\\2&1&3
\end{bmatrix} \begin{bmatrix}
    y_1\\y_2\\y_3
\end{bmatrix} & \geq \begin{bmatrix}
    4\\7
\end{bmatrix} \\
y_1,y_2,y_3 & \geq 0
\end{aligned}
$$

## 7. LP Meets Linear Regression

Ask to find the 
$$min\sum^n_{i=1}|y_i-(a+bx_i)|$$

The problem is to replace the absolute symbol, to do this, we can creat an new variables $z_i$

$$\begin{aligned}
    \text{min } & \sum^n_{i=1}z_i \\
    \text{subject to } & \left\{ \begin{aligned}
    z_i & \geq y_i-(a+bx_i) \\
    \\
    z_i & \geq -(y_i-(a+bx_i))
    \end{aligned}
    \right.
\end{aligned}
$$
