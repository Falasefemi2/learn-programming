import os

# 1. os.name
# Returns the name of the operating system.
# 'posix' for Unix/Linux/Mac, 'nt' for Windows.
print(f"Operating system name: {os.name}")

# 2. os.getcwd()
# Returns the current working directory.
print(f"Current working directory: {os.getcwd()}")

# 3. os.listdir()
# Lists all files and directories in the specified path (or current directory if no path is given).
print(f"Files and directories: {os.listdir()}")

# 4. os.mkdir() and os.makedirs()
# mkdir(path): Creates a single directory.
# makedirs(path): Creates intermediate directories if needed.
# Create a single directory
# os.mkdir("example_dir")

# Create nested directories
# os.makedirs("nested_dir/level1/level2")

# 5. os.remove() and os.rmdir()
# remove(path): Deletes a file.
# rmdir(path): Deletes an empty directory.

# Remove a file
os.remove("example.txt")

# Remove an empty directory
os.rmdir("example_dir")

# 6. os.rename()
# Renames or moves a file or directory.
# Rename a file or directory
os.rename("old_name.txt", "new_name.txt")


# 7. Environment Variables
# Access or set environment variables using os.environ.
# Get an environment variable
print(f"PATH: {os.environ.get('PATH')}")

# Set an environment variable
os.environ['MY_VAR'] = 'Python is awesome!'
print(f"MY_VAR: {os.environ.get('MY_VAR')}")


os.mkdir("text_dir")
os.listdir()
os. makedirs("project/data/logs")
os.rename("test_dir", "example_dir")
os.environ["my_env"] = "12233"

# Create a new directory named "my_project"
os.mkdir("my_project")
print("Directory 'my_project' created.")

# Rename the directory to "completed_project"
os.rename("my_project", "completed_project")
print("Directory renamed to 'completed_project'.")

# Set an environment variable PROJECT_STATUS to "Done"
os.environ["PROJECT_STATUS"] = "Done"
print("Environment variable PROJECT_STATUS set to:", os.environ["PROJECT_STATUS"])

# Check if a file named "README.md" exists in the directory
file_exists = os.path.exists("README.md")
print("Does 'README.md' exist?", file_exists)
