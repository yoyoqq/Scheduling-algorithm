from read_data import Read_csv
from typing import List
from Process import Process
from AlgoStruct import AlgoStruct

class FCFS(AlgoStruct):
    def __init__(self, processes: List[Process]):
        self.processes = processes

r = Read_csv('data.csv')
a = FCFS(r)