

data="""
1	,can not start sequence - Bit not done
2	,can not start sequence - not at auto mode
3	,can not start sequence - not at manual mode
4	,X motor at error while machine not at any sequence 
5	,Y motor at error while machine not at any sequence 
6	,Sequence stoped because StopAll Command
7	,can not start sequence - EMO
8	,
9	,
100	,Piston time-out, can not move piston to home position
101	,Y motor at error while searching for home sensor
102	,Y homing time out
103	,X motor at error while searching for home sensor
104	,X homing time out
105	,X not moving while measuring X limit (check current limit)
106	,X motor at Time-Out while measuring X limits
107	,X 'stop on the limit' Time-Out (internal error)
108	,X and Y motors at error while moving to home position 
109	,X motor at error while moving to home position 
110	,Y motor at error while moving to home position 
111	,process of moving to home - time out
112	,
113	,
200	,cell data is not correct
201	,cell target does not exist
202	,loaded speed is zero
203	,Piston time-out - at prepare: fail to move pistons to home position
204	,X and Y motors at error while moving to cell target
205	,X motor at error while moving to cell target
206	,Y motor at error while moving to cell target
207	,time out error while moving to cell target
208	,Piston time-out - at getting the item: fail to move pistons to in position
209	,
210	,Y motors at error while moving to search for item
211	,time out error while moving to search for item
212	,
213	,Y motors at error while moving back to the head of the cell (after collecting an item)
214	,time out error while moving back to the head of the cell (after collecting an item)
215	,Y motors at error while moving back to the head of the cell (after not found an item)
216	,time out error while moving back to the head of the cell (after not found an item)
217	,piston time-out - after getting the item: fail to move pistons to home position
218	,X and Y motor at error while moving back to home
219	,X motor at error while moving back to home
220	,Y motor at error while moving back to home
221	,time out error while moving back to home
222	,The item was not seem by the item exit sensor
223	,The item is blocking the item exit sensor
224	,
225	,
300	,Y motors at error while moving to search for item
301	,time out error while moving to search for item
302	,reach low limit without arm sensor
303	,
304	,
400	,Y motors at error while moving to search for item
401	,time out error while moving to search for item
402	,
403	,
404	,
405	,
406	,
407	,
408	,
409	,
500	,X motors at error while moving relative X
501	,time out error while moving relative X
502	,can not start sequence - target is out of limits or crossing the obstacle
503	,
504	,
600	,Y motors at error while moving relative Y
601	,time out error while moving relative Y
602	,can not start sequence - target is out of limits or crossing the obstacle
603	,
604	,
700	,X and Y motors at error while moving to home
701	,X motor at error while moving to cell home
702	,Y motor at error while moving to cell home
703	,
704	,
"""

lines = data.split('\n')
print("Hello, world")
for line in lines:
    if len(line) == 0:
        continue
    line = line.replace(';', '')
    parts = line.split(',')
    if len(parts)>1 and parts[1]!="":
        print("new SysErrorDef () {{errorNum={0}, source=SysErrorSourceEnum.PLC, reportNum=null, description=\"{1}\"}},".format(parts[0], parts[1]))