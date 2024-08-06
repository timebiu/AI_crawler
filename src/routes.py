from crawlee.basic_crawler import Router
from crawlee.playwright_crawler import PlaywrightCrawlingContext

router = Router[PlaywrightCrawlingContext]()


@router.default_handler
async def request_handler(context: PlaywrightCrawlingContext) -> None:
    context.log.info(f'Processing {context.request.url}')

    # Wait for the category cards to render on the page. This ensures that
    # the elements we want to interact with are present in the DOM.
    await context.page.wait_for_selector('.title')

    # Enqueue links found within elements that match the specified selector.
    # These links will be added to the crawling queue with the label CATEGORY.
    await context.enqueue_links(
        selector='.title',
        label='CATEGORY',
    )


# @router.handler('CATEGORY')
# async def category_handler(context: PlaywrightCrawlingContext) -> None:
#     # This replaces the context.request.label == CATEGORY branch of the if-clause.
#     context.log.info(f'category_handler is processing {context.request.url}')
#
#     await context.page.wait_for_selector('.product-item > a')
#
#     await context.enqueue_links(
#         selector='.product-item > a',
#         label='DETAIL',
#     )
#
#     next_button = await context.page.query_selector('a.pagination__next')
#
#     if next_button:
#         await context.enqueue_links(
#             selector='a.pagination__next',
#             label='CATEGORY',
#         )
#
#
# @router.handler('DETAIL')
# async def detail_handler(context: PlaywrightCrawlingContext) -> None:
#     # This replaces the context.request.label == DETAIL branch of the if-clause.
#     context.log.info(f'detail_handler is processing {context.request.url}')
#
#     url_part = context.request.url.split('/').pop()
#     manufacturer = url_part.split('-')[0]
#
#     title = await context.page.locator('.product-meta h1').text_content()
#
#     sku = await context.page.locator('span.product-meta__sku-number').text_content()
#
#     price_element = context.page.locator('span.price', has_text='$').first
#     current_price_string = await price_element.text_content() or ''
#     raw_price = current_price_string.split('$')[1]
#     price = float(raw_price.replace(',', ''))
#
#     in_stock_element = context.page.locator(
#         selector='span.product-form__inventory',
#         has_text='In stock',
#     ).first
#     in_stock = await in_stock_element.count() > 0
#
#     data = {
#         'manufacturer': manufacturer,
#         'title': title,
#         'sku': sku,
#         'price': price,
#         'in_stock': in_stock,
#     }

    # await context.push_data(data)