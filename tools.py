from datetime import datetime


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S)

# Each { } will represent one function and it's property to LLM
TOOLS = [
    {
        "type" : "function",
        "function" : {
            "name" : "get_current_time",
            "description" : "Returns the current date and time in formatted string.",
            "parameters" : {
                "type" : "object",
                "properties" : {}
            }
        }
    }
]
