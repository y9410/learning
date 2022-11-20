#!/usr/bin/env python
# coding: utf-8

# In[1]:


#双端队列是与队列类似的有序集合
#它有一前、一后两端，元素在其中保持自己的位置
#与队列不同的是，双端队列对在哪一端添加和移除元素没有任何限制


# In[3]:


class Deque: #创建一个空的双端队列。它不需要参数，且会返回一个空的双端队列
    def __init__(self):
        self.items = []

    def isEmpty(self): #检查双端队列是否为空。它不需要参数，且会返回一个布尔值
        return self.items == []

    def addFront(self, item): #将一个元素添加到双端队列的前端。它接受一个元素作为参数，没有返回值。复杂度：O(1)
        self.items.append(item)

    def addRear(self, item): #将一个元素添加到双端队列的后端。它接受一个元素作为参数，没有返回值。复杂度：O(n)
        self.items.insert(0, item)

    def removeFront(self): #从双端队列的前端移除一个元素。它不需要参数，且会返回一个元素，并修改双端队列的内容。复杂度：O(1)
        return self.items.pop()

    def removeRear(self): #从双端队列的后端移除一个元素。它不需要参数，且会返回一个元素，并修改双端队列的内容。复杂度：O(n)
        return self.items.pop(0)

    def size(self): #返回双端队列中元素的数目。它不需要参数，且会返回一个整数
        return len(self.items)


# In[ ]:




