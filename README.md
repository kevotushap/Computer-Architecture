              simulator_pro README
Overview


This simulator is designed to execute programs written in RISC-V assembly language. It provides a basic emulation of a RISC-V CPU with support for a subset of instructions. The simulator reads assembly code from a file, executes the instructions, and outputs the final state of the CPU's registers and memory.


Compiling the Source Code


To compile the source code, follow these steps:
Make sure you have Python 3 installed on your system.
Clone the repository to your local machine.
Navigate to the root directory of the project.

Run the following command to install any required dependencies:


Copy code
pip install -r requirements.txt

Command Line Parameters/Configurations


The simulator supports the following command line parameters:

input_file: Path to the input file containing the RISC-V assembly code to be executed.
output_file: Path to the output file where the final register values will be written.


Example usage:


bash

Copy code

python simulator.py input_file.asm output_file.txt


Running the Simulator

To run the simulator, execute the following command:


bash

Copy code

python simulator.py input_file.asm output_file.txt

Replace input_file.asm with the path to your RISC-V assembly code file, and output_file.txt with the desired path for the output file containing the register values.


Example Input File

An example input file (prog.txt) is provided in the examples directory. You can use this file to test the simulator. Make sure your assembly code follows the syntax and format specified by the simulator.


Additional Information

The simulator supports a subset of RISC-V instructions, including addi, fld, fmul, fadd, fsd, and bne.

Input files should follow a specific format, with memory content lines containing address-value pairs separated by a comma, and instruction lines following the RISC-V assembly syntax.

