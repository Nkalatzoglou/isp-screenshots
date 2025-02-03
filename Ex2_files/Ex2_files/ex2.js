let audioContext;
let audioSource;
let analyzer;

function preload() {
  sound1 = loadSound('C:\Users\user\Desktop\INTELIGENT SIGNAL\Ex2_files\Ex2_sound1.wav');
  sound1 = loadSound('C:\Users\user\Desktop\INTELIGENT SIGNAL\Ex2_files\Ex2_sound2.wav');
  sound1 = loadSound('C:\Users\user\Desktop\INTELIGENT SIGNAL\Ex2_files\Ex2_sound3.wav');
}

function setup() {
  createCanvas(400, 400);
  audioContext = getAudioContext();

  // Use one of the sounds or implement a way to switch between them
  audioSource = sound1;

  analyzer = Meyda.createMeydaAnalyzer({
    "audioContext": audioContext,
    "source": audioSource,
    "bufferSize": 512,
    "featureExtractors": [
      "spectralCentroid",
      "rms",
      "spectralFlux",
      "mfcc",
      "energy"
    ],
    "callback": features => {
      // Do something with the features
      visualize(features);
    }
  });

  audioSource.loop();
}

function draw() {
  background(0);
  // Visualization code goes here
}

function visualize(features) {
  // Example: Use the RMS feature to draw a circle that changes size
  let size = map(features.rms, 0, 1, 0, width);
  ellipse(width / 2, height / 2, size, size);
}

// Call this function to start feature extraction
function toggleAudio() {
  if (getAudioContext().state !== 'running') {
    getAudioContext().resume();
  }
  analyzer.start();
}

function mouseClicked() {
  toggleAudio();
}
