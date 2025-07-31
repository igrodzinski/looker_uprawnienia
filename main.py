from looker_sdk import init40
from looker_sdk.sdk.api40.models import Group, Role

# Inicjalizacja SDK (upewnij się, że masz skonfigurowany looker.ini)
sdk = init40()

def get_user_id_by_email(email: str) -> int:
    users = sdk.search_users(email=email)
    if not users:
        raise ValueError(f"Nie znaleziono użytkownika o e-mailu: {email}")
    return users[0].id

def get_group_by_name(group_name: str) -> Group:
    groups = sdk.all_groups()
    for group in groups:
        if group.name == group_name:
            return group
    raise ValueError(f"Nie znaleziono grupy o nazwie: {group_name}")

def get_role_by_name(role_name: str) -> Role:
    roles = sdk.all_roles()
    for role in roles:
        if role.name == role_name:
            return role
    raise ValueError(f"Nie znaleziono roli o nazwie: {role_name}")

def add_user_to_group(user_id: int, group_id: int):
    sdk.add_user_to_group(group_id=group_id, user_id=user_id)
    print(f"✅ Dodano użytkownika ID {user_id} do grupy ID {group_id}")

def add_role_to_user(user_id: int, role_id: int):
    existing_roles = sdk.user_roles(user_id=user_id)
    existing_role_ids = [role.id for role in existing_roles if role.id is not None]

    if role_id in existing_role_ids:
        print(f"ℹ️ Użytkownik ID {user_id} już ma przypisaną rolę ID {role_id}")
        return

    updated_role_ids = existing_role_ids + [role_id]
    sdk.set_user_roles(user_id=user_id, body=updated_role_ids)
    print(f"✅ Dodano rolę ID {role_id} użytkownikowi ID {user_id}")

def assign_user_to_group_and_add_role(user_email: str, group_name: str, role_name: str):
    try:
        user_id = get_user_id_by_email(user_email)
        group = get_group_by_name(group_name)
        role = get_role_by_name(role_name)

        add_user_to_group(user_id=user_id, group_id=group.id)
        add_role_to_user(user_id=user_id, role_id=role.id)

    except Exception as e:
        print(f"❌ Błąd: {e}")

# 🔧 Przykład użycia:
assign_user_to_group_and_add_role(
    user_email="jan.kowalski@example.com",
    group_name="Data Analysts",
    role_name="Standard Analyst"
)
