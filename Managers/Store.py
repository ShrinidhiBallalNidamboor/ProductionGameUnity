from Define import readfile
from Define import sendgoods
from Define import filepath
import time

print(readfile(filepath[6]))
while True:
    print('Send items: ')
    commandinput=input('Enter the command(Y/N): ')
    if commandinput=='Y':
        data=readfile(filepath[5])
        data=data.split('\n')
        if data==['']:
            continue
        data=data[-1]
        a,b=data.split('-')
        array=a.split(',')
        components=[]
        length=len(array)
        result=readfile(filepath[int(b)+8]).split('\n')
        for i in range(length):
            components.append([result[i].split('-')[0], int(array[i])])
        time.sleep(10)
        sendgoods('Orders Delivered', int(b), components)
    else:
        break