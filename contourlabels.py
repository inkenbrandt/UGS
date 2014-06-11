def FindLabel([CONTOUR]):
  if (float([CONTOUR])*10)%20<1: 
    return [CONTOUR]
  else:
    return ''
    
