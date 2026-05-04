class BaseStrategy:
    def process(self, page, doc, index):
        raise NotImplementedError