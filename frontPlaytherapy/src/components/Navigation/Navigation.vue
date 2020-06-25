<template>
    <div>
        <mdb-navbar
            id="main-navbar"
            dark 
            color="info"
            position="top"
            scrolling
            :scrollingOffset="20"
        >
            <mdb-navbar-brand to="/" waves class="font-weight-bold">Playtherapy</mdb-navbar-brand>
            <mdb-navbar-toggler>
                <mdb-navbar-nav right>
                    <mdb-nav-item exact to="/home">
                        <strong>Inicio</strong>
                    </mdb-nav-item>                   
                    <mdb-dropdown tag="li" class="nav-item">
                        <mdb-dropdown-toggle
                        tag="a"
                        navLink
                        color="info"
                        slot="toggle"
                        waves-fixed
                        ><strong>Pacientes</strong></mdb-dropdown-toggle>
                        <mdb-dropdown-menu>
                        <mdb-dropdown-item exact to="/patient/create">Registrar</mdb-dropdown-item>
                        <mdb-dropdown-item exact to="/patient">Listar</mdb-dropdown-item>
                        </mdb-dropdown-menu>
                    </mdb-dropdown>  
                    <mdb-dropdown tag="li" class="nav-item">
                        <mdb-dropdown-toggle
                        tag="a"
                        navLink
                        color="info"
                        slot="toggle"
                        waves-fixed
                        ><strong>Terapeutas</strong></mdb-dropdown-toggle>
                        <mdb-dropdown-menu>
                        <mdb-dropdown-item exact to="/therapist/create">Registrar</mdb-dropdown-item>
                        <mdb-dropdown-item exact to="/therapist">Listar</mdb-dropdown-item>
                        </mdb-dropdown-menu>
                    </mdb-dropdown><!--
                    <mdb-nav-item exact to="/entitys">
                        <strong>Entidad médica</strong>
                    </mdb-nav-item>  
                    <mdb-nav-item exact to="/FIM/create">
                        <strong>FIM</strong>
                    </mdb-nav-item> 
                    <mdb-dropdown tag="li" class="nav-item">
                        <mdb-dropdown-toggle
                        tag="a"
                        navLink
                        color="info"
                        slot="toggle"
                        waves-fixed
                        ><strong>Diagnóstico</strong></mdb-dropdown-toggle>
                        <mdb-dropdown-menu>
                            <mdb-dropdown-item exact to="/diagnostic/create">Crear</mdb-dropdown-item>
                            <mdb-dropdown-item exact to="/diagnostic">Listar</mdb-dropdown-item>
                        </mdb-dropdown-menu>
                    </mdb-dropdown> -->
                    <mdb-dropdown tag="li" class="nav-item">
                        <mdb-dropdown-toggle
                        tag="a"
                        navLink
                        color="info"
                        slot="toggle"
                        waves-fixed
                        icon="user-alt"
                        ></mdb-dropdown-toggle>
                        <mdb-dropdown-menu right>
                            <mdb-dropdown-item exact to="">Perfil</mdb-dropdown-item>
                            <mdb-dropdown-item exact to="">Configuración</mdb-dropdown-item>
                            <hr />
                            <mdb-dropdown-item exact to="/">Cerrar sesión</mdb-dropdown-item>
                        </mdb-dropdown-menu>
                    </mdb-dropdown>                              
                </mdb-navbar-nav>
            </mdb-navbar-toggler>
        </mdb-navbar>
    </div>
</template>

<script>
import {
  mdbDropdown,
  mdbDropdownItem,
  mdbDropdownMenu,
  mdbDropdownToggle,
  mdbNavbar,
  mdbNavItem,
  mdbNavbarNav,
  mdbNavbarToggler,
  mdbNavbarBrand, 
} from "mdbvue";

export default {
  name: "Navigation",
  components: {
    mdbDropdown,
    mdbDropdownItem,
    mdbDropdownMenu,
    mdbDropdownToggle,
    mdbNavbar,
    mdbNavItem,
    mdbNavbarNav,
    mdbNavbarToggler,
    mdbNavbarBrand,
  },   
};
</script>

<style scope>

</style>

