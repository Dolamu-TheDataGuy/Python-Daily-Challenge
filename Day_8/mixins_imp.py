from dataclasses import dataclass

@dataclass
class Order:
    customer_email: str
    product_id: int
    quantity: int


class LogMixin:
    def log(self, message: str) -> None:
        print(f"LOG: {message}")


class SaveMixin:
    def save(self) -> None:
        print("Data Saved")


class ProcessOrder:
    def __init__(self, saver: SaveMixin, logger: LogMixin):
        self.saver = saver
        self.logger = logger
        
    def process(self, order: Order) -> None:
        self.logger.log(f"Processing order {order}")
        self.saver.save()


class CancelOrder:
    def __init__(self, saver: SaveMixin, logger: LogMixin):
        self.saver = saver
        self.logger = logger

    def cancel(self, order: Order) -> None:
        self.logger.log(f"Cancelling order {order}")

def main() -> None:
    order = Order("dolamuoludare@gmail.com", 123, 4)
    logger = LogMixin()
    saver = SaveMixin()
    processor = ProcessOrder(saver, logger)
    processor.process(order)
    canceler = CancelOrder(saver, logger)
    canceler.cancel(order)
    
if __name__ == "__main__":
    main()