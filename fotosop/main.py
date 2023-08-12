class a:
    def __init__(self,a):
        self.n = a
    def changen(self,a):
        self.n = a

def change (x):
    x.n = 5

x = a(20)
print(x.n)
change(x)
print(x.n)