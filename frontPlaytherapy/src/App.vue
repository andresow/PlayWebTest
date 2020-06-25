<template>
  <div id="app" class="flyout">
    
    <main>      
      <router-view></router-view>     
    </main>

    <mdb-footer color="stylish-color">
      <p class="footer-copyright mb-0 py-3 text-center">
        &copy; {{new Date().getFullYear()}} Copyright:
        <a
          href="https://mdbootstrap.com/docs/vue/?utm_source=DemoApp&utm_medium=MDBVue"
        >MDBootstrap.com</a>
      </p>
    </mdb-footer>

  </div>
</template>

<script>
  import { mdbFooter,} from "mdbvue";

  export default {
    name: "app",
    components: { mdbFooter, }
  };
</script>

<style>
  .flyout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    justify-content: space-between;
  }
</style>
