class TransactionBuy:
    def __init__(
            self,
            price_transaction_datetime,
            transaction_id,
            payment_service_provider,
            username,
            ticket_id,
            website_address):
        self.price_transaction_datetime = price_transaction_datetime
        self.transaction_id = transaction_id
        self.payment_service_provider = payment_service_provider
        self.username = username
        self.ticket_id = ticket_id
        self.website_address = website_address
