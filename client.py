from server import Client, CommandError

client = Client()

try:
    # Set the value of 'key1' to 'value1'
    response = client.execute(b'SET', b'key1', b'value1') # b'SET' is the command, b'key1' and b'value1' are the arguments
    print(response)

    # Get the value of 'key1'
    response = client.execute(b'GET', b'key1') # b'GET' is the command, b'key1' is the argument
    print(response)

    # Check if 'key1' exists
    response = client.execute(b'EXISTS', b'key1') # b'EXISTS' is the command, b'key1' is the argument
    print(response)

    # Delete 'key1'
    response = client.execute(b'DEL', b'key1') # b'DEL' is the command, b'key1' is the argument
    print(response)

    # Check again if 'key1' exists
    response = client.execute(b'EXISTS', b'key1') # b'EXISTS' is the command, b'key1' is the argument
    print(response)

except CommandError as e:
    print(f"CommandError: {e}")
