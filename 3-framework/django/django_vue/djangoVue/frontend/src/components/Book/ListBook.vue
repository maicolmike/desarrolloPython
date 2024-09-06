<template lang="">
    <div class="container">
      <div class="row">
        <div class="col text-left">
          <h2>Listado de libros</h2>

          <div class="col-md-12">

          <b-table striped hover :items="books" :fields="fields">

          </b-table>

          </div>

        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data () {
    return {
      fields: [
        { key: 'title', label: 'Título' },
        { key: 'description', label: 'Descripción' },
        { key: 'action', label: 'Action' }
      ],
      books: []
    }
  },
   
  };
  </script>
  
  <style lang="css" scoped>
  /* Aquí puedes agregar estilos específicos del componente */
  </style>
  