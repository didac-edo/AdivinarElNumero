import random
from colorama import Fore, init
from rich import print as rprint

def play_guessing_game():
    init()
    rprint("[bold magenta]Bienvenido al juego de adivinanza![/bold magenta]")

    while True:
        try:
            lower_bound = int(input("Ingrese el límite inferior: "))
            upper_bound = int(input("Ingrese el límite superior: "))

            if lower_bound >= upper_bound:
                rprint(
                    "[bold red]El límite inferior debe ser menor que el límite superior. Por favor, inténtalo de nuevo.[/bold red]")
                continue

            break
        except ValueError:
            rprint("[bold red]Por favor, ingresa números válidos.[/bold red]")

    target = random.randint(lower_bound, upper_bound)
    attempts = 5
    guess = None

    while attempts > 0:
        guess = int(input(f"Ingresa un número entre {lower_bound} y {upper_bound}: "))
        attempts -= 1

        if guess < target:
            rprint(f"{Fore.YELLOW}¡Demasiado bajo!{Fore.RESET} Te quedan {Fore.CYAN}{attempts}{Fore.RESET} intentos.")
        elif guess > target:
            rprint(f"{Fore.YELLOW}¡Demasiado alto!{Fore.RESET} Te quedan {Fore.CYAN}{attempts}{Fore.RESET} intentos.")
        else:
            rprint(
                f"[bold green]Felicidades, has adivinado el número {target} con {attempts} intentos restantes![/bold green]")
            return

    rprint(
        f"[bold red]Lo siento, has perdido. El número era {target}.[/bold red]")


if __name__ == "__main__":
    play_guessing_game()
