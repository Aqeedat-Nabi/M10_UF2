contacts = {'Roger':678232311, 'Oriol':566879326}

def remove(contacts, user):
    if user in contacts:
        del contacts[user]
        return f"Contact {user} removed ... "
    else:
        return f"Contact {user} does not exists ."

print(remove(contacts, 'Pablo'))
