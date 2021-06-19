class Lector:

    def __init__(self):
        self.counter = 0
        self.orders = []

    def increase_counter(self):
        self.counter = self.counter + 1

    def read_file(self):
        filename = 'input.txt'
        with open(filename) as f_obj:
            for line in f_obj:
                self.orders.append(line.rstrip())

    def obtain_order(self):
        if self.counter < len(self.orders):
            result = self.orders[self.counter]
            self.increase_counter()
            print(result)
            return result
        else:
            return "-1"
