<template>
  <div>
    <h2>
      Dolfijner uit de oceaan toevoegen
    </h2>
    <v-text-field
      v-model="lastName"
      label="achternaam"
      placeholder="dolfijntje"
      type="lastname"
    ></v-text-field>
    <v-text-field
      v-model="firstName"
      label="voornaam"
      placeholder="skippy"
      type="firtname"
    ></v-text-field>
    <v-select
      v-model="func"
      label="Functie"
      :items="functions"
    ></v-select>
    <v-select
      v-model="company"
      label="Bedrijf"
      :items="companies"
    ></v-select>
    <v-btn @click="postData">
      Toevoegen
    </v-btn>
    {{ }}
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'

interface Functie {
  id_functie: number
  functie: string
}

interface Bedrijf {
  id_bedrijf: number
  bedrijfs_naam: string 
}

interface User {
  id_gebruiker: number
  achternaam: string
  voornaam: string
  id_functie: string
  id_bedrijf: string
  ts_create: Date
  functie: Functie
  bedrijf: Bedrijf
}

const users  = ref<User[]>([])

const fetchData = () => {
      fetch('http://localhost:8000/api/gebruikers/relations?skip=0&limit=1000')
        .then(response => response.json())
        .then((data: User[]) => {
          users.value = data;
        })
        .catch(error => {
          console.error('Error:', error);
        })
}

const postData = () => {
      fetch(`http://localhost:8000/api/gebruikers/new`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          voornaam: firstName.value,
          achternaam: lastName.value,
          id_functie: id_func.value,
          id_bedrijf: id_company.value,
        }),
      })
        .then(response => response.json())
        .then((data: User[]) => {
          users.value = data;
        })
        .catch(error => {
          console.error('Error:', error);
        })
}

const companies = computed(() => {
  const companyNames = users.value.map(user => user.bedrijf.bedrijfs_naam)
  return [...new Set(companyNames)]
})
const functions = computed(() => {
  const functionNames = users.value.map(user => user.functie.functie)
  return [...new Set(functionNames)]
})
const lastName = ref('')
const firstName = ref('')

const func = ref('')
const company = ref('')

const id_func = computed(() => {
    const id_func_names = users.value
    .filter(user => user.functie.functie === func.value)
    .map(user => user.functie.id_functie);

    return id_func_names.length > 0 ? id_func_names[0] : null;
})
const id_company = computed(() => {
    const id_company_names = users.value
    .filter(user => user.bedrijf.bedrijfs_naam === company.value)
    .map(user => user.bedrijf.id_bedrijf);

    return id_company_names.length > 0 ? id_company_names[0] : null;
})


onMounted(fetchData)

</script>

<style>
.flex-table {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.flex-table thead {
  flex: 0 0 auto;
}

.flex-table tbody {
  flex: 1 1 auto;
  overflow-y: auto;
}

.flex-table th,
.flex-table td {
  width: 33.33%; /* Equal width for each column */
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}
</style>




