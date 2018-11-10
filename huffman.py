class Huffman():
	"""key = character, val = freq"""
	def __init__(self):
		self.forest = forest
		self.freqs = array[0]*257
		self.huff_tree = None
		self.encode_counter = 0
		# self.byte = 0
		self.decode_node == None

	def build_forest():
		for i in range(256):
			HForest::add_tree(i, self.freqs[i])
		return forest
	def build_huff_tree():
		while forest.size() > 1:
			t1 = forest.pop_top()
			t2 = forest.pop_top()
			t3 = HTree::HTree(-1, (t1.get_val()+t2.get_val))
			HForest::add_tree(t3)
		self.huff_tree = t3
		return
	def path_to_bits(str path):
		# byte = 0
		path = []
		for char in path:
			if char == "l":
				path.append(False)
			else:
				path.append(True)
				# byte.flip_LSB
				# byte.right_shift
		return path

		"""what about the potential extra zeroes here? Or what if it spills over?"""
	def encode(char c):
		build_forest()
		build_huff_tree()
		c == ascii(c)
		path = HTree.path_to(c)
		path = path_to_bits(path)
		self.freqs[c] += 1	
		for turn in path:
			BitIO::output_bit(turn)
		return path
	def decode(bt bit):
		if self.decode_node == None:
			build_forest()
			build_huff_tree()
			node = self.huff_tree
		else:
			node = self.decode_node
			if bit == 0:
				next = node.get_child(LEFT)
			elif bit == 1:
				next = node.get_child(RIGHT)
			if next.get_key() == -1:
				decode_node = next
				return -1
			else:
				self.freqs[next.get_key()] += 1
				build_forest()
				build_huff_tree()
				decode_node = huff_tree
				return next.get_key()




		