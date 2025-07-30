#Q1] Count vowels and consonants in a string.

# s='Rhiannon'
# print(s[1])
# print(s.lower())

# for i in range(len(s)):
#     if s[i]=='a':
#         print(f"{s[i]} is a vowel")
#     elif s[i]=='e':
#         print(f"{s[i]} is a vowel")
#     elif s[i]=='i':
#         print(f"{s[i]} is a vowel")
#     elif s[i]=='o':
#         print(f"{s[i]} is a vowel")
#     elif s[i]=='u':
#         print(f"{s[i]} is a vowel")
#     else:
#         print(f"{s[i]} is a consonant")


#### OR
    
# vowels='aeiou'

# for char in s:
#     if char.lower() in vowels:
#         print(f"{char} is a vowel")
#     else:
#         print(f"{char} is a consonant")


# Q2] Check if a string is a valid email.

# email=input("Enter email:")

# if email.startswith('@gmail.com'):
#     print("invalid")
# elif  email.endswith('@gmail.com'):
#         print("valid")
# else:
#     print("invalid")
  




# Q3] Capitalize each word in a sentence.

# cap=input("Enter sentence:")
# print(cap.title())

# OR
# print(' '.join(word.capitlize() for word in cap.split()))

#OR

# cap=cap.split()
# for word in cap:
#     word=word.capitalize()
#     print(''.join(word),end=' ')

# Q4] Remove punctuation from a sentence.

# sentences=input("Enter Sentence:")
# my_dict={}
# for i in range(33,48):
#     my_dict[i]=32 
# print(sentences.translate(my_dict))

#Better version

# import string

# sentences=input("Enter Sentence:")
# remove_punct=str.maketrans('','', string.punctuation)
# clean_sent=sentences.translate(remove_punct)
# print(clean_sent)


# Q5] Compress repeated characters: "aaabbbc" → "a3b3c1"


characters=input("Emter characters:")
character=characters.isalpha()
lenofchar=len(characters)-1
lst=[]

if character!=True:
    print("Only alphabets allowed")
else:
    for char in characters:
        lst +=char
   
    for index in range(lenofchar):
        count=0
        if lst[index]==lst[index+1]:
            count+=1
            if count>1:
                print(count,lst[index],end=',')
            else:
                print(lst[index])

    # for index in range(lenofchar):
    #     count=0
    #     if characters[index]==characters[index+1]:
    #         count+=1
    #         newstr=count
    # print(newstr,characters)

                 
                      
                 
            
                      
                 
                 

