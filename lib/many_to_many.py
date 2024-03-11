class Author:

    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contracts = []
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        # Using the Contract class as an intermediary to get related books
        return [contract.get_book() for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class.")

        # Creating a new Contract object
        new_contract = Contract(self, book, date, royalties)
        # Adding the contract to the author's list of contracts
        self._contracts.append(new_contract)

        return new_contract

    def total_royalties(self):
        return sum(contract.get_royalties() for contract in self._contracts)


class Book:
    def __init__(self, title):
        self.title = title


class Contract:

    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class.")
        royalties = royalties
        self.author = author
        self.book = book
        self.date = date
        Contract.all_contracts.append(self)

    @classmethod

    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.get_date() == date]
    
    def get_author(self):
        return self.author
    
    def get_book(self):
        return self.book
    
    def get_date(self):
        return self.date

    def get_royalties(self):
        return self.royalties
    
    def set_author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        self.author = author

    def set_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class.")
        self.book = book

    def set_date(self, date):
        if not isinstance(date, str):
            raise TypeError("Date must be a string.")
        self.date = date

    def set_royalties(self, royalties):
        if not isinstance(royalties, (int, float)):
            raise TypeError("Royalties must be a number.")
        self.royalties = royalties
    