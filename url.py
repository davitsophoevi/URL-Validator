import os
import sys
import asyncio
import aiohttp
from colorama import init, Fore

# Initialize colorama
init()
sys.stdout.reconfigure(encoding='utf-8')

# Function to read endpoints from a text file
def read_endpoints(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

async def check_page_exists(base_url, endpoints):
    results = {}
    async with aiohttp.ClientSession() as session:
        tasks = []
        for endpoint in endpoints:
            full_url = f"{base_url.rstrip('/')}{endpoint}"
            tasks.append(check_status(session, full_url, endpoint))
        responses = await asyncio.gather(*tasks)
        for endpoint, result in responses:
            results[endpoint] = result
    return results

async def check_status(session, url, endpoint):
    try:
        async with session.head(url, allow_redirects=True) as response:
            # If the status is 200 and the URL exists, print that it exists
            if response.status == 200 and str(response.url) == url:
                return endpoint, "Exists"
            else:
                return endpoint, f"Does not exist or error (final URL: {response.url})"
    except Exception as e:
        return endpoint, f"Error: {e}"

# Usage
async def main():
    base_url = "https://example.com/"
    # Read endpoints from the text file
    endpoints = read_endpoints("endpoints.txt")
    results = await check_page_exists(base_url, endpoints)
    
    print("Results:")
    for endpoint, status in results.items():
        if status == "Exists":            
            print(f"{Fore.GREEN}{status}: {base_url + endpoint.lstrip('/')}") 



# Run the asynchronous function
asyncio.run(main())
