# Execution and Output
# If you run the above code:

# GET Request:

# Fetches and prints the first 5 posts from the jsonplaceholder API.
# POST Request:

# Sends the payload to the API and prints the response confirming the data is sent.
# Filtered GET with Query Parameters:

# Retrieves comments for the postId 1 and displays the first 3.


import requests

# === GET Request ===
url = "https://jsonplaceholder.typicode.com/posts"

# Make a GET request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert the response to JSON
    print("=== GET Request Output (First 5 Posts) ===")
    for post in data[:5]:
        print(post)
else:
    print(f"GET request failed. Status code: {response.status_code}")

# === POST Request ===
payload = {
    "title": "API Tutorial",
    "body": "Learning to work with APIs in Python",
    "userId": 1
}

response_post = requests.post(url, json=payload)

if response_post.status_code == 201:  # 201 Created
    print("\n=== POST Request Output ===")
    print(response_post.json())
else:
    print(f"POST request failed. Status code: {response_post.status_code}")

# === Filtered GET with Query Parameters ===
url_comments = "https://jsonplaceholder.typicode.com/comments"
params = {"postId": 1}  # Filter by postId=1

response_filtered = requests.get(url_comments, params=params)

if response_filtered.status_code == 200:
    filtered_data = response_filtered.json()
    print("\n=== Filtered GET Request Output (First 3 Comments) ===")
    for comment in filtered_data[:3]:
        print({"name": comment["name"], "body": comment["body"]})
else:
    print(f"Filtered GET request failed. Status code: {response_filtered.status_code}")
