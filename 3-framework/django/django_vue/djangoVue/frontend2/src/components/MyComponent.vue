<template>
    <div>
      <h2>{{ title }}</h2>
      <p>{{ message }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MyComponent',
    data() {
      return {
        title: 'Hola desde MyComponent',
        message: 'Este es un componente en Vue 3.'
      }
    }
  }
  </script>
  
  <style scoped>
  h2 {
    color: blue;
  }
  </style>
  