# input & output file EOL should be '\n' or a space
f = open("sample.in", mode="r+", encoding='utf-8')
lines_in = f.readlines()
f.close()

f = open("sample.out", mode="r+", encoding='utf-8')
lines_out = f.readlines()
f.close()

maxlen = max(len(lines_in), len(lines_out))

result = "\\begin{table}[H]\n"
result += "\\begin{tabularx}{\\textwidth}{|X|X|}\n"
result += "    \hline\n"
result += "    \\textbf{Standard Input} & \\textbf{Standard Output} \\\\\n"
result += "    \hline\n"

result += "    \\tablecell{\n"
for line in lines_in:
    result += "        " + line[0:-1] + " \\\\\n"
for i in range(len(lines_in), maxlen):
    result += "        \\\\\n"
result += "    } & \n"

result += "    \\tablecell{\n"
for line in lines_out:
    result += "        " + line[0:-1] + " \\\\\n"
for i in range(len(lines_out), maxlen):
    result += "        \\\\\n"
result += "    } \\\\ \n"
result += "    \hline\n"
result += "\end{tabularx}\n"
result += "\end{table}"

print(result)