from datetime import datetime

photo3 = "https://telegra.ph/file/485d5b950411e554ff696.jpg"

def sample_response(input_text):
  user_message = str(input_text).lower()

  if user_message in ("hi", "hello", "sup", "hiii", "hii", "kha hai"):
    return f"{photo3}\n\
    hey! adil is not here i am lara wanna play with me"

  if user_message in ("cute", "baccha", "your crush", "@ID_SELLER00"):
    return "HE is busy in her schedule. you can tell me i inform her"
  if user_message in ("bsdk", "madharchod", "bkl", "behanchod", "cgutiya",
                      "gaandu"):
    return "RANDI OFF HAI TO APNI MAA CHUDWA RHA RANDI KA PILA"

  if user_message in ("ladki", "pyar", "dhoka"):
    return "Pyar ek dhoka hai...dur he accha h"

  if user_message in ("time", "time?", "waqt"):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")

    return f"chal ab time dekh {str(date_time)}. haa dekh liya na time ab bhaag"
  # return "I don't understand"


# from replit import db
