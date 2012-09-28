import timeit
import time

def print_timing(func):
	def wrapper(*arg):
		t1 = time.time()
		res = func(*arg)
		t2 = time.time()
		print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.00)
		return res
	return wrapper

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  @print_timing
  def __call__(self, *args):
    try:
      return self.memoized[args]
    except KeyError:
      self.memoized[args] = self.function(*args)
      return self.memoized[args]

@memoize
def fact(n):
	if n > 1:
		return n*fact(n-1)
	else:
		return 1
@print_timing
def fact2(n):
	if n > 1:
		return n*fact(n-1)
	else:
		return 1
def main():
#	for i in xrange(1, 100):
		print str(1000) + "  :  " + str(fact(1000))
#	return

#	for i in xrange(1, 100):
		print str(1000) + "  : " + str(fact2(1000))
#	return


if __name__ == "__main__":
	main()
