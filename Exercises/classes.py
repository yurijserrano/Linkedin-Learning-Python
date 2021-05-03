'''
Example file for working with classes
'''

class MyClass():
    def method1(self):
        print("MyClass method1")

    def method2(self, someString):
        print("MyClass method2 " + someString)

class AnotherClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print("AnotherClass method1")

    def method2(self, someString):
        print("AnotherClass method2 " + someString)

def main():
    c = MyClass()
    c.method1()
    c.method2("This is a string")

    c2 = AnotherClass()
    c2.method1()
    c2.method2("This is another string")

if __name__ == '__main__':
    main()