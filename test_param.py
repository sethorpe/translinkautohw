import unittest
import pytest
from time  import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import desired_capabilities
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class TestTranslinkAuto: 
    bus_routes = (99, 28, 25)
    driver = ''

    def setup_method(self):
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.page_load_strategy = 'normal'
        desired_capabilities = {}
        # self.driver = webdriver.Edge(executable_path='/Users/seyithorpe/Downloads/edgedriver_mac64/msedgedriver', capabilities=desired_capabilities)
        # self.driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), capabilities=desired_capabilities)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.implicitly_wait(10)
        #Open URL
        self.driver.get("https://new.translink.ca")
        #Maximize Window / Set Window Size
        # self.driver.maximize_window()
        self.driver.set_window_size(1440, 800)
    
   
    @pytest.mark.skip
    @pytest.mark.parametrize('route',[(99)])
    def test_find_bus_route(self, route):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        # self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys(route)

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()
        sleep(5)

    @pytest.mark.skip
    @pytest.mark.parametrize('route, fav_title',
                            [
                                (99, 'Seyi\'s Fave Route')
                            ]

                            )
    def test_find_bus_route_and_save_to_favs(self, route, fav_title):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys(route)

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys(fav_title)

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)

    @pytest.mark.skip
    @pytest.mark.parametrize('route, fav_title',
                            [
                                (99, 'Seyi\'s Fave Route')
                            ]

                            )
    def test_validate_favs_link_title(self, route, fav_title):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys(route)

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys(fav_title)

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)

        # Get current url and save to param for comparison later
        my_route_url = self.driver.current_url

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()

        # Validate “Translink Auto Homework” link is present.
        # First we check the link text matches, then we check the URLs too.
        # Set variable
        my_route = self.driver.find_element(By.LINK_TEXT, fav_title)
        assert my_route.text == fav_title, "Link text does not match expected result"
        # self.assertEqual(my_route.text, fav_title, 'Link text does not match expected result')

        # Click on "Translink Auto Homework" link
        my_route.click()

        # Now get the current url and compare with param my_route_url from earlier.
        # self.assertEqual(self.driver.current_url, my_route_url, 'URLs do not match!')
        assert self.driver.current_url == my_route_url, "URLs do not match!"
    
    @pytest.mark.skip
    @pytest.mark.parametrize('route, fav_title, expected_route_title',
                            [
                                (99, 'Seyi\'s Fave Route','99 Commercial-Broadway / UBC (B-Line)')
                            ]

                            )
    def test_validate_route_title_displayed(self, route, fav_title, expected_route_title):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        # self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys(route)

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys(fav_title)

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)

        # Get current url and save to param for comparison later
        my_route_url = self.driver.current_url

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()

        # Validate “Translink Auto Homework” link is present
        # Set variable
        my_route = self.driver.find_element(By.LINK_TEXT, fav_title)
        # self.assertEqual(my_route.text, 'Translink Auto Homework', 'Link text does not match expected result')
        assert my_route.text == fav_title, "Link text does not match expected result"

       
        # Click on "Translink Auto Homework" link
        my_route.click()

        # Now get the current url and compare with param my_route_url from earlier.
        # self.assertEqual(self.driver.current_url, my_route_url, 'URLs do not match!')
        assert self.driver.current_url == my_route_url, "URLs do not match!"


        # Select frame element on the page, set to variable "iframe" and switch to it
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2) main:nth-child(14) div.gridContainer.NarrowFlexColumnBlockLayout.noBottomPadding.introBlockTheme:nth-child(7) section.CopyMain > iframe:nth-child(1)')
        self.driver.switch_to.frame(iframe)

        # Validate “99 Commercial-Broadway / UBC (B-Line)” is displayed on page
        # self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".txtRouteTitle").text,\
        #      route_title, "The text displayed does not match expected result")
        actual_route_title = self.driver.find_element(By.CSS_SELECTOR,".txtRouteTitle").text
        assert actual_route_title == expected_route_title, "The route title does NOT match expected result!"
        print("Got to the end of function!")
        
        # self.driver.get_screenshot_as_file(os.getcwd() + "/Translink_Screenshots/" + "screenshot_" + self.id() + "__" + utility.current_time() + ".png")
    
    # @pytest.mark.skip
    @pytest.mark.parametrize('route, fav_title, expected_route_title, destination, stop_name, stop_no',
                            [
                                (99, 'Seyi\'s Fave Route','99 Commercial-Broadway / UBC (B-Line)', 'To Comm\'l-Bdway Stn / Boundary B-Line', 'UBC Exchange Bay 7', "Stop # 61935"),
                                # (28, 'Seyi\'s Fave Route 2', '28 Phibbs Exch / Joyce Stn', 'To Kootenay Loop / Phibbs Exch', 'Joyce Stn Bay 4', 'Stop # 61609'),
                                # (25, 'Seyi\'s Fave Route 3', '25 Brentwood Stn / UBC', 'To Brentwood Stn / Nanaimo Stn', 'Nanaimo Stn Bay 1', 'Stop # 60314')
                            ]

                            )
    def test_full(self, route, fav_title, expected_route_title, destination, stop_name, stop_no):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        # self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys(route)

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys(fav_title)
        sleep(2)

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)

        # Get current url and save to param for comparison later
        my_route_url = self.driver.current_url

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()

        # Validate “Translink Auto Homework” link is present
        # Set variable
        my_route = self.driver.find_element(By.LINK_TEXT, fav_title)
        # self.assertEqual(my_route.text, 'Translink Auto Homework', 'Link text does not match expected result')
        assert my_route.text == fav_title, "Link text does not match expected result"

       
        # Click on "Translink Auto Homework" link
        my_route.click()

        # Now get the current url and compare with param my_route_url from earlier.
        # self.assertEqual(self.driver.current_url, my_route_url, 'URLs do not match!')
        assert self.driver.current_url == my_route_url, "URLs do not match!"


        # Select frame element on the page, set to variable "iframe" and switch to it
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2) main:nth-child(14) div.gridContainer.NarrowFlexColumnBlockLayout.noBottomPadding.introBlockTheme:nth-child(7) section.CopyMain > iframe:nth-child(1)')
        self.driver.switch_to.frame(iframe)

        # Validate “99 Commercial-Broadway / UBC (B-Line)” is displayed on page
        # self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".txtRouteTitle").text,\
        #      route_title, "The text displayed does not match expected result")
        actual_route_title = self.driver.find_element(By.CSS_SELECTOR,".txtRouteTitle").text
        assert actual_route_title == expected_route_title, "The route title does NOT match expected result!"
        print("Got to the end of function!")
        
        # self.driver.get_screenshot_as_file(os.getcwd() + "/Translink_Screenshots/" + "screenshot_" + self.id() + "__" + utility.current_time() + ".png")

        # Click on 'To Comm'l-Bdway Stn / Boundary B-Line'
        self.driver.find_element(By.LINK_TEXT, destination).click()

        # Wait for page load
        sleep(5)

        # Click on stop name
        pg_stop_name = self.driver.find_element(By.LINK_TEXT, stop_name)
        self.driver.execute_script("arguments[0].scrollIntoView();", pg_stop_name)
        sleep(3)
        pg_stop_name.click()
        # webdriver.ActionChains(self.driver).move_to_element(pg_stop_name).click().perform()
        # self.driver.find_element(By.LINK_TEXT, stop_name).click()
        
        # Wait for page load
        sleep(5)

        # Validate “Stop # 61935” is displaying
        # self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, '.stopNo').text,\
        #      stop_no, "The Stop # displayed does not match expected result")
        actual_stop_no = self.driver.find_element(By.CSS_SELECTOR, '.stopNo').text
        assert actual_stop_no == stop_no, "The Stop # displayed does NOT match expected result!"
        # self.driver.get_screenshot_as_file(os.getcwd() + "/Translink_Screenshots/" + "screenshot_" + self.id() + "__" + utility.current_time() + ".png")
    
    def teardown_method(self):
        # As a note, In addCleanup, the first in, is executed last.
        self.driver.quit()
        # self.addCleanup(self.driver.quit)


# if __name__ == '__main__':
#     unittest.main()