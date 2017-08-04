import random
import math
import os

class Request:
    def __init__(self,server_frequency):
        global prev_arrival_time
        self.mean_arrival_rate = 7.2
        self.uniform_a = 0.75
        self.uniform_b = 1.17
        self.alpha1 = 0.43
        self.alpha2 = 0.98
        self.beta = 0.86
        self.server_frequency = server_frequency
        self.inter_arrival_time = self.generate_arrival_time()
        prev_arrival_time += self.inter_arrival_time
        self.arrival_time = prev_arrival_time
        #print(self.arrival_time)
        self.service_time = self.generate_service_time()
        self.end_time = self.arrival_time + self.service_time

    def generate_arrival_time(self):
        a1 = random.expovariate(self.mean_arrival_rate)
        a2 = random.uniform(self.uniform_a, self.uniform_b)
        return a1*a2

    def generate_service_time(self):
        gama = (1-self.beta)/(math.pow(self.alpha2, (1-self.beta)) - math.pow(self.alpha1, (1-self.beta)))
        time = random.random()*(self.alpha2 - self.alpha1) + self.alpha1
        return time/self.server_frequency


class Server:
    def __init__(self, frequency, power):
        self.request_under_exec = None
        self.waiting_queue = []
        self.ready_queue = []
        self.frequency = frequency
        self.power = power
        self.execution_time = 0
        self.idle_time = 0

    def set_frequency(self, frequency):
        self.frequency = frequency

    def is_busy(self):
        if self.request_under_exec is None:
            return False
        else:
            return True

    def is_ready_queue_full(self):
        if len(self.ready_queue) >= MAX_READY_QUEUE:
            return True
        else:
            return False

    def receive_request(self, request):
        self.waiting_queue.append(request)

    def print(self):
        print("Waiting Queue : " + str(len(self.waiting_queue)))
        print("Ready Queue : " + str(len(self.ready_queue)))
        print("Executing Request : " + str(self.request_under_exec))
        print("Idle Time : " + str(self.idle_time))
        print("Execution Time : " + str(self.execution_time))
        #input("Press enter to continue")

    def update_queues(self):
        if self.is_busy():
            self.execution_time += UNIT_TIME
        else:
            self.idle_time += UNIT_TIME
        if self.is_busy() and self.request_under_exec.end_time <= global_time:
            self.request_under_exec = None
        for request in self.waiting_queue:
            if request.arrival_time <= global_time:
                self.ready_queue.append(request)
                self.waiting_queue.remove(request)
        for request in self.ready_queue:
            if not self.is_busy():
                self.request_under_exec = request
                self.ready_queue.remove(request)


class ServerPool:
    def __init__(self, server_num, power):
        self.server_num = server_num
        self.servers = []
        self.power = power
        self.server_power = self.power / self.server_num
        self.server_frequency = self.calculate_frequency(self.server_power)
        for i in range(self.server_num):
            s = Server(self.server_frequency, self.server_power)
            self.servers.append(s)

    def calculate_frequency(self, power):
        return (1.25 + 0.31*((power/200) - 1))

    def receive_requests(self, requests):
        for i in range(len(requests)):
            self.servers[i%self.server_num].receive_request(requests[i])

    def are_all_servers_busy(self):
        for server in self.servers:
            if not server.is_ready_queue_full():
                return False
        return True

    def is_waiting_queues_empty(self):
        for server in self.servers:
            if len(server.waiting_queue) == 0:
                return True
        return False

    def update_servers(self):
        for server in self.servers:
            server.update_queues()

    def print(self):
        i = 1
        for server in self.servers:
            print("Server : "+str(i))
            server.print()
            i += 1
    def get_average_idle_time(self):
        idle_time = 0
        for server in self.servers:
            idle_time += server.idle_time
        return idle_time / self.server_num

    def get_average_busy_time(self):
        busy_time = 0
        for server in self.servers:
            busy_time += server.execution_time
        return busy_time / self.server_num

def generate_requests(num_request,server_frequency):
    requests = []
    for i in range(num_request):
        r = Request(server_frequency)
        requests.append(r)
    return requests

def show_details():
    os.system("clear")
    print("Average Idle Time : ", server_pool.get_average_idle_time())
    print("Average Busy Time : ", server_pool.get_average_busy_time())
    total_time = server_pool.get_average_idle_time() + server_pool.get_average_busy_time()
    percent_idle_time = server_pool.get_average_idle_time() * 100 / total_time
    percent_busy_time = server_pool.get_average_busy_time() * 100 / total_time
    print("Idle : ", percent_idle_time, "%")
    print("Busy : ", percent_busy_time, "%")

TOTAL_SERVERS = 10
MAX_GLOBAL_TIME = 9999
MAX_READY_QUEUE = 10
total_power = 2000
SIMULATION_ID = input('Enter SIMULATION ID (use same ID for reproducibility) : ');
random.seed(SIMULATION_ID)
for i in range(1,TOTAL_SERVERS+1):
    os.system("clear")
    print("Starting Simulation for",i,"Servers")
    prev_arrival_time = 0
    global_time = 0
    num_servers = i
    server_pool = ServerPool(num_servers, total_power)
    UNIT_TIME = 1/server_pool.server_frequency
    print("Number of servers : ",server_pool.server_num)
    print("Server Frequency : ",server_pool.server_frequency,"Ghz")
    print("Server Power : ",server_pool.server_power,"Watts")
    input("Press Enter to continue..")
    print(num_servers*100,"request generated...")
    requests = generate_requests(num_servers*100,server_pool.server_frequency)
    server_pool.receive_requests(requests)
    print("Simulation is running")
    success = False
    while True:
        server_pool.update_servers()
        if server_pool.are_all_servers_busy():
            break
        global_time += UNIT_TIME
        if server_pool.is_waiting_queues_empty():
            print(num_servers * 100, "request generated...")
            requests = generate_requests(num_servers * 100, server_pool.server_frequency)
            server_pool.receive_requests(requests)
            show_details()
        show_details()
        if global_time >= MAX_GLOBAL_TIME:
            print("Simulation passed system is stable with ", server_pool.server_num, "Servers ON")
            success = True
            break;
    print("Global Time : ",global_time)
    if not success:
        print("Congestion is too much try to Switch ON some more Servers")
    input("Press enter to continue")


