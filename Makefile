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
