import csv
import datetime
import ipaddress


class FWRule:
    datetime_created: datetime.datetime
    src_address: ipaddress.IPv4Address
    src_netmask: ipaddress.ip_interface('0.0.0.0/32')
    dst_address: ipaddress.IPv4Address
    dst_netmask: ipaddress.ip_interface('0.0.0.0/32')
    ports: str
    action: str


class FWRuleSorter:
    rules: list()

    def __init__(self, rules):
        self.rules = rules

    def open_remote_connections(self):
        lst_open_remote_connection = list()
        list_of_rules = self.rules

        for x in list_of_rules:

            if x.action == 'permit' and '22' in x.ports:
                lst_open_remote_connection.append(x)

            elif x.action == 'permit' and '3389' in x.ports:
                lst_open_remote_connection.append(x)

        return lst_open_remote_connection

    def open_web_connections(self):
        lst_open_web_connection = list()
        list_of_rules = self.rules

        for x in list_of_rules:

            if x.action == 'permit' and '80' in x.ports:
                lst_open_web_connection.append(x)

            elif x.action == 'permit' and '443' in x.ports:
                lst_open_web_connection.append(x)

        return lst_open_web_connection

    def open_ftp_connections(self):
        list_open_ftp_connection = list()
        list_of_rules = self.rules

        for x in list_of_rules:

            if x.action == 'permit' and '21' in x.ports:
                list_open_ftp_connection.append(x)

        return list_open_ftp_connection

    def permissive_rules(self):
        list_permissive = list()
        list_of_rules = self.rules

        for x in list_of_rules:

            if x.action == 'permit':
                list_permissive.append(x)

        return list_permissive

    def forbidding_rules(self):
        list_forbidding = list()
        list_of_rules = self.rules

        for x in list_of_rules:

            if x.action == 'forbid':
                list_forbidding.append(x)

        return list_forbidding

    def created_over_year_ago(self):
        list_rules_was_year_ago = list()
        list_of_rules = self.rules

        now = datetime.datetime.now(datetime.timezone.utc)
        delta_year = datetime.timedelta(days=365)
        datetime_year_ago = now - delta_year

        for x in list_of_rules:

            iso_x = datetime.datetime.fromisoformat(x.datetime_created)

            if iso_x < datetime_year_ago:
                list_rules_was_year_ago.append(x)

        return list_rules_was_year_ago

    def created_in_last_three_months(self):
        list_rules_was_created_in_last_3_months = list()
        list_of_rules = self.rules

        now = datetime.datetime.now(datetime.timezone.utc)
        delta_3_months = datetime.timedelta(days=90)
        datetime_3_months_ago = now - delta_3_months

        for x in list_of_rules:

            iso_x = datetime.datetime.fromisoformat(x.datetime_created)

            if datetime_3_months_ago < iso_x:
                list_rules_was_created_in_last_3_months.append(x)

        return list_rules_was_created_in_last_3_months

    def show_all_networks(self):

        list_of_networks = list()
        list_of_rules = self.rules

        for x in list_of_rules:
            src_ip = ipaddress.ip_interface(x.src_address + '/' + x.src_netmask)
            list_of_networks.append(src_ip.network)

            dst_ip = ipaddress.ip_interface(x.dst_address + '/' + x.dst_netmask)
            list_of_networks.append(dst_ip.network)

        return list_of_networks


def read_rules_from_file(file_name):
    list_of_csvs = list()

    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:

            c = FWRule()
            c.datetime_created = row['datetime_created']
            c.src_address = row['src_address']
            c.src_netmask = row['src_netmask']
            c.dst_address = row['dst_address']
            c.dst_netmask = row['dst_netmask']
            c.ports = row['ports']
            c.action = row['action']
            list_of_csvs.append(c)

    return list_of_csvs


def print_list(action_to_print: list):
    count = 1
    smth = 1

    for x in action_to_print:

        try:

            src_address_full = ipaddress.ip_interface(x.src_address + '/' + x.src_netmask)
            dst_address_full = ipaddress.ip_interface(x.dst_address + '/' + x.dst_netmask)

            print('\n',  '(', smth, '.)', 'Date/time =', x.datetime_created,
                  '| Source address =', src_address_full.with_prefixlen,
                  '| Destination address =', dst_address_full.with_prefixlen,
                  '| Ports =', x.ports, '| Action =', x.action)
            smth += 1

        except:

            if count % 2 != 0:
                print('\n', '(', smth, '.)', 'Network address = (src)', x, '-> ', end='')
                count += 1
                smth += 1

            elif count % 2 == 0:
                print('(dst)', x)
                count += 1
