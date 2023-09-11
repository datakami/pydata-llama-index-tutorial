#!/usr/bin/env python
import os, sys

print("[INFO] Python", sys.version)
if "VIRTUAL_ENV" in os.environ:
    print("[INFO] venv:", os.environ["VIRTUAL_ENV"])
if sys.version_info.major != 3 or sys.version_info.minor not in (8,9,10,11):
    print("[WARNING] Unsupported python version!")

print("[INFO] Testing imports...")
try:
    import llama_index, jupyterlab, loguru
except ImportError:
    print("[ERROR] /!\ Could not import some requirements, make sure you've installed everything " \
          "according to README.md")
    print("[INFO] python path set to:", sys.path)
    raise

print("[INFO] OK. Loading model...")
service_context = llama_index.ServiceContext.from_defaults(
  embed_model="local:sentence-transformers/all-minilm-l6-v2", chunk_size=256, llm=None
)

print("[INFO] OK. Testing model...")
service_context.embed_model.get_text_embedding('Sphinx of black quartz, judge my vow')

print("All OK!")
