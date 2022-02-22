import addednums


newlst = addednums.added

count = 0

for i in range(len(newlst)):
    if newlst[i + 1] == newlst[-1]:
        if newlst[i] < newlst[i+1]:
            count+=1
            print(count)
            break
    elif newlst[i] < newlst[i+1]:
        count += 1
    else:
        pass
print(count)