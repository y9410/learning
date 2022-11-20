#!/usr/bin/env python
# coding: utf-8

# In[1]:


#利用二叉堆可以实现优先级队列：优先级队列从头部移除元素，不过元素的逻辑顺序是由优先级决定的，优先级最高的元素在最前，优先级最低的元素在最后


# # 结构属性

# In[2]:


#在实现二叉堆时，通过创建一棵完全二叉树来维持树的平衡
#完全二叉树中，除了最底层，其他每一层的节点都是满的
#完全二叉树可用列表表示
#对于在列表中处于位置 p 的节点来说，它的左子节点正好处于位置2p；同理，右子节点处于位置2p+1


# # 堆的有序性

# In[3]:


#对于堆中任意元素x及其父元素p，p都不大于x


# # 实现

# In[9]:


class BinaryHeap: #新建一个二叉堆
    def __init__(self):
        self.heapList = [0] #列表heapList的第一个元素是 0，它的唯一用途是为了使后续的方法可以使用整数除法
        self.currentSize = 0
        
    def insert(self, k): #往堆中加入一个新元素
        self.heapList.append(k) #向列表末尾插入新元素
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize) #调整新元素的位置
        
    def percUp(self, i): #为了保证堆的有序性，需要将小于父节点的新元素与父节点交换位置
        while i // 2 > 0: #i//2会跳到当前节点的父节点——从子节点一路检查到根节点
            if self.heapList[i] < self.heapList[i // 2]: #如果子节点小于父节点，交换两者的值
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    def delMin(self): #删除堆中最小的元素，并调整堆的结构使之有序
        retval = self.heapList[1] #根节点是最小的元素
        self.heapList[1] = self.heapList[self.currentSize] #将根节点替换为二叉堆最后一个元素
        self.currentSize = self.currentSize - 1 #二叉堆大小减一
        self.heapList.pop() #把最后一个元素删除
        self.percDown(1) #从根节点开始向下检查排列错误的元素并纠正错误
        return retval
    
    def percDown(self, i):
        while (i * 2) <= self.currentSize: 
            mc = self.minChild(i) #取出当前节点的最小子节点的位置
            if self.heapList[i] > self.heapList[mc]: #如果父节点值大于其最小子节点值，交换这两个节点
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc #将i设置为最小子节点位置继续向下判断

    def minChild(self, i): #给定一个父节点，返回最小子节点的位置
        if i * 2 + 1 > self.currentSize: #若父节点只有一个子节点，那么这个子节点就是最小子节点
            return i * 2
        else: #否则两个子节点进行比较，返回最小子节点
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    '''将n个元素插入堆中的操作为O(nlogn) ，因为插入元素时需要移动其他元素，复杂度为O(n)，使用二分搜索查找插入位置的复杂度为O(logn)'''
    '''从完整的列表开始，构建整个堆只需O(n)'''
    def buildHeap(self, alist): #给定用于构建二叉堆的列表，构建一个二叉堆
        i = len(alist) // 2 #最后一个叶子节点的父节点（超过该节点的节点全是叶子节点）
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0): #从后往前遍历所有父节点，并纠正错误（因此一定能保证排序正确）
            self.percDown(i)
            i = i - 1