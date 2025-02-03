from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

service = Service(executable_path=r'D:\\Semester 3\\DSA Lab\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

url = 'http://eduko.spikotech.com/Course/Index'  
driver.get(url)

courses = []

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'card'))
)

course_cards = driver.find_elements(By.CLASS_NAME, 'card')  

for card in course_cards:
  
    title = card.find_element(By.CLASS_NAME, 'card-title').text.strip() 
     
    h7_tags = card.find_elements(By.TAG_NAME, 'h7')
    instructor = h7_tags[0].text.strip() 
    semester = h7_tags[1].text.strip() 

    page_button = card.find_element(By.CSS_SELECTOR, 'a.btn.btn-md.waves-effect')
    page_button.click()

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    time.sleep(10) 

    course_code =  driver.find_element(By.ID, 'CourseCode').text.strip()
    desc = driver.find_element(By.ID , 'CourseDescription').text.strip()

    book_items = driver.find_elements(By.TAG_NAME, 'li')
    for item in book_items:
      a_tags = item.find_elements(By.TAG_NAME, 'a')

    text_book1 = 'N/A'
    text_book2 = 'N/A'
    if len(a_tags) >= 4: 
        text_book1 = a_tags[4].text.strip() 
        text_book2 = a_tags[5].text.strip()  


    courses.append({'Title': title, 'Instructor': instructor, 'Semester': semester, 'Code': course_code, 'Description' : desc, 'TextBook1' : text_book1, 'TextBook2' : text_book2})

    driver.back()  
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'card'))
    )

df = pd.DataFrame(courses, columns=['Title', 'Instructor', 'Semester', 'Code', 'Description', 'TextBook1', 'TextBook2'])
df.to_csv('eduko_courses.csv', index=False)

driver.quit()