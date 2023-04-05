#!/usr/bin/env python3

# minify argster for direct inclusion in other scripts
# strips comments and blank lines

with open('argster.py', 'r') as file:
    content = file.read()

out = []
for line in content.split('\n'):
    if line == '' or line.strip().startswith('#'):
        continue
    out.append(line)

with open('argster-min.py', 'w') as file:
    file.write('\n'.join(out[:-2])) # exclude .parse method
