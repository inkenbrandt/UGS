def quarterfill(tow, ran, sec, quad, x, a):
 g=x[0:2]
 h=x[2:4]
 if g=='NE':
  qq = 'a'
 elif g=='NW':
  qq = 'b'
 elif g=='SW':
  qq = 'c'
 elif g=='SE':
  qq = 'd'
 else:
  qq = ''
 if h=='NE':
  q = 'a'
 elif h=='NW':
  q = 'b'
 elif h=='SW':
  q = 'c'
 elif h=='SE':
  q = 'd'
 else:
  q = ''
 if a > 90:
  qqq='d'
 elif a <-90:
  qqq='a'
 elif a < 90 and a > 0:
  qqq = 'c'
 elif a < 0 and a > -90:
  qqq = 'b'
 else:
  qqq = ''
 p = int(quad) 
 if p==1:
  j='A'
 elif p==2:
  j='B'
 elif p==3:
  j='C'
 elif p==4:
  j='D'
 else:
  j=''
 return '('+str(j)+'-'+str(tow)+'-'+str(ran)+')'+str(sec)+q+qq+qqq
