class Patient:
    def __init__(self, id, name, address, phone, vet):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__vet = vet
    '''
    def set_id(self, id):
        self.__id = id
    
    def set_vet(self,vet, answer):
        self.__vet = answer
    '''
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
    
    def get_vet(self):
        return self.__vet