import glob
import re

def replace_fill_attribute(pattern):
    for filename in glob.glob(pattern):
        with open(filename, 'r+') as file:
            content = file.read()
            content_new = re.sub(r'(<rect[^>]*?)fill=".*?"', r'\1', content)
            content_new = re.sub(r'(<rect[^>]*?)stroke="black"', r'\1', content_new)
            file.seek(0)
            file.write(content_new)
            file.truncate()

replace_fill_attribute('*.svg')
