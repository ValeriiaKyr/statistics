# Job Scraper & Analysis
### Project Overview
This project combines web scraping and data analysis to extract, clean, and analyze job postings from the Polish job portal www.pracuj.pl. Specifically, it focuses on Python-related job offers and provides insights into market trends. The project processes data using Selenium, Pandas, and Matplotlib, making it easy to understand hiring trends in Poland.

### Features
#### Web Scraping:
Using Selenium, the program collects detailed information about Python-related job postings, including:

- Job title
- Company name
- Expected skills
- Job link
- Project details
- Experience level (e.g., Junior, Mid, Senior)
- Work mode (e.g., Remote, Hybrid, Office work)
- Salary range and frequency (monthly/yearly)
- City
- Preference for Ukrainian candidates

#### Data Cleaning & Translation:

Collected data is standardized to English for consistency.

#### Data Analysis:
The program provides valuable insights, such as:

- The number of companies inviting Ukrainian candidates.
- Cities in Poland with the most job postings.
- The most common work modes offered (Remote, Hybrid, Office work).
- The most in-demand experience levels.

#### Visualization:

Trends and statistics are visualized using Matplotlib, offering a clear overview of the job market.

### Installation

- Clone this repository:
```bash
git clone https://github.com/ValeriiaKyr/statistics
```
- Install the required Python packages:
```bash
pip install -r requirements.txt
```
- Go to the directory "scraping"
```bssh
cd scraping 
```

- Run the program for scraping and writing data and wait until the program is completely finished (this can take some time)
```bash
scrapy crawl job -O jobs.csv
```

