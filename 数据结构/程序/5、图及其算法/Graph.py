#!/usr/bin/env python
# coding: utf-8

# In[1]:


#在邻接表实现中，我们为图对象的所有顶点保存一个主列表，同时为每一个顶点对象都维护一个列表，其中记录了与它相连的顶点
#在对 Vertex 类的实现中，我们使用字典（而不是列表），字典的键是顶点，值是权重


# In[2]:


class Vertex: #每个实例对应一个顶点
    def __init__(self, key):
        self.id = key #初始化id（顶点）
        self.connectedTo = {} #初始化与其连接的其他点及权重（字典）
        self.color = 'white'
        self.dist = 100000 #一个很大的值
        self.pred = None
        self.disc = 0
        self.fin = 0
    
    def addNeighbor(self, nbr, weight=0): #为顶点添加一个相邻节点和权重
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self): #返回邻接表中的所有顶点，由 connectedTo 来表示
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr): #返回从当前顶点到以参数传入的顶点之间的边的权重
        return self.connectedTo[nbr]
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
        
    def setDistance(self,d):
        self.dist = d
    
    def getDistance(self):
        return self.dist

    def setPred(self,p):
        self.pred = p

    def getPred(self):
        return self.pred
    
    def setDiscovery(self, dtime):
        self.disc = dtime
    
    def getDiscovery(self):
        return self.disc
        
    def setFinish(self, ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin


# In[3]:


class Graph: #新建一个空图
    def __init__(self):
        self.vertList = {} #初始化包含顶点的字典
        self.numVertices = 0 #顶点个数
    
    def addVertex(self, key): #向图中添加一个顶点实例
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key) #创建一个顶点实例
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n): #在图中找到名为n的顶点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, cost=0): #向图中添加一条带权重cost的有向边，用于连接顶点f和t
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    
    
    def getVertices(self): #以列表形式返回图中所有顶点
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())