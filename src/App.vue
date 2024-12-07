<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div id="principal">
    <header>
      <div class="logo">
        <img src="/Group 7.png" />
        <span>AY</span>
      </div>
      <nav>
        <RouterLink
          to="/"
          class="icon-text-link"
          :class="{ selected: $route.path === '/' }"
        >
          <svg
            width="24"
            height="25"
            viewBox="0 0 24 25"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M21.0001 3.12671L14.5001 21.1267C14.4562 21.2225 14.3858 21.3036 14.2971 21.3605C14.2085 21.4173 14.1054 21.4476 14.0001 21.4476C13.8948 21.4476 13.7917 21.4173 13.703 21.3605C13.6144 21.3036 13.5439 21.2225 13.5001 21.1267L10.0001 14.1267L3.00007 10.6267C2.90433 10.5828 2.8232 10.5124 2.76632 10.4238C2.70944 10.3351 2.6792 10.232 2.6792 10.1267C2.6792 10.0214 2.70944 9.91829 2.76632 9.82966C2.8232 9.74102 2.90433 9.67058 3.00007 9.62671L21.0001 3.12671Z"
              stroke="#36B368"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          Localización
        </RouterLink>
        <RouterLink
          to="/analysis"
          class="icon-text-link"
          :class="{ selected: $route.path === '/analysis' }"
        >
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M9 5H7C6.46957 5 5.96086 5.21071 5.58579 5.58579C5.21071 5.96086 5 6.46957 5 7V19C5 19.5304 5.21071 20.0391 5.58579 20.4142C5.96086 20.7893 6.46957 21 7 21H17C17.5304 21 18.0391 20.7893 18.4142 20.4142C18.7893 20.0391 19 19.5304 19 19V7C19 6.46957 18.7893 5.96086 18.4142 5.58579C18.0391 5.21071 17.5304 5 17 5H15M9 5C9 4.46957 9.21071 3.96086 9.58579 3.58579C9.96086 3.21071 10.4696 3 11 3H13C13.5304 3 14.0391 3.21071 14.4142 3.58579C14.7893 3.96086 15 4.46957 15 5M9 5C9 5.53043 9.21071 6.03914 9.58579 6.41421C9.96086 6.78929 10.4696 7 11 7H13C13.5304 7 14.0391 6.78929 14.4142 6.41421C14.7893 6.03914 15 5.53043 15 5M14 11H11.5C11.1022 11 10.7206 11.158 10.4393 11.4393C10.158 11.7206 10 12.1022 10 12.5C10 12.8978 10.158 13.2794 10.4393 13.5607C10.7206 13.842 11.1022 14 11.5 14H12.5C12.8978 14 13.2794 14.158 13.5607 14.4393C13.842 14.7206 14 15.1022 14 15.5C14 15.8978 13.842 16.2794 13.5607 16.5607C13.2794 16.842 12.8978 17 12.5 17H10M12 17V18M12 10V11"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          Análisis de precios
        </RouterLink>
        <RouterLink
          to="/tendency"
          class="icon-text-link"
          :class="{ selected: $route.path === '/tendency' }"
        >
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M3 17L9 11L13 15L21 7M21 7H14M21 7V14"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          Tendencias
        </RouterLink>
        <RouterLink
          to="/help"
          class="icon-text-link"
          :class="{ selected: $route.path === '/help' }"
        >
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M9.5 11H9.51M14.5 11H14.51M9.5 15C9.82588 15.3326 10.2148 15.5968 10.6441 15.7772C11.0734 15.9576 11.5344 16.0505 12 16.0505C12.4656 16.0505 12.9266 15.9576 13.3559 15.7772C13.7852 15.5968 14.1741 15.3326 14.5 15M7 5H8V3H16V5H17C17.7956 5 18.5587 5.31607 19.1213 5.87868C19.6839 6.44129 20 7.20435 20 8V17C20 17.7956 19.6839 18.5587 19.1213 19.1213C18.5587 19.6839 17.7956 20 17 20V21H7V20C6.20435 20 5.44129 19.6839 4.87868 19.1213C4.31607 18.5587 4 17.7956 4 17V8C4 7.20435 4.31607 6.44129 4.87868 5.87868C5.44129 5.31607 6.20435 5 7 5Z"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          Bot ayudante
        </RouterLink>
      </nav>
    </header>

    <RouterView />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

#principal {
  display: grid;
  grid-template-columns: 0.4fr 2fr;
  /* width: 100vw; */
  height: 100vh;
}

nav {
  display: flex;
  flex-direction: column;
}

.logo {
  justify-self: center;
  margin: 20px;
}

a,
.router-link {
  text-decoration: none;
  color: inherit;
}

.icon-text-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  margin-bottom: 20px;
  padding: 6px;
  gap: 10px;
}

.icon-text-link:hover {
  border-left: solid #36b368;
}

.selected {
  border-left: solid #36b368;
  color: #36b368;
  background-color: #f5f5f5;
}

.icon-text-link svg {
  margin-right: 8px;
}

.logo {
  display: flex; /* Configura el contenedor como un contenedor flexible */
  align-items: center; /* Alinea verticalmente los elementos */
  /* gap: 10px; */
}

.logo img {
  max-width: 100px; /* Ajusta el tamaño máximo de la imagen si es necesario */
  height: auto; /* Mantén la proporción de la imagen */
}

.logo span {
  font-size: 30px; /* Ajusta el tamaño del texto según sea necesario */
  font-weight: bold; /* Opcional: hace el texto más destacado */
  color: #333; /* Cambia el color del texto según tu diseño */
}
/*
.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
} */
</style>
