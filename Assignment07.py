# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with binary files and pickle module,
#              When the program starts, dump some lines in a .dat file,
#              gather more data, read the whole file,
#              catch the exception thrown when there is no more data to read
# ChangeLog (Who,When,What):
# KClarke,2.26.2023,created file to complete assignment 07
# KClarke,2.16.2023,Modified code to complete assignment 07
# ---------------------------------------------------------------------------- #

import pickle

testData = "test line 1\n" \
           "line 2\n" \
           "line 3"
testFileName = "Data.dat"

objFile = open(testFileName, "wb")
pickle.dump(testData, objFile)
objFile.close()

# more data -------------------------
moreData = "line 4"
objFile = open(testFileName, "ab")
pickle.dump(moreData, objFile)
objFile.close()
# -----------------------------------

objFile = open(testFileName, "rb")
while True:
    try:
        fileData =  pickle.load(objFile)
    except EOFError as e:
        fileData = "end of file"
    if fileData !="end of file":
        print(fileData)
    else:
        objFile.close()
        break
