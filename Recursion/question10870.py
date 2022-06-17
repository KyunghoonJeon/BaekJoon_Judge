n=int(input())

def fibo_recursion(n):
    if n<=1:
        return n
    return fibo_recursion(n-1)+fibo_recursion(n-2)

print(fibo_recursion(n))