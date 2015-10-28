for arg in sys.argv[1:]:
    try:
        f = open(arg, 'w')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()