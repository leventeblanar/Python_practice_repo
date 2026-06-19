REALM_TO_SCHEMA = {
    "hansa": "agora",
    "pl": "agora",
    "kl4": "atlas",
}

ALLOWED_ROLES_BY_SCHEMA = {
    "agora": {"admin", "vevo", "kepviselo"},
    "atlas": {"admin", "partner"},
}

def validate_realm_and_role(realm: str, role: str) -> bool:
    if realm == "" or role == "":
        raise ValueError("A realm és a role megadása ehhez a functionhöz kötelező.")
    
    schema = REALM_TO_SCHEMA.get(realm)

    if schema is None:
        return False

    roles = ALLOWED_ROLES_BY_SCHEMA.get(schema)

    return role in roles

print(validate_realm_and_role(realm="kl4", role="vevo"))