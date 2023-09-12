#!/usr/bin/python
# adapted from: https://github.com/brandon-rhodes/pycon-pandas-tutorial

import glob
import json
import os
import re

def blank_code_cell():
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {
            "collapsed": True
        },
        "outputs": [],
        "source": [],
    }

def question_cell(text):
    return {
        "cell_type": "markdown",
        "metadata": {
            "collapsed": True
        },
        "source": '### ' + text.strip(),
    }


def convert(filename):
    f = open(filename)
    j = json.load(f)
    j['cells'] = list(filter_cells(filename, j['cells']))
    assert 'Solutions' in filename
    with open(filename.replace('Solutions', 'Exercises'), 'w') as f:
        f.write(json.dumps(j, indent=1))

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

        yield question_cell(question)

        yield blank_code_cell()
        yield blank_code_cell()

        n += 1
    print('{:6}   {}'.format(n, filename))

def main():
    for filename in sorted(glob.glob('Solutions-*.ipynb')):
        convert(filename)

if __name__ == '__main__':
    main()
