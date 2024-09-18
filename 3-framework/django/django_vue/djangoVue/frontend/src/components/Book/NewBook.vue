<template>
    <div class="container">
        <div class="row">
            <div class="col text-start">
                <h2>Nuevo libro</h2>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">
                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Título</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Título" name="title" class="form-control" v-model.trim="form.title">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="description" class="col-sm-2 col-form-label">Descripción</label>
                                <div class="col-sm-6">
                                    <textarea name="description" class="form-control" placeholder="Descripción" rows="3" v-model.trim="form.description">
                                    </textarea>
                                </div>
                            </div>
                            <br>

                            <div class="rows">
                                <div class="col text-start">
                                    <b-button type="submit" variant="primary">Crear</b-button>
                                    <b-button type="submit" variant="danger" class="btn-large-space" :to="{ name: 'ListBook' }">Cancelar</b-button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        
    </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'
export default {
    data () {
        return {
            form: {
                title: '',
                description:''
            }
        }
    },
    methods: {
    onSubmit (evt) {
      evt.preventDefault()
      const path = 'http://localhost:8000/api/v1.0/books/'

        axios.post(path, this.form).then((response) => {

        this.form.title = response.data.title
        this.form.description = response.data.description

        //alert("Libro actualizado exitosamente")
        swal("Libro creado existosamente!", "", "success")
        })
        .catch((error) => {
            swal("Libro no ha sido creado existosamente!", "", error)
        })
    },
 
  },
  created() {
    
  }

}
</script>

<style lang="css" scoped>
/* Estilos específicos del componente */
</style>