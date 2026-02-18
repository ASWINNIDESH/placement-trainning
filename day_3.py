# n=int(input("Enter the number="))
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     t=a+b
#     a=b
#     b=t




# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fib = fibonacci()

# for _ in range(8):
#     print(next(fib), end=" ")

# def fibonacci():
#     yield 0
#     yield 1
    
#     a, b = 0, 1
#     while True:
#         a, b = b, a + b
#         yield b
# fib = fibonacci()

# for _ in range(8):
#     print(next(fib), end=" ")

# list=[1,2,3,4,5]

# print(list[4])

#slicing
# print(list[1:3])
# print(list[0:])
# print(list[-5:-1])

#list operator
#concatemation(+) 
# a=[1,2,3]
# b=[4,5]
# print(a+b)

#reptition (*)
# num=[1,2]
# print(num*3)

#membership(in,not-in)
# f=["apple","banana","orange"]
# print("apple" in f)
# print("apple" not in f)
# print("grape" in f)

#comparsion 
# l1=[1,2,3]
# l2=[1,2,4]
# print(l1==l2)
# print(l1<l2)

# a=[1,2,3,4,5,6]
# b=[6,5,4,3,2,1]
# print(list[4])
# print(list[1:3])
# print(a+b)
# print(a*3)
# print("3" in a)
# print("5" not in a)
# print(a==b)
# print(a<b)

#list method
#append
# n=[1,2,3]
# n.append(4)
# print(n)

#insert
#syntax insert(index,item)
# n=[1,2,3,5]
# n.insert(3,4)
# print(n)

#extend 
# a=[1,2]
# b=[3,4]
# a.extend(b)
# print(a)

#remove
# a=[1,2,3,4]
# a.remove(3)
# print(a)

#pop
# a=[10,20,30,40]
# a.pop(2)
# print(a)

#clear
# a.clear()
# print(a)

# a=[1,5,3,4,2]
# print(a.index(2))
# print(a.count(2))
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.reverse()
# print(a)
#copy
# b=a.copy()
# print(b)

#map , filter 
# n=[1,2,3]
# r=list(map(lambda x:x*2,n))
# print(r)

# def function (x):
#     return x*2
# n=[1,2,3]
# r=list(map(function,n))
# print(r)

# n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# r=list(filter(lambda x:x%2==0,n))
# print(r)

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# def n(x):
#     return x%2==0
# r=list(filter(n,a))
# print(r)

#reduce
# from functools import reduce
# n=[1,2,3,4,5,6]
# r=reduce(lambda a,b:a*b,n)
# print(r) 

# n=[1,2,3,4,5,6,7,8,9,10]
# r=list(filter(lambda x:x%2==0,n))
# print(r)
# from functools import reduce
# h=reduce(lambda a,b:a+b,r)
# print(h)

# n=[1,2,3,4,5,6,7,8,9,10]
# r=list(filter(lambda x:x%2!=0,n))
# print(r)
# from functools import reduce
# h=reduce(lambda a,b:a+b,r)
# print(h)

# n=input("enter the value : ")
# if (n==n [::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")    

# n=input("enter the value : ")
# reversed_n = "".join(reversed(n))
# if (n==reversed_n):
#     print("palindrome")
# else:
#     print("not palindrome")    

# n=input("enter the value : ")
# rev=""
# for s in n :
#     rev=s+rev
# if (n==rev):
#     print("palindrome")
# else:
#     print("not palindrome")

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # Negative numbers are not palindrome
#         if x < 0:
#             return False
        
#         # Convert number to string and compare with its reverse
#         s = str(x)
#         return s == s[::-1]
# sol = Solution()
# print(sol.isPalindrome(121))   # True
# print(sol.isPalindrome(-121))  # False
# print(sol.isPalindrome(10))    # False


