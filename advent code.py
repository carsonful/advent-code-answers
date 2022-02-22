import keys
import csv

lst =[]
with open('data.csv','w+',newline ='') as f:

    writer = csv.writer(f)
    try:
        for i in range(len(keys.depths)):
            x = keys.depths[i] +keys.depths[i+1]+keys.depths[i+2]
            lst.append(x)
    except IndexError:
        pass
    writer.writerows(map(lambda x: [x], lst))



    
''''''