# This script provides clothing recommendations based on user-inputted weather conditions.

def get_weather_advice():
    """
    Prompts the user for weather input and provides clothing recommendations
    based on the input using if, elif, and else statements.
    """
    # Prompt the user to input the current weather condition.
    # The input is converted to lowercase to ensure case-insensitive matching.
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

    # Use conditional statements to provide clothing recommendations based on the weather.
    if weather == "sunny":
        # If the weather is sunny, recommend light clothing and sun protection.
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        # If the weather is rainy, recommend rain gear.
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        # If the weather is cold, recommend warm clothing.
        print("Make sure to wear a warm coat and a scarf.")
    else:
        # If the input does not match any of the predefined conditions,
        # print a message indicating that no recommendation is available.
        print("Sorry, I don't have recommendations for this weather.")

# Call the function to execute the script.
if __name__ == "__main__":
    get_weather_advice()
