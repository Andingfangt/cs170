## 1. FFT Intro
**RECALL:**  
&emsp;**Fast Fourier Transform!** *The Fast Transform* FFT($p,n$) takes arguments n, some power of 2, and $p$ is some vector [$p_0,p_1,....p_{n-1}$].  
&emsp;Treating $p$ as a polynomial $P(x)=p_0+p_1x+...+p_{n-1}x^{n-1}$, the FFT computes the value of $P(x)$ for all $x$ that are n-th roots of unity by doing the following matrix multiplication in $\Omicron(n\log n)$:
$$\begin{bmatrix}
    P(1)\\P(w_n)\\P(w_n^2)\\\vdots\\P(w_n^{n-1})
\end{bmatrix} = \begin{bmatrix}
    1&1&1&...&1\\1&w_n^1&w_n^2&...&w_n^{(n-1)}\\1&w_n^2&w_n^4&...&w_n^{2(n-1)}\\\vdots&\vdots&\vdots&\ddots&\vdots\\1&w_n^{(n-1)}&w_n^{2(n-1)}&...&w_n^{(n-1)(n-1)}
\end{bmatrix}\cdot \begin{bmatrix}
    p_0\\p_1\\p_2\\\vdots\\p_{n-1}
\end{bmatrix}$$
&emsp;If we let $E(x) = p_0+p_2x+..p_{n-2}x^{n/2-1}$ and $O(x) = p_1+p_3x+..p_{n-1}x^{n/2-1}$, then $P(x) = E(x^2)+xO(x^2)$, and then $FFT(p,n)$ can expressed as a divide-and-conquer algorithm:
1. Compute $E'=FFT(E,n/2)$ and $O'=FFT(O,n/2)$.
2. For $i=0\to(n-1)$, assign $P(w_n^i)\leftarrow E((w_n^i)^2)+ w_n^iO((w_n^i)^2)$
   Hint: $E((w_n^i)^2)=E(w_{n/2}^i)$ and $E(w_{n/2}^{i+n/2}) = E(w_{n/2}^i)$
```python
def FFT(p,n)
    """
    p is List of polynomial, n is power of 2.
    return a List of value of P(x).
    """
    # base case
    if n == 1:
        return a
    # compute w
    w_n = exp(i*2*pi/n)
    # divide into 2 parts
    p_e, p_o = [p0,p2,...,p_{n-2}], [p_1,p_3,...,p_{n-1}]
    # use FFT to both to get value List.
    y_e, y_o = FFT(p_e,n/2), FFT(p_o,n/2)
    # Initialize the array to store the results
    result = [0]*n
    # 
    for j in range(n/2):
        y[j] = y_e[j] + (w_n)^j*y_o[j]
        y[j+n/2] = y_e[j] - (w_n)^j*y_o[j] # w^{j+n/2} = -w^j

    return y
```
Also observe that:
$$\frac{1}{n}\begin{bmatrix}
   1&1&1&...&1\\ 1&w_n^{-1}&w_n^{-2}&...&w_n^{-(n-1)}\\ 1&w_n^{-2}&w_n^{-4}&...&w_n^{-2(n-1)}\\ \vdots&\vdots&\vdots&\ddots&\vdots \\ 1&w_n^{-(n-1)}&w_n^{-2(n-1)}&...&w_n^{-(n-1)(n-1)}
\end{bmatrix}=\begin{bmatrix}
    1&1&1&...&1\\ 1&w_n^{1}&w_n^{2}&...&w_n^{(n-1)}\\ 1&w_n^{2}&w_n^{4}&...&w_n^{2(n-1)}\\ \vdots&\vdots&\vdots&\ddots&\vdots \\ 1&w_n^{(n-1)}&w_n^{2(n-1)}&...&w_n^{(n-1)(n-1)}
\end{bmatrix}^{-1}$$
And so given the values $P(1),P(w_n),P(w_n^2),\cdots$, we can compute $P$ by doing the following matrix multiplication:
$$\begin{bmatrix}
p_0\\p_1\\p_2\\\vdots\\p_{n-1}
\end{bmatrix} = \frac{1}{n}\begin{bmatrix}
   1&1&1&...&1\\ 1&w_n^{-1}&w_n^{-2}&...&w_n^{-(n-1)}\\ 1&w_n^{-2}&w_n^{-4}&...&w_n^{-2(n-1)}\\ \vdots&\vdots&\vdots&\ddots&\vdots \\ 1&w_n^{-(n-1)}&w_n^{-2(n-1)}&...&w_n^{-(n-1)(n-1)}
\end{bmatrix} \cdot \begin{bmatrix}
    P(1)\\P(w_n)\\P(w_n^2)\\\vdots\\P(w_n^{n-1})
\end{bmatrix}$$
This can be done in $\Omicron(n\log n)$ times using a similar dived and conquer algorithm.

(a): $p = [p_0]\Leftrightarrow P(x) = p_0, \therefore FFT(p,1)= [1]\cdot[p_0]=p_0$
$\uparrow$ is the base case of FFT algorithm.
(b):
1. $FFT([1,4],2)=\begin{bmatrix}
    P(1)\\P(w_n)
