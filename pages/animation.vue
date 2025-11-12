<template>
  <div class="scene">
    <div class="sun"></div>
    <div class="sky"></div>
    <div v-for="i in 50" :key="`particle-${i}`" class="particle" :style="particleStyle(i)"></div>
    <div class="city">
      <div class="building" v-for="i in 10" :key="`bldg-${i}`" :style="buildingStyle(i)">
        <div class="window" v-for="j in 15" :key="`wndw-${j}`" :style="windowStyle(j)"></div>
      </div>
    </div>
    <div class="stage">
      <div class="character feng-xiong">
        <div class="head">
          <div class="eye left"></div>
          <div class="eye right"></div>
          <div class="mouth"></div>
        </div>
        <div class="body"></div>
        <div class="speech-bubble">-___-</div>
      </div>
      <div class="character tu-ge">
        <div class="head">
          <div class="eye left"></div>
          <div class="eye right"></div>
          <div class="mouth open"></div>
        </div>
        <div class="body singing"></div>
        <div class="music-note">♪ ムリムリ! ♪</div>
      </div>
      <div class="crowd">
        <div class="person" v-for="i in 5" :key="`person-${i}`">
          <div class="flag"></div>
        </div>
      </div>
    </div>
    <div class="ai-screen">
      <p>市長進化中...</p>
      <div class="progress-bar"></div>
    </div>
    <div class="final-text">台北有鋒兄真好！</div>
    <div class="ballots">
      <div class="ballot" v-for="i in 10" :key="`ballot-${i}`" :style="ballotStyle(i)"></div>
    </div>
  </div>
</template>

<script setup>
const particleStyle = (i) => {
  const size = Math.random() * 5 + 2;
  return {
    width: `${size}px`,
    height: `${size}px`,
    left: `${Math.random() * 100}vw`,
    top: `${Math.random() * 100}vh`,
    animationDuration: `${Math.random() * 10 + 5}s`,
    animationDelay: `${Math.random() * 5}s`,
  };
};

const buildingStyle = (i) => {
  return {
    height: `${Math.random() * 200 + 100}px`,
    width: `${Math.random() * 50 + 40}px`,
    left: `${i * 9 - 5}vw`,
    backgroundColor: `hsl(210, 15%, ${Math.random() * 10 + 25}%)`,
    animationDelay: `${i * 0.1}s`
  };
};

const windowStyle = (j) => {
  return {
    backgroundColor: Math.random() > 0.3 ? '#f7f7a1' : '#4c5a6e',
    animationDelay: `${Math.random() * 5}s`
  };
}

const ballotStyle = (i) => {
  return {
    left: `${Math.random() * 100}vw`,
    animationDuration: `${Math.random() * 3 + 2}s`,
    animationDelay: `${Math.random() * 3}s`,
  }
}
</script>

