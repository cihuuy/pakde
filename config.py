
# Ports for your workers
STRATUM_HOST = "0.0.0.0"
STRATUM_PORT = 4052

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = 'RP6jeZhhHiZmzdufpXHCWjYVHsLaPXARt1'
# Only if you mine direct to the exchange
PAYMENT_ID = ''

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = False
MONITORING_EMAIL = 'aganagun553@gmail.com'

# Main pool
POOL_HOST = 'eu.luckpool.net'
POOL_PORT = 3956

# Failover pool
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'pool.hashvault.pro'
POOL_PORT_FAILOVER = 443

# ERROR, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = False
LOGFILE = "logfile.log"
