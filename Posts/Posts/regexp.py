import re

pattern="\<p style.+\>"
chain="<p style=\"text-align: justify;\">Desde esta oficina tenemos como princip"
if re.search(pattern, chain):
    print re.sub(pattern, '', chain)
