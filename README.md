# Advent of Code 2022 ![status](https://github.com/pmareke/advent_of_code_2022/actions/workflows/python-app.yml/badge.svg)

## Solutions for the AoC 2022

- [X] [Day 1](https://adventofcode.com/2022/day/1)

## How to use this repo

- First install the dependencies with `make install`
- Then run the tests with `make test`

## How to check the code

This repository has a pre-commit hook whichs validates the following:
- `make check-typing` with `mypy`.
- `make check-format` with `black`.
- `make check-imports` with `isort`.
- `make check-style` with `flake8` and `pylint`.
