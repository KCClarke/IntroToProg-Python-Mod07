Kasey Clarke 

2/28/2023 

Foundations of Programming (Python) 

Assignment07 

 

# Assignment 7 

## Introduction 

This document outlines the steps I took to learn about how Python deals with Binary Files and Exceptions. 

 

## Previewing the Class Material 

I started by watching the Mod07 YouTube video, reading the corresponding chapter from the assigned book and watching the Panopto recording for the week. I go through the material in one shot to get an overview of the topics covered in the assignment for the week. After Getting an idea of the topics I download the class materials and prepared to dive in. 

 

## Diving In 

I wrote in my planner a checklist of the listings in the Panopto recording with the intention of writing them with binary files instead of text files. The first two listings were simple to write with binary instead of text files. Attempting the third listing I ran into a problem because the function to read objects from a binary file only reads one line at a time and the third listing required more than one line to be read from a file. I felt this a good place to start researching to see what solutions could be found on the internet for my problem with listing 3. 
![Listing3-AppendB](https://user-images.githubusercontent.com/125520296/222291417-5c5b3da7-aa33-4a8f-bcd2-5e1ad7306f6a.png)

Figure 1. My first attempt to read multiple lines of a binary file (line 30) feels like it should work with a for-loop and the keyword “in” (line 17) but it simply does not. 

 

## Researching 

I began searching the internet for terms that I was using in my code. I was looking for keywords and phrases such as “pickling”, “reading a binary file in python”, “pickle.load()” and “for-loop” in various combinations for hours. I found material that was at best tangential to what I needed, and I was burning through time and becoming stressed. 

  ![thanx](https://user-images.githubusercontent.com/125520296/222291496-b78d5a8a-b1c4-4272-8955-
  Figure 2. Most* of the examples I found when I was researching felt above my level of comprehension or irrelevant. *Most because I am sure that after a while, I was in a dazed state of clicking links and closing tabs on my internet browser. 46756f115f53.png)
  
![time stamp](https://user-images.githubusercontent.com/125520296/222291907-04b9abec-5ab1-498c-abfe-d7d4d87e9ac4.png)

Figure 3. The timestamp of the concept I was stuck on (39:40). 

The problem I was having with Listing 3 is outlined in this week's lecture video, so I wanted to make sure I was able to get it, so I kept trying. 

 

## The problem 

I want to be able to read a binary file of unknown length and print it to the console. I did not know the syntax to do this with a Python for-loop and the “in” keyword and was stuck in a painful trial and error cycle wasting tons of time. 

 

Eventually I stopped trying to jam python’s pickle.load() function into for-loops and tried a while-loop. I thought that if I have a while loop that checks for an empty string at the end of a file, I might be able to read a binary file with any number of lines in it. It worked! I was able to read a binary file with any number of lines, but it generated an exception saying that it was out of data to read. I was so excited that it worked I tried to fix the error and forgot to document it. 

 

## Dealing With the Error 

I had not yet made it to typing the listings from the Panopto recording that detailed exception handling and I thought I could work through the problem without the “try & except” structure. 

I could append a flag variable to the end of my file and have the while-loop and load() check for the flag to know when to stop reading the file. With my handy flag any number of lines of data could be written to a file and I could make the flag the last thing in the file.  
![handy flag](https://user-images.githubusercontent.com/125520296/222291983-8900d55d-7f50-464c-8299-b2b371b80b32.png)

Figure 4. Listing9-B, a structure to use the pickle module to read any number of lines from a binary file. Substitute lines 16 to 21 with a loop that gathers data from a user and the flag is still the last thing in the file (lines 23 to 26). The user would not see the flag because it is never printed. 

Finally, I had actualized my idea and I began writing the remaining listings like a bat out of heck. 🦇

 

## Handling the Exception 

After working through all the listings, I realized that I could rewrite the code from figure 4 to show the use of the “try & except” structure. 
![try except](https://user-images.githubusercontent.com/125520296/222292055-de8dbcd7-310e-453d-b798-6eaf9ede25e4.png)

Figure 5. Listing 13-B, a structure with the same net result as in figure 4 using the "try except” block and 3 less lines of code. 

 

## Conclusion 

I am trying something new, in the earlier 6 assignments I have avoided the first-person pronoun. The first three example assignments used “I” and the fourth did not. I was aiming at imitating “Writing example 4.pdf” because it seemed the most professional to me, but it seemed to be costing me points (precious points!). The point may not be the points but the lesson I learned. 

 

The most important thing I learned in this module is that the solution to the specific problem I have may not be published on the internet. The material in the lectures was sufficient for me to solve my problem but I may not have realized that had I not stress-surfed the internet for hours. 
![A07 in pycharm](https://user-images.githubusercontent.com/125520296/222292108-e59c380c-6044-499b-8128-09a6f92113f5.png)

Figure 6. Assignment 7 in PyCharm.

![dat file in notepad](https://user-images.githubusercontent.com/125520296/222292155-c70b9def-785c-40f3-8dfe-bf17a8513a52.png)

Figure 7. Binary file used in assignment 7. 

![A07 in cmd](https://user-images.githubusercontent.com/125520296/222292215-b3614623-db0f-4190-9b48-207aaf067581.png)

Figure 8. Assignment 7 in the command window. 

```
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
```
Figure 9. The code for reading a binary file of any size.
