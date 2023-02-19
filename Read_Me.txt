CPU scheduling algorithm

This is a simulator on how a CPU scheduling algorithm would work.
It will have:
    First come first serve (FCFS)
    Shortest job first (SJF)
    Round Robin (RR)
    Multilevel feedback queue(MLFQ)

For the program input it uses a csv file and read the columns in the following structure:
    process_id, arrival_time, service_time, IO_time

Program output:
    Each process will have:
        Run time
        End time
        Wait time
        IO time (blocked)
    
    The algorithm will show:
        Total time 
        Idle time
        Average waiting time
        average response time
        CPU utilization
        