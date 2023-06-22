from mycroft import MycroftSkill, intent_file_handler


class FruitLister(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lister.fruit.intent')
    def handle_lister_fruit(self, message):
        self.speak_dialog('lister.fruit')


def create_skill():
    return FruitLister()

