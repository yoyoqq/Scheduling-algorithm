import sys
import pandas
from Data.Collect_data import Collect_data
from Algorithms.RR import RR
from Algorithms.MLFQ import MLFQ
from Algorithms.SJF import SJF
from Algorithms.FCFS import FCFS

# from Data import *

csv_file = "Data/data.csv"


while True:
    # Select algorithm
    print("Choose an algorithm")
    print("FCFS, SJF, RR, MLFQ")
    choice = input()
    if choice not in ["FCFS", "SJF", "RR", "MLFQ"]:
        print("Invalid choice")
        continue

    # Read data from csv file
    data = Collect_data(csv_file)

    # Algorithm
    if choice == "FCFS":
        output = FCFS(data)
    elif choice == "SJF":
        output = SJF(data)
    elif choice == "RR":
        output = RR(data)
    elif choice == "MLFQ":
        output = MLFQ(data)
    break