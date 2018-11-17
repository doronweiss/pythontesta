contacts = {'David': '555-0123', 'Tom': '555-5678'}
contacts['Nora'] = '555-2413'
print(contacts)
name="Tomy"
if name in contacts.keys():
    print(contacts[name])
else:
    print ("Name {} not found".format(name))
print(len(contacts))