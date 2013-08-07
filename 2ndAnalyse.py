#filename:2ndAnalyse.py
#To analyse the action of user 

import os

#split address
def splitadd(line):
    s = 0
    e = 0
    tmp1 = 1
    #print line
    for i in range(len(line)):
        if line[i]<='z' and line[i]>='a':
            if (line[i-1]==' ' or line[i-1]=='\t') and tmp1:
                s = i
                tmp1 = 0
            #print line[i+1]
        if line[i]=='N' or (line[i]>='a' and line[i]<='z'):
            if (line[i-1]=='\t'):
                e = i
        
#    print s,e
    address = line[s:e]
    return address
        

#decide start
#def start(address):


#decide jump
##def isJump(addn,addl):
##    if addn != addl:
##        return True
##    else:
##        return False
    
###addn means current address, addf means former address, addl means latter address   

#decide fresh
def isFresh(addn,addl):
    if addn == addl:
        return True
    else:
        return False
        
#decide back
def isBack(addf,addl):
    if addf == addl:
        return True
    else:
        return False

    
def main():
    path = r"D:\CS2012\python\ProgrammingPython\results-tmp"#the 1stAnalyse results
    pathr = r"D:\CS2012\python\ProgrammingPython\results"#the results directory  and you can change
                                                         #the directory to results-s and comment
                                                         #            "else:
                                                         #              newf.write(line)"
                                                         #to get simple results
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path,p)
        pathnamer = os.path.join(pathr,p)
        #print p
        f = file(pathname,'r')
        newf = file(pathnamer,'w+')

        line = f.readline()
        #print line
        addf = ' '
        addn = splitadd(line)
        #print addn
        newf.write("Start\t"+line)
        
        while True:
            line = f.readline()
            if len(line)==0:
                break
            if line[0] != '-':
                addl = splitadd(line)
##                print "addf: "+addf
##                print "addn:",addn
##                print "addl:",addl
                if isFresh(addn,addl):
                    newf.write('Refresh\t'+line)
                else:
                    if isBack(addf,addl):
                        newf.write('Back to\t'+line)
                    else:
                        newf.write('Jump to\t'+line)
                addf = addn
                addn = addl
            else:                    #comment here to
                newf.write(line)     #get simple results
        f.close()
        newf.close()
        
    return 0
    
main()        






        
