# pip install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Webpage:
    def __init__(self, _driver, url, username ="", password ="", waiting_time = 60):
        self.driver = None
        if _driver == "firefox":
            self.driver = webdriver.Firefox()
        elif _driver == "chrome":
            self.driver = webdriver.Chrome()
        else:
            raise ValueError("Driver must be either 'firefox' or 'chrome'")
        self.waiting_time = waiting_time
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, self.waiting_time)
        self.username = username
        self.password = password

class Web_Controller:
    def __init__(self, _driver, url, username ="", password ="", waiting_time = 10):
        self.webpage = Webpage(_driver,url, username, password,  waiting_time)
    
    def element_exists(self, xpath):
        try:
            self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

    def click(self, xpath):
        #print(f"Clicking {xpath}")
        self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()

    def click_with_scroll(self, xpath):
        #print(f"Clicking {xpath}")
        element = self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        self.webpage.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    
    # select dropdown option by data-value
    def select_multivalue_dropdown_option_by_value(self, drowdown_xpath, list_xpath, _in_value):
        #print(f"Dropdown xpath: '{drowdown_xpath}'")
        dropdown = self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, drowdown_xpath)))
        dropdown.click()
        time.sleep(2)
        
        # search all li and span elements in the dropdown list
        _search_xpath_li = f"{list_xpath}//li"
        _search_xpath_span = f"{list_xpath}//span"

        #print(f"Search xpath for li: '{_search_xpath_li}'")
        #print(f"Search xpath for span: '{_search_xpath_span}'")
        
        list_items = self.webpage.driver.find_elements(By.XPATH, _search_xpath_li)
        spans = self.webpage.driver.find_elements(By.XPATH, _search_xpath_span)
        
        data_value = None
        
        # First, check within li elements
        for item in list_items:
            if item.text.strip().upper().replace(" ", "") == _in_value.strip().upper().replace(" ", ""):
                data_value = item.get_attribute('data-value')
                if data_value:
                    item.click()
                    return data_value
        
        # If not found in li elements, check within span elements
        for span in spans:
            if span.text.strip().upper().replace(" ", "") == _in_value.strip().upper().replace(" ", ""):
                parent_li = span.find_element(By.XPATH, '..')
                if parent_li and parent_li.get_attribute('data-value'):
                    data_value = parent_li.get_attribute('data-value')
                    parent_li.click()
                    return data_value
        
        raise ValueError(f"No matching items are found for: '{_in_value}'")

    # select dropwdown option by value
    def select_dropdown_option_by_value(self, drowdown_xpath, value):
        dropdown = self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, drowdown_xpath)))
        dropdown.click()
        time.sleep(1)
        _temp_data_value = f"{drowdown_xpath}/select/option[@value='{value}']"
        option = self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, _temp_data_value)))
        option.click()

    def send_keys(self, xpath, keys):
        self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).clear()
        self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(keys)
    def get_text(self, xpath):
        return self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).text
    def get_attribute(self, xpath, attribute):
        return self.webpage.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).get_attribute(attribute)
    
    """
    def click_horizontal_radio_button(self, xpath, _in_value):
        print(f"Clicking horizontal radio button with value {_in_value}")
        print(f"Xpath: {xpath}")
        parent_elements = self.webpage.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))       
        for parent_element in parent_elements:
            radio_buttons = parent_element.find_elements(By.XPATH, f".//input[@type='radio' and @value='{_in_value}']")
            for radio_button in radio_buttons:
                if radio_button.get_attribute('value').upper().replace(" ","") == _in_value.upper().replace(" ",""):
                    #print(f"Radio button with value {_in_value} found. The radio attribute is {radio_button.get_attribute('value')}")
                    label = radio_button.find_element(By.XPATH, "./ancestor::label")
                    label.click()
                    return 
    """
    def click_horizontal_radio_button(self, xpath, _in_value):
        #print(f"Clicking horizontal radio button with value {_in_value}")
        #print(f"Xpath: {xpath}")
        parent_elements = self.webpage.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))   
        for parent_element in parent_elements:
            radio_buttons = parent_element.find_elements(By.XPATH, f".//input[@type='radio' and @value='{_in_value}']")
            for radio_button in radio_buttons:
                if radio_button.get_attribute('value').upper().replace(" ","") == _in_value.upper().replace(" ",""):
                    #print(f"Radio button with value {_in_value} found. The radio attribute is {radio_button.get_attribute('value')}")
                    label = radio_button.find_element(By.XPATH, "./ancestor::label")
                    label.click()
                    return
        for element in parent_elements:
            radio_button = element.find_element(By.XPATH, f".//input[@type='radio' and @value='{_in_value.lower()}']")
            if radio_button:
                self.webpage.driver.execute_script("arguments[0].click();", radio_button)
                break

    def click_radio_button(self, xpath, _in_value):
        # list of radio buttons
        parent_elements = self.webpage.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))       
        for parent_element in parent_elements:
            radio_buttons = parent_element.find_elements(By.XPATH, f".//input[@type='radio' and @value='{_in_value}']")
            for radio_button in radio_buttons:
                if radio_button.get_attribute('value').upper().replace(" ","") == _in_value.upper().replace(" ",""):
                    #print(f"Radio button with value {_in_value} found. The radio attribute is {radio_button.get_attribute('value')}")
                    radio_button.click()
                    break

    def close(self):
        self.webpage.driver.close()

"""
# # TEST CODE
# sample 1
#controller = Web_Controller("https://www.google.com", username="user", password="password")
# sample 2

controller = Web_Controller("https://www.google.com")
import time
time.sleep(10)
controller.close()
"""
