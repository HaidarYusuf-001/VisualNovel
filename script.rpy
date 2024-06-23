image bg blck = "images/blck.png"

define e = Character("Detektif")
define s = Character("Saksi")
define b = Character("Bos")
define w = Character("Kolega")

define char_pos = Position(xalign=0.14, yalign=0.7)

init python:
    from Node import LinkedList
    choices = LinkedList()

label start:
    scene bg office

    show detective at char_pos
    e "Hari ini aku menerima sebuah kasus pembunuhan yang rumit. Aku harus berhati-hati dalam mengambil keputusan."
    hide detective

    menu:
        "Interogasi saksi":
            $ choices.add("Interogasi saksi")
            jump interogasi_saksi1
        "Cari petunjuk di TKP":
            $ choices.add("Cari petunjuk di TKP")
            jump tkp1

label interogasi_saksi1:
    scene bg interrogation

    show detective at char_pos
    e "Baiklah, aku akan mulai dengan menginterogasi saksi pertama."
    hide detective
    show witness1 at char_pos
    s "Saya melihat seseorang berlari dari tempat kejadian dengan membawa tas besar."
    hide witness1
    show detective at char_pos
    e "Bisakah Anda memberikan deskripsi lebih lanjut?"
    hide detective
    show witness1 at char_pos
    s "Dia tinggi, memakai jaket hitam dan topi merah."
    hide witness1

    menu:
        "Interogasi saksi kedua":
            $ choices.add("Interogasi saksi kedua")
            jump interogasi_saksi2
        "Cari petunjuk di TKP":
            $ choices.add("Cari petunjuk di TKP")
            jump tkp1
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label interogasi_saksi2:
    scene bg interrogation

    show detective at char_pos
    e "Sekarang aku akan menginterogasi saksi kedua."
    hide detective
    show witness2 at char_pos
    s "Saya mendengar suara tembakan dari dalam rumah itu."
    hide witness2
    show detective at char_pos
    e "Apakah Anda melihat siapa yang keluar setelahnya?"
    hide detective
    show witness2 at char_pos
    s "Tidak, saya hanya mendengar suara itu."
    hide witness2

    menu:
        "Interogasi saksi ketiga":
            $ choices.add("Interogasi saksi ketiga")
            jump interogasi_saksi3
        "Cari petunjuk di TKP":
            $ choices.add("Cari petunjuk di TKP")
            jump tkp2
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label interogasi_saksi3:
    scene bg interrogation

    show detective at char_pos
    e "Sekarang aku akan menginterogasi saksi ketiga."
    hide detective
    show witness3 at char_pos
    s "Saya melihat seseorang membuang sesuatu ke tong sampah di dekat situ."
    hide witness3
    show detective at char_pos
    e "Apakah Anda tahu apa yang dibuangnya?"
    hide detective
    show witness3 at char_pos
    s "Tidak, saya tidak melihatnya dengan jelas."
    hide witness3

    menu:
        "Cari petunjuk di TKP":
            $ choices.add("Cari petunjuk di TKP")
            jump tkp3
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label tkp1:
    scene bg tkp1
    show detective at char_pos

    e "Ini adalah tempat kejadian perkara. Aku harus mencari petunjuk di sini."
    e "Ada bekas kaki di tanah dan sebuah topi merah."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            $ choices.add("Periksa lebih lanjut di TKP")
            jump tkp_detail1
        "Interogasi saksi lagi":
            $ choices.add("Interogasi saksi lagi")
            jump interogasi_saksi1
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label tkp2:
    scene bg tkp2
    show detective at char_pos

    e "Aku kembali ke TKP untuk mencari petunjuk lebih lanjut."
    e "Ada sebuah tas besar yang tertinggal di sini."
    hide detective

    menu:
        "Periksa isi tas":
            $ choices.add("Periksa isi tas")
            jump periksa_tas
        "Interogasi saksi lagi":
            $ choices.add("Interogasi saksi lagi")
            jump interogasi_saksi2
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label tkp3:
    scene bg tkp3
    show detective at char_pos

    e "Aku kembali ke TKP untuk mencari petunjuk lebih lanjut."
    e "Ada bekas darah di tanah, dan ada tong sampah di dekat sini."
    hide detective

    menu:
        "Periksa tong sampah":
            $ choices.add("Periksa tong sampah")
            jump periksa_tong
        "Interogasi saksi lagi":
            $ choices.add("Interogasi saksi lagi")
            jump interogasi_saksi3
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label tkp_detail1:
    scene bg crime_scene
    show detective at char_pos

    e "Aku menemukan sebuah topi merah dan bekas kaki di tanah. Mungkin ini petunjuk penting."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            $ choices.add("Periksa lebih lanjut di TKP")
            jump tkp_detail2
        "Interogasi saksi lagi":
            $ choices.add("Interogasi saksi lagi")
            jump interogasi_saksi1
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label tkp_detail2:
    scene bg crime_scene
    show detective at char_pos

    e "Aku menemukan beberapa rambut di topi ini. Ini mungkin bisa dianalisis di lab."
    hide detective

    menu:
        "Kembali ke kantor":
            $ choices.add("Kembali ke kantor")
            jump kantor
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label periksa_tas:
    scene bg crime_scene
    show detective at char_pos

    e "Aku membuka tas dan menemukan beberapa alat yang mungkin digunakan dalam kejahatan ini."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            $ choices.add("Periksa lebih lanjut di TKP")
            jump tkp_detail3
        "Interogasi saksi lagi":
            $ choices.add("Interogasi saksi lagi")
            jump interogasi_saksi2
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label periksa_tong:
    scene bg tong_sampah
    show detective at char_pos

    e "Aku menemukan senjata api di dalam tong sampah ini. Ini mungkin senjata yang digunakan."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            $ choices.add("Periksa lebih lanjut di TKP")
            jump tkp_detail3
        "Interogasi saksi lagi":
            $ choices.add("Interogasi saksi lagi")
            jump interogasi_saksi3
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label tkp_detail3:
    scene bg crime_scene
    show detective at char_pos

    e "Aku menemukan beberapa jejak penting yang bisa membantu menyelesaikan kasus ini."
    hide detective

    menu:
        "Kembali ke kantor":
            $ choices.add("Kembali ke kantor")
            jump kantor
        "Lapor ke bos":
            $ choices.add("Lapor ke bos")
            jump lapor_bos

