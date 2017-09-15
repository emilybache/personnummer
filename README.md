Personnummer
============

This is a Python 3 module for generating random valid and invalid [Swedish personal numbers](https://en.wikipedia.org/wiki/Personal_identity_number_(Sweden)) for testing purposes.

To use it you will need to install the following python modules:

	- luhn
	- python-dateutil

For example using pip:

	$> pip install luhn python-dateutil

Usage
-----

The script includes help text which you can view by running it:

	$> personnummer.py --help

Sample usage:

	$> ./personnummer.py --count 5 --invalid-checksum
	19560512-3543
	19420326-2844
	19870204-3833
	19110902-1548
	19630228-4814

Self-tests
----------

To run the self-tests, use [py.test](https://docs.pytest.org):

	$> py.test

