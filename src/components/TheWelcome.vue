<template>
  <!-- <h2>Cantidad de productos {{ cantProduct }}</h2> -->
  <div id="filtrar-section">
    <div class="card flex justify-center">
      <AutoComplete
        v-model="selectedProduct"
        optionLabel="product"
        :suggestions="filteredProduct"
        @complete="search"
      />
    </div>
    <div class="card flex justify-center">
      <Button label="Filtrar" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
// import { ProductService } from '@/service/ProductService'
const products = ref([])
onMounted(() => {
  products.value = ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4']
})


// const countries = ref()
const selectedProduct = ref()
const filteredProduct = ref()

const search = event => {
  setTimeout(() => {
    if (!event.query.trim().length) {
      filteredProduct.value = [...products.value]
    } else {
      filteredProduct.value = products.value.filter(product => {
        return product.name.toLowerCase().startsWith(event.query.toLowerCase())
      })
    }
  }, 250)
}
</script>

<style scoped>
#filtrar-section {
  display: flex;
}
</style>
