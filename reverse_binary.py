

def binary_reverse(num):
	rev = 0
	while num > 0:
		#print 'num:', num
		tail = get_tail(num)

		rev = append(rev, tail)

		num = num >> 1

	return rev


def append(num, bit):
	num = num << 1
	num = num | bit
	return num



def get_tail(num):
	return num & 1


def logit(num):
	print 'Number: %d, Binary: %s' % (num, bin(num))
	rev = binary_reverse(num)
	print 'Reversed: %d, Binary: %s' % (rev, bin(rev))

if __name__ == '__main__':
	print logit(13);
	print logit(47);
	print logit(0b101001);
	print logit(0b11111);