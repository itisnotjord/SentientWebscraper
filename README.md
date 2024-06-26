# SentientWebscraper

## Overview

SentientWebscraper is a powerful tool designed to scrape cybersecurity news from multiple sources and perform sentiment analysis using a Huggingface AI model. This project leverages `python`, `beautifulsoup4`, and `huggingface transformers` for the back-end, with `streamlit` for the front-end.

## Features

- **Web Scraping:** Currently supports scraping from:
  - [BleepingComputer](https://www.bleepingcomputer.com/)
  - [Cybersecurity News](https://cybersecuritynews.com/)
- **Sentiment Analysis:** Utilizes [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) for analyzing the sentiment of the news articles.
- **Customization:** Easily add new scraping sources by modifying `CollatingNews.py`.

## Getting Started

### Prerequisites

- Docker
- Python 3.x

### Build and Run Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-repo/sentientwebscraper.git
    cd sentientwebscraper
    ```

2. **Build the Docker image:**

    Update the port specification in the Dockerfile if necessary.

    ```sh
    docker build -t my-app .
    ```

3. **Run the Docker container:**

    Replace `[port]` and `[directory]` with your desired port and directory.

    ```sh
    docker run -p [port]:[port] -v [directory]:/app my-app
    ```

## Adding New Scraping Sources

To add a new website for scraping, simply add the respective scraping logic to `CollatingNews.py`. Follow the existing structure for guidance.

## Credits

- Sentiment Analysis AI Model: [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert)

