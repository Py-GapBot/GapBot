from gapbot import Gap  # import library;

app = Gap(bot_token='your_bot_token')  # instance of Main Class;
# if you need use bot parameters you must set bot_token;

if __name__ == '__main__':  # If you are running this module as the main program;
    target_id = 000000  # whose to be send text to him;
    text = "GapBot SendText"
    reply_keyboard = {
        "keyboard": [
            [
                {"row1-btn1":"خط اول-دکمه اول"},
                {"row1-btn2":"خط اول-دکمه دوم"}
            ],
            [
                {"row2-btn1": "خط دوم-دکمه اول"}
            ],
            [
                {"$contact": "تلفن"},  # to get target's phone number;
                {"$location": "لوکیشن"}  # to get target's location;
            ],
        ],
    }
    inline_keyboard = [
        [
            {"text":"معمولی","cb_data":"normal"},
        ],
        [
            {"text":"وب سایت","url":"http://google.com","open_in":"webview_with_header"},
            {"text":"دونیت","amount":2000,"currency":"IRR","ref_id":"XXXXXXX","desc":"توضیحات مربوط به پرداخت برای نمایش در لیست تراکنش ها"}
        ]
    ]
    form = [
        {"name": "name", "type": "text", "label": "Name"},
        {"name": "married", "type": "radio", "label": "Married", "options": [{"y": "Yes"}, {"n": "No"}]},
        {"name": "city", "type": "select", "label": "City", "options": [{"mah": "Mashhad"}, {"teh": "Tehran"}]},
        {"name": "address", "type": "textarea", "label": "Address"},
        {"name": "test_bc", "type": "inbuilt", "value": "barcode", "label": "Scan barcode"},
        {"name": "test_qr", "type": "inbuilt", "value": "qrcode", "label": "Scan qr-code"},
        {"name": "agree", "type": "checkbox", "label": "I agree"},
        {"type": "submit", "label": "Save"}
    ]
    app.send_text(
        chat_id=target_id,  # https://developer.gap.im/doc/botplatform#chatId-description
        text=text,
        reply_keyboard=reply_keyboard,  # https://developer.gap.im/doc/botplatform#reply_keyboard-description
        inline_keyboard=inline_keyboard,  # https://developer.gap.im/doc/botplatform#inline_keyboard-description
        reply_form=form,  # https://developer.gap.im/doc/botplatform#form-description
    )

# https://developer.gap.im/doc/botplatform#method-send-text
