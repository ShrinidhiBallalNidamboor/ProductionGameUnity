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
    # Machine Assembly Manager
    if user==1:
        commandManager(0,1,[['Engine',['Battery','Wire','Piston']],['Frame',['UpperPlate','BottomPlate']]],order,commandinput)
    # Engine Assembly Manager
    elif user==2:
        commandManager(1,2,[['BikeFrame',['Engine','Frame']]],order,commandinput)
    # Painted Assembly Manager
    elif user==3:
        commandManager(2,3,[['BikeFramePainted',['Paint','BikeFrame']]],order,commandinput)
    # Vehicle Assembly Manager
    elif user==4:
        commandManager(3,4,[['Bike',['Tyre','Screw','BikeFramePainted']]],order,commandinput)
    # Store Manager
    elif user==5:
        storeManager(order)
    # Initialising files
    elif user==6:
        createmessenger()
    # Production Manager
    else:
        setTarget(order)




