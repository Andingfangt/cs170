def max_independent_set(adjacency_list, weights):
    """
    Return a list containing the vertices in the maximum weighted independent set.

    args:
        adjacency_list:ListList[[int]] = the adjacency list of the tree. 
        weights:List[int] = a list of vertex weights. weights[i] is the weight of vertex i.

    return:
        List[int] Containing the labels of the vertices in the maximum weighted independent set.
    """
    n = len(weights)
    mem_weight = [[-1,-1] for _ in range(n)]
    mem_set = [[[],[]] for _ in range(n)]
    
    
    def f(v, p, parent):
        '''
        return the maximum weight and maximum independent set list with v is the root now 
        and p==1 means v can be use, and v can't travel to all vertex in visited_list
        '''
        if mem_weight[v][p] != -1:
            return (mem_weight[v][p], mem_set[v][p])
        
        
        # base case
        if adjacency_list[v] == [parent]:
            if p == 1:
                mem_weight[v][1] = weights[v]
                mem_set[v][1].append(v)
            else:
                mem_weight[v][0] = 0
            
            return (mem_weight[v][p], mem_set[v][p])
        
        sum_child_weight_0, sum_child_weight_1, sum_child_set_0, sum_child_set_1= 0,0,[],[]
        for child in adjacency_list[v]:
            if child == parent:
                continue
            max_weight_0, max_set_0 = f(child,0,v)
            max_weight_1, max_set_1 = f(child,1,v)
            if max_weight_0 > 0:
                sum_child_weight_0 += max_weight_0
                sum_child_set_0 += max_set_0
            if max_weight_1 > 0:
                sum_child_weight_1 += max_weight_1
                sum_child_set_1 += max_set_1

        if p == 1:
            if weights[v] + sum_child_weight_0 > f(v,0,parent)[0]:
                mem_weight[v][p] = weights[v] + sum_child_weight_0
                mem_set[v][p] = [v] + sum_child_set_0
            else:
                mem_weight[v][p] = f(v,0,parent)[0]
                mem_set[v][p] = f(v,0,parent)[1]
        
        else:
            mem_weight[v][p] = sum_child_weight_1
            mem_set[v][p] = sum_child_set_1

        return (mem_weight[v][p], mem_set[v][p])
    
    (max_weight, max_set) = f(0,1,-1)        
    
    return max_set


def main():
    T = [[1, 2, 3, 4], [0], [0, 5], [0], [0], [2]]
    W = [-8, 6, 8, -6, -4, 7]
    print(max_independent_set(T,W))
    
if __name__ == '__main__':
    main()