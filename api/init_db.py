import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

TITLE = 0
DESC = 1
TIME = 2
IMAGE = 3

activities = [["Bungee Jump into Olympus Mons", "After its last eruption in 2410, Olympus Mons is expected to remain dormant for the next few centuries. Take advantage of this opportunity in an exhilarating drop inside the volcano itself. With state-of-the-art, turbo-boosted, heat-resistant bungee rope, you can enjoy a 5km dive and explore 1/5 of Olympus Mons' incredible depth! **Planetinerary Tourism Office takes no responsibility for any accidents :)", "10/10/2560, 09:00-17:00", "mars_olympus.png"],
              ["A Tour of Oppy Museum", "With the famous last words of “my battery is low and it’s getting dark,” as shown in the 2022 classic “Goodnight Oppy”, the Opportunity Mars Rover won the hearts of the public after it’s almost 15 year long space expedition ended in 2018. You have the chance to see this ground-breaking discoverer for yourself after its remains were found in 2134. The museum was built around it’s initial landing site in 2004, so you can watch its journey come full circle.", "10/10/2560, 18:00-19:00", "mars_oppy.png"],
              ["A Walk Along Kasei Valles", "This outflow channel system of canyons boasts an incredible size of 482km wide and 1580km long, making our Earth’s Grand Canyon look like a walk in the park! Near the Valles Marianeries, learn as the canyon floor may hold the secrets to ancient water on Mars and how major flooding events could have caused the formation of this giant landmark.", "10/11/2560, 13:00-20:00", "mars_valle.png"],
              ]

for a in activities:    
    cur.execute("INSERT INTO activities (title, content, time, image, added) VALUES (?, ?, ?, ?, ?)", (a[TITLE], a[DESC], a[TIME], a[IMAGE], False))

connection.commit()
connection.close()