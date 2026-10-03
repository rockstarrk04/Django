from django.http import HttpResponse


def even_or_odd(request):
    num = 101

    if num % 2 == 0:
        return HttpResponse("Even Number")
    else:
        return HttpResponse("Odd Number")


def palindrome(request):
    num = 121

    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return HttpResponse("Palindrome")
    else:
        return HttpResponse("Not a Palindrome")


def prime_number(request):
    num = 7

    if num <= 1:
        return HttpResponse("Not a Prime Number")

    for i in range(2, num):
        if num % i == 0:
            return HttpResponse("Not a Prime Number")

    return HttpResponse("Prime Number")

def check_number(request):
    num = -19

    if num > 0:
        return HttpResponse("Positive")
    elif num < 0:
        return HttpResponse("Negative")
    else:
        return HttpResponse("Zero")


def factorial(request):
    num = 5

    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return HttpResponse(fact)


def sum_of_digits(request):
    num = 12345

    total = 0   

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return HttpResponse(total)