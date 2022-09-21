import redis
redis_part1 = redis.Redis(host='localhost', port=6379, db=0)
redis_part2 = redis.Redis(host='localhost', port=6377, db=0)

redis_part1.set('foo', 'bar')
redis_part1.get('foo')
print(redis_part1.get('foo'))

redis_part2.set('hola', 'chao')
redis_part2.get('hola')
print(redis_part2.get('hola'))

import psycopg2

# Connect to existing database
conn = psycopg2.connect(
    database="exampledb",
    user="docker",
    password="docker",
    host="127.0.0.1"
)

# Open cursor to perform database operation
cur = conn.cursor()


# Close communications with database
cur.close()
conn.close()