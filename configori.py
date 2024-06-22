
# Ports for your workers
STRATUM_HOST = "0.0.0.0"
STRATUM_PORT = 8080

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = '86P42DaNTvmBmMLM4oL5kL6tVQVo9FfsnJDTqj6VU76whVzjMdMbMa7PV3SHAQuNySan44ToXVFn3gwFmqeDb58t1xqNVAB'
# Only if you mine direct to the exchange
PAYMENT_ID = ''

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = True
MONITORING_EMAIL = 'aganagun553@gmail.com'

# Main pool
POOL_HOST = 'pool.hashvault.pro'
POOL_PORT = 80

# Failover pool
POOL_FAILOVER_ENABLE = True
POOL_HOST_FAILOVER = 'pool.hashvault.pro'
POOL_PORT_FAILOVER = 443

# ERROR, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = True
LOGFILE = "logfile.log"
