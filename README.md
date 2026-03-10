# Github_MCP_exp
Test repo for Github MCP tools

## Contents

This repository contains a simple Python script to test the setup.

### hello.py
A simple "Hello World" Python script.

**Usage:**
```bash
# Make the script executable (first time only)
chmod +x hello.py

# Run the script
./hello.py
```

or using Python directly:

```bash
python3 hello.py
``` 

### calc.py
A simple interactive terminal calculator.

**Setup and run:**
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 calc.py
```

Enter expressions in the form `<num> <op> <num>` where `op` is one of `+`, `-`, `*`, `/`.
Type `exit` or `quit` to leave the REPL.
