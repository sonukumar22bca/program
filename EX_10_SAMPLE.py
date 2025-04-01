import re

print("\tProgram for String Handling and Regular Expressions")

# Email Validation
email = input("Enter your email id: ")
print("Valid email!" if re.match(r'\S+@\S+\.\S+', email) else "Invalid email!")

# String Handling & Regular Expressions
text = input("Enter Your String: ")
print("Split by spaces:", text.split())
key = input("Enter your search sub-string: ")
x=re.search(key,text)
print("Search Found!" if re.search(key, text) else "Not Found!")
print("search result:\n",x)
