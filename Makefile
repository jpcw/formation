test: nosetests flake8
nosetests:
	@echo "==== Running nosetests ===="
	@nosetests  docs/source/chapters/* src/*
flake8:
	@echo "==== Running Flake8 ===="
	@flake8 src/jpcw/formation *.py

