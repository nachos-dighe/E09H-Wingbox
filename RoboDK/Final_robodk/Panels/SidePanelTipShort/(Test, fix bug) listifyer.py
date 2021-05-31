data = open('AE1222-2021-GROUP-E09H-CoordinatFile-SidePanelTipShort.txt')

# Coordinates of the corner of table
x = 1000
y = 1000
z = 1000


table = []
test = []

for line in data:
    row = line.split('\t')
    for i in range(8):
        del row[-1]
        
    try:   
        res = [float(i) for i in row]
    except:
        print(row)
        break
    
    res[0] += x
    res[1] += y
    res[2] += z
    table.append(res)

    
print(table)


