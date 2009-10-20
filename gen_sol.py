import os, re

pwd=os.getcwd
def ls():
	return os.listdir(pwd())

outfile = 'solutions.tex'

print ls()

# Get all tex files
tex_files = filter(lambda x: re.search("\.tex$", x), ls())
print tex_files
if outfile in tex_files:
	tex_files.remove(outfile) # Don't include any previous outputs

# Remove the .tex suffix
tex_files = map(lambda x: re.sub("\.tex", "", x), tex_files)
print tex_files

f = open(outfile, 'w')

f.write('\\input defs/basedef.tex\n')
# Include input statement for each file
for i in tex_files:
	f.write('\\solinput{%s}\n' % (i,))

f.write('\\bye\n')