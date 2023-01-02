import logging
from telegram.ext import *
from telegram import *
from requests import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

cart_cost = []
cart_cost_op='CART'
cart_items = []

#Main Menu Categories
option1="Category 1"
option2="Category 2"
option3="Category 3"

#Submenus
#sub1_menu menu
#Submenu 1 Quantities
qty1 = "Quantity 1"
qty2 = "Quantity 2"
qty3 = "Quantity 3"
qty4 = "Quantity 4"
submenu1_1="Submenu 1 Item 1" #Change this to whatever item name you want
submenu1_1_prices=["30", "60", "110", "220" ]
submenu1_1_qty=[f"{submenu1_1}-{qty1}",f"{submenu1_1}-{qty2}",f"{submenu1_1}-{qty3}",f"{submenu1_1}-{qty4}"]
submenu1_2="Submenu 1 Item 2" #Change this to whatever item name you want
submenu1_2_prices=["30", "60", "110", "220" ]
submenu1_2_qty=[f"{submenu1_2}-{qty1}",f"{submenu1_2}-{qty2}",f"{submenu1_2}-{qty3}",f"{submenu1_2}-{qty4}"]
submenu1_3="Submenu 1 Item 3" #Change this to whatever item name you want
submenu1_3_prices=["30", "60", "110", "220" ]
submenu1_3_qty=[f"{submenu1_3}-{qty1}",f"{submenu1_3}-{qty2}",f"{submenu1_3}-{qty3}",f"{submenu1_3}-{qty4}"]

#sub2_menu Menu
#Submenu 2 Quantities
s2qty1= "Quantity 1"
s2qty2= "Quantity 2"
s2qty3= "Quantity 3"
s2qty4= "Quantity 4"
submenu2_1="Submenu 2 Item 1" #Change this to whatever item name you want
submenu2_1_prices=["8", "70", "300", "500"]
submenu2_1_qty=[f"{submenu2_1}-{s2qty1}",f"{submenu2_1}-{s2qty2}",f"{submenu2_1}-{s2qty3}",f"{submenu2_1}-{s2qty4}"]
submenu2_2="Submenu 2 Item 2" #Change this to whatever item name you want
submenu2_2_prices=['15', "120", "550", "1000"]
submenu2_2_qty=[f"{submenu2_1}-{s2qty1}",f"{submenu2_1}-{s2qty2}",f"{submenu2_1}-{s2qty3}",f"{submenu2_1}-{s2qty4}"]

#Submenu 3's Categories
submenu3_sub_ops1="Submenu 3 Category 1"
submenu3_sub_ops2="Submenu 3 Category 2"

#Submenu 3 Quanitities
s3qty1= "Quantity 1"
s3qty2= "Quantity 2"
s3qty3= "Quantity 3"
s3qty4= "Quantity 4"
submenu3_sub_op1="Submenu 3 Cat 1 Item 1" #Change this to whatever item name you want
submenu3_sub_op1_prices=["30", "60", "110", "220"]
submenu3_sub_op1_qtys=[f"{submenu3_sub_op1}-{s3qty1}",f"{submenu3_sub_op1}-{s3qty2}",f"{submenu3_sub_op1}-{s3qty3}",f"{submenu3_sub_op1}-{s3qty4}"]
submenu3_sub_op2="Submenu 3 Cat 1 Item 2" #Change this to whatever item name you want
submenu3_sub_op2_prices=["30", "60", "110", "220"]
submenu3_sub_op2_qtys=[f"{submenu3_sub_op2}-{s3qty1}",f"{submenu3_sub_op2}-{s3qty2}",f"{submenu3_sub_op2}-{s3qty3}",f"{submenu3_sub_op2}-{s3qty4}"]


submenu3_sub_op3="Submenu 3 Cat 2 Item 1" #Change this to whatever item name you want
submenu3_sub_op3_prices=["30", "60", "110", "220"]
submenu3_sub_op3_qtys=[f"{submenu3_sub_op3}-{s3qty1}",f"{submenu3_sub_op3}-{s3qty2}",f"{submenu3_sub_op3}-{s3qty3}",f"{submenu3_sub_op3}-{s3qty4}"]
submenu3_sub_op4="Submenu 3 Cat 2 Item 2" #Change this to whatever item name you want
submenu3_sub_op4_prices=["30", "60", "110", "220"]
submenu3_sub_op4_qtys=[f"{submenu3_sub_op4}-{s3qty1}",f"{submenu3_sub_op4}-{s3qty2}",f"{submenu3_sub_op4}-{s3qty3}",f"{submenu3_sub_op4}-{s3qty4}"]

