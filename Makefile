PYTHON ?= python

all:
	# Old method, maybe useful as a fallback
	#$(PYTHON) setup.py bdist_wheel
	$(PYTHON) -m build

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf .tox

test:
	tox
