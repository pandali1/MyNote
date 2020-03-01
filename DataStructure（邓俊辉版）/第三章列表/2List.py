class ListNode(object):
    '''节点类'''
    def __init__(self,data = None,prev = None,nexT = None):
        self.data = data
        self.next = nexT
        self.prev = prev

class List(object):
    '''双向链表'''
    def __init__(self):
        self.header = ListNode(float('-inf'))
        self.trailer = ListNode(float('-inf'))
        self.header.next = self.trailer
        self.header.prev = None
        self.trailer.prev = self.header
        self.trailer.next = None
        self.length = 0
    def __len__(self):
        return self.length
    
    def __getitem__(self,index):
        '''定义索引访问操作'''
        h = self.header
        i=0
        if isinstance(index,int):
            if index < 0:
                index += self.length
            if index >= self.length or index < 0:
                raise IndexError
            while(i<index+1):
                i+=1
                h = h.next
            return h.data
        elif isinstance(index,slice):
            return [ self[x] for x in range(*index.indices(len(self)))]
        
    def __setitem__(self,index,v):
        '''定义通过索引赋值'''
        h = self.header
        i=0
        while(i<index+1):
            i+=1
            h = h.next
        h.data = v
        return 
    def find(self,e,p =None,n =None):
        '''从后向前寻找到第一个值并返回节点'''
        if(p == None):
            p =self.trailer
            n = self.length           
        while(n>0):
            n-=1
            p = p.prev
            if(e==p.data):
                return p
        return None
    
    def __getnode(self,index):
        '''返回某一索引值的节点'''
        h = self.header
        i=0
        while(i<index+1):
            i+=1
            h = h.next
        return h
    def insertAsFirst(self,e):
        '''在首位置插入'''
        self.insertBefore(e,0)
        
    def append(self,e):
        '''在末位置插入元素'''
        self.length +=1
        p = self.trailer.prev
        self.insertAsPred(e,p)
    
    def insertAfter(self,e,index):
        '''在index之后插入元素'''
        self.length +=1
        p = self.__getnode(index)
        self.insertAsPred(e,p)
    
    def insertBefore(self,e,index):
        '''在index之前插入e'''
        self.length +=1
        p = self.__getnode(index).prev
        self.insertAsPred(e,p)
        return 
    def insertAsPred(self,e,p):
        '''插入函数，将e插入到P节点之后'''
        B= p
        L = p.next
        node = ListNode(e,B,L)
        L.prev = node
        B.next =node
        
    def copy(self,index = 0,n =0):
        '''将index后的n个元素复制'''
        if(n ==0):
            n = self.length
        L = List()
        node = self.__getnode(index)
        if(node == self.trailer):#如果列表为空，则L[0] = trailer
            node = node.prev
        while(n>0):
            n-=1
            L.append(node.data)
            node = node.next
        return L
    
    def remove(self,index):
        '''删除index节点'''
        self.length -=1
        node = self.__getnode(index)
        return self.__remove(node)
    def __remove(self,p):
        ''' 删除P节点'''
        e = p.data
        p.prev.next = p.next
        p.next.prev = p.prev
        del p
        return e
    
    def clear(self):
        '''清空列表'''
        size = self.length
        while(size>0):
            x = self.header.next
            self.length -=1
            self.__remove(x)
            size -=1
            
    def deduplicate(self):
        '''去除重复元素'''
        l = self.length
        if(self.length <2):
            return 0
        p = self.header
        r = 0
        while(not p == self.trailer):
            p = p.next
            q = self.find(p.data,p,r)
            if(not q==None):
                self.length -=1
                self.__remove(q)
            else:
                r+=1
        return l - self.length
    
    def traverse(self,func = None):
        '''遍历列表元素，并执行一定操作'''
        if(not func == None):
            h = self.header.next
            while(not h ==self.trailer):
                h.data = func(h.data)
                h = h.next
                
                
    ##########################有序列表
    def uniquify(self):
        '''删除重复元素'''
        if(self.length <2):
            return 0
        size = self.length
        p = self.header
        q = p.next
        while(not q == self.trailer ):
            if(p.data == q.data):
                self.length -=1
                self.__remove(q)
            p = q
            q = q.next
        return size - self.length
    
    def search(self,e,n = -1,p =None):
        '''查找不大于e或等于e的最后一个元素'''
        if(p == None):
            p =self.trailer
            n =self.length
        while(n>-1):
            n -=1
            p = p.prev
            if(p.data <= e):
                break
        return p# 失败时返回header
    
    def insertsort(self):
        '''插入排序法'''
        p =self.header.next
        n = 0
        while(not p == self.trailer):
            x = self.search(p.data,n,p)
            self.insertAsPred(p.data,x)
            p = p.next
            n+=1
            self.__remove(p.prev)
            
    def selectsort(self):
        '''选择排序'''
        p = self.trailer
        while(not p == self.header.next):
            x = self.Max(p.prev)
            self.insertAsPred(x.data,p.prev)
            self.__remove(x)
            p = p.prev
    
    def Max(self,p=None):
        '''选择p之前最大值'''
        if(p == None):
            p =self.trailer.prev
        x = p.data
        y = p
        while(not p == self.header):
            p = p.prev
            if(x < p.data):
                x = p.data
                y = p
        return y
    
    def mergesort(self,p =None,n = -1):
        '''归并排序法'''
        #print('s',p.data,n)
        if(n ==-1):
            n = self.length
            p =self.header.next
        if(n <2):
            return p
        m = n>>1
        q = p
        for i in range(m):
            q = q.next

        p = self.mergesort(p,m)

        q = self.mergesort(q, n - m)

        #print(p.data, q.data)
        #print(self.__getnode(0).data, self.__getnode(1).data, self.__getnode(2).data, self.__getnode(3).data)
        return self.merge(p,m,q,n-m)


    def merge(self,p,m,q,n):
        pp = p.prev
        while(m>0):
            if(n>0 and p.data < q.data):
                p = p.next
                if(q == p):
                    break
                n-=1
            else:
                q = q.next
                self.insertAsPred(self.__remove(q.prev),p.prev)
                m -= 1
        p = pp.next
        #print('m', p.data, q.data)
        return p
