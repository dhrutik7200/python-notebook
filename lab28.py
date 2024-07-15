i = 0
a = [1,2,3,4,5,6]

while i < len(a):
    if a[i] == 5 or a[i] == 3:
        i += 1
        continue
    print('Current Letter:',a[i])
    i+=1
    

             