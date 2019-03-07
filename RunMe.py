from pymongo import MongoClient

import DataRepositoryRunsOnlyOnce
import TaskProcessors.ProcessTask1
import TaskProcessors.ProcessTask2
import TaskProcessors.ProcessTask3
import TaskProcessors.ProcessTask4
import TaskProcessors.ProcessTask5

if __name__ == "__main__":
    client = MongoClient()
    db = client.ImageProcessing
    directory_path = input(" Please enter files location path till devset and wait for data to load into db... ")
    DataRepositoryRunsOnlyOnce.runMeForData(directory_path, db)
    while True:
        print(
            "Task 1: Return the most similar k users based on textual descriptors: given user ID, model (tf, df, tfIdf) & k")
        print(
            "Task 2: Return the most similar k images based on textual descriptors: given a image ID, a model (tf, DF, TF-IDF)& k")
        print(
            "Task 3: Return the most similar k locations based on textual descriptors: given a location ID, a model (TF, DF, TF-IDF)& k")
        print(
            "Task 4: Return the most similar k locations based on the corresponding visual descriptors of the images : given location ID, model (CM, CM3x3, CN etc)& k")
        print(
            "Task 5: Return the most similar k locations based on the corresponding visual descriptors of the images : given location ID & k ")

        taskNumber = input("Enter the task no. which you want to test or Enter X/x to exit")
        if taskNumber == '1':
            TaskProcessors.ProcessTask1.processTask1(db)
        elif taskNumber == '2':
            TaskProcessors.ProcessTask2.processTask2(db)
        elif taskNumber == '3':
            TaskProcessors.ProcessTask3.processTask3(directory_path,db)
        elif taskNumber == '4':
            TaskProcessors.ProcessTask4.processTask4(directory_path,db)
        elif taskNumber == '5':
            TaskProcessors.ProcessTask5.processTask5(directory_path,db)
        elif taskNumber == 'x' or taskNumber == 'X':
            break
        else:
            print("Oops. Wrong Input. Try Again")
    client.close()
