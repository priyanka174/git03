from Libraries import data
class pages2:
    def __init__(self, obj):
        global driver
        driver=obj
    def username(self, username):
        driver.find_element_by_name(data.data2('info1', 'username'))

    def email(self, email):
        driver.find_element_by_name(data.data2('info1', 'email'))