import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # Get and print the actual title of the page.
    title = page.title()  
    print("Page title is:", title)

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_checkbox(page: Page):
    page.goto("https://playwright.dev/python/docs/api/class-locator#locator-check")
    checkbox = page.locator('//input[@type="checkbox" and @name="pet2"]')
    checkbox.check()

