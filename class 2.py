class car ():
    def __init__(self, sepeed, color, nitrospeed, model):
        self.sepeed=sepeed
        self.color=color
        self.nitrospeed=nitrospeed
        self.model=model


    def info(self) :
        print("sepeed",self.sepeed,"color",self.color,"nitrospee",self.nitrospeed,"model",self.model)


BMW = car (300,"noir",'oui',2023)
BMW.info()


