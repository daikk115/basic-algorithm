class Binary(object):
	"""docstring for Binary"""
	def __init__(self, value, left=None, right=None):
		super(Binary, self).__init__()
		self.left = left
		self.right = right
		self.value = value

def init_tree():
	left = Binary(1)
	right = Binary(4)
	center = Binary(3, left, right)
	left = center
	right = Binary(6)
	a = Binary(5, left, right)

	left = Binary(2)
	right = Binary(4)
	b = Binary(3, left, right)

	return a, b

def check(a, b):
	if a is None and b is not None:
		return False

	if a is not None and b is None:
		return False

	if a is None and b is None:
		return True
	print a.value, b.value
	if a.value == b.value:
		if check(a.left, b.left) and check(a.right, b.right):
			return True
		else:
			return False
	else:
		return False

if __name__ == '__main__':
	a, b = init_tree()
	print a.value, b.value
	print(check(a.left, b) or check(a.right, b)	)
