import numpy  as np
import pandas as pd
import sys
import os

# file to read in 
f = sys.argv[1]

#f = 'r"' + f + '"'

# file name to output
fNameCSV = os.path.splitext(f)[0]+'.csv'
data = np.load(f)

try:

    #check if data can be read normally 
    DF = pd.DataFrame(data)
    DF.to_csv(fNameCSV)

except:

    #write to csv file directly with header
    out = open(fNameCSV, "w")
    out.write('Crossing_Point,Crossing_level,Threshold,Direction,Learning_rate') #update this to be dynamic
    out.write('\n')

    for tup in data:
        i = 0
        for item in tup:
            out.write(str(item)[1:-1]) 
            i += 1
            if (i != len(tup)):
                out.write(',')
        out.write('\n')

finally: 
    print('generated ', fNameCSV, 'from', f)