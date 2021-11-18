import pathlib
import multiprocessing
import csv
from classes.target import TargetDir
from classes.target import TargetFile

#getting the root directory path
folPath = r'C:\Windows'
path = pathlib.Path(folPath)


if __name__ == "__main__":
    #shared array
    manager = multiprocessing.Manager()
    return_list = manager.list()

    #array that will hold all the processes
    process_array = []

    #adding to the search list all the desired search criterias as classes
    search_list = [TargetDir(pathlib.Path(folPath), 'addins'), TargetDir(pathlib.Path(folPath), '*ERRORREP*'),
                   TargetDir(pathlib.Path(folPath), '*GNOFF'), TargetDir(pathlib.Path(folPath), '*QHE*'),
                   TargetFile(pathlib.Path(folPath), '*XT.ec*'), TargetFile(pathlib.Path(folPath), '*ACGenral*'),
                   TargetFile(pathlib.Path(folPath), '*.sdb')]

    for target in search_list:
        p = multiprocessing.Process(target=target.find_target, args=(return_list, ))
        process_array.append(p)

    for p in process_array:
        p.start()

    for p in process_array:
        p.join()

    #creating the csv file from the final list
    with open('file_assignment.csv', 'w') as new_file:
        fieldnames = ['<FolderPath>', '<FileName>', '<CreationDate>', '<ModifiedDate>', '<DateAccessed>']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for file in return_list:
            csv_writer.writerow(file)

