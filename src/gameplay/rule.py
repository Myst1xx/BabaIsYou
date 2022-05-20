class Rule:
    def __init__(self, first, second):
        # first là giá trị trc chữ 'is', second là giá trị sau chữ 'is'
        self.first = first
        self.second = second

    def __repr__(self):
        return self.first + ' is ' + self.second