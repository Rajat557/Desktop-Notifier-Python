from plyer import notification
import time
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Drink WATER..!!",
            message = "take some break;) strech out'_'                     You are getting it**",
            app_icon ="C:\\Users\Swapnil\Desktop\desktopNotification_drinkWater\icon.ico",
            timeout = 30
        )
        time.sleep(60*60)