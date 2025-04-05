from telegram.ext import Updater, CommandHandler

# التوكن الخاص بالبوت
TOKEN = '7884643878:AAHnUDPxVR1X7fLyTAkRNRobMcYlTy-RVeI'

# دالة الأمر /start
def start(update, context):
    update.message.reply_text("مرحباً بكم في بوت QATEEBAh store! اختر من الأوامر التالية:\n/start لبدء المحادثة\n/products لعرض المنتجات")

# دالة الأمر /products
def products(update, context):
    update.message.reply_text("إليك بعض المنتجات المتوفرة في المتجر:\n1. منتج 1\n2. منتج 2\n3. منتج 3")

# دالة الأمر /cart
def cart(update, context):
    update.message.reply_text("سلة التسوق الخاصة بك تحتوي على:\nمنتج 1\nمنتج 2")

# دالة الأمر /checkout
def checkout(update, context):
    update.message.reply_text("انتقل إلى صفحة الدفع لإتمام عملية الشراء.")

# دالة الأمر /help
def help(update, context):
    update.message.reply_text("للحصول على المساعدة، اختر من الأوامر التالية:\n/start لبدء المحادثة\n/products لعرض المنتجات")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # إضافة الأوامر مع ربطها بالوظائف
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("products", products))
    dp.add_handler(CommandHandler("cart", cart))
    dp.add_handler(CommandHandler("checkout", checkout))
    dp.add_handler(CommandHandler("help", help))

    # بدء البوت
    updater.start_polling()

    # إبقاء البوت يعمل حتى إيقافه يدوياً
    updater.idle()

if __name__ == '__main__':
    main()
