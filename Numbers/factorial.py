"""
Enter a number N and the program will print N!
"""

def factorial(n):
    """
    Returns n!
    """
    if(n == 0):
        return 1;
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    n = int(raw_input())

    print factorial(n)