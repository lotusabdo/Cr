"""
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="Yrw1 " + str(m.from_user.id))],
        [InlineKeyboardButton("➡️ التالي", callback_data="Yrw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع🔙", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],
"""

import asyncio


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from AbdoX import app



@app.on_message(filters.command(["افلام"], ""))
async def aflamAR(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("افلام 🎬", callback_data="film " + str(m.from_user.id))],
        [InlineKeyboardButton("مسلسلات 📼", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("كارتون للاطفال 🎭 ", callback_data="msrahia " + str(m.from_user.id))],

        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
        
    ])
    await m.reply_text("◍ اهلا بيك في قائمة الافلام والمسلسلات العربيه\n√", reply_markup=keyboard)


# Replay Edit
@app.on_callback_query(filters.regex("^aflamAR2 (\\d+)$"))
async def aflamAR2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("افلام 🎬", callback_data="film " + str(m.from_user.id))],
        [InlineKeyboardButton("مسلسلات 📼", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("كارتون للاطفال 🎭 ", callback_data="msrahia " + str(m.from_user.id))],

        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
        
    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام والمسلسلات العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^film (\\d+)$"))
async def film(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("كوميدي 😹", callback_data="comedy " + str(m.from_user.id))],
        [InlineKeyboardButton("اكشن 🔥", callback_data="action " + str(m.from_user.id))],
        [InlineKeyboardButton("دراما 🌚", callback_data="drama " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع🔙", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام العربيه\n√", reply_markup=keyboard)




@app.on_callback_query(filters.regex("^comedy (\\d+)$"))
async def comedy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ وقفة رجاله", callback_data="Xco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الخطة العايمة", callback_data="Xco2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بنات ثانوي", callback_data="Xco3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ عفريت ترانزيت", callback_data="Xco4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ زكي شان", callback_data="Xco5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سمير وشهير وبهير", callback_data="Xco6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تصبح علي خير", callback_data="Xco7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بابا", callback_data="Xco8 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جدو نحنوح", callback_data="Xco9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سمير ابو النيل", callback_data="Xco10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ كلبي دليلي", callback_data="Xco11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بنات العم", callback_data="Xco12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ علي بابا", callback_data="Xco13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ فول الصين العظيم", callback_data="Xco14 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حسن وبقلظ", callback_data="Xco15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الكويسين", callback_data="Xco16 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ يوم مالوش لازمه", callback_data="Xco17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ غبي منه فيه", callback_data="Xco18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ خير وبركه", callback_data="Xco19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ البدله", callback_data="Xco20 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع🔙", callback_data="film " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بك في قائمة الافلام الكوميدي العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco1 (\\d+)$"))
async def Xco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco2 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : وقفة رجالة
    📖 انتاج سنة : 2021
    🌎 الدولة : مصر
    🗄 تصنيف : كوميدي
    📜 قصة الفيلم:
    تدور أحداث العمل في قالب كوميدي حول مجموعة من الأصدقاء الذين يجتمعون بعد سنوات لمساعدة أحدهم في الخروج من ورطة كبيرة، وتتطوّر الأحداث فتقودهم للسفر إلى إحدى المدن الساحلية.
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco2 (\\d+)$"))
async def Xco2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco4 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : الخطة العايمة
        📖 انتاج سنة  : 2020
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        في إطار كوميدي لايت تدور الأحداث حول أحد الأشخاص يتطلع إلى سرقة أحد البنك لوجود أوراق هامة في الخزانة، فيتفق مع (جلال وياسمين) لتولي المهمة، واللذان يختاران اللصان الساذجان (حمزون وعلى الله) لتنفيذ تلك المهمة، ويبدآن في تدريبهما.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco3 (\\d+)$"))
async def Xco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco6 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بنات ثانوي
         انتاج سنة : 2020
        🌎 الدولة : مصر
        🗄 تصنيف : دراما, كوميدي, رومانسي
        📜 قصة الفيلم:
        تدور أحداث الفيلم حول فترة المراهقة، حيث تبحث خمس فتيات في مرحلة المراهقة عن ذواتهن وشخصياتهن، ليقعن في العديد من المتاعب والصعاب خلال مرحلة الدراسة الثانوية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco4 (\\d+)$"))
async def Xco4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco8 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : عفريت ترانزيت
        📖 انتاج سنة : 2020
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        يتناول العمل قصة بائع مخدرات يتعرض للعديد من المشاكل واتهامه في جريمة قتل، الأمر الذي يدفعه لمحاولة البحث عن براءته والسير في طريق التوبة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco5 (\\d+)$"))
async def Xco5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco10 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : زكي شان
        📖 انتاج سنة  : 2005
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        زكي شاب كثير المشاكل سواء مع أفراد أسرته أو في عمله، يعلم أن رب عمل والده يرغب في تعيين بودي جارد كي يحرس ابنه وابنته، ويقرر التقدم للوظيفة رغم عدم ملائمته جسديًا للوظيفة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco6 (\\d+)$"))
async def Xco6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco12 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : سمير وشهير وبهير
        📖 انتاج سنة  : 2010
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي, رومانسي
        📜 قصة الفيلم:
        ثلاثة أخوة لنفس الأب؛ ولكن لأمهات مختلفة هم  (سمير)، ويعمل دوبلير فى السينما، و (شهير) يحب الموسيقي ومعروف بعلاقاته النسائية المتعددة، (بهير) وهو ابن لأسرة أرستقراطية. نتيجة سوء تعامل مع إحدى آلآت الزمن يسافروا عبر الزمن إلى اليوم الذي قابل فيه والدهم الأمهات الثلاثة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco7 (\\d+)$"))
async def Xco7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco14 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : تصبح علي خير
        📖 انتاج سنة  : 2017
        🌎 الدولة : مصر
        🗄 تصنيف : دراما , كوميدي , رومانسي
        📜 قصة الفيلم:
        في إطار كوميدي رومانسي تشويقي، تدور قصة الفيلم في إطار مُختلف عن مهندس ناجح وثري يدعى (حسام الخديوي)، ولكنه يعاني في اﻵونة اﻷخيرة من مشاكل في حياته الطبيعية فيلجأ إلي حياة بديلة من خلال جهاز جديد يُدخله في عالم الأحلام.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco8 (\\d+)$"))
async def Xco8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco16 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بابا
        📖 انتاج سنة  : 2012
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي , رومانسي
        📜 قصة الفيلم:
        تدور أحداث الفيلم في إطار رومانسي كوميدي حيث الطبيب حازم (أحمد السقا) طبيب أمراض النساء الذي تتعلق بحبه مهندسة الديكور فريدة (درة) وعقب زواجهما يفاجأ حازم بعدم قدرته على الإنجاب فيضطر للجوء إلى عملية الحقن المهجري، فترى هل سيتمكن من تحقيق رغبتهما؟
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco9 (\\d+)$"))
async def Xco9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco18 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : جدو نحنوح
        📖 انتاج سنة  : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        مجموعة من الشباب يتوفى جدهم، وعند توزيع الميراث يكتشفون أن جدهم لم يترك أموالًا لهم، بينما ترك وصية يُطالبهم فيها بالبحث عن كنز مدفون، وبالبحث عن مكان الكنز يتضح أنه داخل مستشفى المجانين. فيخططون لدخول مستشفى المجانين سعيًا لإيجاد هذا الكنز، وهناك تحدث لهم الكثير من المفارقات الكوميدية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco10 (\\d+)$"))
