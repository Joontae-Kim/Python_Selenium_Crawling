#-*- coding: utf-8 -*- 
## http://selenium-python.readthedocs.io/installation.html
## 위의 튜토리얼을 연습하며 제가 공부하고, 연습한 필기노트 입니다. 
## 설명(주석처리) 및 코드는 위의 튜토리얼을 연습하며 제게 필요한 혹은 
## 알고 있으면 좋갰다고 생각한 내용들을 번역한 것입니다. 
## 문제 시 bexellenting@gmail.com으로 연락주시면 감사하겠습니다 .

# -------------------------------------------------------------------- #

## Chp1.1 - Introduction. 
# Selenium Python bindings는 Selenium WebDriver를 사용하여 기능 / 수용 테스트를 작성하는 간단한 API를 제공합니다. 
# Selenium Python API를 통해 직관적인 방식으로 Selenium WebDriver의 모든 기능에 액세스 할 수 있습니다.
# Selenium Python bindings는 Firefox, Ie, Chrome, Remote etc.와 같은 Selenium WebDriver에 접근할 수 있는 편리한 API를 제공합니다. 
# 현재 지원되는 파이썬 버전은 2.7. 3.5그리고 그 이상의 버전입니다.

# 위 URL 문서는 Selenium 2 WebDriver API를 설명한 것입니다.
# 여기서는 Selenium 1 / Selenium RC API는 포합되지 않습니다.

# -------------------------------------------------------------------------------------- #

## Chp1.2 - Downloading Python bindings for Selenium.
# 컴퓨터에 python이 설치되어 있다면, command shell에서 
# pip install selenium 을 통해 설치하시면 됩니다.

# -------------------------------------------------------------------------------------- #

## Chp1.3 - Drivers.
# Selenium은 선택된 브라우저와 인터페이스 할 드라이버가 필요합니다.
# 예를 들어 Firefox는 geckodriver가 필요합니다. geckodriver는 아래 예제를 실행하기 전에 설치해야합니다.
# 드라이버를 다운로드 한 후 경로를 기억하고 계시거나 메모해주셔야 합니다.
# 나중에 예제 실행 시 브라우저를 실행하기 위해 .exe 위치를 지정해야 하거든요.

# 지원되는 다른 브라우저들은 자체 드라이버가 제공됩니다.
# 일부 인기있는 브라우저 드라이버에 대한 링크가 이어집니다.
# Chrome - https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge - https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox - https://github.com/mozilla/geckodriver/releases
# Safari - https://webkit.org/blog/6900/webdriver-support-in-safari-10/

# -------------------------------------------------------------------------------------- #

## Chp1.4 - Detailed instructions for Windows users
# 주의 - 설치를 실행하기 위해서 인터넷에 연결되어 있어야 합니다.
# https://www.python.org/downloads/
# 1. 위 URL에에서 Python 3.6을 설치해주세요.
# 2. cmd.exe를 실행해 명령 프로프트를 시작하시고,  아래의 주어진 pip 명령어를 실행해 Selenium을 설치해주세요.
# C:\Python35\Scripts\pip.exe install selenium

# 지금부터 Python을 사용해 당신의 테스트 스크립트를 실행해보실 수 있습니다. 
# 예를 들어, 만약 Selenium 기반의 스크립트를 만들고, 
# C:\my_selenium_script.py에 저장했다면 당신은 아래와 같이 실행시킬 수 있습니다. 
# C:\Python35\python.exe C:\my_selenium_script.py

## 1.5. Downloading Selenium server
# - - (자바 내용으로 일단 생략) -- 

# -------------------------------------------------------------------------------------- #
## Chp1.  Installation은 여기까지!!!!