from js import document, window  # type: ignore


def Signing_in(event=None):
    username = document.querySelector("#Username").value
    password = document.querySelector("#Password").value

    if len(password) < 10: #len checks the number of characters there is in a string. So if it's less than 10, then prompt the failed sign-in message
        document.querySelector("#result").innerHTML = (
            f"<br>Sign-in Failed! Password must be at least 10 characters long. "
            f"Add atleast {10 - len(password)} more characters."
        )
        return

    if len(username) < 7: #same thing
        document.querySelector("#result").innerHTML = (
            "<br>Sign-in failed! Username must be above 7 characters!"
        )
        return
            
    for x in password: 
        if x.isalpha(): #this checks if there is a singular alphabetical letter in the password input. If not, prompt the failed sign-in message
            break
    else:
        document.querySelector("#result").innerHTML = (
            "<br>Sign-in failed! Password must contain at least 1 letter!"
        )
        return
        
    document.querySelector("#result").innerHTML = (
        f"Username: <b>{username}</b><br>Sign-in Successful! Welcome, {username}!<br> <a href='seatwork2.html'>Click here to continue.</a>"

    )
