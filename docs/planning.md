# Done
- Coordinates for 1-4, 2-2, 2-4, 3-2, 3-4, 4-2, 6-3
- Get from main menu to Campaign
- Exit, go from Campaign to main menu
- Set surface fleets for slot 1
- Clear surface fleet 2
- Quick Retire for Rare and Common ships
- Send keyboard events using Win32 API
- Basic command line interface
- Automatically switch to Bluestacks window

# Tasks (in Bluestacks)
- Coordinates for Chapter 3 SOS
- Access SOS missions (for Chapter 3)
- Repeat on defeat

# Tasks (in Python)
- Discord monitoring
- Screenshot/visual based decision-making

Ideas:
- Use a "floor" value (program will wait at least this long before attempting to finish)
- Take a screenshot after this amount of time has elapsed
- If the level has already been completed, decrement the floor value by a per-stage amount
- If the level has not already been cleared yet, increment the floor value by a per-stage amount
- To determine whether the level is cleared yet, use a classifier
    - Take a screenshot as a PNG
    - Use a PNG recompressor to make the file size smaller
    - Use clustering colours to reduce the colour range
    - Run the screenshot through the classifier
    - Keep the screenshot for future classification


- Basic telemetry - log victories
- Basic telemetry - check timebox

# New architecture

- Use a finite state machine
- States should have the following fields:
    - Name of state
    - Collection of valid transitions to take
- Use transitions to move between states. Remap existing scripts/key bindings to match new transitions (rather than the old all-in-one scripts)
    - Transitions should have the following fields:
        - Binding to execute transition
        - Time it takes for transition to elapse
        - Result state
    - Add "universal transitions" later (transitions that can happen from any state and trigger on some event or condition)
- Move the following to the "top" of the application
    - Window manager
    - Screenshot utility (since it should only be opened infrequently)
- Configuration for states and transitions should be done in files that can be read in (so on updates, only those need to be updated)

## DB schema

Stage:
- ID integer
- is_hard bool flag
- Stage string
- Maximum clear time

## List of transitions

- Any state --> disconnected
- Login --> main menu
- Main menu --> quick access (commissions, academy, lab)
- Main menu --> cat lodge
- Main menu --> Retire
- Main menu --> Event stages (if available)
- Main menu --> Battle
- Battle --> Campaign normal
- Battle --> Exercises
- Battle --> Event (backup)
- Battle --> Commissions (backup)
- Battle --> OpSi (when will this be used?)
- Event * --> Event SP
- Event SP --> Event Hard
- Event Hard --> Event Normal
- Campaign chapter N --> chapter N-1
- Campaign chapter N --> chapter N+1
- Campaign chapter N --> stage normal* info
- Stage normal* info --> Combat
    - Select fleet for slot 1
    - Select fleet for slot 2
    - Select submarine fleet
    - Assign roles
    - Set a High Performance Report
- Combat --> Stage complete
- Combat --> Defeat
- Stage complete --> Combat
    - Set report
- Stage complete --> Campaign chapter N or Event *
- Exercises --> Exercises select opponent
- Exercises select opponent --> Exercises select fleet
- Exercises select fleet --> Exercises combat
- Exercises combat --> Exercises victory
- Exercises combat --> Exercises defeat
- Exercises result --> Exercises

# Utilities
- Screenshot helper (done):
    - Takes a screenshot of the application and saves it to the specified path
- Control files copy (done)

# Testing
- Verify that transitions and states work properly