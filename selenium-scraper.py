import pandas as pd 
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_descriptions(browser, job_ids):
    job_descriptions = []
    for job_id in job_ids:
        browser.get(f'https://www.linkedin.com/jobs/search/?currentJobId={job_id}&keywords=software%20developer')
        job_description = browser.find_elements_by_class_name('jobs-search__right-rail')[0].text
        job_descriptions.append(job_description)

    return job_descriptions

# This will open a new Chrome page to test specified url on (for scraping)
browser=webdriver.Chrome("My Chrome Path")
browser.get("https://www.linkedin.com")

# Requires user to enter username and password
username=browser.find_element_by_id("session_key")
username.send_keys("ENTER USERNAME")
password=browser.find_element_by_id("session_password")
password.send_keys("ENTER PASSWORD")

# Once username and password are entered, this will automatically click the submit button to login into LinkedIn
login_button=browser.find_element_by_class_name("sign-in-form__submit-button")
login_button.click()

# This is the URL to test the jobs I want to scrape from
browser.get("https://www.linkedin.com/jobs/search/?keywords=software%20developer")

# This will scrape and display (25) job titles from page (1)
job_title=browser.find_elements_by_class_name("job-card-list__title")
company_title=[]
for i in job_title:
    company_title.append(i.text)
print(company_title)
print()
print(len(company_title))


# This will scrape and display (25) company names from page (1) - correspondent to company_title above
job_company=browser.find_elements_by_class_name("job-card-container__company-name")
company_name=[]
for i in job_company:
    company_name.append(i.text)  
print(company_name)
print()
print(len(company_name))



# This will scrape and display (25) location names from page (1) - correspondent to company_title and company_name above
job_location=browser.find_elements_by_class_name("job-card-container__metadata-item")
location_name=[]
for i in job_location:
    location_name.append(i.text)  
print(location_name)
print()
print(len(location_name))

# At this point, I am trying to iterate over each of the (25) jobs to pull out the description. I've successfully been able to pull out (1) description, but haven't been able to pull out the other descriptions of the remaining (24) jobs. 
job_description=browser.find_elements_by_class_name('jobs-search__right-rail')
description_name = []
for i in job_description:
    description_name.append(i.text)
print(description_name)
print()
print(len(description_name))


# Example of scraping the currentJobId for each item.
job_containers = browser.find_elements_by_class_name('job-card-container relative job-card-list job-card-container--clickable job-card-list--underline-title-on-hover jobs-search-results-list__list-item--active jobs-search-two-pane__job-card-container--viewport-tracking-0')
job_ids = []
for job_container in job_containers:
    job_ids.append(job_container.get_attribute("data-job-id"))


