import random as rand
import sys

class Sorts:
    
    #Sorting Methods
    #Helper - Swap two elements
    def SwapPositions(self, A, i, j):
        A[i], A[j] = A[j], A[i]
        return A

    #SELECTIONSORT -- COMPLETE
    def SelectionSort(self, A):
        """
        for i <- 0 to A.length-1:
            #task: swap an elt into A[i]
            min_pos = i
            for j <- i+1 to A.length-1:
                if A[j] < A[min_pos]:
                    min_pos = j
            swap(A, i, min_pos) #w/in A, swap i and min_pos
        """
        for i in range(0,len(A)-1):
            min_pos = i
            for j in range(i+1, len(A)-1):
                if A[j] < A[min_pos]:
                    min_pos = j
            A = self.SwapPositions(A, i, min_pos)
            #A[i], A[min_pos] = A[min_pos], A[i]
        return A
    
    #INSERTIONSORT -- COMPLETE
    def InsertionSort(self, A):
        """
        for i<-1 to A.length
            key = A[i]
            j = i-1
            while j >= 0 and key < A[j]:
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
        """
        for i in range(1,len(A)):
            key = A[i]
            j = i-1
            while j >= 0 and key < A[j]:
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
        return A
    
    #MERGESORT -- COMPLETE
    def MergeSort(self, A):
        """
        if(h<=lo) return
        int mid = (lo+hi)/2
        MergeSort(A,lo,mid)
        MergeSort(A,mid+1,hi)
        merge(A,lo,mid,hi)
        
        if (hi <= lo):
            return
        mid = (lo+hi)/2

        A = self.Merge(self.MergeSort(A,lo,mid),self.MergeSort(A,mid+1,hi))

        return A
        """
        if len(A) > 1:
            mid = len(A)//2
            L = A[:mid]
            R = A[mid:]
            self.MergeSort(L)
            self.MergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    A[k] = L[i]
                    i +=1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                A[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                A[k] = R[j]
                j += 1
                k += 1
        return A
    
    #QUICKSORT HELPER -- COMPLETE
    def Partition(self, A, lo, hi, r):
        #Quicksort Helper
        #Partition A[lo..hi] arond elt in pos r
        #Return its final location
        A = self.SwapPositions(A,r,lo)
        i = lo + 1
        j = hi
        x = A[lo]
        while(i<=j):
            if(A[i] < x):
                i = i + 1
            elif(A[j] >= x):
                j = j-1
            else:
                A = self.SwapPositions(A, i, j)
                i = i + 1
                j = j + 1
        A = self.SwapPositions(A, lo, j)
        return j

    #QUICKSORT -- COMPLETE
    def QuickSort(self, A, lo, hi):
        """
        if(hi>lo)
            r = rand(lo,hi)
            p = partition(A,lo,hi,r)
            QuickSort(A,lo,p-1)
            QuickSort(A,p+1,hi)
        """
        if hi > lo:
            r = rand.randint(lo,hi)
            p = self.Partition(A, lo, hi, r)
            self.QuickSort(A, lo, p-1)
            self.QuickSort(A, p+1, hi)
        return A

arr = []
sys.setrecursionlimit(1500)
length = 20
for i in range(0,length):
    #arr[i] = rand.randint(0,100)
    arr.append(rand.randint(0,100))
print(arr)
s = Sorts()
#b = s.QuickSort(arr, 0, 49)

b = s.MergeSort(arr)
print(b)
