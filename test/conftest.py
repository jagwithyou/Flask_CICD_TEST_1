import pytest
from selenium import webdriver
import time
import config
driver = None
from datetime import datetime
from pathlib import Path
import os

def pytest_addoption(parser):
    ''' This function adds a argument to choose the broweser '''
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    ''' Here we are doing setup for broweser and the url '''
    global driver
    #Getting the driver name and instantiating the driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=f"{config.DRIVER_PATH}/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=f"{config.DRIVER_PATH}\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    #opening the driver and maximizing the window
    driver.get(config.BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

reports_dir = ''
def create_report_folder():
    ''' Creates a report folder with the datetime stamp '''
    global reports_dir
    # if config is set to create individual report then create individual report with timestamp else create single report
    if config.INDIVIDUAL_REPORT:
        reports_dir = Path('reports', datetime.now().strftime('%y-%m-%d-%H-%M-%S'))
        reports_dir.mkdir(parents=True, exist_ok=True)
    else:
        reports_dir = Path('reports')
        if not os.path.exists(reports_dir):
            reports_dir.mkdir(parents=True, exist_ok=False)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    ''' Updates the default configurations of pytes '''
    # Create the project folder
    create_report_folder()
    # custom report file
    report = reports_dir / "report.html"
    # adjust plugin options (Updating the report path)
    config.option.htmlpath = report
    config.option.self_contained_html = True


from datetime import datetime
from py.xml import html
import pytest

def pytest_html_results_table_header(cells):
    ''' Adds two columns (Description and time) to the report table '''
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

def pytest_html_results_table_row(report, cells):
    ''' Adds row two column values to the row '''
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    ''' Saves the captured screenshot to the report directory '''
    global reports_dir
    #crate the test folder inside the report
    reports_dir = str(Path(reports_dir))
    if not os.path.exists(reports_dir+'/tests'):
        os.makedirs(reports_dir+'/tests')
    #save the screenshot
    driver.get_screenshot_as_file(reports_dir+'/'+name)

def pytest_html_report_title(report):
    ''' Adds title to the report '''
    report.title = config.REPORT_TITLE