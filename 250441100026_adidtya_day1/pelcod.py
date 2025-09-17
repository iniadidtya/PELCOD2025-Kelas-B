# Tugas Pelcod Kelas B

nilai_tugas = 85
nilai_uts = 75
nilai_uas = 90

bobot_tugas = 0.30
bobot_uts = 0.30
bobot_uas = 0.40

nilai_akhir_tugas = nilai_tugas * bobot_tugas
nilai_akhir_uts = nilai_uts * bobot_uts
nilai_akhir_uas = nilai_uas * bobot_uas

total_nilai_akhir = nilai_akhir_tugas + nilai_akhir_uts + nilai_akhir_uas

print(f"--- Nilai yang  diperoleh ---\n"
      f"Nilai Tugas : {nilai_tugas}\n"
      f"Nilai UTS   : {nilai_uts}\n"
      f"Nilai UAS   : {nilai_uas}\n\n"
      f"Nilai akhir dari Tugas (30%) : {nilai_akhir_tugas}\n"
      f"Nilai akhir dari UTS (30%)   : {nilai_akhir_uts}\n"
      f"Nilai akhir dari UAS (40%)   : {nilai_akhir_uas}\n\n"
      f"Total Nilai Akhir Kamu : {total_nilai_akhir}")
