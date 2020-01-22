$(function() {
  // Owl Carousel
  var owl = $(".owl-carousel");
  owl.owlCarousel({
    responsive: {
      0: {
        items: 1
      },
      768: {
        items: 2
      },
      1180: {
        items: 3
      }
    },
    items: 1,
    loop: true,
    nav: true,
    autoplay: true,
    autoplayTimeout: 2000,
    smartSpeed: 1000,
    animateOut: "slideOutDown",
    animateIn: "slideInDown",
  });
});