<template>
  <div class="album-content-container">
    <div class="album-header">
      <h2 class="album-title">Album</h2>
      <button class="upload-btn">Upload</button>
    </div>
    
    <div class="album-grid">
      <div v-for="(album, index) in albums" :key="index" class="album-card">
        <div class="card-header">
          <span class="card-title">{{ album.name }}</span>
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: album.progress + '%', backgroundColor: getProgressColor(album.progress) }"></div>
          </div>
        </div>
        <div class="card-body">
          <div class="image-container">
            <img v-if="album.image" :src="album.image" :alt="album.name" class="album-image">
            <div v-else class="placeholder-image">
              <i class="image-icon">🖼️</i>
            </div>
          </div>
          <div class="card-details">
            <span class="card-name">{{ album.name }}</span>
            <div class="card-actions">
              <button class="card-action-btn">Edit</button>
              <button class="card-action-btn">View</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Define the album data
const albums = ref([
  {
    name: 'Employee',
    progress: 100,
    image: 'https://imgs.search.brave.com/Hxn7Q4rRPNp2e065q7HGOno6rA3-08NLiX0oh2rOYmc/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zMy5p/bmRpYS5jb20vd3At/Y29udGVudC91cGxv/YWRzLzIwMjQvMDgv/a29sa2F0YS1yYXBl/LWFjY3VzZWQuanBn/P2ltcG9saWN5PU1l/ZGl1bV9XaWR0aG9u/bHkmdz0zMjA'
  },
  {
    name: 'Album 6',
    progress: 95,
    image: 'https://imgs.search.brave.com/v_JGODOfaM97xSzBHXx2chrdu4ABZf4TSpzdEKvSjkM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTM4/NzE5MzI3My9waG90/by9hZHVsdC1mZW1h/bGUtc2VjdXJpdHkt/d29ya2VyLXRhbGtp/bmctb24tc21hcnQt/cGhvbmUtd2hpbGUt/bG9va2luZy1hdC1j/b21wdXRlci1tb25p/dG9ycy5qcGc_cz02/MTJ4NjEyJnc9MCZr/PTIwJmM9MUdySi1F/RnF4WGJEZzg0VHI5/TGpRMmQwczluNVRm/NnBpVFZWYkxEek1j/bz0'
  }
]);

// Function to get a color based on progress percentage
const getProgressColor = (progress) => {
  if (progress > 75) {
    return '#4CAF50'; // Green
  } else if (progress > 50) {
    return '#FFC107'; // Yellow
  } else {
    return '#F44336'; // Red
  }
};
</script>

<style scoped>
.album-content-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  height: 100%;
}

.album-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 1rem;
  border-bottom: 1px solid #4a4a4a;
}

.album-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.upload-btn {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.3s ease;
}

.upload-btn:hover {
  background-color: #0056b3;
}

.album-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1rem;
  flex-grow: 1;
  overflow-y: auto;
}

.album-card {
  background-color: #363636;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.card-header {
  padding: 1rem;
  background-color: #4a4a4a;
  border-bottom: 1px solid #5a5a5a;
}

.card-title {
  font-weight: bold;
  font-size: 1.1rem;
}

.progress-bar {
  height: 8px;
  background-color: #666;
  border-radius: 4px;
  margin-top: 0.5rem;
}

.progress-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 0.3s ease;
}

.card-body {
  padding: 1rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.image-container {
  width: 100px;
  height: 100px;
  background-color: #555;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}

.album-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.placeholder-image {
  font-size: 3rem;
  color: #aaa;
}

.card-details {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 1rem;
}

.card-name {
  font-size: 1rem;
  font-weight: bold;
}

.card-actions {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.card-action-btn {
  padding: 0.25rem 0.75rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: bold;
  transition: background 0.3s ease;
}

.card-action-btn:hover {
  background-color: #0056b3;
}
</style>
