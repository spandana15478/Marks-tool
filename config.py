
"""Read KEY=value settings from a .env file."""


def load_env(path=".env"):
    settings = {}

    try:
        with open(path, "r") as handle:
            for line in handle:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                key, _, value = line.partition("=")

                if key.strip():
                    settings[key.strip()] = value.strip()

    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{path}' not found.")

    return settings

