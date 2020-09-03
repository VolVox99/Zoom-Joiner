import schedule
import datetime
import webbrowser



def main():
    webbrowser.open_new_tab('http://google.com')



running = True

while running:
    update_time = datetime.datetime.now()
    update_hrs, update_mins = update_time.hour, update_time.minute
    
    if update_hrs == 17 and update_mins == 50:
        main()
        running = False