const lightbox = GLightbox({
  preload: true,
  openEffect: "fade",
  touchNavigation: true,
  loop: true
});

var grid = document.querySelector('.img-gallery');
imagesLoaded(grid, function() {
  var msnry = new Masonry(grid, {
    itemSelector: '.glightbox',
    columnWidth: 300,
    gutter: 10
  });
});
