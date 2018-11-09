#-*- coding: utf-8 -*-

from LE__SDK__ import * 

print ' ' 
print '#####################################################'
print '## LaserEye (STUD LIDAR Prototype IV) Program      ##'
print '##  * LE_cmd (2018/06/28)                          ##'
print_SDK_VER()
print '##  * designed and programmed by STUD LIDAR Team.  ##'
print '##  * Copyright 2018 ETRI. All rights reserved.    ##'
print '#####################################################'

# V2.1, 180627
#   - 라이브러리 형태로 변경 
# V2.2, 180628 
#   - 전송 명령 및 수신 데이터 출력하도록 변경 


import sys

print''  
print'Input:'        
if len(sys.argv)==3:
    cmd_ID=int(sys.argv[1])
    cmd_Par=int(sys.argv[2])
    print '   *Command ID = %d(%4X) in int16 parameter mode'%(cmd_ID,cmd_ID)
    print '   *Command Parameters =', cmd_Par
elif len(sys.argv)>3:
    cmd_ID=int(sys.argv[1])
    cmd_Par=map(int,sys.argv[2:])
    print '   *Command ID = %d(%4X) in int16 array parameter mode'%(cmd_ID,cmd_ID)
    print '   *Command Parameters =', cmd_Par
else:
    err_exit("   *LE_cmd [commandID) [commandParameter]") 
    
print''
print'Output:'        
sock1=LE_UDP_open()
result=LE_UDP_prompt(sock1, cmd_ID, cmd_Par) # LE_command with cmdID and cmdPar 
print "   *Reponse (%d bytes)"%(len(result)),'.'.join('{:02X}'.format(x) for x in bytearray(result))
print''  

LE_UDP_close(sock1)




