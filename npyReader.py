import numpy  as np
import pandas as pd
import sys
import os
import re

# File to read in 
f = sys.argv[1]

# File name to output
fNameCSV = os.path.splitext(f)[0]+'.csv'
data = np.load(f) # load data 

# Check if data can be read normally. 
# This is to determine if the file is structured or not.
# This will work for an unstructured file.  
try:

    DF = pd.DataFrame(data)
    DF.to_csv(fNameCSV)

# This is the reader for structured array .npy files. 
except:

    # Write header directly to csv file.
    header = np.lib.format.header_data_from_array_1_0(data) # get header
    out = open(fNameCSV, "w")
    # Parse fields from header.
    header = re.sub("\s", "_", str(header))
    fields = re.findall("'([A-Z]\w*)+'*", header)
    # Write fields to csv. 
    i = 0
    for field in fields:
        out.write(str(field))
        i += 1
        if (i != len(fields)):
                out.write(',')
    out.write('\n')

    # Wirte data to csv file.
    for tup in data:
        i = 0
        for item in tup:
            out.write(str(item)[1:-1]) 
            i += 1
            if (i != len(tup)):
                out.write(',')
        out.write('\n')

# Prints out location of the .csv file, it should be in the same directory as the original .npy file.
finally: 
    print('generated ', fNameCSV, 'from', f)