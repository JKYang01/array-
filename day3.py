### 3 sum 
'''Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]'''



### my solution refined 





## others solution 
## separate different conditon insimpler way 
def threeSum(self, nums: List[int]) -> List[List[int]]:
  nums.sort()
  size = len(nums)
  solution = []
  
  for idx in range(0, size-2):
    # avoid repetition
    if idx and nums[idx] == nums[idx-1]:
      idx +=1
      pass
      continue
      
      first_num = nums[idx] 
      target = -first_num
      i, j = idx+1, size-1
      while i < j:
          cur_two_sum = nums[i] + nums[j]
          if cur_two_sum > target:
            j -=1
          elif cur_two_sum < target:
              i += 1
          else:
            solution.append( [ first_num, nums[i], nums[j] ] )
            i += 1
            j -= 1
                    
					# avoid repetition
        while i < j and nums[i] == nums[i-1]:
            i += 1
                    
					# avoid repetition
        while i < j and nums[j] == nums[j+1]:
            j -= 1
                    
    return solution

# solution 1  using the math function and making a hash table with collection.counter()

def threeSum(self, nums: List[int]) -> List[List[int]]:
        C=collections.Counter(nums)
        finds,results,bisl=sorted(C),set([(0,0,0)]) if C[0]>=3 else set(),bisect.bisect_left
        for i,k1 in enumerate(finds):
            if C[k1]>1 and -2*k1 in C and k1:   results.add((k1,k1,-2*k1))
            if k1<0:
                for k2 in finds[bisl(finds,-finds[-1]-k1,i+1):bisl(finds,math.ceil(-k1/2),i+1)]:
                    if -(k1+k2) in C:results.add((k1,k2,-k1-k2))
        return results
                
## solution 2 3rd num shoud be -(1stnum + 2nd num) making two sets that contains the positive and negative 
def threeSum(self, nums: List[int]) -> List[List[int]]:
# Hash maps (dict) to store neg/pos integer counts.
    neg = {}
    pos = {}
    zeros = 0

    # Hash set to store tuples of valid solutions.
    # Automatically handles duplicate solutions if we add
    # sorted tuples to it.
    solutions = set()

# Initializing our counter. O(n).
    for i in nums:
        if i < 0:
            neg.setdefault(i, 0)
            neg[i] += 1
        elif i > 0:
            pos.setdefault(i, 0)
            pos[i] += 1
        else:
            zeros += 1

        # We iterate through all unique values of nums.
        # Note: 'i' and 'j' are always opposite in parity. i.e. 'i'
        # and 'j' will never both be positive or both be negative.
    for i in {num for num in nums}:
            # Seeking positive numbers to offset negative numbers.
         if i < 0:
            for j in pos:
                    # Seek for third number, k = -(i + j) 
                k = -i - j
                if k in pos:
                        # Invalid solution;
                    if k == j and pos[j]-1 < 1:
                            continue
                        # Valid solution;
                    else:
                        solutions.add(tuple(sorted((i, j, k))))
                    # If third number is '0' and we have zeros to use.
                elif k == 0 and zeros > 0:
                    solutions.add(tuple(sorted((i, j, 0))))

            # Logic below is nearly identical logic as above. Kept it verbose for readibility.

            # Seeking negative numbers to offset postive numbers.
        elif i > 0:
            for j in neg:
                k = -i - j
                if k in neg:
                    if k == j and neg[j]-1 < 1:
                        continue
                    else:
                        solutions.add(tuple(sorted((i, j, k))))
                 elif k == 0 and zeros > 0:
                    solutions.add(tuple(sorted((i, j, 0))))

            # If we encounter a zero, check to see we have 3 or more.
        elif zeros >= 3:
            solutions.add((0, 0, 0))

    return [list(s) for s in solutions]

#### my solution: wrong answer not consider [0,0,0] condition

def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nnums = []
        n=0 # the seed 
        i = n+1
        l2 = []
        # the condtion of 0,0,0
        #if nums[index] and nums[index+1] == nums[index+2]
        # sort the imput list
        while nums:
            mini = nums[0]
            for x in nums:
                if x< mini:
                    mini = x
            
            nnums.append(mini)
            nums.remove(mini)
            
            print(nnums)
            
        # get three nums 
        while n<= len(nnums)-3:
            # if nnums[n] and nnums[n+1] == nnums[n+2]:
            #     pass
            #     continue 
            for i in (n+1, len(nnums)-2):
                for j in (i+1, len(nnums)-1):
                    l3 = [nnums[n],nnums[i],nnums[j]]
                    if sum(l3)==0:  
                        l2.append(l3)  
            n+=1
        
        return l2
            
