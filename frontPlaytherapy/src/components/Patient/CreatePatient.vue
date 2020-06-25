<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Registrar paciente</strong></h4>      
                </mdb-row>
                <hr />   
                <section class="demo-section">
                    <section>
                        <form class="needs-validation" novalidate @submit="checkForm">                                
                            <div class="col-md-12 mb-6">
                                <label for="id_type">Tipo de identificación</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.id_type" 
                                        placeholder="Tipo de identificación" 
                                        required>
                                    <option value="1">Cédula de ciudadanía</option>
                                    <option value="2">Tarjeta de identidad</option>
                                    <option value="3">Cédula de extranjería</option>
                                    <option value="2">Registro civil</option>
                                    <option value="3">Número de pasaporte</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el tipo de identificación.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="id_num">Número de identificación</label>
                                <input type="text" 
                                        class="form-control" 
                                        name="id_num" 
                                        placeholder="Número de identificación" 
                                        v-model.trim="form.id_num" 
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
                                <input :formatter="format" 
                                        type="text" 
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
                                <input :formatter="format" 
                                        type="text" 
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
                                <label for="birthday">Fecha de nacimiento</label>
                                <input type="date" 
                                        name="birthday" 
                                        class="form-control" 
                                        v-model.trim="form.birthday" 
                                        required>  
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese la fecha de nacimiento.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="occupation">Ocupación</label>
                                <input :formatter="format" 
                                        type="text" 
                                        class="form-control" 
                                        name="occupation" 
                                        placeholder="Ocupación" 
                                        v-model.trim="form.occupation" 
                                        required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese la ocupación.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6 col-sm-12">
                                <label for="entity">Entidad médica</label>
                                <mdb-row>
                                    <mdb-col center class="col-md-11 col-sm-10">
                                        <select entity class="browser-default custom-select"  
                                                v-model.trim="form.entity" 
                                                required>
                                            <template slot:first>
                                                <option :value="null" disabled>-- Por favor seleccione una entidad médica --</option>
                                            </template>
                                            <option v-for="entity in entity" 
                                                :key="entity.id" 
                                                :value="entity.id" >{{ entity.name }} 
                                            </option>
                                        </select>
                                    </mdb-col>
                                    <mdb-col class="col-md-1 col-sm-2">
                                        <a @click.native="showModal13 = true" class="btn-sm btn-info white-text d-block margin-buttom"><mdb-icon  class="margin-icon" icon="plus" /></a>
                                        
                                    </mdb-col>
                                    <mdb-modal centered :show="showModal13" @close="showModal13 = false">
                                <mdb-modal-header>
                                    <mdb-modal-title>Modal title</mdb-modal-title>
                                </mdb-modal-header>
                                <mdb-modal-body>...</mdb-modal-body>
                                <mdb-modal-footer>
                                    <mdb-btn color="secondary" @click.native="showModal13 = false">Close</mdb-btn>
                                    <mdb-btn color="primary">Save changes</mdb-btn>
                                </mdb-modal-footer>
                            </mdb-modal>
                                </mdb-row>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione la entidad médica.
                                </div>
                            </div>
                            
                            <div class="col-md-12 mb-6 col-sm-12">
                                <label for="list_diagnostic">Diagnóstico</label>
                                <mdb-row>
                                    <mdb-col class="col-md-11 col-sm-10">
                                        <select diagnostic class="browser-default custom-select" 
                                                v-model.trim="form.list_diagnostic" 
                                                required>
                                            <template slot:first>
                                                <option :value="null" disabled>-- Por favor seleccione el diagnóstico del paciente --</option>
                                            </template>
                                            <option v-for="diagnostic in diagnostic" 
                                                    :key="diagnostic.id" 
                                                    :value="diagnostic.id" >{{ diagnostic.name }} 
                                            </option>
                                        </select>
                                    </mdb-col>
                                    <mdb-col class="col-md-1 col-sm-2">
                                        <a href="/diagnostic/create" class="btn-sm btn-info white-text d-block margin-buttom"><mdb-icon  class="margin-icon" icon="plus" /></a>
                                    </mdb-col>
                                </mdb-row>                                    
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el diagnóstico.
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
    import { 
        mdbBtn,
        mdbCol,
        mdbContainer, 
        mdbRow,
        mdbIcon, 
        mdbInput,
        mdbModal, 
        mdbModalHeader, 
        mdbModalTitle, 
        mdbModalBody, 
        mdbModalFooter, 
        mdbTbl, 
        mdbTblHead, 
        mdbTblBody,
    } from "mdbvue";
    import Navigation from '@/components/Navigation/Navigation';

    export default {
        name: "InputsPage",
        components: {
            mdbBtn,
            mdbCol,
            mdbContainer, 
            mdbRow,
            mdbIcon,
            mdbInput,
            mdbModal, 
            mdbModalHeader, 
            mdbModalTitle, 
            mdbModalBody, 
            mdbModalFooter,
            mdbTbl, 
            mdbTblHead, 
            mdbTblBody,
            Navigation
        },
        data(){
            return {
                form: {
                    name: ''
                },
                entity: [],
                diagnostic: [],                
                showModal13: false,
            }
        },
        methods: {
            onSubmit(event){
                event.preventDefault()
                const path= 'http://localhost:8000/api/v1.0/patient/'
                axios.post(path, this.form).then((response)=>{
                    this.form.id_type = response.data.id_type
                    this.form.id_num = response.data.id_num
                    this.form.name = response.data.name
                    this.form.lastname = response.data.lastname
                    this.form.genre = response.data.genre
                    this.form.occupation = response.data.occupation
                    this.form.birthday = response.data.birthday
                    this.form.entity = response.data.entity
                    this.form.list_diagnostic = response.data.list_diagnostic

                    swal("Paciente creado exitosamente.", "", "success")
            })
                .catch((error)=>{
                    swal("No se ha podido crear el paciente.", "", "error")
                    console.log(error)
                })
            },  
            getEntity (){
                const path= 'http://localhost:8000/api/v1.0/entity/' 
            
                axios.get(path).then((response) =>{
                    this.entity = response.data
                })
                .catch((error)=>{
                    console.log(error)
                })
            },
            getDiagnostic (){
                const path= 'http://localhost:8000/api/v1.0/diagnostic/' 
            
                axios.get(path).then((response) =>{
                    this.diagnostic = response.data
                })
                .catch((error)=>{
                    console.log(error)
                })
            },
            format(value, event) {
                return value.toLowerCase()
        },
        checkForm(event) {
            event.target.classList.add('was-validated');
            this.onSubmit(event);

            },              
        },       
        created(){
            this.getEntity()
            this.getDiagnostic ()
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
    .margin-buttom {
        margin-left: -15px;
        height: 100%;
    } 
    .margin-icon {
        margin-top: 20%;
        margin-left: 35%;
    }  
</style>