#Main Menu
main_menu_op="Main Menu"

#Keyboard Menus
Submenu1_kb= [[InlineKeyboardButton(submenu1_1, callback_data=submenu1_1),],[InlineKeyboardButton(submenu1_2, callback_data=submenu1_2),],[InlineKeyboardButton(submenu1_3, callback_data=submenu1_3),],[InlineKeyboardButton(main_menu_op, callback_data=main_menu_op),],]
Submenu2_kb= [[InlineKeyboardButton(submenu2_1, callback_data=submenu2_1),],[InlineKeyboardButton(submenu2_2, callback_data=submenu2_2),],[InlineKeyboardButton(main_menu_op, callback_data=main_menu_op),],]
Submenu3_ops_kb= [[InlineKeyboardButton(submenu3_sub_ops1, callback_data=submenu3_sub_ops1),],[InlineKeyboardButton(submenu3_sub_ops2, callback_data=submenu3_sub_ops2),],[InlineKeyboardButton(main_menu_op, callback_data=main_menu_op),],]
Submenu3_op1_kb= [[InlineKeyboardButton(submenu3_sub_op1, callback_data=submenu3_sub_op1),],[InlineKeyboardButton(submenu3_sub_op2, callback_data=submenu3_sub_op2),],[InlineKeyboardButton("Back", callback_data="1_back"),],]
Submenu3_op2_kb= [[InlineKeyboardButton(submenu3_sub_op3, callback_data=submenu3_sub_op3),],[InlineKeyboardButton(submenu3_sub_op4, callback_data=submenu3_sub_op4),],[InlineKeyboardButton("Back", callback_data="1_back"),],]
main_menu= [[InlineKeyboardButton(option1, callback_data=option1),],[InlineKeyboardButton(option2, callback_data=option2),],[InlineKeyboardButton(option3, callback_data=option3),],[InlineKeyboardButton("Shopping Cart", callback_data=cart_cost_op),],]

#Add to Cart Functions
submenu1_1_add=[[InlineKeyboardButton(f"Add {qty1} to Cart", callback_data=submenu1_1_qty[0]),],[InlineKeyboardButton(f"Add {qty2} to Cart", callback_data=submenu1_1_qty[1]),],[InlineKeyboardButton(f"Add {qty3} to Cart", callback_data=submenu1_1_qty[2]),],[InlineKeyboardButton(f"Add {qty4} to Cart", callback_data=submenu1_1_qty[3]),],[InlineKeyboardButton("Back", callback_data="1_Back_1")],]
submenu1_2_add=[[InlineKeyboardButton(f"Add {qty1} to Cart", callback_data=submenu1_2_qty[0]),],[InlineKeyboardButton(f"Add {qty2} to Cart", callback_data=submenu1_2_qty[1]),],[InlineKeyboardButton(f"Add {qty3} to Cart", callback_data=submenu1_2_qty[2]),],[InlineKeyboardButton(f"Add {qty4} to Cart", callback_data=submenu1_2_qty[3]),],[InlineKeyboardButton("Back", callback_data="2_Back_2")],]
submenu1_3_add=[[InlineKeyboardButton(f"Add {qty1} to Cart", callback_data=submenu1_3_qty[0]),],[InlineKeyboardButton(f"Add {qty2} to Cart", callback_data=submenu1_3_qty[1]),],[InlineKeyboardButton(f"Add {qty3} to Cart", callback_data=submenu1_3_qty[2]),],[InlineKeyboardButton(f"Add {qty4} to Cart", callback_data=submenu1_3_qty[3]),],[InlineKeyboardButton("Back", callback_data="3_Back_3")],]

submenu2_1_add=[[InlineKeyboardButton(f"Add {s2qty1} to Cart", callback_data=submenu2_1_qty[0]),],[InlineKeyboardButton(f"Add {s2qty2} to Cart", callback_data=submenu2_1_qty[1]),],[InlineKeyboardButton(f"Add {s2qty3} to Cart", callback_data=submenu2_1_qty[2]),],[InlineKeyboardButton(f"Add {s2qty4} to Cart", callback_data=submenu2_1_qty[3]),],[InlineKeyboardButton("Back", callback_data="4_Back_4")],]
submenu2_2_add=[[InlineKeyboardButton(f"Add {s2qty1} to Cart", callback_data=submenu2_2_qty[0]),],[InlineKeyboardButton(f"Add {s2qty2} to Cart", callback_data=submenu2_2_qty[1]),],[InlineKeyboardButton(f"Add {s2qty3} to Cart", callback_data=submenu2_2_qty[2]),],[InlineKeyboardButton(f"Add {s2qty4} to Cart", callback_data=submenu2_2_qty[3]),],[InlineKeyboardButton("Back", callback_data="5_Back_5")],]

