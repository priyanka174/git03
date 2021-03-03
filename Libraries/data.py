import configparser

def data1(section, key):
    config=configparser.ConfigParser()
    config.read("C:/Users/User/PycharmProjects/github03/Configuration/readdata.cfg")
    return config.get(section, key)

#print(data1('info', 'Application_URL'))


def data2(section, key):
    config=configparser.ConfigParser()
    config.read("C:/Users/User/PycharmProjects/github03/Configuration/elements.cfg")
    return config.get(section, key)

#print(data2('info1', 'username'))