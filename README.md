# Introducing Python Data Contracts

With this package you can define your own data contracts strictly and define **data validations** and **pre-processing** steps which will insure data integrity and capable of serializing to-and-from JSON format. 

## Example Usage 
    from serializer import Interface
    class IP(Interface):

        # Declaring data type validations
        ip_address = str
        host_name = str

    class Record(Interface):
        user_name = str
        age = int
        ip = IP

        # Pre-processors to standardize data
        def __user_name__(value):
            return value.capitalize()
            
    args = {
        'user_name': 'ximi', 
        'age': 21, 
        'ip': IP(ip_address='192.168.2.1', host_name='localhost')
        }
    request = Record(**args)
    print ("Serializing from Object to JSON: \n", request.serialize())
    # Serializing from Object to JSON:  
    # {'user_name': 'Ximi', 'age': 21, 'ip': {'ip_address':'192.168.2.1', 'host_name': 'localhost'}}
    args = {
        'user_name': 'ximi', 
        'age': 21, 
        'ip': {
            'ip_address': '192.168.2.1',
            'host_name': 'localhost'
            }
        }
    request = Record(**args)
    print ("Serialise with Reverse type conversion: \n", request.serialize())
    # Serialise with Reverse type conversion: 
    # {'user_name': 'Ximi', 'age': 21, 'ip': {'ip_address': '192.168.2.1', 'host_name': 'localhost'}}


