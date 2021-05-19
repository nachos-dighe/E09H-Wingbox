data = open('wingbox_robodk_coordinates generator txt formatted.txt')
table = []


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
    table.append(res)

    

print(table)
