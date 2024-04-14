import sys

# Define the memory object
memory = {}


class Instruction:
    def __init__(self, opcode, operands):
        self.opcode = opcode
        self.operands = operands
        self.fields = {}  # Store decoded fields

    def decode(self):
        # Define fields for different instruction types
        if self.opcode in ['addi', 'add', 'sub', 'mul', 'div']:
            # Decode arithmetic instructions
            self.fields['op'] = 'arithmetic'
            self.fields['rd'] = self.operands[0]
            self.fields['rs1'] = self.operands[1]
            self.fields['imm'] = int(self.operands[2])
        elif self.opcode in ['fld', 'fsd']:
            # Decode load/store instructions
            self.fields['op'] = 'load_store'
            self.fields['fd'] = self.operands[0]
            parts = self.operands[1].split('(')
            self.fields['imm'] = int(parts[0])
            self.fields['rs1'] = parts[1].strip(')')
        # Add more conditions for other instruction types as needed


class CPU:
    def __init__(self, memory, NF=4, NI=16, NW=4, NR=16, NB=4):
        self.memory = memory
        self.instructions = []  # Placeholder for parsed instructions
        self.NF = NF  # Issue width
        self.NI = NI  # Instruction queue size
        self.NW = NW  # Number of instructions issued per cycle
        self.NR = NR  # Reorder buffer size
        self.NB = NB  # Number of Common Data Buses (CDB)
        self.clock_cycles = 0  # Initialize clock cycles to zero
        self.registers = {f'R{i}': 0 for i in range(32)}  # Initialize registers dictionary
        self.register_values = []  # Initialize register values list

    def run_simulation(self, file_path):
        # Parse input file and run simulation
        self.parse_input_file(r"C:\Users\KELVIN KIMUTAI\PycharmProjects\simulator\prog.txt")
        self.cycle_by_cycle_simulation()
        self.write_register_values_to_file()

    def parse_input_file(self, file_path):
        # Reading a plain text file
        with open(file_path, 'r') as file:
            instructions = file.readlines()
            for line in file:
                line = line.strip()  # Remove leading and trailing whitespace
                if line:  # Check if the line is not empty
                    if not line.startswith('%'):  # Ignore comments
                        self.instructions.append(line)

    def cycle_by_cycle_simulation(self):
        # Main simulation loop
        for cycle in range(self.clock_cycles):
            self.execute_cycle()
            # Update statistics or check termination conditions

    def execute_cycle(self):
        # Execute one cycle of simulation
        # Placeholder logic for updating register values
        # Increment clock cycles after each execution
        self.clock_cycles += 1
        # Placeholder logic for updating register values
        current_register_values = {}  # Create a dictionary to store current register values
        for reg, value in self.registers.items():
            current_register_values[reg] = value  # Copy register values to the current dictionary
        self.register_values.append(current_register_values)  # Store register values for the current cycle

    def write_register_values_to_file(self):
        # Write register values to a file
        with open('register_values.txt', 'w') as file:
            for cycle, values in enumerate(self.register_values, start=1):
                file.write(f"Clock Cycle {cycle}: Register values - {values}\n")

    def get_register_values(self):
        # Placeholder method to get register values
        return {'R0': 0, 'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0, 'R6': 0, 'R7': 0, 'R8': 0, 'R9': 0, 'R10': 0,
                'R11': 0, 'R12': 0, 'R13': 0, 'R14': 0, 'R15': 0, 'R16': 0, 'R17': 0, 'R18': 0, 'R19': 0, 'R20': 0,
                'R21': 0, 'R22': 0, 'R23': 0, 'R24': 0, 'R25': 0, 'R26': 0, 'R27': 0, 'R28': 0, 'R29': 0, 'R30': 0,
                'R31': 0}


