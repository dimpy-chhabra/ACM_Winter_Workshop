for x in range(0, 3):
  try:
    print (10/x)
    print "Ahoy! %d" % (x)
  except ZeroDivisionError as err:
    print('Handling run-time error:', err)
