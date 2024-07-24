from Define import readfile
from Define import notify
from Define import createmessenger
from Define import warehouse
from Define import filepath

try:
    print(readfile(filepath[7]))
    createmessenger()
    print('Bikes in warehouse is '+str(warehouse(4,'Bike')[0]))
    target=input('Enter the target: ')
    notify('Target for the day is '+target, [0, 1, 2, 3]) 
    print('Target was successfully broadcasted')
    while True:
        commandinput=input('Check the Bike output(Y/N): ')
        if commandinput=='Y':
            print('Bike output: ', warehouse(4,'Bike')[0])
        else:
            break
except:
    print('An error occurred during the processing of the orders')