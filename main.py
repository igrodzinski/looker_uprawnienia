from looker_sdk import init31
from looker_sdk.sdk.api31.models import WriteGroupIdForGroupUserInclusion

sdk = init31()

def get_user_id_by_email(email: str) -> int:
    users = sdk.search_users(email=email)
    if not users:
        raise ValueError(f"Nie znaleziono użytkownika o adresie e-mail: {email}")
    return users[0].id

def get_group_id_by_name(group_name: str) -> int:
    groups = sdk.all_groups()
    for group in groups:
        if group.name == group_name:
            return group.id
    raise ValueError(f"Nie znaleziono grupy o nazwie: {group_name}")

def get_role_id_by_name(role_name: str) -> int:
    roles = sdk.all_roles()
    for role in roles:
        if role.name == role_name:
            return role.id
    raise ValueError(f"Nie znaleziono roli o nazwie: {role_name}")

def add_role_to_user(user_id: int, new_role_id: int):
    current_roles = sdk.user_roles(user_id=user_id)
    current_role_ids = [role.id for role in current_roles if role.id is not None]

    if new_role_id in current_role_ids:
        print(f"ℹ️ Użytkownik już ma przypisaną rolę ID {new_role_id}.")
        return

    # Dodaj nową rolę do istniejących
    updated_roles = current_role_ids + [new_role_id]
    sdk.set_user_roles(user_id=user_id, body=updated_roles)
    print(f"✅ Dodano rolę ID {new_role_id} użytkownikowi ID {user_id}.")

def assign_user_to_group_and_add_role(user_email: str, group_name: str, role_name: str):
    try:
        user_id = get_user_id_by_email(user_email)
        group_id = get_group_id_by_name(group_name)
        role_id = get_role_id_by_name(role_name)

        # Dodanie do grupy
        sdk.add_group_user(
            group_id=group_id,
            body=WriteGroupIdForGroupUserInclusion(user_id=user_id)
        )
        print(f"✅ Dodano użytkownika '{user_email}' do grupy '{group_name}'.")

        # Dodanie nowej roli bez usuwania starych
        add_role_to_user(user_id, role_id)

    except Exception as e:
        print(f"❌ Błąd: {e}")

# 🔧 PRZYKŁAD:
assign_user_to_group_and_add_role(
    user_email="jan.kowalski@example.com",
    group_name="Analysts",
    role_name="Standard Analyst"
)