<style scoped>
.scene {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  position: relative;
  background: linear-gradient(to bottom, #87CEEB 0%, #FFB6C1 60%, #4a4a88 100%);
  font-family: 'Helvetica Neue', 'Arial', 'sans-serif';
}

.sky {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.sun {
    position: absolute;
    top: 10%;
    left: 15%;
    width: 100px;
    height: 100px;
    background: #FFD700;
    border-radius: 50%;
    box-shadow: 0 0 50px #FFD700, 0 0 100px #FFD700;
}

.particle {
  position: absolute;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 50%;
  animation: float 10s infinite ease-in-out;
  box-shadow: 0 0 5px white;
}

@keyframes float {
  0% { transform: translateY(0); opacity: 0.8; }
  50% { transform: translateY(-50px); opacity: 1; }
  100% { transform: translateY(-100px); opacity: 0; }
}

.city {
  position: absolute;
  bottom: 0;
  width: 100%;
  display: flex;
  justify-content: space-around;
  align-items: flex-end;
}

.building {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  padding: 5px;
  gap: 5px;
  animation: riseUp 1s ease-out forwards;
  opacity: 0;
  transform: translateY(100%);
}

@keyframes riseUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.window {
  width: 8px;
  height: 12px;
  animation: flicker 5s infinite;
}

@keyframes flicker {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}

.stage {
  position: absolute;
  bottom: 10%;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: flex-end;
  z-index: 10;
}

.character {
  position: relative;
  margin: 0 40px;
  animation: bounceIn 1.5s 1s ease-out forwards;
  opacity: 0;
  transform: scale(0.5);
}

@keyframes bounceIn {
    0% { transform: scale(0.5); opacity: 0; }
    60% { transform: scale(1.1); }
    100% { transform: scale(1); opacity: 1; }
}


.head {
  width: 60px;
  height: 60px;
  background-color: #f2d3b3;
  border-radius: 50%;
  position: relative;
  border: 2px solid #555;
}

.eye {
  width: 8px;
  height: 8px;
  background: #333;
  border-radius: 50%;
  position: absolute;
  top: 25px;
}
.eye.left { left: 15px; }
.eye.right { right: 15px; }

.mouth {
  width: 20px;
  height: 2px;
  background: #333;
  position: absolute;
  bottom: 15px;
  left: 20px;
}

.feng-xiong .mouth {
    border-radius: 0;
}

.tu-ge .mouth.open {
    width: 25px;
    height: 15px;
    bottom: 10px;
    left: 18px;
    background: #903030;
    border-radius: 50%;
    animation: sing 0.5s infinite alternate;
}

@keyframes sing {
    from { transform: scaleY(0.5); }
    to { transform: scaleY(1); }
}


.body {
  width: 70px;
  height: 100px;
  background: #89CFF0;
  position: relative;
  top: -10px;
  left: -5px;
  border-radius: 20px 20px 0 0;
  border: 2px solid #555;
}

.tu-ge .body.singing {
    animation: dance 0.5s infinite alternate;
}

@keyframes dance {
    from { transform: skewX(-5deg); }
    to { transform: skewX(5deg); }
}


.speech-bubble {
  position: absolute;
  top: -30px;
  left: 60px;
  background: white;
  padding: 5px 10px;
  border-radius: 10px;
  border: 1px solid #ccc;
  font-size: 14px;
}

.music-note {
    position: absolute;
    top: -20px;
    right: -40px;
    font-size: 20px;
    color: #ff4500;
    animation: musicFloat 1s infinite alternate;
}

@keyframes musicFloat {
    from { transform: translateY(0) rotate(-5deg); }
    to { transform: translateY(-5px) rotate(5deg); }
}

.crowd {
  position: absolute;
  bottom: -50px;
  width: 400px;
  display: flex;
  justify-content: center;
}

.person {
  width: 20px;
  height: 40px;
  background: #666;
  border-radius: 10px 10px 0 0;
  margin: 0 5px;
}
.flag {
  width: 15px;
  height: 10px;
  background: #ff4500;
  position: relative;
  left: 18px;
  animation: wave 0.3s infinite alternate;
}

@keyframes wave {
    from { transform: skewY(-10deg); }
    to { transform: skewY(10deg); }
}


.ai-screen {
  position: absolute;
  top: 20%;
  right: 5%;
  width: 200px;
  height: 120px;
  background: rgba(0, 0, 0, 0.7);
  border: 2px solid #0f0;
  color: #0f0;
  border-radius: 10px;
  padding: 10px;
  animation: screen-flicker 0.1s infinite;
  z-index: 20;
}

@keyframes screen-flicker {
  from { opacity: 1; }
  to { opacity: 0.95; }
}

.progress-bar {
    width: 100%;
    height: 10px;
    background: #333;
    border: 1px solid #0f0;
    margin-top: 10px;
    overflow: hidden;
}

.progress-bar::after {
    content: '';
    display: block;
    width: 75%;
    height: 100%;
    background: #0f0;
    animation: load 2s 1s forwards;
    transform: translateX(-100%);
}

@keyframes load {
    to { transform: translateX(0); }
}

.final-text {
  position: absolute;
  bottom: 5%;
  width: 100%;
  text-align: center;
  font-size: 3em;
  font-weight: bold;
  color: white;
  text-shadow: 2px 2px 5px black;
  z-index: 30;
  opacity: 0;
  transform: scale(1.5);
  animation: fadeInText 2s 3s forwards;
}

@keyframes fadeInText {
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.ballots {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 25;
    pointer-events: none;
}
.ballot {
    position: absolute;
    width: 20px;
    height: 15px;
    background: white;
    border: 1px solid #ccc;
    animation: fall linear infinite;
}

@keyframes fall {
    to {
        transform: translateY(100vh) rotate(720deg);
        opacity: 0;
    }
}

</style>
