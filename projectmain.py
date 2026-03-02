from js import document, window  # type: ignore


def TeamPlays(event=None):

    team = document.querySelector("#TEAM").value

    if team == "Placeholder":
        document.querySelector("#result").innerHTML = (
            "<br>Please select a team to find your players!"
        )
        return

    team_players = {
        "Blue Bears": ["AKINGSON JAKE ANDES", 
                       "ALEXANDER TACAN", "ALEXI VILLANUEVA", "ASHLEY KIRSTEN Y. SANTOS", "AUDREY ANNE DUMAGUING", "AURORA ISHTAR A. UBANA", "CYRENNE MENDEZ", "DANIELLE ALEENA NOBLE", "FIL AYALA", "GABRIELLE L. DAMONDAMON", "GIOVANNI ESCARDA", "JARIX ZALES", "JOHN ALFRED F. TARUC JR.", "JOHN LIGAS", "JOSEPH DERAY", "KURT TENORIO", "MARGAUX ALAINA FERRER", "MARLEY SUMMER MANESE", "MARTINA CABRILLOS", "MARY BERNADETTE DAED", "MIKE JARED DE JESUS", "NATHAN MARI ANTHONY DEVERA GRANDE", "NATHAN TIONGSON", "PAULINE ECRAEALA", "RISO SALAPUNEN", "VIC GOROM", "ZION MARGARET FABUL"],
        "Red Bulldogs": ["TO BE ANNOUNCED"],
        "Yellow Tigers": ["TO BE ANNOUNCED"],
        "Green Hornets": ["TO BE ANNOUNCED"]
    }

    players_html = ""
    for player in team_players[team]:
        players_html += player + "<br>"

    document.querySelector("#result").innerHTML = (
        f"<b>Team:</b> <b>{team}</b><br><b>Players:</b><br> {players_html}"
    )