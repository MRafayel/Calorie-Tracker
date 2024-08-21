# Web Scraping Health-Diet Data

This project is a web scraping script that retrieves nutritional data from the Health-Diet website. It collects product information such as calories, proteins, fats, and carbohydrates, and stores this data in CSV and JSON formats.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Dependencies](#dependencies)


## Installation

To run this script, you need to have Python installed along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install requests beautifulsoup4 lxml
```

## Usage
   1. Clone the repository or download the script.
   2. Ensure that the directory data/ exists in the same folder as the script.
   3. Modify the url and headers variables as needed in the code to point to the desired URL and headers.
   4. Run the script:

```bash
python your_script_name.py
```
The script will create index.html, all_categories_dict.json, and several CSV files containing the nutritional data in the data/ directory.
## Code Explanation
 **1. Fetching the HTML content:**
   - The script sends a GET request to the specified URL and retrieves the HTML content.

**2. Parsing the HTML:**
   - The HTML content is parsed using BeautifulSoup to extract product links and category names.
 
**3. Creating a Dictionary:**
     - A dictionary all_categories_dict is created to store product names and their corresponding links.

**4. Data Retrieval:**
   - For each category link, the script 
     - Fetches the HTML content. 
     - Checks for any alert messages (errors).
     - Extracts nutritional data and stores it in CSV and JSON formats.

**5. Data Storage:** 
   - The nutritional information is written to CSV files, with each file named according to the category and its corresponding index.
   - The script also saves product data in a JSON file for each category.

**6. Iteration:** 
   - The script iterates through each category, keeping track of the iteration count and printing progress messages.

**7. Delay:**
   - A random delay between requests is implemented to avoid overwhelming the server.

## Dependencies
 
- requests: For making HTTP requests.
 
- beautifulsoup4: For parsing HTML and XML documents.
  
- lxml: Required parser for BeautifulSoup.
  
- csv: For writing data to CSV files.
  
- json: For working with JSON data.
  
- random: To generate random delays between requests.
  
- time: For sleep functionality.