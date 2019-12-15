"""When this auxiliary script is run from Python Console, it enables experimenting with the database of a Django app
manually, from the console, by instantiating models and running commands like:
    - <Model>.objects.all() - display all the items of a certain type
    - m = <Model>(<p1>, <p2>,...) - create a new object/item m by instantiating a model class <Model>
                                    (<p1>, <p2>,... are the model field values passed to the <Model> constructor)
    - save it in the database by calling <object>.save() explicitly
      (you can actually instantiate a model class with an empty constructor (no parameters)
      and then populate its fields with <object>.<field> = <new value>;
      don't forget to <object>.save() everything in the end if you need it saved)
    - <Model>.objects.create() - create a new object/item; no need to <object>.save() afterwords
    - <object>.id or <object>.pk - show the id field of an object
    - <object>.<field> - show the value of another field of the object
    - <object/item>.<field> = <new value> - change the value of an object's field
"""


import sys
import django
django.setup()

from django.apps import apps


for _class in apps.get_models():
   globals()[_class.__name__] = _class
