import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#chromedriver = "/usr/local/bin/chromedriver"
chromedriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

my_link = 'https://docs.google.com/forms/d/e/1FAIpQLSe2CDLWh3DvM9gYbtSuTCDt1Q6IEJab-yq1PeOSxBkBfWaCRA/viewform'
link = 'https://docs.google.com/forms/d/e/1FAIpQLScMvCbBeZIz0AFz4xmfuGDvWhIQH3xxuvTGb2Lut7aw3A0Bpw/viewform'
#li = 'file:///C:/Users/Robin's/Documents/test%20python%20automation%20web/Analyze%20the%20Impact%20of%20Occupational%20Stress%20and%20Remote%20working%20on%20Employee%20Performance_%20An%20Empirical%20Study%20from%20Bangladesh%20Perspective..html'
driver.get(link)

def r(x, y):
    z = [x, y]
    return random.choice(z)

labels = [r("i77","i80"), r("i96","i99"), r("i115","i118"), r("i134","i137"),
          r("i147", "i153" ), r("i172", "i175"), r("i191", "i194"),
          r("i210", "i213"), r("i229", "i232"), r("i242", "i248"), r("i267", "i270"),
          r("i286", "i289"), r("i305", "i308"), r("i324", "i327"), r("i343", "i346"), r("i381", "i384"),
          r("i400", "i403"), r("i419", "i422"), r("i438", "i441"), r("i457", "i460"), r("i362", "i365"),
          r("i476", "i479"), r("i495", "i498"), r("i514", "i517"), r("i533", "i536"),
          r("i552", "i555"), r("i29", "i32"), r("i55", "i58"), r("i42", "i45"),
          r("i13", "i16")]

j = 0
ser = 71    #starting label attribute from google form's inspect elements
label = []

while(j < 26):
    label.append(r("i" + str(ser + 19 * j), "i" + str(ser + 19 * j + 3)))
    j += 1

time.sleep(3)
for i in label:
    driver.find_element_by_xpath("//div//label[@for = '" + i + "']").click()
    time.sleep(0.1)

