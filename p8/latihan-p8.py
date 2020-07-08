import aritmatika
import pythagoras

p = 5
q = 12

print('penjumlahan', p, '+', q, '=', aritmatika.penjumlahan(p,q))
print('pengurangan', p, '-', q, '=', aritmatika.pengurangan(p,q))
print('perkalian', p, '*', q, '=', aritmatika.perkalian(p,q))
print('pembagian', p, '/', q, '=', aritmatika.pembagian(p,q))

print('pythagoras a =', p, 'dan b =', q, 'adalah c =', pythagoras.findC(p,q))
