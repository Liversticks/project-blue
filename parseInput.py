import argparse
import sys
import re
from mss import mss

# TODO: rewrite using subparsers

stage_re = re.compile('event(-hard)?|1[0-4]-[1-4]|[1-9]-[1-4]|[A-D][1-4]')

class InvalidStageError(Exception): pass

def validate_and_split_stages(stage_string):
    stages = stage_string.split()
    for stage in stages:
        match = stage_re.match(stage)
        if match is None:
            raise InvalidStageError
    return stages

class FleetsCannotBeSameError(Exception): pass

class FleetOutOfRangeError(Exception): pass

def validate_surface_fleets(fleet1, fleet2, is_hard=False):
    if not is_hard:
        if fleet1 == fleet2:
            raise FleetsCannotBeSameError
        if fleet1 < 1 or fleet1 > 6:
            raise FleetOutOfRangeError
        if fleet2 is not None:
            if fleet2[0] < 1 or fleet2[0] > 6:
                raise FleetOutOfRangeError

def parse_cat_lodge(args):
    parser = argparse.ArgumentParser(
        prog=f'{sys.argv[0]} cat',
        description='Cat lodge submenu: handles Meowfficer and cat lodge tasks.'
    )

    # buy-box - optional (flag, defaults to false)
    parser.add_argument('-bb', '--buy-box', action='store_true',
        help='Whether to buy 1 cat box (defaults to False).'
    )

    # forts - optional (flag, defaults to true)
    parser.add_argument('-f', '--forts', action='store_false',
        help='Whether to perform daily tasks in the Comf-Forts (defaults to True, but only executed once per day)'
    )

    # queue - optional (flag, defaults to true)
    parser.add_argument('-q', '--queue', action='store_false',
        help='Whether to empty the trained Meowfficer and queue new Cat Boxes.'
    )

    a = parser.parse_args(args)
    print(a)

def parse_campaign_or_event(args):
    parser = argparse.ArgumentParser(
        prog=f'{sys.argv[0]} battle',
        description='Battle submenu: handles clearing campaign and event stages.'
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
    parser.add_argument('-f2', '--fleet2', nargs=1, default=None, type=int,
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

    parsed_args = parser.parse_args(args)
    print(parsed_args)

    try:
        split_stages = validate_and_split_stages(parsed_args.stage)
        print(split_stages)
        validate_surface_fleets(parsed_args.fleet1[0], parsed_args.fleet2)
    except InvalidStageError:
        print("The specified stage is invalid.")
        print("List of accepted stages:")
        print()
        print("EVENT STAGES:")
        print("event - Normal Mode event stages")
        print("event-hard - Hard Mode event stages")
        print("X-Y : X = Chapter number (A, B, C, D); Y = stage number (1 - 3)")
        print()
        print("NORMAL STAGES:")
        print("X-Y : X = Chapter number (1 - 14); Y = stage number (1 - 4)")
        return
    except FleetsCannotBeSameError:
        print("Surface fleets cannot be the same (example: cannot have fleet1 = 1, fleet2 = 1).")
        return
    except FleetOutOfRangeError:
        print("For Normal Mode, the value for each surface fleet must be an integer between 1 and 6 (inclusive).")
        return

def main(args):
    modes = ['battle', 'cat', 'raid']
    
    parser = argparse.ArgumentParser(
        description='Automatic AL grinding using a state machine.'
    )
    parser.add_argument('mode',
        choices=modes,
        help='Supported modes: %(choices)s'
    )

    preliminary = parser.parse_args(args[0:1])
    if (preliminary.mode == 'battle'):
        parse_campaign_or_event(args[1:])
    elif (preliminary.mode == 'cat'):
        parse_cat_lodge(args[1:])
    else:
        # Daily raids
        # raids - required (will do as many as possible, but needs external state)
        print('Doing daily raids')

if __name__ == '__main__':
    main(sys.argv[1:])