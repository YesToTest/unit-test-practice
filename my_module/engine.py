class Engine:
    def __init__(self):
        self.enabled = None

    def set_enable(self, enabled):
        self.enabled = enabled

    def start_engine(self):
        if self.enabled:
            print("Run runnnn the engine is working")
            return True
