<template>
  <div class="container">
    <div class="row">
      <div class="col text-start">
        <h2>Listado de libros</h2>
        <div class="col-md-12">
          <!-- Definir la tabla con slots y campos -->
          <b-table striped hover :items="books" :fields="fields">
            
            <!-- Slot para las acciones de cada fila -->
            <template v-slot:cell(action)="data">
              <!-- Agregar en style margin-right para dar margen a la derecha -->
              <b-button size="sm" variant="primary" style="margin-right: 10px;" :to="{ name:'EditBook', params: {bookId: data.item.id} }">
                Editar
              </b-button>
              <b-button size="sm" variant="danger" :to="{ name:'DeleteBook', params: {bookId: data.item.id} }">
                Eliminar
              </b-button>
            </template>

          </b-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      fields: [
        { key: 'title', label: 'Título' },
        { key: 'description', label: 'Descripción' },
        { key: 'action', label: 'Acciones' }
      ],
      books: []
    }
  },
  methods: {
    getBooks () {
      const path = 'http://localhost:8000/api/v1.0/books/'
      axios.get(path)
        .then((response) => {
          this.books = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getBooks()
  }
}
</script>

<style lang="css" scoped>
/* Estilos específicos del componente */
</style>
