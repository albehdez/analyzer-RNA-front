<template>
  <div class="chatbot-container">
    <div class="chatbot-messages">
      <!-- Aquí se pueden mostrar mensajes previos del chatbot -->
      <p class="bot-message">Hola, ¿en qué puedo ayudarte hoy?</p>
    </div>
    <div class="chatbot-input">
      <input
        type="text"
        placeholder="Escribe tu mensaje..."
        class="chat-input"
        v-model="userMessage"
        @keydown.enter="sendMessage"
      />
      <button class="send-button" @click="sendMessage">Enviar</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const userMessage = ref('')

const sendMessage = () => {
  if (userMessage.value.trim()) {
    console.log('Mensaje enviado:', userMessage.value)
    userMessage.value = '' // Limpiar el campo de texto
  }
}
</script>

<style scoped>
.chatbot-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  margin-top: auto;
  background: #ffffff;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.chatbot-messages {
  flex-grow: 1;
  overflow-y: auto;
  max-height: 300px;
  margin-bottom: 10px;
  padding: 10px;
  background: #f9f9f9;
  border-radius: 5px;
}

.bot-message {
  background-color: #e6e6e6;
  color: #333;
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  max-width: 80%;
}

.chatbot-input {
  display: flex;
  gap: 10px;
}

.chat-input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.send-button {
  background-color: #36b368;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.send-button:hover {
  background-color: #309e5c;
}
</style>
