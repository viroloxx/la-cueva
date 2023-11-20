from Metrogram import *
from Api import *

def main():
   
    Api.save_data_user(user_data,user_text)
    Api.save_data_post(post_data, post_text)
    app = Metrogram()
    app.welcome()
main()
