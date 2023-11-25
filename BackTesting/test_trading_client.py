
class TestTradingClient:
    def __init__(self, orders):
        self.orders = orders

    def __str__(self):
        return f"{self.orders}"
    
    def submit_order(self, order_data):
        self.orders.append(order_data)
        return order_data
    
    def get_all_positions(self):
        return self.orders
