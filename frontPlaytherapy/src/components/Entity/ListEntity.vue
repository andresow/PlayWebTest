<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Registrar entidad médica</strong></h4>      
                </mdb-row>
                <hr /> 
                <section class="demo-section">
                    <section>
                        <form class="needs-validation" novalidate @submit="checkForm">                               
                            <div class="col-md-12 mb-6">
                                <label for="name">Nombre</label>
                                <input type="text" 
                                        class="form-control" 
                                        name="name" 
                                        placeholder="Nombre" 
                                        v-model.trim="form.name" required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el nombre
                                </div>
                            </div>  
                            <div class="text-center mt-4">
                                <mdb-btn color="info" type="submit" variant="success">Registrar</mdb-btn>
                                <a href="/patient/create" class="btn btn-light black-text">Cancelar</a>
                            </div>
                        </form>
                    </section>
                </section>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Lista de entidades médicas registradas</strong></h4>                         
                </mdb-row>
                <hr />                   
                <div class="">  
                    <section class="demo-section">
                        <section>
                            <mdb-datatable
                            :data="data2"
                            striped
                            bordered
                            arrows
                            :display="5"
                            responsive
                            defaultRow="Información no encontrada"
                            entriesTitle="Mostrar entradas"
                            searchPlaceholder="Buscar"          
                            noFoundMessage="Información no encontrada"
                            showingText="Cantidad"                
                            focus
                            @selectRow="selected = data2.rows[$event]"
                            />
                            <hr />
                            <h5>Editar la entidad médica seleccionada:</h5>
                            <mdb-container v-if="selected">
                                <mdb-row>
                                    <mdb-col>
                                    <mdb-input v-model="selected.name" />
                                    </mdb-col>
                                </mdb-row>
                                <mdb-row>
                                    <mdb-btn rounded color="info" @click.native="warning = true"><mdb-icon icon="trash-alt" /> Eliminar</mdb-btn>
                                    <mdb-modal :show="warning" @close="warning = false" warning>
                                    <mdb-modal-header>
                                        <mdb-modal-title class="text-center">Advertencia!</mdb-modal-title>
                                    </mdb-modal-header>
                                    <mdb-modal-body>
                                        <mdb-row>
                                        <mdb-col class="text-center">
                                            <mdb-icon icon="exclamation-triangle" size="4x" class="mb-3 animated rotateIn"/>
                                            <p class="card-text"><strong>¿Deseas eliminar la entidad médica: {{selected.name}}?</strong></p>
                                        </mdb-col>
                                        </mdb-row>
                                    </mdb-modal-body>
                                    <mdb-modal-footer center>
                                        <mdb-btn color="warning" @click.native="warning = false">Aceptar <mdb-icon icon="diamond" class="ml-1" color="white"/></mdb-btn>
                                        <mdb-btn outline="warning" @click.native="warning = false">Cancelar</mdb-btn>
                                    </mdb-modal-footer>
                                    </mdb-modal>
                                </mdb-row>
                            </mdb-container>
                        </section>
                    </section>         
                </div>  
            </mdb-container>
        </main>
    </div>
</template>

<script>
    import axios from 'axios';
    import swal from 'sweetalert';
    import Navigation from '@/components/Navigation/Navigation';
    import { 
        mdbContainer, 
        mdbBtn, 
        mdbIcon, 
        mdbRow, 
        mdbInput, 
        mdbCol, 
        mdbDatatable,
        mdbModal,
        mdbModalHeader,
        mdbModalTitle,
        mdbModalBody,
        mdbModalFooter,
    } from "mdbvue";

    export default {
        name: "ListEntity",
        components: {
            mdbContainer,
            mdbBtn,
            mdbIcon,
            mdbRow,
            mdbInput, 
            mdbDatatable,
            mdbCol,
            mdbModal,
            mdbModalHeader,
            mdbModalTitle,
            mdbModalBody,
            mdbModalFooter,
            Navigation
        },
        data() {
            return{
                warning: false,
                form: {
                    name: ''
                },
                entityId: this.$route.params.entityId,
                fields: [
                    { key : 'name', label:'Nombre'},
                    { key : 'action', label:''}
                ],
                entitys: [],
                pages: [],
                fields: [],
                selected: null,
                data2: {
                    columns: [
                        {
                            label: "Nombre",
                            field: "name",
                            sort: "asc"
                        }
                    ],
                    rows: [
                        {
                            name: "Tiger Nixon",
                            
                        },
                        {
                            name: "Garrett Winters",
                        
                        },
                        {
                            name: "Ashton Cox",
                        
                        },
                        {
                            name: "Cedric Kelly",
                            
                        },
                        {
                            name: "Airi Satou",
                        
                        },
                        {
                            name: "Brielle Williamson",
                            
                        }
                    ]
                }
            }
        },
        methods: {
            getEntitys(){
                const path = `${process.env.BASE_URI}entity/`
                axios.get(path).then((response) =>{
                    this.entitys = response.data
                })
                .catch((error)=>{
                    console.log(error)
                })
            },
            onSubmit(event){
                event.preventDefault()
                const path= `${process.env.BASE_URI}entity/` 
            
                axios.post(path, this.form).then((response)=>{
                    this.form.name = response.data.name
                    swal("Entidad medica creada exitosamente.", "", "success")
            })
                .catch((error)=>{
                    console.log(error)
                })
            }, 
            checkForm(event) {
                event.preventDefault();
                event.target.classList.add('was-validated');
            }, 
        },
        created(){
            this.getEntitys()
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
    .demo-section > table {
        padding: 20px 0;
    }
    .demo-title {
        color: #9e9e9e;
        font-weight: 700;
        margin-bottom: 0;
        padding-left: 15px;
    }
    label{
        margin-top: 20px;
        margin-bottom: 4px;
    } 
</style>