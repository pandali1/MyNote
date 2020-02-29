class Fib:
    '''生成斐波那契数列'''
    def next1(self):
        self.g += self.f
        self.f = self.g - self.f
        return self.g
    def prev(self):
        self.f = self.g - self.f
        self.g -= self.f
        return self.g
    def get(self):
        return self.g
    def __init__(self,n):
        self.f = 1
        self.g =0
        while (self.g<n):
            self.next1()

import random as rd
class Vector(object):
    '''向量类：python实现'''
    def __init__(self,a=0):
        if a:
            self.item = a
            self.length = len(self.item)
        else:
            self.item = []
            self.length = 0
        
    def size(self):
        return self.length

    def empty(self):
        return self.length == 0

    def get(self,r):
        '''
            获取秩为r的元素
        '''
        if r < 0 or r> self.length:
            print('r must between :{0} and:{1}'.format(0,self.length))
            return
        return self.item[r]

    def put(self,r,e):
        '''用e代替r位置的值'''
        self.item[r] = e

    def insert(self,r,e):
        '''在r位置插入e'''
        self.item.insert(r,e)
        self.length +=1
    def swap(x,y):
        return y,x

    def unsort(self):
        #随机置乱
        for i in range(self.length,0,-1):
            x = rd.randint(0,i-1) % i
            self.item[i-1],self.item[x] = Vector.swap(self.item[i-1],self.item[x])

    def find(self,e,lo =0,hi =-1):
        #顺序查找某个值的匹配的较小索引
        if(hi == -1):
            return self.item.index(e)
        else:
            for i in range(lo,hi):
                if self.item[i] == e:
                    return i
            return -1
    def remove(self,lo,hi =-1):
        #删除从lo到hi的元素，上限不在内
        if (lo == hi):
            return 0
        if(hi == -1):
            hi = lo+1
        while(hi<self.length):
            self.item[lo] = self.item[hi]
            lo+=1
            hi +=1
        for i in range(hi - lo):
            self.item.pop()
        self.length -= (hi - lo)
        return hi - lo
    
    def deduplicate(self):
        '''删除重复元素'''
        leng = self.length
        i =1
        while (i < self.length):
            if self.find(self.item[i],0,i) < 0 :
                i+=1
            else:
                self.remove(i)
        return leng - self.length
    
    def traverse(self,func):
        '''遍历一个向量执行某个操作'''
        for i in range(self.length):
            self.item[i] = func(self.item[i])
        return
    
    def disordered(self):
        '''判断当前存在的逆序对的数量'''
        n=0
        for i in range(1,self.length):
            if self.item[i-1]>self.item[i]:
                n+=1
        return n
    
    #############################有序向量
    def uniquify(self):
        '''有序向量删除重复元素'''
        i,j = 0,1
        while(j < self.length):
            if(not self.item[i]== self.item[j]):
                i+=1
                self.item[i] = self.item[j]
            j+=1
        self.remove(i+1,self.length)
        self.length = i+1
        return j-i
    
    def binSearchA(self,e,lo=-1,hi=-1):
        '''二分查找算法,上限不在内'''
        if(lo==-1):
            lo = 0
            hi = self.length
        while (lo<hi):
            m = (lo+hi)>>1
            if(e<self.item[m]):
                hi = m
            elif(self.item[m]<e):
                lo = m+1
            else:
                return m
        return -1
    
    def binSearchC(self,e,lo=-1,hi =-1):
        '''返回不大于e的最大元素的最大秩'''
        if(lo==-1):
            lo = 0
            hi = self.length
        while (lo<hi):
            m = (lo+hi)>>1
            if(e<self.item[m]):
                hi = m
            else:
                lo = m+1
        return lo -1
    
    def fibSearch(self,e,lo=-1,hi=-1):
        if(lo==-1):
            lo = 0
            hi = self.length
        fib= Fib(hi - lo)
        while (lo<hi):
            while(hi-lo<fib.get()):
                fib.prev()
            m = lo +fib.get() -1
            if(e<self.item[m]):
                hi = m
            elif(self.item[m]<e):
                lo = m+1
            else:
                return m
        return -1
    
    def search(self):
        '''有序向量进行查找'''
        if(rd.randint(0,11)%2):
            return self.binSearch(self,e,lo,hi)
        else:
            return self.fibSearch(self,e,lo,hi)
        
    def bubbleSort(self,lo=-1,hi=-1):
        '''冒泡排序'''
        if(lo==-1):
            lo = 0
            hi = self.length
        while(True):
            hi = self.bubble(lo,hi)
            if lo < hi:
                continue
            else:
                return
            
    def bubble(self,lo,hi):
        last = lo
        while(lo<hi-1):
            lo+=1
            if(self.item[lo-1]>self.item[lo]):
                last  = lo
                self.item[lo-1],self.item[lo] = Vector.swap(self.item[lo-1],self.item[lo] )
                
        return last
    
    def mergeSort(self,lo=-1,hi =-1):
        '''归并排序'''
        if(lo==-1):
            lo = 0
            hi = self.length
        if(hi - lo <2):
            return
        mi = (lo+hi)>>1
        self.mergeSort(lo,mi)
        self.mergeSort(mi,hi)
        self.merge(lo,mi,hi)
    
    def merge(self,lo,mi,hi):
        A = self.item
        lb = mi - lo
        lc = hi - mi
        B = self.item[lo:mi].copy()
        #print(B)
        C = self.item
        i,j,k = 0,0,0
        while( j<lb or  k<lc):
            if((j<lb) and ((not(k<lc)) or B[j] <= C[mi+k])):                
                A[lo+i] = B[j]
                i+=1
                j+=1
                #print(i)
            if(k<lc and ((not(j<lb)) or B[j]> C[mi+k])):
               # print(i,A[i])
                A[lo+i] = C[mi+k]
                i+=1
                k+=1
        del B