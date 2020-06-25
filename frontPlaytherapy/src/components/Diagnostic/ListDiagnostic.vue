<template>
  <mdb-container class="mt-5">  
    <section class="demo-section">
      <h4>Listado de diagnósticos registrados.</h4>
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
          :tfoot="false"
          @selectRow="selected = data2.rows[$event]"
        />
        <hr />
        <h5>Editar el diagnóstico seleccionado:</h5>
        <mdb-container v-if="selected">
          <mdb-row>
            <mdb-col>
              <mdb-input v-model="selected.code" />
            </mdb-col>
            <mdb-col>
              <mdb-input v-model="selected.name" />
            </mdb-col>
            <mdb-col>
              <mdb-input v-model="selected.typeDiagnostic" />
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
                    <p class="card-text"><strong>¿Deseas eliminar el diagnóstico: {{selected.name}} {{ selected.lastname}}?</strong></p>
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
       <!--
        <b-table striped hover :items="typeDiagnostic" :fields="fields">

            <template v-slot:cell(action)="row" slote-scope="data">
                <b-button size="sm" variant="primary" >
                    Editar
                </b-button>
                <b-button size="sm" variant="danger"  >
                    Eliminar
                </b-button>
                </template>

        </b-table>-->
    </section>
  </mdb-container>   
</template>



<script>
import axios from 'axios';
import {
  mdbDatatable,
  mdbIcon,
  mdbRow,
  mdbCol,
  mdbContainer,
  mdbInput,
  mdbModal,
  mdbModalHeader,
  mdbModalTitle,
  mdbModalBody,
  mdbModalFooter,
  mdbBtn,
} from "mdbvue";

export default {
    components: {
        mdbDatatable,
        mdbContainer,
        mdbRow,
        mdbIcon,
        mdbInput,
        mdbCol,
        mdbModal,
        mdbModalHeader,
        mdbModalTitle,
        mdbModalBody,
        mdbModalFooter,
        mdbBtn,
    },
    data(){
        return{
            warning: false,
            entityId: this.$route.params.entityId,
            fields: [
                { key : 'name', label:'Nombre'},
                { key : 'code', label:'Codigo'},
                { key : 'type_diagnostic', label:'Tipo de diagnostico'},
                { key : 'action', label:''}
            ],
            typeDiagnostic: [],
            selected: null,
            data2: {
                columns: [
                    {
                        label: "Código",
                        field: "code",
                        sort: "asc"
                    },
                    {
                        label: "Nombre",
                        field: "name",
                        sort: "asc"
                    },
                    {
                        label: "Tipo de diagnóstico",
                        field: "typeDiagnostic",
                        sort: "asc"
                    }
                ],
                rows: [         
                {
                    name: "Quinn ",
                    typeDiagnostic: "Edinburgh",
                    code: "22",
                },
                {
                    name: "Charde",
                    typeDiagnostic: "San Francisco",
                    code: "36",
                },
                {
                    name: "Haley",
                    typeDiagnostic: "London",
                    code: "43",
                },          
                {
                    name: "Hope Fuentes",
                    typeDiagnostic: "San Francisco",
                    code: "41",
                },
                {
                    name: "Vivian Harrell",
                    typeDiagnostic: "San Francisco",
                    code: "62",
                }
                ]
            }
        }
    },
    methods: {
        getTypeDiagnostic(){
            const path = `${process.env.BASE_URI}diagnostic/`
            axios.get(path).then((response) =>{
                this.typeDiagnostic = response.data
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    },
    created(){
        this.getTypeDiagnostic()
    }
}
</script>