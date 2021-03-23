import json
import os


class RWFile:
    def __init__(self, patch, name, file):
        self.patch = patch
        self.name = name
        self.file = file

    def read(self):
        with open(os.path.join(self.patch, self.name), 'r', encoding='utf-8') as f:
            self.file = json.load(f)
            return self.file

    def write(self):
        with open(os.path.join(self.patch, self.name), 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.file, indent=2, ensure_ascii=False))


class Message:
    def __init__(self, message, hashtag):
        self.message = message
        self.hashtag = hashtag

    def merge(self):
        temp = ""
        for sample in self.message:
            temp += ''.join(map(str, ('\n', sample)))
        self.message = temp

    def caption(self):
        self.message = ''.join(map(str, (self.hashtag, self.message)))

    def get(self):
        return self.message

class PostReadFromNet:
    def __init__(self):



    def post(self):
        post_msg(vkapp,
                 base['id']['post_group']['key'],
                 postmsg,
                 '')

    def post_msg(vk, group, text_send, attach):
        vk.wall.post(owner_id=group,
                     from_group=1,
                     message=text_send,
                     attachments=attach,
                     v=5.102)

    def upload_post_to_main_group(vkapp, msg, base):
        postatach = ''
        if 'attachments' in msg:
            postatach = get_attach(msg)
        try:
            post_msg(vkapp,
                     base['id']['post_group']['key'],
                     msg['text'],
                     postatach)
        except:
            return False
        return True

