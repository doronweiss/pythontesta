data="""
1	checking init condition
2	moving pistons to home, opennig the gripper
3	Y homing procedure
4	X homing procedure
5	moving X in right direction to search for mechanical limit
6	stop moving X right while search for mechanical limit
7	gripper is moving to X position safe for Y
8	moving Y down direction to search for mechanical limit
9	stop moving Y right while search for mechanical limit
10	gripper is moving to home position - X and Y
11	testing the function of all pistons
12	checking item arm sensor and exit sensor
13	BIT sequence finished with success
14	gripper is moving to home position to open the gripper
15	gripper is moving up to enable moving pistons to HOME
101	checking init condition
102	moving pistons to home
103	moving gripper to cell
104	head of cell sequence finished with success
105	moving target piston to 'IN' while moving gripper to cell
106	moving target piston to 'IN' after gripper reached the head of cell
107	moving gripper down to search for item in cell
111	moving up to the head of cell
112	measure height sequence finished with success
113	moving gripper to home position, moving target piston to 'HOME'
114	opennig gripper to release the item
115	The item is seen by the sensor
116	gripper finish at the head of cell after arm sensor was missing
117	waiting xx ms befor closing the gripper
118	moving gripper down to cell delta
119	moving to cell with delta sequence finished with success
120	gripper is moving up to enable moving pistons to HOME
201	checking init condition
202	moving pistons to home
203	moving gripper to start scan position
204	moving piston to 'IN'
205	moving gripper to end scan position
206	moving piston to 'HOME'
207	csan shelf finished with protruding
208	csan shelf finished without protruding
301	checking init condition
302	moving pistons to home
303	moving gripper to start self study position
304	moving shelf piston to IN
305	moving Y to look for cell empty range and shelf actual position
306	The beginning of an empty cell sensor detection area is found
307	The end of an empty cell sensor detection area is found
308	The Item Arm sensor detection is found - shelf actual position
309	moving on X to find the start/end of cells positions
310	Finish study of DX200
311	moving gripper to start position of DX300 only(right side)
312	Finish study of DX300
"""

lines = data.split('\n')
print("Hello, world")
for line in lines:
    if len(line) == 0:
        continue
    line = line.replace(';', '')
    parts = line.split(maxsplit=1)
    if len(parts)>1 and parts[1]!="":
        print("{{{0}, \"{1}\"}},".format(parts[0], parts[1]))