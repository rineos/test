italy_characteristics = {
    "definition": "Italy is a country in Southern Europe located on the Apennine Peninsula and numerous adjacent islands.",
    "geography": "Italy has diverse geography, including the Alps in the north, the Apennines running down the central peninsula, and numerous islands such as Sicily and Sardinia.",
    "history": "Italy is known for its rich history, spanning millennia. It was the heart of the Roman Empire and the birthplace of the Renaissance.",
    "culture": "Italy is celebrated for its cultural heritage, including art, architecture, cuisine, and music. Italian cuisine is famous for pasta, pizza, olive oil, and wine.",
    "scale": "301,338 square kilometers.",
    "capital of italy": "Rome.",
    "how many people live in italy?": "Approximately 60,461,826 people.",
    "what is the climate in italy?": "Most of the territory of Italy lies in the subtropical climatic zone, the north - in a temperate, transitional from maritime to continental type.",
    "which seas wash italy?": "Italy is washed by the waters of the Mediterranean Sea, the Atlantic Ocean, the Ligurian Sea in the northwest, the Tyrrhenian Sea in the west, the Ionian Sea in the southeast, and the Adriatic Sea in the east.",
}
def get_characteristic_info(characteristic):
    characteristic = characteristic.lower()
    return italy_characteristics.get(characteristic, "Such characteristic is not found.")

while True:
    user_input = input("Enter a characteristic of Italy (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    response = get_characteristic_info(user_input)
    print(response)
