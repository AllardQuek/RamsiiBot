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