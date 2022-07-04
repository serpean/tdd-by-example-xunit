class TestCase:
    def __init__(self, name):
        self.name = name
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        exec("self." + self.name + "()")
        self.tearDown()