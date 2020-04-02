class Tickets():
    def __init__(self,id,operational_status,title,description):
        self.id = id
        self.operational_status = operational_status
        self.title = title
        self.description = description

    def get_id(self):
        return self.id
    def get_descpription(self):
        return  self.description

obj = Tickets(12,"ongoing","I can not access emails","This is a short description on emails.")
print("The Ticket Id Is : ",obj.get_id())
print("The Ticket Description Is : ", obj.description)