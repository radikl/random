import random

first_name = input("Hello questioner, what is your first name?  ")
print("Welcome " + first_name + ", let us now read your fortune.")
reading_type = input(
    "Would you like to know about your Past, Present, or Future?  ")

#Generate a random number from 1-22, then assign a card name based on that number
card_drawn = random.randint(1, 22)
if card_drawn == 1:
    card_drawn = "The Fool"
if card_drawn == 2:
    card_drawn = "The Magician"
if card_drawn == 3:
    card_drawn = "The High Priestess"
if card_drawn == 4:
    card_drawn = "The Empress"
if card_drawn == 5:
    card_drawn = "The Emperor"
if card_drawn == 6:
    card_drawn = "The Hierophant"
if card_drawn == 7:
    card_drawn = "The Lovers"
if card_drawn == 8:
    card_drawn = "The Chariot"
if card_drawn == 9:
    card_drawn = "Strength"
if card_drawn == 10:
    card_drawn = "The Hermit"
if card_drawn == 11:
    card_drawn = "Wheel of Fortune"
if card_drawn == 12:
    card_drawn = "Justice"
if card_drawn == 13:
    card_drawn = "The Hanged Man"
if card_drawn == 14:
    card_drawn = "Death"
if card_drawn == 15:
    card_drawn = "Temperance"
if card_drawn == 16:
    card_drawn = "The Devil"
if card_drawn == 17:
    card_drawn = "The Tower"
if card_drawn == 18:
    card_drawn = "The Star"
if card_drawn == 19:
    card_drawn = "The Moon"
if card_drawn == 20:
    card_drawn = "The Sun"
if card_drawn == 21:
    card_drawn = "Judgement"
if card_drawn == 22:
    card_drawn = "The World"

print(first_name + ", you have drawn the card " + card_drawn + ".")

"""Change the card drawn variable to qualify it based on the type of reading
requested. This allows you to pull the correct meaning below."""
if reading_type == "Past":
    card_drawn += (" - Past")
if reading_type == "Present":
    card_drawn += (" - Present")
if reading_type == "Future":
    card_drawn += (" - Future")

if card_drawn == "The Fool - Past":
    card_meaning = "The Fool can represent you wasting time that you could have used for studies. It could represent a lover from days gone by if you had a deep relationship with an artist or musician or some person who lived outside of conventional society."
if card_drawn == "The Fool - Present":
    card_meaning = "The Fool in the present position signifies that you are about to abandon commitments and constraints in a search for a self-defining freedom. The Fool is the most powerful card in all the Tarot deck when it is in the present position. Your free will can literally move mountains at this moment in time – the Tarot is telling you an ancient slogan: carpe diem – seize the day."
if card_drawn == "The Fool - Future":
    card_meaning = "In the future position, The Fool most likely represents you enjoying a new life. It can also represent a coming love interest who is not ordinary by any of your measurements."

willingness = input("With that in mind, would you like me to explain the meaning of this card in the " + reading_type + " position? Yes or No  ")
if willingness == "Yes":
    print(card_meaning)
if willingness == "No":
    print("""Ah, i completely understand. Knowledge is powerful, and that can be scary.
        Please return when you are more willing to delve into these mysteries with me""")