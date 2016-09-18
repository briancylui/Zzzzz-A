# import thread

# def print_stuff():
#     while True:
#         print "hello"


# import signal
# import sys
# def signal_handler(signal, frame):
#         print('You pressed Ctrl+C!')
#         sys.exit(0)
# print('Press Ctrl+C')
# signal.pause()

# # thread.start_new_thread( print_stuff() )

# signal.signal(signal.SIGINT, signal_handler)
# # thread.start_new_thread( signal.signal(signal.SIGINT, signal_handler) )


try:
    while (True):
        print 'hello'
except (KeyboardInterrupt, SystemExit):
    print 'detected exit'
    raise
except:
    raise
    # report error and proceed
