import sys
import os

if len(sys.argv) != 2:
    print("usage: python command.py <file_name>")
    sys.exit(1)
    
file_name = sys.argv[1]
if os.path.exists(file_name):
    print(f"The file {file_name} exists")
else:
    print(f"The file {file_name} does not exists")
