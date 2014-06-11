def statid(x,y):
    if x is None:
        return  "UDOGM-"+str(int(6000)+int(y)).zfill(4)
    else:
        return  "UDOGM-"+str(int(x)).zfill(4)
        
