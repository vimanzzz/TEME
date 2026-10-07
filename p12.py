b_yr = 2007
b_mo = 2
b_da = 5

c_yr= 2026
c_mo= 10
c_da = 8

TOTAL_DAYS=int(0)

def leap(n):
    n = int(n)

    if( n % 4 ==0 and n %100 != 0 ) or n % 400 ==0 :
        return True
    else :
        return False
#yrs
for i in range(b_yr, c_yr-1) :
    if leap(i) == True:
        TOTAL_DAYS +=366
    else :
        TOTAL_DAYS +=365

#months
months_array = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#               0   1   2  3   4    5   6   7   8  9   10   11  12for i in range

for i in range(b_mo,12 + 1) :
    if i==2 and leap(b_yr):
        TOTAL_DAYS +=29
    else:
        TOTAL_DAYS += months_array[i]

for i  in range(1, c_mo) :
    TOTAL_DAYS+= months_array[i]

#days
if c_da > b_da :
    TOTAL_DAYS += c_da - b_da
elif c_da < b_da :
    TOTAL_DAYS += months_array[c_mo] - b_da + c_da

print(TOTAL_DAYS)