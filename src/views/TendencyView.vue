<template>
  <div class="tendency-section">
    <h1>Tendencias</h1>
    <div class="graphs-tendency">
      <div class="graph g-third">
        <iframe
          src="https://tablero-qtal.avangenio.com/d-solo/fe65dynep23nke/productos?orgId=1&from=1730433600000&to=1735707599000&panelId=1"
          width="100%"
          height="400"
          frameborder="0"
        ></iframe>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* @media (min-width: 1024px) { */
.tendency-section {
  background-color: #f5f5f5;
  padding: 10px 20px;
  height: 100%;
}

.graphs {
  /* display: grid; */
  /* grid-template-areas: 'first second'; */
  /* gap: 10px; */
  justify-content: center;
  align-items: center;
}

/* .g-first {
    grid-area: first;
  }

  .g-second {
    grid-area: second;
  } */

/* .g-third {
    grid-area: third;
  } */

.graph {
  padding: 5px;
}
/* } */
</style>
