import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '37ac4869'.decode('hex')
P2P_PORT = 6094
ADDRESS_VERSION = 15

RPC_PORT = 6093
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'number7address' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 300*100000000 >> (height + 1)//420000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 420 # s
SYMBOL = 'N7'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Number7') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/number7/') if platform.system() == 'Darwin' else os.path.expanduser('~/.number7'), 'number7.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://moonblocks.com:7000/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://moonblocks.com:7000/address/'
TX_EXPLORER_URL_PREFIX = 'http://moonblocks.com:7000/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
