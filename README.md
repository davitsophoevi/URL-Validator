# URL Availability Checker

This Python script asynchronously checks the availability of specific pages (endpoints) on a given website. It reads the list of endpoints from a text file, sends requests to check each URL, and prints the result with color-coded output to indicate if a page exists or if there was an error.

## Features:
- **Asynchronous requests**: Fast and efficient checking of multiple endpoints.
- **Color-coded output**: Green for existing pages and error messages for inaccessible pages.
- **Configurable base URL**: Can be customized for any website.

## Requirements:
- Python 3.6 or higher
- `aiohttp` (for asynchronous HTTP requests)
- `colorama` (for color-coded output)

## Installation:
1. Clone the repository:
git clone https://github.com/davitsophoevi/URL-Validator.git
