from js import document # type: ignore

# a dictionary made to store the images of the team logos
team_images = {
    "Blue Bears": "blue_bears.png",
    "Red Bulldogs": "red_bulldogs.png",
    "Yellow Tigers": "yellow_tigers.png",
    "Green Hornets": "green_hornets.png"
}

def teamassigner(event=None):
    GradeLevel = document.querySelector("#GL").value #Gets the information from the dropdown menu and stores it
    Section = document.querySelector("#GS").value # Same thing as GradeLevel
    
    # Get the selected radio button values for Medical Clearance and Online Registration
    medcert_checked = document.querySelector('input[name="MC"]:checked') # w3schools helped me with this line
    onlinereg_checked = document.querySelector('input[name="OR"]:checked')
    
    Medcert = medcert_checked.value if medcert_checked else None #i am actually a genius
    OnlineReg = onlinereg_checked.value if onlinereg_checked else None # checks if the radio buttons are selected and gets their values. If not selected, it sets itself to none, successfully stopping the errors that terrorized me

    if Medcert == "No" or OnlineReg == "No": # Checks if either medical certificate or online registration is not done
        document.querySelector("#result").innerHTML = "Please complete your Medical Certificate and Online Registration before proceeding to team assignment!" # Error message if the condition above is met
        return
    if Medcert == None or OnlineReg == None: # Checks if either medical certificate or online registration is not selected
        document.querySelector("#result").innerHTML = "Please select both Medical Certificate and Online Registration options!" # Error message if the condition above is met
        return
    
    if GradeLevel == "Placeholder" or Section == "Placeholder": # Checks if either grade level or section is not selected
        document.querySelector("#result").innerHTML = "Please select both Grade Level and Section!" # Error message if the condition above is met
        return
    #the next following code actually stemmed from me wanting to hide other options when you choose something like Grade 12. Meaning it would only show Tinio and Jose or something. But I settled for this cause the former was too hard.
    if GradeLevel and Section: # Shows here that if the condition that Grade level and section are [x] then do the following.
        if GradeLevel == "Twelve" and Section not in ["Tinio", "Jose"]: #Check if the Grade level is twelve and if the section is not Tinio or Jose. This is to make sure you can't place something like 12 Emerald and expect a team.
            document.querySelector("#result").innerHTML = "Please re-check your Grade and Section!" #Error message if the condition above is met
            return
        
        if GradeLevel == "Eleven" and Section not in ["Luna", "Amarsolo"]: #Likewise with this one for grade 11
            document.querySelector("#result").innerHTML = "Please re-check your Grade and Section!"
            return

        if GradeLevel in ["Nine", "Eight"] and Section not in ["Ruby", "Topaz", "Sapphire", "Emerald", "Jade"]: #This is separated from the next group of if lines because Jade is specifically only Grade 8-9
            document.querySelector("#result").innerHTML = "Please re-check your Grade and Section!"
            return
        
        if GradeLevel in ["Seven", "Nine", "Ten"] and Section not in ["Ruby", "Topaz", "Sapphire", "Emerald"]:
            document.querySelector("#result").innerHTML = "Please re-check your Grade and Section!"
            return
        
        team = "" # makes an empty variable called team to store the team name later on when a condition is met yeaupp

        if GradeLevel == "Ten": #Specific groupings, this one being for grade 10.
            if Section == "Topaz": #I actually followed the real life teams that were assigned to us for the TRUEST information.
                team = "Blue Bears" #If Grade level is ten and section is topaz, team is blue bears
            elif Section == "Emerald": #If not, check if section is emerald
                team = "Red Bulldogs" #if so, team is red bulldogs
            elif Section == "Sapphire": #rinse and repeat
                team = "Yellow Tigers"
            elif Section == "Ruby":
                team = "Green Hornets"

        elif GradeLevel == "Nine": #same thing but for grade 9.
            if Section == "Topaz":
                team = "Red Bulldogs"
            elif Section == "Emerald":
                team = "Green Hornets"
            elif Section == "Sapphire":
                team = "Yellow Tigers"
            elif Section == "Ruby":
                team = "Blue Bears"
            elif Section == "Jade": #additional section for Jade, same thing for Grade 8.
                team = "Green Hornets"

        elif GradeLevel == "Eight":
            if Section == "Topaz":
                team = "Blue Bears"
            elif Section == "Jade":
                team = "Blue Bears"
            elif Section == "Emerald":
                team = "Yellow Tigers"
            elif Section == "Sapphire":
                team = "Green Hornets"
            elif Section == "Ruby":
                team = "Red Bulldogs"

        elif GradeLevel == "Seven":
            if Section == "Topaz":
                team = "Green Hornets"
            elif Section == "Emerald":
                team = "Blue Bears"
            elif Section == "Sapphire":
                team = "Red Bulldogs"
            elif Section == "Ruby":
                team = "Yellow Tigers"
        
        elif GradeLevel == "Eleven":
            if Section == "Luna":
                team = "Yellow Tigers"
            elif Section == "Amarsolo":
                team = "Green Hornets"

        elif GradeLevel == "Twelve":
            if Section == "Tinio":
                team = "Red Bulldogs"
            elif Section == "Jose":
                team = "Blue Bears"

        else:
            team = "No team assigned." # you choose nothing and this shows.

        if team == "Blue Bears":  #specific message for blue bears
            image_url = team_images["Blue Bears"]
            document.querySelector("#result").innerHTML = f"You are assigned to: <b>{team}</b> <br> <img src='{image_url}' style='width: 40%'> <br> Welcome to the Blue Bears! Aim high and roar loud! <br> <a href='project.html'>Meet your team members!</a>"
        elif team == "Red Bulldogs": #specific message for red bulldogs
            image_url = team_images["Red Bulldogs"]
            document.querySelector("#result").innerHTML = f"You are assigned to: <b>{team}</b> <br> <img src='{image_url}' style='width: 40%'> <br> Welcome to the Red Bulldogs! Stay strong and bite hard! <br> <a href='project.html'>Meet your team members!</a>"
        elif team == "Yellow Tigers": #specific message for yellow tigers
            image_url = team_images["Yellow Tigers"]
            document.querySelector("#result").innerHTML = f"You are assigned to: <b>{team}</b> <br> <img src='{image_url}' style='width: 40%'> <br> Welcome to the Yellow Tigers! Be fierce and unstoppable! <br> <a href='project.html'>Meet your team members!</a>"
        elif team == "Green Hornets": #specific message for green hornets
            image_url = team_images["Green Hornets"]
            document.querySelector("#result").innerHTML = f"You are assigned to: <b>{team}</b> <br> <img src='{image_url}' style='width: 40%'> <br> Welcome to the Green Hornets! Strike fast and work together! <br> <a href='project.html'>Meet your team members!</a>"
        else:
            document.querySelector("#result").innerHTML = f"You are assigned to: <b>{team}</b>"
        #displays the team assigned based on the conditions met above.
        