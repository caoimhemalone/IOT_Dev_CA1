import dweepy

def publish():
    dict = {}
    dict["publish"] = "true"
    dweepy.dweet_for('caoimhe', dict)

    String thingName = "CaoimhesThing";

publish()