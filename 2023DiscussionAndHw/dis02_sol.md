## 1. Counting inversions

**Algorithm:**

```python
def countInversion(A):
    """
    given an unsorted array A, 
    return a sorted A and the number of inversions.
    >>> countInversion([4, 1, 3, 2])
    [1, 2, 3, 4], 4
    """
    n = len(A)
    if n <= 1:
        return A, 0

    L, R = A[:n//2], A[n//2:]
    sorted_L, countL = countInversion(L)
    sorted_R, countR = countInversion(R)
    sorted_A, countM = merge(sorted_L, sorted_R)
    
    return sorted_A, countL + countR + countM

def merge(L, R):
    '''
    Modify from merge sort, given tow sorted array L and R,
    return merge sorted array L + R, and the number of inversions between them.
    >>> merge([1, 3, 5, 7], [2, 4, 6, 8])
    [1, 2, 3, 4, 5, 6, 7, 8], 6
    '''
    sorted_A = []
    countM = 0
    while len(L) != 0 and len(R) != 0:
        if L[0] <= R[0]:
            sorted_A.append(L.pop(0)) 
        else:
            sorted_A.append(R.pop(0))
            countM += len(L) # this means all the number in L now is inversions

    sorted_A = sorted_A + L + R #once one array is empty, add all the left into sorted_A.

    return sorted_A, countM
    
```

**Runtime:**

in this algorithm: merge(L, R) = $\Omicron(n)$
$\therefore$ countInversion(A) has $T(n) = 2T(\frac{n}{2}) + \Omicron(n) \Rightarrow T(n) = \Omicron(n\log n)$


## 2. Maximum Subarray Sum

```python
def mss(A):
    '''
    given an array A, find the maximum subarray sum 
    which means find the max(sum(A[i:j+1]))
    >>> mss([-2,1,-3,4,-1,2,1,-5,4])
    6 
    which is the sum of [4,-1,2,1]
    '''
    n = len(A)
    # base case
    if n == 1:
        return A[0]

    # divide into 2 pieces.
    L, R = A[:n//2], A[n//2:] 
    # has 3-parts
    max_sum_left = mss(L) # i,j all in left side.
    max_sum_right = mss(R) # i,j all in right side.
    max_sum_middle = middle_help(L, R) # i in left, j in right.

    return max(max_sum_left, max_sum_right, max_sum_middle)

def middle_help(L, R):
    '''
    simply loop i from L[-1] to L[0], find the max sum of L;
    loop j form R[0] to R[-1], find the max sum of R;
    return the sum of those two
    >>> middle([-2,1,-3,4], [-1,2,1,-5,4])
    6 
    which is 4 + 2
    '''
    sum_L, max_L = 0, float('-inf')
    sum_R, max_R = 0, float('-inf') 

    # find the max sum of left side.
    for i in range(-1,-(len(L) + 1),-1):
        sum_L += L[i]
        max_L = max(max_L, sum_L)
    # find the max sum of right side.
    for i in range(-1,-(len(R) + 1),-1):
        sum_R += R[i]
        max_R = max(max_R, sum_R)

    return max_L + max_R
```

**Runtime:**
in this algorithm, middle_help = $\Omicron(n)$
$\therefore T(n) = 2T(\frac{n}{2}) + \Omicron(n) \Rightarrow T(n) = \Omicron(n\log n)$

## 5. Pareto-optimal points

1. divide all the points $(x_i,y_j)$ into two parts according to x;
2. now we have L and R,
   find  the Pareto-optimal points in L, which is $f(L)$,
   the same is $f(R)$.
3. all the points in $f(R)$ is the answer cause points in $f(L)$ won't affect them, so only need to consider points in $f(L)$.
4. for p in $f(L)$, cause it will always have point in its right(because R is on it's right), so need to check if its $y_j > max(x_i, \text{ for } x_i \text{ in } f(R))$.
   Find the $max(x_i)$ cast $\Omicron(n)$.
   Check all points in $f(L)$ also cast $\Omicron(n)$.
   So the total cast time is still $\Omicron(n)$
5. $\therefore T(n) = 2T(\frac{n}{2}) + \Omicron(n) \Rightarrow T(n) = \Omicron(n\log n)$

## Complex Numbers

**some highlights:**
$a+ ib = re^{i\theta}$ two ways to implement complex number.
$re^{\theta+2k\pi}$ = $re^{i\theta}$
$Ae^{i\theta}\cdot Be^{i\phi} = ABe^{i(\theta + \phi)},\quad 1 = e^{i2k\pi}, \quad ...$
$z = e^{i\theta}, z^2 = e^{i2\theta}, z^3 = e^{ie\theta}$

**roots of unity:**
$\omega ^6 =1 \Rightarrow \omega^6 = e^{i2k\pi} \Rightarrow \omega = e^{i\frac{2k\pi}{6}}, \quad k = 1,2,3,4,5,6, \quad \text{means } \omega^6 - 1 =0 \text{ has 6 roots of unity}$

**some excise:**

(a) $e^{i\frac{3}{10}2\pi}\cdot e^{i2\pi\frac{5}{10}} = e^{i\frac{4}{5}2\pi}$
(b) $$\sum_{k=0}^{n-1}\omega^k =\omega^0 +\omega^1 +\omega^2 ... +\omega^{n-1} = \frac{\omega^{n}-1}{\omega-1} \\ \because w = e^{i\frac{2k\pi}{n}},\quad \omega^n = 1 \\ \therefore \sum_{k=0}^{n-1}\omega^k = 0$$
(c)
 $\omega^2 =-1 \Rightarrow \omega^2 =e^{i(\pi+2k\pi)} \therefore \omega = e^{i(\frac{\pi}{2}+k\pi)},\text{ has 2 answers}$

 $\omega^4 =-1 \Rightarrow \omega^4 =e^{i(\pi+2k\pi)} \therefore \omega = e^{i(\frac{\pi}{4}+\frac{k\pi}{2})},\text{ has 4 answers}$

## (OPTINAL) Monotone matrices
matrix A is monotone if each row's minimus number Sorting from left to right.

**Algorithm to find the minimum in each row of an m-by-n monotone matrix A:**

1. find the middle row(m//2) in given monotone matrix(nxm).
2. in this middle row, liner scan and find the minimus and its index **J**, which cost $\Omicron(n)$
3. according to this middle row, it divide the matrix into 2 parts top_M and blow_M.
4. because it is monotone matrix, so we only need to check first J elements in top_M, and last n-J elements in blow_M.
5. so $top_M = A[:m//2][:J], blow_M = A[(m//2 +1):][(J+1):]$
6. $\therefore T(mn) = T(\frac{m}{2}j) + T(\frac{m}{2}(n-j)) + \Omicron(n) \Rightarrow T(n) =\Omicron(n\log m)$ (draw recursion trees)
