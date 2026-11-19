from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re

class DashAdderInlineProcessor(Preprocessor):
    # add dashes to headings

    def run(self, lines):
        new_lines = []
        for line in lines:
            m = re.search(r'^## (.*)', line)
            if not m:
                new_lines.append(line)
            else:
                new_lines.append(f'## &#8212; {m.group(1)} &#8212;')
        return new_lines

class DashAdderExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(DashAdderInlineProcessor(md), 'fortressnebula_dashadder', 999)