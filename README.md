# Bank-managements-system
An implementation of a bank management system


## DELIVERABLES:
###  AS A BANK:
	list out branches
	list out managers
	list out accounts
	list out debit balance
### AS A MANAGER
	list out accounts a manager manages
	approve loans 
		debit accounts with loan amounts
### AS AN ACCOUNT
	debit accounts
	credit accounts
	
### AS A USER.
	apply loans
	transfer money to other accounts
	withdraw money from my accounts
	deposit money to my accounts

 
## ENTITIES/CLASSES
        
    Bank:
        Bank __init__(self, name):
        Bank is initialized with a name
            attributes:
        1. branches
        2. accounts
        3. managers
        4. balance



    Manager:
        Manager __init__(name,branch_assigned)
            attribtues:
        1. employee_id

        Manager properties:
        1. accounts_managed = [] // depends on branch assigned i.e all accounts of the branch assigned

        Should be able to change after the bank is instantiated

    Account:
        Account __init__(account_type,deposit):
            attributes:
        1. 
        Account properties:
        1. account balance
        2. account_id

    Should be able to change after the bank is instantiated

    User:
        User __init__(name,password)
            attributes:
        1.
        User properties:
        1. user_id
