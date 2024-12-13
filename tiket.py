class Movie:
    def __init__(self, title, price):
        self.title = title
        self.price = price
print("==== Daftar Tiket ====")
class TicketCounter:
    def __init__(self):
        self.movies = [
            Movie("Wicked", 50000),
            Movie("Moana", 55000),
            Movie("Terrifier", 40000)
        ]

    def display_movies(self):
        print("Daftar Film:")
        for index, movie in enumerate(self.movies):
            print(f"{index + 1}. {movie.title} - Harga: Rp {movie.price}")

    def select_movie(self):
        self.display_movies()
        choice = int(input("Pilih film (masukkan nomor): ")) - 1
        if 0 <= choice < len(self.movies):
            return self.movies[choice]
        else:
            print("Pilihan tidak valid.")
            return None

    def get_ticket_quantity(self):
        quantity = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
        return quantity

    def calculate_total(self, movie, quantity):
        return movie.price * quantity

def main():
    print("Selamat datang di Kasir Tiket Bioskop!")
    ticket_counter = TicketCounter()

    selected_movie = ticket_counter.select_movie()
    if selected_movie:
        quantity = ticket_counter.get_ticket_quantity()
        total = ticket_counter.calculate_total(selected_movie, quantity)
        print(f"\nAnda telah memilih: {selected_movie.title}")
        print(f"Jumlah tiket: {quantity}")
        print(f"Total harga: Rp {total}")

if __name__ == "__main__":
    main()