from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from types import TracebackType
from typing import Type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By

# link = "https://writing9.com/text/66101c99143b1d001153a13a-scientists-and-technology-experts-are-more-valuable-to-society-than-artiststo-what-extent-do-you-agr"


class Essay(webdriver.Chrome):
    def __init__(
        self,
        driver_path=r"C:\Workspace\data_crawler\learn_selenium\chromedriver-win64",
        tear_down=False,
        link=None
    ):
        self.driver_path = driver_path
        self.tear_down = tear_down
        self.link = link
        os.environ["PATH"] += self.driver_path
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        super(Essay, self).__init__(options=chrome_options)
        self.implicitly_wait(15)

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ):
        if self.tear_down:
            self.quit()

    def land_page(self):
        self.get(self.link)

    def get_question(self):
        div_tag = self.find_element(
            By.CSS_SELECTOR, 'div[class="jsx-3307320108 page-text__question"]'
        )
        return div_tag.text

    def get_topic(self):
        div_tag = self.find_element(
            By.CSS_SELECTOR, 'div[class="jsx-3307320108 page-text__topics"]'
        )
        return div_tag.text

    def get_essay(self):
        div_tag = self.find_element(
            By.CSS_SELECTOR, 'div[class="jsx-3307320108 page-text__text"]'
        )
        return div_tag.text

    def get_overall_band(self):
        a_tag = self.find_elements(By.CSS_SELECTOR, 'a[class="jsx-721911361 link link_theme_gray     "]')[-1]
        overall = a_tag.text.split()[-1]
        return overall
        
    def get_feedback(self):
        div_tag = self.find_element(
            By.CSS_SELECTOR, 'div[class="jsx-3307320108 page-text__gpt"]'
        )
        return div_tag.text

    def get_num_linking_words(self):
        div_tag = self.find_element(
            By.CSS_SELECTOR,
            'div[class="jsx-2993038294 highlight-legends__item highlight-legends__item_linkingwords"]',
        )
        span_tag = div_tag.find_element(
            By.CSS_SELECTOR,
            'span[class="jsx-2993038294 highlight-legends__item-counter"]',
        )
        return span_tag.text

    def get_num_word_repetition(self):
        div_tag = self.find_element(
            By.CSS_SELECTOR,
            'div[class="jsx-2993038294 highlight-legends__item highlight-legends__item_repeatedwords"]',
        )
        span_tag = div_tag.find_element(
            By.CSS_SELECTOR,
            'span[class="jsx-2993038294 highlight-legends__item-counter"]',
        )
        return span_tag.text

    def get_num_grammar_mistakes(self):
        div_tag = self.find_element(
            By.CSS_SELECTOR,
            'div[class="jsx-2993038294 highlight-legends__item highlight-legends__item_mistake"]',
        )
        span_tag = div_tag.find_element(
            By.CSS_SELECTOR,
            'span[class="jsx-2993038294 highlight-legends__item-counter"]',
        )
        return span_tag.text

    def get_num_paragraphs_and_words(self):
        div_tag = self.find_element(
            By.CSS_SELECTOR,
            'div[class="jsx-2802957637 page-draft-text-analyzer__section-container page-draft-text-analyzer__stats"]',
        )
        span_tag = self.find_elements(By.CSS_SELECTOR, 'span[class="jsx-2802957637"]')
        return span_tag[0].text, span_tag[1].text # num paragraphs, num words

    def get_detail_score(self):
        div_tags = self.find_elements(By.CSS_SELECTOR, 'div[class="jsx-2802957637 page-draft-text-analyzer__section-container"]')[1:]
        overall_score_list = []
        detail_score_list = []
        for div_tag in div_tags:
            overall = div_tag.find_element(By.CSS_SELECTOR, 'span[class="jsx-2601907021 caps"]').text[-3:]
            overall_score_list.append(overall)
            detail_score_list.extend([small_div_tag.text[0] for small_div_tag in div_tag.find_elements(By.CSS_SELECTOR, 'div[class="jsx-2802957637 page-draft-text-analyzer__row"]')])
        return overall_score_list, detail_score_list

    def essay_details(self):
        question = self.get_question()
        topic = self.get_topic()
        essay = self.get_essay()
        overall = self.get_overall_band()
        feedback = self.get_feedback()
        linking_words = self.get_num_linking_words()
        word_repetition = self.get_num_word_repetition()
        grammar_mistakes = self.get_num_grammar_mistakes()
        paragraphs, words = self.get_num_paragraphs_and_words()
        overall_score, detail_score = self.get_detail_score()
        coherence_and_cohesion, lexical_resource, grammatical_range, task_achievement = overall_score
        co1, co2, co3, co4, co5, le1, le2, gr1, gr2, ta1, ta2, ta3, ta4 = detail_score
        self.quit()
        
        return [self.link, question, topic, essay, overall, feedback, linking_words, word_repetition, grammar_mistakes, 
                paragraphs, words, coherence_and_cohesion, lexical_resource, grammatical_range, task_achievement, co1, co2, co3, co4, co5, le1, le2, gr1, gr2, ta1, ta2, ta3, ta4]