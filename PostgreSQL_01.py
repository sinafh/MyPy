import datetime

import db_connection
from Helpers import string_helper


# Main Code starts here!!!

focal_wallet_addr_list = [ '0xe2dbd4756f1749e20ed7f891403e70543e25298a' ]

print(focal_wallet_addr_list, "\n")


# conn_str = 'host=server2 port=5432 dbname=postgres user=sina13890'
# conn = psycopg2.connect(conn_str)

conn = db_connection.connect_db('postgres')

cursor = conn.cursor()

query = """
            SELECT 
                pk_id, erc20_token, erc20_from, erc20_to, erc20_value, block_timestamp
            FROM 
                eth_cleaned.tmp_erc20_xfers_tamp__v2 E
            WHERE 
                erc20_from = %s
                OR
                erc20_to = %s
            ORDER BY 
                block_timestamp;
        """
data = (focal_wallet_addr_list[0], focal_wallet_addr_list[0])

cursor.execute(query, data)

# print("The number of rows: ", cursor.rowcount)
# row = cursor.fetchone()
#
# while row is not None:
#     print(row)
#     row = cursor.fetchone()

print("The number of rows: {} \n".format(cursor.rowcount))
all_rows = cursor.fetchall()


print('pk_id\t\terc20_token\t\terc20_from\t\terc20_to\t\terc20_value\t\t\t\t\t\tblock_timestamp_tamp')
print('-----\t\t-----------\t\t----------\t\t--------\t\t-----------\t\t\t\t\t\t--------------------')

for row in all_rows:

    tamp = ''
    if row[5] is not None:
        tamp = datetime.datetime.utcfromtimestamp(row[5]).strftime('%Y-%m-%d %H:%M:%S')

    print("{0:10,}\t{1}\t\t{2}\t\t{3}\t\t{4:40,}\t{5} "
          .format(row[0],
                  string_helper.extract_0x_6_4(in_str=row[1]),
                  string_helper.extract_0x_6_4(in_str=row[2]),
                  string_helper.extract_0x_6_4(in_str=row[3]),
                  row[4],
                  tamp))


cursor.close()
conn.close()



