import requests

# Set the API endpoint URL
url = "https://your-splunk-instance.com:8089/services/search/jobs/export"

# Set the request headers and parameters
headers = {
    "Authorization": "Splunk <your-token>",
    "Content-Type": "application/x-www-form-urlencoded"
}
params = {
    "search": "search index=main | head 10",
    "output_mode": "json"
}

# Make the API call
response = requests.get(url, headers=headers, params=params)

# Print the response content
print(response.content)
