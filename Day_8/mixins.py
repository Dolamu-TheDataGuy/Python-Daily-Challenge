class Order:
    def __init__(self, food) -> None:
        self.food = food


class LogMixin:
    def log(self, message: str) -> None:
        print(f"LOG: {message}")
        

class SaveMixin:
    def save(self) -> None:
        print("Data Saved")
        

class ProcessOrder(LogMixin, SaveMixin):
    def process(self, order: Order) -> None:
        self.log(f"Processing order {order}")
        self.save()

    
class CancelOrder(LogMixin, SaveMixin):
    def cancel(self, order: Order) -> None:
        self.log(f"Cancelling order {order}")
