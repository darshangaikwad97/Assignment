from datetime import timedelta
from typing import List, Tuple
from .models import Company, BankAccount, TransferSchedule

class FundTransferScheduler:
    def __init__(self, companies: List[Company], bank_accounts: List[BankAccount], start_date: datetime):
        self.companies = sorted(companies, key=lambda x: x.invoice_amount, reverse=True)
        self.bank_accounts = bank_accounts
        self.current_date = start_date

    def schedule_transfers(self) -> List[TransferSchedule]:
        transfers = []
        for company in self.companies:
            transfer_date, bank_account = self.find_available_bank(company)
            if not transfer_date or not bank_account:
                raise ValueError(f"No available bank account for {company.name}")
            transfers.append(TransferSchedule(company=company, bank_account=bank_account, transfer_date=transfer_date))
            self.update_bank_limits(bank_account, company.invoice_amount)
        return transfers

    def find_available_bank(self, company: Company) -> Tuple[datetime, BankAccount]:
        for day in range((company.invoice_amount // max(b.weekday_limit for b in self.bank_accounts)) + 1):
            current_day = self.current_date + timedelta(days=day)
            bank_accounts_sorted = sorted(self.bank_accounts, key=lambda x: x.instant_limit or x.weekday_limit, reverse=True)
            for account in bank_accounts_sorted:
                if current_day.weekday() < 5:  # Weekday
                    if account.weekday_limit >= company.invoice_amount:
                        return current_day, account
                else:  # Weekend
                    if account.weekend_limit >= company.invoice_amount:
                        return current_day, account
        return None,None # No available bank account

    def update_bank_limits(self, bank_account: BankAccount, amount: float):
        if bank_account.instant_limit == bank_account.weekday_limit:
            self.current_date += timedelta(days=1)
        bank_account.weekday_limit -= amount
