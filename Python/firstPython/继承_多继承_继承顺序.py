class A:
	def test(self):
		print("A------test 方法")
	def demo(self):
		print("A------demo 方法")
class B:
	def demo(self):
		print("B------demo 方法")
	def test(self):
		print("B------test 方法")
#class C(A, B):
class C(B, A):

	''''多继承可以让子类对象，同时继承对个父类的属性和方法'''
	pass


c = C()
c.test()
c.demo()
# 确定C类对象调用方法的顺序
print(C.__mro__)
print(C.__dir__)

