from datetime import datetime


def read_timestamp():
    with open('current_timestamp.txt', 'r') as f:
        timestamp_now = datetime.now().timestamp()
        reader = f.read()
        result = timestamp_now - float(reader)
        return result


def record_timestamp():
    with open('current_timestamp.txt', "w") as f:
        timestamp_now = datetime.now().timestamp()
        f.write(str(timestamp_now))


if __name__ == '__main__':
    record_timestamp()
