class CDS:
    def __init__(self):
        self.value=0
        self.threshold=0

    def get_value(self):
        pass
    def margin(self):
        self.get_value()
        if self.value>=self.threshold:
            return True
        else:
            return False

