import os, re

date_pattern = re.compile(r"""^(.*?)
((0|1)?\d-       #month, 1x or x
(0|1|2|3)?\d)-   #date, 3x, 2x, 1x or x
(19|20)\d\d)     #year, 19xx or 20xx
(.*?)$
""", re.VERBOSE)

