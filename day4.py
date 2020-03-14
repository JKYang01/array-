## Three sum best solution 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()# sort it first [-4,-1,-1,0,1,2]
        ans = set()
        # the v here is the first number, -v the target in two_sum function
        # the two_sum is first_number*-1
        for i,v in enumerate(nums):
            # get the first number v, and then find two nums in the rest of the list
            # process the two
            self.twoSum(nums[i+1:],-v,ans)
            #print (ans)
        return ans
    
    def twoSum(self,nums,target,ans):
        d = {}
        for i,v in enumerate(nums): # the nums here is start from -1 
            if target-v in d: -nums[i]-nums[i+1]
                #3sum wants the numbers, while 2sum wanted the indices
                ans.add((v,target-v,-target)) 
            d[v] = i # make a dictionary of the index of numbers number:index
            print (d)
            print(ans)
