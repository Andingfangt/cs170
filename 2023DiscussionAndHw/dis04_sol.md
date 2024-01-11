## 1. Graph Short Answer

(a): true
(b): false, $\because (u,v)$ may not be an edge.
(c): false
(d): true
The way we find SCC algorithm is:

1. Reverse the original graph $G\to G^R$
2. Run DFS in $G^R$ with pre and post time.
3. Sort all edges by posting order form high to low.
4. Run DFS form the highest post_number vertex in **original** graph $G$, each time done one DFS, change the group number and do DFS for the left highest vertex until all vertex is visited.

## 2. Some DFS

1. Edges in DFS: Tree edge, Back edge, Cross edge, Forward edge.
2. Runtime: $\Omicron(|V|+|E|)$

(a) critical vertex: remove will cause other vertex disconnected(increase the number of SCC).

* The idea is to use DFS (Depth First Search). In DFS, follow vertices in a tree form called the DFS tree. In the DFS tree, a vertex $u$ is the parent of another vertex $v$, if $v$ is discovered by $u$.

In DFS tree, a vertex u is an articulation point if one of the following two conditions is true:

1. $u$ is the root of the DFS tree and it has at least two children.
2. $u$ is not the root of the DFS tree and it has a child $v$ such that no vertex in the subtree rooted with $v$ has a back edge to one of the ancestors in DFS tree of $u$.

(b) critical edges: aside from $(u,v)$, no other path for $u$ to $v$

* The idea is to use DFS algorithm to decide whether an edge is in a cycle or not.

1. Assign a rank(pre-order) to each node while traversing using the dfs.
2. dfs function returns the minimum rank it finds. **During** a step of search from node u to its neighbor v, if dfs(v){This should avoid straight back to its parent u.} returns something smaller than or equal to rank(u), then u knows its neighbor v helped it to find a cycle back to u or u‘s ancestor. So u knows it should discard the edge (u, v) which is in a cycle.
3. Discard all edges in the cycles, then the remaining connections are a complete collection of critical connections.

## 4. Waypoint

Question: given a strong directed graph $G=(E,V)$ with positive weights, and a specific node $v_0\in V$, find a $\Omicron(|V|^2+|E|\log |V|)$ algorithm to compute for all pairs $s,t$, their shortest path from $s$ to $t$ passes through $v_0$.

Hint:

* cause it is positive weights, so we can use Dijkstra algorithm.
* there are two parts: shortest path from $s\to v_0$ and shortest path from $v_0\to t$

1. Using Dijkstra to find all shortest path from $v_0$ to all other nodes(which is the universal set of $t$).
   $\to \Omicron((|V|+|E|)\log|V|)$
2. For shortest path for all $s$ to $v_o$, we can't use $|V|$ time Dijkstra. Instead:
   * 1. Reverse the graph. $\to \Omicron(|E|)$
   * 2. Find shortest path from $|v_0| \to s$ in $G^R$,  $\to \Omicron((|V|+|E|)\log|V|)$
   * 3. Reverse all the result. $\Omicron(V)$

$\therefore $ step1 and step2 all give $|V|$ path, to combine them together cause $\Omicron(|V|^2)$

$\Rightarrow$The total runtime is $\Omicron(|V|^2+|E|\log |V|)$

## 4. Running Errands

In Directed positive weight graph, have home vertex $h$, the errands $(S_i), {i=1\to k}$ must be completed in order, and every errand is a set of vertexes like $S_1 = \{A,B \}$, visit any of them will complete the errands.

Find a efficient algorithm to start from $h$ and complete all the errands:

* Idea: make $K+1$ copy of original graph $G$, and connect the $S_i$ by order like $(S_1)\in G_1 \to (S_1)\in G_2, (S_2)\in G_3 \to (S_2)\in G_4\cdots$, this ensure the order of complying errands. And than we can run dijkastra only once.
* The runtime is $\Omicron(k(|V|+|E|)\log(k|V|))$

## 3. Dijkstra's Algorithm Fails on Negative Edges

Sudo code for Dijkstra:

```python
def dijkstra(s,G):
    '''
    s is the start point in graph G
    '''
    for u in G.V:
        u.dist = float('inf') # initialize all vertex's distance to ∞;
        u.prev = Null
    s.dist = 0 # the distance of start vertex is 0;
    H = help_make_PQ(V) # initialize a priority queue with all the vertex.
    while !H.empty(): # do the loop util H is empty.
        u = H.popMin() # use the smallest distance vertex, and remove it from the priority queue.
        for v in u.neighbors:
            if v in H: # v should not be visited
                if u.dist + l(u,v) < v.dist: # if find a smaller distance, update it. 
                    v.prev = u
                    v.dist = u.dist + l(u,v)
                    H.updateKey(v)
```

If graph have negative weights, sometimes dijkstra will fail, cause we can only visited a vertex once.


## 2. BFS Intro

Runtime: $\Omicron(|V|+|E|)$

* If in graph all weights are equal, BFS can be used to find the shortest path.
* If weights are not equal, we can replace all edges to 1 and add $w_e$ vertex inside. Runtime is $\Omicron(|E|'+|V|')$, if we represent $w_e$ with bits $2^a$, now the input size of graph is a, but $|V| = |E|= 2^a$,
* Or use dijkstra.