# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", nickname="",
                        title="", company="", address="",
                        home="", mobile="", work="",
                        fax="", email="", email2="",
                        email3="", homepage="", address2="",
                        phone2="", notes="")] + [
                Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname",10),
                        title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
                        home=random_string("9190000000", 10), mobile=random_string("9190000000", 10), work=random_string("9190000000", 10),
                        fax=random_string("9190000000", 10), email=random_string("email@mail.im", 10), email2=random_string("email2@mail.im", 10),
                        email3=random_string("email@mail3.im", 10), homepage=random_string("www.homepage.ru", 10), address2=random_string("address2", 10),
                        phone2=random_string("phone2", 10), notes=random_string("notes", 10))
                for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact_list = app.contactFixture.get_contact_list()
    app.contactFixture.add_contact(contact)
    assert len(old_contact_list) + 1 == app.contactFixture.contact_count()
    new_contact = app.contactFixture.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)