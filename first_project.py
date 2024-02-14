
def getInfo():
    f = open("romeo.txt")

    s = f.read()
    print(s)


    s = s.split("***")
    s = s[2]
  
    print(s)

    chars = {"a":0,
             "b":0,
             "c":0,
             "d":0,
             "e":0,
             "f":0,
             "g":0,
             "h":0,
             "i":0,
             "j":0,
             "k":0,
             "l":0,
             "m":0,
             "n":0,
             "o":0,
             "p":0,
             "q":0,
             "r":0,
             "s":0,
             "t":0,
             "u":0,
             "v":0,
             "w":0,
             "x":0,
             "y":0,
             "z":0}

    listOfChars = chars.keys()

    for word in s:
        word = word.replace(",", "")
        word = word.replace("!", "")
        word = word.replace("?", "")
        word = word.replace("-", "")
        word = word.replace("_", "")
        word = word.replace(".", "")
        word = word.replace("；", "")
        word = word.replace("：", "")
        word = word.replace("（", "")
        word = word.replace("）", "")
        word = word.replace("【", "")
        word = word.replace("】", "")
        word = word.replace("‘", "")
        word = word.replace("“", "")
        word = word.replace("+", "")
        word = word.replace("/", "")
        word = word.replace("%", "")
        word = word.replace("~", "")
        word = word.replace("=", "")
        word = word.replace("@", "")
        word = word.replace("#", "")
        word = word.replace("$", "")
        word = word.replace("^", "")
        word = word.replace("0", "")
        word = word.replace("1", "")
        word = word.replace("2", "")
        word = word.replace("3", "")
        word = word.replace("4", "")
        word = word.replace("5", "")
        word = word.replace("6", "")
        word = word.replace("7", "")
        word = word.replace("8", "")
        word = word.replace("9", "")
        
  
        for c in word:
                c = c.lower()
                if c in listOfChars:
                     chars.update({c:chars.get(c) + 1})

    print(chars) 
            
    minC = ""
    maxC = ""
    minAmount = 99999
    maxAmount = 0

    for c in listOfChars:
        c = c.lower()
        v = chars.get(c)
        if v > maxAmount:
            maxAmount = v
            maxC = c
        if v < minAmount:
            minAmount = v
            minC = c

    return [minC, minAmount, maxC, maxAmount]

def average():
    f = open("romeo.txt")

    s = f.read()
    
    print(s)

    s = s.split("***")
    
    s = s[2]

    s = s.split()

    t_length = 0
    
    num_words = len(s)
  
    print(s)

    chars = {"a":0,
             "b":0,
             "c":0,
             "d":0,
             "e":0,
             "f":0,
             "g":0,
             "h":0,
             "i":0,
             "j":0,
             "k":0,
             "l":0,
             "m":0,
             "n":0,
             "o":0,
             "p":0,
             "q":0,
             "r":0,
             "s":0,
             "t":0,
             "u":0,
             "v":0,
             "w":0,
             "x":0,
             "y":0,
             "z":0}

    listOfChars = chars.keys()

    for word in s:
        word = word.replace(" ", "")
        word = word.replace(",", "")
        word = word.replace("!", "")
        word = word.replace("?", "")
        word = word.replace("-", "")
        word = word.replace("_", "")
        word = word.replace(".", "")
        word = word.replace("；", "")
        word = word.replace("：", "")
        word = word.replace("（", "")
        word = word.replace("）", "")
        word = word.replace("【", "")
        word = word.replace("】", "")
        word = word.replace("‘", "")
        word = word.replace("“", "")
        word = word.replace("+", "")
        word = word.replace("/", "")
        word = word.replace("%", "")
        word = word.replace("~", "")
        word = word.replace("=", "")
        word = word.replace("@", "")
        word = word.replace("#", "")
        word = word.replace("$", "")
        word = word.replace("^", "")
        word = word.replace("0", "")
        word = word.replace("1", "")
        word = word.replace("2", "")
        word = word.replace("3", "")
        word = word.replace("4", "")
        word = word.replace("5", "")
        word = word.replace("6", "")
        word = word.replace("7", "")
        word = word.replace("8", "")
        word = word.replace("9", "")
   
        
        t_length = t_length + len(word)

    avg_length = t_length / num_words

    avg_length = round(avg_length,2)

    return avg_length

    

def main():

    
    results = getInfo()
    print(" ---------- Calculating ----------- ")
    print("The minimum character used is " + results[0] + "," + str(results[1]) + " times")
    print("The maximum character used is " + results[2] + "," + str(results[3]) + " times")
    print("The average length of the words is", average())
    
 

if __name__ == "__main__":
        main()
           
