from copy import deepcopy

class GraphAdjacencyMap(object):
    """ Representation of a simple graph using an adjacency map. """

    def __init__(self, directed=False):
        """ Create an empty graph (undirected, by defalt).
        Graph is directed if optional param is set to True
        """

        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Return True if is a directe graph. False if undirected.
        Property is based on the original declaration of the graph, not its contents
        """
        return self._incoming is not self._outgoing     # directed if maps are distinct

    def vertex_count(self):
        """ Return the num of vertices in the graph. """
        return len(self._outgoing)

    def vertices(self):
        """ Return an iteration of all vertices of the graph. """
        return self._outgoing.keys()

    def edge_count(self):
        """ Return the num of edges in the graph. """
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        """ Return a set of all edges of the graph. """
        result = set()          # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())       # add edges to resulting set
        return result

    def get_edge(self, u, v):
        """ Return the edge from u to v, or None if not adjacent. """
        return self._outgoing[u].get(v)                 # returns None if v not adjacent

    def degree(self, v, outgoing=True):
        """ Return number of (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to count incoming edges. """

        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """ Return all (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to request incoming edges
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """ Insert and return a new Vertex with element x. """
        v = self.Vertex(x)
        self._outgoing[v] = { }
        if self.is_directed():
            self._incoming[v] = { }         # need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, x=None):
        """ Insert and return a new Edge from u to v with auxiliary element x."""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

def DFS(g, u, discovered):
    """ Peform Depth-First-Search of the undiscovered portion of Graph g starting at Vertex u.

    discovered is a dictionary mapping each vertex to the edge that was used to discover it during the
    DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in g.incident_edges(u):               # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:                 # v is an unvisited vertex
            discovered[v] = e                   # e is the tree edge that discovered v
            DFS(g, v, discovered)               # recursively explore from v


def DFS_complete(g):
    """ Perform DFS for entire graph and return forest as a dictionary.

    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest = { }
    for u in g.vertices():
        if u not in forest:
            forest[u] = None                    # u will be the root of the tree
            DFS(g, u, forest)
    return forest

def BFS(g, s, discovered):
    """ Perform BFS of the undiscovered portion of Graph g starting at Vertex s.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s]                                 # first level includes only s
    while len(level) > 0:
        next_level = []                         # prepare to gather newly found vertices
        for u in level:
            for e in g.incident_edges(u):       # for every outgoing edge from u
                v = e.opposite(u)
                if v not in discovered:         # v is an unvisited vertex
                    discovered[v] = e           # e is the tree edge that discovered v
                    next_level.append(v)        # v will be further considered in next pass
        level = next_level                      # relabel 'next' level to become current


def floyd_warshall(g):
    """ Return a new graph that is the transitive closure of g. """
    closure = deepcopy(g)                       # imported from copy module
    verts = list(closure.vertices())            # make indexable list
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # verify that edge (i,k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # verify that edge (k,j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k],verts[j]) is not None:
                        # if (i,j) not yet included, add it to the closure
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure

def topological_sort(g):
    """ Returns a list of vertices of directed acyclic graph g in topological order.

    If graph g has a cycle, the result will be incomplete.
    """
    topo = []                                   # a list of vertices placed in topological order
    ready = []                                  # list of vertices that have no remaining constraints
    incount = { }                               # keep track of in-degree for each vertex
    for u in g.vertices():
        incount[u] = g.degree(u, False)         # parameter requests incoming degree
        if incount[u] == 0:                     # if u has no incoming edges,
            ready.append(u)                     # it is free of constraints
    while len(ready) > 0:
        u = ready.pop()                         # u is free of constraints
        topo.append(u)                          # add u to the topological order
        for e in g.incident_edges(u):           # consider all outgoing neighbors of u
            v = e.opposite(u)
            incount[v] -= 1                     # v has one less constraint without u
            if incount[v] == 0:
                ready.append(v)
    return topo

def shortest_path_lengths(g, src):
    """ Dijkstra's algorithm for computing the shortest-path distances from a single source

    compute shortest-path distances from src to reachable vertices of g
    Graph g can be undirected or directed, but must be weighted such that e.element() returns a numeric weight for each
    edge e.

    Return dictionary mapping each reachable vertex to its distance from src
    """
    d = { }                                     # d[v] is upper bound from s to v
    cloud = { }                                 # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()           # vertex v will have key d[v]
    pqlocator = {}                              # map from vertex to its pq locator

    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')                 # syntax for positive infinity
        pqlocator[v] = pq.add(d[v], v)          # save locator for future updates

        while not pq.is_empty():
            key, u = pq.remove_min()
            cloud[u] = key                      # its correct d[u] value
            del pqlocator[u]                    # u is no longer in pq
            for e in g.incident_edges(u):       # outgoing edges (u,v)
                v = e.opposite(u)
                if v not in cloud:
                    # perform relaxation step on edge (u,v)
                    wgt = e.element
                    if d[u] + wgt < d[v]:       # better path to v?
                        d[v] = d[u] + wgt       # update the distance
                        pq.update(pqlocator[v], d[v], v)

        return cloud


class AdaptableHeapPriorityQueue(object):
    def __init__(self):
        raise NotImplementedError('need to implement')


def MST_PrimJarnik(g):
    """ Compute a minimum spanning tree of weighted graph g.

    Return a list of edges that comprise the MST (in arbitrary order). """

def MST_Kruskal(g):
    """ Compute a minimum spanning tree of a graph using Kruskal's algorithm.

    Return a list of edges that comprise the MST.
    The elements of the graph's edges are assumed to be weights."""