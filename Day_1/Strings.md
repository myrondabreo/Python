✅ DAY 1 DEEP DIVE: TEXTS (STRINGS) IN PYTHON
🔹 1. What is a String?
A string is a sequence of Unicode characters. In Python, it's enclosed by:

Single quotes 'Hello'

Double quotes "Hello"

Triple quotes for multiline strings '''Hello''' or """Hello"""


s1 = 'Python'
s2 = "is awesome"
s3 = '''This is 
a multiline 
string'''

🔹 2. String Indexing & Slicing
Strings are like lists of characters.

✅ Indexing
text = "Python"
print(text[0])   # P
print(text[-1])  # n (last character)

✅ Slicing
python
Copy
Edit
print(text[0:3])   # Pyt (from index 0 to 2)
print(text[::2])   # Pto (every second character)
print(text[::-1])  # nohtyP (reversed)

🔹 3. String Immutability
Strings are immutable — they can't be changed in place.


s = "hello"
# s[0] = "H"  ❌ Error!
s = "H" + s[1:]  # ✅ New string

🔹 4. Common String Methods
🔤 Case Methods:

text = "hello WORLD"
print(text.lower())     # hello world
print(text.upper())     # HELLO WORLD
print(text.title())     # Hello World
print(text.capitalize())  # Hello world
print(text.swapcase())    # HELLO world

📐 Alignment & Padding:

print("Hi".center(10, "-"))  # ---Hi-----
print("Hi".ljust(10, "*"))   # Hi********
print("Hi".rjust(10, "."))   # ........Hi

🔍 Search & Replace:

msg = "banana is yellow"
print(msg.count("a"))        # 3
print(msg.find("is"))        # 7
print(msg.replace("yellow", "green"))  # banana is green

🧼 Trimming:

s = "   hello   "
print(s.strip())     # 'hello'
print(s.lstrip())    # 'hello   '
print(s.rstrip())    # '   hello'

🔹 5. String Testing Methods

word = "Hello123"

print(word.isalpha())   # False (has numbers)
print("Hello".isalpha())  # True
print(word.isdigit())   # False
print("123".isdigit())  # True
print(word.isalnum())   # True
print("   ".isspace())  # True
print("Hello".isupper()) # False
print("HELLO".isupper()) # True

🔹 6. String Concatenation & Repetition

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)       # Hello World
print(s1 * 3)              # HelloHelloHello

🔹 7. Escape Sequences
Escape sequences start with \ and are interpreted specially:

Escape	Meaning
\n	Newline
\t	Tab
\\	Backslash
\'	Single quote
\"	Double quote

Example:


print("Line1\nLine2")
print("She said: \"Hi!\"")

🔹 8. Raw Strings
Raw strings ignore escape sequences:


print("C:\\new_folder\\test.txt")  # With escape
print(r"C:\new_folder\test.txt")   # Raw string

🔹 9. String Formatting
✅ f-strings (modern, preferred):

name = "Myron"
age = 24
print(f"My name is {name}, I’m {age} years old.")

✅ .format() method:

print("My name is {} and I’m {}.".format(name, age))

✅ % formatting (older, not recommended now):

print("My name is %s and I’m %d years old." % (name, age))

🔹 10. Multiline Strings
For long strings or docstrings:


paragraph = """This is a
multi-line string
with line breaks."""

🔹 11. String to List and Vice Versa

s = "apple,banana,grape"
lst = s.split(",")      # ['apple', 'banana', 'grape']
print(lst)

rejoined = "-".join(lst)
print(rejoined)         # apple-banana-grape

🔹 12. Encoding and Decoding
Python strings are Unicode. You can encode them:


s = "hello"
b = s.encode("utf-8")     # bytes
print(b)                  # b'hello'

print(b.decode("utf-8"))  # back to string

🔹 13. String Identity vs Equality

s1 = "hello"
s2 = "hello"
print(s1 == s2)      # True (same value)
print(s1 is s2)      # True in CPython for short strings

s3 = ''.join(['h', 'e', 'l', 'l', 'o'])
print(s3 == s1)      # True
print(s3 is s1)      # False (different object)


🧠 PRO TIP: String Performance
Use .join() instead of repeated + in loops.

# Bad:
result = ""
for word in ["hi", "there"]:
    result += word  # costly

# Good:
result = "".join(["hi", "there"])

