<!-- <script setup lang="ts">
import { ref, computed } from 'vue'
import ProductCard from '../components/Card.vue'

const products = ref([
  {
    item: 'azucar',
    price: 340.0,
    coordinates: { lat: 33.749, lng: -84.388 },
    municipality: '10 de octubre, Lawton',
    tendency: 23,
  },
  {
    item: 'pollo',
    price: 100.5,
    coordinates: { lat: 25.7617, lng: -80.1918 },
    municipality: 'La Habana, Cuba',
    tendency: -12,
  },
])

const selectedProduct = ref(null)
const productLooking = ref('')
const filteredProduct = ref(products.value)

const iframeUrl = ref(
  'https://tablero-qtal.avangenio.com/d-solo/fe65dynep23nke/productos?orgId=1&from=1730433600000&to=1735707599000&panelId=2',
)

const productsToDisplay = computed(() => {
  return filteredProduct.value
})

const selectProduct = (product: any) => {
  selectedProduct.value = product
  iframeUrl.value = `https://tablero-qtal.avangenio.com/d-solo/fe65dynep23nke/productos?orgId=1&from=1730433600000&to=1735707599000&panelId=2&var-Producto=${product.item}`
}

const searchProduct = () => {
  if (!productLooking.value.trim().length) {
    filteredProduct.value = [...products.value]
  } else {
    const results = products.value.filter(product =>
      product.item.toLowerCase().includes(productLooking.value.toLowerCase()),
    )
    filteredProduct.value = results
  }
}

const loading = ref(true)

setTimeout(() => {
  loading.value = false
}, 1000)
</script> -->

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import ProductCard from '../components/Card.vue'

const products = ref([])
const filteredProduct = ref([])
const selectedProduct = ref(null)
const productLooking = ref('')
const loading = ref(true)

const iframeUrl = ref(
  'https://tablero-qtal.avangenio.com/d-solo/fe65dynep23nke/productos?orgId=1&from=1730433600000&to=1735707599000&panelId=2&var-Producto= ',
)

const fetchProducts = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/words')
    if (!response.ok) {
      throw new Error('Error al obtener los productos')
    }
    const data = await response.json()
    // Transformamos los datos al formato esperado
    products.value = data.map(item => ({
      item: item.word,
      price: item.avg,
      coordinates: { lat: 0, lng: 0 },
      municipality: 'Sin municipio',
      tendency: item.trend,
    }))
    filteredProduct.value = [...products.value]
  } catch (error) {
    console.error('Error al cargar los productos:', error)
  } finally {
    loading.value = false
  }
}

const productsToDisplay = computed(() => {
  return filteredProduct.value
})

const selectProduct = (product: any) => {
  selectedProduct.value = product
  iframeUrl.value = `https://tablero-qtal.avangenio.com/d-solo/fe65dynep23nke/productos?orgId=1&from=1730433600000&to=1735707599000&panelId=2&var-Producto=${product.item}`
}

const searchProduct = () => {
  if (!productLooking.value.trim().length) {
    filteredProduct.value = [...products.value]
  } else {
    const results = products.value.filter(product =>
      product.item.toLowerCase().includes(productLooking.value.toLowerCase()),
    )
    filteredProduct.value = results
  }
}

// Llamamos a `fetchProducts` al montar el componente
onMounted(() => {
  fetchProducts()
})
</script>

<template>
  <main>
    <section v-if="loading" class="loading-section">
      <h2>Cargando productos...</h2>
    </section>
    <section v-else>
      <h2>
        Cantidad <br />de productos:
        {{ filteredProduct.length }}
      </h2>
      <div id="filtrar-section">
        <div class="card flex justify-center">
          <input
            v-model="productLooking"
            @input="searchProduct"
            placeholder="🔍 producto..."
            class="search-input"
          />
        </div>
      </div>
      <div class="product-list">
        <div v-if="filteredProduct.length > 0">
          <ProductCard
            v-for="(product, index) in productsToDisplay"
            :key="index"
            :item="product.item"
            :price="product.price"
            :coordinates="product.coordinates"
            :municipality="product.municipality"
            :tendency="product.tendency"
            :class="{ 'selected-card': selectedProduct === product }"
            @click="selectProduct(product)"
          />
        </div>

        <div v-else class="no-results">No se encontraron coincidencias</div>
      </div>
    </section>
    <section id="map-section">
      <iframe
        :src="iframeUrl"
        width="100%"
        height="100%"
        frameborder="0"
      ></iframe>
    </section>
  </main>
</template>

<style scoped>
main {
  display: grid;
  grid-template-columns: 0.7fr 2fr;
  background-color: #f5f5f5;
  padding: 10px 20px;
  /* border-radius: 37px 0 0 37px; */
}

#map-section {
  margin-left: 3%;
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.4);
}

#filtrar-section {
  margin: 10% 0;
  justify-content: space-between;
}

.search-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.product-list {
  overflow-x: auto;
  overflow-y: hidden;
  padding-bottom: 16px;
}

.filter-button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.filter-button:hover {
  background-color: #45a049;
}

.selected-card {
  border-left: 4px solid #4caf50;
  border-radius: 8px;
  /* background-color: #e8f5e9; */
  transition: 0.3s ease-in-out;
}

.no-results {
  text-align: center;
  color: #888;
  margin-top: 20px;
  font-style: italic;
}
</style>
