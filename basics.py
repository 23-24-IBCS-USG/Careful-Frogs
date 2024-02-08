
def p1(w,s):
    return s[:2] + w + s[2:]

def p2(str):
    mylist = ["H","e","l","l","o"]
    mylist.remove("l")
    mylist.remove("l")
    mylist.remove("o")
    return mylist

def p3(a, b):
    if len(a) < len(b):
        short, long = a, b
    else:
        short, long = b, a
    
    return short + long + short

def p4(str):
    mylist = ["H","e","l","l","o"]
    mylist.remove("H")
    mylist.remove("o")
    return mylist

def p5(speed,birthday):
    if birthday:
        speed = speed - 5
    if speed <= 60:
        return 0  
    if speed <= 80:
        return 1  
    else:
        return 2
def p6(a,b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

#left2
def p7(str):
    return str[2:] + str[:2]


    
def main():
    print(p2(["Hello"]))
    print(p1("Yay", "<<>>"))
    print(p3("hello","hi"))
    print(p4(["Hello"]))
    print(p5(65,False))
    print(p6(1, 5))
    print(p7("java"))


if __name__ == "__main__":
    main()
