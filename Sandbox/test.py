import jaydebeapi

import jaydebeapi
conn = jaydebeapi.connect("org.h2.Driver", # driver class
                            "jdbc:h2:tcp://localhost/~/test", # JDBC url
                            ["sa", ""], # credentials
                            "/home/sumer/Desktop/Hmm/Major/Search/Sandbox/h2-1.4.200.jar",) # location of H2 jar
try:
        curs = conn.cursor()
        # Fetch the last 10 timestamps
        curs.execute("create table letssss")
        for value in curs.fetchall():
                # the values are returned as wrapped java.lang.Long instances
                # invoke the toString() method to print them
                print(value[0].toString())
finally:
        if curs is not None:
                curs.close()
        if conn is not None:
                conn.close()
