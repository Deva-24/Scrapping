# Web Scraping Project using Python and Selenium

## Project Overview
This project is a web scraper that uses **Python Selenium** to extract product details such as **name**, **price**, **rating**, and **URL** from Amazon. The scraped data is saved into a CSV file for further analysis.

---

## Features
- Scrapes product data from multiple pages.
- Extracts product names, prices, ratings, and product links.
- Saves the data into a CSV file.
- Includes exception handling for missing data or errors.
- User-friendly interface with manual input.

---

## Prerequisites
Ensure you have the following installed:
- **Python** (>= 3.7)
- **Selenium**
- **Google Chrome**
- **ChromeDriver** (Matching the Chrome browser version)

### Install Required Packages
```bash
pip install selenium pandas
```

### Download ChromeDriver
Download ChromeDriver from the official website: [ChromeDriver](https://sites.google.com/chromium.org/driver/) and ensure it's in your system's PATH.

---

## Project Structure
```
Scrapping/
│
├── Scrap.py
├── products.csv
└── README.md
```

---

## How to Run
1. Clone this repository using Git:
    ```bash
    git clone https://github.com/Deva-24/Scrapping.git
    cd Scrapping
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the scraper:
    ```bash
    python Scrap.py
    ```

4. Enter the product you want to search for when prompted.
5. Follow on-screen instructions to scrape the next pages.
6. The extracted data will be saved to `products.csv`.

---

## Example Output
| Product Name                   | Price       | Rating       | URL                                      |
|---------------------------------|-------------|--------------|----------------------------------------|
| HP Pavilion 15 Laptop           | $679.00     | 4.5 out of 5 | https://www.amazon.com/example-link    |
| Dell XPS 13                     | $999.99     | 4.7 out of 5 | https://www.amazon.com/example-link    |
| Apple MacBook Air M2            | $1,199.00   | 4.8 out of 5 | https://www.amazon.com/example-link    |

---

## Troubleshooting
- **If Chrome doesn't open:**
  - Ensure ChromeDriver is installed and matches the Chrome browser version.
  - Check that ChromeDriver is accessible in your system's PATH.
- **If Amazon blocks your scraper:**
  - Use a VPN or proxy.
  - Introduce a small delay with `time.sleep(5)`.
- **If data is missing:**
  - Amazon may change its HTML. Update the XPath selectors if necessary.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

---

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request.

---

## Contact
For any questions, feel free to reach out to [Deva-24](https://github.com/Deva-24).

