from pickle import TRUE


class Engine:
    def __init__(self):
        self.__enabled = False

    def start_engine(self):
        self.__enabled = True

    def is_enabled(self):
        return self.__enabled
