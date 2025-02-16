import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyarrow as pa

# Lue Titanic data Excel-tiedostosta
file_path = "C:\\Users\\othma\\Desktop\\Koulu\\Data Analysis and Visualisation\\Titanic Data.xlsx"
titanic_data = pd.read_excel(file_path)

# Näytä pääotsikko
st.title("Titanic Data Analysis")

# Näytä data taulukkomuodossa
st.write(titanic_data)

# Muuta 'Ticket'-sarake merkkijonoksi ennen dataframeen syöttämistä
titanic_data['Ticket'] = titanic_data['Ticket'].astype(str)

# Lataa pyarrow-taulukko
table = pa.Table.from_pandas(titanic_data)

# Ikäjakauman visualisointi
st.write("Titanicin ikäjakauma:")
fig, ax = plt.subplots(figsize=(10,6))
sns.histplot(titanic_data['Age'].dropna(), kde=True, bins=20, color='skyblue', ax=ax)
ax.set_title('Ikäjakauma Titanic-matkustajilla', fontsize=16)
ax.set_xlabel('Ikä', fontsize=12)
ax.set_ylabel('Frequenttisuus', fontsize=12)
st.pyplot(fig)

# Sukupuolen jakauma
st.write("Titanicin sukupuolen jakauma:")
gender_count = titanic_data['Sex'].value_counts()
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(x=gender_count.index, y=gender_count.values, palette="pastel", ax=ax)
ax.set_title('Sukupuolen jakauma', fontsize=16)
ax.set_xlabel('Sukupuoli', fontsize=12)
ax.set_ylabel('Määrä', fontsize=12)
st.pyplot(fig)

# Selite: Matkustajaluokka
st.write("Titanicin matkustajaluokan jakauma:")
class_count = titanic_data['Pclass'].value_counts()
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(x=class_count.index, y=class_count.values, palette="muted", ax=ax)
ax.set_title('Matkustajaluokan jakauma', fontsize=16)
ax.set_xlabel('Matkustajaluokka', fontsize=12)
ax.set_ylabel('Määrä', fontsize=12)
st.pyplot(fig)

# Selite: Selviytyminen
st.write("Titanicin selviytyneiden jakauma:")
survival_count = titanic_data['Survived'].value_counts()
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(x=survival_count.index, y=survival_count.values, palette="coolwarm", ax=ax)
ax.set_title('Selviytyminen Titanicissa', fontsize=16)
ax.set_xlabel('Selviytyminen (0=Ei, 1=Kyllä)', fontsize=12)
ax.set_ylabel('Määrä', fontsize=12)
st.pyplot(fig)

# Interaktiivinen ikävalitsin
selected_age = st.slider('Valitse ikä', min_value=0, max_value=80, value=30)
st.write(f'Valitsit iän: {selected_age}')

# Interaktiivinen sukupuolivalitsin
selected_gender = st.selectbox("Valitse sukupuoli", ["male", "female"])
filtered_data = titanic_data[titanic_data['Sex'] == selected_gender]
st.write(f"Data {selected_gender} matkustajista")
st.dataframe(filtered_data)

# Interaktiivinen matkustajaluokka valitsin
selected_class = st.selectbox("Valitse matkustajaluokka", [1, 2, 3])
class_data = titanic_data[titanic_data['Pclass'] == selected_class]
st.write(f"Data matkustajaluokassa {selected_class}")
st.dataframe(class_data)

# Kaikkien matkustajien selviäminen valitsimella
selected_survival = st.selectbox("Valitse selviytymisstatus", [0, 1])
survival_data = titanic_data[titanic_data['Survived'] == selected_survival]
st.write(f"Data selviytyneistä: {selected_survival}")
st.dataframe(survival_data)

# Muuta 'Ticket'-sarake merkkijonoksi ennen dataframeen syöttämistä
titanic_data['Ticket'] = titanic_data['Ticket'].astype(str)

# Yritä konvertoida Arrow-taulukoksi
table = pa.Table.from_pandas(titanic_data)