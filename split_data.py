# Code for splitting the database into two sets: training data, and data to be analysed.

# Import Python libraries to work with SciServer

# Query with CasJobs
import SciServer.CasJobs as CasJobs
# R/W to/from SciDrive
import SciServer.SciDrive as SciDrive
# Show individual objects and generate thumbnail images through SkyServer (module not found)
#import SciServer.SkyServer as SkyServer
print("SciServer libraries imported")

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
print('Supporting libraries imported')

# Apply some special settings to the imported libraries

# Ensure columns get written completely
pandas.set_option('display.max_colwidth', -1)
# Don't show python warnings
import warnings
warnings.filterwarnings('ignore')
print('Settings applied')

# This query finds all galaxies in SDSS data release 14 (DR14) with a size (petror90_r) greater than 10 arcseconds, 
# within a region of sky with 100 < RA < 250, a redshift between 0.02 and 0.5, and a g-band magnitude brighter than 17.
# 
# First, store the query in an object called "query"
query = """
SELECT p.objId,p.ra,p.dec,p.petror90_r, p.expAB_r,
    p.dered_u as u, p.dered_g as g, p.dered_r as r, p.dered_i as i, 
    s.z, s.plate, s.mjd, s.fiberid
FROM galaxy AS p
   JOIN SpecObj AS s ON s.bestobjid = p.objid
WHERE s.z between 0.75 and 1
ORDER BY p.ra
"""

query2 = """
SELECT g.specObjID, g.ra, g.dec, g.spectrotype
FROM galSpecInfo AS g
WHERE g.ra > 0
ORDER BY g.specObjID
"""

query3 = """
SELECT p.specObjID, p.type, p.u, p.g, p.r, p.i, p.z
FROM PhotoObjAll as p
WHERE p.type = 3
    and p.ra > 0
    and p.z between 0 and 0.05
ORDER BY p.specObjID
"""

#Then, query the database. The answer is a table that is being returned to a dataframe that we've named all_gals.
all_gals = CasJobs.executeQuery(query, "dr14")
q2 = CasJobs.executeQuery(query2, "dr14")
#q3 = CasJobs.executeQuery(query3, "dr14")

print(q2)
print("")
#print(q3)
#print("")

for c in all_gals.columns:
    print(c)
print("")

#f = open("result", "w")
#f.write(all_gals)
#f.close()

print("SQL query finished.")
