from check_environment import show_environment
from json_writer import create_json_db_record, create_json_file, create_json_from_url, read_db_record


def main():
    print('Hello from Subash')
    show_environment()

    # sample creation of json
    create_json_file()

    # sample creation of db
    create_json_db_record()
    read_db_record()

    # sample reading url
    create_json_from_url()

if(__name__=='__main__'):
    main()