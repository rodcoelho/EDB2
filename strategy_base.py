from abc import ABCMeta, abstractmethod

class AbstractStrategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate_signals(self, event):
        raise NotImplementedError("Should implement calculate_signals()")

class Strategies(AbstractStrategy):
    def __init__(self, *strategies):
        self._lst_strategies = strategies

    def calculate_signals(self, event):
        for strategy in self._lst_strategies:
            strategy.calculate_signals(event)