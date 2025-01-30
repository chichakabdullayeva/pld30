#!/usr/bin/python3
text = str(input())
text = text.lower()
text = text.replace("!"," ")
text = text.replace(".","")
count = 0
text = text.split()
print (text)
for i in text:
    for k in text:
        if i == k:
            count = count+1
    print (i,count)
    count = 0
