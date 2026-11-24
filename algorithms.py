"""Модуль с реализацией базовых алгоритмов по блок-схемам."""


def reverse_number(n):
    """Возвращает целое число с цифрами в обратном порядке."""
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


def gcd(a, b):
    """Возвращает наибольший общий делитель чисел a и b."""
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

def fibonacci(n):
    """Функция вычисляет n-е число Фибоначчи для целого """
    if n==0:
        return 0
    prev=0
    curr=1
    i=1
    while i<n:
        nxt=prev+curr
        prev=curr
        curr = nxt
        i=i+1
    return curr

def max_increasing_len(arr):
    """Возвращает максимальную длину непрерывного строго возрастающего подотрезка в списке arr."""
    if len(arr)==0:
        return 0
    cur = 1
    best = 1
    i = 1
    while i<len(arr):
        if arr[i]>arr[i-1]:
            cur = cur + 1
            if cur > best:
                best = max(best, cur)
        else:
            cur = 1
        i=i+1
    return best

def sqrt_newton(n, eps=1e-6):
    """Вычисляет квадратный корень из числа n методом Ньютона с точностью eps."""
    if n==0:
        return 0.0
    else:
        x=n/2
    while abs(x * x - n) > eps:
        x=0.5*(x+n/x)
    return x

def second_max(arr):
    """Возвращает второй по величине уникальный элемент списка arr или None, если его нет."""
    if len(arr)<2:
        return None
    else:
        m1 = float('-inf')
        m2 = float('-inf')
        i = 0
        while i<len(arr):
            if arr[i]>m1:
                m2=m1
                m1=arr[i]
            elif m2<arr[i]<m1:
                m2=arr[i]
            i=i+1
        return m2

def count_primes_up_to(n):
    """Возвращает количество простых чисел в диапазоне от 2 до n включительно."""
    cnt = 0
    num = 2
    while num <= n:
        is_p = True
        d = 2
        while d * d <= num and is_p:
            if num % d == 0:
                is_p = False
            d = d + 1
        if is_p:
            cnt = cnt + 1
        num = num + 1
    return cnt
