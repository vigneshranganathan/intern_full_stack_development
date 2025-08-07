<template>
  <div class="main-app-wrapper">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="navbar-left">
        <!-- Logo or app name can go here -->
      </div>
      <div class="navbar-center">
        <!-- Main Navigation Tabs -->
        <a 
          href="#" 
          class="nav-tab" 
          :class="{ 'active-main': activeMainTab === 'target' }" 
          @click.prevent="activeMainTab = 'target'"
        >
          TARGET
        </a>
        <a 
          href="#" 
          class="nav-tab" 
          :class="{ 'active-main': activeMainTab === 'investigation' }" 
          @click.prevent="activeMainTab = 'investigation'"
        >
          INVESTIGATION
        </a>
        <a 
          href="#" 
          class="nav-tab" 
          :class="{ 'active-main': activeMainTab === 'case' }" 
          @click.prevent="activeMainTab = 'case'"
        >
          CASE
        </a>
      </div>
      <div class="navbar-right">
        <!-- Admin text and icon -->
        <div class="admin-info">
          <span class="admin-text">Admin</span>
        </div>
        <!-- Time display -->
        <div class="time-display">{{ currentTime }}</div>
      </div>
    </nav>
    
    <div class="main-layout">
      <div class="main-content-area">
        <!-- Sub-Navbar for 'TARGET' tab -->
        <nav v-if="activeMainTab === 'target'" class="sub-navbar">
          <div class="sub-navbar-center">
            <a 
              href="#" 
              class="sub-nav-tab" 
              :class="{ 'active-sub': activeTargetTab === 'faceboard' }" 
              @click.prevent="activeTargetTab = 'faceboard'"
            >
              Faceboard
            </a>
            <a 
              href="#" 
              class="sub-nav-tab" 
              :class="{ 'active-sub': activeTargetTab === 'album' }" 
              @click.prevent="activeTargetTab = 'album'"
            >
              Album
            </a>
          </div>
        </nav>

        <!-- Dynamic Content for Left Panel -->
        <div class="content-panel">
          <div v-if="activeMainTab === 'target'">
            <FaceBoard v-if="activeTargetTab === 'faceboard'" />
            <Album v-if="activeTargetTab === 'album'" />
          </div>
          <div v-else-if="activeMainTab === 'investigation'">
            <Investigation />
          </div>
          <div v-else-if="activeMainTab === 'case'">
            <Case />
          </div>
          <div v-else class="welcome-message">
            <h1>Welcome to the {{ activeMainTab }} section!</h1>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import FaceBoard from '../components/FaceBoard.vue';
import Album from '../components/Album.vue';
import Investigation from '../components/Investigation.vue';
import Case from '../components/Case.vue';

const activeMainTab = ref('target');
const activeTargetTab = ref('faceboard');
const currentTime = ref('');
let timerId = null;

// Function to update the time
const updateTime = () => {
  const now = new Date();
  const options = { weekday: 'short', month: 'short', day: 'numeric' };
  const dateStr = now.toLocaleDateString('en-US', options);
  const timeStr = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: true });
  currentTime.value = `${dateStr} ${timeStr}`;
};

onMounted(() => {
  // Update time immediately and then every second
  updateTime();
  timerId = setInterval(updateTime, 1000);
});

onUnmounted(() => {
  // Clear the interval when the component is unmounted
  clearInterval(timerId);
});
</script>

<style scoped>
.main-app-wrapper {
  height: 100vh;
  background-color: #1a1a1a;
  color: white;
  font-family: 'Segoe UI', sans-serif;
  display: flex;
  flex-direction: column;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #2c2c2c;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

.main-layout {
  display: grid;

  height: calc(100vh - 4.5rem);
  gap: 1rem;
  padding: 1rem;
}

.main-content-area {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sub-navbar {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.5rem 2rem;
  background-color: #383838;
  border-bottom: 2px solid #007bff;
}

.sub-navbar-center {
  display: flex;
  gap: 1.5rem;
}

.navbar-center {
  display: flex;
  gap: 2rem;
}

.nav-tab {
  color: #888;
  text-decoration: none;
  font-weight: bold;
  padding: 0.5rem 1rem;
  transition: all 0.3s ease;
}

.nav-tab:hover {
  color: white;
}

.nav-tab.active-main {
  color: #007bff;
  border-bottom: 2px solid #007bff;
}

.sub-nav-tab {
  color: #888;
  text-decoration: none;
  font-weight: bold;
  padding: 0.5rem 1rem;
  transition: all 0.3s ease;
}

.sub-nav-tab:hover {
  color: white;
}

.sub-nav-tab.active-sub {
  color: white;
  background-color: #007bff;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.admin-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.admin-text {
  font-weight: bold;
}

.admin-icon {
  font-size: 1.5rem;
}

.time-display {
  font-size: 0.8rem;
  color: #aaa;
}

.content-panel {
  flex-grow: 1;
  background-color: #2c2c2c;
  border-radius: 8px;
  padding: 1rem;
}

.welcome-message {
  padding: 2rem;
  text-align: center;
}
</style>
