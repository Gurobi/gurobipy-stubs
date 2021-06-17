PYTHON ?= python

all:
	$(PYTHON) setup.py bdist_wheel

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

check:
	mypy -p gurobipy
