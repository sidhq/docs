import glob
import re

def replace_fill_attribute(pattern):
    for filename in glob.glob(pattern):
        with open(filename, 'r+') as file:
            content = file.read()
            content_new = re.sub(r'fill=".*?"', '', content)
            file.seek(0)
            file.write(content_new)
            file.truncate()

replace_fill_attribute('*.svg')
