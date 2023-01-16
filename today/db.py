from models import ConfModel

class CreateRecord:
    def conferences(self, **kwargs):
        ConfModel.create(
            #id=kwargs['id'],
            name=kwargs['name'],
            link=kwargs['link'],
            abbreviation=kwargs['abbreviation'],
            shortname=kwargs['shortname'],
            active=kwargs['active']
        )

class UpdateRecord:
    def conferences(self):
        pass

class DeleteRecord:
    def conferences(self):
        pass

class ReadRecord:
    def conferences(self):
        pass