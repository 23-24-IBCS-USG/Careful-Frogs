
def p1(x,y):
    if x*y < 200:
        return x*y
    else:
        return x+y

def main():
    print(p1(6,8))
    p2(5)
    p3(5)


def p2(n):
    for i in range(n + 1):
     print(i)

   
    
    
def p3(n):
    for i in range(n + 1):
        current_sum = i * (i - 1)
        print(current_sum)

    


myString = "Hello"
def p4():
    s = input()
    print(s)
    count = 0
    for char in s:
        if count % 2 == 1:
            print(char)
        count = count + 1
    

if __name__ == "__main__":
    main()
