from .pages.product_page import ProductPage
import pytest


def link_compilator(excluded_link=None, number_of_links=10):
    base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    return [base + str(i) if i != excluded_link else pytest.param(base + str(i), marks=pytest.mark.xfail)
            for i in range(number_of_links)]


@pytest.mark.parametrize('link', link_compilator(7))
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_item_to_basket_notification()
    page.should_be_correct_price_of_product()
