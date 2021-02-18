class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        n = len(nums) 
        heap = []
        if n!=0:
            heap = [nums[0]]
            for i in range(1,n):
                heap = self.make_heap(heap,nums[i])

        while len(heap)>k:
            heap = self.del_smallest(heap)

        self.heap = heap   
        
        

    def add(self, val: int) -> int:
        
        if len(self.heap)<self.k:
            self.heap = self.make_heap(self.heap,val)
        else:    
            self.heap = self.make_heap(self.heap,val)
            self.heap = self.del_smallest(self.heap)
            
            
        return self.heap[0]
                
                
    def make_heap(self,heap,val):
        isminheap = False
        ind = len(heap)
        heap.append(val)
        while isminheap is False and ind!=0:
            ind_par = (ind-1)//2
            minnum = heap[ind]
            if heap[ind_par]>minnum:            
                heap[ind] =  heap[ind_par] 
                heap[ind_par] = minnum
                ind = ind_par
            else:
                isminheap = True
        return  heap
    
    def del_smallest(self,heap):
        newHeap = heap.copy()
        newHeap[0]=newHeap[-1]
        newHeap.pop()
        
        organized = False
        ind = 0
        while organized is False:
            l = 2*ind+1            
            r = 2*ind+2
            if l >=len(newHeap):
                break

            smaller_ind = l
            m = newHeap[l]
            
            if r<len(newHeap):
                
                if newHeap[r]<newHeap[l]:
                    m = newHeap[r]
                    smaller_ind = r


            if m<newHeap[ind]:                
                newHeap[smaller_ind] = newHeap[ind]
                newHeap[ind] = m 
                ind = smaller_ind
            else:
                organized = True

        return newHeap
        
        