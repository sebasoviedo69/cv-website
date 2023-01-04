import pdfkit

# Additional options
# 'page-size': [width,height] #'A4', letter, legal
# 'page-width': '100',
# 'page-height': '100',

options = {
         'dpi': 92,
         'page-size': 'A4',
         'page-width': '210',
         'page-height': '305',
         'margin-top': '0.25in',
         'margin-right': '0.25in',  
         'margin-bottom': '0.25in',
         'margin-left': '0.25in',
         'encoding': "UTF-8",
         'custom-header' : [
            ('Accept-Encoding', 'gzip')
         ],
         'no-outline': None,
    }

pdfkit.from_file('index.html', 'docs/CV-sebastian-oviedo.pdf', options=options)