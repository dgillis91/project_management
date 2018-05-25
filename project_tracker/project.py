from project_task import Task
from collections import defaultdict
from graph import Graph

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

    def get_task(self, name):
        for task in self.task_list:
            if task.name == name:
                return task

    ''' --- Magic Methods --- '''
    def __len__(self):
        return len(self.task_list)

    def __str__(self):
        _ret = defaultdict(set)
        for vertex, edge in self._task_struct.adjacency_list.items():
            _ret[vertex.name] = set([x.name for x in list(edge)])
        return '{}({})'.format(self.__class__.__name__, dict(_ret))