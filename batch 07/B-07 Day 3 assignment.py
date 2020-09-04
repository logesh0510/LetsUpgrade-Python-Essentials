#Assignment question
print('''1)You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is
1000ft, it it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask
the pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try
later”''')
a=input("enter the altitude:")#taking input
alt=int(a)#assigning input to altitude
if alt<1000:
    print("land the plane")
elif 1000<alt<5000:
    print("come down to 1000ft")
else:
    print("go around and try later")

#1st question completed.

print('''(2)Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE
function.''')
start=1
end=200
print("prime numbers between 1-200 are:")
for num in range(2,end+1):
    for i in range(2,num):
            if (num%i)==0:
                break
    else:
        print(num,end=',')
            
    

