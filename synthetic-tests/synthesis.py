import sys

n = int(sys.argv[1])

with open('template_header.c', 'r', encoding='utf-8') as input:
    header = input.read()
    header += '\n\n'

with open('template_body.c', 'r', encoding='utf-8') as input:
    body = input.read()

# Generate fpgen programs
block = 'injected_sum\n'
for i in range(n):
    block += '\twhile (L[0])\n'
    new_body = body.replace('// FLAG\n', block + '\tinjected_sum;\n')
    with open('fpgen/synthesized' + str(i+1) + '.c', 'w', encoding='utf-8') as output:
        output.write(header)
        output.write(new_body)

# Generate metrinome programs
header += "_local" # modify the klee include statement
