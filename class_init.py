class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("CPU is = ", self.cpu)
        print("RAM is = ", self.ram)


a = Computer('i5', '16GB')
b = Computer('i7', '8GB')

a.config()
b.config()