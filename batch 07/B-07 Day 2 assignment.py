#List
lst=[5,25.3,'insta',[2,885,55]]
lst.append(98)
print(lst)
print(lst.count('insta'))
lst.reverse()
print("lst1:",lst)
print(lst)
lst.insert(2,'logesh')
print(lst)
lst1=lst.copy()
print(lst1)
 
#dictionary
dct={"maths":"98",'science':'95'}
print(dct.get('maths'))
keys=dct.keys()
print(keys)
d1={'social':'99'}
dct.update(d1)
print(dct)
print(dct.popitem())
print(dct.setdefault('maths','100'))

#sets
s1={1,5,8,'logesh',10}
s2={5,8,4,6}
print(s1.isdisjoint(s2))
set1=s1.difference(s2)
print(set1)
set2=s1.intersection(s2)
print(set2)
print(s1.union(s2))
set3=s1.symmetric_difference(s2)
print(set3)

#tuples
tup=(1,5,8,4,2,5,1,2,9)
print(tup.count(8))
print(tup.index(2))

#strings
a="I am Indian"
print(a.center(20))
print(a.istitle())
b=a.encode()
print(b)
print(a.partition('Indian'))
c=a.replace('Indian','tamilan')
print(c)








