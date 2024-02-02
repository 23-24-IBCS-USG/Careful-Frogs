def p1(S):
    
    for i in range(len(S) - 1):
        if S[i] == 7:
            if S[i+1]== 7:
                return True
    return False


def p2(S):
    primes = [2, 3, 5, 7, 11]
    result = 0

    for num in S:
        if num in primes and S.index(num) <= 4:
            break 
        result += num

    return result

def p3(S):

    total = 0
    N = False

    for num in S:
        if num == 2:
            N = True
        elif num == 3:
            N = False
        elif not ex:
            total = total + num

    return total

def main():
    print(p1([1,2,3,7,7]))
    print(p2([1,4,2,3,6]))
    print(p3([1,4,4]))
    
if __name__ == "__main__":
    main()

    
