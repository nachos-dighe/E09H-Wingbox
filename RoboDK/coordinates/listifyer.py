data = open('C:/Users/damia/OneDrive/Documents/GitHub/E09H-Wingbox/RoboDK/coordinates/coordinates txt files/panels/AE1222-2021-GROUP-E09H-CoordinateFile-PanelRootTop.txt')

# Coordinates of the corner of table
x = 1000
y = 1000
z = 1000


table = []
test = []

for line in data:
    row = line.split('\t')
    for i in range(7):
        del row[-1]
    res = [float(i) for i in row]
    res[0] += x
    res[1] += y
    res[2] += z
    table.append(res)



    
print(table)


