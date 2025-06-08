import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Data Penduduk.xlsx'
df = pd.read_exel(file_path)

hitung_profesi = df['Profesi'].value_counts()

plt.figure(gigsize=(8,6))
plt.pie(
    hitung_profesi,
    labels = hitung_profesi.indeks,
    autopct = '%1.1f%%',
    startangle = 140,
    colors = plt.cm.Set3.colors
)

plt.title('Distributin Profesi Warga Desa Cibodas')
plt.axis('equal')
plt.tight_layout()
plt.show()