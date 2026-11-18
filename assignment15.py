
import gc

# Check automatic garbage collection
print("Garbage collection enabled:", gc.isenabled())

# Disable automatic garbage collection
gc.disable()
print("Automatic garbage collection disabled")

# Create a class
class Student:
    pass

# Create circular references
s1 = Student()
s2 = Student()

s1.friend = s2
s2.friend = s1

print("Circular references created")

# Delete references
del s1
del s2

print("Objects deleted")

# Perform manual garbage collection
collected = gc.collect()

print("Objects collected manually:", collected)

# Display garbage collection status
print("Garbage collection enabled:", gc.isenabled())

# Enable automatic garbage collection again
gc.enable()

print("Automatic garbage collection enabled:", gc.isenabled())
