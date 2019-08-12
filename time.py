class time:
    def get_time(self):
        self.time=int(input("enter the total number of seconds:"))
    def show_time(self):
        hour=self.time//3600
        self.time%=3600
        minutes=self.time//60
        self.time%=60
        seconds=self.time
        print("time is:",hour,":",minutes,":",seconds)
t=time()
t.get_time()
t.show_time()