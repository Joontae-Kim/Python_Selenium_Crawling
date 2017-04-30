#-*- coding: utf-8 -*- 
## http://selenium-python.readthedocs.io/getting-started.html
## 위의 튜토리얼을 연습하며 제가 공부하고, 연습한 필기노트 입니다. 
## 설명(주석처리) 및 코드는 위의 튜토리얼을 연습하며 제게 필요한 혹은 
## 알고 있으면 좋갰다고 생각한 내용들을 번역한 것입니다. 
## 문제 시 bexellenting@gmail.com으로 연락주시면 감사하겠습니다 .

# -------------------------------------------------------------------- #

## Chp2.1 - Simple Usage
# If you have installed Selenium Python bindings, you can start using it from Python like this.
# 만약 셀리니움 파이썬 바인딩을 설치했다면 아래와 같이 파이썬을 사용할 수 있다. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()


## Chp2.2 - Example Explained

from selenium import webdriver
# selenium.webdriver module은 모든 WebDriver 실행을 제공한다. 
# 현재 지원되고 있는 WebDriver 실행은 Firefox, Chrome, IE and Remote 이다.

from selenium.webdriver.common.keys import Keys
# Keys class는 RETURN, F1, ALT 등과 같은 키보드 키를 제공한다. 

driver = webdriver.Firefox().
# 다음은 Firefox WebDriver의 인스턴스가 만들어졌다

driver.get("http://www.python.org")
# driver.get 메서드는 URL에 의해 지정된 페이지로 이동할것 이다.
# WebDriver는 당신의 테스트 또는 스크립트에 대한 컨트롤을 반환하기 전에 페이지가 완전히 로드될 때까지(즉, "onload" 이벤트가 발생된다.) 기다릴 것이다.
# 페이지 로드 시 AJAX를 많이 사용하면 WebDriver가 완전히 로드된시기를 알 수 없다는 점에 유의해야한다.

assert "Python" in driver.title
# The next line is an assertion to confirm that title has “Python” word in it:
# 다음 줄은 이 명령어 안에 "Python"이라는 제목이 있음을 확인하는 선언입니다.

elem = driver.find_element_by_name("q")
# WebDriver는 find_element_by_* 메서드 중의 하나를 사용해 요소들을 찾을 수 있는 다양한 방법을 제공합니다.
# 예를 들어, 텍스트 박스(Input box) 요소는 find_element_by_name 메서드를 사용해 텍스트 박스의 네임 속성으로 찾을 수 있다. 
# 요소를 검색하기 위한 상세한 설명은 Locating Elements chapter에서 볼 수 있습니다.

elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# 다음은 우리가 키값을 보낼 것이다. 이것은 여러분의 키보드를 사용해 키를 입력하는 것과 유사하다.
# 특수키는 selenium.webdriver.common.keys 로부터 임포트 된 Keys class를 이용해 보낼 수 있다.
# 안전을 위해 우리는 첫번째로 input field에 미리 채워진 텍스트를 지울 것입니다(예. “Search”).
# 그럼 우리의 검색 결과들에 대한 영향을 끼칠 수 없다.

assert "No results found." not in driver.page_source
# 페이지를 제출한 후, 우리는 결과가 있으면 결과를 얻어야만 한다. 
# 몇 가지 결과가 검색됐는지 확인하려면 (위의 명령문을) 선언한다.

driver.close()
# 마지막으로, 브라우저 창을 닫는다. 또한 우리는 close 메서드 대신에 quit 메서드를 call 할 것이다.
# close 메서드가 하나의 탭만 닫는 반면, quit 메서드는 전체 브라우저를 닫는다. 
# 그러나 만약 하나의 탭만 열려 있다면, 기본적으로 대부분의 브라우저들은 전체를 exit 할 것이다.