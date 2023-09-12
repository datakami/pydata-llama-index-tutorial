#!/usr/bin/env python
#source: https://github.com/brandon-rhodes/pycon-pandas-tutorial

import json

for notebook_type in ("Solutions", "Exercises"):
    contents = None
    for filename in ["build/colab_preamble.ipynb", f"{notebook_type}-1.ipynb", f"{notebook_type}-2.ipynb"]:
        f = open(filename)
        j = json.load(f)
        if not contents:
            contents = j
        else:
            contents["cells"] += j["cells"]
            
    with open(f"Colab-{notebook_type}.ipynb", 'w') as f:
        f.write(json.dumps(contents, indent=2))
