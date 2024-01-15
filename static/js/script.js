/*jshint esversion: 6 */
$(".autoplay").slick({
  arrows: false,
  slidesToShow: 4,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2500,
  pauseOnHover: true,
  infinite: true,
  adaptiveWidth: true,
  variableWidth: false,
  responsive: [
    {
      breakpoint: 993,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2

      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 476,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

$('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  fade: true,
  arrows: true,
  appendArrows: $('.arrow-sert'),
  prevArrow: '<button id="prev" type="button" class="btn shadow-none"><i class="fa fa-chevron-left" aria-hidden="true"></i> <svg class="project__arrow project__arrow--back" width="31" height="8" viewBox="0 0 31 8"fill="none" xmlns="http://www.w3.org/2000/svg" ><path d="M30.3536 4.35355C30.5488 4.15829 30.5488 3.84171 30.3536 3.64645L27.1716 0.464466C26.9763 0.269204 26.6597 0.269204 26.4645 0.464466C26.2692 0.659728 26.2692 0.976311 26.4645 1.17157L29.2929 4L26.4645 6.82843C26.2692 7.02369 26.2692 7.34027 26.4645 7.53553C26.6597 7.7308 26.9763 7.7308 27.1716 7.53553L30.3536 4.35355ZM0 4.5H30V3.5H0V4.5Z"fill="#0F57C9"></path></svg></button > ',
  nextArrow: '<button id="next" type="button" class="btn shadow-none"><i class="fa fa-chevron-right" aria-hidden="true"></i><svg class= "project__arrow project__arrow--next" width="31" height="8" viewBox="0 0 31 8" fill="none" xmlns="http://www.w3.org/2000/svg" ><path d="M30.3536 4.35355C30.5488 4.15829 30.5488 3.84171 30.3536 3.64645L27.1716 0.464466C26.9763 0.269204 26.6597 0.269204 26.4645 0.464466C26.2692 0.659728 26.2692 0.976311 26.4645 1.17157L29.2929 4L26.4645 6.82843C26.2692 7.02369 26.2692 7.34027 26.4645 7.53553C26.6597 7.7308 26.9763 7.7308 27.1716 7.53553L30.3536 4.35355ZM0 4.5H30V3.5H0V4.5Z"fill="#0F57C9"></path></svg></button > ',
  asNavFor: '.slider-nav'

});
$('.slider-nav').slick({

  slidesToShow: 4,
  slidesToScroll: 1,
  asNavFor: '.slider-for',
  arrows: false,
  centerMode: true,
  focusOnSelect: true

});

$('.sertificate-slider').slick({
  infinite: true,
  dots: false,
  slidesToShow: 3,
  slidesToScroll: 3,
  autoplay: true,
  speed: 1000,
  autoplay: 3000,
  appendArrows: $('.arrow-sert'),
  prevArrow: '<button id="prev" type="button" class="btn btn-outline-primary btn col-2"><i class="fa fa-chevron-left" aria-hidden="true"></i> <svg class="project__arrow project__arrow--back" width="31" height="8" viewBox="0 0 31 8"fill="none" xmlns="http://www.w3.org/2000/svg" ><path d="M30.3536 4.35355C30.5488 4.15829 30.5488 3.84171 30.3536 3.64645L27.1716 0.464466C26.9763 0.269204 26.6597 0.269204 26.4645 0.464466C26.2692 0.659728 26.2692 0.976311 26.4645 1.17157L29.2929 4L26.4645 6.82843C26.2692 7.02369 26.2692 7.34027 26.4645 7.53553C26.6597 7.7308 26.9763 7.7308 27.1716 7.53553L30.3536 4.35355ZM0 4.5H30V3.5H0V4.5Z"fill="#0F57C9"></path></svg></button > ',
  nextArrow: '<button id="next" type="button" class="btn btn-outline-primary btn col-2"><i class="fa fa-chevron-right" aria-hidden="true"></i><svg class= "project__arrow project__arrow--next" width="31" height="8" viewBox="0 0 31 8" fill="none" xmlns="http://www.w3.org/2000/svg" ><path d="M30.3536 4.35355C30.5488 4.15829 30.5488 3.84171 30.3536 3.64645L27.1716 0.464466C26.9763 0.269204 26.6597 0.269204 26.4645 0.464466C26.2692 0.659728 26.2692 0.976311 26.4645 1.17157L29.2929 4L26.4645 6.82843C26.2692 7.02369 26.2692 7.34027 26.4645 7.53553C26.6597 7.7308 26.9763 7.7308 27.1716 7.53553L30.3536 4.35355ZM0 4.5H30V3.5H0V4.5Z"fill="#0F57C9"></path></svg></button > ',
  responsive: [
    {
      breakpoint: 993,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2

      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 475,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});



