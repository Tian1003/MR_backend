class BaseDto():
    def serialize(self):
        serialized_data = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                serialized_data[key] = value
        return serialized_data
