#Operator Bitwise

a = 4
b = 11
print('nilai :',a,', binary :', format(a,'08b'))
print('nilai :',b,', binary :', format(b,'08b'))

#Bitwise |
c = a | b;
print("\n","==========A==========")
print('nilai a|b :',c,', binary :', format(c,'08b'))

#Bitwise >>
c = a >> b;
print("\n","==========B==========")
print('nilai 4>>11 :',c,', binary :', format(c,'08b'))

#Bitwise ^
c = a ^ b
print("\n","==========C==========")
print('nilai 4^11 :',c,',binary :', format(c,'08b'))

#Bitwise ~
c = ~a
print("\n","==========D==========")
print('nilai ~4 :',c,',binary :', format(c,'08b'))

#Biswise &
c = 11 & 4
print("\n","==========E==========")
print('nilai 11 & 4 :',c,',binary :', format(c,'08b'))

