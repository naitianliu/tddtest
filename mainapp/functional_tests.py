from selenium import webdriver
import unittest

'''
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title, 'Browser title was %s' % browser.title

browser.quit()
'''


class NewTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)
        self.fail('Finished the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')