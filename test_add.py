# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAdd():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_add(self):
    self.driver.get("http://127.0.0.1:5500/testselenium/3.html")
    self.driver.set_window_size(784, 835)
    self.driver.find_element(By.ID, "bookName").click()
    self.driver.find_element(By.ID, "bookName").send_keys("hhh")
    self.driver.find_element(By.ID, "author").send_keys("hhh")
    self.driver.find_element(By.ID, "quantity").send_keys("2")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    assert self.driver.switch_to.alert.text == "Book added successfully!"
  
  def test_duplicate_book(self):
    self.driver.get("http://127.0.0.1:5500/testselenium/3.html")
    self.driver.set_window_size(784, 835)
    self.driver.find_element(By.ID, "bookName").send_keys("Duplicate Book")
    self.driver.find_element(By.ID, "author").send_keys("Author A")
    self.driver.find_element(By.ID, "quantity").send_keys("3")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # Thêm lần thứ hai
    self.driver.find_element(By.ID, "bookName").send_keys("Duplicate Book")
    self.driver.find_element(By.ID, "author").send_keys("Author A")
    self.driver.find_element(By.ID, "quantity").send_keys("3")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    alert_text = self.driver.switch_to.alert.text
    assert "Book with the same name already exists!" in alert_text

  def test_invalid_quantity(self):
    self.driver.get("http://127.0.0.1:5500/testselenium/3.html")
    self.driver.find_element(By.ID, "bookName").send_keys("Invalid Quantity Book")
    self.driver.find_element(By.ID, "author").send_keys("Author B")
    self.driver.find_element(By.ID, "quantity").send_keys("-5")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    alert_text = self.driver.switch_to.alert.text
    assert "Vui lòng nhập thông tin hợp lệ!" in alert_text
