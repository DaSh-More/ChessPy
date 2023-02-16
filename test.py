class Test:
    def __getattr__(self, path):
        return self.move(path)

    def move(self, path):
        def f():
            print('move to', path)
        return f


t = Test()
t.line()
