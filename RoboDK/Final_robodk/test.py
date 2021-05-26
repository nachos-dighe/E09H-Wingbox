data = open("wingbox_robodk_coordinates generator txt formatted.txt")
POINTS = []

for line in data:
    row = line.replace('\\n','')
    row = line.replace('\t',' ')
    POINTS.append(row)

print(POINTS)
