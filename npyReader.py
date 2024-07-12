import numpy  as np
import pandas as pd
import sys
import os
import re

# file to read in 
f = sys.argv[1]

#f = 'r"' + f + '"'

# file name to output
fNameCSV = os.path.splitext(f)[0]+'.csv'
data = np.load(f)

try:

    # check if data can be read normally 
    DF = pd.DataFrame(data)
    DF.to_csv(fNameCSV)

except:

    # write header directly to csv file
    header = np.lib.format.header_data_from_array_1_0(data) # get header
    out = open(fNameCSV, "w")
    # parse fields from header
    header = re.sub("\s", "_", str(header))
    fields = re.findall("'([A-Z]\w*)+'*", header)
    # write fields to csv 
    i = 0
    for field in fields:
        out.write(str(field))
        i += 1
        if (i != len(fields)):
                out.write(',')
    out.write('\n')

    # wirte data to csv file
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