\end{bmatrix} \text{where } P(x) = 1+4x \text{ and } n=2, w_2^2=1 \Rightarrow w_2=-1$
using FFT algorithm: $P(x) = 1+4x \Rightarrow E(x) = 1,O(x) = 4$ and $P(x) =E(x^2)+xO(x^2)$
$\therefore P(1) = E(1)+1\cdot O(1)=5\\ \quad P(-1) = E(1)+(-1)\cdot O(1)= -3$
1. $FFT([3,2],2)\Rightarrow P(x) = 3 + 2x \Rightarrow E(x) = 3, O(x)=2\\ \therefore  P(1) = E(1)+1\cdot O(1)=5\\ \quad P(-1) = E(1)+(-1)\cdot O(1)= 1$

(c): $FFT([1,3,4,2],4) \Rightarrow P(x)=1+3x+4x^2+2x^3\text{ and }w_4=e^{i\frac{\pi}{2}}=i\\ \Rightarrow E(x) =1+4x=P_{FFT([1,4],2)}(x), O(x) = 3+2x = P_{FFT([3,2],2)}(x) \\\therefore P(1) = E(1)+1\cdot O(1)=P_{FFT([1,4],2)}(1)+P_{FFT([3,2],2)}(1)=5+5=10 \\ \quad P(w_4)=E(i^2)+i\cdot O(i^2) = P_{FFT([1,4],2)}(-1)+i\cdot P_{FFT([3,2],2)}(-1) = -3+i\\ \quad P(w_4^2)=E(-1^2)+(-1)\cdot O(-1^2) = 5-5=0\\ \quad P(w_4^3)=E((-i)^2)+(-i)\cdot O((-i)^2) = -3-i\\ \therefore FFT([1,3,4,2],4) = [10,-3+i,0,-3-i]^T$

(d): How to use FFT to multiply two polynomials $p(x),q(x)$ in coefficient form of degree at most d.
$p(x) = a_0+a_1x+ \cdots+a_{d_p}x^{d_p}$, $q(x) = b_0+b_1x+ \cdots+b_{d_q}x^{d_q} $
1. Pike the smallest $2^k \geq d_p + d_q +1$, pad both polynomials $p(x)$ and $q(x)$ with zeros to make their degrees equal to $2^k$. This is done to ensure that the FFT algorithm works correctly and to prevent aliasing.
2. Runing $FFT(p,2^k)$ to get $\begin{bmatrix}
    P(w_{2^k}^0)\\ \vdots \\ P(w_{2^k}^{2^k-1})
\end{bmatrix}$ and runing $FFT(q,2^k)$ to get $\begin{bmatrix}
    Q(w_{2^k}^0)\\ \vdots \\ Q(w_{2^k}^{2^k-1})
\end{bmatrix}$ 
3. Perform element-wise multiplication of the coefficients in $\mathbf{P}$ and $\mathbf{Q}$ to obtain a new vector $\mathbf{PR}$:
   $PR_i = P(w_{2^k}^i) \cdot Q(w_{2^k}^i)$ for $i = 0, 1, \ldots, 2^k-1$. 
   * Hint: Element-wise multiplication in the frequency domain corresponds to convolution in the time domain.
4. Compute the inverse FFT of the result from step 3. This will yield the coefficients of the product polynomial.

```python
import numpy as np

def fft_multiply_polynomials(p, q):
    # Pad both polynomials to the nearest power of 2
    n = len(p) + len(q) - 1
    N = 2**int(np.ceil(np.log2(n)))
    p = np.pad(p, (0, N - len(p)))
    q = np.pad(q, (0, N - len(q)))

    # Compute the FFT of p and q
    P = np.fft.fft(p)
    Q = np.fft.fft(q)

    # Element-wise multiplication
    R = P * Q

    # Inverse FFT to get the product polynomial
    result = np.real(np.fft.ifft(R))

    # Trim any small imaginary parts due to numerical errors
    result = result[:n]
    return result
```
## 3. Modular Fourier Transform
**All calculations should be performed modulo 5**
(a)
 $1^4=1=1\pmod 5,2^4=16=1\pmod5,3^4=81=1 \pmod 5,2^4=256=1\pmod5$
 if $w=2\Rightarrow 1+w+w^2+w^3 =1+2+2^2+2^3=15=0\pmod5$