async def Xco10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco20 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : سمير ابو النيل
        📖 انتاج سنة : 2013
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        في إطار كوميدي تدور أحداث الفيلم حول الشاب البخيل سمير أبو النيل (أحمد مكي) الذي يقطن بحي شعبي، ونتيجة لبخله الشديد تقع له العديد من المفارقات والمشاكل مع أهل منطقته، ويزيد من كرههم له لسوء معاملته لهم، وبين ليلة وضحاها يمرض ابن عمه حسين أبو النيل (حسين اﻹمام) ويقرر أن يترك ثروته لسمير الذي يستغل ذلك ويقوم بإنشاء قناة فضائية يناقش فيها أحواله وعلاقاته بأصدقائه وأهل منطقته.. تتوالى الأحداث في سياق كوميدي بعد إنشاء حزب سياسي يدعو له المواطنين.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco11 (\\d+)$"))
async def Xco11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco22 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : كلبي دليلي
        📖 انتاج سنة : 2013
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        تدور قصة الفيلم حول ضابط الشرطة مغاوري (سامح حسين)، الذي يعيش في صعيد مصر، ثم يُنقل فجأة إلى مارينا بالساحل الشمالي، وما عليه هناك إلا إثبات ذاته كضابط يحتذى به أمام الضباط وإشادة رئيسه بأدائه، إلى جانب ذلك يجد (مغاوري) نفسه واقعًا في حب فتاة تختلف عنه تمامًا في كل شيء.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco12 (\\d+)$"))
async def Xco12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco24 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بنات العم
        📖 انتاج سنة : 2012
        🌎 الدولة : مصر
        🗄 تصنيف : دراما, كوميدي
        📜 قصة الفيلم:
        ثلاث فتيات تربطهن علاقة عمومة يعشن مع جدتهن، يتطلعن إلى بيع القصر الذي يعشن به، فيتوجهن إلى (عزيز الهانش) ليشتري القصر، فتحاول الجدة منعهن وتحذرهن من لعنة حدثت لأجدادهن، إلا أن الفتيات لا ينصتن لها، فأصابتهن اللعنة ويتحولن إلى رجال، وطوال الأحداث تسعى الفتيات لإعادة القصر، ومحاولة فك اللعنة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco13 (\\d+)$"))
async def Xco13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco26 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : علي بابا
        📖 انتاج سنة : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : دراما، كوميدي
        📜 قصة الفيلم:
        تدور أحداث الفيلم في إطار كوميدي حول شخص انتهازي يُدعى (علي)، يسعى إلى تحقيق مصالحه الشخصية حتى ولو كانت على حساب الآخرين، وإذا به يفاجئ بوجود ابنة له (أيتن عامر) في سن العشرينات، وتبدأ من هنا المفارقات الكوميدية التي يقع فيها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco14 (\\d+)$"))
async def Xco14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco28 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : فول الصين العظيم
        📖 انتاج سنة : 2004
        🌎 الدولة : مصر
        🗄 تصنيف :  كوميدي، اكشن
        📜 قصة الفيلم:
        يدور الفيلم في إطار كوميدي حول شاب مصري يدعى (محي الشرقاوي)، يشكل كل من جده (جابر الشرقاوي) وأعمامه عصابة للتهريب، ولأنه جبان لا يستطيع مسايرتهم والعمل معهم، يذهب لوالدته وزوجها والذي يرسله للصين ليمثل مصر في مسابقة للطبخ، ليقع في العديد من المشكلات.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco15 (\\d+)$"))
async def Xco15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco30 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حسن وبقلظ
        📖 انتاج سنة : 2016
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي , رومانسي , دراما
        📜 قصة الفيلم:
        تدور أحداث الفيلم حول شقيقين ملتصقين ببعضهما البعض (علي ربيع) و(كريم فهمي)، تقع معهما العديد من المواقف الكوميدية، يتورط معهما ابن خالتهما (محمد أسامة) وفي مشاكلهما.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco16 (\\d+)$"))
async def Xco16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco32 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : الكويسين
        📖 انتاج سنة : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        مفتاح وشقيقته غزال ثنائي متخصص في النصب، يكتشف مفتاح وجود جوهرة ثمينة تدعى القرموط القرمزي في منزل عائلة الكويسين، فيقرر اختراق صفوف هذه العائلة من خلال انتحال شخصية ابنهم مظهر المفقود منذ سنوات طويلة، لكن هذه المهمة تواجه الكثير من الصعوبات رغم نجاحها في البداية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco17 (\\d+)$"))
async def Xco17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco33 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco34 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : يوم مالوش لازمة
        📖 انتاج سنة : 2015
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        اليوم هو يوم زفاف يحيى ومها ,و منذ الصباح الباكر يستعد العروسان لاستقبال هذا اليوم، لكن بمجرد أن يبدأ هذا اليوم حتى يقع العروسان طوال اليوم وفي حفل الزفاف نفسه في سلسلة طويلة لا تنتهي من المفارقات والمواقف الصعبة، وما يزيد الطين بلة هو مطاردة الفتاة المهووسة بوسي ليحيى طوال اليوم، وإصرارها الشديد أن تكون هي زوجته بدلًا من مها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco18 (\\d+)$"))
async def Xco18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco36 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : غبي منه فيه
        📖 انتاج سنة : 2004
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        يشعر سلطان باليأس من تحقيق حلمه بالزواج من حبيبته سامية التي أعطى له والدها مهلة شهر واحد كي يعد خلاله بيت الزوجية، فتعرف سامية على زوج خالتها ضبش، والذي يشركه في سرقاته لمساعدته، لكنه يوقعه في المتاعب بسبب غبائه الشديد.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco19 (\\d+)$"))
async def Xco19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco38 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : خير وبركة
        📖 انتاج سنة : 2017
        🌎 الدولة : مصر
        🗄 تصنيف : كوميديا
        📜 قصة الفيلم:
        تدور أحداث الفيلم في إطار كوميدي يتناول قصة شقيقين يحاولان البحث عن فرصة عمل، وخلال رحلة البحث يواجهان العديد من المواقف الكوميدية عندما يعملان في مهن لا يعرفان عنها شيئًا.

        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco20 (\\d+)$"))
