import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = DATA_DIR / "processed"
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

def load_games():
    """Load and clean games data"""
    file_path = DATA_DIR / "games.csv"
    df = pd.read_csv(file_path)

    # Keep only high-value columns
    columns = [
        "date",
        "home_club_name",
        "away_club_name",
        "home_club_goals",
        "away_club_goals",
        "competition_id"
    ]

    df = df[columns].dropna()
    return df


def games_to_facts(df, limit=5000):
    """
    Convert game rows into human-readable football facts.
    Limit is important to avoid massive embeddings.
    """
    facts = []

    df = df.head(limit)

    for _, row in df.iterrows():
        fact = (
            f"On {row['date']}, {row['home_club_name']} played "
            f"{row['away_club_name']} in {row['competition_id']}. "
            f"The final score was {int(row['home_club_goals'])}–{int(row['away_club_goals'])}."
        )
        facts.append(fact)

    return facts



if __name__ == "__main__":
    print("Loading players data...")
    players_df = load_players()
    player_facts = players_to_facts(players_df)
    save_facts(player_facts, "player_facts.txt")

    print("Loading games data...")
    games_df = load_games()
    print(f"Games dataframe loaded with {len(games_df)} rows")

    game_facts = games_to_facts(games_df)
    print(f"Generated {len(game_facts)} game facts")
    save_facts(game_facts, "game_facts.txt")
    print("Saved game_facts.txt")


    print("Sample game facts:")
    for fact in game_facts[:5]:
        print("-", fact)

    print("Ingestion complete.")


