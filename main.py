import pathlib
import datetime
import time
import glob
import os
import multiprocessing
from classes.target import Target
from classes.target import TargetDiv
from classes.target import TargetFile


file_list = []


def convert_date(timestamp):
    d = datetime.datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

folPath = r'C:\Windows'
path = pathlib.Path(folPath)

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    return_list = manager.list()
    process_array = []

    search_list = [TargetDiv(pathlib.Path(folPath), 'addins'), TargetDiv(pathlib.Path(folPath), '*ERRORREP*'),
                   TargetDiv(pathlib.Path(folPath), '*GNOFF'), TargetDiv(pathlib.Path(folPath), '*QHE*'),
                   TargetFile(pathlib.Path(folPath), '*XT.ec*'), TargetFile(pathlib.Path(folPath), '*ACGenral*'),
                   TargetFile(pathlib.Path(folPath), '*.sdb')]

    for target in search_list:
        p = multiprocessing.Process(target=target.find_target, args=(return_list, ))
        process_array.append(p)

    for p in process_array:
        p.start()

    for p in process_array:
        p.join()

    for file in return_list:
        print(file['name'], file['path'], file['mdate'])

