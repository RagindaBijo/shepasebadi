class Ticket:
    def __init__(self,filmname,ticketprice,ticketamm,language="ქართული"):
        self.filmname=filmname
        self.ticketprice=ticketprice
        self.ticketamm=ticketamm
        self.language=language

    def __str__(self):
        print(f'ფილმის დასახელებაა "{self.filmname}", რომლის ბილეთის ფასია {self.ticketprice} ლარი,'
              f'ბილეთების რაოდენობაა {self.ticketamm}, ხოლო ფილმი მიმდინარეობს შემდეგ ენაზე: {self.language} ')

    def compare_tickets_left(self, other):
        if self.filmname < other.filmname:
            return (f"{self.filmname} - ის ბილეთები ნაკლებია {other.filmname} - ის ბილეთებზე")
        elif self.filmname > other.filmname:
            return (f"{self.filmname} - ის ბილეთები მეტია {other.filmname} - ის ბილეთებზე")
        else:
            return (f"{self.filmname} - ის ბილეთები და {other.filmname} - ის ბილეთების რაოდენობა ტოლია")




class User:
    def __init__(self,name,moneyinbank):
        self.name=name
        self.moneyinbank=moneyinbank

    def __str__(self):
        return f"მყიდველის სახელი: {self.name} \nანგარიშზე თანხა:{self.moneyinbank}"


    def deposit(self):
        rule=int(input("გსურთ რომ აიღოთ სესხი? ( 1-კი , 2-არა)"))

        if rule==1:
            moneydeposit=float(input("მიუთითეთ სასესხებელი თანხის რაოდენობა: "))
            yesorno=int(input(f"დარწმუნებული ხართ რომ გსურთ {moneydeposit} ₾-ის დამატება ანგარიშზე? ( 1-კი , 2-არა)"))
            if yesorno==2:
                print("მადლობა რომ სარგებლობთ თქვენი სერვისით")
            elif yesorno==1:
                self.moneyinbank=self.moneyinbank+moneydeposit
                print(f"თქვენს ანგარიშზე არის {self.moneyinbank}₾")
            else:
                yesorno = int(input(f"დარწმუნებული ხართ რომ გსურთ {moneydeposit} ₾-ის დამატება ანგარიშზე? ( 1-კი , 2-არა)"))


        elif rule==2:
            print("მადლობა რომ სარგებლობთ თქვენი სერვისით")
        else:
            rule = int(input("გსურთ რომ აიღოთ სესხი? ( 1-კი , 2-არა)"))




    def buy(self,ticket):
        self.ticket=ticket
        amm=int(input("რამდები ბილეთის შეძენა გსურთ?: "))
        if self.moneyinbank >= ticket.ticketprice*amm and ticket.ticketamm>=amm:
            self.moneyinbank=self.moneyinbank-ticket.ticketamm*amm
            ticket.ticketamm=ticket.ticketamm-amm
            print(f"თქვენ წარმათებით შეიძინეთ {amm} ბილეთი {ticket.filmname}-ზე")
        elif self.moneyinbank >= ticket.ticketprice*amm and ticket.ticketamm < amm:
            print(f"სამწუხაროდ მითითებული რაოდენობის ბილეთები არ არის ხელმისაწვდომი")
        elif self.moneyinbank < ticket.ticketprice*amm:
            print(f"სამწუხაროდ თქვენ არ გაქვთ ბილეთების შესაძენად განკუთვნილი თანხის რაოდენობა ანგარიშზე")
            User.deposit(self)
            User.buy(self,ticket)












film1=Ticket("ცისფერი მთები",50,1000)
film1.__str__()
user1=User("luka",3)
user1.buy(film1)
