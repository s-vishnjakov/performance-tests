import xml.etree.ElementTree as EL

# Пример XML строки
xml_data = '''
<user>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <email>john.doe@example.com</email>
    <address>
        <street>Main Street 1</street>
        <city>New York</city>
        <zip>10001</zip>
    </address>
</user>
'''

# Парсинг XML
root = EL.fromstring(xml_data)

# Доступ к данным
print("User ID:", root.find('id').text)
print("User Name:", root.find('first_name').text, root.find('last_name').text)
print("User Email:", root.find('email').text)
