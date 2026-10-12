# A Simple Python Brainfuck Interpreter

A simple Brainfuck interpreter written in Python. It parses and executes standard `.b` source files.

## Features
* Implements a standard 30,000-cell memory array with byte wraparound (`0–255`).
* Handles nested loops.
  
---

## Requirements
* Python 3.x installed on your system.

---

## How to Use

1. **Clone or Download** this repository into a local folder.
2. Ensure your Python script (`interpreter.py`) and your Brainfuck source files (`demo.b`) are in the same directory.
3. Open your terminal in that folder and run the script by passing your `.b` file as an argument:

```bash
python interpreter.py demo.b
