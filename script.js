 // Ambil elemen anchor dengan ID yang sesuai
    var antv = document.getElementById("antv");
    var indosiar = document.getElementById("indosiar");
    var mnctv = document.getElementById("mnctv");
    var sctv = document.getElementById("sctv");

    // Tambahkan event listener untuk mengatur href ketika anchor diklik
    antv.addEventListener("click", function(event) {
      event.preventDefault(); // Mencegah perilaku default tautan
      window.location.href = "intent://cdnjkt2.transvision.co.id:1001/live/master/4/4028c6856c3db2cc016cd6e9c5992395/manifest.mpd|drmScheme=widevine&drmLicense=https://gausahcopybesokilang.satvb.workers.dev/#Intent;scheme=https;type=video/*;package=com.genuine.leone;S.browser_fallback_url=market://details?id=com.genuine.leone.ad;S.title=ANTV;end";
    });

    indosiar.addEventListener("click", function(event) {
      event.preventDefault(); // Mencegah perilaku default tautan
      window.location.href = "intent://cdnjkt2.transvision.co.id:1001/live/master/1/4028c6856c3db2cc016cd6e773b02392/manifest.mpd|drmScheme=widevine&drmLicense=https://gausahcopybesokilang.satvb.workers.dev/#Intent;scheme=https;type=video/*;package=com.genuine.leone;S.browser_fallback_url=market://details?id=com.genuine.leone.ad;S.title=INDOSIAR;end";
    });

     mnctv.addEventListener("click", function(event) {
      event.preventDefault(); // Mencegah perilaku default tautan
      window.location.href = "intent://cdnjkt2.transvision.co.id:1001/live/master/1/4028c6856c3db2cc016cd6ebd82f2396/manifest.mpd|drmScheme=widevine&drmLicense=https://gausahcopybesokilang.satvb.workers.dev/#Intent;scheme=https;type=video/*;package=com.genuine.leone;S.browser_fallback_url=market://details?id=com.genuine.leone.ad;S.title=MNC TV;end";
    });

    sctv.addEventListener("click", function(event) {
      event.preventDefault(); // Mencegah perilaku default tautan
      window.location.href = "intent://cdnjkt2.transvision.co.id:1001/live/master/5/4028c6856c3db2cc016cd6e647532391/manifest.mpd|drmScheme=widevine&drmLicense=https://gausahcopybesokilang.satvb.workers.dev/#Intent;scheme=https;type=video/*;package=com.genuine.leone;S.browser_fallback_url=market://details?id=com.genuine.leone.ad;S.title=SCTV;end";
    });
