class TestStateHandler:
    # This class helps to handle how many times we already run certain test
    # to figure out when set enableVideo to True from BrowserCapabilitiesHandler class

    def __init__(self):
        self.failure_count = 0
        self.total_run_count = 0
        self.session_id = []

    def set_to_default_state(self):
        self.failure_count = 0
        self.total_run_count = 0
        self.session_id = []
