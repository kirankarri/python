from typing import List
import string
import random
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
            #print(num_to_index)
        return []
    def twoSub(self, nums: List[int], target= 1) -> List[int]:
        num_to_index={}
        for i, val in enumerate(nums):
            diff = val - target
            if diff in num_to_index:
                return [num_to_index[diff], i]
            num_to_index[val] = i
        return []
    def twosumNumber(self, num: List[int], target: int, dummy=9) -> List[int]:
        dic = {}
        for i, val in enumerate(num):
            diff = target - val;
            if diff in dic:
                return [diff , val]
            dic[val] = i
        return []
# 1. Create an instance of the class
sol = Solution()

# 2. Pass BOTH arguments (nums and target)
result = sol.twoSum([2, 3, 4, 5], 9)
result1 = sol.twosumNumber([2, 3, 4, 5], 10)
inputList = input('Enter List Number')
# convert the list of string to int
inputListint = list(map(int, inputList.split(',')))
inputListinttrimpy = [x.strip() for x in inputList.split(',')]

print(inputListinttrimpy)
inputListintpy = [int(x) for x in inputList.split(',')]
print([x*2 for x in inputListintpy])
#print(list(map(lambda x:x*2 if x > 3 else , inputListintpy)))
print([x*2 for x in inputListintpy if x>3])
print(inputListint)

print(result) # Output: [2, 3] (because 4 + 5 = 9)
print(result1) 
print('Hello World\nHello World')
print('Welcome to tip calculator!')
x=input('What was your total bill?')
y=input('How much tip would you like to give? 10, 12 or 15?')
z=input('How many people to split the bill?')
print('Each person should pay:'+ str(round(float(x)*(1+float(y)/100)/float(z),2)))#bresult
print('Hello "test"')
friends = ["Friend1","Friend2","Friend3","Friend4","Friend5"]
print(friends[random.randint(0,len(friends)-1)])
student_scores = [1, 44, 33, 29, 39, 494, 2903, 333, 23,2323,344,6456]
    



    
                             