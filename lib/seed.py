#!/usr/bin/env python3
from Models.__init__ import CONN, CURSOR
from Models.branch import Branch
from Models.user import User

def seed_database():
    User.drop_table()
    User.create_table()
    joe = User.create("joe doe", '1234')
    jane = User.create("Jane doe", '12345jane')
    peter = User.create("peter clark", '44peter.')
    andrew = User.create("andrew clark",'12west')
    

seed_database()