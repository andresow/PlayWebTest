<template>  
  <div>
    <Navigation />
    <main :style="{marginTop: '90px'}">              
      <mdb-container>
        <mdb-row class="mt-5 justify-content-start">
            <h4 class="demo-title"><strong>Lista de terapeutas</strong></h4>      
        </mdb-row>
        <hr />
        <div class="flex-center">  
          <section class="demo-section">
            <section>
              <mdb-datatable
                :data="data"
                striped
                bordered
                arrows
                :display="5"
                responsive
                entriesTitle="Mostrar entradas"
                searchPlaceholder="Buscar"          
                noFoundMessage="Información no encontrada"
                showingText="Cantidad"
                :tfoot= false
              />
            </section>            
          </section>           
        </div>  
      </mdb-container> 
    </main>
  </div>  
</template>
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
                                        <p class="card-text"><strong>¿Deseas eliminar al terapeuta: {{selected.name}} {{ selected.lastname}}?</strong></p>
                                    </mdb-col>
                                    </mdb-row>
                                </mdb-modal-body>
                                <mdb-modal-footer center>
                                    <mdb-btn color="warning" @click.native="warning = false">Aceptar <mdb-icon icon="diamond" class="ml-1" color="white"/></mdb-btn>
                                    <mdb-btn outline="warning" @click.native="warning = false">Cancelar</mdb-btn>
                                </mdb-modal-footer>
                            </mdb-modal>
                        </mdb-row>

<script>
    import axios from 'axios';
    import {
        mdbDatatable,
        mdbRow,
        mdbContainer,
    } from "mdbvue";
    import Navigation from '@/components/Navigation/Navigation';

  export default {
    components: {
      mdbDatatable,
      mdbContainer,
      mdbRow,
      Navigation,
    },
    data() {
      return {
        columns: [],
        rows: []
      };
    },
    computed: {
      data() {
        return {          
          columns: [
            {
              label: "Tipo de documento",
              field: "typeIdentification",
              sort: "asc",
            },
            {
              label: "Número de documento",
              field: "identification",
              sort: "asc"
            },
            {
              label: "Genero",
              field: "genre",
              sort: "asc"
            },
            {
              label: "Nombre",
              field: "name",
              sort: "asc"
            },
            {
              label: "Apellido",
              field: "lastname",
              sort: "asc"
            },
            {
              label: "",
              field: "editar",
              sort: false,
            },
            {
              label: "",
              field: "eliminar",
              sort: false,
            },
          ],
          rows: this.rows 
        };
      },
    },
    methods: {
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
      }
    },
    mounted(){
      fetch('http://localhost:8000/api/v1.0/therapists/all-therapist?format=json')
        .then(res => res.json())
        .then(json => {
          let keys = ["typeIdentification", "identification", "genre",'name','lastname', 'user'];
          let entries = this.filterData(json, keys);
          //columns
          console.log(json)
          this.columns = keys.map(key => {
            return {
              label: key,
              field: key,
            };
          });
          //rows
          entries.map(entry => this.rows.push(entry));        
        })
        .catch(err => console.log(err));
    }
  };
</script>

<style scoped>
    .demo-section {
        padding: 20px 0;
    }
    .demo-section > section {
        border: 1px solid #e0e0e0;
        padding: 15px;
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
</style>