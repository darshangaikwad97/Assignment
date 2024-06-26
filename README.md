# Assignment
# Fund Transfer Scheduler

This Python project implements a fund transfer scheduler that optimizes the distribution of fund transfers across multiple bank accounts while adhering to daily limits. It utilizes Pydantic for data modeling and validation.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install Poetry (dependency manager):
    ```bash
    pip install poetry
    ```
3. Clone this repository:
    ```bash
    git clone https://github.com/your-username/fund_transfer_scheduler.git
    ```
4. Navigate to the project directory:
    ```bash
    cd fund_transfer_scheduler
    ```
5. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

## Usage

### Running the Fund Transfer Scheduler

To run the fund transfer scheduler script, follow these steps:

1. Navigate to the project directory in your terminal:

    ```bash
    cd /path/to/fund_transfer_scheduler
    ```

2. Ensure that Python 3.x is installed on your system.

3. Install Poetry (dependency manager) if you haven't already:

    ```bash
    pip install poetry
    ```

4. Install project dependencies using Poetry:

    ```bash
    poetry install
    ```

5. Create a Python script (e.g., `main.py`) and add the following code to use the scheduler:

    ```python
    from datetime import datetime
    from fund_transfer_scheduler.models import Company, BankAccount
    from fund_transfer_scheduler.scheduler import FundTransferScheduler

    # Create instances of companies
    companies = [
        Company(name="Company 1", invoice_amount=214000),
        Company(name="Company 2", invoice_amount=372000),
        # Add more companies as needed
    ]

    # Create instances of bank accounts
    bank_accounts = [
        BankAccount(name="Bank 1", weekday_limit=200000, weekend_limit=100000),
        BankAccount(name="Bank 2", weekday_limit=50000, weekend_limit=50000, instant_limit=20000),
        # Add more bank accounts as needed
    ]

    # Set the start date
    start_date = datetime(2024, 1, 1)

    # Create an instance of the scheduler
    scheduler = FundTransferScheduler(companies, bank_accounts, start_date)

    # Schedule transfers
    transfers = scheduler.schedule_transfers()

    # Display transfer schedules
    for transfer in transfers:
        print(f"Transfer {transfer.company.name} to {transfer.bank_account.name} on {transfer.transfer_date}")
    ```

6. Save the script and execute it using Python:

    ```bash
     python your_script.py
    ```

This will run the script and display the transfer schedules on the console.
