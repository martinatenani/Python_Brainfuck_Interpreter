import sys 

def interpret(filename):
    with open(filename, "r") as f:
        code = f.read()

    memory = [0]*30000
    data_ptr = 0 #cell index (Data Pointer)
    pc = 0 #instruction pointer
    code_len = len(code)

    while pc < code_len:
        cmd = code[pc]
        match cmd:
            case '+':
                memory[data_ptr] = (memory[data_ptr] + 1) % 256
            case '-':
                memory[data_ptr] = (memory[data_ptr] - 1) % 256
            case '>':
                data_ptr += 1
                if(data_ptr >= len(memory)):
                    print("Memory overflow")
            case '<':
                data_ptr = max(0, data_ptr - 1)
            case '.':
                print(chr(memory[data_ptr]), end='')
            case ',':
                char = sys.stdin.read(1)
            case '[':
                if memory[data_ptr] == 0:
                    depth = 1
                    while depth > 0:
                        pc += 1
                        if pc >= code_len:
                           raise SyntaxError("Unmatched '['")
                        if code[pc] == '[':
                            depth += 1
                        elif code[pc] == ']':
                            depth -= 1
            case ']':
                if memory[data_ptr] != 0:
                    depth = 1
                    while depth > 0:
                        pc -= 1
                        if pc < 0:
                            raise SyntaxError("Unmatched ']")
                        if code[pc] == ']':
                            depth += 1
                        elif code[pc] == '[':
                            depth -= 1

        pc += 1

if __name__ == "__main__":

    if len(sys.argv)<2:
        print("USage: python interpreter.py <filename.b>")
        sys.exit(1)

    target_file = sys.argv[1]
    interpret("name.b")