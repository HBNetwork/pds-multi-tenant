import uuid
from django.db import models


class AccountsPayable(models.Model):
    number = uuid.UUID

class AccountsReceivable(models.Model):
    number = uuid.UUID

class Vendor(models.Model):
    cnpj = models.CharField(max_length=50)
    corporate_name = models.CharField(max_length=200)

class BankDetail(Vendor):
    vendor = models.ForeignKey(Vendor, related_name='bank_details', on_delete=models.CASCADE)
    holder_name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    agency = models.CharField(max_length=15)
    account = models.CharField(max_length=15)
    account_type = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

class Invoice(models.Model):
    STATUS = (
        ("no_payment", "sem pagamento"),
        ("payment_not_made", "pagamento não efetuado"),
        ("payment_made", "pagamento realizado"),
        ("payment_received", "pagamento recebido"),
        ("payment_canceled", "pagamento cancelado"),
        ("payment_processed", "pagamento processado"),
        ("payment_in_process", "pagamento em processamento")
    )
    value = models.DecimalField(decimal_places=2)
    due_date = models.DateField()
    invoice_status = models.CharField(choices=STATUS, default=STATUS[0])
    vendor = models.ForeignKey(Vendor, related_name='invoices', on_delete=models.CASCADE)
    accounts_payable = models.ForeignKey(AccountsPayable, related_name='invoices', on_delete=models.CASCADE)
    accounts_receivable = models.ForeignKey(AccountsReceivable, related_name='invoices', on_delete=models.CASCADE)
