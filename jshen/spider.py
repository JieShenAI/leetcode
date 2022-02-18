# _*_coding     : UTF_8_*_
# Author        :Jie Shen
# CreatTime     :2022/2/15 20:01

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


def sleep(t=0.3):
    time.sleep(t)


class jselenium:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def hover_by_xpath(self, xpath_str):
        element_to_hover_over = self.driver.find_element_by_xpath(xpath_str)
        ActionChains(self.driver).move_to_element(element_to_hover_over).perform()
        sleep()

    def hover_by_css(self, css_selector):
        element_to_hover_over = self.driver.find_element_by_css_selector(css_selector)
        ActionChains(self.driver).move_to_element(element_to_hover_over).perform()
        sleep()

    def click_by_xpath(self, xpath_str):
        self.driver.find_element_by_xpath(xpath_str).click()
        sleep()

    def main_windows_scroll(self, y, x=0):
        js = f"window.scrollTo({x}, {y})"
        self.driver.execute_script(js)

    def windows_scroll_by_class(self, class_name, id, offset):
        """
        把省窗口，滚动条下滑到offset
        :param offset:
        :return:
        """
        js = f'document.getElementsByClassName("{class_name}")[{id}].scrollTop={offset}'
        self.driver.execute_script(js)
        sleep()

    def __del__(self):
        # self.driver.quit()，无法关闭chromedriver，会导致内存泄露。即使程序结束，chromedriver也会一直占用内存；
        # bug说明: https://github.com/SeleniumHQ/selenium/issues/8571

        # pass
        sleep(2)
        try:
            self.driver.quit()
        except:
            # dos命令杀死chromedriver进程即可
            os.system("taskkill /F /im chromedriver.exe")
