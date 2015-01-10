var scrollInSeconds = 10;    //set the scrolling time in seconds

var myPhoto = document.getElementById("mainImage");

var photoArray = ["photos/LaylaBeach.jpg","photos/CrazyGoggles.jpg","photos/MaryAnneDickJohn.jpg"];

var photoIndex = 0;

var changePhoto = function(){
    myPhoto.setAttribute("src",photoArray[photoIndex]);
    photoIndex++;
    if (photoIndex >= photoArray.length){
        photoIndex = 0;
    }
}

setInterval(changePhoto,scrollInSeconds*1000);