#queue.py
class Queue:
    def __init__(self):
        self.items = []

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

lineup = Queue()

lineup.add_rear("kevin_mitnick")
print(lineup.items)
lineup.add_rear("gary_mckinnon")
lineup.add_rear("jonathan_james")
print(lineup.items)
lineup.remove_front()
print(lineup.items)