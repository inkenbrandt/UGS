def decdeg(x,y):
  degx = int(abs(x))
  degy = int(abs(y))
  tempx = 60* (abs(x) - degx)
  tempy = 60* (abs(y) - degy)
  minx = int(tempx)
  miny = int(tempy)
  secx = str(int(round(60*(tempx-minx),0))).zfill(2)
  secy = str(int(round(60*(tempy-miny),0))).zfill(2)
  return str(degy).zfill(2)+str(miny).zfill(2)+str(secy).zfill(2)+str(degx).zfill(2)+str(minx).zfill(2)+str(secx).zfill(2)
