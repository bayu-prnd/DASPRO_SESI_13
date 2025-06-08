import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Data Penduduk.xlsx'
df = pd.read_exel(file_path)

def kategori_penghasilan(penghasilan):
    if penghasilan < 2500000:
        return 'sangat rendah'
    elif penghasilan < 5000000:
        return 'rendah'
    elif penghasilan <10000000:
        return 'menengah'
    else :
        return 'sangat tinggi'
    
df['Kategori Penghasilan'] = df ['Penghasilan Per_Bulan'].apply(kategori_penghasilan)

kategori_counts = ['Kategori_Penghasilan'].value_counts()

plt.figure(figsize=(8,6))
plt.pie(
    kategori_counts,
    labels=kategori_counts.index,
    autopact='%1.1f%%',
    startangle=140,
    colors=plt.cm.Paired.colors
    
)
plt.title('Distribusi Kategori Penghasilan Warga')
plt.axis('equal')
plt.tight_layout()
plt.show()