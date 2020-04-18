import re
S = input()

match = re.search(r'A[a-z][a-z]*C[a-z]*[a-z]', S)
if match == None:
    print("WA")
    exit()
if match.group() == S:
    print("AC")
else:
    print("WA")