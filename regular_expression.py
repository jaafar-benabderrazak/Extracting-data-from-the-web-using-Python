#find()
for line in hand:
    line = line.rstrip()
    if line.find("From:") >= 0 :
        print(line)
        
#re.search()  
import re
for line in hand:
    line = line.rstrip()
    if re.search("From:",line):
        print(line)
        
#startswith() 
for line in hand:
    line = line.rstrip()
    if line.startswith("From:") >= 0 :
        print(line)

#re.findall()
sentence = "my 2 favorite numbers are 3 and 71"
numbers = re.findall("[0-9]+",sentence)
print(numbers)
