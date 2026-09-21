from collections import deque

class ClimateQueue:
    def __init__(self):
        self.queue = deque()

    def add_challenge(self, event_name):
        self.queue.append(event_name)

    def process_hazard(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        print("Queue is empty!\n")
        

q = ClimateQueue()

q.add_challenge("Typhoon")
    # q.add_challenge("Flood")
q.add_challenge("Drought")

# q.process_hazard()
# q.process_hazard()
# q.process_hazard()
# q.process_hazard()\]'/[;./]

updateClimateQueue(list(q.queue))
print("Climate Queue (FIFO ready!)")
