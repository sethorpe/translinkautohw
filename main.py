import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located, presence_of_element_located
from selenium.webdriver import Chrome
from time import sleep


class TestTranslinkAuto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
        #Open URL
        self.driver.get("https://new.translink.ca")
        #Maximize Window
        self.driver.maximize_window()
        
    
    def tearDown(self):
        self.driver.quit()

    def test_find_bus_route(self):

        # Set wait param with a 10 second timeout value
        wait = WebDriverWait(self.driver, 20)
        #print('Waiting for \'Next Bus\' to be available on page...')
        # Wait for 'Next Bus' to be located on the screen before proceeding
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Next Bus')))
        #print('clicking on \'Next Bus\'...')
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()
        #print('now to find the search box and click in it...')

        # Wait until the 'NextBusSearchTerm' element is visible on the page
        wait.until(EC.visibility_of_element_located((By.ID, 'NextBusSearchTerm')))

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()
        #print('Clicked on find my next bus...')

    def test_find_bus_route_and_save_to_favs(self):
        # Set wait param with a 10 second timeout value
        wait = WebDriverWait(self.driver, 20)
        #print('Waiting for \'Next Bus\' to be available on page...')
        # Wait for 'Next Bus' to be located on the screen before proceeding
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Next Bus')))
        #print('clicking on \'Next Bus\'...')
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()
        #print('now to find the search box and click in it...')

        # Wait until the 'NextBusSearchTerm' element is visible on the page
        wait.until(EC.visibility_of_element_located((By.ID, 'NextBusSearchTerm')))

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()
        #print('Clicked on find my next bus...')

        # Wait for the Add Fav Icon to be visible on the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'AddDelFav')))

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()
        #print('Clicked on Add Fav Icon...')

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()
        #print('Clicked the dialog box to make sure it\'s active...')

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys('Translink Auto Homework')
        #print('Added Fave Name to text box...')

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)
        #print('Saved \'Translink Auto Homework \'to Faves...')

    def test_validate_favs_link_title(self):
        # Set wait param with a 10 second timeout value
        wait = WebDriverWait(self.driver, 20)
        #print('Waiting for \'Next Bus\' to be available on page...')
        # Wait for 'Next Bus' to be located on the screen before proceeding
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Next Bus')))
        #print('clicking on \'Next Bus\'...')
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()
        #print('now to find the search box and click in it...')

        # Wait until the 'NextBusSearchTerm' element is visible on the page
        wait.until(EC.visibility_of_element_located((By.ID, 'NextBusSearchTerm')))

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()
        #print('Clicked on find my next bus...')

        # Wait for the Add Fav Icon to be visible on the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'AddDelFav')))

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()
        #print('Clicked on Add Fav Icon...')

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()
        #print('Clicked the dialog box to make sure it\'s active...')

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys('Translink Auto Homework')
        #print('Added Fave Name to text box...')

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)
        #print('Saved \'Translink Auto Homework \'to Faves...')

        # Get current url and save to param for comparison later
        my_route_url = self.driver.current_url
        #print('My route url: ' + my_route_url)

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()
        #print('Clicked on \'My Favs\' icon...')

        # Validate “Translink Auto Homework” link is present.
        # First we check the link text matches, then we check the URLs too.
        # Set variable
        my_route = self.driver.find_element(By.LINK_TEXT, 'Translink Auto Homework')
        self.assertEqual(my_route.text, 'Translink Auto Homework', 'Link text does not match expected result')
        #print('\'Translink Auto Homework\' link text is present')

        # Click on "Translink Auto Homework" link
        my_route.click()
        #print('Clicked on Translink Auto Homework link...')

        # Now get the current url and compare with param my_route_url from earlier.
        self.assertEqual(self.driver.current_url, my_route_url, 'URLs do not match!')

    def test_validate_route_title_displayed(self):
        # Set wait param with a 10 second timeout value
        wait = WebDriverWait(self.driver, 20)
        #print('Waiting for \'Next Bus\' to be available on page...')
        # Wait for 'Next Bus' to be located on the screen before proceeding
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Next Bus')))
        #print('clicking on \'Next Bus\'...')
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()
        #print('now to find the search box and click in it...')

        # Wait until the 'NextBusSearchTerm' element is visible on the page
        wait.until(EC.visibility_of_element_located((By.ID, 'NextBusSearchTerm')))

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()
        #print('Clicked on find my next bus...')

        # Wait for the Add Fav Icon to be visible on the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'AddDelFav')))

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()
        #print('Clicked on Add Fav Icon...')

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()
        #print('Clicked the dialog box to make sure it\'s active...')

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys('Translink Auto Homework')
        #print('Added Fave Name to text box...')

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)
        #print('Saved \'Translink Auto Homework \'to Faves...')

        # Get current url and save to param for comparison later
        my_route_url = self.driver.current_url
        #print('My route url: ' + my_route_url)

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()
        #print('Clicked on \'My Favs\' icon...')

        # Validate “Translink Auto Homework” link is present
        # Set variable
        my_route = self.driver.find_element(By.LINK_TEXT, 'Translink Auto Homework')
        self.assertEqual(my_route.text, 'Translink Auto Homework', 'Link text does not match expected result')
        #print('\'Translink Auto Homework\' link text is present')
       
        # Click on "Translink Auto Homework" link
        my_route.click()
        #print('Clicked on Translink Auto Homework link...')

        # Now get the current url and compare with param my_route_url from earlier.
        self.assertEqual(self.driver.current_url, my_route_url, 'URLs do not match!')

        # Wait, then select frame element on the page, set to variable "iframe" and finally switch to it
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body:nth-child(2) main:nth-child(14) div.gridContainer.NarrowFlexColumnBlockLayout.noBottomPadding.introBlockTheme:nth-child(7) section.CopyMain > iframe:nth-child(1)')))
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2) main:nth-child(14) div.gridContainer.NarrowFlexColumnBlockLayout.noBottomPadding.introBlockTheme:nth-child(7) section.CopyMain > iframe:nth-child(1)')
        self.driver.switch_to.frame(iframe)

        # Wait for page to be completely loaded before continuing
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'txtRouteTitle')))

        # Validate “99 Commercial-Broadway / UBC (B-Line)” is displayed on page
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".txtRouteTitle").text,\
             "99 Commercial-Broadway / UBC (B-Line)", "The text displayed does not match expected result")
        #print('99 Commerical-Broadway / UBC (B-Line) is displayed on page')

   

    def test_validate_stop_no_displayed(self):
        
        # Set wait param with a 10 second timeout value
        wait = WebDriverWait(self.driver, 20)
        #print('Waiting for \'Next Bus\' to be available on page...')
        # Wait for 'Next Bus' to be located on the screen before proceeding
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Next Bus')))
        #print('clicking on \'Next Bus\'...')
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()
        #print('now to find the search box and click in it...')

        # Wait until the 'NextBusSearchTerm' element is visible on the page
        wait.until(EC.visibility_of_element_located((By.ID, 'NextBusSearchTerm')))

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()
        #print('Clicked on find my next bus...')

        # Wait for the Add Fav Icon to be visible on the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'AddDelFav')))

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()
        #print('Clicked on Add Fav Icon...')

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()
        #print('Clicked the dialog box to make sure it\'s active...')

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys('Translink Auto Homework')
        #print('Added Fave Name to text box...')

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)
        #print('Saved \'Translink Auto Homework \'to Faves...')

        # Get current url and save to param for comparison later
        my_route_url = self.driver.current_url
        #print('My route url: ' + my_route_url)

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()
        #print('Clicked on \'My Favs\' icon...')

        # Validate “Translink Auto Homework” link is present
        # Set variable
        my_route = self.driver.find_element(By.LINK_TEXT, 'Translink Auto Homework')
        self.assertEqual(my_route.text, 'Translink Auto Homework', 'Link text does not match expected result')
        #print('\'Translink Auto Homework\' link text is present')
       
        # Click on "Translink Auto Homework" link
        my_route.click()
        #print('Clicked on Translink Auto Homework link...')

        # Now get the current url and compare with param my_route_url from earlier.
        self.assertEqual(self.driver.current_url, my_route_url, 'URLs do not match!')

        # Wait, then select frame element on the page, set to variable "iframe" and finally switch to it
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body:nth-child(2) main:nth-child(14) div.gridContainer.NarrowFlexColumnBlockLayout.noBottomPadding.introBlockTheme:nth-child(7) section.CopyMain > iframe:nth-child(1)')))
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2) main:nth-child(14) div.gridContainer.NarrowFlexColumnBlockLayout.noBottomPadding.introBlockTheme:nth-child(7) section.CopyMain > iframe:nth-child(1)')
        self.driver.switch_to.frame(iframe)

        # Wait for page to be completely loaded before continuing
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'txtRouteTitle')))

        # Validate “99 Commercial-Broadway / UBC (B-Line)” is displayed on page
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".txtRouteTitle").text,\
             "99 Commercial-Broadway / UBC (B-Line)", "The text displayed does not match expected result")
        #print('99 Commerical-Broadway / UBC (B-Line) is displayed on page')

        # Click on 'To Comm'l-Bdway Stn / Boundary B-Line'
        self.driver.find_element(By.LINK_TEXT, 'To Comm\'l-Bdway Stn / Boundary B-Line').click()
        #print('Clicked on To Comm\'l-Bdway Stn / Boundary B-Line link...')

        # Wait for page load
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'UBC Exchange Bay 7')))
        sleep(5)

        # Click on UBC Exchange Bay 7
        self.driver.find_element(By.LINK_TEXT, 'UBC Exchange Bay 7').click()
        #print('Clicked on UBC Exchange Bay 7 link...')
        
        # Wait for page load
        sleep(5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.stopNo')))

        # Validate “Stop # 61935” is displaying
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, '.stopNo').text,\
             "Stop # 61935", "The Stop # displayed does not match expected result")
        #print('The text \'Stop # 61935\' is displayed on page...')

if __name__ == '__main__':
    unittest.main()