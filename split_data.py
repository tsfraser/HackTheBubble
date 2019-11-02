# Code for splitting the database into two sets: training data,
# and data to be analysed.

# Import Python libraries to work with SciServer

# Query with CasJobs
import SciServer.CasJobs as CasJobs
# R/W to/from SciDrive
import SciServer.SciDrive as SciDrive

# Import other libraries

# Standard Python library for math operations
import numpy as np
# Save images as files
from scipy.misc import imsave
# Data manipulation
import pandas
# Graphing
import matplotlib.pyplot as plt
# Managing local files
import os
# Warnings
import warnings

print("SciServer libraries imported")
print('Supporting libraries imported')

# Apply some special settings to the imported libraries

# Ensure columns get written completely
pandas.set_option('display.max_colwidth', -1)
# Don't show python warnings
warnings.filterwarnings('ignore')

print('Settings applied')

# This query finds all objects from galSpecInfo
# with extra data pulled from PhotoObjAll.
query = """
SELECT g.specObjID, p.type, p.u, p.g, p.r, p.i, p.z, g.spectrotype
FROM galSpecInfo AS g
    JOIN PhotoObjAll as p ON p.specObjID = g.specObjID
ORDER BY g.specObjID
"""

# Then, query the database. The answer is a table that is
# being returned as a csv.
q2 = CasJobs.executeQuery(query, "dr14", format="csv")

f = open("result.txt", "w")
f.write(q2)
f.close()

print("SQL query finished.")
