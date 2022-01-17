#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

#import Pandas
import pandas as pd 


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### 10.3.3 Visit the mars nasa news site

# In[ ]:


#visit URL
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


#set up HTML parser 
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


#now start scraping 
slide_elem.find('div', class_='content_title')


# In[ ]:


#we just want the text
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


#when executed your results should be the most recent title published on the website 


# In[ ]:


# Use the parent element (slide_elem) to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### 10.3.4 Featured Images 

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
#when this is run the automated browser should now show the slideshow or full size image 


# In[ ]:


# Parse the resulting full size image html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
#link will be the output 


# In[ ]:


#combine base URL (spaceimages-mars.com) and above partial URL 
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### 10.3.5 Mars Facts 

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


#convert df back to HTM so it can be displayed on website 
df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
html_soup = soup(html, 'html.parser')

#gets the titles
title_one = browser.find_by_tag('h3')[0].text
title_two=browser.find_by_tag('h3')[1].text
title_three=browser.find_by_tag('h3')[2].text
title_four=browser.find_by_tag('h3')[3].text


#click on picture 1
full_image_elem = browser.find_by_tag('h3')[0]
full_image_elem.click()
# get the full res URL 
html = browser.html
img_soup = soup(html, 'html.parser')
img_one=img_soup.find('img', class_='wide-image').get('src')

#clicks on picture 2 
browser.back()
full_image_elem = browser.find_by_tag('h3')[1]
full_image_elem.click()
html = browser.html
img_soup = soup(html, 'html.parser')
img_two=img_soup.find('img', class_='wide-image').get('src')

#clicks on picture 3 
browser.back()
full_image_elem = browser.find_by_tag('h3')[2]
full_image_elem.click()
html = browser.html
img_soup = soup(html, 'html.parser')
img_three=img_soup.find('img', class_='wide-image').get('src')

#clicks on picture 4
browser.back() 
full_image_elem = browser.find_by_tag('h3')[3]
full_image_elem.click()
html = browser.html
img_soup = soup(html, 'html.parser')
img_four=img_soup.find('img', class_='wide-image').get('src')

#create full URL's 
img_url_one = f'https://marshemispheres.com/{img_one}'
img_url_two = f'https://marshemispheres.com/{img_two}'
img_url_three = f'https://marshemispheres.com/{img_three}'
img_url_four = f'https://marshemispheres.com/{img_four}'


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls = [{'img_url':img_url_one, 'title':title_one},
                         {'img_url':img_url_two, 'title':title_two},
                         {'img_url':img_url_three, 'title':title_three},
                         {'img_url':img_url_four, 'title':title_four}]
hemisphere_image_urls

# 5. Quit the browser
browser.quit()
