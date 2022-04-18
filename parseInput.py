import argparse
import sys
import re
import logging
from logging import handlers
import os
# silence TensorFlow, see https://stackoverflow.com/questions/40426502/is-there-a-way-to-suppress-the-messages-tensorflow-prints
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import RunMachine as rm

stage_re = re.compile('event(-hard)?|1[0-4]-[1-4]|[1-9]-[1-4]|([A-D]|SP)-[1-4]|T-[1-4]')

class InvalidStageError(Exception): pass

def validate_and_split_stages(stage_string):
    collector = []
    for stage in stage_string.split():
        match = stage_re.match(stage)
        if match is None:
            raise InvalidStageError
        if stage == 'event':
            collector.extend(['A-1', 'A-2', 'A-3', 'B-1', 'B-2', 'B-3'])
        elif stage == 'event-hard':
            collector.extend(['C-1', 'C-2', 'C-3', 'D-1', 'D-2', 'D-3'])
        else:
            collector.append(stage)
    return collector

class FleetsCannotBeSameError(Exception): pass

class FleetOutOfRangeError(Exception): pass

class ValidationError(Exception): pass

def validate_surface_fleets(fleet1, fleet2, is_hard=False):
    if not is_hard:
        if fleet1 is not None:
            if fleet1[0] < 1 or fleet1[0] > 6:
                raise FleetOutOfRangeError
            if fleet2 is not None:
                if fleet2[0] < 1 or fleet2[0] > 6:
                    raise FleetOutOfRangeError
                if fleet1[0] == fleet2[0]:
                    raise FleetsCannotBeSameError 
        
def validate_campaign_or_event(args):
    try:
        args.split = validate_and_split_stages(args.stage)
        validate_surface_fleets(args.fleet1, args.fleet2)
    except InvalidStageError:
        print("The specified stage is invalid.")
        print("List of accepted stages:")
        print()
        print("EVENT STAGES:")
        print("event - Normal Mode event stages")
        print("event-hard - Hard Mode event stages")
        print("X-Y : X = Chapter number (A, B, C, D, SP); Y = stage number (1 - 3)")
        print()
        print("NORMAL STAGES:")
        print("X-Y : X = Chapter number (1 - 14); Y = stage number (1 - 4)")
        raise ValidationError
    except FleetsCannotBeSameError:
        print("Surface fleets cannot be the same (example: cannot have fleet1 = 1, fleet2 = 1).")
        raise ValidationError
    except FleetOutOfRangeError:
        print("For Normal Mode, the value for each surface fleet must be an integer between 1 and 6 (inclusive).")
        raise ValidationError

def validate_cat(args):
    pass

def validate_raid(args):
    pass

def parse_arguments(args):
    parser = argparse.ArgumentParser(
        description='Automatic AL grinding using a state machine.'
    )

    parser.add_argument('-d', '--debug', action='store_true',
        help='Enable debug logging and screenshots.'
    )

    subparsers = parser.add_subparsers(dest='subparser')

    ## BATTLE OPTIONS

    parser_b = subparsers.add_parser('battle',
        description='Battle submenu: handles clearing campaign and event stages.'
    )

    # stage - required (string or list of strings)
    parser_b.add_argument('stage',
        help='Stage code. Use <command> to view available stages.'
    )
    parser_b.add_argument('iterations', default=1, type=int,
        help='Number of times to repeat stage (must be at least 1)'
    )
    parser_b.add_argument('-f1', '--fleet1', nargs=1, required=True, default=1, type=int,
        help='First fleet number (integer from 1 to 6 for Normal Mode stages)'
    )
    parser_b.add_argument('-f2', '--fleet2', nargs=1, default=None, type=int,
        help='Second fleet number (integer from 1 to 6 for Normal Mode stages). Cannot be the same as -f1/--fleet1.'
    )
    parser_b.add_argument('-s', '--sub', nargs=1, default=1, type=int,
        help='Submarine fleet number (1 or 2 for Normal Mode stages)'
    )
    parser_b.add_argument('-he', '--heclp', action='store_true',
        help='Set a High-Efficiency Combat Logistics Plan for all clears.'
    )
    parser_b.add_argument('-t', '--timeout', action='store_true',
        help='Use the default_clear_time (defined in db.sql) instead of screenshot-polling for clearing stages.'
    )
    parser_b.set_defaults(validate=validate_campaign_or_event, run=rm.run_battle)
    # hard - optional (flag)
    # qr - optional (flag, will Quick Retire blue and grays using existing settings)
    

    ## CAT LODGE OPTIONS

    parser_c = subparsers.add_parser('cat',
        description='Cat lodge submenu: handles Meowfficer and cat lodge tasks.'
    )

    parser_c.add_argument('-bb', '--buy-box', action='store_true',
        help='Whether to buy 1 cat box (defaults to False).'
    )
    parser_c.add_argument('-f', '--forts', action='store_false',
        help='Whether to perform daily tasks in the Comf-Forts (defaults to True, but only executed once per day)'
    )
    parser_c.add_argument('-q', '--queue', action='store_false',
        help='Whether to empty the trained Meowfficer and queue new Cat Boxes.'
    )
    parser_c.set_defaults(validate=validate_cat, run=rm.run_cat)

    ## DAILY RAID OPTIONS

    parser_d = subparsers.add_parser('raid',
        description='Daily raid submenu: handles once-a-day Daily Raids'
    )

    parser_d.add_argument('-s', '--sub', action='store_true',
        help='Whether to try once-a-week Supply Line Disruption (defaults to False)'
    )
    parser_d.set_defaults(validate=validate_raid, run=rm.run_raid)

    return parser.parse_args(args)

def main(args):    
    options = parse_arguments(args)
    
    logger = logging.getLogger('al_state_machine')
    rfh_handler = handlers.RotatingFileHandler('al_state_machine.log', maxBytes=1000000, backupCount=1, encoding='utf-8')
    
    if options.debug:
        logger.setLevel(logging.DEBUG)
        rfh_handler.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
        rfh_handler.setLevel(logging.INFO)
    
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    rfh_handler.setFormatter(log_format)
    logger.addHandler(rfh_handler)

    logger.debug(options)
    try:
        options.validate(options)
        options.run(options)
    except ValidationError as e:
        print(e)
        return
    except AttributeError:
        print("Must run in one of the three modes <battle>, <cat>, or <raid>. Use -h for more details.")

if __name__ == '__main__':
    main(sys.argv[1:])