class EventHandler:
    before = []
    after = []

    def __init__(self, x):
        self.x = x

    def execute(self):
        print("Start Execute -> do before")
        for callback in EventHandler.before:
            callback(self)
        print("Execute")
        self.x = 2*self.x
        print("Do after")
        for callback in EventHandler.after:
            callback(self)
        print("Finish")
        return self.x

    @staticmethod
    def registerBefore(callback):
        EventHandler.before.append(callback)
    
    @staticmethod
    def registerAfter(callback):
        EventHandler.after.append(callback)

class Injection:
    def __init__(self, y):
        self.y = y
        self.register()
    
    def register(self):
        EventHandler.registerBefore(self.doBefore)
        EventHandler.registerAfter(self.doAfter)
    
    def doBefore(self, handler):
        print(f'Injection.before.1 {handler.x}')
        handler.x = handler.x + self.y
        print(f'Injection.before.2 {handler.x}')
    
    def doAfter(self, handler):
        print(f'Injection.after.1 {handler.x}')
        handler.x = (handler.x - self.y)/2
        print(f'Injection.after.2 {handler.x}')

@EventHandler.registerBefore
def increase(handler):
    print(f"Increase.1 {handler.x}")
    handler.x = handler.x + 1
    print(f"Increase.2 {handler.x}")

handler = EventHandler(10.0)
injection = Injection(2.0)
print(handler.execute())

print(20*'=')
injection.y = 4
print(handler.execute())

otherHandler = EventHandler(20.0)
print(20*'=')
print(otherHandler.execute())
