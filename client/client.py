import argparse
import functools
import sys, os
import fetch, utils
from decorators import with_apikey, with_apikey_restored, with_user_password

prog_name = 'Plants Watering Client'

class ClientCli:
    """
    Commandline tool used in communication with backend.
    """
    def __init__(self):
        dirname, filename = os.path.split(__file__)
        print('''
    |----------------------------------------------------------|
    |                  Plants Watering Client                  |
    |----------------------------------------------------------|''')
        parser = argparse.ArgumentParser(
            prog=prog_name,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            usage=filename + ' [command] {args}',
            description='''
    |----------------------------------------------------------|
    |     Client used to interact with web app integrating     |
    |      IoT sensors used in supervising potted plants.      |
    |----------------------------------------------------------|''',
        epilog='''
    |----------------------------------------------------------| 
    |           First try to 'register' or 'login'.            |
    |     Then type -h or --help for further instruction.      |       
    | All commands despite 'register' require to be logged in. |
    |----------------------------------------------------------|''')

        self.choices = ['register', 'login', 'status', 'info', 'apikey', 'test']
        parser.add_argument('command', help='Type command to be used', choices=self.choices)

        def _retrieve_cmd_or_exit():
            cmd = None
            if len(sys.argv) > 1:
                cmd = parser.parse_args(sys.argv[1:2])  # if incorrent parser will exit
            if not cmd or not hasattr(self, cmd.command):
                parser.print_help()
                exit(1)
            return cmd.command, sys.argv[2:]

        cmd, args = _retrieve_cmd_or_exit()
        print(getattr(self, cmd)(*args))



    def status(self, *args, **kwargs):
        """
        Test if backend server works. Access open (no permission no authentication) endpoint.
        """
        status_parser = argparse.ArgumentParser()
        status_parser.add_argument('-v', '--verbose', action='store_true')
        status_args = status_parser.parse_args(args)
        return fetch.fetch_status(status_args.verbose)


    @with_apikey(user_name_ext='wrong_user', api_key_ext='wrong_key')
    @with_apikey_restored  # if dotenv file is created and has username and apikey
    @with_user_password()  # pass username/password and retrive apikey
    def test(self, *args,  **kwargs):
        """
        Just for testing decorators functionality. Retrive API Token using BasicAuthentication providing username and password.
        """
        print(args, kwargs)
        username = kwargs.get('user_name')
        apikey = kwargs.get('api_key')
        return f"Retrived username {username} and API KEY {apikey[0:6]}{functools.reduce(lambda prev, curr: prev + '*', apikey[6:], '')}"



if __name__ == "__main__":
    ClientCli()

    # info
    # 'datetime', 'time', 'date', 'timezones'
    # def register(self, *args, **kwargs):
    #     return
    #
    # @with_api_key()
    # def login(self, *args, user_name, api_key, **kwargs):
    #     return f'{user_name} now you can use commands: {self.choices}.' if api_key is not None else 'Exited.'

    # def datetime(self, tail):
    #     parser = argparse.ArgumentParser(description='Some info about time', usage='useeee')
    #
    #     TIME_ZONES = fetch.fetch_timezones_list()
    #     parser.add_argument('-tz', '--timezone',
    #                         default='UTC',
    #                         const='UTC',
    #                         nargs='?',
    #                         choices=TIME_ZONES['labels'], help='asd')
    #
    #     args = parser.parse_args(tail)
    #     print('time', args.timezone)
    #     return fetch.fetch_date_time(timezone=args.timezone)
    #
    # def time(self, tail):
    #     date_time = self.datetime(tail)
    #     return None if not date_time else date_time['time']
    #
    # def date(self, tail):
    #     date_time = self.datetime(tail)
    #     return None if not date_time else date_time['date']
    #
    # def timezones(self, tail):
    #     parser = argparse.ArgumentParser(description='Available timezones', usage='dont know')
    #
    #     TIME_ZONES = fetch.fetch_timezones_list()
    #     parser.add_argument('-l', '--list', action='store_true', help='Dont care')
    #
    #     args = parser.parse_args(tail)
    #     return TIME_ZONES['labels'] if not args.list else TIME_ZONES['count']
    #
    # def status(self, tail):
    #     return None
    #
    # def login(self, tail):
    #     return fetch.fetch_login()
    #
    # def register(self, tail):
    #     return None
