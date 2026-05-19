import urllib.request
import json
import urllib.error

def test_airport_code_api():
    url = "http://localhost:8000/api/airport/airport-code"
    
    print(f"Testing API endpoint: {url}")
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            status_code = response.getcode()
            print(f"Status Code: {status_code}")
            
            data = response.read()
            json_data = json.loads(data)
            
            print("Response Data:")
            print(json.dumps(json_data, indent=2, ensure_ascii=False))
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        print(e.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Connection Error: {e.reason}")
        print("Is the server running? Check docker-compose.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_airport_code_api()