submenu3_sub_op1_add=[[InlineKeyboardButton(f"Add {s3qty1} to Cart", callback_data=submenu3_sub_op1_qtys[0]),],[InlineKeyboardButton(f"Add {s3qty2} to Cart", callback_data=submenu3_sub_op1_qtys[1]),],[InlineKeyboardButton(f"Add {s3qty3} to Cart", callback_data=submenu3_sub_op1_qtys[2]),],[InlineKeyboardButton(f"Add {s3qty4} to Cart", callback_data=submenu3_sub_op1_qtys[3]),],[InlineKeyboardButton("Back", callback_data="6_Back_6")],]
submenu3_sub_op2_add=[[InlineKeyboardButton(f"Add {s3qty1} to Cart", callback_data=submenu3_sub_op2_qtys[0]),],[InlineKeyboardButton(f"Add {s3qty2} to Cart", callback_data=submenu3_sub_op2_qtys[1]),],[InlineKeyboardButton(f"Add {s3qty3} to Cart", callback_data=submenu3_sub_op2_qtys[2]),],[InlineKeyboardButton(f"Add {s3qty4} to Cart", callback_data=submenu3_sub_op2_qtys[3]),],[InlineKeyboardButton("Back", callback_data="6_Back_6")],]
submenu3_sub_op3_add=[[InlineKeyboardButton(f"Add {s3qty1} to Cart", callback_data=submenu3_sub_op3_qtys[0]),],[InlineKeyboardButton(f"Add {s3qty2} to Cart", callback_data=submenu3_sub_op3_qtys[1]),],[InlineKeyboardButton(f"Add {s3qty3} to Cart", callback_data=submenu3_sub_op3_qtys[2]),],[InlineKeyboardButton(f"Add {s3qty4} to Cart", callback_data=submenu3_sub_op3_qtys[3]),],[InlineKeyboardButton("Back", callback_data="7_Back_7")],]
submenu3_sub_op4_add=[[InlineKeyboardButton(f"Add {s3qty1} to Cart", callback_data=submenu3_sub_op4_qtys[0]),],[InlineKeyboardButton(f"Add {s3qty2} to Cart", callback_data=submenu3_sub_op4_qtys[1]),],[InlineKeyboardButton(f"Add {s3qty3} to Cart", callback_data=submenu3_sub_op4_qtys[2]),],[InlineKeyboardButton(f"Add {s3qty4} to Cart", callback_data=submenu3_sub_op4_qtys[3]),],[InlineKeyboardButton("Back", callback_data="7_Back_7")],]

#Start Function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = main_menu
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.effective_message.reply_photo(photo= "https://images.cdn2.stockunlimited.net/preview1300/menu-logo-icon_1710148.jpg", caption="Choose a category:", reply_markup=reply_markup)

