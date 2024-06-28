image bg blck = "images/blck.png"

define e = Character("Detektif")
define s = Character("Saksi")
define b = Character("Bos")
define w = Character("Kolega")

define char_pos = Position(xalign=0.14, yalign=0.7)

init python:
    # Node class to store data and the next node reference
    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next_node = next_node

    # LinkedList class to manage nodes
    class LinkedList:
        def __init__(self):
            self.head = None

        def add(self, data):
            if not self.head:
                self.head = Node(data)
            else:
                current = self.head
                while current.next_node:
                    current = current.next_node
                current.next_node = Node(data)

        def get(self, index):
            current = self.head
            count = 0
            while current:
                if count == index:
                    return current.data
                count += 1
                current = current.next_node
            return None

        def length(self):
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next_node
            return count

    story_bubbles = LinkedList()

$ story_bubbles.add("interogasi_saksi1")
$ story_bubbles.add("interogasi_saksi2")
$ story_bubbles.add("interogasi_saksi3")
$ story_bubbles.add("tkp1")
$ story_bubbles.add("tkp2")
$ story_bubbles.add("tkp3")
$ story_bubbles.add("tkp_detail1")
$ story_bubbles.add("tkp_detail2")
$ story_bubbles.add("periksa_tas")
$ story_bubbles.add("periksa_tong")
$ story_bubbles.add("telusuri_tkp")
$ story_bubbles.add("lapor_bos")
$ story_bubbles.add("kembali_kantor")
$ story_bubbles.add("analisis_rambut")
$ story_bubbles.add("telusuri_jejak")
$ story_bubbles.add("cari_tersangka")
$ story_bubbles.add("periksa_rumah")
$ story_bubbles.add("tahan_tersangka")
$ story_bubbles.add("istirahat")
$ story_bubbles.add("ending_sukses")
$ story_bubbles.add("ending_gagal")
$ story_bubbles.add("ending_tidak_jelas")
$ story_bubbles.add("ending_kabur")
$ story_bubbles.add("ending_salah_tangkap")
$ story_bubbles.add("kejanggalan")
$ story_bubbles.add("kesalahan")

