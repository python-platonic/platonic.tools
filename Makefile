SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	mypy platonic_website tests/**/*.py
	flake8 .
	doc8 -q docs

.PHONY: unit
unit:
	pytest

.PHONY: package
package:
	poetry check
	pip check
	# Ignoring sphinx@2 security issue for now, see:
  # https://github.com/miyakogi/m2r/issues/51
	safety check --full-report -i 38330

.PHONY: test
test: lint package unit

.PHONY: docs
.ONESHELL:
docs:
	cd docs && make dirhtml
