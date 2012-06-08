import random
from datatools.FrequencyBase import FrequencyBase
from datatools.FrequencyArray import FrequencyArray
from datatools.FrequencyTable import FrequencyTable

class BootStrap(object):

    def __init__(self, frequency, *args, **kwargs):
        if not issubclass(type(frequency), FrequencyBase):
            raise TypeError("Frequency must be a subclass of FrequencyBase")

        self.sample_size = int(kwargs.get("sample_size", frequency.n))
        self.resample_count = int(kwargs.get("resample_count", frequency.n))
        self.ci = float(kwargs.get("ci", .025))

        self.functions = args or ["mean"]
        self.function_results = [FrequencyArray() for i in self.functions]

        self.frequency = frequency

        if kwargs.has_key("seed"):
            random.seed(kwargs.get("seed"))

    def run(self):
        for n in self.resample_count():
            for stats in self.run_sample_statistics():
                for i, s in enumerate(stats):
                    self.functions[i].add(s)

        # maybe print out graph here too
        return [self.confidence_interval(i) for i in self.functions]

    def confidence_interval(self, freq_array):
        return (freq_array.percentile(.5 - self.ci), freq_array.percentile(.5 + self.ci))

    def run_sample_statistics(self):
        moments = FrequencyTable() # add option to make this and streaming

        for i in range(self.sample_size):
            for j in self.random_with_replacement():
                moments.add(j)

        return map(lambda a: getattr(moments, a)(), self.functions)

    def random_with_replacement(self):
        yield random.choice(self.frequency.explode())