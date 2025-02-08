Steps

1. I added <xml> and <root> tags on the document.
2. I used ^([A-z]+):(.*)$ in the find section to try to capture all dialogue and colons.
3. I used \1:\n<sp>\2</sp> in the replace section to try to wrap <sp> tags around spoken dialogue. 
