## Bike Assembly and Production
#### A. There are 6 types of users. This includes the:
1. Production Manager - Person responsible for setting the target for the day based on the order, and checking the warehouse for final products.
2. Machine Assembly Manager - Person responsible for producing the frame and engine, and sending it to Engine assembly department.
3. Engine Assembly Manager - Person responsible for producing the bikeframe, and sending it to Painting assembly department.
4. Painting Shop Manager - Person responsible for painting the bikeframes, and sending it to the vehicle assembly department.
5. Vehicle Assembly Manager - Person responsible for producing bike, and sending it to the production warehouse.
6. Shop Manager -  Person responsible for sending out the requested orders.
   
#### B. The components in the warehouse of each of the departments are processed, assembled and sent to next detpartment.

![image](https://github.com/user-attachments/assets/549e90f7-4467-45a2-a6c2-57fad28039a3)

Conversing with NPCs to get information about the game features

![image](https://github.com/user-attachments/assets/5c661231-2d36-448a-87e4-648ad55d0f70)

Checking out the desk and computer to perform different operations

#### C. What to install?
1. Install python 3.5 or above to run the games.
2. Install Unity hub and necesary version of unity (as suggested by unity hub) to view the code.

#### D. How to use?
1. Enter to converse with the NPCs or computer.
2. Up and down, and left and right arrows to move.
3. Esc to come out of the option box or dialog box.
4. To understand the code check out the comments in the MachineAssembly folder.
   The code for rest of the departments are only sligntly different.

#### E. How to play?
1. Open all the Application .exe files of each department.
2. Change the demand in the Demand.txt file to the one you require.
3. Start with the production department and set the target.
4. Other departments can now see the target and begin assembly and production.
5. Other departments can even order from the store the components necessary based on the rule.
6. The store is responsible for sending out the ordered products.
7. Finally the production department is able to view the total bike produced.
8. Players can view the rules by pressing enter in the desk.
   
#### F. How to update or change?
1. The rules used for this the assembly are as follows:
# Engine           - 1xBattery + 5xWire + 2xPiston (Produced in machine assembly)
# Frame            - 1xUpperPlate + 1xBottomPlate (Produced in machine assembly)
# BikeFrame        - 1xEngine + 1xFrame (Produced in engine assembly)
# BikeFramePainted - 1xBikeFrame + 3xPaint (Produced in painted assembly)
# Bike             - 1xBikeFramePainted + 2xTyre + 10xScrew (Produced in vehicle assembly)
2. This rule can be changed by first changing the python code Manager.py, that states the above rule.
3. The next step is to change the warehouse files labelled from 1 to 5. For example - (item-0,1) means
   there are 0 item in warehouse and 1 of them is used to produce one product. If the second number is 0
   then it means that is the final product to be produced in the department.
4. The number assignment for warehouse is as follows:
   A. Machine Assembly department - Warehouse1.txt
   B. Engine Assembly department - Warehouse2.txT
   C. Painted Assembly department - Warehouse3.txt
   D. Vehicle Assembly department - Warehouse4.txt
   E. Production department - Warehouse5.txt
6. The next step is change the inventoryUI and orderUI gameobjects after opening each department games in unity and changing it to the new rule you want to change to.
