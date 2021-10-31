#Read a text file and display the number of vowels/consonants/uppercase/lowercase
#characters in the file
file1=open('testfile.txt','r')
var1=file1.read()
vcount=0
concount=0
uppercount=0
lowercount=0
for word in var1:
    if word in ['a','e','i','o','u','A','E','I','O','U']:
        vcount+=1
    elif word.isalpha():
        concount+=1
for word in var1:
    if word.isupper():
        uppercount+=1
    if word.islower():
        lowercount+=1
print('Number of vowels:',vcount)
print('Number of consonants:',concount)
print('Number of lowercase characters:',lowercount)
print('Number of uppercase characters:',uppercount)
        
