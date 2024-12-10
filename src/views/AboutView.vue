<template>
  <div class="analisys-section">
    <h1>Análisis de precios</h1>
    <div class="graphs-analisys">
      <div class="graph g-first">
        <iframe
          src="https://tablero-qtal.avangenio.com/d-solo/fe65dynep23nke/productos?orgId=1&from=1730433600000&to=1735707599000&panelId=3"
          width="100%"
          height="400"
          frameborder="0"
        ></iframe>
      </div>
      <div class="graph g-second">
        <iframe
          src="https://tablero-qtal.avangenio.com/d-solo/fe65dynep23nke/productos?orgId=1&from=1730433600000&to=1735707599000&panelId=4"
          width="100%"
          height="400"
          frameborder="0"
        ></iframe>
      </div>
    </div>
  </div>
</template>

<style>
/* @media (min-width: 1024px) { */
.analisys-section {
  background-color: #f5f5f5;
  padding: 10px 20px;
  height: 100%;
}

.graphs-analisys {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  /* grid-template-areas: 'first second'; */
  gap: 10px;
  justify-content: center;
  align-items: center;
}

/* .g-first {
  grid-area: 'first';
}

.g-second {
  grid-area: 'second';
} */

.graph {
  padding: 5px;
}
/* } */
</style>
