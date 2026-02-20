# from typing import List

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False


# # -------- Driver Code --------
# if __name__ == "__main__":
#     nums = list(map(int, input("Enter numbers separated by space: ").split()))
    
#     sol = Solution()
#     result = sol.containsDuplicate(nums)
    
#     print(result)



#     from typing import List

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         result = []
#         combination = []

#         def backtrack(start: int):
#             if len(combination) == k:
#                 result.append(combination[:])
#                 return
            
#             for i in range(start, n + 1):
#                 combination.append(i)
#                 backtrack(i + 1)
#                 combination.pop()

#         backtrack(1)
#         return result

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#         def backtrack(arr,i):
#             if len(arr) == k:
#                 res.append(arr[:])
#                 return
            
#             for j in range(i,n+1):
#                 arr.append(j)
#                 backtrack(arr,j+1)
#                 arr.pop()
#         backtrack([],1)
#         return res
# __import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return int(x ** 0.5)


# # -------- Driver Code --------
# if __name__ == "__main__":
#     x = int(input("Enter a non-negative integer: "))
    
#     sol = Solution()
#     result = sol.mySqrt(x)
    
#     print("Square root (rounded down):", result)

# n=int(input())
# a=2**n
# print(a)


#OOPS 
# def func(a,b):
#     return a+b 
# result =func(5,6)
# print(result) 

# class student:
#     def details(self,name,marks):
#         if marks>=40:
#             result="pass"
#             print( result)
#             print(name,marks)
#         else:
#             print("fail")
# s1=student()
# s2=student()
# s1.details("rvs",88)    


#syntax
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def show_result(self):
#         if self.marks>=40:
#             result="pass"
#         else:
#             result="fail"    
#         print("\ student name :",self.name)
#         print("marks",self.marks)
#         print("result",result)

# name=input("enter name ")
# marks=int(input("enter the marks"))
# s1=student(name,marks)
# s1.show_result()            

# class converter:
#     def __init__(self,c,f):
#         self.c=c
#         self.f=f
#     def result(self):
#         for c in (self):
#             f=c*(9/5)+32 
#             print(f)
c=int(input("enter value ="))
f=c*(9/5)+32 
print(f)