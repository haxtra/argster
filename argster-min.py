def argster(argv, spec={}):
	""" argster v0.4 https://github.com/haxtra/argster """
	aliases = {}
	result = {'$':[]}
	for opt in spec:
		items = opt.split('|')
		if len(items) == 2:
			aliases[ items[0] ] = items[1]
			key = items[1]
		else:
			key = items[0]
		if spec[opt] is not None:
			result[key] = spec[opt]
	def expand_alias(arg):
		return aliases[arg] if arg in aliases else arg
	for arg in argv:
		if arg.startswith('-'):
			if arg.startswith('--'):
				if '=' in arg:
					pair = arg.split('=', 1)
					result[ expand_alias(pair[0][2:]) ] = pair[1]
				else:
					opt = expand_alias(arg[2:])
					result[opt] = True
			else:
				if '=' in arg:
					pair = arg.split('=', 1)
					result[ expand_alias(pair[0][-1]) ] = pair[1]
					for flag in pair[0][1:-1]:
						opt = expand_alias(flag)
						result[opt] = True
				else:
					for flag in arg[1:]:
						opt = expand_alias(flag)
						result[opt] = True
		else:
			result['$'].append(expand_alias(arg))
	return result