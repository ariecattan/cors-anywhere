import requests
import time

url = "https://cors-anywhere-ajeo.onrender.com"

# Function to send a request to the website
def keep_alive():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully pinged {url} at {time.ctime()}")
        else:
            print(f"Failed to ping {url} at {time.ctime()} - Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error pinging {url} at {time.ctime()} - Error: {e}")

# Main loop to call the function every 2 minutes
if __name__ == "__main__":
    while True:
        keep_alive()
        time.sleep(120)  # Sleep for 120 seconds (2 minutes)


