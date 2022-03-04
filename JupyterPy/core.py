from nbformat import read, NO_CONVERT
from pathlib import Path
import regex as re

class j2p:
    '''
    Automation API to convert Jupyter Notebook (*.ipynb) JSON 
    format into Python file (*.py), with the capabilities to add magic functions
    to determine which cells to be exported.

    Args:
        magic -> str: "magic" keyword to identify the code cells to be parsed
        jupyter_file -> str: path to the Jupyter notebook (.ipynb)
        output_file -> str: path to the output file (.py)
        output_mode -> str: mode for open() in the write() for the output_file. 
                                - "w" for write-only
                                - "a" for appending
    '''
    def __init__(self, jupyter_file, output_file, magic="#@EXPORT", output_mode="w" ):


        self.magic = str(magic)
        self.jupyter_file = Path(jupyter_file)
        self.output_file = Path(output_file)
        self.output_mode = output_mode

        # extract jupyter
        self.ipynb, self.code_cells = self.extract_jupyter()

        # write to .py file
        self.write_to_py()

    def extract_jupyter(self):
        with open(self.jupyter_file, "r") as ipynb_file:
            ipynb = read(ipynb_file, NO_CONVERT)
        
        cells = ipynb["cells"]            
        code_cells = [cell for cell in cells if cell["cell_type"] == "code" if self.magic in cell["source"] if "#@EXCLUDE@" not in cell["source"] ]

        return ipynb, code_cells
    
    def write_to_py(self):
        with open(self.output_file, self.output_mode) as py:
            for cell in self.code_cells:
                py.write(re.sub(self.magic,"", cell["source"]))

    def __repr__(self):
        return f"Extracted '{self.magic}' codes from {self.jupyter_file} into {self.output_file}"

