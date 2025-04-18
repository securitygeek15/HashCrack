import hashlib
target = "4dcc4173d80a2817206e196a38f0dbf7850188ff"

with open(f'rocku.txt','r') as f:
         content = f.readlines()  
         
for line in content:
    if hashlib.sha1(line.strip().encode()).hexdigest() == target:
        print("Match found:", line.strip())
        break
else:
    print("ERROR")
