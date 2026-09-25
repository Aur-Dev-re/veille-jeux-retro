import re
from typing import Dict, Optional
from bs4 import BeautifulSoup
import requests

from .base import BaseScraper

class EBayScraper(BaseScraper):
    def __init__(self, locale: str = "fr"):
        super().__init__(locale)
        self.base_url = f"https://www.ebay.{self.locale}"
        self.currency_map = {"es": "EUR", "fr": "EUR", "de": "EUR", "us": "USD"}

    def _parse_price(self, price_str: str) -> float:
        """Parse price string with locale-specific formatting (e.g., '59,00 €' for ES)."""
        price_str = price_str.replace(",", ".").replace("€", "").strip()
        return float(price_str)

    def _validate_keywords(self, listing: Dict) -> bool:
        """Check if listing matches search keywords (case-insensitive)."""
        keywords = self.config.get("keywords", [])
        return all(keyword.lower() in listing["title"].lower() for keyword in keywords)

    def scrape(self, query: str) -> Dict:
        """Scrape eBay listings for a given query, supporting multiple locales."""
        search_url = f"{self.base_url}/sch/i.html?_nkw={query.replace(' ', '+')}"
        response = requests.get(search_url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        listings = []
        for item in soup.select("#srp-river-results li"):
            title = item.select_one("h3.s-item__title")
            if not title:
                continue

            title_text = title.get_text(strip=True)
            url = self.base_url + item.select_one("a.s-item__link")["href"]
            price_str = item.select_one(".s-item__price")
            price = self._parse_price(price_str.get_text(strip=True)) if price_str else None

            listings.append({
                "title": title_text,
                "url": url,
                "price": price,
                "currency": self.currency_map.get(self.locale, "EUR"),
                "locale": self.locale
            })

        return {
            "query": query,
            "listings": listings,
            "marketplace": self.locale.upper()
        }