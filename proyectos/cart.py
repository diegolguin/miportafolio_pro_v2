from decimal import Decimal

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product_id, name, price, qty=1):
        pid = str(product_id)
        if pid not in self.cart:
            self.cart[pid] = {'name': name, 'price': str(price), 'qty': 0}
        self.cart[pid]['qty'] += qty
        self.save()

    def remove(self, product_id):
        pid = str(product_id)
        if pid in self.cart:
            del self.cart[pid]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def items(self):
        for pid, item in self.cart.items():
            price = Decimal(item['price'])
            yield {'id': pid, 'name': item['name'], 'price': price, 'qty': item['qty'], 'subtotal': price * item['qty']}

    def total(self):
        from decimal import Decimal
        return sum(Decimal(i['price']) * i['qty'] for i in self.cart.values())
