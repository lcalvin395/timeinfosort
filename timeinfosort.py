
x=0
y=0
path='/Users/lukecalvin/2023/eli_np_muon_primaries/'
file1 = open("%smuon+_time.txt"%(path), "w")
file2 = open("%spositime.txt"%(path), "w")
for l in range(1,5):
    
    file3 = open("%smuon_production00%d_timeInfo"%(path,l),'r')
    
    for line in file3.readlines():
        columns=line.split()		
        if columns[2]=='10' or x!=0:
            file1.write(line)
            x=x+1
    if x==3:
        x=0
        file1.write("\n")
        if columns[2]=='11' or y!=0:
            file2.write(line)
            y=y+1
            if y==3:
                y=0
        file2.write("\n")
    file3.close()
    

file1.close()
file2.close()
