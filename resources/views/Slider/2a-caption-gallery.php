<!DOCTYPE html>
<html>
  <head>
    <title>Very Simple PHP gallery</title>
    <meta charset="utf-8">

    <!-- (A) CSS & JS -->
    <link href="2b-caption-gallery.css" rel="stylesheet">
    <script src="1c-gallery.js"></script>
  </head>
  <body>
    <div class="gallery"><?php
      // (B) GET IMAGES IN GALLERY FOLDER
      $dir = __DIR__ . DIRECTORY_SEPARATOR . "gallery" . DIRECTORY_SEPARATOR;
      $images = glob("$dir*.{jpg,jpeg,gif,png,bmp,webp}", GLOB_BRACE);

      // (C) OUTPUT IMAGES
      foreach ($images as $i) {
        $img = basename($i);
        $caption = substr($img, 0, strrpos($img, "."));
        printf("<figure><img src='gallery/%s'><figcaption>%s</figcaption></figure>", 
          rawurlencode($img), $caption
        );
      }
    ?></div>
  </body>
</html>