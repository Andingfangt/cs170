## 1.Asymptotics and Limits
(a) $\lim_{n\to\infty} \frac{n^3}{n^4} = 0$
    => $n^3 = O(n^4)$

(b) make $f(n) =\theta(g(n))$ will do it.
for example $f(n) = 3n, g(n) = 5n$

(c) L'Hopotal's Rule: if $$\lim_{n\to\infty}f(n) = \lim_{n\to\infty}g(n) = \infty$$ then $$\lim_{n\to\infty}\frac{f(n)}{g(n)} = \lim_{n\to\infty}\frac{f'(n)}{g'(n)}$$if the RHS exists.
$$∵ \lim_{n\to\infty}log(n) = \lim_{n\to\infty}n^c = \infty$$
$$∴ \lim_{n\to\infty}\frac{log(n)}{n^c} = \lim_{n\to\infty}\frac{\frac{1}{n}}{cn^{c-1}} = \lim_{n\to\infty}\frac{1}{cn^{c}} = 0 (c >0)$$
∴ $log(n) = O(n^c)$

(d)  let $f(n) = (\sin n + 1) n,\ g(n) = n$
$$∴\lim_{n\to\infty}\frac{(\sin n + 1 )n}{n} = \lim_{n\to\infty}\sin n + 1 (do\ not\ exist)$$
because $f(n) = O(g(n)) $ if there exists a c > 0 where after large enough n, $f(n) ≤ c · g(n)$.(Asymptotically, f grows at most as much as g)
so apply c = 2, it fits cause $(\sin n + 1) \leq 2$
∴ $f(n) = O(g(n)) $


## Asymptotic Complexity Comparisons
(a) $f_3 < f_7< f_2 < f_5 < f_4 < f_9  < f_8 < f_6 < f_1$ 
$constant < log < poly < exp$

(b) 
(i) $f(n) = \Theta(g(n))$
(ii) $f(n) = \Omicron(g(n))$
(iii) $f(n) = \Omega(g(n))$
(iv) $f(n) = \Theta(g(n))$

## Hadamard matrices
$H_0 = \begin{bmatrix}
    1 
 \end{bmatrix}$

$H_k = \begin{bmatrix}
    H_{k-1} & H_{k-1} \\ H_{k-1} & -H_{k-1} 
 \end{bmatrix}$
 (a)
 $$∴ H_0 = \begin{bmatrix}
    1 
 \end{bmatrix}, H_1 = \begin{bmatrix}
    1 & 1 \\ 1 & -1
 \end{bmatrix}, H_2 = \begin{bmatrix}
    1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1
 \end{bmatrix}$$
 
 (b) $$v = \begin{bmatrix}
    1\\-1\\-1\\1
 \end{bmatrix} \therefore H_2 \cdot v = \begin{bmatrix}
    0\\0\\0\\4
 \end{bmatrix} = u$$

 (c) 
$$v = \begin{bmatrix}
    v_1\\v_2
\end{bmatrix}, v_1 = \begin{bmatrix}
    1\\-1
\end{bmatrix}, v_2 = \begin{bmatrix}
    -1\\1
\end{bmatrix}$$
$$\therefore u_1 = H_1\cdot(v_1+v_2) = \begin{bmatrix}
    0\\0
\end{bmatrix},u_2 = H_1\cdot(v_1-v_2) = \begin{bmatrix}
    0\\4
\end{bmatrix} $$
notice that $u = \begin{bmatrix}
    u_1\\u_2
\end{bmatrix}$

(d) 
$$H_k \cdot v = \begin{bmatrix}
    H_{k-1} & H_{k-1} \\ H_{k-1} & -H_{k-1} 
 \end{bmatrix} \cdot \begin{bmatrix}
    v_1\\v_2
\end{bmatrix} = \begin{bmatrix}
    H_{k-1}(v_1+v_2)\\ H_{k-1}(v_1-v_2)
\end{bmatrix}$$

(e) 
$$H_k'\ length = 2^k \cdot 2^k$$

$$v's\ length = 2^k = n$$

$$\therefore H_k \cdot v = \begin{bmatrix}
    H_{k-1}(v_1+v_2)\\ H_{k-1}(v_1-v_2)
\end{bmatrix} = \begin{bmatrix}
    H_{k-1}(v_a)\\ H_{k-1}(v_b)
\end{bmatrix} = \begin{bmatrix}
    H_{k-2}(v_{a1}+v_{a2})\\ H_{k-2}(v_{a1}-v_{a2})\\H_{k-2}(v_{b1}+v_{b2})\\H_{k-2}(v_{b1}-v_{b2})
\end{bmatrix}$$ $$ = ... until\ H_0$$
$$\therefore T(n) = 2T(n/2) + Cn \Rightarrow \Theta(nlog(n))$$
