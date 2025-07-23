# def Find_sum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum

# if __name__=='__main__':
#     print(Find_sum(5))

# def Find_sum(n):
#     if n==1:
#         return 1
#     return n+Find_sum(n-1)

# if __name__=='__main__':
#     print(Find_sum(1))


# def Fib(n): # 0,1,1,2,3,5,8,13
#     if n==0 or n==1:
#         return n
#     return Fib(n-1)+Fib(n-2)

# if __name__=='__main__':
#     print(Fib(5))



# def print_name(i,n):    #TC=O(n)  #SC=O(n)
#     if i>n:
#         return
#     print("Pranav")
#     print_name(i+1,n)
    
# if __name__=='__main__':
#      (print_name(1,5)

# def num(i,n):
#     if i>n:
#         return
#     print(i,end=" ")
#     num(i+1,n)
    
# if __name__=='__main__':
#       (num(1,10)


# def num(i, n):
#     if i < n:
#         return
#     print(i, end=" ")
#     num(i - 1, n)

# if __name__ == '__main__':
#     num(10, 1)


# def num(i,n):
#     if i<1:
#         return
#     num(i-1,n)
#     print(i,end=" ")
    
    
# if __name__=='__main__':
#       num(10,10)



# def num(n,i): #parametarised recursion
#     if n<i:
#         return
#     num(n,i+1)
#     print(i,end=" ")
    
    
# if __name__=='__main__':
#       num(10,1)


# def num(n):
#     if(n==0):
#         return 0
#     return n+num(n-1)

# if __name__=='__main__':
#     print(num(3))

# def fact(n):
#     if(n==0):
#         return 1
#     return n*fact(n-1)
# if __name__=='__main__':
#     print(fact(5))

            
# def rev(a, l, r):
#     if l >= r:
#         return
#     a[l], a[r] = a[r], a[l]  # Swap elements
#     rev(a, l + 1, r - 1)

# if __name__ == '__main__':
#     a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     rev(a, 0, len(a) - 1)
#     print("Reversed list:", a)



#using one pointer
# def func(i):
#     if(i>=n/2):
#         return
#     a[i],a[n-i-1]=a[n-i-1],a[i]
#     func(i+1)
    
# if __name__ == '__main__':
#     a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#     n=len(a)
#     func(0)
#     print("Reversed list:", a)


#palindrom
def func(i):
    if i >= n // 2:
        return True
    elif s[i] != s[n - i - 1]:
        return False
    return func(i + 1)

if __name__ == '__main__':
    s = 'MADAM'
    n = len(s)
    result = func(0)
    print(result)

    