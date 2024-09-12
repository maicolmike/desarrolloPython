<template>
    <div class="container">
        <div class="row">
            <div class="col text-start">
                <h2>Editar libros</h2>
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
                                    <input type="text" placeholder="Título" name="title" class="form-control">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="description" class="col-sm-2 col-form-label">Descripción</label>
                                <div class="col-sm-6">
                                    <textarea name="description" class="form-control" placeholder="Descripción" rows="3">
                                    </textarea>
                                </div>
                            </div>
                            <br>

                            <div class="rows">
                                <div class="col text-start">
                                    <b-button type="submit" variant="primary">Editar</b-button>
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
export default {

}
</script>

<style lang="css" scoped>
/* Estilos específicos del componente */
</style>