class DatabaseMapper(dict):
    def __init__(self, default):
        self.cache = {'default': default}

    def __getitem__(self, item):
        if item not in self.cache:
            self.cache[item] = {
                **self.cache['default'],
                'USER': item,
            }
        return self.cache[item]

    def __contains__(self, item):
        return True
