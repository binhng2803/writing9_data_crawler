from types import TracebackType
from typing import Type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import writing9.urls as urls
from selenium.webdriver.common.by import By


class Band(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Workspace\data_crawler\learn_selenium\chromedriver-win64",
                 tear_down=False):
        self.driver_path = driver_path
        self.tear_down = tear_down
        os.environ["PATH"] += self.driver_path
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        super(Band, self).__init__(options=chrome_options)
        self.implicitly_wait(15)
        # self.maximize_window()
        
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
        if self.tear_down:
            self.quit()

    def land_page(self, band=None, page=0):
        if band:
            self.get(f'https://writing9.com/band/{band}/{page}')
        else:
            self.get(urls.URLS[0])

    
    def pull_all_essay_on_page(self):
        all_block =  self.find_element(By.CSS_SELECTOR, 'div[class="jsx-2609154510 list"]')
        essay_list = all_block.find_elements(By.CSS_SELECTOR, 'div[class="jsx-2609154510 item"]')
        all_links = []
        for essay in essay_list:
            a_tag = essay.find_element(By.TAG_NAME, 'a')
            link = a_tag.get_attribute('href')
            all_links.append(link)
        self.quit()
        return all_links
    
    
    
    
    
    