from playwright.sync_api import sync_playwright
import requests, json


def scrape_tds_site():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://tds.s-anand.net/#/2025-01/",
                  wait_until="networkidle")
        content = page.content()
        browser.close()
    return content


def scrape_discourse():
    import os
    headers = {"Cookie": f"_t={os.environ['DISCOURSE_TOKEN']}"}
    url = "https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34"
    r = requests.get(url, headers=headers)
    if r.ok:
        return r.json()
    return {}


def save_data():
    course_data = scrape_tds_site()
    discourse_data = scrape_discourse()

    with open("tds_data.json", "w") as f:
        json.dump({
            "tds_course": course_data,
            "discourse": discourse_data
        },
                  f,
                  indent=2)


save_data()
