from pyPdf import PdfFileWriter, PdfFileReader
import glob
output = PdfFileWriter()
files = glob.glob(r'./*.pdf')
for stuff in list(sorted(files)):
	input = PdfFileReader(file(str(stuff), "rb"))
	print "processing %s " % (stuff)
	output.addPage(input.getPage(0))
	
print "output has %s pages." % output.getNumPages()

outputStream = file("out.pdf", 'wb')
output.write(outputStream)
outputStream.close()

