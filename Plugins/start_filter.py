from pyrogram import filters

def s_filter(_,__,message):
   if str(message.text)[1:] == "start":
      return True
   else:
      return False

start_filter = filters.create(s_filter)
