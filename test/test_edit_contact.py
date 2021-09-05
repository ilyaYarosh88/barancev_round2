from model.contact import Contact



def test_edit_first_contact(app):

    app.contactFixture.edit_first_contact(Contact(firstname="EditedIvan", middlename="EditedSergeevich", lastname="EditedPetrov", nickname="EditedButthead",
                            title="Editedtest", company="EditedGazprom", address="EditedMoscow", home="Edited+74950000000",
                            mobile="Edited+79190000000", work="Edited+74951000000", fax="Edited+74952000000",
                            email="Editedispetrov@mail.ru", email2="Editedispetrov2@mail.ru", email3="Editedispetrov3@mail.ru",
                            homepage="Editedwww.petrov.su", bday="2", bmonth="April", byear="1973", aday="6", amonth="May",
                            ayear="1999", address2="EditedMoscow", phone2="Edited1", notes="EditedTest"))
