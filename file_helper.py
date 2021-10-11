def write_json_to_file(jsonObject, fileName):
    print('Creating a file: ' + fileName)
    with open(fileName,'w') as file:
        file.write(jsonObject)