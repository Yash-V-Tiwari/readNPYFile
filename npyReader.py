import numpy  as np
import pandas as pd
import glob
import os
import re

# Recursively finds all .npy files
npyFiles = glob.glob("*.npy")

# data = np.array([
#     (1, 'Zayden Jer', 86.5),
#     (2, 'Luna Marci', 90.0),
#     (3, 'Kord Shane', 88.0),
#     (4, 'Coeus Zora', 91.5)
# ], dtype=[('ID', 'i4'), ('Name', 'U10'), ('Score', 'f4')])

# np.save('data', data)

for f in npyFiles:
    fName = os.path.splitext(f)[0]+'.csv'
    fCSV = np.load(f, allow_pickle = True)
    try:
        DF = pd.DataFrame(fCSV)
        DF.to_csv(fName)
    except:
        dt = np.dtype([])
        print('fail')
    else: 
        print('generated ', fName, 'from', f)