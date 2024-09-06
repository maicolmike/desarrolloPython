<template>
  <!-- Contenedor principal de la aplicación -->
  <div id="app">
    <!-- Imagen del logo de Vue, con una ruta relativa a la carpeta de assets -->
   <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    
    <!-- Componente HelloWorld, se le pasa una propiedad (msg) con un mensaje -->
     <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->

    <!-- Botones creados con BootstrapVue -->
    <div>
      <!-- Botón por defecto -->
      <b-button>Button</b-button>

      <!-- Botón con variante de estilo 'danger' (rojo) -->
      <b-button variant="danger">Button</b-button>

      <!-- Botón con variante de estilo 'success' (verde) -->
      <b-button variant="success">Button</b-button>

      <!-- Botón con estilo de contorno y color primario (azul) -->
      <b-button variant="outline-primary">Button</b-button>
    </div>

    <!-- Aquí se renderizarán los componentes según la ruta actual definida en el router -->
    <router-view></router-view>
  </div>
</template>

<script>
/* Importa el componente HelloWorld desde el archivo correspondiente */
//import HelloWorld from './components/HelloWorld.vue';

export default {
  /* Nombre del componente raíz de la aplicación */
  name: 'App',

  /* Componentes que estarán disponibles en este componente */
  components: {
    //HelloWorld  // Se registra el componente HelloWorld para usarlo en este template
  }
};
</script>

<style>
/* Estilos aplicados al contenedor principal de la aplicación */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;  /* Fuentes a utilizar */
  -webkit-font-smoothing: antialiased;  /* Mejora el renderizado de fuentes en WebKit */
  -moz-osx-font-smoothing: grayscale;   /* Mejora el renderizado de fuentes en macOS */
  text-align: center;  /* Centra el contenido dentro del contenedor */
  color: #2c3e50;  /* Color del texto */
  margin-top: 60px;  /* Añade un margen superior de 60px */
}
</style>
