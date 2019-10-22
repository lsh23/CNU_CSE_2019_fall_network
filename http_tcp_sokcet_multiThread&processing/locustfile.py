from locust import HttpLocust, TaskSet, task
class websiteTasks(TaskSet):
    def on_start(self):
        self.client.verify = False

    @task(1)
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = websiteTasks
    min_wait = 1500
    max_wait = 5000