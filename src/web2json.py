import datetime as dt
from xml.dom.minidom import Element
import utils

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


def getinput(*ags, **kws):

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
    print (input)


#def parseinput(*args, **kws):
#    json="{"
#    for elem in getinput():
#        json+=str(elem)
#        json+=","
#        json2=json[:-1]
#    json2 +="}"
#    print (json2)
#    return json2

#def main():
#    getinput(*ags, **kws)
#    getinput(*ags, **kws)

#main()

getinput()
