class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        # Validate flavor
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
            return
        
        # Validate scoops
        if not (1 <= scoops <= 3):
            print("Choose between 1-3 scoops")
            return

        print("Order created!")
        order = {
            "customer": customer,
            "flavor": flavor,
            "scoops": scoops
        }
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        for order in self.orders.items:
            print(f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}")

    def next_order(self):
        order = self.orders.dequeue()
        if order:
            print("\nNext order up!")
            print(f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}")
        else:
            print("No orders left.")

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()