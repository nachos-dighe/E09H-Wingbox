from robolink import *   
from robodk import *  

data = open('AE1222-2021-GROUP-E09H-CoordinateFile-SidePanelRootShort.txt')






# read table and get rid of fat
x = 1000
y = 1000
z = 1000


table = []
test = []

for line in data:
    row = line.split('\t')
    for i in range(8):
        del row[-1]
    res = [float(i) for i in row]
    res[0] += x
    res[1] += y
    res[2] += z
    table.append(res)
print(table)




RDK = Robolink()


RDK.Render(False) 


list_items = RDK.ItemList() 
for item in list_items:
    if item.Name().startswith('Auto'):
        item.Delete()


robot = RDK.ItemUserPick('Select a robot', ITEM_TYPE_ROBOT)


RDK.Render(True) 


if not robot.Valid():
    quit()


reference = robot.Parent()


robot.setPoseFrame(reference)


pose_ref = robot.Pose()
print(Pose_2_TxyzRxyz(pose_ref))





for i in range(len(table)):
    
    pose_i = pose_ref
    pose_i.setPos(table[i])
    
    
    robot.MoveL(pose_i)
    

quit()
