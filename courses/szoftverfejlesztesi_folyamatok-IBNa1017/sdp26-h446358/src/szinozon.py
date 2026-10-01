import json
import os
import random

from colorama import Fore, Style, init

init(autoreset=True)


# ── Konfiguráció ──────────────────────────────────────────────────────────────
CODE_LENGTH = 4  # ennyi színt kell kitalálni
MAX_ATTEMPTS = 10  # ennyi próbálkozási lehetőség van
SYMBOL = "●"  # ez a szimbólum jelenik meg a 'táblán' színesen

COLORS = ["R", "G", "B", "Y", "M", "C"]

COLOR_MAP = {
    "R": Fore.RED,
    "G": Fore.GREEN,
    "B": Fore.BLUE,
    "Y": Fore.YELLOW,
    "M": Fore.MAGENTA,
    "C": Fore.CYAN,
}

COLOR_NAMES = {
    "R": "Piros",
    "G": "Zöld",
    "B": "Kék",
    "Y": "Sárga",
    "M": "Lila",
    "C": "Cián",
}

# Eredeti szín és hely jelölő szimbólumok nem jelentek meg bizonyos terminal felületeken...
EXACT_SYM = "■"
MISPLACED_SYM = "□"

SAVE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "szinozon_save.json"
)


# ── Segédfüggvények ───────────────────────────────────────────────────────────
def colored(code: str) -> str:
    """Visszaad egy színezett szimbólumot a megadott színkódhoz."""
    return COLOR_MAP[code] + SYMBOL + Style.RESET_ALL


def generate_secret() -> list[str]:
    """Véletlenszerűen generál egy CODE_LENGTH hosszú titkos kódot."""
    return random.choices(COLORS, k=CODE_LENGTH)


def evaluate_guess(secret: list[str], guess: list[str]) -> tuple[int, int]:
    """
    Visszaadja:
      exact – hány szín van pontos helyen
      misplaced – hány szín helyes, de rossz pozícióban van
    """
    exact = sum(s == g for s, g in zip(secret, guess))
    total = sum(min(secret.count(c), guess.count(c)) for c in COLORS)
    return exact, total - exact


def get_guess(attempt: int, current_guess: list[str]) -> list[str]:
    """Bekér és validál egy tippet a felhasználótól lépésenként."""
    print("Tipp összeállítása ['R', 'G', 'B', 'Y', 'M', 'C'] (megse, rendben): ")

    while True:
        display = " ".join(current_guess + [" "] * (CODE_LENGTH - len(current_guess)))
        raw = input(f"[{display}]> ").strip().lower()

        if raw == "megse":
            if len(current_guess) > 0:
                current_guess.pop()
            else:
                print(
                    "Tipp összeállítása ['R', 'G', 'B', 'Y', 'M', 'C'] (megse, rendben): "
                )

        elif raw == "rendben":
            if len(current_guess) == CODE_LENGTH:
                return list(current_guess)
            else:
                print(Fore.YELLOW + "  - Tessék?" + Style.RESET_ALL)

        elif raw.upper() in COLOR_MAP:
            if len(current_guess) < CODE_LENGTH:
                current_guess.append(raw.upper())
            else:
                print(Fore.YELLOW + "  - Nincs több" + Style.RESET_ALL)

        else:
            print(Fore.YELLOW + "  - Tessék?" + Style.RESET_ALL)


# ── Megjelenítés ──────────────────────────────────────────────────────────────
def print_header() -> None:
    print(Fore.CYAN + Style.BRIGHT)
    print("╔══════════════════════╗")
    print("║       SZÍNÖZÖN       ║")
    print("╚══════════════════════╝")
    print(Style.RESET_ALL)
    print(
        f"Találd ki a {CODE_LENGTH} színből álló titkos kódot {MAX_ATTEMPTS} kísérletből!\n"
    )


def print_legend() -> None:
    parts = [f"{colored(k)} {COLOR_NAMES[k]}({k})" for k in COLORS]
    print("Elérhető színek:")
    print("    " + "    ".join(parts))
    print()
    print(f"{EXACT_SYM} = pontos szín + pontos pozíció")
    print(f"{MISPLACED_SYM} = helyes szín, de rossz pozíció")
    print()


