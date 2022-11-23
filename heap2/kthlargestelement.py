class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #creating a array
        hq=[]
        
        #iterate through the nums array
        for num in nums:
            #pushing every element in the heap 
            heappush(hq,num)
            #if the lenght of array is greater than k
            if len(hq)>k:
                #then pop the element
                heappop(hq)
                
        #returning the top of heap        
        return hq[0]
        