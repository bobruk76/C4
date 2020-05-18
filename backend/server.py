import bottle


class TodoItem:
    def __init__(self, description, unique_id):
        self.description = description
        self.is_completed = False
        self.uid = unique_id

    def __str__(self):
        return self.description.lower()

    def to_dict(self):
        return {
            "description": self.description,
            "is_completed": self.is_completed,
            "uid": self.uid
        }


tasks_db = {
    uid: TodoItem(desc, uid)
    for uid, desc in enumerate(
        start=1,
        iterable=[
            "прочитать книгу",
            "учиться жонглировать 30 минут",
            "помыть посуду",
            "поесть",
        ],
    )
}


@bottle.route("/api/tasks/")
def index():
    tasks = [task.to_dict() for task in tasks_db.values()]
    return {"tasks": tasks}


@bottle.route("/api/add-task", method="POST")
def add_task():
    desc = bottle.request.POST.description.strip()
    if len(desc) > 0:
        new_uid = max(tasks_db.keys()) + 1
        t = TodoItem(desc, new_uid)
        tasks_db[new_uid] = t
    return "OK"


@bottle.route("/api/delete/<uid:int>")
def api_delete(uid):
    tasks_db.pop(uid)
    return "OK"


@bottle.route("/api/complete/<uid:int>")
def api_complete(uid):
    tasks_db[uid].is_completed = True
    return "Ok"


bottle.run(host="localhost", port=5000)
