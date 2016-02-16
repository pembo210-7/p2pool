from p2pool.bitcoin import networks

PARENT = networks.nets['numberseven']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '37ac4869'.decode('hex')
P2P_PORT = 6093
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 6095
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#numberseven-n7'
VERSION_CHECK = lambda v: None if 1000000 <= v else 'numberseven version too old. Upgrade to 0.10.0 or newer!'
VERSION_WARNING = lambda v: None
