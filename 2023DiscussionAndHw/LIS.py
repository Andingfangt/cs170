def longest_increasing_subsequences(A):
    '''
    return the the increasing subsequence of greatest length.
    >>> longest_increasing_subsequences([5,2,8,6,3,6,9,7])
    (4, [2,3,6,9])
    '''
    n = len(A)
    max_length = [1] * n # initialize all elements has its own.
    path = [[i] for i in range(n)] # initialize all path with its own
    G_R= reverse_graph(make_DAG(A))
    # form bottom up
    for i in range(n):
        # max increasing subs for element i is those elements that point to i 's max + 1.
        nodes_point_to_i = G_R[i]
        for j in nodes_point_to_i:
            if max_length[j] + 1 > max_length[i]:
                max_length[i] = max_length[j] + 1
                path[i] = path[j] + [i]
        
    length = max(max_length)
    longest_node_end_index = max_length.index(length)
    longest_node_path = path[longest_node_end_index]
    subsequences = [A[v] for v in longest_node_path]
    
    return (length, subsequences)
        
def make_DAG(A):
    '''
    create a graph of all permissible transitions: establish a node i for each element ai, 
    and add directed edges (i, j) whenever it is possible for ai and aj to be consecutive elements in an increasing subsequence,
    that is, whenever i < j and ai < aj.
    '''
    n = len(A)
    G = [[] for _ in range(n)]
    for i in range(n):
        current_number = A[i]
        for j in range(i+1,n):
            compare_number = A[j]
            if compare_number > current_number: # only connect when numbers after are greater than current number.
                G[i].append(j)
    return G

def reverse_graph(G):
    '''return G^R.'''
    n = len(G)
    G_R = [[] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            G_R[j].append(i)
    return G_R
    

def main():
    A = [5,2,8,6,3,6,9,7]
    print(longest_increasing_subsequences(A))
    
if __name__ == '__main__':
    main()
