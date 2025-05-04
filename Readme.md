# 📚 **BookScraper** - A Professional Web Scraper for Book Data

**BookScraper** is a web scraping project built using **Scrapy** that extracts detailed information from [Books to Scrape](https://books.toscrape.com). This scraper collects key book data such as title, category, description, price, and availability, which can be outputted in a JSON format or saved to a PostgreSQL database.

---

## 🚀 **Key Features**

* **Comprehensive Scraping:** Scrapes all available books from [Books to Scrape](https://books.toscrape.com), a website listing a large collection of books.
* **Data Extraction:** Collects the following book details:

  * **Title**
  * **Category**
  * **Description**
  * **Price**
  * **Availability Count**
* **Output Formats:** Data can be saved in a `booksData.json` file (default). Optionally, data can also be stored in a **PostgreSQL** database.
* **Dynamic User-Agent Rotation:** The scraper uses dynamic user-agent rotation for each request to avoid being blocked or flagged by the website.

---

## 📂 **Project Structure**

```
BookScraper/
├── scrapy.cfg                    # Scrapy project configuration file
└── BookScraper/
    ├── __init__.py                # Marks the folder as a Python package
    ├── booksData.json             # Default output file for scraped data
    ├── items.py                   # Defines the data model for the scraped data
    ├── middlewares.py             # Custom middlewares for request handling
    ├── pipelines.py               # Data processing pipelines (including DB storage)
    ├── settings.py                # Configuration settings for Scrapy
    └── spiders/
        ├── __init__.py            # Marks the spiders folder as a Python package
        └── bookSpyder.py           # The main spider responsible for scraping
```

---

## ⚙️ **Installation Guide**

### 1. **Clone the Repository**

Start by cloning the repository to your local machine.

```bash
git clone https://github.com/yourusername/BookScraper.git
cd BookScraper
```

### 2. **Set Up a Virtual Environment** (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. **Install Dependencies**

Install the required libraries by running:

```bash
pip install -r requirements.txt
```

> **Note:** `requirements.txt` should contain the following dependencies:

```txt
scrapy
psycopg2-binary
fake-useragent
```

---

## 🕷 **Running the Spider**

### Run the Spider for JSON Output (Default)

To run the spider and store the scraped data in `booksData.json`, use:

```bash
scrapy crawl bookSpyder
```

This will initiate the spider, which will scrape the website and store the results in `booksData.json` located in your project directory.

### Run the Spider with PostgreSQL Integration (Optional)

1. **Enable the PostgreSQL Pipeline:**

To store the scraped data in a PostgreSQL database, open the `settings.py` file and uncomment the line for the `DBpipeline`:

```python
ITEM_PIPELINES = {
    "BookScraper.pipelines.DemobookscraperPipeline": 300,
    "BookScraper.pipelines.DBpipeline": 400,  # Uncomment to use DB pipeline
}
```

2. **Database Setup:**

Ensure you have a PostgreSQL database named `Scrapy` running, and update the credentials in `pipelines.py` under `DBpipeline` accordingly.

---

## 🧠 **How It Works**

1. **Start Crawling:** The spider begins crawling from the homepage of Books to Scrape.
2. **Follow Links:** It follows each book’s individual page for detailed data.
3. **Data Extraction:** Each book’s page is parsed using **CSS Selectors** and **XPath** to extract relevant details.
4. **Handle Pagination:** The spider automatically detects and follows pagination links to scrape multiple pages.
5. **Store Data:** The scraped data can be saved either in a **JSON** file or directly into a **PostgreSQL** database, depending on the configuration.
6. **Middleware:** Dynamic **User-Agent rotation** ensures that each request uses a different User-Agent header, helping to avoid detection and blocking.

---

## 🛠 **Optional Configuration: PostgreSQL Integration**

If you want to store the scraped data in a PostgreSQL database:

* Install `psycopg2` for PostgreSQL interaction:

```bash
pip install psycopg2-binary
```

* The database schema is automatically created during the first scrape. You can modify the database connection details in the `DBpipeline` class found in `pipelines.py`.

---

## 🛡 **Disclaimer**

* **Educational Purposes Only:** This project is intended for educational purposes. Please ensure that you follow the **robots.txt** rules and terms of service of any websites you scrape.
* **Respect for Website Policies:** Scraping websites without permission may violate their policies. Be mindful when using this project for real-world applications.

---

## 📬 **Contact & Contributing**

* If you have suggestions, issues, or contributions, feel free to open an issue or pull request.
* **Email:** [your.email@example.com](mailto:your.email@example.com)

---

## 📄 **License**

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for more details.

---

## 🌟 **Acknowledgements**

* **Scrapy:** The powerful and flexible web scraping framework used in this project. Visit [Scrapy Documentation](https://docs.scrapy.org/en/latest/) for more information.
* **PostgreSQL:** The relational database used for storing scraped data. Visit [PostgreSQL](https://www.postgresql.org/) for more information.

---

Thank you for checking out **BookScraper**! Happy scraping! 🚀
