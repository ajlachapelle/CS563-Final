import sys

n = int(sys.argv[1])

with open('template_header.c', 'r', encoding='utf-8') as input:
    header = input.read()

with open('template_body.c', 'r', encoding='utf-8') as input:
    body = input.read()

# Generate fpgen programs
new_header = header + '\n\n'
block = 'injected_sum\n'
for i in range(n):
    block += '\twhile (L[0])\n'
    new_body = body.replace('// FLAG\n', block + '\tinjected_sum;\n')
    with open('fpgen/synth' + str(i+1) + '.c', 'w', encoding='utf-8') as output:
        output.write(new_header)
        output.write(new_body)

# Generate metrinome programs
new_header = header + '_local\n\n' # modify the klee include statement
block = 'sum\n'
for i in range(n):
    block += '\twhile (L[0])\n'
    new_body = body.replace('// FLAG\n', block + '\tsum;\n')
    with open('metrinome/synth' + str(i+1) + '.c', 'w', encoding='utf-8') as output:
        output.write(new_header)
        output.write(new_body)