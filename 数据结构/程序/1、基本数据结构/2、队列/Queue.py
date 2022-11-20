#!/usr/bin/env python
# coding: utf-8

# In[1]:


#队列是有序集合，添加操作发生在“尾部”，移除操作则发生在“头部”
#新元素从尾部进入队列，然后一直向前移动到头部，直到成为下一个被移除的元素
#最新添加的元素必须在队列的尾部等待，在队列中时间最长的元素则排在最前面。这种排序原则被称作 FIFO（ first-in first-out），即先进先出，也称先到先得


# In[2]:


class Queue: #创建一个空队列。它不需要参数，且会返回一个空队列
    def __init__(self):
        self.items = []

    def isEmpty(self): #检查队列是否为空。它不需要参数，且会返回一个布尔值
        return self.items == []

    def enqueue(self, item): #在队列的尾部添加一个元素。它需要一个元素作为参数，不返回任何值。复杂度：O(n)
        self.items.insert(0, item)

    def dequeue(self): #从队列的头部移除一个元素。它不需要参数，且会返回一个元素，并修改队列的内容。复杂度：O(1)
        return self.items.pop()
    
    def size(self): #返回队列中元素的数目。它不需要参数，且会返回一个整数
        return len(self.items)


# In[ ]:




