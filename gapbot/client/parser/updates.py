from gapbot.client.types import update
from json import loads as json_loads


class Updates:
    @staticmethod
    def json2object(json_update):
        return update.Update(
            chat_id=json_update.get('chat_id'),
            from_user=json_update.get('from'),
            update_type=json_update.get('type'),
            data=json_update.get('data'),
            json_update=json_update
        )

    @staticmethod
    def update2json(immutable_multi_dict_update):
        immutable_update = dict(immutable_multi_dict_update)
        json_update = {
            'chat_id': immutable_update.get('chat_id'),
            'type': immutable_update.get('type'),
        }
        if immutable_update.get('from'):
            try:
                json_update['from'] = json_loads(immutable_update.get('from'))
            except:
                json_update['from'] = immutable_update.get('from')
        if immutable_update.get('data'):
            try:
                json_update['data'] = json_loads(immutable_update.get('data'))
            except:
                json_update['data'] = immutable_update.get('data')
        return json_update
