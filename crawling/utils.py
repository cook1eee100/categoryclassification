import re



doublespace_pattern = re.compile('\s+')
lineseparator_pattern = re.compile('\n+')

def normalize_text(text):
    #text = text.replace('\t', ' ')
    #text = text.replace('\r', ' ')
    #text = lineseparator_pattern.sub('\n', text)
    text = doublespace_pattern.sub(' ', text)
    return text.strip()


def normalize_number(text):
    text = re.findall('\d+', text)
    text = int(''.join(text))
    return text