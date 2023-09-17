#!/usr/bin/python
# adapted from: https://github.com/brandon-rhodes/pycon-pandas-tutorial

import glob
import json
import os
import re

def blank_code_cell(id):
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": id,
        "metadata": {},
        "outputs": [],
        "source": [],
    }

def question_cell(text, id):
    return {
        "cell_type": "markdown",
        "id": id,
        "metadata": {},
        "source": ['### ' + text.strip()],
    }


def convert(filename):
    with open(filename) as f:
        j = json.load(f)
    j['cells'] = list(filter_cells(filename, j['cells']))
    assert 'Solutions' in filename
    with open(filename.replace('Solutions', 'Exercises'), 'w') as f:
        json.dump(j, f, indent=1)
        f.write("\n")

def filter_cells(filename, cells):
    n = 0
    active_question = False
    for cell in cells:
        # clear error messages, outputs, etc. 
        if cell.get('outputs'):
            cell['outputs'] = []
        
        if cell['cell_type'] != 'code':
            active_question = False
            yield cell
            continue
        
        source = u''.join(cell['source'])

        if not active_question:
            if not source.startswith('# '):
                yield cell
            else:
                active_question = True

        if not source.startswith('# '):
            continue

        question = []

        for line in cell['source']:
            if not line.startswith('# '):
                break
            question.append(line[2:].strip())

        question = ' '.join(question)

        # deterministic cell ids across multiple runs
        yield question_cell(question, id=cell["id"] + "-q")

        yield blank_code_cell(id=cell["id"] + "-a1")
        yield blank_code_cell(id=cell["id"] + "-a2")

        n += 1
    print('{:6}   {}'.format(n, filename))

def main():
    for filename in sorted(glob.glob('Solutions-*.ipynb')):
        convert(filename)

if __name__ == '__main__':
    main()
