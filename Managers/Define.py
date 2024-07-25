import time
filepath=[]
filepath.append('../Database/Messenger/Manager1.txt')
filepath.append('../Database/Messenger/Manager2.txt')
filepath.append('../Database/Messenger/Manager3.txt')
filepath.append('../Database/Messenger/Manager4.txt')
filepath.append('../Database/Messenger/Manager5.txt')
filepath.append('../Database/Messenger/Manager6.txt')

filepath.append('../Database/RuleSet.txt')
filepath.append('../Database/Demand.txt')

filepath.append('../Database/Warehouse/Warehouse1.txt')
filepath.append('../Database/Warehouse/Warehouse2.txt')
filepath.append('../Database/Warehouse/Warehouse3.txt')
filepath.append('../Database/Warehouse/Warehouse4.txt')
filepath.append('../Database/Warehouse/Warehouse5.txt')

def warehouse(i, component):
    print(i+8)
    print(filepath[i+8])
    with open(filepath[i+8], 'r') as file:
        data=file.read()
        data=data.split('\n')
        for j in data:
            a, b=j.split('-')
            b=b.split(',')
            if a==component:
                return [int(b[0]), int(b[1])]
    return None

def storewarehouse(i, component, value):
    array=[]
    with open(filepath[i+8], 'r') as file:
        data=file.read()
        data=data.split('\n')
        for j in data:
            a,b=j.split('-')
            b=b.split(',')
            if a==component:
                array.append(a+'-'+str(value)+','+b[1])
            else:
                array.append(j)
        with open(filepath[i+8], 'w') as file:
            file.write('\n'.join(array))
    return None

def notify(message, list):
    for i in list:
        with open(filepath[i], 'r') as file:
            value=file.read()
        with open(filepath[i], 'w') as file:
            if value=='':
                file.write(message)
            else:
                file.write(value+'\n'+message)

def createmessenger():
    for i in range(6):
        with open(filepath[i], 'w') as file:
            file.write('')

def readfile(filepath):
    with open(filepath, 'r') as file:
        data=file.read()
        return data

def sendgoods(msg, to, components):
    notify(msg, [to])
    for i in components:
        value=warehouse(to,i[0])[0]+i[1]
        storewarehouse(to,i[0],value)

# 1. Order Products from shop
# 2. Send finished products
# 3. Assemble or paint
def command(i,next,list,order,commandinput):
    if commandinput==1:
        notify(order+'-'+str(i), [4])
    elif commandinput==2:
        val=[]
        for j in list:
            val.append([j[0],warehouse(i,j[0])[0]])
        for j in list:
            storewarehouse(i,j[0],0)
        time.sleep(10)
        sendgoods('Ordered Goods delivered', next, val)
    elif commandinput==3:
        val=[]
        for j in list:
            minimum=[]
            for k in j[1]:
                minimum.append(warehouse(i,k)[0]//warehouse(i,k)[1])
            minimum=min(minimum)
            for k in j[1]:
                storewarehouse(i,k,warehouse(i,k)[0]-minimum*warehouse(i,k)[1])
            val.append([j[0],warehouse(i,j[0])[0]+minimum])
        for j in val:
            storewarehouse(i,j[0],j[1])