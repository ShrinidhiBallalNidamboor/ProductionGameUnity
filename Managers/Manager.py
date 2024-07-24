from Define import command
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
        command(0,1,[['Engine',['Battery','Wire','Piston']],['Frame',['UpperPlate','BottomPlate']]],order,commandinput)
    elif user==2:
        command(1,2,[['BikeFrame',['Engine','Frame']]],order,commandinput)
    elif user==3:
        command(2,3,[['BikeFramePainted',['Paint','BikeFrame']]],order,commandinput)
    else:
        command(3,4,[['Bike',['Tyre','Screw','BikeFramePainted']]],order,commandinput)


