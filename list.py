#lists are a collection of data
# lists have an order to them

mylist = [45,20,10,"yellow",True]

print(mylist)

for item in mylist:
    print(item)
for i in range(len(mylist)):
    print(mylist[i])
#add item to a list

mylist.append("abby")
print(mylist)

mylist.insert(2,"vera")
print(mylist)

#remove intem from a list
mylist.pop()
print(mylist)

#remove at particualr index
mylist.pop(2)
print(mylist)

#remove specific elements
mylist.remove("yellow")
print(mylist)

#check to see if an item is in a list
if 45 in mylist:
    print(True)

else:
    print(False)

#example problems.
    #Give a list of integers, calculate the average

L = [34, 500, 101, 4, 7, 9, 25]
total = 0
for num in L:
    total = total + num

#one / includes remaining two / is integer
avg = total / len(L)
print(avg)

#Given a list of words, print the smallest and the largest word

S = ["Chicago","New York","Boston", "Beijing", "Tokyo","Hangzhou","Copenhagen"]

maxCity = 0
maxName = ""
minCity = 999
minName = ""

for city in S:
    if len(city) > maxCity:
        maxCity = len(city)
        maxName = city
    if len(city) < minCity:
        minCity = len(city)
        minName = city

print("The city with the longest name is: " + maxName)
print("The city with the shortest name is: "+ minName)

    