def print_board(history: list[tuple[list[str], int, int]]) -> None:
    sep = "  " + "─" * 34
    print(sep)
    print(f"{'Nr':>3} {'Tipp':<14} {EXACT_SYM} {MISPLACED_SYM}")
    print(sep)
    for i, (guess, exact, misplaced) in enumerate(history, 1):
        symbols = "  ".join(colored(c) for c in guess)
        print(f"{i:>3} {symbols}     {exact} {EXACT_SYM} {misplaced} {MISPLACED_SYM}")
    print(sep)
    print()


# ── Mentés / Betöltés ─────────────────────────────────────────────────────────
def save_game(
    secret: list[str], history: list, attempt: int, current_guess: list[str]
) -> None:
    """Elmenti a játék aktuális állását JSON fájlba.
    Ha már létezik mentés, felülírás előtt megerősítést kér."""
    q = input("Szeretnél menteni? (y/n): ")
    if q != "y":
        return

    if os.path.exists(SAVE_FILE):
        q2 = input("Már van egy mentett játék. Felülírod? (y/n): ").strip().lower()
        if q2 != "y":
            print(Fore.YELLOW + "Mentés megszakítva." + Style.RESET_ALL)
            return

    data = {
        "secret": secret,
        "history": [[guess, exact, misplaced] for guess, exact, misplaced in history],
        "attempt": attempt,
        "current_guess": current_guess if current_guess else [],
    }

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=3)
        print(Fore.GREEN + "Játék elmentve." + Style.RESET_ALL)


def load_game() -> tuple[list[str], list, int, list[str]] | None:
    """Betölti a mentett játékot. Sikertelen beolvasás esetén None-t ad vissza."""
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            secret = data["secret"]
            history = [(item[0], item[1], item[2]) for item in data["history"]]
            attempt = data["attempt"]
            current_guess = data.get("current_guess", [])
            return secret, history, attempt, current_guess
    except Exception:
        print(Fore.RED + "Hiba a mentés betöltésekor." + Style.RESET_ALL)
        return None


def delete_save() -> None:
    """Törli a mentésfájlt, ha létezik."""
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)


# ── Játékciklus ───────────────────────────────────────────────────────────────
def main() -> None:
    print_header()
    print_legend()
    print(Fore.YELLOW + "- Szia! Kezdheted a játékot!" + Style.RESET_ALL)

    secret: list[str] = []
    history: list[tuple[list[str], int, int]] = []
    attempts = 1
    attempt = attempts
    current_guess: list[str] = []

    if os.path.exists(SAVE_FILE):
        print("Van mentett játék. Mit szeretnél tenni?")
        choice = input(
            "Betöltés és folytatás (c) vagy Törlés és új játék (d): "
        ).strip()  # (c) - continue, (d) - delete
        print()

        if choice in ("c", "C"):
            game = load_game()

            if game:
                secret, history, attempts, current_guess = game
                print(Fore.CYAN + "Játék betöltve, folytatás...\n" + Style.RESET_ALL)
                print_board(history)
            else:
                print(
                    Fore.YELLOW
                    + "Nem sikerült betölteni, új játék kezdődik.\n"
                    + Style.RESET_ALL
                )
                delete_save()

        elif choice in ("d", "D"):
            delete_save()
            print(
                Fore.YELLOW + "Mentés törölve, új játék kezdődik.\n" + Style.RESET_ALL
            )

    if not secret:
        secret = generate_secret()

    try:
        for attempt in range(attempts, MAX_ATTEMPTS + 1):
            guess = get_guess(attempt, current_guess)
            exact, misplaced = evaluate_guess(secret, guess)
            history.append((guess, exact, misplaced))
            current_guess.clear()
            print_board(history)

            if exact == CODE_LENGTH:
                print(
                    Fore.GREEN
                    + Style.BRIGHT
                    + f"Gratulálok! Kitaláltad a kódot {attempt} kísérletből!\n"
                    + Style.RESET_ALL
                )
                delete_save()
                return

        secret_display = "  ".join(colored(c) for c in secret)
        print(
            Fore.RED
            + Style.BRIGHT
            + f"✗ Vége! A titkos kód: {secret_display}\n"
            + Style.RESET_ALL
        )
        delete_save()

    except KeyboardInterrupt:
        print()
        if secret and history or current_guess:
            save_game(secret, history, attempt, current_guess)


if __name__ == "__main__":
    main()
