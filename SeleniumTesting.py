from selenium import webdriver
browser = webdriver.Firefox()
def findVid(Name):
    browser.get('https://google.com')
    searchElem = browser.find_element_by_css_selector('#searchInput')
    searchElem.send_keys(Name)
    searchElem.submit() 

def main():
    vidName = input("What video would you like to search: ")
    findVid(vidName)

main()