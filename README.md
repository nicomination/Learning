# Project Setup with Makefile

This project uses a **Makefile** to manage the creation of a virtual environment, installation of dependencies, running tests, and starting the application. Below are the available commands and their functions.

## Prerequisites

Ensure that the following programs are installed on your system:

1. **Python 3** (version 3.x.x)
2. **Make**

You can verify the installations using:

```bash
python3 --version
make --version
```

## Commands

### 1. Create Virtual Environment

Create a virtual environment and install dependencies from the `requirements.txt` file:

```bash
make venv
```

This command creates a `.venv` directory and installs all necessary packages.

### 2. Run the Application

Start the application by executing the `main.py` script:

```bash
make run
```

This command ensures that the virtual environment exists and is activated before running the script.

### 3. Run Tests

Run all tests located in the `tests/` directory using `pytest`:

```bash
make test
```

The virtual environment will be created automatically if it doesn't exist yet.

### 4. Clean the Virtual Environment

Remove the virtual environment to clean up the project:

```bash
make clean
```

This command deletes the `.venv` directory completely.

## Makefile Overview

```makefile
.PHONY: run test venv clean

# Create virtual environment
venv:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

# Delete virtual environment
clean:
	rm -rf $(VENV_DIR)

# Run tests
test: venv
	$(VENV_DIR)/bin/pytest tests/

# Run the application
run: venv
	$(VENV_DIR)/bin/python main.py
```

## Notes

- **`requirements.txt`**: Ensure that all required dependencies are listed in the `requirements.txt` file.
- **Test Directory**: Place your tests in the `tests/` directory.
- The **`venv`** command is automatically executed with `run` and `test` if the virtual environment does not already exist.
