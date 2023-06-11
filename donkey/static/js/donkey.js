var utterance = new SpeechSynthesisUtterance();
var currentSpeakingButton = null;

// TTS로 텍스트 읽기 함수
function speakText(text) {
    stopSpeaking();
    utterance.text = text;
    window.speechSynthesis.speak(utterance);
    currentSpeakingButton = event.target;
}

// TTS 중지 함수
function stopSpeaking() {
    if (currentSpeakingButton !== null) {
        window.speechSynthesis.cancel();
        currentSpeakingButton = null;
    }
}

// Tabs 실행 함수
const category_1 = document.getElementById('category_1');
const category_2 = document.getElementById('category_2');
const category_3 = document.getElementById('category_3');

function moveInTabs(evt, tabName) {
    var i, tabcontent, tablinks;
// 해당 탭 제외 가리기
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // tab이름 위 파일 형식 만들기
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        if (evt.target == tablinks[i]) {
            tablinks[i].style.borderBottom = 'none';
            // console.log(evt.target, 'cur')
        } else {
            // console.log(evt.target)
            tablinks[i].style.borderBottom = '3px solid #000';
        }

    }
// 해당 탭 보여주기
    document.getElementById(tabName).style.display = "block";
}

document.getElementById("defaultOpen").click();