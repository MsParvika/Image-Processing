# Image Processing
The project experiments with
• text and image features,
• vector models, and
• similarity/distance measures
**_Not meant to be Copied


### Getting Started
```
- Open a terminal. Browse into Project directory -Image Processing
 - For Windows: Type "RunMe.py"
 - For Mac and Linux: Type "python ./RunMe.py"
Note: Project creates a local connection(localhost:27017) with MongoDb and creates/uses DataBase name "ImageProcessing"
```

### Format of the input
- Inputs except Directory Path should be space separated.
- The model type name should be all in upper case
e.g.  Command: Enter directory path
       Input: C:\Users\abc\OneDrive\Documents\devSet
      Command: Enter task Number
       Input:1
      Command: Enter id,type and k
       Input:abc@N00 TF 3  (space separated, uppercase Model name)


### Prerequisites
- Python 3 or better should be installed and configured on the system
- MongoDb v4.0.2 should be installed and configured


### Libraries Required
```
math
pymongo
xml.etree.ElementTree
sklearn.Kmeans
pandas
```

### Author
Parvika Singhal
psingha4@asu.edu
