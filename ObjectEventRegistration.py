class EventHandler:
    def __init__(self, x):
        self.x = x
        self.before = []
        self.after = []


    def execute(self):
        print("Start Execute -> do before")
        for callback in self.before:
            callback(self)
        print("Execute")
        self.x = 2*self.x
        print("Do after")
        for callback in self.after:
            callback(self)
        print("Finish")
        return self.x

    def registerBefore(self, callback):
        self.before.append(callback)
    
    def registerAfter(self, callback):
        self.after.append(callback)

class Injection:
    def __init__(self, y, handler):
        self.y = y
        self.handler = handler
        self.register()
    
    def register(self):
        self.handler.registerBefore(self.doBefore)
        self.handler.registerAfter(self.doAfter)
    
    def doBefore(self, handler):
        print(f'Injection.before.1 {handler.x}')
        handler.x = handler.x + self.y
        print(f'Injection.before.2 {handler.x}')
    
    def doAfter(self, handler):
        print(f'Injection.after.1 {handler.x}')
        handler.x = (handler.x - self.y)/2
        print(f'Injection.after.2 {handler.x}')


handler = EventHandler(10.0)

@handler.registerBefore
def increase(h):
    print(f"Increase.1 {h.x}")
    h.x = h.x + 1
    print(f"Increase.2 {h.x}")

injection = Injection(2.0, handler)
print(handler.execute())

print(20*'=')
injection.y = 4
print(handler.execute())

otherHandler = EventHandler(20.0)
print(20*'=')
print(otherHandler.execute())
