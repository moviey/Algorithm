str = input()
test = ""
for i in str:
    if i.isupper() :
        test += i.lower()
    else :
        test += i.upper()
print(test)