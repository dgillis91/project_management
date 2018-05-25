from collections import defaultdict

class Graph(object):
    def __init__(self, vertices=[], edges=None, directed=False):
        '''
        @Description:   Initialize a graph object. The graph can theoretically contain any arbitrary object. It is important that
                        the vertices be hashable. In addition, you want to ensure that your hash doesn't change for mutable objects.
                        This method is setup in a type safe manner. That is, it will not allow you to pass a parameter of incorrect type.
        @Params:        * vertices - A list of vertices.
                        * edges - A list of 'relationships' between vertices.
                        * directed - Whether or not the graph is directed. This CANNOT be changed after instantiation.
        @Created:       05.20.2018
        @Throws:        TypeError - If you don't pass in the appropriate types for the parameters.
        @UsageExamples:
            >>> g = Graph(vertices=[1, 2, 3], edges={1 : [2, 3]}
            >>> # We've created a graph with 1->2, 1->3.
        '''
        # We need to ensure that the right types were passed in. Now, for the edges, we want to check if it's None before 
        # performing type checking.
        if edges != None and not isinstance(edges, list):
            raise TypeError
        # Next, check the type of the vertices and directed
        if not isinstance(vertices, list) or not isinstance(directed, bool):
            raise TypeError
        # A list of vertices
        self._vertices = vertices
        # The adjacency list
        self._adj_list = defaultdict(set)
        # Boolean value identifying whether the graph is directed
        self._directed = directed
        # Iterate over the list of edges and add them
        if edges != None:
            self.add_edges(edges)

    ''' --- Properties --- '''
    @property
    def vertices(self):
        return self._vertices

    @property
    def adjacency_matrix(self):
        pass

    @property
    def adjacency_list(self):
        return self._adj_list

    @property
    def directed(self):
        return self._directed
    
    ''' --- Magic Methods --- '''
    def __len__(self):
        '''
        @Description:   Return the number of vertices in the graph.
        @Params:        None
        @Created:       05.19.2018
        @Throws:        None
        @UsageExamples:
            >>> g = Graph(vertices=[1, 2, 3], edges={1 : 2, 2 : 3}, directed=True)
            >>> print(len(g))
            3
        '''
        return len(self._vertices)
    
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._adj_list))
    
    ''' --- Primary Methods --- '''
    def add_vertex(self, vertex):
        '''
        @Description:       Add a vertex, if it is not already in the list of vertices. 
        @Params:            vertex - element to add to the graph.
        @Created:           05.20.2018
        @Throws:            None
        @UsageExamples: 
            >>> g = Graph()
            >>> g.add_vertex(1)
            >>> g.add_vertex(2)
            >>> g.add_vertex(2) # Does nothing
            >>> print(g.vertices)
            [1, 2]
        '''
        # I don't want to throw an error for trying to duplicate an entry. Instead, I'll just return.
        if vertex in self.vertices:
            return None 
        self._vertices.append(vertex)
        
    def add_vertices(self, vertices):
        '''
        @Description:   Add any number of vertices. User must pass in a list.
        @Params:        vertices - a list of vertices
        @Created:       05.19.2018
        @Throws:        * Errors handled within the method this method delegates to, add_vertex. See documentation for add_vertex.
                        * TypeError - If vertices is not a list
        @UsageExamples:
        '''
        # If the list of vertices is not of type list, throw an error.
        if not isinstance(vertices, list):
            raise TypeError
        # Iterate over the list of vertices, and delegate to the add_vertex method.
        for vertex in vertices:
            self.add_vertex(vertex)

    def add_edge(self, edge):
        '''
        @Description:   Add an edge between two vertices. If the graph is directed, the edge will only be added from the
                        left entry of the 'edge' tuple to the right entry. If the graph is not directed, however, the order
                        is irrelevant. There is no need to worry about duplicating edges, it isn't possible. The structure 
                        within the dict is a set.
        @Params:        edge - a 2-tuple describing which vertices an edge should exist between. 
        @Created:       05.20.2018
        @Throws:        IndexError - if the len(edge) != 2
                        TypeError - if edge is not of type tuple
                        KeyError - If the vertices in edge do not already exist in the graph
        @UsageExamples:
            >>> # Create a graph and add an edge between two nodes
            >>> # The graph in this example only contains three nodes, and is directional
            >>> dg = Graph(vertices=[1, 2, 3], directed=True)
            >>> dg.add_edge((1, 2))
            >>> dg.add_edge((2, 3))
            >>> dg.add_edge((3, 1))
            >>> # Note that this has created a circuit with 1->2, 2->3, and 3->1
            >>> # Now let's do the same with a graph that is not directed
            >>> g = Graph(vertices=[1, 2, 3], directed=True)
            >>> g.add_edge((1, 2))
            >>> g.add_edge((2, 3))
            >>> g.add_edge((3, 1))
            >>> # Now we have 1<->2, 2<->3, and 3<->1
        '''
        # Ensure the user is trying to add an edge between two vertices.
        if len(edge) != 2:
            raise IndexError
        # Verify that edge is a tuple.
        if not isinstance(edge, tuple):
            raise TypeError
        # Get the vertices from the edge tuple.
        vertex_one, vertex_two = edge
        # To add an edge between two vertices, both vertices must already be in the vertex list.
        if vertex_one not in self.vertices or vertex_two not in self.vertices:
            raise KeyError

        # Add the edge from the left vertex, to the right vertex.
        self._adj_list[vertex_one].add(vertex_two)
        # If the graph is not directed, add the edge from the right vertex to the left.
        if not self.directed:
            self._adj_list[vertex_two].add(vertex_one)

    def add_edges(self, edges):
        '''
        @Description:   Add a list of edges. Like with Graph.add_edge(...), the behavior is dependant on whether the graph is directed. If it is,
                        an edge is added from the left hand vertex in each two-tuple, to the right.
        @Params:        * edges - a list of two-tuples of nodes representing an edge between the two.
        @Created:       05.21.2018
        @Throws:        * TypeError - if edges is not of type list.
                        * Review documentation for Graph.add_edge(...) for a list of additional errors.
        @UsageExamples:
            >>> g = Graph(vertices=[1, 2, 3, 4], directed=False)
            >>> g.add_edges([(1, 2), (2, 3), (2, 4), (3, 4), (4, 1)])
            >>> # The code above has created a graph with 1<->2, 2<->3, 2<->4, 3<->4, 4<->1
            >>> dg = Graph(vertices=[1, 2, 3, 4], directed=True)
            >>> dg.add_edges([(1, 2), (2, 3), (2, 4), (3, 4), (4, 1)])
            >>> # The code above has created a graph with 1->2, 2->3, 2->4, 3->4, 4->1
        '''
        # Verify that the caller has passed in a list, then iterate over that list, and begin adding entries
        if not isinstance(edges, list):
            raise TypeError
        for edge in edges:
            self.add_edge(edge)

    def remove_vertex(self, vertex):
        '''
        @Description:   Remove a vertex from a graph.
        @Author:        David Gillis
        @Params:        vertex - the vertex to remove, must already be in the graph
        @Created:       05.21.2018
        @Throws:        * IndexError - If the vertex is not in the graph 
        @UsageExamples: 
            >>>
        '''
        # Throw an error if the vertex isn't in the list of vertices.
        if vertex not in self.vertices:
            raise KeyError
        # To remove the vertex, we have to move all of the edges, as well. It's important to note, however, that we don't know what vertices have edges to
        # and from the vertex we want to remove. Therefore, we must iterate over all off them.
        for vert, edges in self._adj_list.items():
            if vertex in edges:
                edges.remove(vertex)
        # Now we need to remove the entry from the adjacency list, itself.
        if vertex in self._adj_list.keys():
            del self._adj_list[vertex]
        # Last, we remove the vertex from the list of vertices
        self._vertices.remove(vertex)

    def remove_edge(self, edge):
        '''
        @Description:   Remove the connection between two nodes. Throws an error if the connection doesn't exist. The behavior will vary based on
                        whether the graph is directed. If the graph is directed, we only attempt to move the edge between the left vertex, and the right.
                        If it is not directed, we try to remove both. This method has no error handling built into it. If you try to access edges or vertices
                        which don't exist, errors will be thrown.
        @Author:        David Gillis
        @Params:        edge - a tuple representing the connection between two nodes
        @Created:       05.21.2018
        @Throws:        * TypeError - if edge is not of type tuple
                        * KeyError - If the vertex passed in doesn't exist
                        * IndexError - If the edge doesn't exist
        @UsageExamples:
            >>> g = Graph(vertices=[1, 2, 3], edges={1 : [2, 3]}
        '''
        if not isinstance(edge, tuple):
            raise TypeError
        # Remove the edge in the adjacency list, from the left hand vertex, to the right. If the edge doesn't exist, this will throw an error.
        node_one, node_two = edge
        self._adj_list[node_one].remove(node_two)
        # Remove the edge from the right vertex to the left if the graph isn't directed.
        if not self.directed:
            self._adj_list[node_two].remove(node_one)



