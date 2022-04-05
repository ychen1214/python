import re

s ='"orange", carnage, dongle,test'
#print(re.search('(?+<!\()(?<!eq )"(?!\)|\Z)',s))

print(re.search('(?<!,|,|^)',s))

#"(?<!,|,|^)"(?!\,|$)"
#(?<!,|,|^)"(?!,|$)

#r'\b\s*"(?!,|$)', '" "'

#(?<!\()(?<!eq )'(?!\)|\Z)