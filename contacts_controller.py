from db import get_db

def insert_contact(name, age, phone, photo, email, nick):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO contacts(name, age, phone, photo, email, nick) VALUES( ? , ? , ? , ? , ? , ?)"
    cursor.execute(statement, [name, age, phone, photo, email, nick])
    db.commit()
    return True


def update_contact(id, name, age, phone, photo, email, nick):
    db=get_db()
    cursor = db.cursor()
    statement = "UPDATE contacts SET name = ?, age = ?, phone = ?, photo = ?, email = ?, nick = ? WHERE email = ? "
    cursor.execute(statement,[name, age, phone, photo, email, nick, email])
    db.commit()
    return True


def delete_contact(email):
    db=get_db()
    cursor = db.cursor()
    statement="DELETE FROM contacts WHERE email = ?"
    cursor.execute(statement,[email])
    db.commit()
    return True


def consult_contact_age(age):
    db=get_db()
    cursor = db.cursor()
    statement="SELECT id, name, age, phone, photo, email, nick FROM contacts WHERE age=? "
    cursor.execute(statement,[age])
    return cursor.fetchone()


def consult_contact_email(email):
    db=get_db()
    cursor = db.cursor()
    statement="SELECT id, name, age, phone, photo, email, nick FROM contacts WHERE email=? "
    cursor.execute(statement,[email])
    return cursor.fetchone()


def consult_contact_phone(phone):
    db=get_db()
    cursor = db.cursor()
    statement="SELECT id, name, age, phone, photo, email, nick FROM contacts WHERE phone=? "
    cursor.execute(statement,[phone])
    return cursor.fetchone()


def get_contacts():
    db=get_db()
    cursor = db.cursor()
    query="SELECT id, name, age, phone, photo, email, nick FROM contacts"
    cursor.execute(query)
    return cursor.fetchall()