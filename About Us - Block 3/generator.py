import os
import pyperclip

f = []
mypath = os.getcwd()
directories = os.listdir(mypath)
outtext = ''

for directory in directories:
	for (dirpath, dirnames, filenames) in os.walk(directory):
	    for filename in filenames:
	    	print(filename[-5:])
	    	if filename[-5:].lower() == '.html':
	    		relDirectory = './' + dirpath + '/' + filename
	    		studentName = dirpath.split('-')[-1].strip().replace('About Me', '')
	    		f.append(
	    			{
	    				"studentName" : studentName,
	    				"relDirectory" : relDirectory
	    			}
	    		)
	    		
	    print(dirpath)
	    break

for website in f:
	outtext += f'<li><a href="{website["relDirectory"]}">{website["studentName"]}</a></li>\n'

pyperclip.copy(outtext)
