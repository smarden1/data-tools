

class PercentageGreaterThanOne(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Cannot have a percentage value greater than 1.0 -- current percentage value is %s"%(self.value)
