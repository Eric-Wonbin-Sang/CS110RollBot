
class Student:

    def __init__(self, data_dict):

        self.data_dict = data_dict

        self.canvas_id = self.data_dict["ID"]
        self.first_name = self.data_dict["First"]
        self.last_name = self.data_dict["Last"]
        self.email = self.data_dict["Email"]

        self.lab = self.data_dict["Lab"]
        self.section_id = self.data_dict["Section"]
        self.manager = self.data_dict["TA"]

    def get_class_list(self):
        pass

    def __str__(self):
        return "Section {}, Lab {}: {} {}".format(
            self.section_id,
            self.lab,
            self.first_name,
            self.last_name
        )
