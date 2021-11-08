import argparse

parser = argparse.ArgumentParser(
    # Add stuff in here
)

# Arguments:
# Farming:
# fleet1 - required (int 0 or 1-6)
# fleet2 - optional (int 0 or 1-6)
# sub - optional (int 0 or 1-2)
# stage - required (string or list of strings)
# hard - optional (flag)
# heclp - optional (flag)
# iterations - required (int, at least 1)
# qr - optional (flag, will Quick Retire blue and grays using existing settings)

# Cat lodge
# cat - required
# buy-box - optional (flag, defaults to false)
# forts - optional (flag, defaults to true)
# queue - optional (flag, defaults to true)

# Daily raids
# raids - required (will do as many as possible, but needs external state)

# Import procedures and run machine
args = parser.parser_args()
print(args)