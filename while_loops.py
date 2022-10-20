#loops that continue to run until the condition becomes false

c = 0
while c < 5:
    print(c)
    c = c + 1
    
c = 0
while c < 5:
    print(c)
    if c == 3:
        break
    c = c + 1
    
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        continue
    print(c)
    
    
c = 0
while c <5:
    c = c + 1
    if c == 3:
        pass
    print(c)