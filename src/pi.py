#! /usr/bin/python

def aprxpi(n):
  s = 0.0
  for i in range(1,n+1):
    x_i = float((i-0.5)/n)
    fx_i = float(4.0/(1.0 + x_i * x_i))
    s = s + fx_i
    r = s / n
  return r
   
n= int(raw_input('Introduzca el numero de intevalos (n > 0): '))
v= int(raw_input('Introduzca el numero de veces a repetirse: '))
l = [ ]
for i in range(1,v+1):
  a= aprxpi(n*i)
  l=l+[a]
  print a
print l