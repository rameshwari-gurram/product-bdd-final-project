"""Reusable Selenium step definitions for the product BDD feature."""

from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('I press the "{button}" button')
def step_press_button(context, button):
    context.browser.find_element(
        By.XPATH, f"//button[normalize-space()='{button}']"
    ).click()


@then('I should see "{text}" in the results')
def step_should_see_in_results(context, text):
    results = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, "search_results"))
    )
    WebDriverWait(context.browser, 10).until(
        lambda driver: text in driver.find_element(
            By.ID, "search_results"
        ).text
    )
    assert text in results.text, f"Expected {text!r} in results"


@then('I should not see "{text}" in the results')
def step_should_not_see_in_results(context, text):
    results = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, "search_results"))
    )
    assert text not in results.text, f"Did not expect {text!r} in results"


@then('I should see the message "{message}"')
def step_should_see_message(context, message):
    def matching_flash(driver):
        for element in driver.find_elements(By.CLASS_NAME, "flash"):
            if element.is_displayed() and message in element.text:
                return element
        return False

    element = WebDriverWait(context.browser, 10).until(matching_flash)
    assert message in element.text


# The feature also uses these project-specific steps:
# - visit Home Page
# - enter text in a named field
# - copy product ID and enter copied ID
# - clear form / clear all filters
# - select dropdown option
# - verify product field values
# - update product name
# Implement or retain these from the original course starter project.
