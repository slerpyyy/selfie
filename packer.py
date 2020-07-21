from PIL import Image, ImageFilter
import os, sys, subprocess

img = Image.open("simplified.png")

def tree_generator(x, y, size):
	if size < 4:
		coord = (x, 255-y)
		return img.getpixel(coord)

	size = size // 2
	branch = []
	for c in range(4):
		tx = x + size * int(c  % 2)
		ty = y + size * int(c // 2)
		branch.append(tree_generator(tx, ty, size))

	maxval = 0
	minval = 256
	for item in branch:
		if type(item) is list: return branch

		if item > maxval: maxval = item
		if item < minval: minval = item

	amp = abs(maxval - minval)
	if amp > 10: return branch

	avg = sum(branch) / 4
	return avg

def tree_encoder(t):
	if type(t) is list:
		s = "+"
		for b in t:
			s += tree_encoder(b)
		return s
	b = int(t) // 16
	return "{:1x}".format(int(b))

tree = tree_generator(0, 0, 256)
code = tree_encoder(tree)

#code = "++0123+4567+89ab+cdef" # test

output_folder = "output/"
tmp_file = output_folder + "uncompressed.py"
out_file = output_folder + "sler.py"

if not os.path.exists(output_folder):
	os.makedirs(output_folder)

with open(output_folder + "code.txt", "w") as file:
	file.write(code)

template = ""
with open("template.py") as file:
	template = file.read().format(code)

with open(tmp_file, "w") as file:
	file.write(template)

subprocess.call("python crispy/cris.py {} -o {} -ml".format(tmp_file, out_file).split())
subprocess.call("python {}".format(out_file).split())
