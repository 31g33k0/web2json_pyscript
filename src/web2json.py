import datetime as dt
from xml.dom.minidom import Element
#import pyscript
# import utils

#tasks = []
#task_template = Element("task-template").select(".task", from_content=True)
#task_list = Element("list-tasks-container")
#new_task_content = Element("new-task-content")


#input=[1,3,4,3]
id = Element("id")
creators = Element("creators")
work_scope = Element("work_scope")
work_time = Element("work_time")
impact_scope = Element("impact_scope")
impact_time = Element("impact_time")
rights = Element("rights")
uri = Element("uri")


def getInput(*ags, **kws):

    input = {
#        "id": id,
        "creators": creators,
        "work_scope": work_scope,
        "work_time":work_time,
        "impact_scope":impact_scope,
        "impact_time":impact_time,
        "rights":rights,
        "uri":uri,
#        "done": False,
#        "created_at": dt.now(),
    }
    return (input)

#pyscript.write('json',getInput())


Element('json').innerText = getInput(creators,work_scope,work_time)

#print("test")
print(getInput())
