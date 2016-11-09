odin = {"name": "Odin", "age": 6000, "height": 3 * 3 + 9 / 5}
print(odin)
print(odin["name"])

odin["city"] = "Asgard"
print(odin)

thor = {1: "Thor", 2: 5000, 3: "Asgard"}
print(thor[1])

del thor[2]
print(thor)

days = {
    "Sunday":
        """
        Cool
        Cool
        gay
        """,
    "Monday":
        """
        Yoo
        Yoo
        Gay
        """
}
print("=" * 50)
print(days["Monday"])
