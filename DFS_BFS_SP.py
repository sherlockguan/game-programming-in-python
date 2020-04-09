# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Node(object):
    def __init__(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() +'->'+self.dest.getName()
    
class Digraph(object):
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('duplicate node')
        else:
            self.edges[node] = []
            
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.edges and dest in self.edges):
            raise ValueError('node not in graph')
        self.edges[src].append(dest)
        
    def ChildrenOf(self,node):
        return self.edges[node]
    
    def hasNode(self,node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
        
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName()+'->'\
                +dest.getName()+'\n'
    
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self,edge)
        rev = Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self, rev)


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence','New York','Chicago','Denver','Phoenix',
                 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def printPath(path):
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result+'->'
    return result
""" DFS the algorithm begin by choosing one child of the start node
then choosing one child of that node , going deeper and deeper until
it either reach the goal node or node with no children , the search then backtrack,return the most recent node with children that has not yet been visited, when all paths have been explored it choose the shortest path,assuming there is one,from the start to the goal 
because there might be cycles in the graph, we keep track of the node we visited,so that we dont visit them again
also if we look at the code instead of checking the path at the end of the algorithms,we keep track of the shortest path from the start to the end that we found so far
whenever we found a  new path we discard it if it is not shorter than the path we already found, also a little optimization we dont bother explore the path that is longer than we already found"""




def DFS(graph,start,end,path,shortest,toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:
        print('current path of DFS is', printPath(path))
    
    if start== end:
        return path
    for node in graph.ChildrenOf(start):
        if node not in path:
            if shortest == None or len(path)<len(shortest):
                newPath = DFS(graph, node, end, path,shortest, toPrint)
                if newPath!= None:
                    shortest = newPath
        elif toPrint:
            print('already visited', node)
    return shortest


# wrapper function

def shortestPath(graph, start, end, toPrint = False):
    return DFS(graph, start, end,[],None, toPrint)

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source),g.getNode(destination),toPrint = True)
    if sp!= None:
        print('shortest path from',source,'to',destination, 'is', printPath(sp))
    else:
        print('there is no path from ', source, 'to', destination)
        
testSP('Boston','Phoenix')


def BFS(graph, start , end, toPrint = False):
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('current BFS path: ', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode  in  graph.ChildrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath +[nextNode]
                pathQueue.append(newPath)
    return None

def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)
    
testSP('Boston', 'Phoenix')
  
"""
BFS pathQueue: all the path currently being explored
if last node in the tmp path is end, tmp_path is the shortest path   and returned 
otherwise a set of new path is created.each of which extend the tmp path by adding
one of its children, each of these new path is an added to an pathQueue.
BFS is enumerating path in length order -> notice WHY only one return sp!!!
if we want to minimize the sum of weights of the edges,not the num
of edges so DFS-> WEIGHTED SP
"""


    
    

