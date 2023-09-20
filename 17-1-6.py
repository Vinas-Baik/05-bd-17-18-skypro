import psycopg2

try:
    with psycopg2.connect(host='localhost',
                          database='test',
                          user='postgres',
                          password='12345') as conn_sql:

        with conn_sql.cursor() as cur_sql:

            cur_sql.execute('SELECT MAX(prof_id) FROM profile ')

            max_prof_id = int(cur_sql.fetchone()[0])



            cur_sql.execute('SELECT * FROM profile ')
            for row in cur_sql.fetchall():
                print(row)

            print('-----------')
            cur_sql.executemany('INSERT INTO profile VALUES (%s, %s, %s)',
                                [(max_prof_id+1, f'add {max_prof_id+1}', str(max_prof_id+1)),
                                 (max_prof_id+2, f'add {max_prof_id+2}', str(max_prof_id+2))])

            cur_sql.execute('INSERT INTO profile VALUES (%s, %s, %s)',
                             (max_prof_id+3, f'add {max_prof_id+3}', str(max_prof_id+3)))

            conn_sql.commit()

            cur_sql.execute('SELECT * FROM profile ')
            for row in cur_sql.fetchall():
                print(row)


finally:
    conn_sql.close()