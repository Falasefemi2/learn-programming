import weakref

class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self) -> str:
        return f"MyClass{self.name}"
    
obj = MyClass("Example")

weak_ref = weakref.ref(obj)

print("Weak reference:", weak_ref())
print("Is the weak reference alive?", weak_ref() is not None)

del obj

print("Weak reference after deletion:", weak_ref())
print("Is the weak reference alive?", weak_ref() is not None)
