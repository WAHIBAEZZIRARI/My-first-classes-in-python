class Mobile():
    def __init__(self, name, companyName, storage,  dualSim, support4K):

        self.name = name
        self.companyName = companyName
        self.storage = storage
        self.dualSim = dualSim
        self.support4K = support4K

    def info(self):
        
        print("The {} is produced by {} Company. It has {}GB storage capacity, and it {}supports dual SIM functionality. With {} support, it has a 4K display.".format(self.name, self.companyName, self.storage, self.dualSim, self.support4K))


mobile1 = Mobile("iPhone 15", "Apple", 256, "not", "yas")


mobile1.info()