from project_task import Task
from project import Project

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
'''
       
if __name__ == '__main__':
    p = Project(name='my test project', description='testing')
    t1 = Task(name='call barrett', description='')
    t2 = Task(name='call brandon', description='')
    t3 = Task(name='research', description='')

    p.add_task(p.BASE, t1)
    p.add_task(t1, t2)
    p.add_task(p.BASE, t3)

    t4 = p.get_task('research')

    print(t4)
    print(p)