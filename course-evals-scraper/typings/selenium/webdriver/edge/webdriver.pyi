"""
This type stub file was generated by pyright.
"""

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from typing import Any, Optional

class WebDriver(RemoteWebDriver):
    def __init__(self, executable_path=..., capabilities: Optional[Any] = ..., port=..., verbose: bool = ..., service_log_path: Optional[Any] = ..., log_path: Optional[Any] = ..., keep_alive: bool = ...):
        """
        Creates a new instance of the chrome driver.

        Starts the service and then creates new instance of chrome driver.

        :Args:
         - executable_path - path to the executable. If the default is used it assumes the executable is in the $PATH
         - capabilities - Dictionary object with non-browser specific
           capabilities only, such as "proxy" or "loggingPref".
         - port - port you would like the service to run, if left as 0, a free port will be found.
         - verbose - whether to set verbose logging in the service
         - service_log_path - Where to log information from the driver.
         - log_path: Deprecated argument for service_log_path
         - keep_alive - Whether to configure ChromeRemoteConnection to use HTTP keep-alive.
         """
        self.port = ...
        self.edge_service = ...
    
    def quit(self):
        ...
    


