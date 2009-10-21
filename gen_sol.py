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

def include_sol(f, sol):
	f.write(ll('\\solinput{%s}' % (sol,)))


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

# Include input statement for each file
for i in tex_files:
	include_sol(f, i)

end_doc(f)

gen_epilogue(f)
