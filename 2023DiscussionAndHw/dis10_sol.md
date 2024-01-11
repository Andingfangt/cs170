## 1. Zero-Sum Game Short Answer

**Definition:** We say that a game is a *zero-sum game* if the sum of payoffs of all players is always zero.
In other words, if we have tow plyers $A$ and $B$, the payoff matrix $G_A = -G_B$, and the expected payoff $E_R = -E_C$

(a) If payoff matrix $M = -M^T$, means tow player have same payoff matrix.
$\therefore $ the expected payoff for row player $E_R = E_C$ the expected payoff for colum player, also it has relations $E_R = -E_C \Rightarrow E_R=0$

(b) True or False: If every entry in the payoff matrix is either 1 or -1 and the maximum number of 1s in any row is $k$, then for any row with less than $k$ 1s, the row player's optimal strategy chooses this row with probability 0. Justify your answer.

False. Example:$\begin{bmatrix}
    1&-1&1 \\
    -1&1&-1
\end{bmatrix}$ for colum player, every strategy is same, so for row player.

(c) True or False: Let $M_i$ denote the $i$th row of the payoff matrix. If $M_1=\frac{M_2+M_3}{2} $ , then there is an optimal strategy for the row player that chooses row 1 with probability 0.

True.
$Y=[y_1,y_2,y_3]^T,\therefore E_R = x_1M_1Y+x_2M_2Y+x_3M_3Y= x_1(\frac{M_2+M_3}{2})Y+x_2M_2Y+x_3M_3Y$
$\therefore x_1$ could be 0, and just factor $x_1$'s value into the coefficients of $M_2$ and $M_3$

## 2. Permutation Games

the optimal strategies for both players is pick it uniformly.

## 3. Zero-Sum Game

**payoff matrix:**
|Alice\Bob|1|2|
|:----:|----|----|
|1|4|1|
|2|2|5|

(a) Write the linear program for choosing Alice's strategy to maximize her payoff.
$x_1,x_2$ stand for Alice choice possibility for row1 and row2.
$\therefore$
$$
4x_1+2x_2 \quad\text{if Bob choose colum1}\\
x_1+5x_2 \quad\text{if Bob choose colum2}\\
$$
$\therefore$ for Bob, he will choose the $min(4x_1+2x_2,x_1+5x_2)$
for Alice, he will make $\underset{\forall x_1,x_2}{max} \{min(4x_1+2x_2,x_1+5x_2)\}$
$\therefore \text{ if we define }  p:=min(4x_1+2x_2,x_1+5x_2)$ We can write LP as follow.
$$\begin{aligned}
& max \quad p \\
& p \leq 4x_1+2x_2 \\
& p \leq x_1+5x_2  \\
& x_1+x_2 = 1 \\
& x_1, x_2\geq 0
\end{aligned}$$

(b) Write a linear program from Bob's perspective trying to minimizing Alice's payoff. Let the variables of the linear program be $y_1, y_2$ and $p$, where $y_i$ is the probability that Bob plays strategy $i$ and $p$ denotes Alice's payoff.

$$\begin{aligned}
    & min \quad p \\
    & p \geq 4y_1+y_2 \\
    & p \geq 2y_1+5y_2 \\ 
    & y_1+y_2 =1 \\
    & y_1,y_2 \geq 0
\end{aligned}$$

(c) LP in (a) and (b) are duals of each other.

(d) the optimal answer for above LP is: $x_1=x_2=\frac{1}{2}, p=3$

## 4. Bad Reductions

(a) The shortest simple path problem(SSPP) with non-negative edge weights can be reduced to the longest simple path problem(LSPP) by just negating the weights of all edges. There is an efficient algorithm for the shortest simple path problem with non-negative edge weights, so there is also an efficient algorithm for the longest path problem.

First part is correct, we can reduce SSPP to LSPP by negating all edges weights.
Second part is wrong, it should be if there is also an efficient algorithm for LSPP, we can say there is also an efficient algorithm for SSPP.

(b) We have a reduction from problem B to problem A that takes an instance of B of size $n$, and creates a corresponding instance of A of size $n^2$. There is an algorithm that solves A in quadratic time. So our reduction also gives an algorithm that solves B in quadratic time.

Should be $n^4$ time.

(c) We have a reduction from problem B to problem A that takes an instance of B of size $n$, and creates a corresponding instance of A of size $n$ in $\Omicron(n^2)$ time. There is an algorithm that solves A in linear time. So our reduction also gives an algorithm that solves B in linear time.

Should be $n^2$ time.

(d) Minimum vertex cover can be reduced to shortest path in the following way: Given a graph G, if the minimum vertex cover in G has size $k$, we can create a new graph $G'$ where the shortest path from $s$ to $t$ in $G'$ has length $k$. The shortest path length in $G'$ and size of the minimum vertex cover in $G$ are the same, so if we have an efficient algorithm for shortest path，we also have one for vertex cover.

... Only make the result answer $k$ to be same means we need to know the answer $k$ before we reduce, which is not possible.

## 2. Graph Coloring Problem

An undirected graph $G = (V,E)$ is $k$-colorable if we can assign every vertex a color from the set $1, … k$, such that no two adjacent vertices have the same color. In the $k$-coloring problem,we are given a graph $G$ and want to output “Yes” if it is $k$-colorable and “No” otherwise.

(a) Show how to reduce the 2-coloring problem to the 3-coloring problem. That is,describe an algorithm that takes a graph $G$ and outputs a graph $G'$, such that $G'$ is 3-colorable if and only if $G$ is 2-colorable. 'To prove the correctness of your algorithm, describe how to construct a 3-coloring of $G'$ from a 2-coloring of $G$ and vice-versa.(No runtime analysis needed).

How to reduce:
1. copy $G$ to $G'$
2. add a new vertex, which connected to all the other vertexes.
3. output $G'$

(b) The 2-coloring problem has a $O(|V|+|E|)$ time algorithm. Does the above reduction imply an efficient algorithm for the 3-coloring problem? If yes,what is the runtime of the resulting algorithm? If no, justify your answer.

No, cause we are reducing $2col \rightarrow 3col$, need algorithm for 3col.
**PS:** 3col is NP problem.

**Hint:** efficient reducing Problem A $\rightarrow$ B, means A is no harder than B.