<script setup lang="ts">
import ChatBot from '../components/ChatBot.vue'
</script>

<template>
  <div class="help-section">
    <h1>¿Necesitas ayuda para tus compras?</h1>

    <div class="chatbot-wrapper">
      <ChatBot />
    </div>
  </div>
</template>

<style>
.help-section {
  background-color: #f5f5f5;
  padding: 10px 20px;
  min-height: 100vh;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-image: url('../../public/Group\ 7.png');
  background-repeat: no-repeat;
  /* background-size: cover; */
  background-position: center;
}

.chatbot-wrapper {
  bottom: 0;
  left: 0;
  /* width: 100%; */
  padding: 10px;
  z-index: 1000;
  align-self: center;
  width: 90%;
}
</style>