async def Xco20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco40 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : البدلة
        📖 انتاج سنة : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي , رومانسي
        📜 قصة الفيلم:
        تدور القصة حول حمادة، ووليد اللذين ولدا في نفس اليوم فاشلين في الحياة، يقرران الذهاب إلى حفلة تنكرية، ويتنكران في زي رجال الشرطة لمقابلة زملائهم القدامى، الأمر الذي يجعل الجميع يعتقد بأنهما شرطيين حقيقيين، وتقع لهما العديد من الأحداث والمشاكل.

        """, reply_markup=keyboard)


#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^XXco1 (\\d+)$"))
async def XXco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/121", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco2 (\\d+)$"))
async def XXco2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/122", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco3 (\\d+)$"))
async def XXco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/123", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco4 (\\d+)$"))
async def XXco4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/124", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco5 (\\d+)$"))
async def XXco5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/125", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco6 (\\d+)$"))
async def XXco6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/126", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco7 (\\d+)$"))
async def XXco7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/127", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco8 (\\d+)$"))
async def XXco8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/128", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco9 (\\d+)$"))
async def XXco9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/129", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco10 (\\d+)$"))
async def XXco10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/130", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco11 (\\d+)$"))
async def XXco11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/131", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco12 (\\d+)$"))
async def XXco12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/132", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco13 (\\d+)$"))
async def XXco13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/133", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco14 (\\d+)$"))
async def XXco14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/134", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco15 (\\d+)$"))
async def XXco15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/135", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco16 (\\d+)$"))
async def XXco16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/136", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco17 (\\d+)$"))
async def XXco17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/137", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco18 (\\d+)$"))
async def XXco18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/139", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco19 (\\d+)$"))
async def XXco19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/140", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco20 (\\d+)$"))
async def XXco20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/141", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco21 (\\d+)$"))
async def XXco21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/142", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco22 (\\d+)$"))
async def XXco22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/143", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco23 (\\d+)$"))
async def XXco23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/144", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco24 (\\d+)$"))
async def XXco24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/145", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco25 (\\d+)$"))
async def XXco25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/146", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco26 (\\d+)$"))
async def XXco26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/147", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco27 (\\d+)$"))
async def XXco27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/148", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco28 (\\d+)$"))
async def XXco28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/149", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco29 (\\d+)$"))
async def XXco29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/150", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco30 (\\d+)$"))
async def XXco30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/151", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco31 (\\d+)$"))
async def XXco31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/152", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco32 (\\d+)$"))
async def XXco32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/153", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco33 (\\d+)$"))
async def XXco33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/154", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco34 (\\d+)$"))
async def XXco34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/155", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco35 (\\d+)$"))
async def XXco35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/156", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco36 (\\d+)$"))
async def XXco36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/157", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco37 (\\d+)$"))
async def XXco37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/158", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco38 (\\d+)$"))
async def XXco38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/159", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco39 (\\d+)$"))
async def XXco39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/160", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco40 (\\d+)$"))
async def XXco40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/161", reply_to_message_id=mid)


#########################################################################################
#########################################################################################
#########################         # Aflam Action #             ##########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^action (\\d+)$"))
async def action(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("حملة فرعون", callback_data="Xact1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بني ادم", callback_data="Xact2 " + str(m.from_user.id))],
        [InlineKeyboardButton("الخليه", callback_data="Xact3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حرب كرموز", callback_data="Xact4 " + str(m.from_user.id))],
        [InlineKeyboardButton("من ضهر راجل", callback_data="Xact5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("زنزانة سبعة", callback_data="Xact6 " + str(m.from_user.id))],
        [InlineKeyboardButton("خارج عن القانون", callback_data="Xact7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ولاد العم", callback_data="Xact8 " + str(m.from_user.id))],
        [InlineKeyboardButton("وش سجون", callback_data="Xact9 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("اهلا بك في قائمة الافلام الاكشن العربيه", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact1 (\\d+)$"))
async def Xact1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact2 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حملة فرعون
📖 انتاج سنة : 2019
🌎 الدولة : مصر
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تدور أحداث الفيلم في إطار تشويقي مثير حول الشاب يحيى الشهير بفرعون والذي يدير أكبر شبكة اغتيالات منظمة في مصر، ويضطر إلى التوجه إلى سوريا لتحرير أبنه المخطوف .
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact2 (\\d+)$"))
async def Xact2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact4 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بني ادم
📖 انتاج سنة : 2018
🌎 الدولة : مصر
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تدور الأحداث في إطار بوليسي تشويقي مثير حول رجل الأعمال (آدم) الذي يتهم بأعمال إجرامية، في الوقت الذي تلجأ إليه الشرطة في مهمة خطيرة، فهل الأحداث ستتطور وتجعله متورط، أم هناك جانب غامض غير معروف عنه؟.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact3 (\\d+)$"))
async def Xact3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact6 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""فيلم #الخلية | دراما , اكشن | 2017
عندما يذهب صديقه ضحية عملية إرهابية، يقسم سيف، وهو ضابط عمليات خاصة، على الثأر لصديقه، ويطلب مساعدة الضابط صابر في سبيل تحقيق ذلك.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact4 (\\d+)$"))
async def Xact4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact8 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حرب كرموز
📖 انتاج سنة : 2018
🌎 الدولة : مصر
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تتعرض فتاة للاعتداء على يد جنود إنجليز فيثأر لها ثلاثة شبان مصريين ويقومون باحتجاز أحد الجنود في مركز شرطة كرموز، الأمر الذي ستترتب عليه عواقب وخيمة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact5 (\\d+)$"))
async def Xact5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact10 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : من ضهر راجل
📖 انتاج سنة : 2015
🌎 الدولة : مصر
🗄 تصنيف : دراما، رومانسي، اكشن
📜 قصة الفيلم:
رحيم أدهم ملاكم شاب ويعيش في حارة شعبية مع والده المسن إمام المسجد، ويحب مي وينوي الزواج منها، وفور علم حِنش بما يدور بين رحيم ومي من لقاءات عن طريق طه الذي ينافس رحيم على حب مي، تتحول حياة رحيم ووالده إلى جحيم مقيم على الأرض، خاصة مع انكشاف أسرار من الماضي.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact6 (\\d+)$"))
async def Xact6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact12 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : زنزانة سبعة
📖 انتاج سنة : 2020
🌎 الدولة : مصر
🗄 تصنيف : دراما , اكشن , تشويق , اثارة
📜 قصة الفيلم:
تدور حول شاب يدعى "حربي الكومي"، يدخل السجن بعد اتهامه في إحدى القضايا, داخل السجن يلتقي "حربي" بـ"منصور العايق" ، ويحدث بينهما خلافات كثيرة في بداية الأحداث، وبعد ذلك تنشأ بينهما علاقة صداقة قوية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact7 (\\d+)$"))
async def Xact7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact14 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : خارج عن القانون
📖 انتاج سنة : 2007
🌎 الدولة : مصر
🗄 تصنيف : دراما, اكشن, اثارة وتشويق
📜 قصة الفيلم:
تدور أحداث الفيلم حول شخصية عمر (كريم عبدالعزيز). تبدأ مأساة عمر منذ أن كان طفلًا صغيرًا حيث شهد علي تبادلٍ لإطلاق النار بين والده (محمود الجندي) وقوات الشرطة ،وبالرغم من أن والده استسلم وترك سلاحه لكن يتم قنصه. ومن هنا يصبح ما تبقى من عائلته مهددًا بالهلاك ولا يجد أمامه خيارٌ غير أن يرمي نفسه في أحضان أحد حيتان تجارة المخدرات (حسن حسني) ليأخذه تحت جناحه وينشأ عمر ليجد نفسه وقد أصبح تاجرًا للمخدرات. 
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact8 (\\d+)$"))
async def Xact8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact16 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : ولاد العم
📖 انتاج سنة : 2009
🌎 الدولة : مصر
🗄 تصنيف : دراما, اكشن, اثارة وتشويق
📜 قصة الفيلم:
ضابط بالموساد مسئول عن تكوين شبكة جاسوسية لتنفيذ اغتيالات في مصر، يتزوج بفتاة مصرية دون أن يخبرها بحقيقته، ثم يهرب بها رغمًا عنها إلى إسرائيل ضاغطًا عليها بحرمانها من أولادها. فترسل المخابرات المصرية ضابطًا لكشف نوعية المعلومات التي حصل عليها وإعادة الزوجة المخدوعة للقاهرة بصحبة طفليها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact9 (\\d+)$"))
async def Xact9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact18 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : وش سجون
📖 انتاج سنة : 2014
🌎 الدولة : مصر
🗄 تصنيف : اثارة وتشويق, اكشن
📜 قصة الفيلم:
تدور الأحداث في إطار درامي شيق حول ثلاث شباب، يتقابلون داخل سجن واحد، ولكل منهم حكاية عن سبب دخوله للسجن، أولهم شاب  يُحكم عليه بالإعدام في قضية اغتصابه لفتاة من العمارة التي كان يعمل بها كبواب، والثاني جابر المتزوج من عزة والذي يدخل السجن بسببها مرتين، والثالث وليد رجل الأعمال المتزوج من نور التي تورطه في قضية شيكات بعد أن تعلم بخيانته لها وزواجه من واحدة أخرى فتحاول الانتقام منه. يتناول الفيلم تفاصيل الحياة داخل السجن، والعلاقات اﻹنسانية بين السجناء.
        """, reply_markup=keyboard)


