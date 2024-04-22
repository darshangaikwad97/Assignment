from datetime import datetime
from .models import Company, BankAccount
from .scheduler import FundTransferScheduler

def test_transfer_scheduler():
    companies = [
        Company(name="Company 1", invoice_amount=214000),
        Company(name="Company 2", invoice_amount=372000),
        Company(name="Company 3", invoice_amount=112000),
        Company(name="Company 4", invoice_amount=72000),
        Company(name="Company 5", invoice_amount=198000),
        Company(name="Company 6", invoice_amount=97000)
    ]
    bank_accounts = [
        BankAccount(name="Bank 1", weekday_limit=200000, weekend_limit=100000),
        BankAccount(name="Bank 2", weekday_limit=50000, weekend_limit=50000, instant_limit=20000),
        BankAccount(name="Bank 3", weekday_limit=200000, weekend_limit=200000),
        BankAccount(name="Bank 4", weekday_limit=100000, weekend_limit=50000)
    ]
    start_date = datetime(2024, 1, 1)
    scheduler = FundTransferScheduler(companies, bank_accounts, start_date)
    transfers = scheduler.schedule_transfers()
    assert len(transfers) == len(companies)

if __name__ == "__main__":
    test_transfer_scheduler()
