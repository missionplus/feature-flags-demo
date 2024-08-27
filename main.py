import ldclient
from ldclient.config import Config
from ldclient.context import Context
import time
import os
from colorama import init, Fore, Back, Style

# Initialize colorama for colored output
init(autoreset=True)

# LaunchDarkly SDK key (set env var, or replace with your actual SDK key)
sdk_key = os.getenv("LAUNCHDARKLY_SDK_KEY") or "sdk-1234"

# LaunchDarkly client initialization
ldclient.set_config(Config(sdk_key))

# Context object
context = Context.builder("demo-user-key") \
    .name("Ned Lowe") \
    .set("email", "ned@missions.plus") \
    .build()

def space_mission(flag_enabled):
    if flag_enabled:
        print(Fore.CYAN + Style.BRIGHT + "🚀 Initiating advanced space mission...")
        time.sleep(1)
        print(Fore.YELLOW + "🛰️  Deploying satellite...")
        time.sleep(1)
        print(Fore.GREEN + "🌍 Establishing communication with Earth...")
        time.sleep(1)
        print(Back.BLUE + Fore.WHITE + "🌌 Exploring new galaxies!" + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "🚀 Initiating basic space mission...")
        time.sleep(1)
        print(Fore.WHITE + "🛰️  Orbiting Earth...")
        time.sleep(1)
        print(Fore.WHITE + "📡 Collecting basic data...")

def main():
    try:
        client = ldclient.get()

        while True:
            # Check the feature flag
            flag_value = client.variation("mission-demo", context, False)

            print("\n" + "=" * 40)
            if flag_value:
                print(Back.GREEN + Fore.BLACK + "Feature Flag 'mission-demo' is ON")
            else:
                print(Back.RED + Fore.WHITE + "Feature Flag 'mission-demo' is OFF")
            print("=" * 40 + "\n")

            space_mission(flag_value)

            time.sleep(5)  # Wait for 5 seconds before checking again

    finally:
        ldclient.get().close()

if __name__ == "__main__":
    main()
