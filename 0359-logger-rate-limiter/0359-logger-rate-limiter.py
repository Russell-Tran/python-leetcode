class Logger:

    def __init__(self):
        self.storage = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.storage:
            self.storage[message] = timestamp
            return True
        
        if timestamp >= self.storage[message] + 10:
            self.storage[message] = timestamp
            return True
        
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)