from pyscript import display, document



def signin(e):
    document.getElementById('passwordalert').innerHTML = ''

    username = document.getElementById('username').value
    password = document.getElementById('password').value

    if len(username)<=8:
        display(f'your username must have at least 8 characters.', target="passwordalert")

    if password.isalpha()<=2:
        display(f'Your password needs atleast 2 numbers.', target="passwordalert")

    elif password.isdigit():
        display(f'Your password must have at least 5 letters.', target="passwordalert")

    elif len(password)<= 12:
        display(f'Your password it too short, it must have at least 12 characters.', target="passwordalert")
    
    else:
        display(f'Account has been created. You may now login.', target="passwordalert")