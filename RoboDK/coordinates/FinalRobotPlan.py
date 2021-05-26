from robolink import *   
from robodk import *  

data = open('C:/Users/damia/OneDrive/Documents/GitHub/E09H-Wingbox/RoboDK/coordinates/coordinates txt files/panels/AE1222-2021-GROUP-E09H-CoordinateFile-PanelRootTop.txt')
POINTS = []




# read table and get rid of fat
x = 0
y = 0
z = 0


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





print(POINTS)
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

'''
RDK.AddFrame("Frame")
RDK.setPose(transl(100,200,300) * rotz(pi/2))
'''
reference = robot.Parent()


robot.setPoseFrame(reference)


pose_ref = robot.Pose()
print(Pose_2_TxyzRxyz(pose_ref))





for i in range(len(POINTS)):
    
    pose_i = pose_ref
    pose_i.setPos(POINTS[i])
    
    
    robot.MoveJ(pose_i)
    

quit()
