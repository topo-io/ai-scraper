from pathlib import Path
from typing import List

from services.scraper import ScrapingResult


async def load_domains(path: Path, limit: int) -> List[str]:
    domains: list[str] = []
    index = 0
    with path.open() as file:
        for line in file:
            domain = line.strip()
            if not domain:
                continue
            domains.append(domain)
            index += 1
            if index >= limit:
                break

    return domains


def display_result(result: ScrapingResult):
    if result.success and result.data:
        print(f"✅  {result.url} -> {result.data.pricing}")
    else:
        print(f"❌  {result.url} -> {result.error}")
