import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Data Penduduk.xlsx'
df = pd.read_excel(file_path)

grouped = df.groupby(['Pendidikan Terakhir', 'Jenis Kelamin']).size().unstack(fill_value=0)

grouped.plot(kind='bar', figsize=(10,6))

plt.title('Jumlah Warga Berdasarkan Pendidikan Terakhir dan Jenis Kelamin')
plt.xlabel('Pendidikan Terakhir')
plt.ylabel('Jumlah Marga')
plt.xticks(rotation=45)
plt.legend(title='Jumlah Kelamin')
plt.tight_layout()
plt.show()
