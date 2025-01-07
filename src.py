from datetime import datetime, timedelta, date

Books = list()

Members = []


def add_book(
    ISBN,
    Title,
    Description,
    Category,
    Quantity,
    Author,
    Publisher,
    Language,
    READD,
    SKU,
):

    if READD == True:
        for ele in Books:

            if ele["ISBN"] == SKU.split("-")[0]:
                ele["Quantity"] = int(ele["Quantity"]) + 1
                date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                ele["SKU"].setdefault(str(SKU), date)
                return
    else:

        if len(Books) > 0:
            for ele in Books:

                if ele["ISBN"] == ISBN:
                    ele["Quantity"] = int(ele["Quantity"]) + int(Quantity)
                    sku = str(ISBN) + "-" + str(len(ele["SKU"]) + 1)
                    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    ele["SKU"] = ele["SKU"].setdefault(sku, date)
                    break

                else:

                    sku_dict = {}
                    for i in range(int(Quantity)):
                        sku = str(ISBN) + "-" + str(i + 1)
                        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        sku_dict.setdefault(sku, date)

                    Books.append(
                        {
                            "ISBN": ISBN,
                            "Title": Title,
                            "Description": Description,
                            "Category": Category,
                            "Quantity": Quantity,
                            "SKU": sku_dict,
                            "Author": Author,
                            "Publisher": Publisher,
                            "Language": Language,
                        }
                    )
                    break

        else:
            sku_dict = {}
            for i in range(int(Quantity)):
                sku = str(ISBN) + "-" + str(i + 1)
                date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                sku_dict.setdefault(sku, date)

            Books.append(
                {
                    "ISBN": ISBN,
                    "Title": Title,
                    "Description": Description,
                    "Category": Category,
                    "Quantity": Quantity,
                    "SKU": sku_dict,
                    "Author": Author,
                    "Publisher": Publisher,
                    "Language": Language,
                }
            )

    return Books


def update_books(ISBN, Title, Description, Category, Author, Publisher, Language):

    for ele in Books:

        if ele["ISBN"] == ISBN:

            ele["Description"] = Description
            ele["Title"] = Title
            ele["Category"] = Category
            ele["Author"] = Author
            ele["Publisher"] = Publisher
            ele["Language"] = Language
            return

        else:
            return "No book found"


def remove_book(SKU):

    ISBN = SKU.split("-")[0]

    for book in Books:
        if book["ISBN"] == ISBN:
            for sku in book["SKU"]: 
                if sku == SKU:
                    book["SKU"].pop(SKU)
                    book["Quantity"] = int(book["Quantity"]) - 1
                    return
                else:
                    continue 
        else:
            return "No Book found"


def read_book(ISBN):

    for ele in Books:
        if ele["ISBN"] == ISBN:
            return ele


def add_member(Name, Email, Password):

    Members.append(
        {
            "UID": len(Members) + 1,
            "Name": Name,
            "Email": Email,
            "Password": Password,
            "SKU": {},
        }
    )

    return Members


def update_member(UID, SKU, ADD_BOOK):

    future_date = (datetime.now() + timedelta(days=15)).strftime("%d/%m/%Y %H:%M:%S")


    if ADD_BOOK == True:
        for ele in Books:
            if ele["ISBN"] == SKU.split("-")[0]:
                for sku in ele["SKU"]:
                    if sku == str(SKU):

                        for mem in Members:
                            if mem["UID"] == int(UID):
                                mem["SKU"].setdefault(str(SKU), str(future_date))
                                remove_books(SKU)
                                return
                    else:
                        return "The Book you are searching for is not available"

    elif ADD_BOOK == False:
        for mem in Members:
            if mem["UID"] == int(UID):
                days = int(str( datetime.now() - datetime.strptime(mem["SKU"][SKU], "%d/%m/%Y %H:%M:%S") ).split(" ")[0])
                mem["SKU"].pop(str(SKU))
                add_book("", "", "", "", "", "", "", "", True, SKU)
                if days > 0:
                    fine = 5
                    total_fine = 0
                    for i in range(1, days + 1):
                        total_fine += fine
                        fine = fine + (fine * 0.02)

                    return total_fine
                else:
                    return

    else:
        return "ADD_BOOK should be a boolean value"


def remove_member(UID):

    for ele in Members:
        if ele["UID"] == int(UID):
            Members.remove(ele)
            return
        else:
            return "Member not found"


def Sign_in(Name, Email, Password):

    for ele in Members:
        if (
            ele["Name"] == Name
            and ele["Email"] == Email
            and ele["Password"] == Password
        ):
            return ele

add_book("00001","Tale of the melon city","","","5","","","",'','')
remove_book("00001-3")
print(remove_book("00001-3"))
remove_book("00001-1")
remove_book("00001-2")
print(Books)