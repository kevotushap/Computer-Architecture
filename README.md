              simulator_pro README
# RISC-V Simulator README

## Overview

This simulator emulates a RISC-V CPU, allowing users to execute programs written in RISC-V assembly language. It supports a subset of instructions and provides a basic emulation environment for CPU execution. After processing the assembly code, the simulator outputs the final state of the CPU's registers and memory.

## Compiling the Source Code

To compile the source code, follow these steps:

1. Ensure Python 3 is installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project's root directory.
4. Install any required dependencies using the following command:

   ```bash
   pip install -r requirements.txt

## Command Line Parameters/Configurations

The simulator supports the following command-line parameters:

- `input_file`: Path to the input file containing the RISC-V assembly code.
- `output_file`: Path to the output file where the final register values will be written.

Example usage:

```bash
python simulator.py input_file.asm output_file.txt

#Running the Simulator
To run the simulator, execute the following command:

python simulator.py input_file.asm output_file.txt


     
Example Input File
An example input file (prog.txt) is provided in the examples directory. This file can be used to test the simulator. Ensure your assembly code follows the syntax and format specified by the simulator.





Additional Information


The simulator supports a subset of RISC-V instructions, including addi, fld, fmul, fadd, fsd, and bne.
Input files should follow a specific format, with memory content lines containing address-value pairs separated by a comma, and instruction lines following RISC-V assembly syntax.
