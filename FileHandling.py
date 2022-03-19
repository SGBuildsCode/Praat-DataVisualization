# Working with Praat, this program (through accessing TextGrid Files) determines how long it takes the recipient to answer the phone 
# after the Ring Tone has ended.

# Note: For files which handle or deal with Textgrid Files that are associated with Praat 
# (which is a software package for speech analysis in phonetics), a module named Praatio (specifically Praatio-4.4.0) 
# will need to be installed in order for there not to be any incompatibilies or errors which may arise. 


from praatio import tgio 
import os 
import glob


txtGFile = tgio.openTextgrid(r'C:\Users\PC\Desktop\TextGFiles\002_00000039.TextGrid',readRaw=True)  
rData = txtGFile.tierNameList  # Displays the labels for the textgrid file specified in the file path.
print(rData)


# FilePa = glob.glob(r'C:\Users\PC\Desktop\TextGFiles')
# print(FilePa)

GridContents = txtGFile.tierDict['Live Start'] # This statement passes a string into a dictionary that corresponds to one of many labels 
                                               # that can be found in a TextGrid file. In this case the label in question is Live Start.
REnd = txtGFile.tierDict['Ring End']        

ValExtraction = []

for time in REnd.entryList[0]:   # For reference (and as is detailed in their documentation which can be accessed at
                                 # https://timmahrt.github.io/praatIO/),  
    ValExtraction.append(time)   # Index 0 of the entryList is where the values or timestamps are contained (May sometimes contain multiple values). 
                                 # Index [1] is where the labels are contained.  
 

Lstart = [] 

for time in GridContents.entryList[0]: 
    Lstart.append(time)

LsTime = Lstart[0]
RingT = ValExtraction[0]

ResponseT = int(LsTime - RingT) 

LabelTimes = "Ring End is labelled at: {0} Seconds, Live Start is labelled at : {1} Seconds"
print(LabelTimes.format(int(RingT),int(LsTime)))

Duration = "The recipient picked up the phone after {0} seconds"
print(Duration.format(ResponseT)) 
































