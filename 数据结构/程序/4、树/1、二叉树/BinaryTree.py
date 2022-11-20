#!/usr/bin/env python
# coding: utf-8

# In[9]:


#“节点与引用”的二叉树表示方法遵循面向对象编程范式，因此采用这种方法
#定义一个类，其中有根节点和左右子树的属性


# In[12]:


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode): #新建一棵二叉树，并将其作为当前节点的左子节点
        if self.leftChild == None: #若当前节点没有左子节点
            self.leftChild = BinaryTree(newNode) #直接添加一个左子节点
        else: #若当前节点有左子节点，则插入一个节点，并将已有的左子节点降一层
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode): #新建一棵二叉树，并将其作为当前节点的右子节点
        if self.rightChild == None: #若当前节点没有右子节点
            self.rightChild = BinaryTree(newNode) #直接添加一个右子节点
        else: #若当前节点有右子节点，则插入一个节点，并将已有的右子节点降一层
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t
    
    def getRightChild(self): #返回当前节点的右子节点所对应的二叉树
        return self.rightChild
    
    def getLeftChild(self): #返回当前节点的左子节点所对应的二叉
        return self.leftChild
    
    def setRootVal(self, obj): #在当前节点中存储参数obj中的对象
        self.key = obj
    
    def getRootVal(self): #返回当前节点存储的对象
        return self.key
    
    def preorder(self): #前序遍历
        print(self.key)
        if self.leftChild:
            self.left.preorder()
        if self.rightChild:
            self.right.preorder()