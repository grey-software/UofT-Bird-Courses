"""
This type stub file was generated by pyright.
"""

class Options(object):
    KEY = ...
    def __init__(self):
        ...
    
    @property
    def binary_location(self):
        """
        Returns the location of the binary otherwise an empty string
        """
        ...
    
    @binary_location.setter
    def binary_location(self, value):
        """
        Allows you to set where the chromium binary lives

        :Args:
         - value: path to the Chromium binary
        """
        ...
    
    @property
    def capabilities(self):
        ...
    
    def set_capability(self, name, value):
        """Sets a capability."""
        ...
    
    @property
    def debugger_address(self):
        """
        Returns the address of the remote devtools instance
        """
        ...
    
    @debugger_address.setter
    def debugger_address(self, value):
        """
        Allows you to set the address of the remote devtools instance
        that the ChromeDriver instance will try to connect to during an
        active wait.

        :Args:
         - value: address of remote devtools instance if any (hostname[:port])
        """
        ...
    
    @property
    def arguments(self):
        """
        Returns a list of arguments needed for the browser
        """
        ...
    
    def add_argument(self, argument):
        """
        Adds an argument to the list

        :Args:
         - Sets the arguments
        """
        ...
    
    @property
    def extensions(self):
        """
        Returns a list of encoded extensions that will be loaded into chrome

        """
        ...
    
    def add_extension(self, extension):
        """
        Adds the path to the extension to a list that will be used to extract it
        to the ChromeDriver

        :Args:
         - extension: path to the \*.crx file
        """
        ...
    
    def add_encoded_extension(self, extension):
        """
        Adds Base64 encoded string with extension data to a list that will be used to extract it
        to the ChromeDriver

        :Args:
         - extension: Base64 encoded string with extension data
        """
        ...
    
    @property
    def experimental_options(self):
        """
        Returns a dictionary of experimental options for chrome.
        """
        ...
    
    def add_experimental_option(self, name, value):
        """
        Adds an experimental option which is passed to chrome.

        Args:
          name: The experimental option name.
          value: The option value.
        """
        ...
    
    @property
    def headless(self):
        """
        Returns whether or not the headless argument is set
        """
        ...
    
    @headless.setter
    def headless(self, value):
        """
        Sets the headless argument

        Args:
          value: boolean value indicating to set the headless option
        """
        ...
    
    def set_headless(self, headless: bool = ...):
        """ Deprecated, options.headless = True """
        self.headless = ...
    
    def to_capabilities(self):
        """
            Creates a capabilities with all the options that have been set and

            returns a dictionary with everything
        """
        ...
    


