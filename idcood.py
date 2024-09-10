def ask_for_id():
    global isikukood
    while True:
        idcode = input('Please enter your national id: ')
        if len(idcode) != 11:
            if len(idcode) < 11:
                print('ID you entered is too short.')
                continue
            else:
                print('ID you entered is too long.')
                continue
        else:
            isikukood = idcode
            return


def get_gender():
    n = isikukood[0]
    if n in '1357':
        print('You are male')
    elif n in '2468':
        print('You are female')
    else:
        print('Invalid ID code.')


def get_date_of_birth():
    day = isikukood[5:7]
    month = isikukood[3:5]
    year = isikukood[1:3]
    bcent = ''
    n = isikukood[0]

    if n in '12':
        bcent = '18'  # 1800-1899
    elif n in '34':
        bcent = '19'  # 1900-1999
    elif n in '56':
        bcent = '20'  # 2000-2099
    elif n in '78':
        bcent = '21'  # 2100-2199

    print(f'Date of Birth: {day}.{month}.{bcent}{year}')


def get_birth_region():
    region_code = int(isikukood[7:10])
    region = ''

    if 1 <= region_code <= 10:
        region = 'Kuressaare haigla'
    elif 11 <= region_code <= 19:
        region = 'Tartu Ülikooli Naistekliinik'
    elif 21 <= region_code <= 150:
        region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif 151 <= region_code <= 160:
        region = 'Keila haigla'
    elif 161 <= region_code <= 220:
        region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif 221 <= region_code <= 270:
        region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif 271 <= region_code <= 370:
        region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif 371 <= region_code <= 420:
        region = 'Narva haigla'
    elif 421 <= region_code <= 470:
        region = 'Pärnu haigla'
    elif 471 <= region_code <= 490:
        region = 'Haapsalu haigla'
    elif 491 <= region_code <= 520:
        region = 'Järvamaa haigla (Paide)'
    elif 521 <= region_code <= 570:
        region = 'Rakvere haigla, Tapa haigla'
    elif 571 <= region_code <= 600:
        region = 'Valga haigla'
    elif 601 <= region_code <= 650:
        region = 'Viljandi haigla'
    elif 651 <= region_code <= 700:
        region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
    else:
        region = 'Unknown region or outside of Estonia'

    print(f'Birth Region: {region}')


def validate_id():
    weights1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    id_digits = list(map(int, isikukood[:10]))
    checksum = int(isikukood[-1])

    sum1 = sum(x * y for x, y in zip(id_digits, weights1))
    remainder1 = sum1 % 11

    if remainder1 < 10:
        calculated_checksum = remainder1
    else:
        sum2 = sum(x * y for x, y in zip(id_digits, weights2))
        remainder2 = sum2 % 11
        calculated_checksum = remainder2 if remainder2 < 10 else 0

    if calculated_checksum == checksum:
        print('ID is valid.')
    else:
        print('Invalid ID.')


def menu():
    while True:
        ask_for_id()
        user_choice = input('Please choose:\n'
                            '1. Gender\n'
                            '2. Date of Birth\n'
                            '3. Birth Region\n'
                            '4. Validate ID\n'
                            '0. Exit\n'
                            '--> ')
        if user_choice == '1':
            get_gender()
        elif user_choice == '2':
            get_date_of_birth()
        elif user_choice == '3':
            get_birth_region()
        elif user_choice == '4':
            validate_id()
        elif user_choice == '0':
            break
        else:
            print('Choice out of range.')


isikukood = ''
menu()