class Simulator:
    def __init__(self):
        self.memory = {}  # Initialize memory
        self.registers = {f'R{i}': 0 for i in range(32)}  # Initialize registers
        self.pc = 0  # Program counter
        self.labels = {}  # Dictionary to store labels and their corresponding line numbers
        self.clock_cycles = 0  # Initialize clock cycles attribute
        self.register_values = []  # Initialize register values list

    def parse_input_file(self, file_path):
        instructions = []
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading and trailing whitespace
                if line and not line.startswith('%'):  # Ignore comments and empty lines
                    if ',' in line:  # Memory content line
                        parts = line.split(',')
                        if len(parts) == 2:
                            address, value = parts
                            # Extract numeric parts from the address and value
                            address = ''.join(filter(lambda x: x.isdigit(), address))
                            value = ''.join(filter(lambda x: x.isdigit(), value))
                            # Check if address and value are not empty
                            if address and value:
                                self.memory[int(address)] = int(value)
                            else:
                                print(f"Ignoring invalid memory content line: {line}")
                        else:
                            print(f"Ignoring invalid memory content line: {line}")
                    else:  # Instruction line
                        instructions.append(line)
        return instructions

    def execute_instruction(self, instruction):
        opcode, *operands = instruction.split()
        if opcode == 'addi':
            rd, rs1, imm = operands
            self.registers[rd] = self.registers[rs1] + int(imm)
        elif opcode == 'fld':
            fd, imm_rs1 = operands
            imm, rs1 = imm_rs1.split('(')
            rs1 = rs1.strip(')')
            address = self.registers[rs1] + int(imm)
            self.registers[fd] = self.memory[address]
        elif opcode == 'fmul':
            fd, fs1, fs2 = operands
            self.registers[fd] = self.registers[fs1] * self.registers[fs2]
        elif opcode == 'fadd':
            fd, fs1, fs2 = operands
            self.registers[fd] = self.registers[fs1] + self.registers[fs2]
        elif opcode == 'fsd':
            fs, imm_rs1 = operands
            imm, rs1 = imm_rs1.split('(')
            rs1 = rs1.strip(')')
            address = self.registers[rs1] + int(imm)
            self.memory[address] = self.registers[fs]
        elif opcode == 'bne':
            rs1, label = operands
            if self.registers[rs1] != 0:
                self.pc = self.labels[label]
        else:
            raise ValueError(f'Unsupported instruction: {instruction}')

    def execute_cycle(self):
        # Implementation of execute_cycle method
        pass

    def write_register_values_to_file(self, output_file):
        # Write register values to the output file
        with open(r"C:\Users\KELVIN KIMUTAI\PycharmProjects\simulator\.idea\register_values.txt", 'w') as file:
            for reg, value in self.registers.items():
                file.write(f"{reg}: {value}\n")
    def cycle_by_cycle_simulation(self):
        # Main simulation loop
        for cycle in range(self.clock_cycles):
            self.execute_cycle()
            # Update other simulation logic as needed

    def run_simulation(self, file_path, output_file_path):        # Parse input file and populate self.instructions
        instructions = self.parse_input_file(r"C:\Users\KELVIN KIMUTAI\PycharmProjects\simulator\prog.txt")
        self.clock_cycles = len(instructions)
        self.cycle_by_cycle_simulation()

        # After simulation completes, write register values to the specified file path
        self.write_register_values_to_file(
            r"C:\Users\KELVIN KIMUTAI\PycharmProjects\simulator\.idea\register_values.txt")

        # Main simulation loop
        for cycle in range(self.clock_cycles):
            self.execute_cycle()
            # Update other simulation logic as needed
            # For example, you can print the state after each cycle
            self.print_state()

    def print_state(self):
        # Print register values
        print("Register Values:")
        for reg, value in self.registers.items():
            print(f"{reg}: {value}")

        # Print memory contents
        print("\nMemory Contents:")
        for address, value in self.memory.items():
            print(f"{address}: {value}")

        # Print program counter
        print(f"\nProgram Counter (PC): {self.pc}")


if __name__ == "__main__":
    # Define the default input and output file paths
    default_input_file = input_file = r"C:\Users\KELVIN KIMUTAI\PycharmProjects\simulator\prog.txt"
    default_output_file = r"C:\Users\KELVIN KIMUTAI\PycharmProjects\simulator\.idea\register_values.txt"

    # Extract input and output file paths from command line arguments
    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = default_input_file
        output_file = default_output_file

    # Initialize memory object
    memory = {}

    # Initialize CPU object
    cpu = CPU(memory=memory)

    # Parse input file and populate self.instructions
    cpu.parse_input_file(r"C:\Users\KELVIN KIMUTAI\PycharmProjects\simulator\prog.txt")

    # Run simulation for CPU
    cpu.run_simulation(input_file)

    # Initialize Simulator object
    simulator = Simulator()

    # Parse input file and populate memory
    simulator.parse_input_file(r"C:\Users\KELVIN KIMUTAI\PycharmProjects\simulator\prog.txt")

    # Run simulation for Simulator
    simulator.run_simulation(input_file, output_file)
