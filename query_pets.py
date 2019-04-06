#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sqlite3 as lite


def main():
    # Get user input
    while True:
        try:
            uid = int(input("Please enter an ID to look up: "))
        except (SyntaxError, NameError) as exception:
            print('You have not entered a number.')
            continue
        else:
            break

    # Logic on user response
    if uid == -1:
            print('End')
    else:
        (str_1, str_2) = getPersonPetInfo(uid)
        if str_1:
            print str_1
            print str_2
        else:
            print('Unable to find user')
            main()


def getPersonPetInfo(uid):
    person_name = None
    person_age = None
    person_pet_info = None
    count = 1

    con = lite.connect('pets')

    with con:
        con.row_factory = lite.Row
        cur = con.cursor()

        cur.execute("SELECT person.first_name AS pr_fn, person.last_name AS pr_ln, person.age AS pr_age, pet.name AS pt_name, pet.breed AS pt_breed, pet.age AS pt_age FROM person INNER JOIN person_pet ON  person_pet.person_id = person.id INNER JOIN pet ON  pet.id =  person_pet.pet_id  WHERE person.id=:ID", {"ID": uid})

        rows = cur.fetchall()
        row_len =  len(rows)

        if row_len > 0:
            for row in rows:
                person_name = "{} {}".format(row["pr_fn"], row["pr_ln"])
                person_age = "{}".format(row["pr_age"])
                person_pet_info_temp = " {}, a {}, that was {} years old".format(row["pt_name"], row["pt_breed"], row["pt_age"])

                if count == 1:
                    person_pet_info = person_pet_info_temp
                elif count == row_len:
                    person_pet_info += ", and {}.".format(person_pet_info_temp)
                else:
                    person_pet_info += ", {}".format(person_pet_info_temp)

                count += 1

    if person_name:
        output_1 = "{}, {} years old".format(person_name, person_age)
        output_2 =  "{} owned {}".format(person_name, person_pet_info)
    else:
        output_1 = None
        output_2 =  None

    return (output_1, output_2)


# Run main if file direcrly executed
if __name__ == '__main__':
    main()
