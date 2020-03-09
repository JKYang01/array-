
## find the maximum area 

def maxArea(self, height: List[int]) -> int:
        area = 0 
        i,j=0,len(height)-1
        while i<j:    
            area = max(area,(j-i)*min([height[i],height[j]]))
            i1,j1 = i,j  # transform the value to new variable
            if height[i]<= height[j]: 
                i1+=1  # move inward 
                while i1<j and height[i1]<=height[i]:
                    i1+=1    # make comparison and move under the condition untill finde a taller one
            
            if height[i] >= height[j]:
                j1-=1
                while i1<j1 and height[j1]<= height[j]:
                    j1-=1  # make comparison and move inward untill find a taller one
            
            i,j=i1,j1 # updata the value

        return area

## simpler solution! 
## compare the two heights on the left an right bound rather than compare to the on next 
    
    def maxArea(self, h: List[int]) -> int:
        area, l, r = 0, 0, len(h) - 1
        for i in range(len(h)): # use for loop 
            if l > r:
                break
            # here it compare the result of current area to the previous max one
            # so that we do not have to compare the heights to the next seperately like the first solution
            area = max(area, min(h[l], h[r]) * (r - l))  
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1

        return area
