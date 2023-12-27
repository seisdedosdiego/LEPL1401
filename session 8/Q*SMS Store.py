class SMS_Store:
    def __init__(self):
        self.stockage = []
    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        tuple = (False, from_number, time_arrived, text_of_SMS)
        self.stockage.append(tuple)
    def message_count(self):
        return len(self.stockage)
    def get_unread_indexes(self):
        unread = []
        for i in range (len(self.stockage)):
            if self.stockage[i][0] == False:
                unread.append(i)
    def get_message(self, i):
        if self.stockage[i]:
            tuple = (self.stockage[i][1],self.stockage[i][2],self.stockage[i][3])
            new_tuple = (True, self.stockage[i][1], self.stockage[i][2], self.stockage[i][3])
            self.stockage[i] = new_tuple
            return tuple
        else:
            return None
    def delete(self, i):
        del(self.stockage[i])
    def clear(self):
        self.stockage = []
        
my_inbox = SMS_Store()