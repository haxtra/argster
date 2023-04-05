#!/usr/bin/env python3

from argster import argster

tests = {

	'commands': {
		'input': 'cmd1 cmd2 cmd3 4',
		'spec': {},
		'test_cmd': ['cmd1', 'cmd2', 'cmd3', '4'],
		'test_arg': {}
	},

	'opts short': {
		'input': '-a -b -c=val',
		'spec': {},
		'test_cmd': [],
		'test_arg': {
			'a': True,
			'b': True,
			'c': 'val',
		}
	},

	'opts long': {
		'input': '--aaa --bbb --ccc=val',
		'spec': {},
		'test_cmd': [],
		'test_arg': {
			'aaa': True,
			'bbb': True,
			'ccc': 'val',
		}
	},

	'opts group': {
		'input': '-abc=val',
		'spec': {},
		'test_cmd': [],
		'test_arg': {
			'a': True,
			'b': True,
			'c': 'val',
		}
	},

	'cmd aliases': {
		'input': 'fo ba bz',
		'spec': {
			'fo|foo': None,
			'ba|bar': None,
			'bz|baz': None,
		},
		'test_cmd': ['foo','bar','baz'],
		'test_arg': {}
	},

	'opt aliases': {
		'input': '-abc=val',
		'spec': {
			'a|aaa': False,
			'b|bbb': False,
			'c|ccc': False,
		},
		'test_cmd': [],
		'test_arg': {
			'aaa': True,
			'bbb': True,
			'ccc': 'val',
		}
	},

	'opt long aliases': {
		'input': '--flg --opt=val',
		'spec': {
			'flg|flag': False,
			'opt|option': False,
		},
		'test_cmd': [],
		'test_arg': {
			'flag': True,
			'option': 'val',
		}
	},

	'defaults': {
		'input': '',
		'spec': {
			'a': 1,
			'b': False,
			'c': 'foo',
		},
		'test_cmd': [],
		'test_arg': {
			'a': 1,
			'b': False,
			'c': 'foo',
		}
	},

	'full': {
		'input': 'cm sc -abc=val --flg --opt=v2',
		'spec': {
			'cm|cmd': None,
			'sc|subcmd': None,
			'a': 1,
			'b|bbb': False,
			'c': 'noval',
			'd|ddd': 'def',
			'flg|flag': 'def',
			'opt|option': 'def',
		},
		'test_cmd': ['cmd','subcmd'],
		'test_arg': {
			'a': True,
			'bbb': True,
			'c': 'val',
			'ddd': 'def',
			'flag': True,
			'option': 'v2',
		}
	},
}


def print_error(*args):
	print('\033[1;91m✖\033[0m', *args)

errors = 0

for tid in tests:
	test = tests[tid]
	print('Test:', tid)

	try:
		args = argster(test['input'].split(), test['spec'])

		# test commands
		for cmd in test['test_cmd']:
			if cmd not in args['$']:
				errors += 1
				print_error('cmd "' + cmd + '" not found in commands')

		# test args
		for arg in test['test_arg']:
			if args[arg] != test['test_arg'][arg]:
				errors += 1
				print_error('arg "' + arg + '" error, expected', test['test_arg'][arg], 'got', args[arg],)

	except Exception as e:
		errors += 1
		print_error('test %s has thrown an exception' % tid)
		print('\x1b[41;1;38m')
		print(repr(e))
		import traceback
		traceback.print_exc()
		print('\x1b[0m\n')


if not errors:
	print('\n\033[1;92m[ok]\033[0m tests passed\n')
else:
	print('\n\033[1;91m[fail]\033[0m tests failed with', errors, 'errors\n' if errors > 1 else 'error\n')

from sys import exit
exit(errors)