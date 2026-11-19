from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re

class HeadingAugmenterInlineProcessor(Preprocessor):
    # add dashes or stuff to headings
    def __init__(self, heading_level, left_char, right_char, md = None):
        super().__init__(md)
        self.heading_level = heading_level
        self.left_char = left_char
        self.right_char = right_char

    def run(self, lines):
        new_lines = []
        for line in lines:
            m = re.search(r'^' + ('#'*self.heading_level) + r' (.*)', line)
            if not m:
                new_lines.append(line)
            else:
                new_lines.append(f'{'#'*self.heading_level} {self.left_char} {m.group(1)} {self.right_char}')
        return new_lines


class DashAdderExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(HeadingAugmenterInlineProcessor(2, '&#8212;', '&#8212;', md), 'fortressnebula_h2dashadder', 999)
        md.preprocessors.register(HeadingAugmenterInlineProcessor(6, '[', ']', md), 'fortressnebula_h6bracketadder', 998)