def drange(x_0, x_1, step):
	curr = float(x_0)
	while curr < (x_1):
		yield curr
		curr += float(step)


def integrate(f, x_0, x_1, step):
	acc = float(x_0)
	for dx in drange(x_0, x_1, step):
		acc += float(f(dx))
	return acc

