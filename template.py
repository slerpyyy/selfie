from turtle import *

# hash for random subdivs
h = 4; up(); ht()

# create random subdivs
def r(n, l):
	global h
	h = hash(str(h)); s = n + (h&1) * (2**(l-7))
	if not l == 6: s = [r(s, l+1), r(s, l+1), r(s, l+1), r(s, l+1)] #[r(s, l+1) for _ in range(4)]
	return s

# convert string to tree
def p(s, l):
	a = []
	for c in "++++":
		s = s[1:]
		if s[0] == c: n, s = p(s, l+1); a += [n]
		#else: a += [int(s[0], 16)]
		else: a += [r(int(s[0], 16), l)]
	return a, s

# gen img from tree
def d(t, r, y, s):
	if type(t) == list:
		for c, n in enumerate(t): a = s/2; d(n, r + a*(c&1), y + a*(c//2), a)
	else: n = t/16; a = n**(20/21.); color(a*a*(3-a-a), n, n); goto(r, y); begin_fill(); fd(s); lt(90); fd(s); lt(90); fd(s); lt(90); fd(s); lt(90); end_fill()

# main func stuff
s = 512; setup(s+s, s+s); tracer(s, 0); d(p("{}", 0)[0], -s, -s, s+s); mainloop() #exitonclick()
