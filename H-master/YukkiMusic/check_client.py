
 

def _check_client(CallbackQuery):

    user_id = CallbackQuery.from_user.id
    if user_id != CallbackQuery.message.reply_to_message.from_user.id:
        return 
    return True
