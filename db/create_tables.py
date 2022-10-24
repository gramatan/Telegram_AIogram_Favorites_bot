from bot import bot


async def create_table_users(pool):
    sql = '''
    CREATE TABLE IF NOT EXISTS public.bot_users
    (
        id bigint NOT NULL,
        first_name text,
        username text,
        is_admin boolean,
        PRIMARY KEY (id)
    );
    '''
    await pool.execute(sql)


async def create_table_log_types(pool):
    sql = '''
    CREATE TABLE IF NOT EXISTS public.log_id
    (
        "id" smallint NOT NULL,
        definition text NOT NULL,
        PRIMARY KEY ("id")
    );
    '''
    await pool.execute(sql)
    values = [(1, 'local'), (2, 'group'), (3, 'forward')]
    sql2 = '''
    INSERT INTO log_id (id, definition)
    VALUES 
    ($1, $2)
    ON CONFLICT DO NOTHING 
    '''
    for pair in values:
        await pool.execute(sql2, pair[0], pair[1])


async def create_table_logs(pool):
    pass


async def run(pool):
    await create_table_users(pool)
    await create_table_log_types(pool)
    await create_table_logs(pool)
