"""
data types -> int, float, str, list, dict, set, tuple, collection

collections -> standard kutubxonalardi bir qismi xisoblanadi va ularga Counter(element lardi sanidi ichida borlardu),
    namedtuple () bunda bir nechta elementlarni bir joyda saqlashga yordam beradi

collections -> ozini strukturasi bilan saqlaydigan malumot turlari

itertools -> takroriy amallardi bajarishda yordam beradi (count, cycle, repeat)

os -> file va kataloklar bilan ishlashda yordam beradi

muttble -> list, dict, set,

immutuble -> touple, str, bytes

tuple -> database dan joy olmaydi, va unga malumotlar qoshib bolmaydi

list -> royxatlar bilan ishlashda qulay\

dict -> esa lugatlar bilan ishlashda qulay

set -> tartibsiz malumotlar tuzilmasi

comprehension -> list, dict, set  -> mana shulardi tez va oson yaratsa boladi

hashable -> int, string, float

unhashable -> list, dict, set

function -> nomga ega va bir neshta ammalardi bajaradigan code

lambda -> 1 ta argument yokida ifoda bilan ishlaydi

scope -> Global scope -> dasturda barcha funksiyalar va klasslar uchun mavjud
                         bo'lgan o'zgaruvchilarni belgilaydigan xudud

dataclasses -> bu sinflarni tez va oson yaratish uchun ishlatiladigan moduldur



OOP principles
    Encapsulation
    Abstraction
    Inheritance
    Polymorphism
    Modul
    Class

slots -> xotira sarflarini kamaytiradi

dunder methods (magic methods) -> __init__, __str__, __repr__

Threads -> bir vaqt ozida bitta ish bajariladi va shu ish qilinganidan kein boshqa ishga otiladi

multiprocessing -> bir vaqt ozida kop ish xarakatini bajarish

Async -> bir vaqtda 2 3 ta funksya bajarishda yordam beradi

concurrency/parallelism -> bir vaqtda bir neshta vazifaalardi bajarishda yordam beradi


Gil global inteperet lock -> ichki qisimdi boshqaradi -> 1 taa python code ni boshqaradi

logging -> bu pythonda qilinilayotgan xatoliklarni korish imkonini beradi
    info, warning, debug, error, critical,

Postgres
subquery -> bu SQL so'rovlarida boshqa so'rov ichida yozilgan so'rovdir, select ikki marta ishlata oladi
group by ->  so'rov natijalarini guruhlash uchun ishlatiladigan buyruqdir (agregat funktsiyalarni -> sum, count, avg)
all join -> inner join, left join, right join, full join, cross join, self join
    inner join -> mos yozuvlardi birlashtiradi
    left join -> barcha yozuvlarni va ikkinchi jadvaldagi mos yozuvlarni qaytaradi
    right join -> barcha yozuvlarni va birinchi jadvaldagi mos yozuvlarni qaytaradi
    full join -> ikkala table di toliq birlashtiradi
    cross join -> jadvalning har bir yozuvini bir-biriga birlashtiradi
    self join -> jadvalni o'ziga o'zini birlashtirishidir

index -> qidiruv tezligi, filtrlash uchun kerak boladi

transaction -> bir qator operatsiyalarni birlashtirish uchun ishlatiladigan
atomic transaction -> bu ma'lumotlar bazasida amalga oshiriladigan operatsiyalar to'plami,
view -> so'rov (SQL query) natijasini aks ettiruvchi virtual jadval
trigger -> malumotlar qoshilgan da yokida ozgartirilganda avtomatik tarzda ishga tushadigan code
partition -> kota kota jadvalllardi kichikroq bolimlarga bolish
pl/pgsql -> operatsiyalarini avtomatlashtirish, murakkab hisob-kitoblar, shartli mantiq va tsikllar kabi dasturlash
            elementlarini amalga oshirish uchun mo'ljallangan.



cashing -> redis, rambitmq

ttl -> kompyuter tarmoqlarida va ma'lumotlar bazalarida ma'lumot yoki resursning amal qilish muddati
expire time ->  ma'lum bir obyekt yoki ma'lumotning amal qilish muddati,
memory use in python -> zarur bo'lgan xotira miqdorini anglatadi. Xotira foydalanishi dasturlarning samaradorligi va tezligini ta'sir qiladi,
                        shuningdek, xatolarga (masalan, "memory error") olib kelishi mumkin.
garbage collector ->  xotira obyektlarini aniqlaydi va ularni o'chiradi.
reference count ->  xotira boshqarish mexanizmi bo'lib, u obyektlarning xotirada qancha marta foydalanilayotganini kuzatadi.

web protocol ->  internet orqali ma'lumotlarni uzatish va aloqa qilish uchun belgilangan qoidalar to'plamidir.
    http, websocket, graphql

http methods -> HTTP protokoli orqali serverga qanday turdagi so'rovlar yuborilishini belgilovchi operatsiyalar.

how works web

websocket -> real korish

graphql ->  Api di bir turi va Api dan kuchli ishlaydi

cron -> Unix va Unix-ga o'xshash operatsion tizimlarda (masalan, Linux) vaqtni belgilash va avtomatik ravishda vazifalarni bajarish uchun ishlatiladigan dastur.

Big O notation -> algoritmlarning samaradorligini baholash uchun ishlatiladigan matematik asbob

sorts (merge, quick, bubble, insert, select)
    merge -> bu bo'linish va egallash (divide and conquer) usuliga asoslangan bir tartiblash algoritmi
    quick -> o'ng va chap qismga ajratadi va har bir qismni rekursiv ravishda tartiblaydi.
    insert ->  bu oddiy tartiblash algoritmi, u elementlarni tartiblangan qismga joylashtirish jarayonini simulyatsiya qiladi
    select -> Selection sort tartiblash algoritmi har bir o'tishda eng kichik (yoki eng katta) elementni topadi va uni tartiblangan qismga qo'shadi
    bubble ->  U qo'shni elementlarni taqqoslaydi va tartibsiz bo'lsa, ularni almashtiradi.

search (linear, binary)
    linear ->  elementlarni birma-bir tekshiradi.
    binary -> ma'lumotlar to'plamidagi elementlarni tartiblangan holda qidiradi


context manager (custom) -> with open bilan qollaniladi
generator ->  bu funktsiya, u yield kalit so'zidan foydalanib, qiymatlarni ishlab chiqaradi va qaytaradi.
decorator -> bu funktsiyani qabul qiladigan va yangi funktsiya qaytaradigan funktsiya.
iterator ->  bu ob'ekt, u qator elementlarni ketma-ketlikda ishlatishga imkon beradi.

ci/cd, kanban
celery, redis, rabbitmq, elasticsearch

design patterns -> dasturiy ta'minotni yaratishda yuzaga keladigan umumiy muammolarni hal qilish uchun taklif etilgan tavsiyalar yoki andozalar.

OOP/SOLID/YAGNI/KISS

PUT -> ma'lum bir resursni yangilash yoki o'rnatish uchun ishlatiladi

Patch -> resursning bir qismini yangilash uchun ishlatiladi

SCRUM -> agile metodologiyasi doirasida ishlov berish va loyiha boshqarish uchun qo'llaniladigan bir uslubdir.

Sql/NoSql -> asosi farqi sql da strukturali boladi va jadval shaklida saqlaydi va vertikal olchaydi, malumotlar foreign key orqali boglanadi
nosql da esa json, mongoDb, ustunli -> Cassandra kabi boladi va garizantal olchaydi, malumotlar cheklangan boladi

List comprehension — bu Python dasturlash tilida ro'yxatlarni samarali va qisqa usulda yaratish imkonini beruvchi sintaksis. Bu usul yordamida ro'yxatni yaratishda, ma'lumotlarni filtrlash yoki o'zgartirish jarayonlarini bir joyda bajarish mumkin.

"""

