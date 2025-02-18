from random import randint

from pydantic import BaseModel


class ScrapingData(BaseModel):
    company_name: str
    company_description: str
    business_type: str
    pricing: str


class ScrapingResult(BaseModel):
    url: str
    success: bool
    data: ScrapingData | None = None
    error: str | None = None


class ScraperService:
    def scrape_url(self, url: str) -> ScrapingResult:
        fail = randint(1, 10) == 1
        if fail:
            return ScrapingResult(url=url, success=False, error="Failed to scrape")

        return ScrapingResult(
            url=url,
            success=True,
            data=ScrapingData(
                company_name="Example Company",
                company_description="Example description",
                business_type="Example business type",
                pricing="Example pricing",
            ),
        )
