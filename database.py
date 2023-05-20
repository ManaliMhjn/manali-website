import sqlalchemy
from sqlalchemy import create_engine, text

db_connection = "mysql+pymysql://re6ll02a1emeykyzs6oz:pscale_pw_VX9kybwUAwqWegSuSLTPJ08Y2tg3Fq3wJOVfLlxYVg8@aws.connect.psdb.cloud/manalicareers?charset=utf8mb4"
engine = create_engine(db_connection,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

# print("type(result): ", type(result))
# result_all = result.all()
# print("type(result_All(): ", type(result_all))
# print(result_all)
# print(type(result_all[0]))
# first_result_dict = result_all[0]._asdict()
# print("type of first relut: ", type(first_result_dict))
# print(first_result_dict)
