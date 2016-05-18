class Binary(object):
	"""docstring for AB"""
	def __init__(self, value, left=None, right=None):
		super(AB, self).__init__()
		self.left = None
		self.right = None
		self.value = 0

def init_tree():
	pass
	return a, b

def check(a, b):
	if a.value == b.value:
		if check(a.left, b.left) and check(a.right, b.right):
			return True
		else:
			return False
	else:
		return False

if __name__ == '__main__':
	a, b = init_tree()
	print(check(a, b))