#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^XXact1 (\\d+)$"))
async def XXact1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/162", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact2 (\\d+)$"))
async def XXact2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/163", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact3 (\\d+)$"))
async def XXact3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/164", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact4 (\\d+)$"))
async def XXact4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/165", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact5 (\\d+)$"))
async def XXact5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/166", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact6 (\\d+)$"))
async def XXact6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/167", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact7 (\\d+)$"))
async def XXact7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/168", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact8 (\\d+)$"))
async def XXact8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/169", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact9 (\\d+)$"))
async def XXact9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/170", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact10 (\\d+)$"))
async def XXact10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/171", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact11 (\\d+)$"))
async def XXact11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/172", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact12 (\\d+)$"))
async def XXact12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/173", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact13 (\\d+)$"))
async def XXact13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/174", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact14 (\\d+)$"))
async def XXact14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/175", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact15 (\\d+)$"))
async def XXact15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/176", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact16 (\\d+)$"))
async def XXact16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/177", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact17 (\\d+)$"))
async def XXact17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/178", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact18 (\\d+)$"))
async def XXact18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/179", reply_to_message_id=mid)


#########################################################################################
#########################################################################################
#########################         # Aflam Drama #             ###########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^drama (\\d+)$"))
async def drama(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ هذه ليلتي", callback_data="Xdra1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ورقة جمعية", callback_data="Xdra2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حظر تجوال", callback_data="Xdra3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ القط", callback_data="Xdra4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ خان تيولا", callback_data="Xdra5 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("اهلا بك في قائمة الافلام الدراما العربيه", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra1 (\\d+)$"))
async def Xdra1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra2 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="drama " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : هذه ليلتي
📖 انتاج سنة : 2019
🌎 الدولة : مصر
🗄 تصنيف : دراما
📜 قصة الفيلم:
تقرر (عزة) الاستمتاع بيومها، والذهاب رفقة ابنها المصاب بمتلازمة داون في مغامرة، وحينما تتجه من عشوائيات القاهرة إلى الأحياء الفخمة من أجل تناول المثلجات، تقابل العديد من المضايقات والعقبات في طريقها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra2 (\\d+)$"))
async def Xdra2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra4 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="drama " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : ورقة جمعية
📖 انتاج سنة : 2020
🌎 الدولة : مصر
🗄 تصنيف : دراما
📜 قصة الفيلم:
تتناول أحداث الفيلم في قالب درامي قصة امرأة يُطلق عليها أم عبدالله، حيث تسعى لرعاية شقيقتها وعائلتها في حارة بسيطة من خلال إدارة محل كوافير خاص بها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra3 (\\d+)$"))
async def Xdra3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra6 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="drama " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حظر تجول
📖 انتاج سنة : 2021
🌎 الدولة : مصر
🗄 تصنيف : دراما
📜 قصة الفيلم:
تدور الأحداث في خريف عام 2013 بعد قرار حظر التجوال بمصر، حيث تخرج فاتن من السجن بعد قضائها عشرين عامًا بسبب ارتكابها جريمةّ مريعة، وتجبر فاتن على قضاء ليلتها عند ابنتها ليلى والتي تعرضها لمحاكمة ثانية بحثاً عن اجابات لأسئلة مسكوت عنها. لتمر الليلة في محاولة كل منهما لتقبل الأخرى.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra4 (\\d+)$"))
async def Xdra4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra8 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="drama " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : القط
📖 انتاج سنة : 2014
🌎 الدولة : مصر
🗄 تصنيف : دراما
📜 قصة الفيلم:
يتناهى إلى سمع القط (عمرو واكد) خبر اختطاف مجموعة من الأطفال في المنطقة التي يعيش بها ، بغرض الحصول على أعضائهم الحيوية وبيعها في السوق السوداء ، وعلى إثر ذلك يقوم (القط) بقتل أحد رجال المعلم فتحي (صلاح الحنفي) ، وتخليص الفتاة التي بقت على قيد الحياة ، وبعدها ينخرط في رحلة طويلة محمومة مع غجري (عمرو فاروق) ؛ لملاحقة المعلم (فتحي) بتشجيع من أحد الرجال النافذين (فاروق الفيشاوي) .
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra5 (\\d+)$"))
async def Xdra5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra10 " + str(m.from_user.id))],
        [InlineKeyboardButton("Ⴆᥲ️ᥴk", callback_data="drama " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : خان تيولا
📖 انتاج سنة : 2020
🌎 الدولة : مصر
🗄 تصنيف : دراما, اثارة وتشويق، غموض
📜 قصة الفيلم:
تدور أحداث الفيلم في حقبة الأربعنيات خلال الحرب العالمية الثانية داخل أحد الفنادق بمدينة العالمين، الذي يملكه الفنان محمود البزاوي والذي يعيش مع أسرته المكونة من  زوجته والتي تجسد دورها الفنانة وفاء عامر ونجله الذي يقوم بدوره الفنان علي الشجيري ونجلته التي تجسدها الفنانة الشابة زهرة الحاروفي، ويصل إليهم في أحد الليالي نزيل جديد والذي يجسد دوره الفنان نضال الشافعي، ليتفاجئ بالكثير من الأشياء الغامضة داخل هذا الفندق تقلب أحداث العمل.
        """, reply_markup=keyboard)


#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^XXdra1 (\\d+)$"))
async def XXdra1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/180", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra2 (\\d+)$"))
async def XXdra2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/181", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra3 (\\d+)$"))
async def XXdra3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/182", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra4 (\\d+)$"))
async def XXdra4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/183", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra5 (\\d+)$"))
async def XXdra5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/184", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra6 (\\d+)$"))
async def XXdra6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/185", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra7 (\\d+)$"))
async def XXdra7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/186", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra8 (\\d+)$"))
async def XXdra8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/187", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra9 (\\d+)$"))
async def XXdra9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/188", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra10 (\\d+)$"))
async def XXdra10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/189", reply_to_message_id=mid)


#########################################################################################
#########################################################################################
#########################         # END Aflam AR #             ##########################
#########################################################################################
#########################################################################################


#########################################################################################
#########################################################################################
#########################         # Start Moslsl AR #          ##########################
#########################################################################################
#########################################################################################


@app.on_callback_query(filters.regex("^moslsl (\\d+)$"))
async def moslsl(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("حشمت في البيت الأبيض 📼", callback_data="Xmos1 " + str(m.from_user.id))],
        [InlineKeyboardButton("لعبة النسيان 📼", callback_data="Xmos2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ب 100 وش 📼", callback_data="Xmos3 " + str(m.from_user.id))],
        [InlineKeyboardButton("آدم 📼", callback_data="Xmos4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("توبه 📼", callback_data="toba " + str(m.from_user.id))],
        [InlineKeyboardButton("ابو العروسة 📼", callback_data="Xmos5 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة المسلسلات العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos1 (\\d+)$"))
async def Xmos1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos214 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos215 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos216 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos217 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos218 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos219 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos220 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos221 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos222 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos223 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos224 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos225 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos226 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 حشمت في البيت الأبيض\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos2 (\\d+)$"))
async def Xmos2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos229 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos230 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos231 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos232 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos233 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos234 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos235 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos236 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos237 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos238 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos239 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos240 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos241 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmos242 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmos243 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmos244 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmos245 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmos246 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmos247 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmos248 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmos249 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmos250 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="Zmos251 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="Zmos252 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="Zmos253 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="Zmos254 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="Zmos255 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="Zmos256 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="Zmos257 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="Zmos258 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 2- لعبة النسيان\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos3 (\\d+)$"))
async def Xmos3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos261 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos262 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos263 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos264 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos265 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos266 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos267 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos268 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos269 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos270 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos271 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos272 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos273 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmos274 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmos275 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmos276 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmos277 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmos278 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmos279 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmos280 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmos281 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmos282 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="Zmos283 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="Zmos284 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="Zmos285 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="Zmos286 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="Zmos287 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="Zmos288 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="Zmos289 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="Zmos290 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 3- ب 100 وش\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos4 (\\d+)$"))
async def Xmos4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos293 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos294 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos295 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos296 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos297 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos298 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos299 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos300 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos301 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos302 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos303 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos304 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos305 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmos306 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmos307 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmos308 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmos309 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmos310 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmos311 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmos312 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmos313 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmos314 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="Zmos315 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="Zmos316 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="Zmos317 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="Zmos318 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="Zmos319 " + str(m.from_user.id))], 
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="Zmos320 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="Zmos321 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="Zmos322 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 4- آدم\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos5 (\\d+)$"))
async def Xmos5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos325 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos326 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos327 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos328 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos329 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos330 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos331 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos332 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos333 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos334 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos335 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos336 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos337 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmos338 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmos339 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmos340 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmos341 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmos342 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmos343 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmos344 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmos345 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmos346 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="Zmos347 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="Zmos348 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="Zmos349 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="Zmos350 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="Zmos351 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="Zmos352 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="Zmos353 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="Zmos354 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 31", callback_data="Zmos355 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 32", callback_data="Zmos356 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 33", callback_data="Zmos357 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 34", callback_data="Zmos358 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 35", callback_data="Zmos359 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 36", callback_data="Zmos360 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 37", callback_data="Zmos361 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 38", callback_data="Zmos362 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 39", callback_data="Zmos363 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 40", callback_data="Zmos364 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 41", callback_data="Zmos365 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 42", callback_data="Zmos366 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 43", callback_data="Zmos367 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 44", callback_data="Zmos368 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 45", callback_data="Zmos369 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 46", callback_data="Zmos370 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 47", callback_data="Zmos371 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 48", callback_data="Zmos372 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 49", callback_data="Zmos373 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 50", callback_data="Zmos374 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 51", callback_data="Zmos375 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 52", callback_data="Zmos376 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 53", callback_data="Zmos377 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 54", callback_data="Zmos378 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 55", callback_data="Zmos379 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 56", callback_data="Zmos380 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 57", callback_data="Zmos381 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 58", callback_data="Zmos382 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 59", callback_data="Zmos383 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 60", callback_data="Zmos384 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 6-ابو العروسة\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^toba (\\d+)$"))
async def toba(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="toba1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="toba2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="toba3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="toba4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="toba5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="toba6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="toba7" + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="toba8 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="toba9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="toba10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="toba11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="toba12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="toba13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="toba14 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="toba15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="toba16 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="toba17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="toba18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="toba19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="toba20 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="toba21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="toba22 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="toba23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="toba24 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="toba25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="toba26 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="toba27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="toba28 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="toba29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="toba30 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 5-توبه\n√", reply_markup=keyboard)
    

## link moslsl
@app.on_callback_query(filters.regex("^Zmos214 (\\d+)$"))
async def Zmos214(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/190", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos215 (\\d+)$"))
async def Zmos215(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/191", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos216 (\\d+)$"))
async def Zmos216(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/192", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos217 (\\d+)$"))
async def Zmos217(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/193", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos218 (\\d+)$"))
async def Zmos218(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/194", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos219 (\\d+)$"))
async def Zmos219(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/195", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos220 (\\d+)$"))
async def Zmos220(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/196", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos221 (\\d+)$"))
async def Zmos221(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/197", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos222 (\\d+)$"))
async def Zmos222(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/198", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos223 (\\d+)$"))
async def Zmos223(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/200", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos224 (\\d+)$"))
async def Zmos224(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/201", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos225 (\\d+)$"))
async def Zmos225(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/202", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos226 (\\d+)$"))
async def Zmos226(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/203", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos228 (\\d+)$"))
async def Zmos228(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/205", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos229 (\\d+)$"))
async def Zmos229(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/205", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos230 (\\d+)$"))
async def Zmos230(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/206", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos231 (\\d+)$"))
async def Zmos231(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/207", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos232 (\\d+)$"))
async def Zmos232(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/208", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos233 (\\d+)$"))
async def Zmos233(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/209", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos234 (\\d+)$"))
async def Zmos234(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/210", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos235 (\\d+)$"))
async def Zmos235(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/211", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos236 (\\d+)$"))
async def Zmos236(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/212", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos237 (\\d+)$"))
async def Zmos237(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/213", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos238 (\\d+)$"))
async def Zmos238(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/214", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos239 (\\d+)$"))
async def Zmos239(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/215", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos240 (\\d+)$"))
async def Zmos240(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/216", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos241 (\\d+)$"))
async def Zmos241(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/217", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos242 (\\d+)$"))
async def Zmos242(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/218", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos243 (\\d+)$"))
async def Zmos243(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/219", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos244 (\\d+)$"))
async def Zmos244(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/220", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos245 (\\d+)$"))
async def Zmos245(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/221", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos246 (\\d+)$"))
async def Zmos246(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/222", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos247 (\\d+)$"))
async def Zmos247(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/223", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos248 (\\d+)$"))
async def Zmos248(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/224", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos249 (\\d+)$"))
async def Zmos249(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/225", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos250 (\\d+)$"))
async def Zmos250(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/226", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos251 (\\d+)$"))
async def Zmos251(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/227", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos252 (\\d+)$"))
async def Zmos252(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/228", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos253 (\\d+)$"))
async def Zmos253(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/229", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos254 (\\d+)$"))
async def Zmos254(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/230", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos255 (\\d+)$"))
async def Zmos255(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/231", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos256 (\\d+)$"))
async def Zmos256(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/232", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos257 (\\d+)$"))
async def Zmos257(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/233", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos258 (\\d+)$"))
async def Zmos258(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/234", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos261 (\\d+)$"))
async def Zmos261(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/261", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos262 (\\d+)$"))
async def Zmos262(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/262", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos263 (\\d+)$"))
async def Zmos263(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/263", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos264 (\\d+)$"))
async def Zmos264(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/264", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos265 (\\d+)$"))
async def Zmos265(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/265", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos266 (\\d+)$"))
async def Zmos266(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/266", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos267 (\\d+)$"))
async def Zmos267(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/267", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos268 (\\d+)$"))
async def Zmos268(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/268", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos269 (\\d+)$"))
async def Zmos269(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/269", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos270 (\\d+)$"))
async def Zmos270(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/270", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos271 (\\d+)$"))
async def Zmos271(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/271", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos272 (\\d+)$"))
async def Zmos272(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/272", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos273 (\\d+)$"))
async def Zmos273(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/273", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos274 (\\d+)$"))
async def Zmos274(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/274", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos275 (\\d+)$"))
async def Zmos275(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/275", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos276 (\\d+)$"))
async def Zmos276(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/276", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos277 (\\d+)$"))
async def Zmos277(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/277", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos278 (\\d+)$"))
async def Zmos278(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/278", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos279 (\\d+)$"))
async def Zmos279(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/279", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos280 (\\d+)$"))
async def Zmos280(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/280", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos281 (\\d+)$"))
async def Zmos281(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/281", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos282 (\\d+)$"))
async def Zmos282(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/282", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos283 (\\d+)$"))
async def Zmos283(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/283", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos284 (\\d+)$"))
async def Zmos284(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/284", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos285 (\\d+)$"))
async def Zmos285(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/285", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos286 (\\d+)$"))
async def Zmos286(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/286", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos287 (\\d+)$"))
async def Zmos287(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/287", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos288 (\\d+)$"))
async def Zmos288(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/288", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos289 (\\d+)$"))
async def Zmos289(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/289", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos290 (\\d+)$"))
async def Zmos290(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/290", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos293 (\\d+)$"))
async def Zmos293(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/293", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos294 (\\d+)$"))
async def Zmos294(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/294", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos295 (\\d+)$"))
async def Zmos295(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/295", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos296 (\\d+)$"))
async def Zmos296(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/296", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos297 (\\d+)$"))
async def Zmos297(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/297", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos298 (\\d+)$"))
async def Zmos298(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/298", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos299 (\\d+)$"))
async def Zmos299(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/299", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos300 (\\d+)$"))
async def Zmos300(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/300", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos301 (\\d+)$"))
async def Zmos301(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/301", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos302 (\\d+)$"))
async def Zmos302(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/302", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos303 (\\d+)$"))
async def Zmos303(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/303", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos304 (\\d+)$"))
async def Zmos304(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/304", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos305 (\\d+)$"))
async def Zmos305(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/305", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos306 (\\d+)$"))
async def Zmos306(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/306", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos307 (\\d+)$"))
async def Zmos307(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/307", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos308 (\\d+)$"))
async def Zmos308(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/308", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos309 (\\d+)$"))
async def Zmos309(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/309", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos310 (\\d+)$"))
async def Zmos310(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/310", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos311 (\\d+)$"))
async def Zmos311(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/311", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos312 (\\d+)$"))
async def Zmos312(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/312", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos313 (\\d+)$"))
async def Zmos313(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/313", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos314 (\\d+)$"))
async def Zmos314(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/314", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos315 (\\d+)$"))
async def Zmos315(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/315", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos316 (\\d+)$"))
async def Zmos316(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/316", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos317 (\\d+)$"))
async def Zmos317(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/317", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos318 (\\d+)$"))
async def Zmos318(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/318", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos319 (\\d+)$"))
async def Zmos319(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/319", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos320 (\\d+)$"))
async def Zmos320(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/320", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos321 (\\d+)$"))
async def Zmos321(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/321", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos322 (\\d+)$"))
async def Zmos322(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/322", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos325 (\\d+)$"))
async def Zmos325(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/325", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos326 (\\d+)$"))
async def Zmos326(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/326", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos327 (\\d+)$"))
async def Zmos327(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/327", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos328 (\\d+)$"))
async def Zmos328(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/328", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos329 (\\d+)$"))
async def Zmos329(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/329", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos330 (\\d+)$"))
async def Zmos330(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/330", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos331 (\\d+)$"))
async def Zmos331(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/331", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos332 (\\d+)$"))
async def Zmos332(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/332", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos333 (\\d+)$"))
async def Zmos333(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/333", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos334 (\\d+)$"))
async def Zmos334(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/334", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos335 (\\d+)$"))
async def Zmos335(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/335", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos336 (\\d+)$"))
async def Zmos336(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/336", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos337 (\\d+)$"))
async def Zmos337(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/337", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos338 (\\d+)$"))
async def Zmos338(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/338", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos339 (\\d+)$"))
async def Zmos339(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/339", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos340 (\\d+)$"))
async def Zmos340(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/340", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos341 (\\d+)$"))
async def Zmos341(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/341", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos342 (\\d+)$"))
async def Zmos342(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/342", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos343 (\\d+)$"))
async def Zmos343(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/343", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos344 (\\d+)$"))
async def Zmos344(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/344", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos345 (\\d+)$"))
async def Zmos345(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/345", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos346 (\\d+)$"))
async def Zmos346(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/346", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos347 (\\d+)$"))
async def Zmos347(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/347", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos348 (\\d+)$"))
async def Zmos348(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/348", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos349 (\\d+)$"))
async def Zmos349(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/349", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos350 (\\d+)$"))
async def Zmos350(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/350", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos351 (\\d+)$"))
async def Zmos351(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/351", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos352 (\\d+)$"))
async def Zmos352(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/352", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos353 (\\d+)$"))
async def Zmos353(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/353", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos354 (\\d+)$"))
async def Zmos354(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/354", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos355 (\\d+)$"))
async def Zmos355(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/355", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos356 (\\d+)$"))
async def Zmos356(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/356", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos357 (\\d+)$"))
async def Zmos357(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/357", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos358 (\\d+)$"))
async def Zmos358(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/358", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos359 (\\d+)$"))
async def Zmos359(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/359", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos360 (\\d+)$"))
async def Zmos360(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/360", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos361 (\\d+)$"))
async def Zmos361(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/361", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos362 (\\d+)$"))
async def Zmos362(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/362", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos363 (\\d+)$"))
async def Zmos363(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/363", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos364 (\\d+)$"))
async def Zmos364(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/364", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos365 (\\d+)$"))
async def Zmos365(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/365", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos366 (\\d+)$"))
async def Zmos366(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/366", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos367 (\\d+)$"))
async def Zmos367(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/367", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos368 (\\d+)$"))
async def Zmos368(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/368", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos369 (\\d+)$"))
async def Zmos369(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/369", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos370 (\\d+)$"))
async def Zmos370(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/370", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos371 (\\d+)$"))
async def Zmos371(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/371", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos372 (\\d+)$"))
async def Zmos372(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/372", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos373 (\\d+)$"))
async def Zmos373(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/373", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos374 (\\d+)$"))
async def Zmos374(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/374", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos375 (\\d+)$"))
async def Zmos375(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/375", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos376 (\\d+)$"))
async def Zmos376(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/376", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos377 (\\d+)$"))
async def Zmos377(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/377", reply_to_message_id=mid)

    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/381", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos382 (\\d+)$"))
async def Zmos382(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/382", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos383 (\\d+)$"))
async def Zmos383(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/383", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos384 (\\d+)$"))
async def Zmos384(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/384", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^toba1 (\\d+)$"))
async def toba1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/7", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba2 (\\d+)$"))
async def toba2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/8", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba3 (\\d+)$"))
async def toba3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/9", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba4 (\\d+)$"))
async def toba4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/10", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba5 (\\d+)$"))
async def toba5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/11", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba6 (\\d+)$"))
async def toba6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/12", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba7 (\\d+)$"))
async def toba7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/13", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba8 (\\d+)$"))
async def toba8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/14", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba9 (\\d+)$"))
async def toba9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/15", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba10 (\\d+)$"))
async def toba10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/16", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba11 (\\d+)$"))
async def toba11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/17", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba12 (\\d+)$"))
async def toba12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/18", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba13 (\\d+)$"))
async def toba13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/19", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba14 (\\d+)$"))
async def toba14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/20", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba15 (\\d+)$"))
async def toba15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/21", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba16 (\\d+)$"))
async def toba16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/22", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba17 (\\d+)$"))
async def toba17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/23", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba18 (\\d+)$"))
async def toba18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/24", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba19 (\\d+)$"))
async def toba19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/25", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba20 (\\d+)$"))
async def toba20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/26", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba21 (\\d+)$"))
async def toba21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/27", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba22 (\\d+)$"))
async def toba22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/28", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba23 (\\d+)$"))
async def toba23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/29", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba24 (\\d+)$"))
async def toba24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/30", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba25 (\\d+)$"))
async def toba25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/31", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba26 (\\d+)$"))
async def toba26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/32", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba27 (\\d+)$"))
async def toba27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/33", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba28 (\\d+)$"))
async def toba28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/34", reply_to_message_id=mid)
   
  
 
@app.on_callback_query(filters.regex("^toba29 (\\d+)$"))
async def toba29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/35", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba30 (\\d+)$"))
async def toba30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/36", reply_to_message_id=mid)
   
   
#########################################################################################
#########################################################################################
#########################         # END Moslsl AR #            ##########################
#########################################################################################
#########################################################################################


#########################################################################################
#########################################################################################
#########################         # Start msrahia AR #        ##########################
#########################################################################################
#########################################################################################


#########################################################################################
#########################################################################################
#########################         # Msrh Masr #               ##########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^msrahia (\\d+)$"))
async def msrahia(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🎭 1- افلام كرتون", callback_data="Xms1 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
        
        [InlineKeyboardButton("رجوع", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الكارتون للاطفال العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xms1 (\\d+)$"))
async def Xms1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("توم وجيري", callback_data="Xmsrh1 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبونج بوب", callback_data="Xmsrh2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طيور الجنه", callback_data="Xmsrh3 " + str(m.from_user.id))],
        [InlineKeyboardButton("افلام كرتون", callback_data="Xmsrh4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عالم كارتونيتو", callback_data="Xmsrh5 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="msrahia " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
        
    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة اجزاء افلام كرتون\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmsrh1 (\\d+)$"))
async def Xmsrh1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmsrh388 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmsrh389 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmsrh390 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmsrh391 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmsrh392 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmsrh393 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmsrh394 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmsrh395 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmsrh396 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmsrh397 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmsrh398 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmsrh399 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmsrh400 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmsrh401 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmsrh402 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmsrh403 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmsrh404 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="Xms1 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
        
    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | كرتون توم وجيري |\n√", reply_markup=keyboard)
    return


@app.on_callback_query(filters.regex("^Xmsrh2 (\\d+)$"))
async def Xmsrh2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmsrh406 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmsrh407 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmsrh408 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmsrh409 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmsrh410 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmsrh411 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmsrh412 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmsrh413 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmsrh414 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmsrh415 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmsrh416 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmsrh417 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmsrh418 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmsrh419 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="Xms1 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | كرتون اسبونج بوب |\n√", reply_markup=keyboard)
    return


@app.on_callback_query(filters.regex("^Xmsrh3 (\\d+)$"))
async def Xmsrh3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmsrh421 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmsrh422 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmsrh423 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmsrh424 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmsrh425 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmsrh426 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmsrh427 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmsrh428 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmsrh429 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmsrh430 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmsrh431 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmsrh432 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmsrh433 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmsrh434 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmsrh435 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmsrh436 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmsrh437 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmsrh438 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmsrh439 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmsrh440 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmsrh441 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmsrh442 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="Xms1 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
        
    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | اغاني طيور الجنه 😍 |\n√", reply_markup=keyboard)
    return


@app.on_callback_query(filters.regex("^Xmsrh4 (\\d+)$"))
async def Xmsrh4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("ربانزل", callback_data="Zmsrh444 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سمبا 1", callback_data="Zmsrh445 " + str(m.from_user.id))],
        [InlineKeyboardButton("سمبا 2", callback_data="Zmsrh446 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ملكه الجليد", callback_data="Zmsrh447 " + str(m.from_user.id))],
        [InlineKeyboardButton("الامير والضفضع", callback_data="Zmsrh448 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطباخ الفار", callback_data="Zmsrh449 " + str(m.from_user.id))],
        [InlineKeyboardButton("طرزان", callback_data="Zmsrh450 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السمكه نينو", callback_data="Zmsrh451 " + str(m.from_user.id))],
        [InlineKeyboardButton("تنه ورنه", callback_data="Zmsrh452 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بيتر بان", callback_data="Zmsrh453 " + str(m.from_user.id))],
        [InlineKeyboardButton("الابطال المقنعون", callback_data="Zmsrh454 " + str(m.from_user.id))] +
        [InlineKeyboardButton("علاء الدين", callback_data="Zmsrh455 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكلب بولت", callback_data="Zmsrh456 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="Xms1 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
        
    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | افلام كرتون |\n√", reply_markup=keyboard)
    return


@app.on_callback_query(filters.regex("^Xmsrh5 (\\d+)$"))
async def Xmsrh5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("السنافر 1", callback_data="Zmsrh467 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السنافر 2", callback_data="Zmsrh468 " + str(m.from_user.id))],
        [InlineKeyboardButton("السنافر 3", callback_data="Zmsrh469 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السنافر 4", callback_data="Zmsrh470 " + str(m.from_user.id))],
        [InlineKeyboardButton("السنافر 5", callback_data="Zmsrh471 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ السنافر 6", callback_data="Zmsrh472 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ السنافر 7", callback_data="Zmsrh473 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmsrh474 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmsrh475 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmsrh476 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmsrh477 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmsrh478 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmsrh479 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmsrh480 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmsrh481 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmsrh482 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmsrh483 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmsrh484 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmsrh485 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmsrh486 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmsrh487 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmsrh488 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع", callback_data="Xms1 " + str(m.from_user.id))],
        [InlineKeyboardButton("𓆩 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐑𝐀𝐙𝐘 𓆪", url=f"https://t.me/CH_CRAZ")],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
        
    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | حلقات متنوعه من كارتوننيتو |\n√", reply_markup=keyboard)
    return


# link msrh
@app.on_callback_query(filters.regex("^Zmsrh388 (\\d+)$"))
async def Zmsrh388(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/61", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh389 (\\d+)$"))
async def Zmsrh389(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/63", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh390 (\\d+)$"))
async def Zmsrh390(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/66", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh391 (\\d+)$"))
async def Zmsrh391(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/67", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh392 (\\d+)$"))
async def Zmsrh392(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/69", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh393 (\\d+)$"))
async def Zmsrh393(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/74", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh394 (\\d+)$"))
async def Zmsrh394(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/76", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh395 (\\d+)$"))
async def Zmsrh395(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/77", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh396 (\\d+)$"))
async def Zmsrh396(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/79", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh397 (\\d+)$"))
async def Zmsrh397(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/78", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh398 (\\d+)$"))
async def Zmsrh398(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/106", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh399 (\\d+)$"))
async def Zmsrh399(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/108", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh400 (\\d+)$"))
async def Zmsrh400(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/111", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh401 (\\d+)$"))
async def Zmsrh401(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/113", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh402 (\\d+)$"))
async def Zmsrh402(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/116", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh403 (\\d+)$"))
async def Zmsrh403(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/119", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh404 (\\d+)$"))
async def Zmsrh404(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/120", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh406 (\\d+)$"))
async def Zmsrh406(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/121", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh407 (\\d+)$"))
async def Zmsrh407(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/122", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh408 (\\d+)$"))
async def Zmsrh408(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/123", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh409 (\\d+)$"))
async def Zmsrh409(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/124", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh410 (\\d+)$"))
async def Zmsrh410(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/125", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh411 (\\d+)$"))
async def Zmsrh411(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/126", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh412 (\\d+)$"))
async def Zmsrh412(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/127", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh413 (\\d+)$"))
async def Zmsrh413(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/128", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh414 (\\d+)$"))
async def Zmsrh414(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/129", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh415 (\\d+)$"))
async def Zmsrh415(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/129", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh416 (\\d+)$"))
async def Zmsrh416(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/130", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh417 (\\d+)$"))
async def Zmsrh417(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/131", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh418 (\\d+)$"))
async def Zmsrh418(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/136", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh419 (\\d+)$"))
async def Zmsrh419(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/137", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh421 (\\d+)$"))
async def Zmsrh421(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/191", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh422 (\\d+)$"))
async def Zmsrh422(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/192", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh423 (\\d+)$"))
async def Zmsrh423(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/193", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh424 (\\d+)$"))
async def Zmsrh424(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/194", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh425 (\\d+)$"))
async def Zmsrh425(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/195", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh426 (\\d+)$"))
async def Zmsrh426(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/196", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh427 (\\d+)$"))
async def Zmsrh427(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/197", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh428 (\\d+)$"))
async def Zmsrh428(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/198", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh429 (\\d+)$"))
async def Zmsrh429(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/199", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh430 (\\d+)$"))
async def Zmsrh430(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/200", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh431 (\\d+)$"))
async def Zmsrh431(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/201", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh432 (\\d+)$"))
async def Zmsrh432(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/202", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh433 (\\d+)$"))
async def Zmsrh433(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/203", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh434 (\\d+)$"))
async def Zmsrh434(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/204", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh435 (\\d+)$"))
async def Zmsrh435(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/205", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh436 (\\d+)$"))
async def Zmsrh436(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/206", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh437 (\\d+)$"))
async def Zmsrh437(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/207", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh438 (\\d+)$"))
async def Zmsrh438(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/208", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh439 (\\d+)$"))
async def Zmsrh439(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/209", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh440 (\\d+)$"))
async def Zmsrh440(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/210", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh441 (\\d+)$"))
async def Zmsrh441(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/211", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh442 (\\d+)$"))
async def Zmsrh442(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/212", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh444 (\\d+)$"))
async def Zmsrh444(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/141", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh445 (\\d+)$"))
async def Zmsrh445(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/143", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh446 (\\d+)$"))
async def Zmsrh446(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/147", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh447 (\\d+)$"))
async def Zmsrh447(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/154", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh448 (\\d+)$"))
async def Zmsrh448(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/159", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh449 (\\d+)$"))
async def Zmsrh449(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/165", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh450 (\\d+)$"))
async def Zmsrh450(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/167", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh451 (\\d+)$"))
async def Zmsrh451(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/173", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh452 (\\d+)$"))
async def Zmsrh452(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/190", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh453 (\\d+)$"))
async def Zmsrh453(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/178", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh454 (\\d+)$"))
async def Zmsrh454(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/183", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh455 (\\d+)$"))
async def Zmsrh455(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/186", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh456 (\\d+)$"))
async def Zmsrh456(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/188", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh467 (\\d+)$"))
async def Zmsrh467(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/356", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh468 (\\d+)$"))
async def Zmsrh468(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/357", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh469 (\\d+)$"))
async def Zmsrh469(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/358", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh470 (\\d+)$"))
async def Zmsrh470(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/359", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh471 (\\d+)$"))
async def Zmsrh471(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/360", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh472 (\\d+)$"))
async def Zmsrh472(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/361", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh473 (\\d+)$"))
async def Zmsrh473(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/362", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh474 (\\d+)$"))
async def Zmsrh474(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/363", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh475 (\\d+)$"))
async def Zmsrh475(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/364", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh476 (\\d+)$"))
async def Zmsrh476(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/365", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh477 (\\d+)$"))
async def Zmsrh477(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/366", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh478 (\\d+)$"))
async def Zmsrh478(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/367", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh479 (\\d+)$"))
async def Zmsrh479(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/368", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh480 (\\d+)$"))
async def Zmsrh480(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/369", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh481 (\\d+)$"))
async def Zmsrh481(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/370", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh482 (\\d+)$"))
async def Zmsrh482(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/371", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh483 (\\d+)$"))
async def Zmsrh483(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/372", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh484 (\\d+)$"))
async def Zmsrh484(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/273", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh485 (\\d+)$"))
async def Zmsrh485(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/374", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh486 (\\d+)$"))
async def Zmsrh486(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/375", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh487 (\\d+)$"))
async def Zmsrh487(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/376", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh488 (\\d+)$"))
async def Zmsrh488(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/377", reply_to_message_id=mid)

#########################################################################################
#########################################################################################
#########################         # END masrahia AR #          ##########################
#########################################################################################
#########################################################################################
