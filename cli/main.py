import sys
import banner, voice_mode
from livekit.agents.cli import run_app
from livekit.agents import WorkerOptions

def main():
    # 1. Show the animated banner & footer
    banner.main()

    # 2. Inject "console" subcommand into sys.argv so run_app will auto-select it
    # If your entrypoint accepts additional CLI args, include them here.
    sys.argv.insert(1, "console")

    # 3. Start the LiveKit voice agent interactively
    opts = WorkerOptions(entrypoint_fnc=voice_mode.entrypoint)
    run_app(opts)

if __name__ == "__main__":
    main()
