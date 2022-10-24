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
    values = [(1, 'user_local'), (2, 'user_group'), (3, 'user_forward'), (4, 'bot_action')]
    sql2 = '''
    INSERT INTO log_id (id, definition)
    VALUES 
    ($1, $2)
    ON CONFLICT DO NOTHING 
    '''
    for pair in values:
        await pool.execute(sql2, pair[0], pair[1])


async def create_table_logs(pool):
    sql = '''
    CREATE TABLE IF NOT EXISTS public.logs
    (
        datetime text NOT NULL,
        user_id bigint NOT NULL,
        type smallint NOT NULL,
        action text NOT NULL,
        CONSTRAINT "user" FOREIGN KEY (user_id)
            REFERENCES public.bot_users (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
            NOT VALID,
        CONSTRAINT log_type FOREIGN KEY (type)
            REFERENCES public.log_id (id) MATCH SIMPLE
            ON UPDATE NO ACTION
            ON DELETE NO ACTION
            NOT VALID
    );
       '''
    await pool.execute(sql)


async def run(pool):
    await create_table_users(pool)
    await create_table_log_types(pool)
    await create_table_logs(pool)
