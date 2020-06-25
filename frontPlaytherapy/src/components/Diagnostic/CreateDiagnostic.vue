<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Registrar diagnóstico</strong></h4>      
                </mdb-row>
                <hr />  
                <section class="demo-section">
                    <section>
                        <form class="needs-validation" novalidate @submit="checkFormD">                            
                            <div class="col-md-12 mb-6">
                                <label for="code">Código</label>
                                <input type="text" 
                                        class="form-control" 
                                        name="username" 
                                        placeholder="Código de diagnóstico"
                                        v-model.trim="form.code" required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el código del diagnóstico.
                                </div>
                            </div>                        
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
                                    Por favor ingrese el nombre.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">                            
                                <label for="typeDiagnostic">Tipo de diagnóstico</label>
                                <select typeDiagnostic 
                                        class="browser-default custom-select" 
                                        id="inputGroupSelect04" 
                                        v-model.trim="form.type_diagnostic" 
                                        placeholder="Tipo de diagnóstico" 
                                        aria-label="Example select with button addon" 
                                        required>
                                    <template slot:first>
                                        <option :value="null" disabled>-- Por favor seleccione un tipo de diagnóstico --</option>
                                    </template>
                                        <option v-for="typeDiagnostic in typeDiagnostic" 
                                                :key="typeDiagnostic.id" 
                                                :value="typeDiagnostic.id" >{{ typeDiagnostic.name }} 
                                        </option>
                                </select>                                
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el tipo de diagnóstico.
                                </div>
                            </div>  
                            <div class="text-center mt-4">
                                <mdb-btn color="info" type="submit" variant="success">Registrar</mdb-btn>
                                <a href="/patient/create" class="btn btn-light black-text">Cancelar</a> 
                            </div>                  
                        </form>
                    </section>                                       
                </section>      
                <mdb-col>  
                    <hr />
                    <mdb-row>
                        <mdb-btn color="info" @click.native="info = true">
                            <mdb-icon icon="plus" /> Añadir tipo de diagnóstico 
                        </mdb-btn>
                        <mdb-modal size="lg" :show="info" @close="info = false" info>
                            <mdb-modal-header>
                                <mdb-modal-title><strong>Registrar tipo de diagnóstico</strong> </mdb-modal-title>
                            </mdb-modal-header>
                            <mdb-modal-body>
                                <section>
                                    <form  class="needs-validation" novalidate @submit="checkForm">
                                        <div class="form-row">                                            
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
                                                    Por favor ingrese el nombre.
                                                </div>
                                            </div>
                                        </div>  
                                        <div class="text-center mt-4">                                
                                            <mdb-btn color="info" >Registrar</mdb-btn>
                                            <a href="/diagnostic/create" class="btn btn-light black-text">Cancelar</a> 
                                        </div>            
                                    </form>
                                </section>
                                <mdb-col> 
                                    <mdb-row class="mt-5 justify-content-start">
                                        <h4> Listado de tipos de diagnósticos registrados.</h4>   
                                    </mdb-row>                                 
                                    <hr/>
                                    <mdb-row>
                                        <section class="demo-section">                                    
                                            <section>
                                                <mdb-datatable
                                                    :data="data"
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
                                                />
                                                <hr />
                                                <h5>Editar el tipo de diagnóstico seleccionado:</h5>
                                                <mdb-container v-if="selected">
                                                    <mdb-row>
                                                        <mdb-col>
                                                        <mdb-input v-model="selected.name" />
                                                        </mdb-col>
                                                    </mdb-row>
                                                    <mdb-row>
                                                        <mdb-btn rounded color="info" 
                                                                @click.native="warning = true"><mdb-icon 
                                                                icon="trash-alt" /> Eliminar
                                                        </mdb-btn>
                                                        <mdb-modal centered :show="warning" @close="warning = false" >
                                                            <mdb-modal-body>
                                                                <mdb-row>
                                                                    <mdb-col class="text-center">
                                                                        <mdb-modal-title class="text-center"><strong>Advertencia!</strong></mdb-modal-title>
                                                                        <mdb-icon color="warning" 
                                                                                    icon="exclamation-triangle" 
                                                                                    size="4x" 
                                                                                    class="mb-3 animated rotateIn"/>
                                                                        <p class="card-text">
                                                                            <strong>¿Deseas eliminar el tipo de diagnóstico: {{selected.name}}?</strong>
                                                                        </p>
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
                                    </mdb-row>
                                </mdb-col>       
                            </mdb-modal-body>
                        </mdb-modal>
                    </mdb-row>
                </mdb-col>       
            </mdb-container>   
        </main>
    </div>
</template>
<script>
    import axios from 'axios';
    import swal from 'sweetalert';
    import { mdbContainer, 
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
    import Navigation from '@/components/Navigation/Navigation';

    export default {
        name: "InputsPage",
        components: {
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
            Navigation
        },
        data(){
            return {
                info: false,
                warning: false,
                form: {
                    name: ''
                },
                
                typeDiagnostic: [],            
                selected: null,
                
                columns: [],
                rows: []
                
            }
        },computed: {
            data() {
                return {
                columns: [{
                    label: "Nombre",
                    field: "name",
                    sort: "asc",
                    }
                ],
                rows: this.rows
                };
            },
        },
        methods: {
            onSubmit(event){
                event.preventDefault()
                const path= 'http://localhost:8000/api/v1.0/typeDiagnostic/';
                axios.post(path, this.form).then((response)=>{
                    this.form.nameTD = response.data.name;
                    swal("Tipo de diagnostico creado exitosamente.", "", "success")
            })
                .catch((error)=>{
                    swal("No se ha podido crear el tipo de diagnostico.", "", "error")
                    console.log(error);
                })
            },onSubmitD(event){
                event.preventDefault()
                const path= 'http://localhost:8000/api/v1.0/diagnostic/';
                axios.post(path, this.form).then((response)=>{
                    this.form.code = response.data.code;
                    this.form.type_diagnostic = response.data.type_diagnostic;
                    this.form.name = response.data.name;
                    swal("Tipo de diagnostico creado exitosamente.", "", "success")
            })
                .catch((error)=>{
                    swal("No se ha podido crear el tipo de diagnostico.", "", "error")
                    console.log(error);
                })
            },
            checkForm(event) {
                event.target.classList.add('was-validated');
                this.onSubmit(event);

            },
            checkFormD(event) {
                event.target.classList.add('was-validated');
                this.onSubmitD(event);

            },
            filterData(dataArr, keys) {
                let data = dataArr.map(entry => {
                let filteredEntry = {};
                keys.forEach(key => {
                    if (key in entry) {
                    filteredEntry[key] = entry[key];
                    }
                });
                return filteredEntry;
            });
            return data;
      },getTypeDiagnostic (){
                const path= 'http://localhost:8000/api/v1.0/typeDiagnostic/' 
            
                axios.get(path).then((response) =>{
                    this.typeDiagnostic = response.data
                })
                .catch((error)=>{
                    console.log(error)
                })
            }              
        },
    mounted(){
      fetch('http://localhost:8000/api/v1.0/typeDiagnostic/?format=json')
        .then(res => res.json())
        .then(json => {
          let keys = ["name"];
          let entries = this.filterData(json, keys);
          this.columns = keys.map(key => {
            return {
              label: key.toUpperCase(),
              field: key,
              sort: true
            };
          });
          //rows
          entries.map(entry => this.rows.push(entry));
        })
        .catch(err => console.log(err));
    },created(){
            this.getTypeDiagnostic ()
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
    label{
        margin-top: 20px;
        margin-bottom: 4px;
    }  
</style>