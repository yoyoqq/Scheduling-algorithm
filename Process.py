class Process:

    run_time = 0
    end_time = 0
    wait_time = 0
    io_time = 0

    def __init__(self, process_id, arrival_time, service_time, IO_time) -> None:
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.IO_time = IO_time

    def get_Process(self):
        return self.process_id, self.arrival_time, self.service_time, self.IO_time