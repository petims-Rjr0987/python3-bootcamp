def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    # any= farafahakeliny
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    length_ok = len(password) >= 8


    if has_digit and has_lower and has_upper and length_ok:
        return "Strong"
    elif length_ok and (has_upper or has_digit):
        return "Medium"
    else:
        return "Weak"








    
    
    
    """
    has_upper= any(c.isupper() for c in password)#caractère majuscule
    has_lower = any(c.islower() for c in password)#caractère muniscule 
    has_digit = any(c.isdigit() for c in password)
    length_ok = len(password) >=8

    if has_upper and has_lower and has_digit and length_ok:
        return "🔥 fort"
    elif length_ok and (has_upper or has_digit):
        return "⚖️ Moyen"
    else:
        return "⚠️ Faible (Il faut 8 caractères, des majuscules et des chiffres)"
    """