from lib.config import Config

if __name__ == '__main__':
    print('Run!')
    conf = Config()
    print(conf.get_json_string())

