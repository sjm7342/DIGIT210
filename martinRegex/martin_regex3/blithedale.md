Steps

1. I used \n{3,} to find and replaced with \n\n to format the text.
2. I used (\n\s*\n) to find and replaced with </p>$1<p> to section off each paragraph.
3. I used ^(.*+)$ to find and replaced with <line>\1</line> to try and section off each line,
4. I used ^<p>[IVXLCDM](.+)</p>$ to find and replaced with <title>\1</title> to section off chapters.
5. I used (<title>.+?</title>) to find and replaced with <chapter>\n\1 to start chapters.
6. I used (</p>.+?) to find and replaced with \n</chapter>\n to end chapters.
7. I used "(.+?)" to find and replaced with <quote>\1</quote> to find quotes.
8. I used <line>\s*([IVXLCDM]+\..*?)</line> to find and replaced with <title>\1</title> to give chapters title tags.