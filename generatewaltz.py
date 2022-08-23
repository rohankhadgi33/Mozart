import stdarray
import stdrandom
import stdio

# create two 2D list named MINUET and TRIO
MINUET = stdarray.create2D(11, 16)
TRIO = stdarray.create2D(6, 16)

# in a loop input all the values in 2D list MINUET
for i in range(0, 11):
    for j in range(0, 16):
        MINUET[i][j] = stdio.readInt()

# in a loop input all the values in 3D list TRIO
for i in range(0, 6):
    for j in range(0, 16):
        TRIO[i][j] = stdio.readInt()

# in a loop compute and write the Minuet measures
for j in range(0, 16):
    x = stdrandom.uniformInt(0, 6)
    y = stdrandom.uniformInt(0, 5)
    i = x + y
    stdio.write(str(MINUET[i][j]) + ' ')

# in a loop compute and write the Trio measures
for j in range(0, 16):
    i = stdrandom.uniformInt(0, 6)
    stdio.write(str(TRIO[i][j]) + ' ')