"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

class Service(object):
    def __init__(self, executable, port=..., log_file=..., env: Optional[Any] = ..., start_error_message=...):
        self.path = ...
        self.port = ...
        self.start_error_message = ...
        self.log_file = ...
        self.env = ...
    
    @property
    def service_url(self):
        """
        Gets the url of the Service
        """
        ...
    
    def command_line_args(self):
        ...
    
    def start(self):
        """
        Starts the Service.

        :Exceptions:
         - WebDriverException : Raised either when it can't start the service
           or when it can't connect to the service
        """
        ...
    
    def assert_process_still_running(self):
        ...
    
    def is_connectable(self):
        ...
    
    def send_remote_shutdown_command(self):
        ...
    
    def stop(self):
        """
        Stops the service.
        """
        ...
    
    def __del__(self):
        ...
    


