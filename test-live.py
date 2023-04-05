#!/usr/bin/env python3
from sys import argv
from argster import argster

opts = argster(argv[1:], {
	'cmd|command': None,
	'sub|subcommand': None,
	'f|foo': 'fail',
	'b|bar': False,
	'baz': None,
	'l|leet': 1337,	})

for opt in opts:
	print(opt.rjust(10, ' '), ':', opts[opt])
