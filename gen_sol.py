import os, re

pwd=os.getcwd
def ls():
	return os.listdir(pwd())

outfile = 'solutions.tex'

# A line of latex code
def ll(s):
	return s + '\n'

# Generate prologue for latex document
def gen_prologue(f):
	f.write(ll('\\documentclass[a4paper,notitle]{article}'))
	f.write(ll('\\author{}'))
	f.write(ll('\\date{}'))
	f.write(ll('\\title{}'))
	f.write(ll('\\include{defs/basedef}'))
	f.write(ll('\\usepackage[margin=1truein]{geometry}'))


# For consistency
def gen_epilogue(f):
	pass

# Start document content
def start_doc(f):
	f.write(ll('\\begin{document}'))

# End document
def end_doc(f):
	f.write(ll('\\end{document}'))

# Compare two problem numbers and decide which comes first
def cormen_cmp(a, b):
	# A pattern for problem numbers. Matches 17.2-3 or 17-2
	prob_pat = "(\d+)([\.-])(\d+)(?:[-](\d+))?"
	(achap, ap, asec, anum) = re.search(prob_pat, a).groups()
	(bchap, bp, bsec, bnum) = re.search(prob_pat, b).groups()

	(achap, asec, anum) = map(int, (achap, asec, anum))
	(bchap, bsec, bnum) = map(int, (bchap, bsec, bnum))
	if achap - bchap != 0:
		return achap - bchap
	# Not from the same chapter
	if ap != bp:
		if ap == ".": return -1 # a is excercise, b is problem
		else: return 1 # a is problem, b is excercise
	# Note:- If a and b are problems and from same chapter if is true
	if asec - bsec != 0:
		return asec - bsec
	return anum - bnum

def include_sol(f, sol):
	f.write(ll('\\solinput{%s}' % (sol,)))
	f.write(ll('')) # A blank line to start next solution in another line


# Now the processing part of algorithm

# Get all tex files
tex_files = filter(lambda x: re.search("\.tex$", x), ls())
if outfile in tex_files:
	tex_files.remove(outfile) # Don't include any previous outputs

# Remove the .tex suffix
tex_files = map(lambda x: re.sub("\.tex", "", x), tex_files)

f = open(outfile, 'w')

gen_prologue(f)

start_doc(f)

tex_files.sort(cormen_cmp)

# Include input statement for each file
for i in tex_files:
	include_sol(f, i)

end_doc(f)

gen_epilogue(f)
