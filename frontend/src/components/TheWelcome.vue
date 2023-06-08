<template>
  <h2>
    Overzicht van werknemers bij DataDolphins
  </h2>
  <v-btn @click=fetchData()>
    Vis alle dolfijnen uit het water
  </v-btn>
   <table v-if="users.length>0" class="flex-table">
      <thead>
        <tr>
          <th>Achternaam</th>
          <th>Voornaam</th>
          <th>Bedrijf</th>
          <th>Functie</th>
          <th>Verwijder</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id_gebruiker">
          <td>{{ user.voornaam }}</td>
          <td>{{ user.achternaam }}</td>
          <td>{{ user.bedrijf.bedrijfs_naam }}</td>
          <td>{{ user.functie.functie }}</td>
          <td>  
            <v-btn @click=deleteData(user.achternaam)>
              Dolfijn loslaten
            </v-btn>
          </td>
        </tr>
      </tbody>
    </table>
</template>

<script setup lang="ts">
import { ref } from 'vue'

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

const deleteData = (lastname: string) => {
      fetch(`http://localhost:8000/api/gebruikers/${lastname}`, {
            method: 'DELETE'
      })
        .then(_ => {
            fetchData()
          })
          .catch(error => {
            console.error('Error:', error);
          })
}

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