#Menu Buttons
async def categories(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    query = update.callback_query
    await query.answer()
    data=query.data

# Menu options dictionary
# Format: {'callback_data': ('item_name', price, 'keyboard')}
    for i in range(4):
        menu_options = {
        submenu1_1_qty[i]: (submenu1_1_qty[i], submenu1_1_prices[i], submenu1_1_add),
        submenu1_2_qty[i]: (submenu1_2_qty[i], submenu1_2_prices[i], submenu1_2_add),
        submenu1_3_qty[i]: (submenu1_3_qty[i], submenu1_3_prices[i], submenu1_3_add),
        submenu2_1_qty[i]: (submenu2_1_qty[i], submenu2_1_prices[i], submenu2_1_add),
        submenu2_2_qty[i]: (submenu2_2_qty[i], submenu2_2_prices[i], submenu2_2_add),
        submenu3_sub_op1_qtys[i]: (submenu3_sub_op1_qtys[i], submenu3_sub_op1_prices[i], submenu3_sub_op1_add),
        submenu3_sub_op2_qtys[i]: (submenu3_sub_op2_qtys[i], submenu3_sub_op2_prices[i], submenu3_sub_op2_add),
}

        if data in menu_options:
        # Add item to cart
            item, price, keyboard = menu_options[data]
            cart_items.append(item)
            cart_cost.append(price)
            total_amount = sum(map(int, cart_cost))
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_caption(caption=f'{item} added to the cart!', reply_markup=reply_markup)
            continue

    back_options = {
        "1_Back_1": (Submenu1_kb, "https://images.cdn2.stockunlimited.net/preview1300/menu-logo-icon_1710148.jpg", f"{option1}:"),
        "2_Back_2": (Submenu1_kb, "https://images.cdn2.stockunlimited.net/preview1300/menu-logo-icon_1710148.jpg", f"{option1}:"),
        "3_Back_3": (Submenu1_kb, "https://images.cdn2.stockunlimited.net/preview1300/menu-logo-icon_1710148.jpg", f"{option1}:"),
        "4_Back_4": (Submenu2_kb, "https://images.cdn2.stockunlimited.net/preview1300/menu-logo-icon_1710148.jpg", f"{option2}:"),
        "5_Back_5": (Submenu2_kb, "https://images.cdn2.stockunlimited.net/preview1300/menu-logo-icon_1710148.jpg", f"{option2}:"),
        "6_Back_6": (Submenu3_ops_kb, "https://images.cdn2.stockunlimited.net/preview1300/menu-logo-icon_1710148.jpg", f"{option3}:"),
        "7_Back_7": (Submenu3_ops_kb, "https://images.cdn2.stockunlimited.net/preview1300/menu-logo-icon_1710148.jpg", f"{option3}:"),
    }

    if data in back_options:
        keyboard, photo, caption = back_options[data]
        reply_markup = InlineKeyboardMarkup(keyboard)
        media = InputMediaPhoto(photo, caption=caption)
        await query.edit_message_media(media=media, reply_markup=reply_markup)

    if cart_cost_op in data:
        total_amount = sum(map(int, cart_cost))
        items = set(cart_items)
        await update.effective_message.reply_text(f'Cart Total: ${(total_amount)}')

        item_counts = {}
        for item in cart_items:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

        for item, count in item_counts.items():
            await update.effective_message.reply_text(f"{count}:{item}")


# Initial Categories
    categories = {
        option1: (Submenu1_kb, query.edit_message_caption, f"{query.data}:",),
        option2: (Submenu2_kb, query.edit_message_caption, f"{query.data}:",),
        option3: (Submenu3_ops_kb, query.edit_message_caption, f"{query.data}:",),
    }

    submenus = {
        submenu1_1: (submenu1_1_add, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Un1.svg/1200px-Un1.svg.png', 'Submenu 1 Option 1'),
        submenu1_2: (submenu1_2_add, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Deux.svg/1200px-Deux.svg.png', 'Submenu 1 Option 2'),
        submenu1_3: (submenu1_3_add, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Trois.svg/1200px-Trois.svg.png', 'Submenu 1 Option 3'),
        submenu2_1: (submenu2_1_add, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Quatre.svg/1200px-Quatre.svg.png', "Submenu 2 option 1"),
        submenu2_2: (submenu2_2_add, query.edit_message_media, "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Cinq.svg/800px-Cinq.svg.png", "Submenu 2 option 2"),
        submenu3_sub_ops1: (Submenu3_op1_kb, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Un1.svg/1200px-Un1.svg.png', f"{submenu3_sub_ops1}:"),
        submenu3_sub_ops2: (Submenu3_op2_kb, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Deux.svg/1200px-Deux.svg.png', f"{submenu3_sub_ops2}:"),
        submenu3_sub_op1: (submenu3_sub_op1_add, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Un1.svg/1200px-Un1.svg.png', f"{submenu3_sub_op1}:"),
        submenu3_sub_op2: (submenu3_sub_op2_add, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Un1.svg/1200px-Un1.svg.png', f"{submenu3_sub_op2}:"),
        submenu3_sub_op3: (submenu3_sub_op3_add, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Un1.svg/1200px-Un1.svg.png', f"{submenu3_sub_op3}:"),
        submenu3_sub_op4: (submenu3_sub_op4_add, query.edit_message_media, 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Un1.svg/1200px-Un1.svg.png', f"{submenu3_sub_op4}:"),
    }

    if data in categories:
        keyboard, func, text = categories[data]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await func(caption=text, reply_markup=reply_markup)

    elif data in submenus:
        keyboard, func, photo, caption = submenus[data]
        media = InputMediaPhoto(photo, caption=caption)
        reply_markup = InlineKeyboardMarkup(keyboard)
        await func(media=media, reply_markup=reply_markup)
        
    #Main Menu Category    
    if main_menu_op in data:
        keyboard=main_menu
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_caption(caption=f"{query.data}:", reply_markup=reply_markup)

        
def main() -> None:
    application = ApplicationBuilder().token('ADD Bot TOKEN HERE').build()
    application.add_handler(CommandHandler("start", start))
    
    #Below this line we will use the query handler for different things
    application.add_handler(CallbackQueryHandler(categories))

    
    application.run_polling()

if __name__ == "__main__":
    main()