"""

data types -> int, tuple, str, float, dict, list, set, collection
collections -> bir vaqtni ozida bir neshta elemntni bir joyda saqlay oladi namedtuple
itertools -> for, while bn ishlanadgan kutubxonalar -> count, reapeat va boshqalar 
os -> operatsion system
list -> buni dictdan farqi royxatlar bilan ishlay oladi, tuple dan farqi esa append qilib qosha oladi
dict -> listdan farqi buni lugatlar bn ishlaydi, key value
set -> set()
comprehension -> 1 qator da yozish 
function -> name bera olamiz va uni ichida bir neshta ammalardi bajara olamiz 
lambda -> 1 qatorda yoziladi va 1 ta ifodani aks etiradi  

scope -> Global name
dataclasses -> yozishni osonlashtradi 
OOP principles -> module, view, Encapsulation, Abstraction, Inheritance, Polymorphism
slots -> sloots dunder method bor shu orqali yoziladi 
dunder methods -> __ ikta chiziqcha bilan yoziladigan method lar 
Threads -> bir oqimda bir tekis ketadigan ishlar
multiprocessing -> Threads lardan tashkil topgan boladi
Async -> code larni tezlashtirish uchun ishlatiladgan kutubxone
concurrency ->
parallelism -> pythonda yooq va bola olmaydi bari bir orasda qanchadir vaqt qolib ketadi

Gil global inteperet lock
logging -> errors, debug, warning, info, critical

Postgres -> database
subquery -> select 2 marta ishatiladi 
group by -> avagrate function lar sum, max, min
all join
    inner join -> mos yozuvlardi birlashtiradi
    self join -> ozga ozi
    left join -> ikkinchi jadval togri kelishi 
    right join -> birinchi jadval togri kelishi 
    cross join -> jadvalning har bir yozuvini bir-biriga birlashtiradi
    full join -> Farq yochasga boglanish 
    
transaction
atomic transaction
view
trigger
partition
pl/pgsql



cashing -> redis, rambitmq
ttl ->  
expire time -> biror bir ishga ketkan vaqt  

memory use in python 

garbage collector 

reference count 

web protocol -> http, websockt kradi 
http methods -> get, put, putch, delete, post
how works web -> ?
websocket -> real time 
graphql -> api dan kuchli bolgan tizim va qulaylik jihati bor
cron -> bu backup olib qolish degani

Big O notation
sorts (merge, quick, bubble, insert, select)
search (linear, binary)
        linear ->  elementlarni birma-bir tekshiradi.
        binary -> ma'lumotlar to'plamidagi elementlarni tartiblangan holda qidiradi

context manager (custom) -> with bn ishlatiladi
generator-> yield kalit sozi bilan boglanadi 
decorator -> funksyaga boglanadi va funksya qaytaradi 
iterator -> __iter__, __next__  doonder method lari orqali ishlaydi 
ci/cd -> server bn ishlash (ci da test korinadi, cd da esa serverga borib keladi)
kanban -> 
celery, redis, rabbitmq, elasticsearch

design patterns -> dizayn


PUT -> ma'lum bir resursni yangilash yoki o'rnatish uchun ishlatiladi

Patch -> resursning bir qismini yangilash uchun ishlatiladi

SCRUM -> agile metodologiyasi doirasida ishlov berish va loyiha boshqarish uchun qo'llaniladigan bir uslubdir.

Sql/NoSql -> asosi farqi sql da strukturali boladi va jadval shaklida saqlaydi va vertikal olchaydi, malumotlar foreign key orqali boglanadi
nosql da esa json, mongoDb, ustunli -> Cassandra kabi boladi va garizantal olchaydi, malumotlar cheklangan boladi


"""

# todo KORISH KERAK
"""
Korilishi kerak bogan narsalar 
dataclasses

"""