# Фреймворк для автоматизации тестирования сайта и мобильного приложения "Онлайн кинотеатр Ivi"
> <a target="_blank" href="https://www.ivi.ru/">ivi.ru</a>

![main page screenshot](/ivi_ui_and_mobile_test_framework/pictures/base_page_web.jpg)

----

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Запуск web/UI автотестов в Selenoid
* Запуск mobile автотестов в BrowserStack
* Для запуска mobile автотестов используется Appium

### Список проверок, реализованных в web/UI автотестах

- [x] Главная страница сайта отображается
- [x] Страница фильма отображается
- [x] Промо страница отображается
- [x] Найти фильм в поиске возможно
- [x] Раздел "Что нового" отображается
- [x] Открыть страницу "Фильмы" через верхнее меню возможно
- [x] Открыть страницу "Сериалы" через верхнее меню возможно
- [x] Открыть страницу "Мультфильмы" через верхнее меню возможно

### Список проверок, реализованных в mobile автотестах

- [x] Элементы управления отображаются
- [x] Раздел "Сериалы" отображается
- [x] Раздел "Профиль" отображается

----

### Используемый стэк

<img title="Python" src="ivi_ui_and_mobile_test_framework/pictures/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="ivi_ui_and_mobile_test_framework/pictures/icons/pytest-original.svg" height="40" width="40"/> <img title="Jira" src="ivi_ui_and_mobile_test_framework/pictures/icons/jira-original.svg" height="40" width="40"/> <img title="Allure Report" src="ivi_ui_and_mobile_test_framework/pictures/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="ivi_ui_and_mobile_test_framework/pictures/icons/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="ivi_ui_and_mobile_test_framework/pictures/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="ivi_ui_and_mobile_test_framework/pictures/icons/selenoid.png" height="40" width="40"/> <img title="Selenium" src="ivi_ui_and_mobile_test_framework/pictures/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="ivi_ui_and_mobile_test_framework/pictures/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="ivi_ui_and_mobile_test_framework/pictures/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="ivi_ui_and_mobile_test_framework/pictures/icons/tg.png" height="40" width="40"/> <img title="Jenkins" src="ivi_ui_and_mobile_test_framework/pictures/icons/jenkins-original.svg" height="40" width="40"/> <img title="Appium" src="ivi_ui_and_mobile_test_framework/pictures/icons/appium.svg" height="40" width="40"/> <img title="BrowserStack" src="ivi_ui_and_mobile_test_framework/pictures/icons/browserstack.svg" height="40" width="40"/>

----

### Локальный запуск автотестов

#### Для запуска web/UI автотестов выполнить в cli:
> [!NOTE]
> Ключ выбора версии `--browser-version` не обязателен
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --browser-version=100 ./tests/web/
```

#### Для запуска mobile автотестов выполнить в cli:
> [!NOTE]
> Ключ `--context` не обязателен, по умолчанию тесты будут запущены на BrowserStack
* Для запуска на реальном устройстве указать ключ `--context=local_real_device`
* Для запуска на виртуальном устройстве указать ключ `--context=local_real_device`
* Для запуска на BrowserStack указать ключ `--context=bstack`

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=bstack ./tests/mobile/
```

#### Для запуска всех автотестов выполнить в cli:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -s -v
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/">Ссылка</a>

#### Параметры сборки
> [!NOTE]
> Параметры сборки не обязательны
```python
ENVIRONMENT = ['STAGE', 'PREPROD', 'PROD'] # Окружение
COMMENT = 'some comment' # Комментарий
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/">проект</a>

![jenkins project main page](ivi_ui_and_mobile_test_framework/pictures/jenkins_project_main_page.png)

2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать любое окружение
4. В поле "COMMENT" ввести комментарий
5. Нажать "Build"

![jenkins_build](ivi_ui_and_mobile_test_framework/pictures/jenkins_build.png)

----

### Allure отчет
#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/">Общие результаты</a>
![allure_report_overview](ivi_ui_and_mobile_test_framework/pictures/allure_report_overview.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#suites">Результаты прохождения теста</a>

![allure_reports_behaviors](ivi_ui_and_mobile_test_framework/pictures/allure_reports_suites.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#graph">Графики</a>


![allure_reports_graphs](ivi_ui_and_mobile_test_framework/pictures/alluere_reports_graphs_1.png)
![allure_reports_graphs](ivi_ui_and_mobile_test_framework/pictures/alluere_reports_graphs_2.png)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3910/dashboards">Ссылка на проект</a>

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/dashboards">Дашборд с общими показателями тестовых прогонов</a>

![allure_test_ops_dashboards](ivi_ui_and_mobile_test_framework/pictures/allure_testops_dashboards.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/launches">История запуска тестовых наборов</a>

![allure_testops_launches](ivi_ui_and_mobile_test_framework/pictures/allure_testops_launches.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/test-cases/28510?treeId=0">Тест кейсы</a>

![allure_testops_suites](ivi_ui_and_mobile_test_framework/pictures/allure_testops_suites.png)

#### <a target="_blank" href="https://allure.autotests.cloud/launch/33573/tree/551292/attachments?treeId=0">Тестовые артефакты</a>

![allure_testops_suites](ivi_ui_and_mobile_test_framework/pictures/allure_testops_test_attachments.png)

#### <a target="_blank" href="https://allure.autotests.cloud/project/3910/test-cases/28510?treeId=0">Ручной запуск авто теста из Allure TestOps</a>

![allure_testops_suites](ivi_ui_and_mobile_test_framework/pictures/allure_testops_manual_test_run.png)

1. Нажать на чек-бокс необходимого тест кейса
2. Нажать на "Bulk actions"
3. Нажать на "Run"

----

### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1021">Ссылка на проект</a>

![jira_project](ivi_ui_and_mobile_test_framework/pictures/jira_project.png)

----

### Оповещения в Telegram
![telegram_allert](ivi_ui_and_mobile_test_framework/pictures/telegram_allert.png)

----

### Видео прохождения web/UI автотеста
![autotest_gif](ivi_ui_and_mobile_test_framework/pictures/autotest.gif)

----

### Видео прохождения mobile автотеста
![autotest_gif](ivi_ui_and_mobile_test_framework/pictures/test_mobile_video.gif)