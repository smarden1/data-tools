import random
from datatools.FrequencyBase import FrequencyBase

class BootStrap(object):

    def __init__(self, frequency, *args, **kwargs):
        if not issubclass(type(frequency), FrequencyBase):
            raise TypeError("Frequency must be a subclass of FrequencyBase")

        self.sample_size = int(kwargs.get("sample_size", frequency.n))
        self.resample_count = int(kwargs.get("resample_count", frequency.n))
        self.functions = args or ["mean"]
        self.ci = float(kwargs.get("ci", .025))


    def run(self):
        #first make the streaming percentile
        pass
