word=input("enter a word")
char=input("enter the character to be searched")
i=0
count=0
while i<len(word):
    if word[i]==char:
        count=count+1
    i=i+1
print(f"the number of times {char} has occured is {count}")