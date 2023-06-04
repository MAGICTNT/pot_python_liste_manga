class Style:
    code = 0
    label = ""

    def __int__(self, code, label):
        self.code = code
        self.label = label

    def get_code(self):
        return self.code

    def get_label(self):
        return self.label

    def set_code(self, new_code):
        self.code = new_code

    def set_label(self, new_label):
        self.label = new_label

    def to_string(self):
        return self.code, self.label
