Steps

1. First I used ^\s*([IVXLC]+)\s*$ in the find feature and <sonnet number="\1"> in the replace feature for the sonnet numbers.
2. Then I used ^(\s*)([\s*].*)$ in the find feature and \1<line>\2</line> in the replace feature for lines.
3. I used (<sonnet number="[^"]+) in the find feature and \1\n<sonnet> in the replace feature for sonnet distinctions.
4. Finally, I used (</line>)(\s*<sonnet number=") in the find feature and \1\n</sonnet>\n\2 in the replace feature to give the sonnets end brackets.
