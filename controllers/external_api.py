url = "http://localhost:8069"
db="db_dev"
username="admin"
password="admin"

from plistlib import UID
import xmlrpc.client

common=xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version=common.version()
print("details :",version) 
uid = common.authenticate(db, username, password, {})
print("uid :::::::::> ",uid)
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
students=models.execute_kw(db, uid, password, 'school.student', 'search', [[]])
print("partners :::::::::> ",students)

