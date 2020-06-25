<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Medida de independencia funcional</strong></h4>      
                </mdb-row>
                <hr />   
                <section class="demo-section">
                    <section>
                        <form class="needs-validation" novalidate @submit="checkForm">                            
                            <div class="col-md-12 mb-6">                                                     
                                <label class="margin-label" for="date">Fecha</label>
                                <input type="date" 
                                        name="date" 
                                        class="form-control" 
                                        v-model.trim="form.date" 
                                        required>  
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese la fecha
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="goal">Meta</label>
                                <div class="custom-control custom-checkbox lg" >
                                    <input type="checkbox" 
                                        class="custom-control-input" 
                                        id="customControlValidation1">
                                    <label class="custom-control-label lg" for="customControlValidation1"></label>
                                </div>                           
                            </div>
                            <mdb-row class="mt-3 align-items-center justify-content-start">
                                <h4 class="demo-title text-center"><strong>Movimiento</strong></h4>
                            </mdb-row>
                            <hr />
                            <h6 class="demo-title-small"><strong>Autocuidado</strong></h6>
                            <hr />
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="food">Comer</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.food" 
                                        placeholder="Comida" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de comer
                                </div>
                            </div>                            
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="personalCare">Arreglo personal</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.personalCare" 
                                        placeholder="Limpieza personal" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de arreglo personal
                                </div>
                            </div>  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="shower">Bañarse/Ducharse</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.shower" 
                                        placeholder="Bañarse/Ducharse" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de bañarse/ducharse
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="clothedTop">Vestirse/Desvertirse superior</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.clothedTop" 
                                        placeholder="Vestirse/Desvertirse Superior" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de vestirse/desvertirse superior
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="clothedLow">Vestirse/Desvertirse inferior</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.clothedLow" 
                                        placeholder="Vestirse/Desvertirse Inferior" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de vestirse/desvertirse inferior
                                </div>
                            </div>  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="use">Uso del baño</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.use" 
                                        placeholder="Uso del baño" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de uso del baño
                                </div>
                            </div> 
                            <h6 class="demo-title-small"><strong>Control de esfínteres</strong></h6>
                            <hr />            
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="control">Control de heces</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.control" 
                                        placeholder="Control de heces" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de control de heces
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="urine">Control de orina</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.urine" 
                                        placeholder="Control de orina" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de control de orina.                                </div>
                            </div> 
                            <h6 class="demo-title-small"><strong>Movilidad</strong></h6>
                            <hr />  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="bed">Traslado de la cama a silla o silla de ruedas</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.bed" 
                                        placeholder="Cama, silla y silla de ruedas" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de traslado de la cama a silla o silla de ruedas.
                                </div>
                            </div>  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="bathroom">Traslado al baño</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.bathroom" 
                                        placeholder="Baño" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de traslado al baño
                                </div>
                            </div>              
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="douche">Traslado en bañera o ducha</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.douche" 
                                        placeholder="Ducha" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de traslado en bañera o ducha
                                </div>
                            </div> 
                            <h6 class="demo-title-small"><strong>Ambulación</strong></h6>
                            <hr />  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="march">Caminar/desplazarse en silla de ruedas y gateo</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.march" 
                                        placeholder="Marcha, silla de ruedas y gateo" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de caminar/desplazarse en silla de ruedas y gateo
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="grades">Subir y bajar escaleras</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.grades" 
                                        placeholder="Gradas" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de subir y bajar escaleras
                                </div>
                            </div>                             
                            <mdb-row class="mt-3 align-items-center justify-content-start">
                                <h4 class="demo-title text-center"><strong>Reconocimiento</strong></h4>
                            </mdb-row> 
                            <hr />
                            <h6 class="demo-title-small"><strong>Comunicación</strong></h6>
                            <hr />
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="compression">Compresión</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.compression" 
                                        placeholder="Compresión" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de compresión
                                </div>
                            </div>            
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="expression">Expresión</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.expression" 
                                        placeholder="Expresión" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de expresión
                                </div>
                            </div> 
                            <h6 class="demo-title-small"><strong>Conocimiento social</strong></h6>
                            <hr />
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="social">Interacción social</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.social" 
                                        placeholder="Interacción social" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de interacción social
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="problem">Resolver problema</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.problem" 
                                        placeholder="Resolver problema" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de resolver problema
                                </div>
                            </div>  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="memory">Memoria</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.memory" 
                                        placeholder="Memoria" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de memoria
                                </div>
                            </div>  
                            <div class="text-center mt-4">
                                <mdb-btn color="info" type="submit" variant="success">Registrar</mdb-btn>
                                <a href="/patient" class="btn btn-light black-text">Cancelar</a>
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
    import swal from 'sweetalert';
    import { mdbContainer, mdbBtn, mdbRow, mdbInput } from "mdbvue";
    import Navigation from '@/components/Navigation/Navigation';

    export default {
        name: "InputsPage",
        components: {
            mdbContainer,
            mdbBtn,
            mdbRow,
            mdbInput,
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
                const path= `${process.env.BASE_URI}FIM/`
                axios.post(path, this.form).then((response)=>{
                    swal("FIM creado exitosamente.", "", "success")
            })
                .catch((error)=>{
                    swal("No se ha podido crear el FIM.", "", "error")
                    console.log(error)
                })
            },
            checkForm(event) {
                event.preventDefault();
                event.target.classList.add('was-validated');
            }
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
        font-weight: 400;
        margin-bottom: 0;
        padding-left: 15px;
    }   
    .demo-title-small {
        color: #9e9e9e;
        font-weight: 400;
        margin-bottom: -10px;
        margin-top: 30px;
    }  
    .margin-label{
        margin-top: 20px;
        margin-bottom: 4px;
    } 
</style>