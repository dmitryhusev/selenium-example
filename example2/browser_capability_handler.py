class BrowserCapabilitiesHandler:

    def __init__(self):
        self.browserName = 'chrome'
        self.enableVNC = True
        self.sessionTimeout = '3m'
        self.screenResolution = '2560x1440x24'
        self.enableVideo = None

    def get_capabilities(self):
        return {
            'browserName': self.browserName,
            'enableVNC': self.enableVNC,
            'sessionTimeout': self.sessionTimeout,
            'screenResolution': self.screenResolution,
            'enableVideo': self.enableVideo
        }

    def set_to_default_state(self):
        self.browserName = 'chrome'
        self.enableVNC = True
        self.sessionTimeout = '3m'
        self.screenResolution = '2560x1440x24'
        self.enableVideo = None
