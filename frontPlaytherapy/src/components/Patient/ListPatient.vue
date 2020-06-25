<template>  
  <div>
    <Navigation />
    <main :style="{marginTop: '90px'}">              
      <mdb-container>
        <mdb-row class="mt-5 justify-content-start">
            <h4 class="demo-title"><strong>Lista de pacientes</strong></h4>      
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

<script>
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
              field: "id_type",
              sort: "asc",
            },
            {
              label: "Número de documento",
              field: "id_num",
              sort: "asc"
            },
            {
              label: "Nombres",
              field: "name",
              sort: "asc"
            },
            {
              label: "Apellidos",
              field: "lastname",
              sort: "asc"
            },
            {
              label: "Género",
              field: "genre",
              sort: "asc"
            },
            {
              label: "Ocupación",
              field: "occupation",
              sort: "asc"
            },
            {
              label: "Fecha de nacimiento",
              field: "birthday",
              sort: "asc"
            },
            {
              label: "Medida de Independencia Funcional",
              field: "FIM",
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
          rows:this.rows
     
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
      fetch('http://localhost:8000/api/v1.0/patient/?format=json')
        .then(res => res.json())
        .then(json => {
          let keys = ["id_type", "id_num", "name", "lastname", "genre", "occupation", "birthday"];
          let entries = this.filterData(json, keys);
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

