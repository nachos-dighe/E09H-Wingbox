from robolink import *   
from robodk import *  

data = open('wingbox_robodk_panel_root_top_coordinates generator txt v3')
POINTS = []




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
    POINTS.append(res)





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