label lapor_bos:
    scene bg office

    show detective at char_pos
    e "Aku harus melaporkan apa yang kutemukan kepada bos."
    hide detective
    show boss at char_pos
    b "Apa yang sudah kamu temukan sejauh ini?"
    hide boss

    menu:
        "Laporkan tentang saksi":
            $ choices.add("Laporkan tentang saksi")
            jump lapor_saksi
        "Laporkan tentang TKP":
            $ choices.add("Laporkan tentang TKP")
            jump lapor_tkp

label lapor_saksi:
    scene bg office

    show detective at char_pos
    e "Para saksi memberikan beberapa informasi penting yang perlu kita tindak lanjuti."
    hide detective
    show boss at char_pos
    b "Baik, lanjutkan pekerjaanmu dan pastikan kita mendapatkan semua bukti yang diperlukan."
    hide boss

    menu:
        "Kembali ke TKP":
            $ choices.add("Kembali ke TKP")
            jump tkp1
        "Interogasi saksi lagi":
            $ choices.add("Interogasi saksi lagi")
            jump interogasi_saksi1
        "Kembali ke kantor":
            $ choices.add("Kembali ke kantor")
            jump kantor

label lapor_tkp:
    scene bg office

    show detective at char_pos
    e "TKP memberikan banyak petunjuk yang perlu kita analisis lebih lanjut."
    hide detective
    show boss at char_pos
    b "Bagus, pastikan semua bukti dikumpulkan dan dianalisis dengan teliti."
    hide boss

    menu:
        "Kembali ke TKP":
            $ choices.add("Kembali ke TKP")
            jump tkp1
        "Interogasi saksi lagi":
            $ choices.add("Interogasi saksi lagi")
            jump interogasi_saksi1
        "Kembali ke kantor":
            $ choices.add("Kembali ke kantor")
            jump kantor

label kantor:
    scene bg office
    show detective at char_pos

    e "Aku sudah punya beberapa petunjuk sekarang. Saatnya menganalisis dan melaporkan."

    e "Kasus ini sepertinya akan terpecahkan dalam waktu singkat."

    # Tamat permainan
    return
