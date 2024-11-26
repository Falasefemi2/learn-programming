import gzip
import zipfile

# Compress a file
with open("example.txt", "w") as f:
    f.write("This is some sample text for compression!")

with open("example.txt", "rb") as f_in:
    with gzip.open("example.txt.gz", "wb") as f_out:
        f_out.writelines(f_in)
print("File compressed successfully!")

# Decompress the file
with gzip.open("example.txt.gz", "rb") as f_in:
    with open("example_decompressed.txt", "wb") as f_out:
        f_out.writelines(f_in)
print("File decompressed successfully!")


try:
    with zipfile.ZipFile('spam.zip', 'r') as myzip:
        with myzip.open('eggs.txt') as myfile:
            print(myfile.read().decode('utf-8'))
except FileNotFoundError:
    print("The zip file or the file inside does not exist!")


with open('sample.txt', 'w') as f:
    f.write("Hello, this is a sample file!")
    
with zipfile.ZipFile("my_archive.zip", 'w') as myzip:
    myzip.write('sample.txt')
    
print("Compressed sample.txt into my_archive.zip successfully!")

# Step 3: Extract and read the file from the zip
with zipfile.ZipFile('my_archive.zip', 'r') as myzip:
    with myzip.open('sample.txt') as myfile:
        print("Content of the file from zip:")
        print(myfile.read().decode('utf-8'))


# Step 1: Create and write a sample text file
with open('samples.txt', 'w') as file:
    file.write("text written")

# Step 2: Create a ZIP file and add the sample text file to it
with zipfile.ZipFile("mysample.zip", "w") as my_zip:
    my_zip.write("samples.txt")

# Step 3: Read the contents of the text file from the ZIP archive
with zipfile.ZipFile("mysample.zip", "r") as my_zip:
    with my_zip.open("samples.txt") as zFile:
        print(zFile.read().decode('utf-8'))
