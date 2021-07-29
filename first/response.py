from simple_chatbot.responses import GenericRandomResponse


class GreetingResponse(GenericRandomResponse):
    choices = ("Hey, how can I help you?",
               "Hey friend. How are you? How can I help you?")

class JusttalkResponse(GenericRandomResponse):
    choices = ("hi Dear,SignUp first",
               "Dear Signup and login ",
               "U can create an event using blog now")
class WorkResponse(GenericRandomResponse):
    choices = ("after login open my blogs to watch  ur blogs",
               "My blogs will take you to ur blogs",
               "Created blogs are found in myblogs")


class GoodbyeResponse(GenericRandomResponse):
    choices = ("See you later.",
               "Thanks for visiting.",
               "See ya! Have a nice day.")