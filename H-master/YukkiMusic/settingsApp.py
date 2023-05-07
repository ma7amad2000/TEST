import json

import os


class BotSettings:
    path_file = 'settings_bot.json'

    # def __init__(self, *args, **kwargs):
    
    #     self.info = kwargs
    #     self.run()

    # def run(self):

    #     search_file = self.check_file()
    #     if search_file:
    #         self.write_in_file()

    # #check if not has create
    # def check_file(self):
    #     if os.path.isfile(self.path_file):
    #         return True
                
    #     else:
    #         with open(self.path_file, 'w') as fp: 
    #             fp.write('[]')
    #             return True
        

    # #write
    # def write_in_file(self):
    #     with open(self.path_file, "r+",encoding='utf-8') as file:
    #         data = json.load(file)
    #         data.append(self.info)
    #         file.seek(0)
    #         json.dump(data, file,ensure_ascii=False,indent=2 )

    # read 
    def read_in_file(self,status_app=None):
        if not status_app:
            return
        with open(self.path_file, "r+",encoding='utf-8') as file:
            data = json.load(file)
            result = data[status_app]
        return result

    # change values
    def edit_in_file(self,status_app=None,new_value=None):
        if (not status_app) or (not new_value):
            return

        data = {"open":new_value}
        with open(self.path_file, 'w') as f:
            json.dump(data, f, indent=4)


        return new_value
# print('Chane')
# c = BotSettings()
# cc = c.edit_in_file('open',"no")
# print(cc)

# print('read Test')
# c = BotSettings()
# cc = c.read_in_file('open')
# print(cc)
