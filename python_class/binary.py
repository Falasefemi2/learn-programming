import struct
import pickle

binary_data = struct.pack('i f s', 42, 3.14, b'Python')
print(f"Packed Data: {binary_data}")

unpacked_data = struct.unpack('i f s', binary_data)
print(f"Unpacked Data: {unpacked_data}")

data = {'name': 'Python', 'version': 3.11, 'features': ['easy', 'powerful', 'dynamic']}

with open('data.pkl', 'wb') as file:
    pickle.dump(data,file)
    
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(f"Loaded Data: {loaded_data}")


person = struct.pack("femi", 24, 3.14)
print(f"Person data: {person}")


# Define data
name = b"femi"  # Strings need to be bytes
age = 24        # Integer
height = 3.14   # Float

# Pack the data into a binary format
# Format string: 4s for a 4-byte string, i for an integer, f for a float
person = struct.pack("4sif", name, age, height)
print(f"Person data (binary): {person}")

# Unpack the binary data back into Python objects
unpacked_person = struct.unpack("4sif", person)
print(f"Unpacked data: {unpacked_person}")

# Decode the string from bytes
decoded_name = unpacked_person[0].decode('utf-8')
print(f"Decoded Name: {decoded_name}, Age: {unpacked_person[1]}, Height: {unpacked_person[2]}")
