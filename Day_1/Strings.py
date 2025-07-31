#Q1] Count vowels and consonants in a string.

s='Rhiannon'
print(s[1])
print(s.lower())

for i in range(len(s)):
    if s[i]=='a':
        print(f"{s[i]} is a vowel")
    elif s[i]=='e':
        print(f"{s[i]} is a vowel")
    elif s[i]=='i':
        print(f"{s[i]} is a vowel")
    elif s[i]=='o':
        print(f"{s[i]} is a vowel")
    elif s[i]=='u':
        print(f"{s[i]} is a vowel")
    else:
        print(f"{s[i]} is a consonant")


#### OR
    
vowels='aeiou'

for char in s:
    if char.lower() in vowels:
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")


# Q2] Check if a string is a valid email.

email=input("Enter email:")

if email.startswith('@gmail.com'):
    print("invalid")
elif  email.endswith('@gmail.com'):
        print("valid")
else:
    print("invalid")
  




# Q3] Capitalize each word in a sentence.

cap=input("Enter sentence:")
print(cap.title())

# OR
print(' '.join(word.capitlize() for word in cap.split()))

#OR

cap=cap.split()
for word in cap:
    word=word.capitalize()
    print(''.join(word),end=' ')

# Q4] Remove punctuation from a sentence.

sentences=input("Enter Sentence:")
my_dict={}
for i in range(33,48):
    my_dict[i]=32 
print(sentences.translate(my_dict))

#OR Better version

import string

sentences=input("Enter Sentence:")
remove_punct=str.maketrans('','', string.punctuation)
clean_sent=sentences.translate(remove_punct)
print(clean_sent)


# Q5] Compress repeated characters: "aaabbbc" → "a3b3c1"


characters=input("Emter characters:")
character=characters.isalpha()
lenofchar=len(characters)
lst=[]
i=0

if character!=True:
    print("Only alphabets allowed")
else:
    while i<lenofchar:
        count=1
        while i+1<lenofchar and characters[i]==characters[i+1]:
            count +=1
            i +=1
        lst.append(characters[i]+str(count))
        i+=1
print(''.join(lst))


                 
                      
                 
            
                      
                 
                 

