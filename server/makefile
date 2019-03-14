
compile:
	python -m compileall -f durkl tests


test:
	python -m coverage run --source=durkl -m unittest discover -vb tests


coverage: test
	python -m coverage report -mi


lint:
	python -m flake8 --statistics
