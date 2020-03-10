### move zero
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastzerofound = 0
        for i in range(len(nums)):
            if nums[i]!=0: # found none zero 
                # exchange the position of zero to non-zero 
                # if there are no 0 nums[i]=nums[lastzerofound]
                # when the loop meets the zero, it will skip it and point to the next-non 0
                # 'lastzerofound' keep the idex of 0 which next to the last non-0 
                # because we set the condition if !=0 at 
                # but the loop skip indx to non-0
                nums[i], nums[lastzerofound]=nums[lastzerofound],nums[i]
                #print(nums[i])
                #print(nums[lastzerofound])
                #print(lastzerofound)
                lastzerofound +=1 # now is it i?
                
        return nums
                



#### 3 sum  num: 35 to be continue.....






