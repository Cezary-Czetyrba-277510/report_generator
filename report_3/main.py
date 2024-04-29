import os
from pathlib import Path

file_name = "lubie_plpacki.tex"
print(os.path.join(os.path.dirname(__file__), "data/", file_name))