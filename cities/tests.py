from django.test import TestCase


# Create your tests here.
class Test:
    s = ['1', '2', '3']
    name = ''

    def foo(self):
        return self.s * 2

    def __str__(self):
        return self.name + '!!!'


ee = Test()
ee.name = 'TT'
print(ee)