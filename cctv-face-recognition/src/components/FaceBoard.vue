<template>
  <div class="faceboard-content">
    <div class="layout-container">
      <!-- Left side: selectors, timeline, and main content area -->
      <div class="left-panel">
        <div class="header-panel">
          <div class="selectors">
            <div class="selector-group">
              <span class="label">Time</span>
              <select class="selector-input">
                <option>Now</option>
              </select>
            </div>
            <div class="selector-group">
              <span class="label">Camera</span>
              <select class="selector-input">
                <option>All</option>
              </select>
            </div>
            <div class="selector-group">
              <span class="label">Album</span>
              <select class="selector-input">
                <option>All</option>
              </select>
            </div>
          </div>
          <div class="timeline-container">
            <div class="timeline-arrows">
              <i class="timeline-arrow" @click="moveTimelineMarker(-1)">◀</i>
            </div>
            <div class="timeline">
              <div class="timeline-bar">
                <div class="timeline-marker" :style="markerStyle">
                  <div class="marker-content">{{ currentHour }}</div>
                </div>
              </div>
              <div class="timeline-hours">
                <span v-for="hour in 24" :key="hour">{{ hour - 1 }}</span>
              </div>
            </div>
            <div class="timeline-arrows">
              <i class="timeline-arrow" @click="moveTimelineMarker(1)">▶</i>
            </div>
          </div>
        </div>
        <div class="main-content">
          <!-- Placeholder for the main content area -->
          <div class="placeholder-box"></div>
        </div>
      </div>
      
      <!-- Right side: sidebar -->
      <div class="right-sidebar">
        <p>Please select one face from the wall. Then, select one of the faces filled in this panel to start investigation.</p>
        <div class="button-group">
          <button class="action-btn">Investigation</button>
          <button class="action-btn">Add to Album</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// Reactive state to hold the current hour, starting at 12
const currentHour = ref(12);

// Computed property to dynamically calculate the marker's position
const markerStyle = computed(() => {
  // Calculate the percentage of the timeline the marker should be at
  // (current hour / total hours) * 100
  // Note: Total hours is 23 (0-23)
  const position = (currentHour.value / 23) * 100;
  return {
    left: `calc(${position}%)`
  };
});

// Function to move the timeline marker left or right
const moveTimelineMarker = (direction) => {
  const newHour = currentHour.value + direction;
  // Ensure the hour stays within the 0-23 range
  if (newHour >= 0 && newHour <= 23) {
    currentHour.value = newHour;
  }
};
</script>

<style scoped>
.faceboard-content {
  background-color: #1a1a1a;
  padding: 1rem;
  height: calc(100vh - 12rem); /* Adjust height to fit within the main layout */
}

.layout-container {
  display: grid;
  grid-template-columns: 1fr 300px; /* Main content takes 1fr, sidebar is fixed width */
  gap: 1rem;
  height: 100%;
}

.left-panel {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.header-panel {
  display: flex;
  flex-direction: column;
  background-color: #2c2c2c;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

.selectors {
  display: flex;
  gap: 2rem;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}

.selector-group {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.label {
  font-size: 0.9rem;
  color: #ccc;
}

.selector-input {
  background-color: #4a4a4a;
  color: white;
  border: 1px solid #555;
  border-radius: 4px;
  padding: 0.25rem 0.5rem;
  outline: none;
}

.timeline-container {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.timeline-arrows {
  font-size: 1.5rem;
  cursor: pointer;
  color: #ccc;
}

.timeline {
  flex-grow: 1;
  position: relative;
  height: 5rem; /* Adjusted height to be smaller */
  background-color: #4a4a4a;
  border-radius: 4px;
}

.timeline-bar {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 0;
  right: 0;
  height: 4px;
  background-color: #666;
}

.timeline-marker {
  position: absolute;
  top: 50%; /* Center vertically */
  transform: translate(-50%, -50%); /* Center horizontally and vertically */
  width: 3rem;
  height: 5rem;
  background-color: transparent; /* Changed from blue to transparent */
  border: 1px solid white;
  border-radius: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.marker-content {
  color: white;
  font-size: 0.8rem;
  line-height: 1; /* Ensures single line height */
}

.timeline-hours {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: #aaa;
  padding-top: 0.5rem;
}

.main-content {
  flex-grow: 1;
  background-color: #2c2c2c;
  border-radius: 8px;
  padding: 1rem;
}

.placeholder-box {
  background-color: #4a4a4a;
  height: 100%;
  min-height: 200px;
}

.right-sidebar {
  background-color: #2c2c2c;
  border-radius: 8px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.button-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.action-btn {
  width: 100%;
  padding: 0.5rem;
  background-color: #007bff;
  border: none;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}
</style>
