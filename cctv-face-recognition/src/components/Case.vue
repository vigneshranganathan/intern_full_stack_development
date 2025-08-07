<template>
  <div class="case-content-container">
    <!-- Header -->
    <div class="case-header">
      <div class="search-section">
        <input type="text" placeholder="Search" class="search-input" />
      </div>
      <div class="filter-buttons">
        <a href="#" :class="{ active: activeFilter === 'all' }" @click.prevent="activeFilter = 'all'">All</a>
        <a href="#" :class="{ active: activeFilter === 'day' }" @click.prevent="activeFilter = 'day'">In a day</a>
        <a href="#" :class="{ active: activeFilter === 'week' }" @click.prevent="activeFilter = 'week'">In a week</a>
        <a href="#" :class="{ active: activeFilter === 'month' }" @click.prevent="activeFilter = 'month'">In a month</a>
        <a href="#" :class="{ active: activeFilter === 'custom' }" @click.prevent="activeFilter = 'custom'">Custom</a>
      </div>
    </div>

    <!-- Table Header -->
    <div class="case-list">
      <div class="case-list-header">
        <span class="header-col">Target</span>
        <span class="header-col">Time</span>
        <span class="header-col">Case Name</span>
        <span class="header-col">Description</span>
        <span class="header-col">By User</span>
        <span class="header-col">Actions</span>
      </div>

      <!-- Rows -->
      <div v-for="(caseItem, index) in cases" :key="index" class="case-card">
        <div class="case-image-container">
          <img :src="caseItem.image" alt="Case Image" class="case-card-image" />
        </div>
        <span class="detail-label">{{ caseItem.time }}</span>
        <span class="detail-label">{{ caseItem.caseName }}</span>
        <span class="detail-label">{{ caseItem.description }}</span>
        <span class="detail-label">{{ caseItem.byUser }}</span>
        <div class="case-actions">
          <!-- Save Button -->
          <button class="action-btn">
            <img src="/icons/save-icon.png" alt="Save" class="action-icon" />
          </button>
          <!-- Delete Button -->
          <button class="action-btn delete-btn">
            <img src="/icons/delete-icon.png" alt="Delete" class="action-icon" />
          </button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="case-footer">
      <p class="footer-message">please remember to download case manually because video archive could be expired.</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeFilter = ref('all')

const cases = ref([
  {
    image: 'https://placehold.co/50x50/363636/E0E0E0?text=Face',
    time: '14 Mar 2025 18:53:58',
    caseName: 'Case-14032025-1859',
    description: 'Admin',
    byUser: 'Admin'
  },
  {
    image: 'https://placehold.co/50x50/363636/E0E0E0?text=Face',
    time: '14 Mar 2025 18:54:22',
    caseName: 'Case-14032025-1900',
    description: 'Admin',
    byUser: 'Admin'
  },
  {
    image: 'https://placehold.co/50x50/363636/E0E0E0?text=Face',
    time: '14 Mar 2025 19:02:10',
    caseName: 'Case-14032025-1903',
    description: 'Admin',
    byUser: 'Admin'
  },
  {
    image: 'https://placehold.co/50x50/363636/E0E0E0?text=Face',
    time: '14 Mar 2025 19:06:18',
    caseName: 'Case-14032025-1907',
    description: 'Admin',
    byUser: 'Admin'
  }
])
</script>

<style scoped>
.case-content-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  height: 100%;
  color: white;
}

.case-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.search-section {
  flex-grow: 1;
  max-width: 300px;
}

.search-input {
  width: 100%;
  background-color: #383838;
  color: white;
  border: 1px solid #555;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  outline: none;
}

.filter-buttons {
  display: flex;
  background-color: #383838;
  border-radius: 8px;
  overflow: hidden;
}

.filter-buttons a {
  padding: 0.5rem 1rem;
  text-decoration: none;
  color: #ccc;
  font-weight: bold;
  transition: all 0.3s ease;
  border-right: 1px solid #4a4a4a;
}

.filter-buttons a:last-child {
  border-right: none;
}

.filter-buttons a:hover {
  background-color: #4a4a4a;
}

.filter-buttons a.active {
  background-color: #007bff;
  color: white;
}

.case-list {
  flex-grow: 1;
  overflow-y: auto;
  border-radius: 8px;
  background-color: #2c2c2c;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

.case-list-header,
.case-card {
  display: grid;
  grid-template-columns: 80px 180px 1fr 1fr 100px 80px;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #4a4a4a;
}

.case-card:last-child {
  border-bottom: none;
}

.header-col,
.detail-label {
  font-size: 0.9rem;
  color: #ccc;
}

.case-image-container {
  width: 50px;
  height: 50px;
  overflow: hidden;
  border-radius: 4px;
}

.case-card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.case-actions {
  display: flex;
  justify-content: flex-start;
  gap: 0.5rem;
}

.action-btn {
  width: 32px;
  height: 32px;
  background-color: #383838;
  border: 1px solid #777;
  border-radius: 6px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 4px;
  cursor: pointer;
}

.action-btn:hover {
  background-color: #4a4a4a;
}

.delete-btn {
  background-color: #F44336;
  border: none;
}

.delete-btn:hover {
  background-color: #d32f2f;
}

.action-icon {
  width: 16px;
  height: 16px;
  pointer-events: none;
}

.case-footer {
  text-align: center;
  margin-top: 1rem;
}

.footer-message {
  font-size: 0.8rem;
  color: #aaa;
}
</style>
