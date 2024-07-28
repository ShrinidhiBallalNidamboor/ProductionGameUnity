from Define import commandManager
from Define import storeManager
from Define import createmessenger
from Define import setTarget
import sys

# 1. Machine Manager
# 2. Engine Assembly Manager
# 3. Painting Assembly Manager
# 4. Vehicle Assembly Manager

if __name__ == "__main__":
    
    user = int(sys.argv[1])
    order = sys.argv[2]
    commandinput = int(sys.argv[3])
    if user==1:
        commandManager(0,1,[['Engine',['Battery','Wire','Piston']],['Frame',['UpperPlate','BottomPlate']]],order,commandinput)
    elif user==2:
        commandManager(1,2,[['BikeFrame',['Engine','Frame']]],order,commandinput)
    elif user==3:
        commandManager(2,3,[['BikeFramePainted',['Paint','BikeFrame']]],order,commandinput)
    elif user==4:
        commandManager(3,4,[['Bike',['Tyre','Screw','BikeFramePainted']]],order,commandinput)
    elif user==5:
        storeManager(order)
    elif user==6:
        createmessenger()
    else:
        setTarget(order)




