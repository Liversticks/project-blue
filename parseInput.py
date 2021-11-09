import argparse
import sys

def main(args):

    parser = argparse.ArgumentParser(
        description='Automatic AL grinding using a state machine.'
    )

    # stage - required (string or list of strings)
    parser.add_argument('stage',
        help='Stage code. Use <command> to view available stages.'
    )

    # iterations - required (int, at least 1)
    parser.add_argument('iterations', default=1, type=int,
        help='Number of times to repeat stage (must be at least 1)'
    )

    # fleet1 - required (int 0 or 1-6). Parse args first, validate later
    parser.add_argument('-f1', '--fleet1', nargs=1, required=True, default=1, type=int,
        help='First fleet number (integer from 1 to 6 for Normal Mode stages)'
    )
    # fleet2 - optional (int 0 or 1-6)
    parser.add_argument('-f2', '--fleet2', nargs=1, default=2, type=int,
        help='Second fleet number (integer from 1 to 6 for Normal Mode stages). Cannot be the same as -f1/--fleet1.'
    )
    # sub - optional (int 0 or 1-2)
    parser.add_argument('-s', '--sub', nargs=1, default=1, type=int,
        help='Submarine fleet number (1 or 2 for Normal Mode stages)'
    )

    # hard - optional (flag)

    # heclp - optional (flag)
    parser.add_argument('-he', '--heclp', action='store_true',
        help='Set a High-Efficiency Combat Logistics Plan for all clears.'
    )

    # qr - optional (flag, will Quick Retire blue and grays using existing settings)

    # Cat lodge
    # cat - required
    # buy-box - optional (flag, defaults to false)
    # forts - optional (flag, defaults to true)
    # queue - optional (flag, defaults to true)

    # Daily raids
    # raids - required (will do as many as possible, but needs external state)

    # Import procedures and run machine
    a = parser.parse_args(args[1:])
    print(a)

if __name__ == '__main__':
    main(sys.argv)