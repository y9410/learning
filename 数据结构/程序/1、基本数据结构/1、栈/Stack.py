#!/usr/bin/env python
# coding: utf-8

# # 构造栈

# In[8]:


#栈的实现（假设列表的尾部是栈的顶端）
class Stack: #创建一个空栈。它不需要参数，且会返回一个空栈
    def __init__(self):
        self.items = []

    def isEmpty(self): #将一个元素添加到栈的顶端。它需要一个参数 item，且无返回值
        return self.items == []

    def push(self, item): #将栈顶端的元素移除。它不需要参数，但会返回顶端的元素，并且修改栈的内容。复杂度：O(1)
        self.items.append(item)

    def pop(self): #返回栈顶端的元素，但是并不移除该元素。它不需要参数，也不会修改栈的内容。复杂度：O(1)
        return self.items.pop()

    def peek(self): #检查栈是否为空。它不需要参数，且会返回一个布尔值
        return self.items[len(self.items)-1]
        
    def size(self): #返回栈中元素的数目。它不需要参数，且会返回一个整数
        return len(self.items)


# In[ ]:




