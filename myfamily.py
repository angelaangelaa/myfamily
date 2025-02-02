myfamily = ("mother", "father", "sister", "brother", "sister") 

print(myfamily)

print(type(myfamily))  # Output: <class 'tuple'>

print(myfamily[2])

try:
    myfamily.append("me")  #it's not working
except AttributeError as e:
    print("Error:", e)

try:
    myfamily.pop()  #also not working
except AttributeError as e:
    print("Error:", e)

