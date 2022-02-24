class Procedure:
    def __init__(self, name, date, pract, charge, id):
        self.__name = name
        self.__date = date
        self.__pract = pract
        self.__charge = charge
        self.__pat_id = id

    def get_name(self):
        return self.__name
    
    def get_date(self):
        return self.__date

    def get_pract(self):
        return self.__pract
    
    def get_charge(self):
        return self.__charge

    def get_pat_id(self):
        return self.__pat_id