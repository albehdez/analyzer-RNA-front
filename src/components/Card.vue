<template>
  <div
    class="status-card"
    :class="{ 'selected-card': selected }"
    @click="$emit('select')"
  >
    <div class="header">
      <span class="item-name">{{ item === 'azucar' ? 'azúcar' : item }}</span>
    </div>
    <div class="details">
      <span class="price">
        Precio promedio: ${{ price }}
        <br />
        <span v-if="tendency !== undefined" :class="tendencyClass">
          <span class="tendency-icon">{{ tendencyIcon }}</span>
          {{ Math.abs(tendency) }}%
        </span>
      </span>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from 'vue'

export default defineComponent({
  name: 'ProductCard',
  props: {
    item: String,
    price: Number,
    tendency: {
      type: Number,
      default: undefined,
    },
    selected: Boolean,
  },
  setup(props) {
    const tendencyClass = computed(() => ({
      'tendency-positive': props.tendency < 0,
      'tendency-negative': props.tendency > 0,
      'tendency-neutral': props.tendency === 0,
    }))

    const tendencyIcon = computed(() => {
      if (props.tendency > 0) return '▲'
      if (props.tendency < 0) return '▼'
      return '-'
    })

    return {
      tendencyClass,
      tendencyIcon,
    }
  },
})
</script>

<style scoped>
.status-card {
  justify-items: center;
  background-color: #fff;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: box-shadow 0.3s;
}

.status-card:hover {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
}

.selected-card {
  border-left: solid 4px green;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.item-name {
  font-weight: bold;
  font-size: 1.2rem;
}

.details {
  margin-top: 12px;
  font-size: 1rem;
  text-align: center;
}

.price {
  color: #555;
}

.tendency-positive {
  color: green;
}

.tendency-negative {
  color: red;
}

.tendency-neutral {
  color: blue;
}

.tendency-icon {
  margin-right: 4px;
  font-size: 0.8em;
}
</style>
