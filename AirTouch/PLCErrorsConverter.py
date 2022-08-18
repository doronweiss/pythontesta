import sys

data="""
(general),0,No error,0
(search panel),3,no home,1
(search panel),3,no prepare,2
(search panel),1,Trolley didnt reach the target,3
(search panel),1,Error with approach motor when going to pre engage position,4
(search panel),-1,Column didnt start move on time,5
(search panel),-1,Column is above high limit for chosen row,6
(search panel),-1,Error with approach when going to fine tuning  position,7
(search panel),3,delta column is 0; probobly no column hight parmeter is enterd,8
(search panel),-1,Angle motor is out of limit,9
(search panel),-1,trolly err when going up to touch panel,10
(search panel),-1,one angle sensor is above high limit,11
(final attached),3,No home,12
(final attached),-1,Panel search didnt finish good,13
(final attached),-1,Approach is above high limit,14
(final attached),-1,only attached sens up is on,15
(final attached),-1,only attached sens down is on,16
(final attached),-1,error with aproach when trying to go to final position,17
(trolley),2,Did not find flag sensor after seconed try,18
(trolley),3,Tolley Target out of limit,19
(home),1,Error with Trolley motor in home,20
(home),1,Error with Angle motor in home,21
(home),1,Error with Approach motor in home,22
(home),1,Error with column motor in home,23
(prepare),1,Error with Approach motor in prepare,24
(prepare),1,Error with Angle motor in prepare,25
(prepare),1,Error with column motor in prepare,26
(final attached),1,error with approch when moving back if traker move,27
,1,EM Is Press,28
(final attached),1,both fixed are on,29
(final attached),1,column err when try to sit on panel,30
(final attached),1,Trolley err when try to sit on panel,31
(trolley),2,Did not find flag sensor after seconed try back,32
(final attached),-1,column high limit err,33
(search panel),1,approach motor error when trying to go back to fix angle if analog sensor touched the panel,34
(search panel),1,angle motor error when trying to fix after analog touch in first approach,35
(Disengage),1,column motor error in disengage,36
(Disengage),1,approach motor error in disengage,37
(search panel),2,Search panel time out,38
(final attached),2,Final attached time out,39
(prepare),1,Prepare time out,40
(trolley jump),1,trolly motor err,41
(Disengage),1,Angle motor err,42
(Disengage),1,disangage TO,43
(home),1,1 attached sensor is on during angle home,44
(home),1,1 attached sensor is on during approach home,45
(home),1,1 attached sensor is on during column home,46
(home),1,1 attached sensor is on during trolley home,47
(search panel),2,column motor error when trying to fix after analog touch in first approach,48
(search panel),2,Down limit is on,49
(search panel),2,Up limit is on,50
(search panel),2,to many angle fixed in first approach,51
(TBD),-1,angle error in drive pos,52
(TBD),-1,column error in drive pos,53
(TBD),-1,drive pos time out,54
,,,
(search panel),3,front analog sens is over resting value,100
(search panel),3,back analog sens is over resting value,101
(search panel),3,front attached sens is on,102
(search panel),3,back attached sens is on,103
(search panel),3,front fixed sens is on,104
(search panel),3,back analog fix sens is above flat position,105
,,,
(TBD),-1,wheel encoder sens stuck,110
(TBD),-1,wheel encoder sens slid,111
"""

lines = [ln for ln in data.split('\n') if len(ln)>0]
for line in lines:
    if len(line) == 0:
        continue
lines = [ln for ln in data.split('\n') if len(ln)>0]
for line in lines:
    if len(line) == 0:
        continue
    parts = line.split(',')
    if len(parts)!=4:
        print ("Parse error in line: {0}".format(line))
        sys.exit(0)
    print("{0}, {1}, {2}, {3} ".format(parts[3], parts[1], parts[2], parts[0]))
    maskName = parts[0].strip().strip(',')
