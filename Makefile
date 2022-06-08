.PHONY:clean

test:
	poetry run tox -e py38,py39,py310

build:
	poetry build

release: test build
	poetry publish --builds=sdist,wheel

clean:
	find -L . -type d -name "__pycache__" -print0 | xargs -0 rm -rf
	rm -rf .pytest_cache .tox dist