<template>
  <div>
    <Navigation />
    <main :style="{marginTop: '90px'}">       
      <mdb-container>
        <mdb-row class="mt-5 align-items-center justify-content-start">
          <h4 class="demo-title"><strong>Inicio </strong></h4>      
        </mdb-row>
        <hr class="mb-5" />
        <mdb-row>
          <mdb-col sm="4">
            <mdb-card cascade>
              <mdb-view class="card-header" cascade> 
                <mdb-row>
                  <mdb-col>
                    <mdb-icon color="white" icon="user-alt fa-4x" />
                  </mdb-col>
                  <mdb-col right>
                    <h2 class="card-header-title text-right color">1</h2>                
                    <p class="mb-0 text-right color">Pacientes</p>  
                  </mdb-col>
                </mdb-row>     
              </mdb-view>
              <mdb-card-body class="text-left" cascade>                
                <mdb-navbar-nav nav vertical>
                  <mdb-nav-item href="/patient/create" >Registrar paciente</mdb-nav-item>
                  <mdb-nav-item href="/patient">Listar Paciente</mdb-nav-item>
                </mdb-navbar-nav>                
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
          <mdb-col sm="4">
            <mdb-card cascade>
              <mdb-view class="card-header" cascade> 
                <mdb-row>
                  <mdb-col>
                    <mdb-icon color="white" icon="user-md fa-4x" />
                  </mdb-col>
                  <mdb-col right>
                    <h2 class="card-header-title text-right color">0</h2>                
                    <p class="mb-0 text-right color">Terapeutas</p>  
                  </mdb-col>
                </mdb-row>     
              </mdb-view>
              <mdb-card-body class="text-left" cascade>                
                <mdb-navbar-nav nav vertical>
                  <mdb-nav-item href="/therapist/create" >Registrar terapeutas</mdb-nav-item>
                  <mdb-nav-item href="/therapist">Listar terapeutas</mdb-nav-item>
                </mdb-navbar-nav>                
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
          <mdb-col sm="4">
            <mdb-card cascade>
              <mdb-view class="card-header" cascade> 
                <h4 class="color">Pasos para crear y/o asignar un FIM a un paciente</h4>   
              </mdb-view>
              <mdb-card-body class="text-left" cascade>                
                <p class="margin-text">1. Buscar el paciente </p>
                <p class="margin-text">2. Ingresar al FIM del paciente</p> 
                <p class="margin-text">3. Seleccionar nuevo para ingresar los datos</p>                               
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </mdb-container>
    </main>
  </div>
</template>

<script>
  import {    
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbCard,
    mdbCardImage,
    mdbCardHeader,
    mdbCardBody,
    mdbCardTitle,
    mdbCardText,
    mdbCardFooter,
    mdbView,
    mdbIcon,
    mdbNavbarNav,
    mdbNavItem,
  } from "mdbvue";
  import Navigation from '@/components/Navigation/Navigation';

  export default {
    name: "Home",
    components: {
      Navigation,
      mdbContainer,
			mdbRow,
			mdbCol,
			mdbCard,
			mdbCardImage,
			mdbCardHeader,
			mdbCardBody,
			mdbCardTitle,
			mdbCardText,
			mdbCardFooter,
			mdbView,
      mdbIcon,
      mdbNavbarNav,
      mdbNavItem,
    },  
  };
</script>

<style>
  .card-header {
    background: #35a0d9;
  }
  .color {
    color: white;
  }
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
  .margin-text {
    margin-bottom: 0px;
  }
</style>

