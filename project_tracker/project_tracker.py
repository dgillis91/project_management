
from collections import defaultdict 
from project_task import Task
from graph import Graph 

'''
@Description:
@Author:        David Gillis
@Created:       05.18.2018
@ToDo:          * Update Documentation
                * Move the graph objects into a module, and enhance to handle more situations. This will include implementing it multiple ways,
                  including an adjacency matrix.
                * Implement get attr, etc, so that we can access tasks by name. This may be tricky, because it has to be implemented in the base class, Graph.
                * Consolidate ToDo statements from comments.
                * We need to look at how a graph is implemented in networkxx. It may be better to implement adding edges and vertices, seperately. 
                * Look into how to add edges without requiring the end user to search for the vertex they want to add.
                !!! Decide how to run the Graph.__init__(...). It is possible to set the edges in a directed fashion on a non directed graph.
                !!! Decide whether we want to have all vertices in the adjacency list.
'''

class Project(object):
    def __init__(self, name, description):
        self._base_task_node = Task(name='start', description='base node for all projects')
        self._task_struct = Graph(vertices=[self.BASE], edges=None, directed=True)

        self._name = name 
        self._description = description

    ''' --- Properties --- '''
    @property
    def task_list(self):
        return self._task_struct.vertices
    @property
    def name(self):
        return self._name 
    @property 
    def description(self):
        return self._description 
    @property
    def BASE(self):
        return self._base_task_node

    ''' --- Primary Methods --- '''
    def add_task(self, prerequisite, task):
        self._task_struct.add_vertex(task)
        self._task_struct.add_edge((prerequisite, task))

    def remove_task(self, task):
        self._task_struct.remove_vertex(task)

    ''' --- Magic Methods --- '''
    def __len__(self):
        return len(self.task_list)

    def __str__(self):
        _ret = defaultdict(set)
        for vertex, edge in self._task_struct.adjacency_list.items():
            _ret[vertex.name] = set([x.name for x in list(edge)])
        return '{}({})'.format(self.__class__.__name__, dict(_ret))
       
if __name__ == '__main__':
    p = Project(name='my test project', description='testing')
    t1 = Task(name='call barrett', description='')
    t2 = Task(name='call brandon', description='')
    t3 = Task(name='research', description='')

    p.add_task(p.BASE, t1)
    p.add_task(t1, t2)
    p.add_task(p.BASE, t3)

    print(p)