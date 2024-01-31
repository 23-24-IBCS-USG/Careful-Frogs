#Strings are text data. They are lists of characters.

myString = "Hello"

def p12(s):
        s = s.replace("@","")
        s = s.replace("!","")
        s = s.replace("%","")
        s = s.replace("&","")
        s = s.replace(" ","")
        return s

# one = is "set variable equal to value" two = is "check if two things are euqal"
def p11(s):
        r = s[::-1]
        if r == s:
                return True
        else:
                return False
                        
def p10(s):
        '''result = ""
        for char in s:
                result = char + result
                print(result)'''

def p10(s):
    s = s[::-1]
    print (s)

def p8(s1, s2):
    x = len(s1)
    y = len(s2)

    result = 0
    for i in range(x-y):
        s = ""
        for j in range(y):
            s = s + s1[i+j]

        if s == s2:
            result = result + 1
    return result
        
#only one character at a time
  



    
def p5again(s, n):                                                                      
    # substring from index n to the end of the string
    print(s[n::])
    
def p5(s, n):

    result = ""
    count = 0
    for char in s:
        if count >= n:
            
            result = result + char
        count = count + 1
    return result

def p4():
    s = input("Type a word")
    print(s)
    
    count = 0
    for char in s:
        if count % 2 == 1:
            print(char)
        count = count + 1

def main():
    p4()
    print (p5("Considine",3))
    print(p8("have a happy halloween","ha"))
    p5again("Yellow ties 2024",5)
    p10("computer")
    print(p11("eye"))
    print(p12("To@da!%y is a &good day"))
    
    
    
if __name__ == "__main__":
    main()
