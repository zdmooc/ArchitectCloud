import psycopg2
import cx_Oracle

import pdb

## ------------
## Postgresql
## ------------
def pg_conn():
    U = "jiradb"
    P = "jiradb2000"
    H = "srajprod"
    p = "5432"
    D = "jiradb"
    connection = psycopg2.connect(user = U, password = P, host = H, port = p, database = D)
    return connection

def get_pg_cursor(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT count(*) from worklog;")
    return cursor

def get_pg_c1(cnx):
    cursor = cnx.cursor()
    req = """
        SELECT  id, issueid, author, grouplevel, rolelevel, worklogbody, created,
                updateauthor, updated, startdate, timeworked
        FROM worklog;
    """
    cursor.execute(req)
    return cursor

def pg_close(cnx, cursor):
    cursor.close()
    cnx.close()

## ------------
## Oracle
## ------------
def ora_conn():
    USER="test"
    PASSWORD="tiger"
    DB="VM-ORA-TEST/ORATEST"
    connection = cx_Oracle.connect(USER, PASSWORD, DB, encoding='UTF-8', nencoding='UTF-8')
    return connection

def get_ora_cursor(cnx):
    cursor = cnx.cursor()
    #cursor.execute("select count(*) from cat")
    cursor.execute("select * from worklog")
    return cursor

def ora_close(cnx, cursor):
    cursor.close()
    cnx.close()

## -------
## Test
## -------

def tst_ora():
    print("Test Oracle")
    cnx = ora_conn()
    r = get_ora_cursor(cnx)
    col_names = [row[0] for row in r.description]
    print(col_names)
    for result in r:
        print(result)
    ora_close(cnx, r)

def tst_pg():
    print("Test PostGreSQL")
    cnx = pg_conn()
    c = get_pg_c1(cnx)
    colnames = [desc[0] for desc in c.description]
    print("=> %s " % colnames )
    for r in c.fetchmany(10):
        print( r )
    pg_close(cnx, c)

def etl1():
    print("Début ETL 1")
    ## cnx PG
    print("Connexion PG")
    cnx_pg = pg_conn()

    ## cnx ora
    print("Connexion ORA")
    cnx_ora = ora_conn()

    ## purge table oracle 
    req = 'delete from worklog purge'
    c = cnx_ora.cursor()
    c.execute(req)
    cnx_ora.commit()
    c.close()

    ## recup des données 
    data_pg = get_pg_c1(cnx_pg)

    ## boucle insert
    req_insert = """ 
    insert into worklog 
    (ID, ISSUEID, AUTHOR, GROUPLEVEL, ROLELEVEL, WORKLOGBODY, CREATED, UPDATEAUTHOR, UPDATED, STARTDATE, TIMEWORKED)
    values
    ( :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11 )
    """
    c = cnx_ora.cursor()
    n = 1
    NB_RECORD=500
    while True:
        print("Insertion No %s " % n)
        d = data_pg.fetchmany(NB_RECORD)
        if d:
            n += 1
            for r in d:
                try:
                    c.execute(req_insert, r)
                except:
                    print(r)
                    raise
            cnx_ora.commit()
        else:
            break

    c.close()
    data_pg.close()


def main():
    #tst_pg()
    #tst_ora()
    etl1()

if __name__ == '__main__':
    main()
