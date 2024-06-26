from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")


@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_result_page.hover_fav_icon()


@then('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_result_page.verify_fav_tooltip()


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    context.app.search_result_page.verify_search_results(expected_item)


@then('Verify that URL has {partial_url}')
def verify_search_page_url(context, partial_url):
    # context.app.base_page.verify_partial_url(partial_url)
    context.app.search_result_page.verify_partial_url(partial_url)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)



