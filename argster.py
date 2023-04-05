def argster(argv, spec={}):
	""" argster v0.4 https://github.com/haxtra/argster """

	aliases = {}
	result = {'$':[]}

	# parse spec, extract aliases and base values
	for opt in spec:
		items = opt.split('|')
		if len(items) == 2:
			# aliased
			aliases[ items[0] ] = items[1]
			key = items[1]
		else:
			# unaliased
			key = items[0]
		# items with value of None are not included
		if spec[opt] is not None:
			result[key] = spec[opt]

	def expand_alias(arg):
		# expand shorthand to full name
		return aliases[arg] if arg in aliases else arg

	# override with user args
	for arg in argv:
		if arg.startswith('-'):
			if arg.startswith('--'):
				# --opt|--opt=val
				if '=' in arg:
					# --opt=val
					pair = arg.split('=', 1)
					result[ expand_alias(pair[0][2:]) ] = pair[1]
				else:
					# --opt
					opt = expand_alias(arg[2:])
					result[opt] = True
			else:
				# -o|-o=val
				if '=' in arg:
					# -o=val / -opx=val
					pair = arg.split('=', 1)
					result[ expand_alias(pair[0][-1]) ] = pair[1]
					for flag in pair[0][1:-1]:
						opt = expand_alias(flag)
						result[opt] = True
				else:
					# -o / -opx
					for flag in arg[1:]:
						opt = expand_alias(flag)
						result[opt] = True
		else:
			# cmd/free
			result['$'].append(expand_alias(arg))

	return result


def parse(argv, spec={}):
	return argster(argv, spec)