label start:
    $ current_node = 0
    scene bg office

    show detective at char_pos
    e "Hari ini aku menerima sebuah kasus pembunuhan yang rumit. Aku harus berhati-hati dalam mengambil keputusan."
    hide detective

    menu:
        "Interogasi saksi":
            $ current_node = 0
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Cari petunjuk di TKP":
            $ current_node = 3
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

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
            $ current_node = 1
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Cari petunjuk di TKP":
            $ current_node = 3
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

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
            $ current_node = 2
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Cari petunjuk di TKP":
            $ current_node = 4
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

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
            $ current_node = 5
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label tkp1:
    scene bg tkp1
    show detective at char_pos

    e "Ini adalah tempat kejadian perkara. Aku harus mencari petunjuk di sini."
    e "Ada bekas kaki di tanah dan sebuah topi merah."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            $ current_node = 6
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Interogasi saksi lagi":
            $ current_node = 0
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label tkp2:
    scene bg tkp2
    show detective at char_pos

    e "Aku kembali ke TKP untuk mencari petunjuk lebih lanjut."
    e "Ada sebuah tas besar yang tertinggal di sini."
    hide detective

    menu:
        "Periksa isi tas":
            $ current_node = 8
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Interogasi saksi lagi":
            $ current_node = 1
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label tkp3:
    scene bg tkp3
    show detective at char_pos

    e "Aku kembali ke TKP untuk mencari petunjuk lebih lanjut."
    e "Ada bekas darah di tanah, dan ada tong sampah di dekat sini."
    hide detective

    menu:
        "Periksa tong sampah":
            $ current_node = 9
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Interogasi saksi lagi":
            $ current_node = 2
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label tkp_detail1:
    scene bg crime_scene
    show detective at char_pos

    e "Aku menemukan sebuah topi merah dan bekas kaki di tanah. Mungkin ini petunjuk penting."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            $ current_node = 10
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Interogasi saksi lagi":
            $ current_node = 0
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label tkp_detail2:
    scene bg crime_scene
    show detective at char_pos

    e "Aku menemukan sebuah tas besar yang mungkin berisi sesuatu yang penting."
    hide detective

    menu:
        "Periksa isi tas":
            $ current_node = 8
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Interogasi saksi lagi":
            $ current_node = 1
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label periksa_tas:
    scene bg crime_scene
    show detective at char_pos

    e "Di dalam tas ini aku menemukan sebuah senjata api. Mungkin ini senjata pembunuhan."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            $ current_node = 5
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Interogasi saksi lagi":
            $ current_node = 2
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label periksa_tong:
    scene bg crime_scene
    show detective at char_pos

    e "Di dalam tong sampah ini aku menemukan beberapa barang bukti yang mungkin terkait dengan kasus ini."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            $ current_node = 5
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Interogasi saksi lagi":
            $ current_node = 2
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 11
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label telusuri_tkp:
    scene bg crime_scene
    show detective at char_pos

    e "Aku terus mencari di TKP dan menemukan lebih banyak petunjuk."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            $ current_node = 14
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Interogasi saksi lagi":
            $ current_node = 1
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 13
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label lapor_bos:
    scene bg office
    show boss at char_pos

    b "Apa yang sudah kamu temukan sejauh ini?"
    hide boss
    show detective at char_pos

    e "Aku menemukan beberapa petunjuk penting, tetapi kita perlu waktu lebih banyak untuk mengungkap ini."
    hide detective

    menu:
        "Kembali bekerja":
            $ current_node = 14
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Istirahat":
            $ current_node = 20
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label kembali_kantor:
    scene bg office
    show detective at char_pos

    e "Aku kembali ke kantor untuk menganalisis petunjuk yang telah ditemukan."
    hide detective

    menu:
        "Analisis rambut":
            $ current_node = 15
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Telusuri jejak":
            $ current_node = 16
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 13
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label analisis_rambut:
    scene bg lab
    show detective at char_pos

    e "Analisis rambut ini menunjukkan bahwa ini milik tersangka yang pernah terlibat kasus serupa sebelumnya."
    hide detective

    menu:
        "Cari tersangka":
            $ current_node = 17
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 13
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label telusuri_jejak:
    scene bg street
    show detective at char_pos

    e "Jejak kaki ini mengarah ke sebuah rumah di dekat sini."
    hide detective

    menu:
        "Periksa rumah tersebut":
            $ current_node = 18
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 13
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Jejak tersangka menghilang":
            $ current_node = 24
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label cari_tersangka:
    scene bg street
    show detective at char_pos

    e "Aku menemukan tersangka berdasarkan petunjuk yang ada. Ini harus segera ditindaklanjuti."
    hide detective

    menu:
        "Tahan tersangka":
            $ current_node = 19
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 13
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label periksa_rumah:
    scene bg crime_scene
    show detective at char_pos

    e "Di dalam rumah ini, aku menemukan lebih banyak bukti yang mengarah ke tersangka utama."
    hide detective

    menu:
        "Tahan tersangka":
            $ current_node = 19
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 13
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label tahan_tersangka:
    scene bg jail
    show detective at char_pos

    e "Dengan semua bukti yang ada, aku berhasil menahan tersangka utama."
    hide detective

    menu:
        "Kasus selesai":
            $ current_node = 21
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Ada masalah":
            $ current_node = 22
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Kembali ke kantor":
            $ current_node = 27
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label istirahat:
    scene bg lounge
    show detective at char_pos

    e "Aku butuh istirahat sejenak sebelum melanjutkan investigasi."
    hide detective

    menu:
        "Kembali bekerja":
            $ current_node = 14
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Lapor ke bos":
            $ current_node = 13
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label ending_sukses:
    scene bg office
    show detective at char_pos

    e "Kasus ini akhirnya berhasil dipecahkan. Tersangka sudah ditahan, dan keadilan telah ditegakkan."
    hide detective

    return

label ending_gagal:
    scene bg office
    show detective at char_pos

    e "Kasus ini tidak bisa diselesaikan. Ada terlalu banyak bukti yang tidak cukup kuat."
    hide detective

    return

label ending_tidak_jelas:
    scene bg office
    show detective at char_pos

    e "Kasus ini masih belum jelas. Banyak pertanyaan yang belum terjawab."
    hide detective

    return

label ending_kabur:
    scene bg office
    show detective at char_pos

    e "Tersangka berhasil kabur. Aku harus mengejar dan menangkapnya."
    hide detective

    return

label ending_salah_tangkap:
    scene bg office
    show detective at char_pos

    e "Ternyata aku salah tangkap. Orang yang kutahan bukan pelakunya."
    hide detective

    return

label kejanggalan:
    scene bg office
    show detective at char_pos

    e "Terlalu banyak kejanggalan dalam kasus ini"
    hide detective

    menu:
        "Sepertinya kasus ini tidak akan terpecahkan dalam waktu dekat":
            $ current_node = 23
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Coba lihat lagi semua bukti yang ada":
            $ current_node = 14
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Tanyakan lagi ke saksi":
            $ current_node = 2
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Analisis lagi barang bukti":
            $ current_node = 15
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

label kesalahan:
    scene bg office
    show detective at char_pos

    e "Ada beberapa kesalahan dalam penyelidikan ini."
    hide detective

    menu:
        "Perbaiki kesalahan dan lanjutkan penyelidikan":
            $ current_node = 14
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)
        "Laporkan ke bos dan evaluasi ulang":
            $ current_node = 13
            if story_bubbles.get(current_node):
                jump expression story_bubbles.get(current_node)

return
