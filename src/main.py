import asyncio

from crawlee.playwright_crawler import PlaywrightCrawler

from routes import router


async def main() -> None:
    crawler = PlaywrightCrawler(
        # Let's limit our crawls to make our tests shorter and safer.
        max_requests_per_crawl=50,
        # Provide our router instance to the crawler.
        request_handler=router,
    )

    await crawler.run(['https://www.163.com/dy/media/T1472562728078.html'])


if __name__ == '__main__':
    asyncio.run(main())