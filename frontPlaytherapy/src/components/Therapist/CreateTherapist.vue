<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Registrar terapeuta</strong></h4>      
                </mdb-row>
                <hr />   
                <section class="demo-section"> 
                    <section>
                        <form class="needs-validation" novalidate @submit="checkForm">
                            <div class="col-md-12 mb-6">
                                <label for="typeUser">Profesional</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.typeUser" 
                                        placeholder="Tipo de profesional" 
                                        required>
                                    <option value="Terapeuta ocupacional">Terapeuta ocupacional</option>
                                    <option value="Fisioterapeuta">Fisioterapeuta</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el tipo de profesional a cargo.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="id_type">Tipo de identificación</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.identification" 
                                        placeholder="Tipo de identificación" 
                                        required>
                                    <option value="Cédula de ciudadanía">Cédula de ciudadanía</option>
                                    <option value="Cédula de extranjería">Cédula de extranjería</option>
                                    <option value="Número de pasaporte">Número de pasaporte</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el tipo de identificación.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="username">Número de identificación</label>
                                <input type="text" 
                                    class="form-control" 
                                    name="username" 
                                    placeholder="Número de identificación" 
                                    v-model.trim="form.username" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el número de identificación.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="name">Nombre</label>
                                <input type="text" 
                                    class="form-control" 
                                    name="name" 
                                    placeholder="Nombre" 
                                    v-model.trim="form.name" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el nombre.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="lastname">Apellido</label>
                                <input type="text" 
                                    class="form-control" 
                                    name="lastname" 
                                    placeholder="Apellido" 
                                    v-model.trim="form.lastname" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el apellido.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="genre">Género</label>
                                <select class="browser-default custom-select" 
                                        placeholder="Sexo" 
                                        v-model.trim="form.genre" 
                                        required>
                                    <option value="1">Femenino</option>
                                    <option value="2">Masculino</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el género.
                                </div>
                            </div>              
                            <div class="col-md-12 mb-6">
                                <label for="email">Correo electrónico</label>
                                <input type="text" 
                                        class="form-control" 
                                        name="email" 
                                        placeholder="Correo electrónico" 
                                        v-model.trim="form.email" 
                                        required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el correo electrónico.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="password">Contraseña</label>
                                <input type="password" 
                                    class="form-control" 
                                    name="password" 
                                    placeholder="Contraseña" 
                                    minlength="8" 
                                    v-model.trim="form.password" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese la contraseña de mínimo 8 dígitos.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="password">Confirmar contraseña</label>
                                <input type="password" 
                                    class="form-control" 
                                    name="confirmPassword" 
                                    placeholder="Confirmar contraseña" 
                                    minlength="8" 
                                    v-model.trim="form.password" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese nuevamente la contraseña.
                                </div>
                            </div>
                            <div class="text-center mt-4">
                                <mdb-btn color="info" type="submit" variant="success">Registrar</mdb-btn>
                                <a href="/home" class="btn btn-light black-text">Cancelar</a>
                            </div>
                        </form>
                    </section>
                </section>
            </mdb-container>
        </main>  
    </div>          
</template>
<script>
    import axios from 'axios';
    import swal from 'sweetalert'
    import { mdbBtn, 
            mdbRow, 
            mdbInput,
            mdbContainer 
            } from "mdbvue";
    import Navigation from '@/components/Navigation/Navigation';

    export default {
        name: "InputsPage",
        components: {
            mdbBtn,
            mdbRow,
            mdbInput,
            mdbContainer,
            Navigation,
        },
        data(){
            return {
                form: {
                    name: ''
                }
            }
        },
        methods: {
            onSubmit(event){
                event.preventDefault()
                const pathCreateUser= 'http://localhost:8000/auth/users/'                
                const pathCreateToken = 'http://localhost:8000/auth/jwt/create/'
                const pathAccessToken = 'http://localhost:8000/auth/users/me/'
                const pathTherapist = 'http://localhost:8000/api/v1.0/therapists/all-profiles'

                axios.post(pathCreateUser, this.form).then((response)=>{
                    localStorage.setItem('password',this.form.password);
                    this.form.username = response.data.username
                    this.form.password = response.data.password
                    this.form.email = response.data.email  
                    this.form.password = localStorage.getItem('password')
                    axios.post(pathCreateToken, this.form).then((response2)=>{
                    this.form.username = response.data.username
                    this.form.password = localStorage.getItem('password');
                    localStorage.setItem('therapistToken',response2.data.access);
                    var postData = {
                            user: this.form.username,
                            typeIdentification: this.form.identification,
                            identification: this.form.username,
                            name: this.form.name,
                            lastname: this.form.lastname,
                            genre: this.form.genre,
                            typeUser:  this.form.typeUser
                    };
                    axios.get(pathAccessToken,
                    { headers: {"Authorization" : `Bearer ${localStorage.getItem('therapistToken')}`} }) .then((response2) =>{
                        axios.post(pathTherapist,postData, {
                        headers: {"Authorization" : `Bearer ${localStorage.getItem('therapistToken')}`} }).then((response3)=>{
                            this.form.identification = response3.data.typeIdentification
                            this.form.username = response3.data.identification
                            this.form.name = response3.data.name 
                            this.form.lastname = response3.data.lastname
                            this.form.genre = response3.data.genre  
                            this.form.typeUser = response3.data.typeUser  
                            swal( postData.typeUser +" creado exitosamente.", "", "success");
                    }).catch((error)=>{
                            swal("No se ha podido crear el "+ postData.typeUser , "", "error")
                        })
                    })
                 })                   
                    
            })              
        },
            checkForm(event) {
            event.target.classList.add('was-validated');
            this.onSubmit(event);

            },              
        },
        created(){
        }    
    }
</script>

<style scoped>
    .demo-section {
        align-items: center;
        display: flex;
        justify-content: center;
        padding: 20px 0;
    }
    .demo-section > section {
        border: 1px solid #e0e0e0;
        padding: 15px;
        width: 80%;
    }
    .demo-section > h4 {
        font-weight: bold;
        margin-bottom: 20px;
    }
    .demo-title {
        color: #9e9e9e;
        font-weight: 700;
        margin-bottom: 0;
        padding-left: 15px;
    }
    h2 {
        font-weight: normal;
    }    
    label{
        margin-top: 20px;
        margin-bottom: 4px;
    }
</style>