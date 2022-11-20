#!/usr/bin/env python
# coding: utf-8

# In[2]:


#二叉搜索树依赖于这样一个性质：小于父节点的键都在左子树中，大于父节点的键则都在右子树中。我们称这个性质为二叉搜索性


# In[3]:


#采用“节点与引用”表示法实现二叉搜索树


# In[4]:


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val): #往映射中加入一个新的键–值对。如果键已经存在，就用新值替换旧值
        if self.root: #若当前树有根节点
            self._put(key, val, self.root) #若有，就调用私有的递归辅助函数_put
        else: #若没有，就创建一个TreeNode，并将其作为树的根节点
            self.root = TreeNode(key, val)
            self.size = self.size + 1
    
    '''插入方法有个重要的问题：不能正确地处理重复的键。遇到重复的键时，它会在已有节点的
       右子树中创建一个具有同样键的节点。这样做的结果就是搜索时永远发现不了较新的键。要处理
       重复键插入，更好的做法是用关联的新值替换旧值'''
    def _put(self, key, val, currentNode):
        if key < currentNode.key: #若要插入的新键小于当前节点的键
            if currentNode.hasLeftChild(): #且当前结点有左子树
                self._put(key, val, currentNode.leftChild) #递归
            else: #基本情况：当前节点没有左子树，则新建一个左子节点
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
    
    def __setitem__(self, k, v): #调用put方法来重载[]运算符，可以使用类似字典的写法
        self.put(k, v)
        
    def get(self, key): #返回key对应的值。如果key不存在，则返回None
        if self.root:
            res = self._get(key, self.root) #给定一个TreeNode
            if res:
                return res.payload #返回key对应的值
            else:
                return None
        else:
            return None
    
    def _get(self, key, currentNode):
        if not currentNode: #若要找的节点不存在，返回None
            return None
        elif currentNode.key == key: #基本情况：找到对应key的节点
            return currentNode
        elif key < currentNode.key: #若要找的key小于当前节点key，向左子树递归
            return self._get(key, currentNode.leftChild)
        else: #否则向右子树递归
            return self._get(key, currentNode.rightChild)
            
    def __getitem__(self, key): #调用get方法来重载[]运算符
        return self.get(key)
    
    def __contains__(self, key): #检查树中是否有某个key，该方法重载了in运算符
        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        if self.size > 1: #如果树中不止一个节点，使用_get方法搜索，找到要移除的TreeNode
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key: #如果树只有一个节点，那么判断是否相同
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
    
    def __delitem__(self, key): #重载del（del obj[“name”]）
        self.delete(key)
        
    def remove(self, currentNode):
        if currentNode.isLeaf(): #情况一：待删除节点是叶子节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None #移除父节点对该叶子节点的引用
            else:
                currentNode.parent.rightChild = None #移除父节点对该叶子节点的引用
        
        elif currentNode.hasBothChildren(): #情况三：待删除节点有两个子节点
            succ = currentNode.findSuccessor() #找到后继节点（能为左右子树都保持二叉搜索树的关系）
            succ.spliceOut() #直接移除节点（使用delete会浪费时间重复搜索）
            currentNode.key = succ.key
            currentNode.payload = succ.payload
    
        else: #情况二：待删除节点只有一个子节点
            if currentNode.hasLeftChild(): #若当前节点仅有的子节点是左子节点
                if currentNode.isLeftChild(): #若当前节点是左子节点
                    currentNode.leftChild.parent = currentNode.parent #将当前节点的左子节点对父节点的引用改为指向当前节点的父节点
                    currentNode.parent.leftChild = currentNode.leftChild #将父节点对当前节点的引用改为指向当前节点的左子节点
                elif currentNode.isRightChild(): #若当前节点是右子节点
                    currentNode.leftChild.parent = currentNode.parent #将当前节点的左子节点对父节点的引用改为指向当前节点的父节点
                    currentNode.parent.rightChild = currentNode.leftChild #将父节点对当前节点的引用改为指向当前节点的右子节点
                else: #若当前节点没有左子节点，则它是一个根节点
                    currentNode.replaceNodeData(currentNode.leftChild.key, #替换根节点的 key、 payload、 leftChild 和 rightChild 数据
                                                currentNode.leftChild.payload, 
                                                currentNode.leftChild.leftChild, 
                                                currentNode.leftChild.rightChild)
    
            else: #若当前节点仅有的子节点是右子节点，与上三种情况类似
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, 
                                                currentNode.rightChild.payload, 
                                                currentNode.rightChild.leftChild, 
                                                currentNode.rightChild.rightChild)


# In[5]:


class TreeNode: #一个辅助类，代表每个节点
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent #与BinaryTree类的一个很大的区别是显式地将每个节点的父节点记录为它的一个属性
        self.balanceFactor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self #“== self”用于判断是否为类的一个实例
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    
    def findSuccessor(self): #寻找后继节点
        succ = None
        if self.hasRightChild(): #如果节点有右子节点，那么后继节点就是右子树中最小的节点
            succ = self.rightChild.findMin()
        else: #如果节点没有右子节点（左子树的节点都小于当前节点）
            if self.parent:
                if self.isLeftChild(): #节点本身是父节点的左子节点，那么后继节点就是父节点（父节点必定大于当前节点左子树的节点）
                    succ = self.parent
                else: #节点本身是父节点的右子节点，那么后继节点就是除其本身外父节点的后继节点
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor() #由于不能是节点本身（因为要删掉），因此再次从父节点出发寻找后继节点
                    self.parent.rightChild = self
        return succ
        
    def findMin(self): #查找子树中最小的键，在任意二叉搜索树中，最小的键就是最左边的子节点
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    
    def spliceOut(self): #用于删除某个节点
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    
    '''二叉树的遍历是中序遍历：在中序遍历中，先递归地中序遍历左子树，然后访问根节点，最后递归地中序遍历右子树'''
    def __iter__(self): #二叉搜索树迭代器，重载了循环的 for x in 操作
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem #与return类似，yield每次向调用方返回一个值。除此之外，yield还会冻结函数的状态，因此下次调用函数时，会从这次离开之处继续
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem


# In[ ]:




