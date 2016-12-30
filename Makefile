project = structible

test: pytest codestyle docstyle

pytest:
	PYTHONPATH=. py.test --cov=$(project) tests

codestyle:
	pycodestyle $(project)

docstyle:
	pydocstyle $(project)
