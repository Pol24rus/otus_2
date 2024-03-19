from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import datetime
from datetime import datetime


link = "https://intranet-test.roslesinforg.ru/stream/"

try:
    driver = webdriver.Chrome()
    driver.get(link)

# �����������
    login = driver.find_element(By.ID, "USER_LOGIN")
    login.send_keys("OK_RLI")
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys("OK_RLIOK_RLI")
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    #time.sleep(1)

    input_txt = datetime.now()
    # print("data=", input_txt)

    input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner") #��������, ���� � ����
    #input1 = driver.find_element(By.ID, "feed-add-post-form-tab-message") #������� ���� (������� �� ������) �������� ��������
    input1.click()
    # ����� ���������
    iframe1: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
    driver.switch_to.frame(iframe1)
    input2 = driver.find_element(By.TAG_NAME, "body")
    input2.send_keys("���� ��������� ����, �� ", str(input_txt))

    element_file = driver.find_element(By.ID, "bx-b-uploadfile-blogPostForm")
    element_file.click()

    driver.switch_to.default_content()

    #driver.implicitly_wait(5)
    #��� � ������� �������� ���
    ok = driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption")
    ok.click()
    # ��� � ����� �������� � ����� ������
    # �� ��� ����������� ��������. �������� �� ��, � ��� ����������.
    #element_input = driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) > div.ui-selector-item > div.ui-selector-item-titles > div.ui-selector-item-title-box > div.ui-selector-item-title")
    #element_input.click()
    element_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box"))
        )
    time.sleep(1)
    element_input.send_keys("��������")
    time.sleep(1)
    element_input.send_keys(Keys.ENTER)
    time.sleep(1)
    element_input.send_keys("�����")
    time.sleep(1)
    element_input.send_keys(Keys.ENTER)
    # ������ ���� ����������
    #driver.find_element(By.CSS_SELECTOR, "div.ui-tag-selector-tag-remove").click() #������ � ��� � ������
    driver.find_element(By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box").click()

    button = driver.find_element(By.ID, "blog-submit-button-save")
    button.click()

finally:
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    driver.quit()

# �� �������� �������� ������ ������ � ����� �����