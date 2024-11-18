import requests

# Example API endpoint for GET and POST
url = "https://jsonplaceholder.typicode.com/posts"

# --- GET Request ---
response = requests.get(url)

# Check if the GET request was successful
if response.status_code == 200:
    data = response.json()  # Convert the response to JSON
    print("GET Request Successful!")
    print("First 5 Posts:")
    print(data[:5])  # Print the first 5 posts
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# --- POST Request ---
payload = {
    "title": "API Tutorial",
    "body": "Learning to work with APIs in Python",
    "userId": 1
}

response = requests.post(url, json=payload)

# Check the response of the POST request
if response.status_code == 201:  # 201 Created
    print("\nPOST Request Successful!")
    print("Response:")
    print(response.json())  # Print the server's response
else:
    print(f"Failed to send data. Status code: {response.status_code}")

# --- Handling Query Parameters ---
url_comments = "https://jsonplaceholder.typicode.com/comments"
params = {"postId": 1}  # Query parameter to filter comments by post ID

response = requests.get(url_comments, params=params)

# Check if the filtered GET request was successful
if response.status_code == 200:
    data = response.json()
    print("\nFiltered Data (First 3 Comments):")
    for comment in data[:3]:  # Display only the first 3 comments
        print(f"{comment['name']}: {comment['body']}")
else:
    print("Failed to fetch filtered data.")
