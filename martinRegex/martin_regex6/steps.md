# Steps

1. I used (^CHAPTER\s+[IVXLCDM]+.*\n)(.*?) into the find feature and <chapter>$1</chapter> into the replace feature. However, I am struggling to get the whole text wrapped in the chapters.
2. I used (\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)) in the find feature and <date>$1</date> in the replace feature.
3. I used (.+?)(\n{2}|\Z) in the find feature and <p>\1</p> in the replace feature.
4. I used "([^"]+)" in the find feature and <quote>"$1"</quote> in the replace feature.
5. I used  [A-Z .’]+(?:JOURNAL|DIARY|MEMORANDUM|LOG|LETTERS).* in the find feature and <journal>/1</journal> in the replace feature for the journal tags..
6. Unfortunately, I've been trying and am struggling to figure out how to capture the letters.