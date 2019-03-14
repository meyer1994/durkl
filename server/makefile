
compile:
	python -m compileall -f durkl tests


test:
	python -m coverage run --source=durkl -m unittest -vb discover tests


coverage: test
	python -m coverage report -m


lint:
	python -m flake8 --statistics
