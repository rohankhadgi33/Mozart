import stdaudio
import stdio
import sys

# create a 1D list and input the WALTZ measures
WALTZ = []
WALTZ += stdio.readAllInts()

# compute to see if there is any error
# write and exit the program if any error found
if len(WALTZ) != 32:
    sys.exit('A waltz must contain exactly 32 measures')
for i in range(0, 16):
    if 1 > int(WALTZ[i]) > 176:
        sys.exit('A minuet measure must be from [1, 176]')
for i in range(16, 32):
    if 1 > int(WALTZ[i]) > 96:
        sys.exit('A trio measure must be from [1, 96]')

# in a loop compute and play the sound
for i in range(0, 16):
    filename = 'data/M' + str(WALTZ[i])
    stdaudio.playFile(filename)

# in a loop compute and play the sound
for i in range(16, 32):
    filename = 'data/T' + str(WALTZ[i])
    stdaudio.playFile(filename)