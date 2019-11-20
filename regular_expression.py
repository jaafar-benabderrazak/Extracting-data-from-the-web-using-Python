line = "Regular expressions are a very specialized language that allow us to succinctly search strings and extract data from strings."

#re.search()
#This method takes a regular expression pattern and a string and searches for that pattern within the string. 
print(re.search("data",line))
        
#find()
#This method determines if string str occurs in string, or in a substring of string if starting index beg and ending index end are given.
print(line.find("data"))
        
#startswith() 
#This method returns true if found matching string otherwise false.
print(line.startswith("data"))

#re.findall()
#findall() is probably the single most powerful function in the re module. 
#Above we used re.search() to find the first match for a pattern. 
#findall() finds *all* the matches and returns them as a list of strings, with each string representing one match.
sentence = "my 2 favorite numbers are 3 and 71"
numbers = re.findall("[0-9]+",sentence)
print(numbers)
