import asyncio
from pathlib import Path

from services.scraper import ScraperService
from utils import display_result, load_domains

IMPORT_LIMIT = 50
DOMAIN_LIST_PATH = Path("data", "domains.csv")


async def main():
    domains = await load_domains(DOMAIN_LIST_PATH, IMPORT_LIMIT)
    print(f"Loaded {len(domains)} domains\n\n")
    scraper = ScraperService()

    # TODO: update this
    for domain in domains:
        result = scraper.scrape_url(domain)
        display_result(result)


if __name__ == "__main__":
    asyncio.run(main())
