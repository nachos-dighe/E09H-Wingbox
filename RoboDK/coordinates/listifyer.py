data = open('wingbox_robodk_panel_root_top_coordinates generator txt v3.txt')

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


