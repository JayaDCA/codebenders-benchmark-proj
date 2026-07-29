import sys, time
# Bench fixture: a stand-in 'dev server' that streams output and stays up.
print('dev server starting on http://127.0.0.1:5000', flush=True)
for _i in range(1800):
    print(f'[dev_server] request {_i} handled', flush=True)
    time.sleep(1)
print('dev server shutting down', flush=True)
sys.exit(0)
