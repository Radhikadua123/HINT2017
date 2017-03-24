<!DOCTYPE html>
<html>
<head>
	<title></title>
	<script>
		function sun(){
			var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
			recognition.lang = 'en-US';
			recognition.interimResults = false;
			recognition.maxAlternatives = 5;
			recognition.start();

			recognition.onresult = function(event) {
			    console.log('You said: ', event.results[0][0].transcript);
			};
		}

		function isko_bolo(line){
			var msg = new SpeechSynthesisUtterance(line);
			window.speechSynthesis.speak(msg);
		}
		
	</script>
</head>
<body>
	<button onclick="sun()">Bolo</button>
	
</body>
</html>

