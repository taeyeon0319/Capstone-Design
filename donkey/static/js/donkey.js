// TTS로 텍스트 읽기 함수
function speakText(text) {
    var utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
}

const category_1 = document.getElementById('category_1');
const category_2 = document.getElementById('category_2');
const category_3 = document.getElementById('category_3');

function moveInTabs(evt,tabName) {
    var i,tabcontent,tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for(i=0;i<tabcontent.length; i++) {
        tabcontent[i].style.display="none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        if(evt.target == tablinks[i]){
            tablinks[i].style.borderBottom = 'none';
            // console.log(evt.target, 'cur')
        } else {
            // console.log(evt.target)
            tablinks[i].style.borderBottom = '3px solid #000';
        }

    }

    document.getElementById(tabName).style.display = "block";}
document.getElementById("defaultOpen").click();