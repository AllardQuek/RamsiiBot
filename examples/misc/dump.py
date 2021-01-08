conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start), CommandHandler("trivia", trivia_command)],
    states={
        GENDER: [MessageHandler(Filters.regex('^(Boy|Girl|Other)$'), gender)],
        PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
        LOCATION: [
            MessageHandler(Filters.location, location),
            CommandHandler('skip', skip_location),
        ],
        BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

dispatcher.add_handler(conv_handler)


keyboard = [
    [
        InlineKeyboardButton("Substitute Ingredient", callback_data='/substitute'),
        InlineKeyboardButton("Trivia", callback_data='trivia'),
    ],
    [InlineKeyboardButton("Option 3", callback_data='3')],
]

reply_markup = InlineKeyboardMarkup(keyboard)

update.message.reply_text(intro, reply_markup=reply_markup) 

update.message.reply_text(text=user_search(f"{ingredient}"), parse_mode= ParseMode.HTML)

===

conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start), CommandHandler('trivia', trivia_command)],
        states={
            FIRST: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                # CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
            ],
            # SECOND: [
            #     CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
            #     CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
            # ],
        },
        fallbacks=[CommandHandler('start', start)],
        per_message=True
    )

    # Add ConversationHandler to dispatcher that will be used for handling
    # updates
    dispatcher.add_handler(conv_handler)


===

def one(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    print("HELLO")
    logger.info("BIEBFE")
    query = update.callback_query
    query.answer()

    # keyboard = [
    #     [
    #         InlineKeyboardButton("3", callback_data=str(THREE)),
    #         InlineKeyboardButton("4", callback_data=str(FOUR)),
    #     ]
    # ]
    # reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="First CallbackQueryHandler, Choose a route"
    )
    return FIRST

===

# Stages
FIRST, SECOND = range(2)
# Callback data
ONE, TWO = range(2)

===

return Updater.stop()
    return ConversationHandler.END

    update.message.reply_text(
        'Bye! See you again 😃', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

    ===

    query.edit_message_reply_markup(ReplyKeyboardRemove())
    query.edit_message_text(text=sub)