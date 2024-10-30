class Cup:
    def __init__(self, size: int, quantity: int) -> None:
        self.size = size
        self.quantity = quantity


    def fill(self, add_new_q: int):
        if self.size >= self.quantity + add_new_q:
            self.quantity += add_new_q
        return self.quantity
        

    def status(self):
        return (self.size - self.quantity)
    

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())