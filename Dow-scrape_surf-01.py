# import dependencies
import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

# import chrome browser for MS Windows
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# scrape the Costa Rica surfing site
def scrape():
    browser = init_browser()
    surf_data = {}

    url = "https://www.surfline.com/surf-reports-forecasts-cams/costa-rica/3624060"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    surf_data["location"] = soup.find_all("h3", class_="sl-spot-details__name")
    surf_data["quiver_surf_height"] = soup.find_all("span", class_="quiver-surf-height")
    surf_data["URL"] = soup.find_all("a", class_="sl-cam-list-link", href=True)

    for x in range(len(surf_data["location"])):
        new_url = "https://www.surfline.com" + surf_data["URL"][x]["href"]
        browser.visit(new_url)

        # Still need to collect Air Temp and Water Temp
        surf_location = {
        "location" = surf_data["location"][x].get_text(),
        }

        # NOTE -- Jacob helped me with much of the above but the "surf_location" above, but looking at this now, 
        # I am not following how to create a dictionary the necessary dictonary  

        water_low = soup.find_all(id="data-reactid").get_text(),         



        # Add individual dictionary to mongo





scrape()