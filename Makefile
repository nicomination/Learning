.PHONY: run test venv clean

# =============================================================================
# region virtual environment
# =============================================================================

VENV_DIR := .venv

venv:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV_DIR)

# =============================================================================
# region test & Run
# =============================================================================

test: venv
	$(VENV_DIR)/bin/pytest tests/

run: venv
	$(VENV_DIR)/bin/python main.py


