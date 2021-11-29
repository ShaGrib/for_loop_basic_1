# print 1-150
for a in range(151):
    print(a)

print("------------------------------") #spacer for readability
# print multiples of 5
for b in range(5, 1001):
    if b % 5 == 0:
        print(b)

print("------------------------------") #spacer for readability
# print Coding Dojo on multiples of 10, Coding on multiples of 5 and print all the numbers inbetween
for c in range(1, 101):
    if c % 10 == 0:
        print("Coding Dojo")
    elif c % 5 == 0:
        print("Coding")
    else:
        print(c)

print("------------------------------") #spacer for readability
# print the sum of the odd numbers up to 500000
addd = 0

for d in range(0, 500001):
    if d % 2 != 0:
        addd = addd + d
print(addd)

print("------------------------------") #spacer for readability
# print the even numbers from 2018 to 0 while counting down by 4
for e in range(2018, 0, -4):
    if e % 2 == 0:
        print(e)

print("------------------------------") #spacer for readability
# Flexible printing from a low value to a high value based on a variable multiplier
lown = 4
highn = 31
mult = 6

for f in range(lown, highn):
    if f % mult == 0:
        print(f)