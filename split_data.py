# Import Python library to work with SciServer

# Query with CasJobs
import SciServer.CasJobs as CasJobs

# Import other libraries

# Data manipulation
import pandas
# Warnings
import warnings

# Don't show python warnings
warnings.filterwarnings('ignore')

print("SciServer library imported")
print('Supporting libraries imported')

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
# being returned as a dataframe.
q = CasJobs.executeQuery(query, "dr14")

# Check data and drop any row that has NaN.
q.dropna()
# Check that all types in columns are as expected.
q.info()

# Write to file.
q.to_csv("result.csv")

print("SQL query finished.")
