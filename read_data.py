import pandas
from Process import Process

class Read_csv:
    processes = []
    # process_id, arrival_time, service_time, IO_time
    def __init__(self, csv_file) -> None:
        self.read_csv(csv_file)
    
    def read_csv(self, csv_file):
        data = pandas.read_csv(csv_file)
        for v in data.values:
            obj = Process(v[0], v[1], v[2], v[3])
            self.processes.append(obj)
    
