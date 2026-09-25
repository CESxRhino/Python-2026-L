# ex1
# import math as np
# radius = int(input())
# a = np.pi
# area = radius*radius*a
# print(area)
# ex2
# tempC = float(input())
# tempF = tempC * 1.8 + 32
# print(tempF)
# ex3
# n = 1000000
# Prime = [True for _ in range(n + 1)]
# def init():
#     Prime[0] = False
#     Prime[1] = False
#     for i in range(2,n):
#         if Prime[i]:
#             for j in range(i * i,n + 1,i):
#                 Prime[j] = False 
# init()
# Num = int(input())
# for i in range(1,Num + 1):
#     if(Prime[i] == True):
#         print(i)

# if check(Num):
#     print("YES\n")
# else:
#     print("NO\n")
# ex4
# def check(num):
#     sum = 0
#     for i in range(1,num):
#         if(num % i == 0):
#             sum = sum + i
#     if sum == num:
#         return True
#     else:
#         return False
# Num = int(input())
# if check(Num):
#     print("Yes")
# else:
#     print("No")
# ex5
# Color = ["RED","YELLOW","BLUE","WHITE"]
# color = input()
# if color in Color:
#     print("Yes")
# else:
#     print("No")
# ex6
# range1 = list(range(0,7))
# range2 = list(range(1,11,3))
# range3 = list(range(5,0,-1))
# range4 = list(range(6,-3,-2))
# print(range1,"\n")
# print(range2,"\n")
# print(range3,"\n")
# print(range4,"\n")
# #ex7
# def remove_dollar_sign(s):
#     return s.replace("$","")
# s = input()
# s1 = remove_dollar_sign(s)
# print(s1)
# #ex8
# def extrac_even(l):
#     even_numbers = []
#     for x in l:
#         if x % 2 == 0:
#             even_numbers.append(x)
#     return even_numbers
# a = [1, 4, 5,-1, 10]
# a = extrac_even(a)
# print(a)
# ex9
# def fac(a):
#     n = 1
#     if a == 0:
#         return 1
#     for i in range(1,a + 1):
#         n = n * i
#     return n
# a = int(input())
# print(fac(a))
# ex10
# def div(a):
#     divs = []
#     for i in range(1,a):
#         if a % i == 0:
#             divs.append(i)
#     return divs
# a = int(input())
# lists = div(a)
# # lists = div(a)
# lists.append(a)
# print(lists)
# ex11
# class Pointer:
# x1 = float(input())
# x2 = float(input())
# y1 = float(input())
# y2 = float(input())
# point1 = (x1,x2)
# point2 = (y1,y2)
# print(np.dist(point1,point2))
# ex12
# def rec(m,n):
#     for i in range(m):
#         if i == 0 or i == m - 1:
#             print("* " * n)
#         else:
#             if n > 1:
#                 print("* " + "  " * (n - 2) + "*")
#             else:
#                 print("*")
# m = int(input())
# n = int(input())
# rec(m,n)
