import fw_tools.truetools

fw1 = 'fw_rules_v1.csv'
fw2 = 'fw_rules_v2.csv'
fw3 = 'fw_rules_v3.csv'
truetools_path = fw_tools.truetools


def choose_fw():
    while True:
        print('\n', 'What fw rules do you want to use?', '\n')
        print('1. - fw_rules_v1.csv')
        print('2. - fw_rules_v2.csv')
        print('3. - fw_rules_v3.csv', '\n')
        what_fw_rules = int(input('Write number here = '))

        if what_fw_rules == 1:
            gg = fw1
            break

        elif what_fw_rules == 2:
            gg = fw2
            break

        elif what_fw_rules == 3:
            gg = fw3
            break

        else:
            print()
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('!       Should be int.       !')
            print('! Choose smth from list pls. !')
            print('! Choose smth from list pls. !')
            print('! Choose smth from list pls. !')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return gg


def fw_rules_print_statistics(path_to_fwrulesorter_class):

    print('\n', '{The statistics}')

    print('\n', '(remote) There are', path_to_fwrulesorter_class.open_remote_connections().__len__(),
          'rules that permit connection via 22 or 3389 port.')

    print('\n', '(web) There are', path_to_fwrulesorter_class.open_web_connections().__len__(),
          'rules that permit connection via 80 or 443 port.')

    print('\n', '(ftp) There are', path_to_fwrulesorter_class.open_ftp_connections().__len__(),
          'rules that permit connection via 21 port.')

    print('\n', '(permit) There are', path_to_fwrulesorter_class.permissive_rules().__len__(),
          'permissive rules.')

    print('\n', '(forbid) There are', path_to_fwrulesorter_class.forbidding_rules().__len__(),
          'forbidding rules.')

    print('\n', '(over year ago) There are', path_to_fwrulesorter_class.created_over_year_ago().__len__(),
          'rules created over year ago.')

    print('\n', '(in last three months) There are', path_to_fwrulesorter_class.created_in_last_three_months().__len__(),
          'rules created in last three months.')


def user_print_menu():

    wall_rules_chosen = choose_fw()

    all_rules = fw_tools.truetools.read_rules_from_file(wall_rules_chosen)

    sorter = fw_tools.truetools.FWRuleSorter(all_rules)

    while True:
        print('\n', 'What do you want?')
        print('1. Watch rules with open remote connections.')
        print('2. Watch rules with open web connections.')
        print('3. Watch rules with open ftp connections.')
        print('4. Watch permissive rules.')
        print('5. Watch forbidding rules.')
        print('6. Watch rules created over a year ago.')
        print('7. Watch rules created in last 3 months.')
        print('8. Watch all networks.')
        print('9. Watch all statistics.')
        print('For exit write 666')
        what_action = int(input('Write number here = '))

        if what_action == 1:
            truetools_path.print_list(sorter.open_remote_connections())

        elif what_action == 2:
            truetools_path.print_list(sorter.open_web_connections())

        elif what_action == 3:
            truetools_path.print_list(sorter.open_ftp_connections())

        elif what_action == 4:
            truetools_path.print_list(sorter.permissive_rules())

        elif what_action == 5:
            truetools_path.print_list(sorter.forbidding_rules())

        elif what_action == 6:
            truetools_path.print_list(sorter.created_over_year_ago())

        elif what_action == 7:
            truetools_path.print_list(sorter.created_in_last_three_months())

        elif what_action == 8:
            truetools_path.print_list(sorter.show_all_networks())

        elif what_action == 9:
            fw_rules_print_statistics(sorter)

        elif what_action == 666:
            break

        else:
            print()
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('!       Should be int.       !')
            print('! Choose smth from list pls. !')
            print('! Choose smth from list pls. !')
            print('! Choose smth from list pls. !')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


user_print_menu()
