<script setup lang="ts">
import { ref, reactive } from 'vue'

const iframeUrl = ref(
  'https://tablero-qtal.avangenio.com/d-solo/fe65dynep23nke/productos?orgId=1&from=1730433600000&to=1735707599000&panelId=2&var-Producto= ',
)

// Predefined list of provinces (you can expand this)
const provinces = [
  'Pinar del Río',
  'Artemisa',
  'La Habana',
  'Mayabeque',
  'Matanzas',
  'Cienfuegos',
  'Villa Clara',
  'Sancti Spíritus',
  'Ciego de Ávila',
  'Camagüey',
  'Las Tunas',
  'Holguín',
  'Granma',
  'Santiago de Cuba',
  'Guantánamo',
  'Isla de la Juventud',
]

const productForm = reactive({
  name: '',
  details: '',
  price: null,
  priceUnit: 'unitario', // Default value
  province: '', // New province field
  municipality: '', // New municipality field
  location: '',
})

const submitProduct = () => {
  // Here you would typically handle form submission
  // For example, send data to an API or store
  console.log('Product submitted:', productForm)

  // Optional: Reset form after submission
  productForm.name = ''
  productForm.details = ''
  productForm.price = null
  productForm.priceUnit = 'unitario'
  productForm.province = ''
  productForm.municipality = ''
  productForm.location = ''
}
</script>

<template>
  <div class="analisys-section">
    <h1>Anunciate con nosotros!</h1>
    <div class="product-form-container">
      <form @submit.prevent="submitProduct" class="product-form">
        <div class="form-group">
          <label for="name">Nombre del Producto</label>
          <input
            id="name"
            v-model="productForm.name"
            type="text"
            required
            placeholder="Ingrese nombre del producto"
          />
        </div>

        <!-- <div class="form-group">
          <label for="details">Detalles</label>
          <textarea
            id="details"
            v-model="productForm.details"
            required
            placeholder="Describa los detalles del producto"
          ></textarea>
        </div> -->

        <div class="form-group">
          <label for="price">Precio</label>
          <div class="price-container">
            <input
              id="price"
              v-model.number="productForm.price"
              type="number"
              required
              placeholder="Ingrese el precio"
              class="price-input"
            />
            <div class="price-unit-selection">
              <label class="price-unit-option">
                <input
                  type="radio"
                  v-model="productForm.priceUnit"
                  value="unitario"
                />
                Unitario
              </label>
              <label class="price-unit-option">
                <input
                  type="radio"
                  v-model="productForm.priceUnit"
                  value="lb"
                />
                Lb
              </label>
              <label class="price-unit-option">
                <input
                  type="radio"
                  v-model="productForm.priceUnit"
                  value="kg"
                />
                Kg
              </label>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="province">Provincia</label>
          <select id="province" v-model="productForm.province" required>
            <option value="" disabled>Seleccione una provincia</option>
            <option
              v-for="provinceName in provinces"
              :key="provinceName"
              :value="provinceName"
            >
              {{ provinceName }}
            </option>
          </select>
        </div>

        <div class="form-group">
          <label for="municipality">Municipio</label>
          <input
            id="municipality"
            v-model="productForm.municipality"
            type="text"
            required
            placeholder="Ingrese el municipio"
          />
        </div>

        <div class="graphs-analisys">
          <section id="map-section">
            <h3>Selecciona la ubicación</h3>
            <iframe
              :src="iframeUrl"
              width="100%"
              height="300"
              frameborder="0"
            ></iframe>
          </section>
        </div>
        <button type="submit" class="submit-btn">Publicar Producto</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.analisys-section {
  background-color: #f5f5f5;
  padding: 10px 20px;
  height: 100%;
  /* min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-repeat: no-repeat;
  /* background-size: cover; */
  /* background-position: center; */
}

.product-form-container {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.product-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group input,
.form-group textarea {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.price-container {
  display: flex;
  /* flex-direction: column; */
  gap: 10px;
}

.price-input {
  width: 100%;
}

.price-unit-selection {
  display: flex;
  justify-content: space-between;
  gap: 10px;
}

.price-unit-option {
  display: flex;
  align-items: center;
  gap: 5px;
}

.price-unit-option input[type='radio'] {
  margin: 0;
}

.submit-btn {
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #45a049;
}

.form-group select {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: white;
}
</style>
