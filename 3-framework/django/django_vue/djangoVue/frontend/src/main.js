//import { createApp } from 'vue'
//import App from './App.vue'

//createApp(App).mount('#app')
// main.js (o main.ts para TypeScript)
import { createApp } from 'vue';
import App from './App.vue';

// Import Bootstrap and BootstrapVue CSS files
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';

// Opcional: Importar los iconos de Bootstrap
//import 'bootstrap-icons/font/bootstrap-icons.css';

// Importar BootstrapVue 3
import BootstrapVue3 from 'bootstrap-vue-3';

const app = createApp(App);

// Usar BootstrapVue 3
app.use(BootstrapVue3);

app.mount('#app');

