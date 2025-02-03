from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

service = Service(executable_path=r'D:\\Semester 3\\DSA Lab\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

course_url = 'http://eduko.spikotech.com/Course/Index'
driver.get(course_url)

course_data = []

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'card'))
)

course_cards = driver.find_elements(By.CLASS_NAME, 'card')

for course_card in course_cards:
    course_title = course_card.find_element(By.CLASS_NAME, 'card-title').text.strip()
    
    header_tags = course_card.find_elements(By.TAG_NAME, 'h7')
    course_instructor = header_tags[0].text.strip() if len(header_tags) > 0 else 'N/A'
    course_semester = header_tags[1].text.strip() if len(header_tags) > 1 else 'N/A'
    
    detail_button = course_card.find_element(By.CSS_SELECTOR, 'a.btn.btn-md.waves-effect')
    detail_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    
    time.sleep(10)  
    
    course_code = driver.find_element(By.ID, 'CourseCode').text.strip()
    course_description = driver.find_element(By.ID, 'CourseDescription').text.strip()

    book_items = driver.find_elements(By.TAG_NAME, 'li')
    textbook_1 = 'N/A'
    textbook_2 = 'N/A'
    
    if len(book_items) > 0:
        anchor_tags = book_items[0].find_elements(By.TAG_NAME, 'a')
        if len(anchor_tags) >= 4:
            textbook_1 = anchor_tags[4].text.strip()
            textbook_2 = anchor_tags[5].text.strip()

    course_data.append({
        'Title': course_title,
        'Instructor': course_instructor,
        'Semester': course_semester,
        'Code': course_code,
        'Description': course_description,
        'TextBook1': textbook_1,
        'TextBook2': textbook_2
    })

    driver.back()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'card'))
    )

courses_df = pd.DataFrame(course_data, columns=['Title', 'Instructor', 'Semester', 'Code', 'Description', 'TextBook1', 'TextBook2'])
courses_df.to_csv('eduko_courses.csv', index=False)

driver.quit()
