<template>
    <div>
        <!--Navbar-->
        <mdb-navbar position="top" 
                    style="margin-top: 0px" 
                    transparent color="info" 
                    name="Your Logo" 
                    href="#" 
                    scrolling >
            <mdb-navbar-brand to="/" waves class="font-weight-bold white-text">Playtherapy</mdb-navbar-brand>
            <mdb-navbar-toggler>
                <mdb-navbar-nav right>
                <mdb-nav-item exact to="">
                    <strong class="white-text">Acerca</strong>
                </mdb-nav-item>   
                <mdb-nav-item exact to="">
                    <strong class="white-text">Características</strong>
                </mdb-nav-item> 
                <mdb-nav-item exact to="">
                    <strong class="white-text">Videojuegos</strong>
                </mdb-nav-item>
                <mdb-nav-item exact to="">
                    <strong class="white-text">Contacto</strong>
                </mdb-nav-item>  
                <mdb-nav-item exact to="/login">
                    <strong class="white-text">Iniciar Sesión</strong>
                </mdb-nav-item>                
                </mdb-navbar-nav>
            </mdb-navbar-toggler>
        </mdb-navbar>
        <!--/Navbar-->
        <!--Content-->
        <div style="height: 100vh; margin-bottom: -25px">
            <div class="view intro-2">
                <div class="full-bg-img">
                    <div class="mask rgba-black-strong flex-center">
                        <div class="container">
                            <div class="white-text text-center">
                                <h2 class="font-weight-bold">Playtherapy</h2><br>
                                <p>Videojuego de apoyo a terapias de rehabilitación física</p><br>
                                <a href="/login" class="btn btn-info white-text">Continuar</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div> 
        <mdb-container>
            <mdb-row class="mt-5 align-items-center justify-content-start">
                <h4 class="demo-title"><strong></strong></h4>
            </mdb-row>
            <section class="demo-section">
                <h4>Minijuegos</h4>
                <section>
                    <mdb-carousel :interval="8000" showControls showIndicators>
                        <mdb-carousel-item img src="https://mdbootstrap.com/img/Photos/Slides/img%20(68).jpg" 
                                            mask="black-light" 
                                            alt="First slide">
                            <mdb-carousel-caption animation="fadeInDown" 
                                                    title="Light mask" 
                                                    text="First text">
                            </mdb-carousel-caption>
                        </mdb-carousel-item>
                        <mdb-carousel-item img src="https://mdbootstrap.com/img/Photos/Slides/img%20(6).jpg" 
                                            mask="black-strong" 
                                            alt="Second slide">
                            <mdb-carousel-caption animation="fadeInDown" 
                                                    title="Strong mask" 
                                                    text="Second text">
                            </mdb-carousel-caption>
                        </mdb-carousel-item>
                        <mdb-carousel-item img src="https://mdbootstrap.com/img/Photos/Slides/img%20(9).jpg" 
                                            mask="black-slight" 
                                            alt="Third slide">
                            <mdb-carousel-caption animation="fadeInDown" 
                                                    title="Super light mask" 
                                                    text="Third text">
                            </mdb-carousel-caption>
                        </mdb-carousel-item>
                    </mdb-carousel>
                </section>
            </section>
        </mdb-container>
        <!--/Content-->
    </div>
</template>

<script>
    import { 
        animateOnScroll,
        mdbCarousel,
        mdbCarouselCaption,
        mdbCarouselItem,
        mdbContainer,
        mdbNavbar,
        mdbNavbarNav,
        mdbNavbarToggler,
        mdbNavItem,
        mdbRow,
    } from 'mdbvue';

    export default {
    name: 'Welcome',
    components: {
        mdbCarousel,
        mdbCarouselCaption,
        mdbCarouselItem,
        mdbContainer,
        mdbNavbar,
        mdbNavbarNav,
        mdbNavbarToggler,
        mdbNavItem,
        mdbRow,   
    },
    directives: {
        animateOnScroll
    },
    mounted() {
        document.getElementById("main-navbar").style.height = '60px';
    },
    beforeDestroy() {
        document.getElementById("main-navbar").style.height = null;
    }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
    h2 {
        font-weight: normal;
    }
    .view {
        background: url("../../assets/index2.jpg")no-repeat center center;
        background-size: cover;
        height: 100%;
    }    
</style>

