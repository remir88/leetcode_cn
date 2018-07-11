class Solution:
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if (len(nums)==0):
			return([-1,-1])
		
		#firstly, binary search the target
		i = 0
		j = len(nums)
		mid = (i+j)//2	
		while ((i<j) and (nums[mid]!=target)):
			if (target < nums[mid]):
				j = mid-1
			else:
				i = mid+1
			mid = (i+j)//2
		if (j<0 or i>=len(nums) or nums[mid]!=target):
			return([-1,-1])
		
		#left search
		i = 0
		j = mid
		k = (i+j)//2
		while ((i<j) and nums[k]==target):
			j = k
			k = (i+j)//2
		while ((k<j) and nums[k]!=target):
			k = k+1
		left = k
			
		#right search
		i = mid
		j = len(nums)-1
		k = (i+j)//2
		while ((i<j) and nums[k]==target):
			i = k+1
			k = (i+j)//2
		while ((k>=mid) and (k<len(nums)) and nums[k]!=target):
			k = k - 1
		if (k > len(nums)-1):
			right = len(nums)-1
		else:
			right = k
		return([left, right])

        
        
		
