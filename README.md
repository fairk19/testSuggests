testSuggests
============
Для тестирования использовался python 3.4. Для установки зависимостей используйте pip

<code>pip install -r requirements.txt</code>

Для запуска тестов на разных браузерах используется Selenium-Grid.

Запускаем hub:
<code>java -jar selenium-server-standalone-2.40.0.jar -role hub</code>

Добавляем nodes по JSON:
<code>java -jar selenium-server-standalone-2.40.0.jar -role webdriver -nodeConfig selenium-nodes.cfg.json -Dwebdriver.chrome.driver=chromedriver.exe</code>

*Для chrome путь к драйверу:
<code>-Dwebdriver.chrome.driver=chromedriver.exe</code>

