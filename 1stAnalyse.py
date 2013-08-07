# Filename: 1stAnalyse.py
###########################################################
#This pyFile is used to divide the address by time        #
#You can chan the time by change the variable 'decidetime'#
###########################################################


import os

decidetime = 10 #the time that you can change

path = r"D:\CS2012\python\ProgrammingPython\sessions"  #the original data directory
pathr = r"D:\CS2012\python\ProgrammingPython\results-tmp" #the results data direcory 
li = os.listdir(path)
for p in li:#To operate every data file in the directory
    pathname = os.path.join(path,p)
    pathnamer = os.path.join(pathr,p)
    f = file(pathname,'r') #open the original data
    newf = file(pathnamer,'w+')#create result data
#-----------------------------------------------------#        
    line = f.readline()
    #split time
    for i in range(len(line)):
        if line[i] == '\t':
            time = line[:i]
            ntime = float(time)+decidetime
            newf.write(line)
            break

    while True:
        line = f.readline()
        if len(line) == 0: #Zero length indicates EOF
            break
        for i in range(len(line)): #catch the time
            if line[i] == '\t':
                time = line[0:i]
                time = float(time)
                if time < ntime: #separate address by time
                    newf.write('------'+line)#'------'means secondary address 
                    break
                ntime = time+decidetime
                newf.write(line)
                break

        
        
        
    f.close() 
    newf.close() 
