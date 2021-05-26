P_start = [0, 0, 0]
P_End = [0, 0, 0]

NUM_POINTS = 10

def MakePoints(xStart, xEnd, numPoints):
    if len(xStart) != 3 or len(xEnd) != 3:
        raise Exception("Start and end point must be 3-dimensional vectors")
    if numpoints < 2:
        raise Exception("at least two points are required")
    pt_list = []
    x = xStart[0]
    y = xStart[1]
    z = xStart[2]

    x_steps = (xEnd[0] - xStart[0])/(numPoints-1)
    y_steps = (xEnd[1] - xStart[1])/(numPoints-1)
    z_steps = (xEnd[2] - xStart[2])/(numPoints-1)

    for i in range(numPoints):
        point_i = [x, y, z]
        pt_list.append(point_i)
        x = x + x_steps
        y = y + y_steps
        z = z + z_steps
        return pt_list

from robolink import *
from robodk import *

POINTS = MakePoints(P_Start, P_END, NUM_POINTS)

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

reference = robot.Parent() #change here to change reference frame

robot.setPoseFrame(reference)

pose_ref = robot.Pose()

print(Pose_2_TxyzRxyz(pose_ref))

RDK.Render(False)
prog = RDK.AddProgram('AutoProgram')

for i in range(NUM_POINTS):
    ti = RDK.AddTarget('Auto Target %i' % (i+1))
    pose_i = pose_ref
    pose_i.setPos(POINTS[i])
    ti.setPose(pose_i)
    ti.setAsCartesianTarget()
    prog.MoveL(ti)

RDK.Render(True)

prog.RunProgram()
quit()
