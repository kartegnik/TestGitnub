def isPrime(n):
    if n==1: return False
    elif n<4: return True #2 and 3 are prime
    elif n%2==0: return False
    elif n<9: return True #we have already excluded 4,6 and 8.
    elif n%3==0: return False
    r=int(n**0.5) # n rounded to the greatest integer r so that r*r<=n
    f=5
    while f<=r:
        if n%f==0: return False
        if n%(f+2)==0: return False
        f=f+6
    return True