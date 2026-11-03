# AI Stock Assistant 📈

**Personal Project | Work in Progress**

**Tech Stack:** Python · Pandas · REST APIs · Alpha Vantage · yfinance · PostgreSQL · SQLAlchemy

## Overview

AI Stock Assistant is a personal hobby project exploring how financial market data, backend development, and artificial intelligence can be combined into an intelligent stock research assistant.

The project currently focuses on **retrieving stock market data, filtering equities based on a user's budget, processing API responses, and storing search results in a relational database**.

My long-term goal is to develop an AI-powered assistant capable of combining stock market information, financial news, and LLM-based analysis to help users explore potential investment opportunities.

The project is being developed incrementally as I expand my practical experience with **Python, API integrations, databases, backend engineering, and LLM applications**.

> **Project Status:** Early development. Market data retrieval, initial stock screening, data processing, and database integration have been implemented. AI-based analysis and the user-facing application are planned.

## Project Objectives

The project aims to:

1. Retrieve financial data through external APIs.
2. Search and filter equities based on user-defined criteria.
3. Process and structure financial data using Python and Pandas.
4. Store stock search requests and results in a PostgreSQL database.
5. Integrate LLMs for financial information analysis and summarization.
6. Eventually provide access through an API-based application.

## Current Implementation

### 1. Financial Data Retrieval

The project explores two approaches to retrieving stock information.

**Alpha Vantage API**

The initial implementation uses the Alpha Vantage `GLOBAL_QUOTE` endpoint to retrieve stock quotes for a predefined selection of German-market equities.

It includes:

- HTTP requests to an external financial data API.
- JSON response processing.
- Conversion of API results into Pandas DataFrames.
- Data cleaning and column standardization.
- Exporting stock information to CSV.

**Yahoo Finance (`yfinance`)**

A second implementation explores broader stock screening using the `yfinance` library.

It includes:

- Filtering equities by exchange and price.
- Retrieving stock information through `EquityQuery`.
- Processing up to 250 results per screening request.
- Selecting relevant stock attributes.
- Standardizing column names and data types.
- Preparing structured datasets for storage and further analysis.

### 2. Budget-Based Stock Screening

The application accepts a user-defined budget in EUR and uses it to identify equities within the specified price range.

The implementation explores:

- Validating numeric user input.
- Applying price-based filters.
- Handling cases where no suitable equities are found.
- Creating structured search results.

The screening functionality is currently script-based.

### 3. Data Processing

Pandas is used to transform raw financial data into structured datasets.

The processing steps include:

- Extracting relevant fields from API responses.
- Renaming and standardizing columns.
- Handling missing values.
- Processing timestamps.
- Exporting results into CSV files.

### 4. Database Integration

The project includes an initial PostgreSQL integration using SQLAlchemy and `psycopg`.

The database component is designed to:

- Record stock-screening requests.
- Associate requests with unique identifiers.
- Store user-defined budget values.
- Save the corresponding stock search results.

Environment variables are used to configure the database connection.

## Current Workflow

The application follows a simple data-processing pipeline:

1. **User Input:** The user enters an investment budget.
2. **Stock Screening:** A financial data provider is queried using the specified criteria.
3. **Data Extraction:** Relevant equity information is retrieved.
4. **Data Transformation:** The response is converted into a structured Pandas DataFrame.
5. **Data Export:** The processed stock data is saved to a CSV file.
6. **Database Persistence:** Search information and the associated results are passed to the PostgreSQL persistence layer.

This workflow provides the foundation for future AI-powered analysis.

## Repository Structure

| File / Directory | Description |
|---|---|
| `get_stock_data.py` | Initial Alpha Vantage stock retrieval and budget filtering |
| `get_yfinance_data.py` | Yahoo Finance equity screening, data transformation, and database integration |
| `database.py` | PostgreSQL connection and SQLAlchemy-based data persistence |
| `data/` | CSV datasets and exported stock search results |
| `.gitignore` | Git exclusion rules |
| `README.md` | Project documentation |

## Technologies

**Programming & Data Processing**
- Python
- Pandas
- JSON
- CSV

**Financial Data**
- Alpha Vantage API
- yfinance

**Database**
- PostgreSQL
- SQLAlchemy
- psycopg

**Development Concepts**
- REST API integration
- Environment variables
- Data transformation
- Relational data persistence
- User input validation

## Running the Project

This repository is currently a collection of development scripts rather than a packaged application.

The scripts use several Python libraries, including `pandas`, `requests`, `yfinance`, `python-dotenv`, `sqlalchemy`, and `psycopg`.

Before running the code, configure the relevant environment variables:

- `API_KEY` — Alpha Vantage API key.
- `DB_URL` — PostgreSQL connection URL.

The PostgreSQL database must also contain the tables expected by the persistence script.

The project does not yet provide a fully tested, automated setup process. Configuration and database initialization are being improved as development continues.

## Development Roadmap

### Phase 1 — Financial Data Retrieval and Processing

- [x] Integrate Alpha Vantage API.
- [x] Retrieve market data for selected equities.
- [x] Convert JSON responses into Pandas DataFrames.
- [x] Implement initial budget-based screening.
- [x] Export stock data to CSV files.

### Phase 2 — Expanded Screening and Data Storage

- [x] Explore `yfinance` equity screening.
- [x] Implement filtering by exchange and price.
- [x] Create unique search-request identifiers.
- [x] Implement an initial PostgreSQL persistence layer.
- [ ] Improve error handling and input validation.
- [ ] Add automated tests.
- [ ] Improve database initialization and reproducibility.

### Phase 3 — Backend and AI Integration

- [ ] Develop a REST API using FastAPI.
- [ ] Extend financial data collection.
- [ ] Integrate financial news retrieval.
- [ ] Add an LLM for stock-related information analysis and summarization.
- [ ] Implement structured AI-generated responses.

### Phase 4 — Application and Deployment

- [ ] Build a simple user interface.
- [ ] Add automated data-refresh workflows.
- [ ] Containerize the application with Docker.
- [ ] Deploy the application.
- [ ] Introduce logging, monitoring, and evaluation.

## Learning Objectives

This project is part of my ongoing transition toward AI and backend engineering.

It provides a practical environment for developing skills in:

- Integrating external APIs.
- Working with JSON and structured data.
- Building Python data-processing pipelines.
- Querying and storing data in relational databases.
- Designing backend application components.
- Integrating LLMs into data-driven applications.
- Developing an application incrementally from prototype to deployment.

## Disclaimer

This is an educational and experimental project.

The application is not intended to provide professional financial advice, and its current implementation does not generate AI-powered investment recommendations or execute trades.

## Author

**Melisa Altinyelek** — [GitHub Profile](https://github.com/melisaaltinyelek)
