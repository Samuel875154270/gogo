import config
from playhouse.pool import PooledMySQLDatabase

# 使用连接池
database = PooledMySQLDatabase(database=config.mysql["db"], max_connections=300, **config.mysql["info"])
__all__ = ["database"]
