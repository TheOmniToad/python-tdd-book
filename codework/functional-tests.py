from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

#Edith has heard about a cool new online to-do app. she goes to check out its homepage
        self.browser.get('http://localhost:8000')

#She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

#She is invited to enter a to-do item straight away

#she types "Buy peaock feathers" into a text box

#when she hits enter, the page updates and now lists her item in a lists

#There is a box ivitier her to adda nother items. She enters "Use feathers to make a fly"

#The page updates again, and now shows both items

#edith wonders whether the site will still remember her list.
#She sees the stie generated a unique url for heard
#Text explains that function

#She vists the url - her list is There

#satisfied


if __name__ == '__main__':
    unittest.main(warnings='ignore')
