# Importing relevant dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import os
import csv

def scrape():

    # Defining a dictionary for all scraped data:
    scraped_mars_data = {}

# # NASA Mars News
    # URL of page to be scraped: NASA Mars News Site
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    html = requests.get(url).text

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    # Extracting the results we want (News Title)
    results_titles = soup.find_all('div', class_="content_title")

    # Extracting the results we want (Paragraph Text)
    results_paragraphs = soup.find_all('div', class_="rollover_description_inner")

    # Loop through returned results to extract the titles
    titles = []
    for result in results_titles:
        try:
            #title = result.find('a')
            titles.append(result.text.strip())        
            print(result.text.strip())        
            print('---------------------------------------------')
        except AttributeError as e:
            print(e)

    # Loop through returned results to extract the paragraphs
    paragraphs = []
    for result in results_paragraphs:
        try:
            paragraphs.append(result.text.strip())        
            print(result.text.strip())        
            print('---------------------------------------------')
        except AttributeError as e:
            print(e)

    # Adding the information to the dictionary of all scraped data
    scraped_mars_data["news_titles"] = titles
    scraped_mars_data['news_paras'] = paragraphs

# # JPL Mars Space Images - Featured Image [CHROME DRIVER ISSUE TO BE RESOLVED!!]

    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)
    
    # url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # browser.visit(url)

    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')

    # browser.links.find_by_partial_text('FULL IMAGE')
    # src=soup('a', class_='button fancybox')[0]['data-fancybox-href']

    # featured_image_url = f'https://www.jpl.nasa.gov' + src
 
    # # Adding the information to the dictionary of all scraped data
    # scraped_mars_data["featured_image_url"] = featured_image_url


## Mars Weather

 # Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page.

    mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'

    html2 = requests.get(mars_twitter_url).text

    soup2 = BeautifulSoup(html2, 'html.parser')

    # Extracting the results we want (the latest Mars weather tweet)
    results2 = soup2.find_all('p', class_="TweetTextSize")
    
    tweets = []
    for result in results2:
        tweets.append(result.get_text())
        
    # Saving the latest Mars weather tweet text as a variable called mars_weather
    mars_weather = tweets[2]
    
    # Adding the information to the dictionary of all scraped data
    scraped_mars_data["mars_weather"] = mars_weather

# # Mars Facts

    # URL of page to be scraped: Mars Facts webpage
    url = 'https://space-facts.com/mars/'

    # Using Pandas to scrape the table containing facts about Mars, including Diameter, Mass, etc.
    tables = pd.read_html(url)
    tables

    df = tables[0]
    df.columns = ['Variables', 'Values_Mars']
    df

    # Using Pandas to convert the data to a HTML table string
    html_table = df.to_html()
    html_table.replace('\n', '')

    href="static/style.css"

    # Adding the information to the dictionary of all scraped data
    scraped_mars_data["mars_html_table"] = html_table

# # Mars Hemispheres

    mars_hemispheres_img = [
        {'title': 'Cerberus Hemisphere', 'img_url': 'https:hhghgmh//astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'},
        {'title': 'Schiaparelli Hemisphere', 'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'},
        {'title': 'Syrtis Major Hemisphere', 'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'},
        {'title': 'Valles Marineris Hemisphere', 'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}
    ]

    # Adding the information to the dictionary of all scraped data
    scraped_mars_data["mars_hemispheres_img"] = mars_hemispheres_img

    print("The end!")

    # Output of the function scrape: the dictionary with all the info
    return scraped_mars_data
