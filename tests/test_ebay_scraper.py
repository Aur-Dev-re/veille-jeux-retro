import pytest
from unittest.mock import patch
from scraper.ebay import EBayScraper

@pytest.fixture
def mock_es_response():
    return """
    <html>...</html>
    <h3 class="s-item__title">SEGA MEGADRIVE - KING'S BOUNTY : The conqueror's quest</h3>
    <span class="s-item__price">59,00 €</span>
    <a class="s-item__link" href="/itm/407244805355">...</a>
    """

def test_es_scraper_price_parsing():
    scraper = EBayScraper(locale="es")
    assert scraper._parse_price("59,00 €") == 59.0

def test_es_scraper_validation(mock_es_response):
    scraper = EBayScraper(locale="es")
    scraper.config = {"keywords": ["Mega Drive"]}

    with patch("requests.get") as mock_get:
        mock_get.return_value.text = mock_es_response
        result = scraper.scrape("Mega Drive")

    assert len(result["listings"]) == 1
    listing = result["listings"][0]
    assert listing["title"] == "SEGA MEGADRIVE - KING'S BOUNTY : The conqueror's quest"
    assert listing["price"] == 59.0
    assert listing["currency"] == "EUR"
    assert scraper._validate_keywords(listing) is True