import os
from barcode import generate
from StringIO import StringIO 
from genshi.template import TemplateLoader


def transform(tmpl_filename, html_filename, context):
	loader = TemplateLoader('templates', auto_reload=True)
	tmpl = loader.load(tmpl_filename)
	rendered = tmpl.generate(title=context['title'] , date=context['date'], images=context['images']).render('html', doctype='html')

	f = open(html_filename, 'w') 
	f.write(rendered)
	f.close()


if __name__ == '__main__':

	files = []	

	if not os.path.exists('output'):
    		os.makedirs('output')

	f = open('eancodes.txt')
	for l in f.readlines():
		l = l.strip()
		generate('EAN13', l, output=os.path.join('output', l))
		files.append(l + '.svg')
	
	f.close()

	transform('index.tmpl', os.path.join('output', 'index.html'), {'title': 'Generated EAN CODES', 'date':'now', 'images': files})



