class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def queue_length(self):
        count = 0
        for _q in self.queue:
            count += 1
        return count
    
    def add_to_queue(self, person):
        self.queue.append(person)

    def clear_queue(self):
        self.queue.clear()