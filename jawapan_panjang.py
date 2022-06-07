import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_TANYA = "Sekiranya anda ada pertanyaan sila message danial untuk menjawap soalan yan rumit "
R_DANIALINFO = "Danial ialah seorang budak yang minat pengaturcaraan"
R_BOTINFO = "saya adalah satu D.bot "
R_DANIALBUAT = "besar kemungkinan danial sekarang tengah buat hw or just buat hobby"
R_FUNTIONBOT ="fungsi utama aku untuk jawap kau ah "
R_BOTJAWAP = "tengah jawap soalan kau lah , takkan ah memasak"
R_SIAPABOT = "Aku bot lah , fungsi utama aku untuk jawap soalan dan cakap dengan kau. "
R_HOWBOT = "Danial tengok yt and belajar coding and basic funtion , adalah sikit dia copy and paste"
R_BETULKA = "betulah ! tapi ada ah sikit dia belajar dekat yt and copy "
R_CANTIKKAH = "eeeeeey tq awak"



#^jawapan untuk soalan yang bot tak tau nak jawap
def unknown():
    response = ["???????????? ",
                "mmmmmmmmmm tak faham",
                "tak faham",
                "maaf, saya tak faham"][
        random.randrange(4)]
    return response