#!/usr/bin/env python2.7
#source: https://github.com/brandon-rhodes/pycon-pandas-tutorial

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
        f.write(json.dumps(j, indent=2))

def filter_cells(filename, cells):
    n = 0
    starting = True
    for cell in cells:
        if cell['cell_type'] != 'code':
            yield cell
            continue
        
        source = u''.join(cell['source'])

        if starting:
            if not source.startswith('# '):
                yield cell
            else:
                starting = False

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

def main2():
    for filename in sorted(glob.glob('Solutions-*.ipynb')):
        convert(filename)

if __name__ == '__main__':
    main2()
