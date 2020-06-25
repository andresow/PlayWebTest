<template>
  <div style="margin-top: -15px">
    <div style="height: 95vh; margin-bottom: -25px">
      <div class="mask flex-center">
        <div class="container">
          <mdb-row>
            <mdb-col md="5" class="mx-auto white z-depth-1 py-2 px-2">
              <mdb-card-body>
                <section class="demo-section">
                  <h4>Bienvenido a Playtherapy</h4>
                  <section>
                    <form  @submit="onSubmit">
                      <p class="h4 text-center mb-4">Inicio de Sesión</p>
                      <label 
                        for="username" 
                        class="black-text">Usuario
                      </label>
                      <input 
                        name="username" 
                        type="text" 
                        id="username" 
                        class="form-control"
                        placeholder="Usuario"
                        v-model.trim="form.username" 
                        />
                      <br/>
                      <label 
                        for="password" 
                        class="black-text">Contraseña
                      </label>
                      <input 
                        name="password" 
                        type="password" 
                        id="password" 
                        class="form-control"
                        placeholder="Contraseña"
                        v-model.trim="form.password" 
                        />
                      <div class="text-center mt-4">
                        <button  
                          class="btn btn-info white-text">Iniciar de Sesión
                        </button>
                        <button  
                          class="btn btn-light black-text">Cancelar
                        </button>
                      </div>                              
                    </form>
                  </section>
                </section>
              </mdb-card-body>
            </mdb-col>
          </mdb-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import swal from 'sweetalert'
  import { 
    animateOnScroll, 
    mdbCardBody,
    mdbCol,  
    mdbInput, 
    mdbRow,   
  } from 'mdbvue';

  export default {
    name: 'Login',
    components: {
      mdbCardBody,
      mdbCol,  
      mdbInput, 
      mdbRow,  
    },
    data() {
      return {
        form: {
 
              },
        showModal: false,
        guests: 4
      };
    },
    directives: {
      animateOnScroll
    }, 
    methods: {
      
            onSubmit(event){
                event.preventDefault()

                const path = 'http://localhost:8000/auth/jwt/create/'
                const pathToken = 'http://localhost:8000/auth/users/me/'

                axios.post(path, this.form).then((response)=>{

                this.form.username = response.data.username
                this.form.password = response.data.password

                localStorage.setItem('refresh', response.data.refresh);
                localStorage.setItem('access', response.data.access);
                
                axios.get(pathToken, 
                { headers: {"Authorization" : `Bearer ${localStorage.getItem('access')}`} }) .then((response) =>{
                    swal("Bienvenido a Playtherapy.", "", "success");
                })
                .catch((error)=>{
                     swal("Error en el servidor", "", "error");
                })

            })
            .catch((error)=>{
                    swal("Error en su usuario o contraseña.", "", "error")
                })
            }  

    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  a {
    color: #42b983;
  }
</style>



