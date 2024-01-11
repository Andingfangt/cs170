import doctest # in order to test >>>.


def count_number(A):
    """
    Giving an array A of n distinct non-negative integers, 
    count the number odd-sized subsets of A 
    whose elements add up to a multiple of 3.
    >>> count_number([1])
    0
    >>> count_number([3,2,1])
    2
    """
    odd, even = count_number_help(A)
    return odd[0]

def count_number_help(A):
    
    odd = [0, 0, 0]
    even = [0, 0, 0]
    n = len(A)
    
    # base case
    if n == 1:
        odd[A[0] % 3] += 1 # A itself.
        even[0] = 1 # A has a subset [].
        return odd, even
    
    # split into left and right part.
    odd_l, even_l = count_number_help(A[:n//2])
    odd_r, even_r = count_number_help(A[n//2:])
    
    # merge those table, whose runtime is 36*O(nlogn): 
    # ∵ If a set has n elements, then the number of subset is 2^n, 
    # ∴ the number is both table will no more than 2^n => n bits in binary
    # ∴ multiple two n bits number will cost O(nlogn)
    for i in range(3):
        for j in range(3):
            # odd = odd + even; even = even + even or odd + odd; 
            # and their mod 3 value add mod 3 = 0.
            odd[i] += odd_l[j] * even_r[(i - j) % 3]
            odd[i] += even_l[j] * odd_r[(i - j) % 3]
            even[i] += even_l[j] * even_r[(i - j) % 3]
            even[i] += odd_l[j] * odd_r[(i - j) % 3]

    return odd, even

def main():
    # test
    print(count_number([1]))
    print(count_number([3,1]))
    print(count_number([3,2,1]))
    print(count_number([2,1,3,4,5]))
    
if __name__ == "__main__":
    doctest.testmod()
    main()