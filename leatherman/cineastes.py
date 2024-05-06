re1 = '(\d+)\. <a style="color:#333!important">'
repl1 = '\\1. <a id="header\\1" href="#annonce\\1" style="color:#333!important">'

re2 = '<p style="color:#111!important" name="annonce(\d+)">([^<\r]+)</p>'
repl2 = '<a style="color:#111!important" id="annonce\\1" href="#header\\1">\\2</a>'


import re

from pathlib import Path

content = Path("/Users/maximebettinelli/Desktop/a.html").read_text()
#assert len(re.findall(re1, content)) == 144, len(re.findall(re1, content))

Path("/Users/maximebettinelli/Desktop/out.html").write_text(
    re.sub(re2, repl2, 
           re.sub(re1, repl1, content)
           )
)
