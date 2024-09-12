// Importamos los módulos necesarios de 'vue-router'
import { createRouter, createWebHistory } from 'vue-router';

// Importamos los componentes que se usarán como vistas en las rutas
import HelloWorld from '@/components/HelloWorld.vue';
import ListBook from '@/components/Book/ListBook.vue';
import EditBook from '@/components/Book/EditBook.vue';

// Definición de las rutas de la aplicación
// Cada objeto en el array 'routes' define una ruta particular
const routes = [
  {
    // Ruta raíz ('/') que carga el componente 'HelloWorld'
    path: '/',  // La URL que el navegador debe coincidir
    name: 'HelloWorld',  // Nombre de la ruta (útil para navegación programática)
    component: HelloWorld  // Componente que se renderizará cuando se acceda a esta ruta
  },
  {
    // Ruta '/books' que carga el componente 'ListBook'
    path: '/books',  // La URL para acceder a la lista de libros
    name: 'ListBook',  // Nombre de la ruta
    component: ListBook  // Componente que se renderiza en esta ruta
  },
  {
    // Ruta '/books/edit' que edita los libros
    path: '/books/:bookId/edit',  // La URL para acceder a la edicion de libros
    name: 'EditBook',  // Nombre de la ruta
    component: EditBook  // Componente que se renderiza en esta ruta
  }
  
];

// Crear una instancia del router con el historial de navegación HTML5
// 'createWebHistory()' habilita la navegación usando el API de historial del navegador
const router = createRouter({
  history: createWebHistory(),  // Configura el modo de historial web en lugar de hash mode ('#')
  routes  // Define las rutas que creamos arriba
});

// Exportamos la instancia del router para que pueda ser utilizada en la aplicación principal
export default router;