(b)
$p=[0,3,2,0] \Rightarrow P(x) = (3x+2x^2) \bmod{5}$
This time $w^i = 2^i\bmod{5}  \Rightarrow [1,2,4,3,\cdots]\\\Rightarrow [P(w_0),P(w_1),P(w_2),P(w_3)] = [0,4,4,2]\\\because p_e=[0,2],p_o=[3,0]$
$\therefore FFT([0,3,2,0]) = FFT([0,2])+[w^0,w^1]*FFT([3,0])+FFT([0,2])-[w^0,w^1]*FFT([3,0])$
and $FFT([0,2]) = FFT(0)+w_0*FFT(2)+FFT(0)-w_0*FFT(2)= [2,-2]\\ \quad FFT([3,0]) = FFT(3)+w_0*FFT(0)+FFT(3)-w_0*FFT(0)= [3,3]$
$\therefore FFT([0,3,2,0])=[2,-2]+[1,2]*[3,3]+ [2,-2] - [1,2]*[3,3] = [0,4,4,2]$ which matches the above answer, so $\{1,2,4,3\}$ is the roots of unit.
(c) 
using inverse FFT to compute [0,4,4,2] $\to$ [0,3,2,0]$, iFFT(p,w) = n^{-1}FFT(p,w^{-1})$
$\because 4*4 = 1 \bmod{5} \therefore \text{the inverse of 4 is 4.}$
$\therefore \omega = 2\Rightarrow \omega^-1 = -2\bmod{5} = 3$
$iFFT([0,4,4,2]) = 4* FFT([0,4,1,0]), \omega \text{ is 3} \\ = FFT([0,4,4,2]) = FFT([0,4])+[w^0,w^1]*FFT([4,2])+FFT([0,4])-[w^0,w^1]*FFT([4,2])$
$[w^0,w^1] = [1,3]$, and $FFT([0,4]) = FFT(0)+w_0*FFT(4)+FFT(0)-w_0*FFT(4)= [4,1]\\ \quad FFT([4,2]) = FFT(4)+w_0*FFT(2)+FFT(4)-w_0*FFT(2)= [1,2]$
$\therefore FFT([0,4,4,2])=[4,1]+[1,3]*[1,2]+ [4,1] - [1,3]*[1,2] = [0,2,3,0]$
$\therefore iFFT([0,4,4,2]) = 4* FFT([0,4,1,0])=[0,3,2,0]$
(d)
multiply $3x+2x^2$ and $3-x$
$p_1=[0,3,2,0],p_2=[3,4,0,0]$
$\therefore P_1(x) = FFT(p_1) = [0,4,4,2],P_2(x) = FFT(p_2) = [2,1,4,0]$
$P_1(x)*P_2(x) = [0,4,1,0]$
$iFFT([0,4,1,0]) = 4*FFT([0,4,1,0]) = [0,4,3,3]$

## 2. Cartesian Sum
**Definition:** $A+B=\{a+b \mid a\in A,b\in B \}$, i.e: $\{1,3\} + \{ 2,4\} = \{3,5,7\}$
* Hit: $\{1,3\} + \{ 2,4\} = \{3,5,7\}$ can be treated as $(x^1+x^3)\cdot(x^2+x^4)=x^3+5x^5+x^7$, where powers tells the sum, and the coefficients tells the pairs.

$\therefore$ given $A$ and $B$, $P=\sum_{a\in A}x^a,Q=\sum_{b\in B}x^b$, using $iFFT(FFT(p)*FFT(q))$ can get the answer, which cost $\Omicron(n\log n)$

## 4. Patten Matching
**Input:**
* A string $g$ og length $n$ made of $0s$ and $1s$. Call $g$ the "pattern".
* A string $s$ og length $m$ made of $0s$ and $1s$. Call $g$ the "sequence".
* Integer $k$.

**Goal:** Find the (staring) locations of all length n-substrings of $s$ which match $g$ in at least $n-k$ positions. 
**Example:** Using 0-indexing, $g=0111,s=01010110111$, and $k=1$, the output is $0,2,4,7$
(a): Find an $\Omicron(nm) $ algorithm:

matching g from the start of s, and move step by step, check the match number weather $\leq n-k$.

(b): $\Omicron(m\log m)$ algorithm:

$g=0111,s=01010110111, \text{ change all }0 \to -1, \text{and reverse the }g$
$\therefore g'=[1,1,1,-1], s'=[-1,1,-1,1,-1,1,1,-1,1,1,1]$
When check g in s's position 0: 
the 3rd degree's coefficient's of $g'\cdot s'$ is the sum of match_number $-$ un_match_number. Check if it is  $\geq n-2k$.
and position 1 is 4rd degree...
$\therefore \text{the total cost runtime is } \Omicron(m\log m)+\Omicron(m)=\Omicron(m\log m)$

## 5. Graph Traversal
(a) Running DFS and count the pre and post number.

$A[1,6],B[2,3],E[4,5],C[7,20],J[8,19],F[9,18],D[10,11],H[12,17],I[13,16],G[14,15]$

(b) Finding the SCCs(strong connected component) of the graph.
* 1. **reverse** the graph.
* 2. running DFS with counting pre and post numbers.
* 3. sort all edges by posting orders form high to low.
* 4. run DFS form the highest post_number vertex in **origin** graph, each time done one DFS, change the group number and do DFS for the left highest vertex until all vertex is visited.

SCCs: $\{E\},\{B\},\{A\},\{G,H,I\},\{J,F,D,C\}$

(c)
Ignore the edges within each SCCs, and draw a new graph only using the edges connecting each SCCs, this new graph will have no cycles, which will be helpful for many problems.
