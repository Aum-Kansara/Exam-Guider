const chapters_container=document.querySelector('.selected_chapters');
const weights_container=document.querySelector('.add_weights');
const chapters_selection=document.querySelector('.ChapterSelection');
const chapters_txt=document.querySelector('.chapters_txt');
const weights_txt=document.querySelector('.weights_txt');
var submit_btn=document.querySelector('#submitBtn');
var isNoChapters=true;
var no_of_chapters=0;

function applyWeights(){
    alert("Not Implemented Yet");
}

function calculate_weight(){
    return Math.round(100/no_of_chapters);
}

function addSelectedChapter(chapter_no){
    no_of_chapters+=1;
    const chapter_card=document.createElement('div');
    chapter_card.classList='chapter_card'
    
    chapter_card.innerHTML=`Chapter ${chapter_no}`
    
    chapters_container.appendChild(chapter_card)
}

function removeChapterFromList(chapter_no){
    var temp=document.getElementById(chapter_no);
    chapters_selection.removeChild(temp);
}

function selectAllChapters(){
    for(var i=1;i<6;i++){
        addSelectedChapter(i);
        if(isNoChapters){
            isNoChapters=false;
            chapters_container.removeChild(document.querySelector('.chp-txt'));
        }
        chapters_txt.innerHTML=i;
        chapters_txt.value+=' '+i;
        removeChapterFromList(i);
        chapters_selection.selectedIndex=0;
    }
}

chapters_selection.addEventListener("change",function(){
    addSelectedChapter(chapters_selection.value);
    if(isNoChapters){
        isNoChapters=false;
        chapters_container.removeChild(document.querySelector('.chp-txt'));
    }
    chapters_txt.innerHTML=chapters_selection.value;
    chapters_txt.value+=' '+chapters_selection.value;
    removeChapterFromList(chapters_selection.value);
    chapters_selection.selectedIndex=0;
})


