
// var swiper = new Swiper(".mySwiper", {
//     slidesPerView: 3,
//     spaceBetween: 30,
//     slidesPerGroup: 3,
//     loop: true,
//     loopFillGroupWithBlank: true,
//     pagination: {
//       el: ".swiper-pagination",
//       clickable: true,
//     },
//     navigation: {
//       nextEl: ".swiper-button-next",
//       prevEl: ".swiper-button-prev",
//     },
//   });


//   let noOfChar = 20;
//   let contents = document.querySelectorAll(".content");
//   contents.forEach(content =>{

//     if (content.textContent.length < noOfChar){
//       content.nextElementSibling.style.display = "none";
//     }
//     else{
//       let displayText = content.textContent.slice
//       (0,noOfChar);
//       let moreText = content.textContent.slice(noOfChar);
//       content.innerHTML = '${displayText}<span class="dots">...</span><span class="hidemore">${moreText}</span>'
//     }
//   })

//   function readMore(btn){


//     let post = btn.parentElement;
//     post.querySelector(".dots").classList.toggle
//     ("hide");
//     post.querySelector(".more").classList.toggle("hide");

//     btn.textContent == "Read More" ? btn.textContent = " Read Less" : btn.textContent = " Read More" ;
//   }
