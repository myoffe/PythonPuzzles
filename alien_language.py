Letters = 3
DictSize = 5
TestCases = 4


class Node(object):
	def __init__(self, level=None, letter=None):
		self.children = []
		
		if None in (level, letter):
			raise Exception("level must be provided for Node ctor")

		self.level = level
		self.letter = letter


	def insert(self, word):
		first_letter = word[0]
		rest_of_word = word[1:]

		for child in self.children:
			if first_letter == child.letter:
				child.insert(rest_of_word)
				break
		else:
			new_child = self.create_child(first_letter)
			new_child.insert(rest_of_word)
		

	def find(self, word):
		first_letter = word[0]
		rest_of_word = word[1:]

		for child in children:
			if first_letter == child.letter:
				return child.find(rest_of_word)
		else:
			return False


	def create_child(self, letter):
		node = Node(self.level+1, letter)
		node.letter = letter
		self.children.append(node)

		return node




def create_tree(words):
	root = Node(0, '(root)')

	for word in words:
		root.insert(word)


def test(tree, subject):
	pass

if __name__ == '__main__':
	words = ['abc','bca','dac','dbc','cba']

	root = create_tree(words)

	test(root, [['a','b'], ['b','c'], ['c','a']])
	test(root, [['a'], ['b'], ['c']])
	test(root, [['a','b','c'], ['a','b','c'], ['a','b','c']])
	test(root, [['z','y','x'], ['b', ['c']]])

