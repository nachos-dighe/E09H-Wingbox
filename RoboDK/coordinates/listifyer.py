data = open('wingbox_robodk_coordinates generator txt formatted.txt')
table = []


# Coordinates of the corner of table
x = 1000
y = 1000
z = 1000

# read table and get rid of fat
for line in data:
    row = line.split('\t')
    rowclean = []
    for item in row:
        item.strip('\t')
        if item == '':
            pass
        else:
            rowclean.append(item)      
    del rowclean[3]
    res = [float(i) for i in rowclean]
    res[0] += x
    res[1] += y
    res[2] += z
    table.append(res)

    

print(table)
