# Orchestration Scripts

This directory contains the core scripts for orchestrating data scraping and posting workflows using Prefect.

## Scripts

### `api_tool.py`

This script provides tools for interacting with the Reddit API and processing the response data.

- **`ApiCaller` class:** Fetches data from a specified subreddit.
- **`ResponseNavigator` class:** Extracts and organizes specific data points from the API response, such as URLs, authors, titles, and votes.

### `orchestration_tools.py`

This script defines the Prefect tasks and flows for the data scraping and posting processes.

- **Tasks:**
    - `fetch_data`: Retrieves data from a subreddit using `ApiCaller`.
    - `fetch_urls`, `fetch_authors`, `fetch_titles`, `fetch_votes`: Extract specific information from the fetched data.
    - `summarize`: Aggregates the extracted data into a structured format.
    - `items_to_post`: Compares the scraped items with stored data to determine which items are new.
    - `post_items`: Posts the new items to a specified endpoint.

- **Flows:**
    - `scrape_flow`: Orchestrates the data fetching and processing tasks.
    - `post_flow`: Orchestrates the tasks for posting new data.

### `orchestration.py`

This is the main script for deploying and scheduling the Prefect flows.

- It serves the `scrape_flow` and `post_flow` with a CRON schedule to run every two hours.
- The `scrape_flow` is named `scraper-flow`.
- The `post_flow` is named `post-flow` and receives the output of the scrape flow.
