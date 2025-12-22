import pandas as pd
from pathlib import Path

DATA_DIR = Path("../data")
OUTPUT_DIR = Path("../data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_players():
    """Load and clean players data"""
    file_path = DATA_DIR / "players.csv"
    df = pd.read_csv(file_path)

    # Keep only useful columns (adjust names if needed)
    columns = [
        "player_id",
        "name",
        "country_of_birth",
        "country_of_citizenship",
        "position",
        "date_of_birth"
    ]

    df = df[columns].dropna(subset=["name"])
    return df


def players_to_facts(df):
    """Convert player rows into human-readable football facts"""
    facts = []

    for _, row in df.iterrows():
        fact = (
            f"Player {row['name']} is a {row['position']} "
            f"born on {row['date_of_birth']}. "
            f"They are from {row['country_of_citizenship']}."
        )
        facts.append(fact)

    return facts


def save_facts(facts, filename="player_facts.txt"):
    output_path = OUTPUT_DIR / filename
    with open(output_path, "w", encoding="utf-8") as f:
        for fact in facts:
            f.write(fact + "\n")


if __name__ == "__main__":
    print("Loading players data...")
    players_df = load_players()

    print(f"Loaded {len(players_df)} players")

    print("Converting players to football facts...")
    player_facts = players_to_facts(players_df)

    print("Sample facts:")
    for fact in player_facts[:5]:
        print("-", fact)

    save_facts(player_facts)
    print("Player facts saved successfully.")
